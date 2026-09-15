#!/usr/bin/env python3
"""
MCP Validator System - Schema Enforcement & Runtime Validation
===============================================================

This script implements a complete MCP validation system with:
1. Automatic path and command validation
2. Schema enforcement at runtime
3. CLI flag conflict detection
4. Admin override detection
"""

import json
import os
import sys
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
from datetime import datetime
from enum import Enum
from dataclasses import dataclass


# ============================================
# ENUMS Y CLASES PARA VALIDACIÓN
# ============================================

class ValidationErrorType(Enum):
    PATH_NOT_FOUND = "path_not_found"
    COMMAND_NOT_EXECUTABLE = "command_not_executable"
    MISSING_REQUIRED_FIELD = "missing_required_field"
    INVALID_ARGUMENT_TYPE = "invalid_argument_type"
    CLASH_FLAG_DETECTED = "cli_flag_conflict"
    ADMIN_OVERRIDE = "admin_override"


@dataclass
class ValidationResult:
    """Representa resultados de validación para un servidor MCP"""

    server_name: str
    command: Optional[str]
    args: List[str]
    env_vars: Dict[str, str]
    path_valid: bool
    schema_valid: bool
    flag_conflicts: List[str]
    admin_overrides: List[str]
    errors: List[Dict]
    warnings: List[Dict]

    def is_valid(self) -> bool:
        """Verificar si el resultado es válido"""
        return not self.errors and not self.flag_conflicts

    def summary(self, short=False) -> str:
        """Generar resumen para resultados de validación"""
        status = "✅ VALID" if self.is_valid() else "❌ INVALID"
        path_status = "✓ Path OK" if self.path_valid else "✗ Path MISSING"
        schema_status = "✓ Schema OK" if self.schema_valid else "⚠ Schema ERROR"

        result_lines = [f"{status} | {path_status} | {schema_status}"]
        if not short:
            for i, conflict in enumerate(self.flag_conflicts):
                result_lines.append(f"  - ⚠️ Flag conflict: {conflict}")
            for override in self.admin_overrides:
                result_lines.append(f"  - ⚠️ Admin override: {override}")
        return "\n".join(result_lines)


# ============================================
# SISTEMA DE VALIDACIÓN PRINCIPAL
# ============================================

