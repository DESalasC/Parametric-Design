# Resumen 2: Configuración del Entorno de Trabajo

**Fecha:** 2026-08-03
**Proyecto:** DiseñoParametrico
**Alcance:** Setup completo del entorno de desarrollo: Windows, Python, estructura de proyecto, Obsidian, Grasshopper, Archicad, y herramientas de exploración.

---

## 1. Puntos Relevantes para Entender el Proceso

### 1.1 El punto de partida

El usuario partió de una máquina Windows 11 Pro (i5-12600K, 64 GB RAM, RTX 4070 Ti 12 GB) con:
- Ollama ya instalado en `D:\Work\AI\ollama\`
- Usuario local `Work` con permisos de administrador
- Dos carpetas de proyecto previas: `DesParametrico` (intentos 1) y `DiseñoParametrico_sistema` (intento 2, más estructurado)

El objetivo era crear un tercer intento limpio, estructurado y documentado.

### 1.2 Las decisiones de arquitectura tempranas

#### Separación binarios vs datos
- **C:\Program Files\** para binarios estándar (Git, Python, Node, Rhino, Archicad)
- **D:\WORK\** para TODO lo que produce valor: vaults, proyectos, modelos, scripts, librerías
- Regla: si se pierde C:\, debe ser recoverable reinstalando. Si se pierde D:\, debe estar en Git.

#### Ollama: no desinstalar
- Ollama estaba en `D:\Work\AI\ollama\` (no estándar pero funcional)
- Modelos en `D:\Users\Work\.ollama\models\` (ubicación por defecto del perfil Work)
- Decisión: mantener, solo configurar variable `OLLAMA_MODELS`

#### Estructura de proyecto por fases
```
src/
├── fase-1-contexto/      (CONTEXTO, LADOS, VECINOS, VALIDADOR)
├── fase-2-demanda/       (DEMANDA, OPTIMIZADOR, PROG_INTERIOR, PROGRAMA_AREAS)
├── fase-3-masa/          (VOLUM, ACCESOS, PREP_LADYBUG)
├── fase-4-ambiental/     (LADYBUG_ANALISIS)
├── fase-5-bim/           (pendiente - MAPEO_TAPIR)
├── interfaces-archicad/
├── components/
└── research/             (GhDefinitionExplorer, GhIoIndexGenerator)
```

### 1.3 La migración de scripts existentes

El usuario tenía dos carpetas de proyecto previas con scripts:

**DesParametrico (intentos iniciales):**
- 7 versiones de CONTEXTO (v03, v04a, v05, v09)
- 2 versiones de CONFIGURAR_LADOS (v02, v04)
- ANALISIS_VECINOS.py
- Scripts utilitarios (validate_ghx, build_canvas_gh, etc.)

**DiseñoParametrico_sistema (arquitectura por capas):**
- layer0_territorial_base (CTX_POT_BOGOATA_v04)
- layer1_territorial_core (LADOS, VECINOS, VALIDADOR)
- layer2_programming_viability (4 scripts de demanda)
- layer3_volumetry (3 scripts de masa)
- layer4_environmental_analysis (LADYBUG_ANALISIS)
- GhDefinitionExplorer (8 scripts de investigación)
- GhIoIndexGenerator (generador de índice)
- 11 definiciones Grasshopper

### 1.4 La nueva nomenclatura

Se estableció: `F{etapa}_{FUNCION}_v{NN}.py`

- F1, F2, F3, F4, F5 = fase
- Versión empieza en v01 (proyecto nuevo)
- Para duplicados: sufijo `_sistema` o `_desparam`

### 1.5 Obsidian como capa de conocimiento

El vault de Obsidian se diseñó con 7 carpetas temáticas:
- `00-index/` — Mapa de conocimiento
- `10-arquitectura/` — ADRs, pipeline, convenciones
- `20-fases/` — Documentación por fase
- `30-referencia/` — APIs externas, normativa, Alexander
- `40-tests/` — Casos de prueba
- `50-lecciones/` — Post-mortems
- `60-diario/` — Daily notes

### 1.6 Plugins de Grasshopper explorados

Se clonaron 3 plugins con sparse checkout (solo .gh/.ghx):
- **Tapir** (ENZYME-APD) — conexión Archicad
- **Ladybug** — análisis ambiental
- **Ladybug Tools** (lbt) — suite moderna

### 1.7 Architect Skills

Plugin de 18 skills + 7 calculadoras Python que aporta:
- Conocimiento de 50+ arquitectos/teóricos
- 50+ métricas cuantitativas
- 28 tipologías edificatorias
- Códigos internacionales (IBC, ADA, ASHRAE)
- Calculadoras de área, U-value, daylight, egress, cargas, energía, costo

---

## 2. Errores Encontrados

### Error 1: ParserError en here-strings de PowerShell
- **Síntoma:** `No characters are allowed after a here-string header but before the end of the line`
- **Causa:** Here-strings `@"..."@` con contenido en la misma línea que la apertura
- **Solución:** Cambiar a `@'...'@` (single-quoted) que no interpreta backticks ni variables
- **Lección:** En PowerShell 7, siempre usar `@'...'@` para contenido Markdown/JSON

### Error 2: Git no inicializado en init-project.ps1
- **Síntoma:** Script fallaba silenciosamente en la sección de Git
- **Causa:** Git no estaba instalado y el script no lo verificaba
- **Solución:** Agregar verificación + instalación automática vía winget + configurar user.name/email
- **Lección:** Siempre verificar dependencias antes de usarlas

### Error 3: pyogrio requiere geopandas
- **Síntoma:** `ImportError: geopandas is required to use pyogrio.read_dataframe()`
- **Causa:** pyogrio delega a geopandas para DataFrames
- **Solución:** `pip install geopandas` + agregar al pyproject.toml
- **Lección:** Las dependencias transitivas no son obvias, siempre probar imports

### Error 4: No se pudo clonar fcc-server
- **Síntoma:** `Repository not found` para JoshuaC215/fcc-server y musistudio/fcc-server
- **Causa:** Los repositorios asumidos no existían o fueron renombrados
- **Solución:** Usuario encontró el repo oficial: `Alishahryar1/free-claude-code`
- **Lección:** Siempre verificar URLs de repos antes de hardcodearlas en scripts

### Error 5: Pylance no resuelve imports
- **Síntoma:** Warnings en VS Code: `Import "click" could not be resolved`
- **Causa:** VS Code no estaba usando el intérprete del .venv
- **Solución:** Seleccionar intérprete `.venv\Scripts\python.exe` en VS Code
- **Lección:** Configurar `python.defaultInterpreterPath` en `.vscode/settings.json`

### Error 6: Warnings LF → CRLF en Git
- **Síntoma:** `warning: LF will be replaced by CRLF the next time Git touches it`
- **Causa:** Git normaliza saltos de línea entre Windows (CRLF) y Unix (LF)
- **Solución:** Crear `.gitattributes` con reglas por tipo de archivo + `git add --renormalize`
- **Lección:** Configurar `.gitattributes` desde el inicio del proyecto

### Error 7: Plugins GH colgándose en git clone
- **Síntoma:** Script se quedó 2 horas clavado en clone de Archicad GH Connection
- **Causa:** URLs inexistentes + git esperando input de credenciales indefinidamente
- **Solución:** Script v2 con timeout de 120s + `GIT_TERMINAL_PROMPT=0`
- **Lección:** Siempre usar timeout en operaciones de red + suprimir prompts interactivos

### Error 8: GhDefinitionExplorer.exe falla en 39/39 archivos
- **Síntoma:** Todos los archivos .gh fallan al procesar
- **Causa probable:** GH_IO.dll no encontrada o Rhino 8 no instalado al momento de ejecutar
- **Estado:** Pendiente de diagnóstico (no crítico para el pipeline principal)
- **Lección:** Las herramientas de investigación son secundarias; priorizar el pipeline principal

### Error 9: Configuración de permisos en settings.json
- **Síntoma:** `Write(**) is not matched by file permission checks`
- **Causa:** Claude Code v2.1.220 cambió el formato de permisos
- **Solución:** Cambiar `Write(**)` por `Edit(**)`
- **Lección:** Las herramientas evolucionan; verificar compatibilidad de configuraciones

---

## 3. Lecciones Aprendidas

### Lección 1: Separar binarios de datos desde el inicio
**Lo que pasó:** Ollama estaba en D: pero los modelos iban a C: por defecto.
**Lo que aprendimos:** Establecer reglas claras: C:\Program Files para binarios, D:\WORK para datos.
**Cómo contribuyó:** Estructura consistente que facilita backups y migraciones.

### Lección 2: DiseñoParametrico_sistema era la base correcta
**Lo que pasó:** Dudosamos entre DesParametrico (CONTEXTO_v09 más reciente) y sistema (arquitectura por capas).
**Lo que aprendimos:** El sistema tenía arquitectura más sólida (5 capas, 15 scripts, ~7,747 líneas).
**Cómo contribuyó:** Migración con base sólida + scripts de fases 2-4 que no existían en DesParametrico.

### Lección 3: La nomenclatura importa
**Lo que pasó:** Los scripts tenían nombres inconsistentes (CONTEXTO_v09, CTX_POT_BOGOATA_v04, ANALISIS_VECINOS).
**Lo que aprendimos:** Establecer `F{etapa}_{FUNCION}_v{NN}.py` desde el inicio.
**Cómo contribuyó:** Navegación clara del pipeline, versionado consistente.

### Lección 4: Obsidian + plugins nativos es suficiente
**Lo que pasó:** Consideramos instalar Graphify como capa adicional de grafo.
**Lo que aprendimos:** Obsidian + Graph View + Dataview + Knowledge Graph Analysis ya cubren todo.
**Cómo contribuyó:** Stack más simple, sin dependencias adicionales.

### Lección 5: Los plugins de GH requieren sparse checkout
**Lo que pasó:** Clonar repos completos de Ladybug/Tapir descargaba GBs innecesarios.
**Lo que aprendimos:** `git sparse-checkout set "*.gh" "*.ghx"` descarga solo definiciones.
**Cómo contribuyó:** 39 archivos relevantes en vez de repos completos de cientos de MB.

### Lección 6: Ruflo es over-engineering para este proyecto
**Lo que pasó:** Consideramos instalar Ruflo (35 plugins, 98 agents).
**Lo que aprendimos:** El problema no era orquestación, era tener pipeline funcional.
**Cómo contribuyó:** Postergación documentada en ADR-004, stack más manejable.

### Lección 7: Siempre validar antes de borrar originales
**Lo que pasó:** Migración de scripts con riesgo de perder trabajo previo.
**Lo que aprendimos:** Copiar (no mover), mantener originales hasta validar.
**Cómo contribuyó:** Cero pérdida de datos durante la migración.

---

## 4. Archivos Producidos

### 4.1 Scripts de setup y configuración

| Archivo | Función | Resultado |
|---------|---------|-----------|
| `setup-env.ps1` | Configura variables de entorno (OLLAMA, RHINO_COMPUTE, etc.) | 6 variables de entorno persistentes |
| `init-project.ps1` | Crea estructura completa del proyecto | 19 carpetas + plantillas + Git inicializado |
| `setup-obsidian.ps1` | Instala Obsidian + crea vault | Vault con 20 carpetas + 5 plugins + Git |
| `fix-pyproject.ps1` | Crea pyproject.toml y requirements.txt | Proyecto Python instalable |
| `fix-git-lf-crlf.ps1` | Configura .gitattributes para saltos de línea | Elimina warnings LF/CRLF |
| `fix-crs-documentation.ps1` | Actualiza docs con CRS correcto | CLAUDE.md + whitelist + ADR-002 actualizados |
| `inventory-existing-project.ps1` | Inventa proyectos existentes | CSV con todos los archivos clasificados |
| `inventory-disenoparametrico-sistema.ps1` | Inventario específico del sistema | 3 CSVs: scripts, GH defs, interfaces |
| `migrate-final.ps1` | Migra scripts con nueva nomenclatura | 15 scripts + 5 utils + 11 GH defs migrados |
| `setup-architect-skills.ps1` | Instala Architect Skills | 18 skills + 7 calculadoras + settings.json |
| `setup-knowledge-repos-v2.ps1` | Migra Alexander + GhDefinitionExplorer + Ruflo | Vault enriquecido + research/ + Ruflo clonado |
| `setup-gh-plugins-explorer-v2.ps1` | Clona plugins GH con timeout | Tapir + Ladybug + LadybugTools clonados |
| `fetch-decreto-555-markdown.py` | Crea estructura Markdown del decreto | 7 archivos MD plantilla |

### 4.2 Estructura de proyecto creada

```
D:\WORK\PROJECTS\DiseñoParametrico\
├── .claude/
│   ├── settings.json          (permisos + skills config)
│   └── skills/                (18 skills Architect)
├── .gitignore
├── .gitattributes
├── .editorconfig
├── .vscode/
│   ├── settings.json
│   └── tasks.json
├── CLAUDE.md                  (reglas del proyecto)
├── README.md
├── pyproject.toml
├── requirements.txt
├── .venv/                     (entorno Python aislado)
│
├── config/
│   └── field-whitelist.json
│
├── data/
│   ├── pot-bogota/            (8 JSONs estructurados)
│   ├── nsr-10/                (3 JSONs estructurados)
│   ├── pot-cache/             (cachés por predio)
│   ├── lotes-ejemplo/
│   └── gdb_fields_inventory.json
│
├── docs/
│   ├── arquitectura/
│   │   ├── pipeline-general.md
│   │   ├── architect-skills-reference.md
│   │   └── decisiones-adr/
│   │       ├── adr-001-uso-tapir.md
│   │       ├── adr-002-catastro-vs-pot.md
│   │       ├── adr-003-elementos-bim-nativos-vs-morphs.md
│   │       └── adr-004-postergar-mcps.md
│   ├── normativa/
│   │   ├── pot-bogota/        (3 Markdowns de decretos)
│   │   └── nsr-10/
│   └── knowledge-base/
│       └── ghx-samples/
│           ├── plugins/        (Tapir, Ladybug, LadybugTools)
│           ├── exports/
│           ├── logs/
│           └── notes/
│
├── src/
│   ├── fase-1-contexto/       (7 scripts GHPython)
│   ├── fase-2-demanda/        (4 scripts)
│   ├── fase-3-masa/           (3 scripts)
│   ├── fase-4-ambiental/      (1 script)
│   ├── fase-5-bim/            (pendiente)
│   ├── interfaces-archicad/
│   ├── components/
│   └── research/
│       ├── gh-definition-explorer/   (subproyecto .NET)
│       └── gh-io-index-generator/    (subproyecto .NET)
│
├── gh-definitions/            (11 definiciones GH migradas)
│
└── scripts/
    ├── utilities/
    │   ├── gpkg-to-cache-v4.py
    │   ├── extract-real-lote.py
    │   ├── inspect-pot-gdb.py
    │   ├── validate-neighbors.py
    │   ├── extract-decreto-555-relevante.py
    │   ├── extract-decreto-670-relevante.py
    │   ├── extract-nsr-10-relevante.py
    │   └── (5 utils migrados)
    └── architect-calculators/  (7 calculadoras Python)
