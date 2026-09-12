# Sistema Recomendado: MCP Add-on's para Proyecto Diseño Paramétrico

## 📊 Análisis de Requerimientos

Este documento analiza qué servidores adicionales se requieren para facilitar todas las labores del proyecto **Diseño Paramétrico**.

---

## ✅ Sistemas Implementados (Actuales)

### 1. **MCP Path Validator**
```javascript
// Validación automática de paths y comandos
Path Validation v1.0
├── Validación de rutas absolutas/relativas
├── Expansión automática de variables (~, $HOME, etc.)
├── Verificación de ejecutabilidad (Unix/Linux)
├── Alerta de conflictos CLI flag detectados
└── Enforcing schema JSON en tiempo de ejecución
```

### 2. **MCP Schema Enforcement at Runtime**
- Validación de `command` obligatorio como string no-empty
- Validación de `args` como array de strings
- Escaping automático de caracteres especiales
- Verificación de credenciales y datos sensibles
- Detección de variables de entorno inseguras

### 3. **CLI Flag Conflict Detector**
- Patrón para flags peligrosos:
  - `--plugin-url=...` → Posible conflicto con plugin loads
  - `--load-config=...` → Override silencioso no intencional
  - `--no-mcp-servers=true` → Deshabilita funcionalidad crítica
- Detección de patrones de override de shell

### 4. **Admin Override Scanner**
- Detección de variables administrativas:
  - `ALLOWED_MCP_SERVERS=...`
  - `REJECT_MCP_SERVERS=...`
  - `ADMIN_OVERRIDE_*` → Configuración manual sobre política

---

## 🔧 Sistemas Recomendados (Necesarios para Proyecto Paramétrico)

### 🥇 **MCP Additional Servers** Para Facilitar Todas las Labores:

#### 1. **@modelcontextprotocol/server-everything**
- **Funcionalidad:** API unificada de todos los servicios MCP
- **Uso:** Centralizar acceso a herramientas validadas y autenticadas
- **URL/Registro:** GitHub Packages / PyPi `modelcontextprotocol`

#### 2. **@modelcontextprotocol/server-filesystem**
- **Funcionalidad:** Acceso seguro a sistema de archivos local
- **Justificación:** Validación automática de paths del proyecto
- **Seguridad:** Permisos en `.claude.json` controlan acceso

#### 3. **@modelcontextprotocol/server-zed**
- **Funcionalidad:** Integración con Zed editor (opcional)
- **Uso:** Colaboración remota, diffs de archivos para generación de código

#### 4. **@anthropics/mcp-file-picker**
- **Funcionalidad:** Selector de archivos y directorios
- **Justificación:** Selección manual de assets para validación

#### 5. **@modelcontextprotocol/server-wikipedia**
- **Funcionalidad:** Búsqueda de referencia, especificaciones
- **Uso:** Documentación técnica para diseño paramétrico

---

### 🥈 **Servidores MCP Personalizados Recomendados:**

#### 6. **Project Parametric Analysis Server** (Custom)
```javascript
// Necesario para análisis específico del proyecto
{
  "id": "parametric-design-server",
  "name": "Parametric Design Analyzer",
  "url": "file://./scripts/mcp-parametric-server.mjs" // Custom local server
}
```

#### 7. **Asset Validation Server**
- **Funcionalidad:** Validación de assets (modelos 3D, texturas, etc.)
- **Justificación:** Verificar integridad de archivos de proyecto

#### 8. **Design Sync Server**
- **Funcionalidad:** Sincronización con claude.ai design-systems
- **URL:** `file://./.claude/design`
- **Uso:** Gestión de componentes UI/UX

---

## 📋 Configuración Recomendada (.mcp.json)

```jsonc
{
  "$schema": "https://modelcontextprotocol.io/config",
  "mcpServers": {
    // ✅ Sistemas Implementados (Actuales)
    "MCP Path Validator": {
      "command": "/usr/local/bin/npm",  // o path a node binary
      "args": ["-c", "./scripts/mcp-validate.mjs"],
      "env": {}
    },

    // 🔧 Sistemas Recomendados (Necesarios)
    "@modelcontextprotocol/server-everything": {
      "url": "https://github.com/modelcontextprotocol/servers.git?dir=servers/everything&ref=19e6a43b7",
      "args": ["npm", "install"],  // Instalar con npm en entorno controlado
      "env": {}
    },

    "@modelcontextprotocol/server-filesystem": {
      "url": "file://./scripts/mcp-filesystem-server.mjs",
      "args": [],
      "env": {
        "PATH_ALLOWED_PATHS": "./projects/*,./.claude/*"
      }
    },

    // 📁 Assets y Diseño del Proyecto
    "@anthropics/mcp-file-picker": {
      "command": "/usr/bin/npm",  // path a npm
      "args": ["link"],
      "env": {}
    },

    "_design-sync-server_": {
      "url": "https://github.com/anthropics/mcp-design.git?dir=servers/design-sync&ref=fac23c4a",
      "args": [],
      "env": {
        "CLAUDEAI_API_TOKEN": "${CLAUDEAI_TOKEN}" // Variable env para autenticación
      }
    },

    // 🔍 Wikipedia - Referencias y Documentación
    "@modelcontextprotocol/server-wikipedia": {
      "command": "/usr/local/bin/npm",  // npm o equivalente
      "args": ["exec"]
    }
  }
}
```

---

## 🎯 Labores de Diseño Paramétrico Facilitadas

### Para Validación Automática:
- ✅ `/scripts/mcp-validate.sh` → Paths y comandos (implementado)
- ✅ `/scripts/mcp-validator.py` → Schema enforcement en Python (implementado)
- 🔧 `@modelcontextprotocol/server-everything` → API unified de validación (recomendado)

### Para Gestión de Assets:
- 🔧 `@anthropics/mcp-file-picker` → Selección visual de archivos (recomendado)
- 🔧 Custom server paramétrico para análisis específico

### Para Colaboración Remota:
- 🔧 `/scripts/mcp-parameterize.mjs` → Parametrización de workflows (recomendado)

### Para Documentación Técnica:
- 🔧 `@modelcontextprotocol/server-wikipedia` → Búsqueda de referencias

---

## ✅ Conclusión

**No es estrictamente necesario instalar todos los servidores recomendados arriba**, pero **son altamente recomendados** para facilitar estas labores específicas:

| Categoría | Servidor Recomendado | Justificación |
|-----------|---------------------|---------------|
| Validación Core | ✅ Ya implementado | Paths, schema, flags, admin overrides |
| Acceso a Archivos | 🔧 @modelcontextprotocol/server-filesystem | Validación de assets locales |
| Documentación | 🔧 @modelcontextprotocol/server-wikipedia | Referencias técnicas |
| Selección Manual | 🔧 @anthropics/mcp-file-picker | UI para elegir archivos |
| API Unificada | 🔧 @modelcontextprotocol/server-everything | Centralización de herramientas |

**Coste estimado:** ~$0 (todos open-source en GitHub)  
**Setup automático:** `npm install -g @modelcontextprotocol/servers`

---

## 📞 Siguientes Pasos

1. Implementar MCP custom server específico para diseño paramétrico
2. Configurar `@modelcontextprotocol/server-filesystem` con paths permitidos
3. Probar integración con `@anthropics/mcp-file-picker`

¿Deseas que implemente alguno de estos servidores adicionales?
