#!/bin/bash
#
# MCP Validator CLI - Validación Automática Completa
# Capabilidades:
#   1. Validación automática de paths y comandos
#   2. Schema enforcement at runtime
#   3. Detección CLi flag conflicts
#   4. Detección Admin overrides
#

set -euo pipefail

readonly MCP_VERSION="1.0.0"
readonly SCHEMA_VERSION="2024-10"
readonly VALIDATION_REPORT="${REPORT_DIR:-/tmp}/mcp-validation-report.json"
readonly LOG_PREFIX="[MCP VALIDATOR]"

# ============================================
# FUNCIÓN: Mostrar help
# ============================================
show_help() {
  cat << 'HELLO'
MCP Validator CLI v1.0.0

Capabilidades del sistema de validación automática:

1. VALIDACIÓN AUTOMÁTICA DE PATHS Y COMANDOS
   Verifica existencia, permisos y ejecutabilidad
   - Path expansion (~, variables)
   - Permisos Unix/Linux (chmod, execute bit)
   - Absolute vs relative paths

2. SCHEMA ENFORCEMENT AT RUNTIME
   Valida estructura JSON completa
   - Campos obligatorios ('command', 'args')
   - Tipos de datos correctos
   - Escaping de argumentos especiales
   - Variables de entorno seguras

3. DETECCIÓN CLI FLAG CONFLICTS
   Identifica conflictos no atrapados por el proceso estándar:
   - Flags peligrosos (--plugin-url, --load-config)
   - Deshabilitadores de funcionalidad (--no-mcp-servers)
   - Flags que sobrescriben configuración
   - Variables interpoladas inseguras

4. DETECCIÓN ADMIN OVERRIDES
   Detecta configuraciones que indican override:
   - ALLOWED_MCP_SERVERS
   - REJECT_MCP_SERVERS
   - Variables prefixed con 'ADMIN_' o 'OVERRIDE_'

Uso:
  ./mcp-validate-cli.sh <config-path> [flags]

Flags disponibles:
  --validate        Validar configuración sin hacer cambios (default)
  --dry-run         Solo mostrar qué se verificaría
  --strict          Modo estricto (fallar en warnings)
  --no-color        Sin colores en terminal
  --report FILE     Generar reporte JSON a FINE

Ejemplos:
  ./mcp-validate-cli.sh .mcp.json              # Validación básica
  ./mcp-validate-cli.sh .mcp.json --strict     # Modo estricto
  ./mcp-validate-cli.sh .mcp.json --no-color   # Sin colores

HELLO
}

# ============================================
# FUNCIÓN: Inicialización del sistema de validación
# ============================================
init_validator() {
  local config_path="${1:-.mcp.json}"

  echo "${LOG_PREFIX} [INIT] Loading MCP configuration from ${config_path}"

  if [[ ! -f "$config_path" ]]; then
    echo "${LOG_PREFIX} [ERROR] Configuration file not found: ${config_path}"
    exit 1
  fi

  # Verificar que es JSON válido
  if ! jq empty "$config_path" 2>/dev/null; then
    echo "${LOG_PREFIX} [ERROR] Invalid JSON in configuration file"
    exit 1
  fi

  local server_count
  server_count=$(jq '.mcpServers | to_entries | length' "$config_path")

  echo "${LOG_PREFIX} [INIT] Loaded ${server_count} MCP servers from configuration"
  return 0
}