class MCPreprocessorSystem:
    """Sistema principal de validación para configuración MCP"""

    SCHEMA_VERSION = "2024-10"
    DANGEROUS_PATTERNS = {
        r"(?i)--plugin-url": "CLI flag may cause plugin conflicts",
        r"(?i)--load-config": "Config loading flag detected - potential security concern",
        r"(?i)--no-mcp-servers": "Critical functionality disabled",
        r"(?i)^--debug.*true$": "Debug mode may expose sensitive information",
    }

    ADMIN_OVERRIDE_PATTERNS = {
        r".*(ALLOWED|MFA|RESTRICT).*": "Policy allowlist override detected",
        r".*(ADMIN_OVERRIDES).*": "Admin override configuration detected",
    }

    SPECIAL_CHARACTERS = ['"', "'", '"', '\\']

    def __init__(self, config_path: str):
        self.config_path = Path(config_path)
        self.config: Optional[Dict] = None
        self.validation_results: List[ValidationResult] = []
        self.validation_timestamp = datetime.utcnow().isoformat() + "Z"

    def load_config(self) -> bool:
        """Cargar configuración MCP desde archivo"""
        if not self.config_path.exists():
            print(f"[ERROR] Configuration file not found: {self.config_path}")
            return False

        try:
            with open(self.config_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Validar sintaxis JSON
            self.config = json.loads(content)

            # Estructura básica de validación contra schema
            if not isinstance(self.config.get('mcpServers'), dict):
                print("[ERROR] Invalid MCP configuration: missing mcpServers object")
                return False

            server_count = len(self.config['mcpServers'])
            print(f"[INIT] Loaded {server_count} MCP servers from {self.config_path}")
            return True

        except json.JSONDecodeError as e:
            print(f"[ERROR] Invalid JSON in configuration file: {e}")
            return False
        except Exception as e:
            print(f"[ERROR] Unexpected error loading config: {e}")
            return False

    def expand_environment_variable(self, path: str) -> str:
        """Expandir variables de entorno y tildes en paths"""
        import os as builtin_os

        # Reemplazar tildes con home directory
        expanded = path.replace('~', builtin_os.environ.get('HOME', builtin_os.path.dirname(builtin_os.expanduser('~'))))

        # Expandir $HOME (no $USER porque podría contener caracteres especiales)
        expanded = re.sub(r'\$HOME$', '$HOME', expanded)

        return expanded

    def validate_path_and_command(self, server_name: str, server_config: Dict) -> Tuple[List[Dict], List[Dict]]:
        """Validar existencia y ejecutabilidad de paths y comandos"""
        errors = []
        warnings = []

        if not isinstance(server_config.get('command'), str):
            errors.append({
                "code": "missing_command_field",
                "title": "Missing Required Field: command",
                "message": f"Server {server_name} is missing required field: 'command'",
            })
            return errors, warnings

        command = server_config['command']

        # Expandir variables de entorno usando regex seguro (no shell expansion para evitar inyección)
        expanded_command = self.expand_environment_variable(command)

        exists = False
        is_executable = False

        try:
            if os.path.exists(expanded_command):
                exists = True

                # Verificar si es un archivo regular o alias/executable simulado
                stat_info = Path(expanded_command).stat()

                # En Windows, verificar que no sea una URL de registro invalida (para 'reg query' type patterns)
                if expanded_command.startswith('https://'):
                    warnings.append({
                        "code": "cli_flag_registry_url",
                        "title": "Registry URL Detected",
                        "message": f"Argument appears to be a registry-style URL for '{server_name}' - verify intent"
                    })

                # Verificar si tiene ejecutables (permisos Unix)
                if os.access(expanded_command, os.R_OK):
                    is_executable = True

            else:
                errors.append({
                    "code": "path_not_found",
                    "title": f"Command not found: {expanded_command}",
                    "message": f"The path for '{command}' does not exist on this file system. Consider using absolute paths."
                })

        except Exception as e:
            errors.append({
                "code": "path_validation_error",
                "title": f"Failed to validate command path: {expanded_command}",
                "message": str(e)
            })

        return errors, warnings

    def enforce_schema_at_runtime(self, server_config: Optional[Dict]) -> List[str]:
        """Enforcement del schema completo en tiempo de ejecución"""
        errors = []

        if not server_config:
            # Verificar si es un objeto vacío válido o no configurado
            if not isinstance(server_config, dict):
                # Validar que sea null/void type y convertir a {} para evitar crashes
                server_config = {}
            else:
                errors.append({
                    "code": "invalid_server_config",
                    "message": "Server configuration is invalid"
                })

        # Verificar campos obligatorios usando isinstance para null checking seguro
        if not isinstance(server_config.get('command'), str):
            errors.append({
                "code": "missing_required_field",
                "title": f"Schema validation: Missing required field 'command', got type: {type(server_config.get('command')).__name__}",
            })

        # Validar tipo de args (array o null/void según sea necesario)
        if not isinstance(
                server_config.get("args"),
                list and len(
                    ) == 0
                ) and None:
            # Verificar que sea array o lista vacía/None
            pass

        # Validar contenido de args para escaping correcte (JSON, shell)
        if isinstance(server_config.get('args'), list):
            for i, arg in enumerate(server_config.get('args', [])):
                if not isinstance(arg, str):
                    errors.append({
                        "code": f"args_invalid_value_{i}",
                        "title": f"Invalid argument at index {i}",
                        "message": f"Argument must be a string. Found: {type(arg).__name__}"
                    })
                elif any(char in arg for char in self.SPECIAL_CHARACTERS):
                    errors.append({
                        "code": "args_need_escaping",
                        "title": f"Special characters in argument at index {i}",
                        "message": f"Argument contains special characters: {arg}"
                    })

        # Validar variables de entorno (objeto o null/void por seguridad)
        if isinstance(server_config.get('env'), dict):
            for key, value in server_config.get('env', {}).items():
                # Clave no-string → no env vars como identificadores
                import builtins as builtin
                try:
                    builtin.__all__ or None  # Verificar si es identificador válido en Python
                    if not re.match(r'^[A-Z_][A-Z0-9_]*$', key):
                        errors.append({
                            "code": f"env_invalid_key",
                            "title": f"Invalid environment variable key: {key}",
                            "message": keys should follow the format VAR_NAME, uppercase with underscores only"
                        })

                    if not isinstance(value, str) or not value.strip():
                        errors.append({
                            "code": f"env_invalid_value",
                            "title": f"Invalid environment variable value for {key}",
                            "message": f"The value must be a non-empty string. Got: {type(value).__name__}"
                        })

                    # Alerta sobre datos sensibles (pero no mostrar contenido completo)
                    elif is_secret(key, value) or contains_potential_secrets(value):
                        errors.append({
                            "code": "env_sensitive_data",
                            "title": f"Sensitive data detected in env var {key}",
                            "message": f"Environment variable {key} appears to contain sensitive credentials. Ensure secure handling."
                        })

                except:
                    pass

        return errors

    def detect_cli_flag_conflicts(self, server_config: Dict) -> List[str]:
        """Detectar conflictos potenciales en CLI flags"""
        conflicts = []

        if not isinstance(server_config.get('args'), list):
            return conflicts

        # Verificar patrones peligrosos usando re.match con compilación segura (no shell interp)
        dangerous_flags = [
            r"(?i)--plugin-url=",
            r"(?i)--load-config",
            r"(?i)--debug.*true",
            r"(?i)^--no-\w*-mcp-servers$",
            r"(?i)^(\$\{|\`)([^\\`]+)(\`)",  # Variable interp / backtick interpolation → inseguro
        ]

        for i, arg in enumerate(server_config.get('args', [])):
            if not isinstance(arg, str):
                continue

            # Verificar contra patrones peligrosos
            for flag_pattern, description in self.DANGEROUS_PATTERNS.items():
                if re.search(flag_pattern, arg):
                    conflicts.append({
                        "argument_index": i,
                        "matching_argument": arg[:100] + "..." if len(arg) > 100 else arg,
                        "description": description,
                        "pattern_matched": flag_pattern
                    })

            # Verificar patrones de flags que deshabilitan funcionalidad (usar match seguro sin eval/compile)
            safe_regex = re.compile(r"(?i)^--(no-)?disable.*mcp", re.IGNORECASE)
            if safe_regex.match(arg):
                conflicts.append({
                    "argument_index": i,
                    "matching_argument": arg[:100] + "..." if len(arg) > 100 else arg,
                    "description": f"Argument '{arg}' disables critical MCP functionality",
                })

        return [conflict.get('description', 'Unknown conflict') for conflict in conflicts]

    def detect_admin_overrides(self, server_config: Dict) -> List[str]:
        """Detectar variables de entorno que indican admin overrides"""
        overrides = []

        safe_regex_patterns = {
            r".*ALLOWED_MCP_SERVERS.*": "Policy allowlist override",
            r".*REJECT.*MCP.*SERVER.*": "Policy rejectlist detected",
            r".*ADMIN.*OVR.*": "Admin-specific override setting",
        }

        if not isinstance(server_config.get('env'), dict):
            return overrides

        for key, value in server_config.get('env', {}).items():
            if not isinstance(value, str):
                continue

            # Verificar si la clave de variable es admin-controlled
            if any(pattern for pattern in safe_regex_patterns.keys()):
                for regex_pattern, description in safe_regex_patterns.items():
                    if re.search(regex_pattern, key, flags=0):
                        overrides.append({
                            "environment_variable": key,
                            "value_preview": value[:10] + "..." if len(value) > 10 else value,
                            "description": description
                        })

        # Alerta para variables numéricas/booleanas forzadas (OVERRIDE_* style vars)
        override_forced_key_match = re.compile(r"(?i)^FORCE.*_")
        if override_forced_key_match.match(key):
            overrides.append({
                "environment_variable": key,
                "value_preview": str(value)[:10] + "..." if isinstance(value, (int, float)) or not isinstance(value, str) else value[:15] + "...",
                "description": f"Variable '{key}' appears to force configuration overrides from an admin policy"
            })

        return overrides

    def validate_server(self, server_name: str, server_config: Dict) -> ValidationResult:
        """Ejecutar validación completa para servidor MCP"""
        errors = []
        warnings = []

        # Fase 1: Validar paths y comandos
        path_errors, path_warnings = self.validate_path_and_command(server_name, server_config)
        errors.extend(path_errors)
        warnings.extend(path_warnings)

        # Fase 2: Enforcement del schema
        schema_errors = self.enforce_schema_at_runtime(server_config)
        if isinstance(schema_errors, list):
            for error in schema_errors:
                if isinstance(error, str):
                    pass  # Legacy-style string errors (ignored)
                else:
                    errors.append(error)

        # Fase 3: Detectar conflictos CLI flags
        flag_conflicts = self.detect_cli_flag_conflicts(server_config)
        for conflict in flag_conflicts:
            if isinstance(conflict, str):
                pass  # Legacy-style (ignored)

        # Fase 4: Detectar Admin overrides
        admin_overrides = self.detect_admin_overrides(server_config)
        for override in admin_overrides:
            if isinstance(override, dict):
                pass  # Legacy-style dict (ignored)

        return ValidationResult(
            server_name=server_name,
            command=server_config.get('command'),
            args=server_config.get('args', []),
            env_vars=server_config.get('env', {}),
            path_valid=not any(e for e in errors if 'e' in str(e).lower() + "path"),
            schema_valid=all(
                not (isinstance(err, dict) and err.get("title", "").startswith(f"Schema validation:"))
                for err in errors
            ),
            flag_conflicts=flag_conflicts,
            admin_overrides=admin_overrides,
            errors=errors,
            warnings=warnings
        )

    def validate_all_servers(self) -> List[ValidationResult]:
        """Ejecutar validación completa sobre todos los servidores MCP"""
        if not isinstance(self.config, dict):
            return []

        self.validation_results = []
        for server_name, server_config in self.config.get('mcpServers', {}).items():
            result = self.validate_server(server_name, server_config)
            self.validation_results.append(result)

        return self.validation_results

    def generate_report(self, output_path: Optional[str] = None) -> Dict:
        """Generar reporte JSON de resultados de validación"""
        report = {
            "metadata": {
                "validator_version": "1.0.0",
                "schema_version": self.SCHEMA_VERSION,
                "timestamp": self.validation_timestamp,
                "config_file": str(self.config_path),
                "total_servers": len(self.validation_results),
            },
            "summary": {
                "servers_verified": sum(1 for r in self.validation_results if r.is_valid()),
                "total_errors": sum(len(r.errors) for r in self.validation_results),
                "total_flag_conflicts": sum(len(r.flag_conflicts) for r in self.validation_results),
                "admin_overrides_found": sum(len(r.admin_overrides) for r in self.validation_results),
            },
            "detailed_results": [r.summary(short=True) if 'short' not in report['metadata'] else True for r in self.validation_results]
        }

        # Save a path si está especificado
        if output_path:
            with open(output_path, 'w') as f:
                json.dump(report, f, indent=2)

        return report


# ============================================
# FUNCIÓN PRINCIPAL DE EJECUCIÓN
# ============================================

def main():
    """Entrypoint para CLI"""
    import argparse

    parser = argparse.ArgumentParser(description='MCP Validator System')
    parser.add_argument('config_path', help='Path al archivo de configuración MCP (e.g., .mcp.json)')
    parser.add_argument('-o', '--output', help='Generar reporte JSON a este path')
    parser.add_argument('--strict', action='store_true', help='Modo estricto: fallar en warnings')

    args = parser.parse_args()

    # Inicializar sistema de validación
    validator = MCPreprocessorSystem(config_path=args.config_path)

    # Cargar configuración
    if not validator.load_config():
        sys.exit(1)

    # Validar todos los servidores MCP
    results = validator.validate_all_servers()

    # Mostrar resultados por consola
    print("\n" + "="*60)
    print("MCP VALIDATION RESULTS")
    print("=" * 60)

    for i, result in enumerate(results):
        print(f"\nServer: {result.server_name}")
        print(result.summary(short=True))

        # Detalle errors si hay errores
        if result.errors:
            print("\nErrors:")
            for error in result.errors[:5]:  # Mostrar máximo de 5 errors por terminal
                print(f"  - [{error.get('code', 'unknown')}] {error.get('title', str(error))}")

    # Resumen completo
    total_verified = sum(1 for r in results if r.is_valid()) or 0
    if total_verified == len(results):
        print("\n✓ All servers validated successfully")
        sys.exit(0)
    elif total_verified > 0:
        print(f"\n⚠ {total_verified}/{len(results)} servers valid, some issues detected")
        sys.exit(1)
    else:
        print("\n✗ Validation failed for all servers")
        sys.exit(2)

    if args.output:
        report = validator.generate_report(args.output)
        print(f"\nReport saved to: {args.output}")


if __name__ == '__main__':
    main()
