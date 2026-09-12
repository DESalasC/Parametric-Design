# Sistema de Validación MCP para Diseño Paramétrico

## 🎯 Visión General

Este sistema implementa **validación automática completa** para la configuración MCP (Model Context Protocol) del proyecto Diseño Paramétrico.

---

## ✅ Sistemas Implementados

### 1. **Validación Automática de Paths y Comandos**
- Expansión automática de variables de entorno (`~`, `$HOME`, etc.)
- Verificación de existencia y ejecutabilidad
- Detección de paths inseguros (ejecutables no autorizados)
```bash
# Ejemplo:
./scripts/mcp-validate.sh ./mcp.json --validate
```

### 2. **Schema Enforcement at Runtime**
- Validación de estructura JSON completa
- Campos obligatorios: `command` y `args`
- Escaping automático de caracteres especiales
- Verificación de tipos de datos correctos
```python
# Python validator
python3 ./scripts/mcp-validator.py .mcp.json --strict
```

### 3. **Detección de CLI Flag Conflicts**
- Patrón para flags peligrosos:
  - `--plugin-url=...` → Posible conflicto con plugin loads
  - `--load-config=...` → Override silencioso no intencional
  - `--debug=true` → Exposición de información sensible
- Alerta automática sobre patrones inseguros

### 4. **Detección de Admin Overrides**
- Variables de entorno que indican override de política:
  - `ALLOWED_MCP_SERVERS=...`
  - `REJECT_MCP_SERVERS=...`
  - `ADMIN_OVERRIDE_*=...`
- Alerta sobre credenciales sensibles

---


## 📁 Archivos del Sistema

```
DiseñoParamétrico/
├── .mcp.json                            # Configuración principal
├── scripts/
│   ├── mcp-validation.js                # Node.js validator
│   ├── mcp-validate.sh                  # Bash validator
│   ├── mcp-validate-cli.sh              # CLI validator completo
│   └── mcp-validator.py                 # Python validator con schema enforcement
├── MCP_SYSTEM_ANALYSIS.md               # Análisis y recomendaciones
└── README_MCP_VALIDATION.md             # Este archivo
```

---

## 🚀 Uso Rápido

### Validación Básica:
```bash
./scripts/mcp-validate.sh .mcp.json --validate
```

### Validación con Schema Enforcement:
```bash
python3 scripts/mcp-validator.py .mcp.json --strict
```

### Generar Reporte JSON:
```bash
./scripts/mcp-validate-cli.sh .mcp.json --report /tmp/report.json
```

---

## 🔧 Configuración Recomendada (.mcp.json)

Ver archivo `.mcp.json` del proyecto para la configuración completa con todos los servidores MCP necesarios.

**Servicios Incluidos:**
- ✅ Path Validator (implementado)
- ✅ Python MCP Validator (schema enforcement)
- ✅ CLI Validator System (complete validation)
- 🔧 Filesystem Server (acceso a archivos locales)
- 🔧 Design Sync Server (sincronización con claude.ai)

---

## 📊 Archivos de Validación Implementados

### 1. `mcp-validator.py` - Python Schema Validator
- **Capabilidades:** Schema enforcement completo en tiempo de ejecución
- **Recomendado para:** Entornos con Python disponible

```python
python3 ./scripts/mcp-validator.py .mcp.json --strict --report report.json
```

### 2. `mcp-validate-cli.sh` - Bash CLI Validator
- **Capabilidades:** Validación completa vía shell
- **Recomendado para:** Linux/macOS o WSL

```bash
./scripts/mcp-validate-cli.sh .mcp.json --validate
```

### 3. `mcp-validation.js` - Node.js Validator
- **Capabilidades:** Validación mediante JavaScript
- **Recomendado para:** Entornos con Node.js instalado

```javascript
node ./scripts/mcp-validation.js ./mcp.json
```

---

## 🎯 Recomendaciones: ¿Necesitas Más MCP?

### Para Facilitar Todas las Labores del Proyecto Paramétrico, se recomienda tener adicionalmente:

| Servidor | Justificación | Estado |
|----------|--------------|--------|
| `@modelcontextprotocol/server-everything` | API unificada para validación múltiple | 🔧 Recomendado |
| `@modelcontextprotocol/server-filesystem` | Acceso seguro a archivos locales | 🔧 Recomendado |
| `@anthropics/mcp-file-picker` | Selección visual de assets | 🔧 Opcional (manual) |
| `@modelcontextprotocol/server-wikipedia` | Documentación técnica | 🔧 Recomendado para doc. |

**Ver:** [`MCP_SYSTEM_ANALYSIS.md`](./MCP_SYSTEM_ANALYSIS.md)

---

## 🛡️ Seguridad Implementada

### Flags de seguridad por defecto:
```jsonc
{
  "securityFlags": {
    "noWriteAccess": true,          // Prevenir escritura no autorizada
    "strictPathSecurity": true,     // Validar paths estrictamente
    "autoSanitization": true,       // Autodesinfección automática
    "sandboxMode": true             // Sandboxed execution
  }
}
```

### Detección de Credentials Sensibles:
- Alerta si `*TOKEN`, `*SECRET`, `*KEY` en variables de entorno
- Masking automático de valores sensibles en logs

---

## 📝 License

MIT © Proyecto Diseño Paramétrico
