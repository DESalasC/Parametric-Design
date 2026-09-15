#!/usr/bin/env python3
"""
MCP config validator (standalone CLI)
=====================================

Validates a Claude Code / MCP style config file (``.mcp.json``). It does NOT
implement the MCP protocol: it is a lint/validation tool you run on demand.

Checks performed per server entry:
  1. Required fields: ``command`` (string), ``args`` (list of strings).
  2. Command resolution: absolute/relative paths are checked for existence;
     bare names are resolved via ``PATH`` (``shutil.which``).
  3. Dangerous CLI flags inside ``args`` (``--plugin-url``, ``--load-config``,
     ``--no-*-mcp-servers``, ...).
  4. Environment variables: valid key syntax, non-empty string values, and a
     warning when a key looks like it carries a credential.
  5. Admin / policy override detection in ``env`` keys.

The config may contain ``//`` and ``/* */`` comments (JSONC), like the sample
``.mcp.json`` shipped with the project.

Usage:
    python scripts/mcp-validator.py .mcp.json
    python scripts/mcp-validator.py .mcp.json --strict -o report.json

Exit codes:
    0 -> no errors (warnings allowed unless --strict)
    1 -> at least one server has errors
    2 -> config could not be loaded / parsed
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

VALIDATOR_VERSION = "2.0.0"
SCHEMA_VERSION = "2024-10"

# ---------------------------------------------------------------------------
# Patterns
# ---------------------------------------------------------------------------

DANGEROUS_FLAG_PATTERNS: List[Tuple[re.Pattern, str]] = [
    (re.compile(r"--plugin-url", re.I), "CLI flag may cause plugin conflicts"),
    (re.compile(r"--load-config", re.I), "Config loading flag detected - potential security concern"),
    (re.compile(r"--no-.*mcp-servers", re.I), "Flag may disable critical MCP functionality"),
    (re.compile(r"--debug(=\S*)?\b.*true", re.I), "Debug mode may expose sensitive information"),
]

ENV_KEY_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")
SECRET_KEY_RE = re.compile(r"(token|secret|password|passwd|api[_-]?key|bearer|authorization|credential)", re.I)
ADMIN_OVERRIDE_RE = re.compile(r"(ALLOWED_MCP_SERVERS|REJECT.*MCP.*SERVER|^ADMIN_|_OVERRIDE$|^FORCE.*_)", re.I)

PATH_EXT_RE = re.compile(r"\.(exe|py|sh|bat|cmd|ps1|js|mjs|cjs)$", re.I)

PATH_LIKE_CHARS = ("/", "\\")
PATH_LIKE_EXT = PATH_EXT_RE


# ---------------------------------------------------------------------------
# JSONC loader (tolerates // and /* */ comments + BOM)
# ---------------------------------------------------------------------------

def loads_jsonc(text: str) -> Any:
    """Parse JSON that may contain // and /* */ comments."""
    text = text.lstrip("\ufeff")
    out: List[str] = []
    i, n = 0, len(text)
    in_str = False
    esc = False
    while i < n:
        c = text[i]
        if in_str:
            out.append(c)
            if esc:
                esc = False
            elif c == "\\":
                esc = True
            elif c == '"':
                in_str = False
            i += 1
            continue
        if c == '"':
            in_str = True
            out.append(c)
            i += 1
            continue
        if c == "/" and i + 1 < n and text[i + 1] == "/":
            i += 2
            while i < n and text[i] not in "\r\n":
                i += 1
            continue
        if c == "/" and i + 1 < n and text[i + 1] == "*":
            i += 2
            while i + 1 < n and not (text[i] == "*" and text[i + 1] == "/"):
                i += 1
            i += 2
            continue
        out.append(c)
        i += 1
    return json.loads("".join(out))


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def resolve_command(command: str) -> Tuple[str, Optional[str]]:
    """Resolve a command string.

    Returns (kind, resolved) where kind is ``"path"`` or ``"which"`` and
    ``resolved`` is the resolved absolute path or ``None`` when not found.
    """
    expanded = os.path.expanduser(command)
    looks_like_path = (
        any(sep in command for sep in PATH_LIKE_CHARS)
        or PATH_LIKE_EXT.search(command) is not None
        or command.startswith("~")
    )
    if looks_like_path:
        p = Path(expanded)
        return "path", (str(p) if p.exists() else None)
    found = shutil.which(command)
    return "which", found


def _err(code: str, title: str, message: str = "") -> Dict[str, str]:
    return {"code": code, "title": title, "message": message}


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

