# fcc-server + Claude Code — Configuración

**Fecha:** 2026-08-01
**Stack:** Ollama (local) + fcc-server + Claude Code + (opcional) Gemini + GLM-4.6/5.2

---

## Arquitectura

```
┌─────────────────┐
│  Claude Code    │ ← CLI interactivo
│  (npm global)   │
└────────┬────────┘
         │ HTTP /v1/messages
         ↓
┌─────────────────┐
│  fcc-server     │ ←Puente (puerto 8787)
│  (Node.js)      │   Enruta por tarea
└────────┬────────┘
         │
    ┌────┴────┬─────────┬──────────┐
    ↓         ↓         ↓          ↓
┌────────┐ ┌──────┐ ┌────────┐ ┌────────┐
│ Ollama │ │ qwen │ │ Gemini │ │  GLM   │
│  11434 │ │ :7b  │ │  API   │ │ 4.6/5.2│
│  (local│ │fallback│ │(nube) │ │ (Z.ai) │
└────────┘ └──────┘ └────────┘ └────────┘
```

## Modelos disponibles

| Modelo | Tipo | VRAM | Cuándo usar |
|--------|------|------|------------|
| `qwen2.5-coder:14b` | Local | ~9 GB | **Default** para código GHPython |
| `qwen2.5:7b` | Local | ~5 GB | Cuando Rhino.Compute activo |
| `qwen2.5:32b` | Local | ~19 GB | Razonamiento profundo (solo si compute apagado) |
| `llama3.2:3b` | Local | ~2 GB | Emergencia (VRAM llena) |
| `mistral:latest` | Local | ~4 GB | Chat conversacional |
| `gemini-1.5-pro` | Nube | 0 | Fallback en la nube (requiere API key) |
| `glm-4.6` / `glm-5.2` | Nube (Z.ai) | 0 | Contexto largo, calidad Anthropic-level (requiere API key) |

## Enrutamiento por tarea

El `.env` de fcc-server define qué modelo usar según tipo de tarea:

```env
ROUTING_CODE=qwen2.5-coder:14b        # Generación de código
ROUTING_CHAT=qwen2.5:7b                # Chat rápido
ROUTING_LONG_CONTEXT=glm-4.6           # Documentos largos (>32k tokens)
ROUTING_FALLBACK=llama3.2:3b           # Emergencia
```

## Instalación

### Paso 1: Configurar fcc-server

```powershell
pwsh -ExecutionPolicy Bypass -File D:\WORK\scripts\setup-fcc-server.ps1
```

El script:
1. Verifica Node.js (lo instala si falta)
2. Clona fcc-server a `D:\WORK\AI\fcc-server\`
3. Instala dependencias npm
4. Crea `.env` con configuración de backends
5. Crea scripts `start-fcc.ps1` y `start-fcc-bg.ps1`
6. Verifica que Ollama está corriendo

### Paso 2: Configurar Claude Code

```powershell
pwsh -ExecutionPolicy Bypass -File D:\WORK\scripts\setup-claude-code.ps1
```

El script:
1. Instala `@anthropic-ai/claude-code` global
2. Configura variables de entorno:
   - `ANTHROPIC_BASE_URL=http://127.0.0.1:8787`
   - `ANTHROPIC_API_KEY=fcc-local-token`
3. Verifica fcc-server
4. Crea script de prueba

### Paso 3: REINICIAR PowerShell

**Crítico:** Las variables de entorno solo cargan al abrir una nueva sesión de PowerShell.

```powershell
exit
# Abrir nueva ventana de PowerShell
```

### Paso 4: Iniciar fcc-server

```powershell
# Modo foreground (muestra logs, Ctrl+C para detener)
pwsh -File D:\WORK\AI\fcc-server\start-fcc.ps1

# O modo background (sin logs)
pwsh -File D:\WORK\AI\fcc-server\start-fcc-bg.ps1
```

### Paso 5: Probar que todo funciona

```powershell
pwsh -File D:\WORK\PROJECTS\DiseñoParametrico\scripts\utilities\test-claude-code.ps1
```

Debe mostrar:
- ✅ fcc-server respondiendo
- ✅ Variables de entorno configuradas
- ✅ Claude Code instalado
- ✅ Ollama con modelos disponibles
- ✅ Test de respuesta: "OK"

### Paso 6: Usar Claude Code

```powershell
cd D:\WORK\PROJECTS\DiseñoParametrico
claude
```

En el prompt de Claude Code, prueba:

```
> Lee CLAUDE.md y dime qué modelos estás usando
> ¿Qué hace el proyecto DiseñoParametrico?
> Lista los scripts en src/fase-1-contexto/
> Explica qué hace F1_CONTEXTO_POT_v01.py
```

## Configuración de API keys (opcional)

### Gemini (Google AI Studio)

1. Ve a https://aistudio.google.com/app/apikey
2. Crea una API key
3. Edita `D:\WORK\AI\fcc-server\.env`:
   ```env
   GEMINI_API_KEY=AIzaSy...
   ```
4. Reinicia fcc-server

### GLM-4.6 / GLM-5.2 (Z.ai)

1. Ve a https://z.ai/ o https://open.bigmodel.cn/
2. Regístrate y obtén API key
3. Edita `D:\WORK\AI\fcc-server\.env`:
   ```env
   GLM_API_KEY=tu_key_aqui
   GLM_MODEL=glm-4.6
   # o para GLM-5.2 (cuando esté disponible):
   # GLM_MODEL=glm-5.2
   ```