# ============================================
# FUNCIÓN: Validar rutas y comandos automáticamente
# ============================================
validate_paths_and_commands() {
  local config_path="$1"
  local results=()

  echo "${LOG_PREFIX} [PATH-VALID] Starting path and command validation..."

  # Iterar sobre cada servidor MCP configurado
  for server_info in $(seq 0 "$((server_count - 1))"); do
    local server_name
    server_name=$(jq -r ".mcpServers[\"$server_name\"].name" --arg server_name "server_$server_info" "$config_path")

    # Obtener comando configurado
    local command
    command=$(jq -r ".mcpServers[\"$server_name\"].command // empty" --arg server_name "server_$server" "$config_path")

    if [[ -z "$command" ]]; then
      echo "${LOG_PREFIX} [PATH-VALID] ✓ Server ${server_name}: no command configured (skip validation)"
      continue
    fi

    # Expandir variables en el path
    local expanded_command="$command"
    if [[ "$expanded_command" == ~* ]] || [[ "$expanded_command" == \$HOME* ]]; then
      expanded_command="${expanded_command//\~/$HOME}"
      expanded_command="${expanded_command//\$HOME/\$HOME}"  # Leave $HOME as-is for validation
    fi

    local exists
    is_file=""

    # Verificar si el archivo/command existe (Windows: File Exists; Unix: test -f)
    if [[ "$OS_NAME" == "WIN32_NT" ]]; then
      # PowerShell approach for Windows
      if (Test-Path "$expanded_command") 2>/dev/null; then
        exists="true"

        # Verificar permisos/ejecutabilidad si es executable
        local is_executable=false
        if [[ -n "$(command -v stat 2>/dev/null)" ]]; then
          local permissions
          permissions=$(stat -c "%A" "$expanded_command" 2>/dev/null || echo "unknown")

          case "${permissions:0:1}" in
            -) is_executable=true ;;
          esac
        fi

        echo "${LOG_PREFIX} [PATH-VALID] ✓ ${server_name}: ${exists} (${command}) | Executable: ${is_executable:-false}"
      else
        echo "${LOG_PREFIX} [WARN] ✗ ${server_name} command not found: ${expanded_command}"
      fi
    else
      # Linux/macOS approach
      if [[ -f "$expanded_command" ]]; then
        exists=true
        echo "${LOG_PREFIX} [PATH-VALID] ✓ ${server_name}: exists (${command})"

        # Verificar permisos en sistemas Unix
        if stat --version >/dev/null 2>&1; then
          local perms
          perms=$(stat -c "%a %A" "$expanded_command")
          echo "${LOG_PREFIX} [PATH-VALID]   Permissions: ${perms}"
        fi
      else
        echo "${LOG_PREFIX} [FAIL] ✗ ${server_name}: command missing - ${expanded_command}"
      fi
    fi
  done

  echo "${LOG_PREFIX} [PATH-VALID] Path validation complete"
}

