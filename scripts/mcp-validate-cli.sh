#!/usr/bin/env bash
#
# MCP Validator CLI - thin wrapper around mcp-validator.py
#
# Kept for backwards compatibility with the original CLI contract:
#     ./scripts/mcp-validate-cli.sh [--validate] <.mcp.json> [--strict] [-o report.json]
#
# The original bash implementation was broken (unterminated quotes, undefined
# variables, dead loops). All validation logic now lives in the Python
# validator so there is a single source of truth.
#
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VALIDATOR="${SCRIPT_DIR}/mcp-validator.py"

PY=""
if command -v python3 >/dev/null 2>&1; then
  PY="python3"
elif command -v python >/dev/null 2>&1; then
  PY="python"
elif command -v py >/dev/null 2>&1; then
  PY="py -3"
else
  echo "[ERROR] No Python interpreter found (python3/python/py)." >&2
  exit 2
fi

forwarded=()
for arg in "$@"; do
  case "$arg" in
    --validate|--dry-run|--no-color) ;;   # accepted, no-op
    *) forwarded+=("$arg") ;;
  esac
done

if [[ ${#forwarded[@]} -eq 0 ]]; then
  forwarded=(".mcp.json")
fi

# shellcheck disable=SC2086
exec $PY "$VALIDATOR" "${forwarded[@]}"
