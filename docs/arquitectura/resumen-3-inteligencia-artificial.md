# Resumen 3: Configuración de Inteligencia Artificial

**Fecha:** 2026-08-03
**Proyecto:** DiseñoParametrico
**Alcance:** Configuración de modelos de IA local (Ollama), proxy multi-backend (FCC), Claude Code, y evaluación de herramientas avanzadas (Ruflo, RHINO-MCP, ROBO-HOPPER).

---

## 1. Puntos Relevantes para Entender el Proceso

### 1.1 El objetivo de IA

El proyecto necesita IA para:
- **Generación de código GHPython** (adaptar scripts a JSONs estructurados)
- **Análisis normativo** (interpretar decretos POT y NSR-10)
- **Asistencia de diseño** (sugerir patrones, calcular áreas, evaluar tipologías)
- **Automatización** (crear tests, documentar, migrar código)

El requisito clave: **minimizar costo de tokens** manteniendo calidad.

### 1.2 Las tres capas de IA configuradas

```
CAPA 1: Modelos locales (Ollama)
├── qwen2.5-coder:14b (9 GB) — primario para código
├── qwen2.5:7b (5 GB) — ligero, para VRAM limitada
├── qwen2.5:32b (19 GB) — razonamiento profundo
├── mistral:latest (4 GB) — chat conversacional
├── codellama:latest (4 GB) — alternativo para código
├── llama3.2:3b (2 GB) — emergencia
└── deepseek-r1:8b (5 GB) — modelo de razonamiento con thinking

CAPA 2: Proxy multi-backend (FCC)
├── Free Claude Code v4.16.2 (Alishahryar1/free-claude-code)
├── Admin UI en http://127.0.0.1:8082/admin
├── 31 providers soportados
├── Enrutamiento por modelo (overrides para Opus/Sonnet/Haiku/Fable)
└── API keys configuradas: OpenAI, Nvidia, Gemini, Kimi, DeepSeek, OpenRouter, Z.ai

CAPA 3: Cliente (Claude Code)
├── Claude Code v2.1.220 (CLI)
├── Architect Skills (18 skills + 7 calculadoras)
├── CLAUDE.md jerárquico (global + proyecto + vault)
└── Conexión vía FCC (ANTHROPIC_BASE_URL=http://127.0.0.1:8082)
```

### 1.3 El descubrimiento del free tier

Inicialmente asumimos que se necesitaba suscripción paga de Anthropic. Descubrimos que:
- Claude Code incluye **free tier** al instalarlo
- Acceso limitado a Opus 5, Sonnet 4, Haiku 4.5
- ~30-50 mensajes cada 5 horas
- Suficiente para desarrollo iterativo

### 1.4 La evaluación de herramientas avanzadas

Se evaluaron 3 herramientas adicionales:

| Herramienta | Función | Decisión |
|-------------|---------|----------|
| **Ruflo** (ruvnet/ruflo) | Orquestación de agentes, memoria RAG, tracking de costos | Postergado (35 plugins = overkill) |
| **RHINO-MCP** (easehee) | Puente Rhino ↔ Claude Desktop vía MCP | Postergado (requiere Claude Desktop) |
| **ROBO-HOPPER** (Peluffo) | Agente construye GH en vivo | Postergado (beta inestable + requiere Claude Desktop) |

### 1.5 El enrutamiento de modelos

FCC permite enrutar diferentes "niveles" de Claude a diferentes backends:

```
Claude Code pide "claude-opus-5" (tarea compleja)
    ↓ FCC busca override para "opus"
    ↓ Si no hay override → usa DEFAULT
    ↓ DEFAULT puede ser: Ollama, Z.ai, DeepSeek, etc.

Claude Code pide "claude-haiku-4.5" (tarea simple)
    ↓ FCC busca override para "haiku"
    ↓ Si hay override → usa ese modelo
```

### 1.6 Los desafíos de compatibilidad

Claude Code está diseñado para Anthropic API. Usarlo con Ollama vía FCC presentó tres incompatibilidades:

1. **Contexto:** System prompt de Claude Code (~7K tokens) excede el default de Ollama (4K)
2. **Thinking:** Claude Code v2.1.220 envía parámetro "thinking" que Qwen no soporta
3. **Tool use:** Formato de herramientas de Anthropic no se traduce perfectamente a Ollama

---

## 2. Errores Encontrados

### Error 1: FCC no se podía clonar (repos inexistentes)
- **Síntoma:** `Repository not found` para JoshuaC215/fcc-server y musistudio/fcc-server
- **Causa:** Los repositorios asumidos no existían
- **Solución:** Usuario encontró el repo oficial `Alishahryar1/free-claude-code`
- **Lección:** Verificar URLs de repositorios antes de hardcodearlas