```

### 4.3 Vault de Obsidian

```
D:\WORK\NOTES\obsidian-vault\
├── .obsidian/
│   └── plugins/
│       ├── dataview/
│       ├── knowledge-graph-analysis/
│       ├── obsidian-admonition/
│       ├── obsidian-git/
│       └── templater-obsidian/
├── 00-index/
│   └── mapa-conocimiento.md
├── 10-arquitectura/
│   └── decisiones-adr/
├── 20-fases/
├── 30-referencia/
│   ├── christopher-alexander/
│   ├── gh-io-docs/
│   ├── grasshopper-plugins/
│   ├── nsr-10/
│   ├── pot-bogota/
│   └── tapir-api/
├── 40-tests/
├── 50-lecciones/
├── 60-diario/
├── assets/
├── CLAUDE.md
├── README.md
└── .gitignore
```

### 4.4 Librerías

```
D:\WORK\LIBRARIES\
└── bim/
    ├── tapir-archicad/
    └── gh-archicad-interface/
```

### 4.5 Otros componentes

| Componente | Ubicación | Estado |
|------------|-----------|--------|
| Ollama + 8 modelos | D:\Work\AI\ollama\ + D:\Users\Work\.ollama\models\ | ✅ Operativo |
| FCC Server 4.16.2 | D:\WORK\AI\fcc-server\ (instalado vía npm) | ✅ Operativo (puerto 8082) |
| Claude Code v2.1.220 | Instalado global | ✅ Operativo con Nemotron (tool use) |
| Ruflo | D:\WORK\AI\ruflo\ (clonado, sin configurar) | ⏳ Pendiente |
| Rhino 8 | Instalado | ✅ Operativo |
| Archicad | Instalado | ✅ Operativo |
| Tapir (plugin) | Instalado en Archicad + GH | ✅ Conectado |
| .NET SDK | Instalado (para GhDefinitionExplorer) | ✅ Disponible |

---

## 5. Validación del Entorno de Desarrollo IA

Una vez configurado el stack, se procedió a validar la capacidad de Claude Code + Nemotron (vía FCC) para realizar tareas de desarrollo reales (tool use).

### 5.1 Descubrimiento de limitaciones en modelos locales

- **DeepSeek R1 / Qwen:** Aunque soportan "thinking", rompen el "tool use" (capacidad de leer archivos y ejecutar comandos) cuando se usan a través de FCC. Generan texto pero no pueden interactuar con el sistema de archivos.
- **Contexto limitado:** Ollama venía configurado con 4096 tokens de contexto por defecto, insuficiente para el system prompt de Claude Code (~7K tokens). Se solucionó configurando `OLLAMA_CONTEXT_LENGTH=32768`.
- **Alucinaciones por contexto largo:** Los modelos locales tienden a alucinar cuando la conversación crece. La solución es usar el comando `/clear` frecuentemente y confiar en los archivos `.md` (CLAUDE.md) como memoria persistente, no en el historial del chat.

### 5.2 Solución: Nvidia NIM (Nemotron)

El modelo `nvidia_nim/nvidia/nemotron-3-super-120b-a12b` demostró ser la opción ideal:
- Soporta "thinking" (razonamiento previo a la respuesta).
- Mantiene el "tool use" funcional (puede leer, escribir y ejecutar archivos).
- Es 100% gratuito (con límites de cuota en horas pico).

### 5.3 Adaptación de Scripts GHPython (Fase 1)

Utilizando Nemotron, se adaptaron exitosamente los 3 scripts principales de la Fase 1 para que lean de los JSONs estructurados en lugar de usar valores hardcodeados:

1. **F1_CONTEXTO_POT_v01.py:**
   - Adapta lectura de coordenadas, datos del POT y catastro desde el JSON.
   - Implementa lógica de inferencia de altura máxima (en pisos) basada en el rango de edificibilidad cuando el dato crudo del POT es nulo o incoherente (ver ADR-005).
   - Mantiene compatibilidad con IronPython 2.7.

2. **F1_LADOS_CONFIGURAR_v01.py:**
   - Lee los retiros del Decreto 555/2021 desde el JSON.
   - Implementa lógica de tipología edificatoria: asigna 0.0m de retiro lateral en tipología "Continua" y 3.0m en "Aislada".

3. **F1_VECINOS_ANALISIS_v01.py:**
   - Implementa la tabla A.6.5-1 del NSR-10 (separaciones sísmicas).
   - Calcula la separación sísmica requerida según el número de pisos y coincidencia de losas.
   - Compara la separación sísmica con el retiro urbanístico del POT y se queda con el valor mayor (regla de oro).

---

## 6. Conclusión

El entorno de trabajo quedó configurado completamente y **validado como herramienta de desarrollo activa**:

- ✅ **Windows 11 Pro** con usuario `Work` administrador
- ✅ **Python 3.12** en venv aislado con todas las dependencias
- ✅ **Git** con `.gitattributes` y `.gitignore` configurados
- ✅ **Estructura de proyecto** por fases (F1-F5) con 15 scripts migrados
- ✅ **Obsidian** con 5 plugins y vault estructurado (7 carpetas temáticas)
- ✅ **Architect Skills** (18 skills + 7 calculadoras Python)
- ✅ **GhDefinitionExplorer + GhIoIndexGenerator** migrados como research
- ✅ **Plugins GH** clonados (Tapir, Ladybug, LadybugTools)
- ✅ **Marco Alexander** migrado al vault
- ✅ **Rhino 8 + Archicad + Tapir** instalados y conectados
- ✅ **5 ADRs** documentando decisiones arquitectónicas (incl. corrección altura POT)
- ✅ **Documentación normativa** completa (3 decretos + NSR-10)
- ✅ **IA Operativa:** Claude Code + Nemotron (FCC) con tool use funcional
- ✅ **Fase 1 Adaptada:** Scripts GHPython leyendo datos reales de JSONs estructurados (POT, NSR-10, Catastro)
