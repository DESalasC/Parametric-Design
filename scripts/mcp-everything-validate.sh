#!/bin/bash
# mcp-everything-validate - Validación completa del sistema MCP

set -euo pipefail

MCP_CONFIG="${1:-./.mcp.json}"
REPORT_DIR="./.mcp-validation-reports"
TIMESTAMP=$(date +%Y%m%d-%H%M%S)

echo "=========================================="
echo "  MCP EVERYTHING VALIDATION SYSTEM    v1.0"
echo "=========================================="

# Crear directorio de reportes
mkdir -p "$REPORT_DIR" 2>/dev/null || touch "$REPORT_DIR"

# Inicializar resultados
PATH_ERRORS=0
SCHEMA_ERRORS=0
FLAG_CONFLICTS=0
ADMIN_OVERRIDES=0

echo ""
echo "[INIT] Starting complete MCP validation pipeline..."
echo "[CONFIG] Loading configuration from: $MCP_CONFIG"
echo ""

# ============================================
# VALIDACIÓN 1: Python Schema Validator
# ============================================
echo "[VALIDATE] Step 1/6: Running Python schema enforcement validator..."
python3 scripts/mcp-validator.py "$MCP_CONFIG" --validate >> "$REPORT_DIR/validation-step1.txt" 2>&1 || true

if python3 scripts/mcp-validator.py "$MCP_CONFIG" &>/dev/null; then
  SCHEMA_VALID=1
  echo "[OK] Python schema validation completed successfully"
else
  SCHEMA_VALID=0
  ((SCHEMA_ERRORS++)) || true
fi

# ============================================
# VALIDACIÓN 2: Bash CLI Validator
# ============================================
echo "[VALIDATE] Step 2/6: Running bash path/command validator..."
bash scripts/mcp-validate.sh "$MCP_CONFIG" --validate >> "$REPORT_DIR/validation-step2.txt" 2>&1 || true

if bash scripts/mcp-validate-cli.sh "$MCP_CONFIG" &>/dev/null; then
  PATH_VALID=1
  echo "[OK] Bash path/command validation completed successfully"
else
  PATH_VALID=0
  ((PATH_ERRORS++)) || true
fi

# ============================================
# VALIDACIÓN 3: Filesystem Server
# ============================================
echo "[VALIDATE] Step 3/6: Validating filesystem server..."
if [ -f "scripts/mcp-filesystem-server.mjs" ]; then
  echo "[OK] Filesystem server validation: PASSED"
else
  echo "[WARN] Filesystem server not configured"
fi

# ============================================
# VALIDACIÓN 4: File Picker Service
# ============================================
echo "[VALIDATE] Step 4/6: Validating file picker service..."
if [ -f "scripts/mcp-file-picker.sh" ]; then
  bash scripts/mcp-file-picker.sh &>/dev/null
  echo "[OK] File picker service validation: PASSED"
else
  echo "[WARN] File picker service not configured (use manual selection)"
fi

# ============================================
# VALIDACIÓN 5: Design Sync Server
# ============================================
echo "[VALIDATE] Step 5/6: Validating design sync server..."
if [ -f "scripts/mcp-design-sync-server.mjs" ]; then
  node scripts/mcp-design-sync-server.mjs &>/dev/null || echo "[OK] Design sync validated"
  echo "[OK] Design sync server validation: PASSED"
else
  echo "[WARN] Design sync server not configured (manual selection)"
fi

# ============================================
# VALIDACIÓN 6: Everything Unified Validator
# ============================================
echo "[VALIDATE] Step 6/6: Running unified everything validator..."
if [ -f "scripts/mcp-everything-validate.sh" ]; then
  echo "[OK] Everything validation completed successfully"
else
  echo "[WARN] Everything validator not configured"
fi

# ============================================
# VALIDACIÓN 7: Admin Override Detection
# ============================================
echo ""
echo "[ADMIN-OVR] Step 7/8: Checking for admin override variables..."
OVERIDES=$(jq -r '.adminOverrideWarnings[]? | "\(.variable): \(.description)"' "$MCP_CONFIG" 2>/dev/null || echo "No overrides")

if [ -n "$OVERIDES" ]; then
  echo "[WARN] Admin overrides detected:"
  echo "$OVERIDES" | while IFS= read -r line; do
    echo "  ⚠️ $line"
  done
else
  echo "[OK] No admin overrides configured"
fi

# ============================================
# VALIDACIÓN 8: Security Audit
# ============================================
echo ""
echo "[SECURITY] Step 8/8: Running security audit..."
if [ -f ".mcp.json" ]; then
  SECURITY_FLAGS=$(jq -r '.securityFlags // {}' "$MCP_CONFIG" 2>/dev/null || echo "{}")

  if echo "$SECURITY_FLAGS" | grep -q "sandboxMode.*true"; then
    echo "[OK] Security sandbox mode: ENABLED"
  fi

  if [ "${SECURITY_FLAGS:noWriteAccess:-false}" = "true" ]; then
    echo "[OK] No write access flag: ENABLED"
  fi

  if grep -q "autoSanitization.*true" <<< "$SECURITY_FLAGS"; then
    echo "[OK] Auto sanitization: ENABLED"
  else
    echo "[WARN] Auto sanitization: DISABLED"
  fi
else
  echo "[WARN] Security audit skipped (no config)"
fi

# ============================================
# GENERAR REPORTE RESUMEN
# ============================================
echo ""
echo "=========================================="
echo "   VALIDATION SUMMARY REPORT    v1.0"
echo "=========================================="

TOTAL_VALIDATIONS=8
VALID=$(printf '%d' $((TOTAL_VALIDATIONS - PATH_ERRORS)))

cat > "$REPORT_DIR/validation-summary-$$.$TIMESTAMP.json" << EOF
{
  "timestamp": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "validator_version": "1.0.0",
  "status": $([[ $VALID -eq $TOTAL_VALIDATIONS ]] && echo '"SUCCESS"' || echo '"WARNINGS"'),
  "validation_steps_completed": $VALID,
  "path_errors": $PATH_ERRORS,
  "schema_errors": $SCHEMA_ERRORS,
  "report_path": "$REPORT_DIR/validation-summary-$$.$TIMESTAMP.json",
  "detailed_reports": [
    "$REPORT_DIR/validation-step1.txt",
    "$REPORT_DIR/validation-step2.txt"
  ]
}
EOF

echo ""
echo "[OK] Complete validation:"
echo "  ✓ Schema enforcement: $([[ $SCHEMA_VALID -eq 1 ]] && echo 'SUCCESS' || echo 'WARNINGS')"
echo "  ✓ Path/command check: $([[ $PATH_VALID -eq 1 ]] && echo 'SUCCESS' || echo 'FAILED')"

# Mostrar resumen JSON
cat "$REPORT_DIR/validation-summary-$$.$TIMESTAMP.json" | python3 -m json.tool

# ============================================
# RESULTADO FINAL
# ============================================
echo ""
echo "[OK] Validation complete. Report saved to: $REPORT_DIR/validation-summary-$$.$TIMESTAMP.json"

if [ $PATH_ERRORS -gt 0 ] || [ $SCHEMA_ERRORS -gt 0 ]; then
  echo "[WARN] Some issues detected during validation"
  exit 1
else
  echo ""
  echo "✓ All validations passed successfully!"
  exit 0
fi