### Error 2: Z.ai API key sin saldo
- **Síntoma:** `HTTP 429: Insufficient balance or no resource package`
- **Causa:** La API key de Z.ai no tenía créditos disponibles
- **Solución:** Cambiar a Ollama (local, gratis) como default
- **Lección:** Verificar saldo de API keys antes de configurarlas como primarias

### Error 3: DeepSeek API key sin saldo
- **Síntoma:** `HTTP 402: Insufficient Balance`
- **Causa:** La API key de DeepSeek tampoco tenía créditos
- **Solución:** Mismo: usar Ollama como default
- **Lección:** Tener siempre un backend local como fallback

### Error 4: "qwen2.5-coder does not support thinking"
- **Síntoma:** `HTTP 400: "qwen2.5-coder:14b" does not support thinking`
- **Causa:** Claude Code v2.1.220 envía parámetro "thinking" por defecto; Qwen no lo soporta
- **Solución:** Descargar `deepseek-r1:8b` que SÍ soporta thinking
- **Lección:** Los modelos de razonamiento (R1, o1) son necesarios para Claude Code

### Error 5: "exceeds the available context size (4096 tokens)"
- **Síntoma:** `HTTP 400: request (6793 tokens) exceeds available context size (4096 tokens)`
- **Causa:** Ollama viene con contexto default de 4096; Claude Code envía ~7K tokens solo en system prompt
- **Solución:** Configurar `OLLAMA_NUM_CTX=32768` + reiniciar Ollama
- **Complicación:** En Windows, Ollama corre como proceso de bandeja, no como servicio
- **Solución final:** Matar proceso + reiniciar con `Start-Process ollama serve` desde sesión con variables

### Error 6: Confusión sobre qué modelo estaba activo
- **Síntoma:** Claude Code decía "Opus 5" pero FCC estaba configurado con Ollama
- **Causa:** Al ejecutar `claude` (no `fcc-claude`), iba directo a Anthropic free tier
- **Solución:** Usar siempre `fcc-claude` para rutear vía FCC
- **Lección:** Verificar qué comando se ejecuta y qué ruta toma

### Error 7: Configuración de permisos en settings.json
- **Síntoma:** `Write(**) is not matched by file permission checks`
- **Causa:** Claude Code v2.1.220 cambió formato de permisos
- **Solución:** Cambiar `Write(**)` por `Edit(**)` en `.claude/settings.json`
- **Lección:** Las herramientas evolucionan; revisar changelogs

### Error 8: Restart-Service no funciona con Ollama
- **Síntoma:** `Restart-Service Ollama` no es comando válido
- **Causa:** Ollama en Windows corre como proceso de bandeja, no como servicio de Windows
- **Solución:** `Stop-Process -Name "ollama" -Force` + `Start-Process ollama serve`
- **Lección:** Verificar cómo está instalado cada servicio antes de intentar gestionarlo

---

## 3. Lecciones Aprendidas

### Lección 1: El free tier de Claude Code es real y útil
**Lo que pasó:** Asumimos que se necesitaba suscripción paga.
**Lo que aprendimos:** Claude Code incluye free tier con Opus 5 (~30-50 mensajes cada 5 horas).
**Cómo contribuyó:** Proporcionó un modelo de alta calidad sin costo mientras configurábamos alternativas locales.

### Lección 2: Ollama + FCC tiene limitaciones de compatibilidad
**Lo que pasó:** Intentamos usar Qwen con Claude Code y falló por "thinking" y contexto.
**Lo que aprendimos:** Claude Code está diseñado para Anthropic API; usarlo con Ollama requiere ajustes (deepseek-r1 + contexto ampliado).
**Cómo contribuyó:** Identificamos que deepseek-r1:8b es el modelo local compatible, y que se necesita `OLLAMA_NUM_CTX=32768`.

### Lección 3: Ruflo es over-engineering para este proyecto
**Lo que pasó:** Consideramos instalar Ruflo (35 plugins) para reducir tokens.
**Lo que aprendimos:** Ruflo NO reduce tokens directamente; solo trackea costos y carga contexto relevante. El framework completo es excesivo.
**Cómo contribuyó:** Postergación documentada (ADR-004). Si se necesita RAG memory, instalar solo `ruflo-rag-memory` y `ruflo-cost-tracker`.