def validate_server(name: str, cfg: Any) -> Tuple[List[Dict[str, str]], List[Dict[str, str]]]:
    errors: List[Dict[str, str]] = []
    warnings: List[Dict[str, str]] = []

    if not isinstance(cfg, dict):
        errors.append(_err(
            "invalid_server_config",
            f"Server '{name}' configuration is not an object",
            f"got {type(cfg).__name__}",
        ))
        return errors, warnings

    # --- command -----------------------------------------------------------
    command = cfg.get("command")
    if not isinstance(command, str) or not command.strip():
        errors.append(_err(
            "missing_required_field",
            "Missing required field 'command'",
            f"got {type(command).__name__}",
        ))
    else:
        kind, resolved = resolve_command(command)
        if resolved is None:
            errors.append(_err(
                "command_not_found",
                f"Command not found: {command!r}",
                "not resolvable as a path nor on PATH" if kind == "which" else "path does not exist",
            ))
        elif kind == "path" and os.name != "nt" and not os.access(resolved, os.X_OK):
            warnings.append(_err(
                "command_not_executable",
                f"Command is not executable: {resolved}",
                "missing execute bit",
            ))

    # --- args --------------------------------------------------------------
    args = cfg.get("args")
    if args is None:
        pass
    elif not isinstance(args, list):
        errors.append(_err(
            "invalid_argument_type",
            "'args' must be a list",
            f"got {type(args).__name__}",
        ))
    else:
        for i, arg in enumerate(args):
            if not isinstance(arg, str):
                errors.append(_err(
                    f"args_invalid_value_{i}",
                    f"Argument at index {i} is not a string",
                    f"got {type(arg).__name__}",
                ))
                continue
            for rx, desc in DANGEROUS_FLAG_PATTERNS:
                if rx.search(arg):
                    errors.append(_err(
                        "cli_flag_conflict",
                        f"Dangerous flag in args[{i}]: {arg}",
                        desc,
                    ))

    # --- env ---------------------------------------------------------------
    env = cfg.get("env")
    if env is not None:
        if not isinstance(env, dict):
            errors.append(_err(
                "invalid_env_type",
                "'env' must be an object",
                f"got {type(env).__name__}",
            ))
        else:
            for key, value in env.items():
                skey = str(key)
                if not ENV_KEY_RE.match(skey):
                    errors.append(_err(
                        "env_invalid_key",
                        f"Invalid environment variable key: {skey}",
                        "use VAR_NAME (letters, digits, underscore)",
                    ))
                if not isinstance(value, str) or not value.strip():
                    errors.append(_err(
                        "env_invalid_value",
                        f"Invalid value for environment variable {skey}",
                        f"value must be a non-empty string, got {type(value).__name__}",
                    ))
                elif SECRET_KEY_RE.search(skey):
                    warnings.append(_err(
                        "env_sensitive_data",
                        f"Possible credential in environment variable {skey}",
                        "ensure secure handling",
                    ))
                if ADMIN_OVERRIDE_RE.search(skey):
                    warnings.append(_err(
                        "admin_override",
                        f"Admin/policy override variable detected: {skey}",
                        "verify this override is intentional",
                    ))

    return errors, warnings


def validate_config(config: Any) -> List[Dict[str, Any]]:
    servers = config.get("mcpServers") if isinstance(config, dict) else None
    if not isinstance(servers, dict):
        return []
    results: List[Dict[str, Any]] = []
    for name, cfg in servers.items():
        errors, warnings = validate_server(name, cfg)
        results.append({
            "server": name,
            "errors": errors,
            "warnings": warnings,
            "valid": not errors,
        })
    return results


# ---------------------------------------------------------------------------
# Reporting / CLI
# ---------------------------------------------------------------------------

def build_report(config_path: str, results: List[Dict[str, Any]]) -> Dict[str, Any]:
    return {
        "metadata": {
            "validator_version": VALIDATOR_VERSION,
            "schema_version": SCHEMA_VERSION,
            "config_file": str(config_path),
            "total_servers": len(results),
        },
        "summary": {
            "valid_servers": sum(1 for r in results if r["valid"]),
            "invalid_servers": sum(1 for r in results if not r["valid"]),
            "total_errors": sum(len(r["errors"]) for r in results),
            "total_warnings": sum(len(r["warnings"]) for r in results),
        },
        "results": results,
    }


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="MCP config validator (standalone)")
    parser.add_argument("config_path", help="Path to the MCP config file (e.g. .mcp.json)")
    parser.add_argument("-o", "--output", help="Write a JSON report to this path")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as failures")
    parser.add_argument("--quiet", action="store_true", help="Only print the summary line")
    args = parser.parse_args(argv)

    path = Path(args.config_path)
    if not path.exists():
        print(f"[ERROR] Configuration file not found: {path}")
        return 2
    try:
        config = loads_jsonc(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, ValueError) as exc:
        print(f"[ERROR] Invalid JSON in {path}: {exc}")
        return 2

    if not isinstance(config, dict) or not isinstance(config.get("mcpServers"), dict):
        print("[ERROR] Invalid MCP config: missing 'mcpServers' object")
        return 2

    results = validate_config(config)
    report = build_report(str(path), results)

    total = len(results)
    invalid = report["summary"]["invalid_servers"]
    warnings_total = report["summary"]["total_warnings"]

    if not args.quiet:
        print("=" * 60)
        print("MCP VALIDATION RESULTS")
        print("=" * 60)
        print(f"Config : {path}")
        print(f"Servers: {total}")
        for r in results:
            status = "[ OK ]" if r["valid"] else "[FAIL]"
            print(f"\n{status} {r['server']}")
            for e in r["errors"]:
                print(f"    ERROR   [{e['code']}] {e['title']}")
            for w in r["warnings"]:
                print(f"    WARNING [{w['code']}] {w['title']}")

    print("-" * 60)
    print(f"Summary: {total - invalid}/{total} valid, "
          f"{report['summary']['total_errors']} error(s), {warnings_total} warning(s)")

    if args.output:
        Path(args.output).write_text(json.dumps(report, indent=2), encoding="utf-8")
        print(f"Report saved to: {args.output}")

    if invalid:
        return 1
    if args.strict and warnings_total:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