4. Reinicia fcc-server

## Comandos útiles

### Iniciar/detener servicios

```powershell
# fcc-server
pwsh -File D:\WORK\AI\fcc-server\start-fcc.ps1      # foreground
pwsh -File D:\WORK\AI\fcc-server\start-fcc-bg.ps1   # background

# Ollama
Start-Service Ollama
Stop-Service Ollama
Restart-Service Ollama

# Verificar estado
pwsh -File D:\WORK\PROJECTS\DiseñoParametrico\scripts\rhino-compute\health-check.ps1
```

### Verificar modelo activo

```powershell
# Desde Claude Code
claude
> ¿Qué modelo estás usando?

# Ver logs de fcc-server (si está en foreground)
# Mostrará qué backend se usa para cada petición
```

### Cambiar modelo primario

Edita `D:\WORK\AI\fcc-server\.env`:

```env
OLLAMA_DEFAULT_MODEL=qwen2.5-coder:14b    # cambiar aquí
```

Reinicia fcc-server.

## Solución de problemas

### "Claude Code no puede conectar a fcc-server"

1. Verifica que fcc-server está corriendo:
   ```powershell
   curl http://127.0.0.1:8787/health
   ```

2. Si no responde, inícialo:
   ```powershell
   pwsh -File D:\WORK\AI\fcc-server\start-fcc.ps1
   ```

3. Verifica variables de entorno:
   ```powershell
   echo $env:ANTHROPIC_BASE_URL
   # Debe mostrar: http://127.0.0.1:8787
   ```

4. Si las variables no están, REINICIA PowerShell.

### "Ollama no responde"

```powershell
Start-Service Ollama
ollama list   # verificar modelos disponibles
```

### "Modelo no encontrado"

```powershell
# Verificar modelos instalados
ollama list

# Descargar modelo faltante
ollama pull qwen2.5-coder:14b
```

### "fcc-server muestra errores de API key"

Si configuraste Gemini o GLM y hay errores:

1. Verifica que las API keys sean válidas
2. Edita `.env` y corrige si es necesario
3. Reinicia fcc-server

### "VRAM saturada con Rhino.Compute + Ollama"

Con 12 GB VRAM, cambiar a modelo más liviano:

```env
OLLAMA_DEFAULT_MODEL=qwen2.5:7b
```

Reinicia fcc-server.

## Estructura de archivos

```
D:\WORK\
├── AI\
│   ├── ollama\                          # binarios Ollama
│   ├── fcc-server\                      # puente Claude Code
│   │   ├── .env                         # configuración backends
│   │   ├── package.json
│   │   ├── start-fcc.ps1                # iniciar foreground
│   │   └── start-fcc-bg.ps1             # iniciar background
│   └── ollama\                          # (alternativa, si lo tienes aquí)
│
├── PROJECTS\DiseñoParametrico\
│   ├── CLAUDE.md                        # reglas del proyecto
│   ├── scripts\
│   │   └── utilities\
│   │       └── test-claude-code.ps1     # script de prueba
│   └── ...
│
└── scripts\
    ├── setup-fcc-server.ps1
    ├── setup-claude-code.ps1
    └── health-check.ps1
```

## Próximos pasos después de configurar

1. **Probar Claude Code con el proyecto:**
   ```powershell
   cd D:\WORK\PROJECTS\DiseñoParametrico
   claude
   > Lee CLAUDE.md y resume las reglas principales
   > Lista los scripts GHPython en src/fase-1-contexto/
   > ¿Qué hace F1_CONTEXTO_POT_v01.py?
   ```

2. **Adaptar scripts GHPython para usar JSONs estructurados:**
   - Pedirle a Claude Code que actualice `F1_CONTEXTO_POT_v01.py` para leer `data/pot-cache/<predio>.json`
   - Pedirle que actualice `F1_LADOS_CONFIGURAR_v01.py` para usar `data/pot-bogota/retiros-estructurados.json`
   - Pedirle que actualice `F1_VECINOS_ANALISIS_v01.py` para usar `data/nsr-10/separaciones-sismicas.json`

3. **Generar tests:**
   - Pedirle a Claude Code que cree tests para cada script de Fase 1

4. **Documentar lecciones en el vault:**
   - Cada vez que aprendas algo, pídele a Claude Code que cree una nota en `D:\WORK\NOTES\obsidian-vault\50-lecciones\`

## Sobre GLM-5.2

GLM-5.2 (de Z.ai / Zhipu AI) es un modelo avanzado que puede superar a Claude/GPT en ciertas tareas de razonamiento y código. Para integrarlo:

1. **Obtener API key:**
   - https://z.ai/ (sitio internacional)
   - https://open.bigmodel.cn/ (sitio chino, más económico)

2. **Configurar en `.env`:**
   ```env
   GLM_API_KEY=tu_key
   GLM_MODEL=glm-4.6    # o glm-5.2 cuando esté disponible
   ```

3. **Usar para tareas específicas:**
   - Contexto largo (documentos POT completos)
   - Razonamiento complejo (análisis normativo)
   - Generación de código BIM complejo

4. **Enrutamiento sugerido:**
   - Default: `qwen2.5-coder:14b` (local, sin costo)
   - Tareas largas: `glm-4.6` (mejor calidad, costo API)
   - Fallback: `gemini-1.5-pro` (cuando Ollama y GLM fallen)