### Lección 4: RHINO-MCP y ROBO-HOPPER requieren Claude Desktop
**Lo que pasó:** Evaluamos instalar MCPs para integración directa con Rhino/Grasshopper.
**Lo que aprendimos:** Ambas herramientas requieren Claude Desktop (no Claude Code CLI). Además, ROBO-HOPPER es beta inestable.
**Cómo contribuyó:** Postergación documentada (ADR-004). Pipeline funcional primero, optimización después.

### Lección 5: Tener múltiples backends da resiliencia
**Lo que pasó:** Z.ai y DeepSeek sin saldo, pero teníamos Ollama como fallback.
**Lo que aprendimos:** Configurar siempre un backend local (gratis) como fallback de los de nube (pagos).
**Cómo contribuyó:** El sistema siguió funcionando aunque las API keys de nube no tuvieran saldo.

### Lección 6: El Admin UI de FCC es poderoso pero confuso
**Lo que pasó:** No quedaba claro qué modelo estaba activo ni cómo enrutar.
**Lo que aprendimos:** El modelo DEFAULT se usa cuando no hay override. Los overrides mapean nombres de Claude a backends específicos.
**Cómo contribuyó:** Configuración clara de enrutamiento (todos los overrides apuntando al mismo modelo para simplificar).

### Lección 7: Las variables de entorno en Windows son engañosas
**Lo que pasó:** Configuramos `OLLAMA_NUM_CTX` a nivel de Usuario pero Ollama no la tomó.
**Lo que aprendimos:** Los procesos que ya están corriendo no leen nuevas variables. Hay que matar y reiniciar.
**Cómo contribuyó:** Procedimiento claro: `Stop-Process` + setear variable en sesión + `Start-Process`.

### Lección 8: El modelo correcto para Claude Code + Ollama
**Lo que pasó:** Probamos qwen2.5-coder, qwen2.5:32b, y todos fallaban.
**Lo que aprendimos:** deepseek-r1:8b es el modelo local compatible con Claude Code porque soporta "thinking".
**Cómo contribuyó:** Identificamos el modelo correcto y lo descargamos.

---

## 4. Archivos Producidos

### 4.1 Scripts de configuración de IA

| Archivo | Función | Resultado |
|---------|---------|-----------|
| `setup-fcc-server.ps1` (v1, obsoleto) | Intentó clonar fcc-server de repos inexistentes | Falló, repos no encontrados |
| `setup-mock-fcc-server.ps1` | Creó servidor FCC manual (Node.js) | Servidor funcional pero limitado |
| `setup-fcc-official.ps1` | Instaló FCC oficial (Alishahryar1/free-claude-code) | FCC 4.16.2 instalado correctamente |
| `setup-claude-code.ps1` | Configuró Claude Code + variables de entorno | Claude Code v2.1.220 operativo |
| `test-claude-code.ps1` | Script de validación end-to-end | Verifica FCC + Ollama + Claude Code |

### 4.2 Configuración de FCC

| Archivo/Componente | Ubicación | Función |
|-------------------|-----------|---------|
| `.env` de FCC | `D:\WORK\AI\fcc-server\.env` | API keys de Z.ai, Gemini, Ollama |
| `start-fcc.ps1` | `D:\WORK\AI\fcc-server\` | Inicia FCC en foreground |
| `start-fcc-bg.ps1` | `D:\WORK\AI\fcc-server\` | Inicia FCC en background |
| Admin UI | http://127.0.0.1:8082/admin | Configuración visual de providers y modelos |
| `settings.json` | `.claude\settings.json` | Permisos y configuración de skills |

### 4.3 Variables de entorno configuradas

| Variable | Valor | Propósito |
|----------|-------|-----------|
| `OLLAMA_HOST` | `127.0.0.1:11434` | URL del servicio Ollama |
| `OLLAMA_MODELS` | `D:\Users\Work\.ollama\models` | Ruta de modelos descargados |
| `OLLAMA_NUM_CTX` | `32768` | Contexto ampliado (32K tokens) |
| `OLLAMA_KEEP_ALIVE` | `24h` | Mantiene modelos en memoria |
| `ANTHROPIC_BASE_URL` | `http://127.0.0.1:8082` | Ruta a FCC (proxy) |
| `ANTHROPIC_API_KEY` | `fcc-local-token` | Token local FCC |
| `RHINO_COMPUTE_URL` | `http://127.0.0.1:6001` | Rhino.Compute headless |
| `DISENO_PARAMETRICO_ROOT` | `D:\WORK\PROJECTS\DiseñoParametrico` | Raíz del proyecto |
| `POT_GPKG_PATH` | `D:\Users\Dario Salas\...bd_uaecd.gpkg` | Ruta al catastro |

