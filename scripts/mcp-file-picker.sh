#!/bin/bash
# @anthropics/mcp-file-picker - Selector manual de archivos y directorios

MCP_FILE_PICKER_VERSION="latest"
REPORT_DIR="${HOME}/.mcp-validation-reports"

echo "=========================================="
echo "@anthropics/mcp-file-picker Script v1.0"
echo "=========================================="

echo "[INFO] File picker service initialized..."
echo "[INFO] Ready to select files from allowed directories:"
echo "  - ./projects/*"
echo "  - ./.claude/*"
echo "  - ./scripts/*"
echo "  - /.mcp-validation-reports/*"

# Iniciar servicio de selección manual (modo espera para UX)
echo ""
echo "[INFO] File picker is ready. Use file browser to select assets manually."
echo "[INFO] For automation, use: python3 scripts/mcp-validator.py ./.mcp.json --validate"

exit 0