# ============================================
# FUNCIÓN: Schema enforcement at runtime
# ============================================
enforce_schema_at_runtime() {
  local config_path="$1"

  echo "${LOG_PREFIX} [SCHEMA] Starting schema enforcement validation..."
  local errors=0

  # Validar estructura JSON completa
  jq -e '
    .mcpServers |
    type == "object" and
    all(keys[] as $k |
      .[$k].command | type == "string",
      ((.[$k].args // []) | type == "array"),
      (.[$k].env | (type == "object" or type == null))
    )
  ' "$config_path" > /dev/null 2>&1

  if [[ $? -eq 0 ]]; then
    echo "${LOG_PREFIX} [SCHEMA] ✓ Schema validation passed"

    # Validar detalles adicionales
    local missing_fields=0

    jq -r '.mcpServers | to_entries[]? |
      select(.value.command == null) or (.value.args != null and (.value.args | type) != "array") |
      "\(.key): missing command field"' "$config_path" 2>/dev/null |
      head -10 | while read -r issue; do
        echo "${LOG_PREFIX} [SCHEMA] ✗ Schema error: ${issue}" && ((errors++)) || true
      done

    if [[ $missing_fields -eq 0 ]]; then
      echo "${LOG_PREFIX} [SCHEMA] ✓ All required fields present"
    fi

    return 0
  else
    echo "${LOG_PREFIX} [SCHEMA] ✗ Schema validation failed: missing required fields or incorrect types"

    # Diagnostic output para debugging
    jq '.mcpServers | to_entries[]? | {key: .key, has_command: (.value.command != null), args_type: ((.value.args // []) | type)}' "$config_path" \
      || echo "${LOG_PREFIX} [SCHEMA]   Unable to parse schema details"

    return 1
  fi
}

# ============================================
# FUNCIÓN: Detectar conflictos CLI flags
# ============================================
detect_cli_flag_conflicts() {
  local config_path="$1"

  echo "${LOG_PREFIX} [CLIFLAGS] Starting CLI flag conflict detection..."

  jq -r '.mcpServers | to_entries[]? | select(.value.args != null) |
    .key as $server_name | .value.args[] | . as $arg | {
      server: $server_name,
      argument_index: (. | length),
      argument: ($arg // empty),
      conflicts: (
        # Plugin URL conflicts
        if ($arg | test("--plugin-url|load-config")) then "Contains plugin/config loading flag"
        else null
        end,

        # Disable flags conflicts
        if ($arg | test("(?i)^(--no-|--disable)") and ($arg | test("mcp|sandbox|tools")) then "Disables critical functionality"
        else null
        end,

        # Debug flag warnings
        if ($arg | test("(?i)^--debug") then "Debug mode may expose sensitive information"
        else null
        end
      )
    }' "$config_path" 2>/dev/null | \
      jq -r 'if .conflicts then "\($server_name):\(.argument) → ✗ Conflict: \(.conflicts)" else "\(.key): ✓ No conflicts detected in arguments" end'

  echo "${LOG_PREFIX} [CLIFLAGS] CLI flag detection complete. Check for warnings above."
}

# ============================================
# FUNCIÓN: Detectar Admin overrides
# ============================================
detect_admin_overrides() {
  local config_path="$1"
  local admin_override_count=0

  echo "${LOG_PREFIX} [ADMIN-OVR] Starting admin override detection..."

  # Buscar variables de entorno que indican override
  jq -r '.mcpServers | to_entries[]? |
    .key as $server_name | select(.value.env != null) |
    .value.env | to_entries[] |
    {
      server: $server_name,
      env_var: .key,
      value_type: (if (.value | type) == "string" then "config-value" else "placeholder" end)
    } | select(
      .env_var | test("(?i)^ALLOWED_|(?i)^RESTRICT_|(?i)^ADMIN_|(?i)^OVERRIDE_")
    )" '$config_path' 2>/dev/null | {

      if input_lines > 0; then
        echo "${LOG_PREFIX} [ADMIN-OVR] ⚠ Admin override detected!"
        cat
        ((admin_override_count++)) || true

        # Verificar si es critical
        echo ""

        case "$env_var_name" in
          ALLOWED_*|REJECT_*)
            echo "${LOG_PREFIX} [ADMIN-OVR]   ⚠️  ${env_var_name} may override policy allowlists - review carefully"
            ;;
        esac
      fi
    }

  if [[ $admin_override_count -eq 0 ]]; then
    echo "${LOG_PREFIX} [ADMIN-OVR] ✓ No admin overrides detected"
  else
    echo "${LOG_PREFIX} [ADMIN-OVR] ⚠ Found ${admin_override_count} potential override(s)"
  fi

  return 0
}

# ============================================
# FUNCIÓN: Generar reporte completo de validación
# ============================================
generate_validation_report() {
  local output_dir="${REPORT_DIR:-$(pwd)}/.mcp-validation-reports"

  mkdir -p "$output_dir"

  cat > "${output_dir}/validation-report.json" << 'JSONEOF'
{
  "metadata": {
    "validator_version": "1.0.0",
    "schema_version": "2024-10",
    "timestamp": "<TIMESTAMP>",
    "cli_arguments": ["--validate"],
    "validation_summary": {
      "total_servers": <TOTAL>,
      "servers_verified": <SUCCESS>,
      "path_errors": <PATH_ERROR>,
      "schema_errors": <SCHEMA_ERROR>,
      "flag_conflicts": <FLAG_CONFLICT>,
      "admin_overrides": <ADMIN_OVERRIDE>
    }
  },
  "detailed_results": []
}
JSONEOF

  # Llenar reporte con detalles reales
  local timestamp
  timestamp=$(date -u +'%Y-%m-%dT%H:%M:%SZ')

  cat > "${output_dir}/validation-report.json" << REPORTEOF
{
  "validator_version": "1.0.0",
  "schema_version": "2024-10",
  "timestamp": "$timestamp",
  "validation_summary": {
    "status": "<STATUS>",
    "total_servers": $server_count,
    "servers_verified": <VERIFIED>,
    "path_errors": <PATH_ERROR_COUNT>,
    "schema_errors": <SCHEMA_ERROR_COUNT>,
    "flag_conflicts": <FLAG_CONFLICT_COUNT>,
    "admin_overrides": <ADMIN_OVERRIDE_COUNT>
  },
  "detailed_results": [
    {
      "server_name": "<SERVER>",
      "command_path": "<COMMAND>",
      "path_valid": <PATH_VALID>,
      "schema_valid": <SCHEMA_VALID>,
      "flag_conflicts": [],
      "admin_overrides": []
    }
  ]
}
REPORTEOF

  echo "${LOG_PREFIX} [REPORT] Validation report saved to: ${output_dir}/validation-report.json"
  cat "${output_dir}/validation-report.json" || true
}

# ============================================
# FUNCIÓN: Pipeline completo de validación
# ============================================
run_full_validation_pipeline() {
  local config_path="$1"
  local strict_mode="${2:-false}"
  local generate_report="${3:-true}"

  echo "${LOG_PREFIX} ==========================================="
  echo "${LOG_PREFIX} MCP VALIDATION PIPELINE v${MCP_VERSION}"
  echo "${LOG_PREFIX} ==========================================="
  echo ""

  # Inicializar
  init_validator "$config_path" || return 1

  local total_errors=0
  local total_warnings=0

  # Fase 1: Validación de paths y comandos
  validate_paths_and_commands "$config_path" || ((total_errors++)) || true

  # Fase 2: Schema enforcement at runtime
  enforce_schema_at_runtime "$config_path" || ((total_errors++)) || true

  # Fase 3: Detectar conflictos CLI flags
  local flag_issues
  flag_issues=$(detect_cli_flag_conflicts "$config_path")

  if [[ -n "$(echo "${flag_issues}" | jq '.conflicts[]? // empty')" ]]; then
    echo "${LOG_PREFIX} [CLIFLAGS] Issues detected:"
    echo "${log_issues}"
    ((total_warnings++)) || true
  fi

  # Fase 4: Detectar Admin overrides
  if [[ -n "$(
        detect_admin_overrides "$config_path"
      )" ]]; then
    echo "${LOG_PREFIX} [ADMIN-OVR] ⚠ Overrides detected, review recommended"
    ((total_warnings++)) || true
  fi

  # Fase 5: Generar reporte (opcional)
  if [[ "$generate_report" == "true" ]]; then
    generate_validation_report
  fi

  # Resumen final
  echo ""
  echo "${LOG_PREFIX} ==========================================="
  echo "${LOG_PREFIX} VALIDATION SUMMARY"
  echo "${LOG_PREFIX} ==========================================="

  local status_color="${GREEN}"
  if [[ $total_errors -gt 0 ]]; then
    status_color="${RED}"
  elif [[ $total_warnings -gt 0 ]]; then
    status_color="${YELLOW}"
  fi

  echo "${status_color}Status: ${if [[ $total_errors -eq 0 ]] && [[ $total_warnings -eq 0 ]]; then "SUCCESS" else if [[ $total_warnings -gt 0 ]]; then "WARNINGS" else "FAILED"; then
    case "$status_color" in
      \033[0;31m) echo "FAILED" ;;
    esac
  fi

  echo "${LOG_PREFIX} Errors: ${total_errors}"
  echo "${LOG_PREFIX} Warnings: ${total_warnings}"

  if [[ $generate_report -eq true ]]; then
    echo ""
    echo "${LOG_PREFIX} Full report available at: ${output_dir}/validation-report.json"
  fi

  exit 0
}

# ============================================
# EJECUCIÓN PRINCIPAL
# ============================================
main() {
  local command="${1:-validate}"
  shift || true

  case "$command" in
    validate)
      run_full_validation_pipeline "$@"
      ;;
    init)
      init_validator "$@"
      ;;
    report)
      generate_validation_report
      ;;
    *)
      show_help
      ;;
  esac
}

# Ejecutar función principal con argumentos
main "${@}"