### 4.4 Modelos Ollama instalados

| Modelo | Tamaño | Uso recomendado |
|--------|--------|-----------------|
| `qwen2.5-coder:14b` | 9 GB | Código GHPython (no soporta thinking) |
| `qwen2.5:7b` | 5 GB | Tareas rápidas, VRAM limitada |
| `qwen2.5:32b` | 19 GB | Razonamiento profundo (solo si compute apagado) |
| `mistral:latest` | 4 GB | Chat conversacional |
| `codellama:latest` | 4 GB | Alternativo para código |
| `llama3.2:3b` | 2 GB | Emergencia (VRAM llena) |
| `deepseek-r1:8b` | 5 GB | **Modelo compatible con Claude Code** (soporta thinking) |

### 4.5 Documentación de IA

| Archivo | Contenido |
|---------|-----------|
| `README-fcc-claude.md` | Guía completa de FCC + Claude Code |
| `ADR-004-postergar-mcps.md` | Decisión de postergar RHINO-MCP y ROBO-HOPPER |
| `CLAUDE.md` (sección IA) | Reglas de modelos, enrutamiento, fallbacks |
| `CLAUDE-vault.md` | Reglas para editar el vault con IA |

### 4.6 Architect Skills (capa de conocimiento IA)

| Componente | Cantidad | Ubicación |
|------------|----------|-----------|
| Skills | 18 | `.claude/skills/` |
| Calculadoras Python | 7 | `scripts/architect-calculators/` |
| Arquitectos referenciados | 50+ | Dentro de skills |
| Movimientos arquitectónicos | 20+ | Dentro de skills |
| Códigos/estándares | 12+ | IBC, ADA, ASHRAE, Eurocodes, etc. |
| Tipologías documentadas | 28+ | Dentro de skills |

---

## 5. Estado Final y Recomendaciones

### 5.1 Estado actual

```
IA CONFIGURADA:
├── Ollama (7 modelos locales, gratis)         ✅ Operativo
├── FCC 4.16.2 (proxy multi-backend)           ✅ Operativo en puerto 8082
├── Claude Code v2.1.220                       ✅ Instalado
├── Architect Skills (18 skills)               ✅ Instalado
├── API keys de nube (Z.ai, DeepSeek, etc.)    ⚠️ Sin saldo
├── Free tier Anthropic (Opus 5)               ✅ Disponible (limitado)
└── deepseek-r1:8b (compatible con Claude Code) ✅ Descargado

PENDIENTE:
├── Validar deepseek-r1:8b con contexto 32K    ⏳ En progreso
├── Ruflo (postergado, ADR-004)                ⏳ Evaluar después
├── RHINO-MCP (postergado, ADR-004)            ⏳ Evaluar después
└── ROBO-HOPPER (postergado, ADR-004)          ⏳ Evaluar después
```

### 5.2 Estrategia recomendada de uso de IA

```
DESARROLLO DIARIO:
├── Tareas complejas (código, análisis normativo):
│   → claude directo (Anthropic free tier, Opus 5)
│   → ~30-50 mensajes cada 5 horas
│
├── Tareas simples (consultas rápidas):
│   → fcc-claude con deepseek-r1:8b (Ollama local, gratis)
│   → Requiere OLLAMA_NUM_CTX=32768
│
└── Cuando se agote free tier:
    → fcc-claude con Ollama exclusivamente

FUTURO (cuando se justifique):
├── Suscripción Anthropic $20/mes → mensajes ilimitados
├── Recargar Z.ai o DeepSeek → modelos económicos en nube
├── Evaluar Ruflo si se necesita RAG memory
└── Evaluar MCPs si se necesita integración directa Rhino/GH
```

### 5.3 Conclusión

La configuración de IA tiene tres caminos viables:

1. **Free tier de Anthropic** (Opus 5, funciona perfecto, limitado)
2. **Ollama + FCC** (deepseek-r1:8b, gratis, requiere ajustes de contexto)
3. **Combinado** (free tier para complejo, Ollama para simple)

Las herramientas avanzadas (Ruflo, RHINO-MCP, ROBO-HOPPER) quedan postergadas hasta que el pipeline base funcione end-to-end. La decisión está documentada en ADR-004 con justificación completa.

El setup de IA está completo para empezar a trabajar. Las limitaciones actuales (saldo de API keys, compatibilidad Ollama) tienen workarounds funcionales. Cuando el pipeline esté operativo, se pueden evaluar inversiones en suscripciones o herramientas adicionales con datos reales de uso.
