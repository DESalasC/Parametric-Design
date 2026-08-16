# CLAUDE.md — Proyecto DiseñoParametrico

> **Nota:** Este archivo debe ir en `D:\WORK\PROJECTS\DiseñoParametrico\CLAUDE.md`
> Es generado automáticamente por `init-project.ps1`. Esta es la plantilla maestra.

## Contexto del proyecto
Ecosistema BIM-GIS-AI para diseño arquitectónico paramétrico en Bogotá.
Automatiza: geolocalización POT, matriz de retiros, separaciones NSR-10, motor de demanda, generación de masa y inyección BIM nativa.

## Stack
- **CAD/BIM**: Rhino 8 + Grasshopper + Archicad
- **Puente geométrico**: Rhino.Compute headless (puerto 6001) + Hops
- **Conexión BIM**: Grasshopper–ArchiCAD Live Connection (plugin Graphisoft; sus componentes son AC_*). El API de comandos usa el protocolo JSON **Tapir** (paquete Python `archicad`, puerto CommandConnection 19723 → 19724 en este equipo).
- **IA local**: Ollama (qwen2.5-coder:14b primario, qwen2.5:7b si compute activo)
- **Orquestador**: Claude Code vía fcc-server (puerto 8787)
- **Conocimiento**: Obsidian + Graphify
- **Python**: 3.12 externo, IronPython 2.7 en GHPython (componente "Script" clásico, NO "Python 3 Script")

## Hardware del sistema
- CPU: Intel i5-12600K (10 cores)
- RAM: 64 GB
- GPU: NVIDIA RTX 4070 Ti (12 GB VRAM)
- OS: Windows 11 Pro 25H2
- Usuario: `Work` (administrador local)

## Reglas obligatorias

### GHPython
5. **⚠️ NO usar el componente "Python 3 Script" de Grasshopper (Rhino 8).**
   El componente "Python 3 Script" tiene un bug documentado en Rhino 8: pierde
   el reconocimiento del tipo de lenguaje, sellando el componente sin posibilidad
   de edición. Han ocurrido 3 fallas en 2 días que obligan a reconstruir todos
   los componentes desde cero.
   ✅ **Usar SIEMPRE el componente "Script"** (el clásico) y seleccionar
   **IronPython 2.7** como lenguaje. Es mucho más estable en este contexto.
6. Los scripts GHPython DEBEN ser compatibles con IronPython 2.7:
   - NO usar f-strings → usar `.format()` o `%`
   - NO usar `pathlib` → usar `os.path`
   - NO usar type hints → quitarlos
   - NO usar `:=` (walrus operator)
   - Usar `globals().get()` para acceder a variables del canvas
   - **NO incluir shebang (`#! /usr/bin/env python3`)** al inicio —
     confunde al detector de lenguaje del componente "Script" y produce
     "Can not determine language", sellando el componente

### ArchiCAD Layers
7. **Capas para clasificación de entorno** (creadas desde Grasshopper vía Live Connection):
   - `00-00-10_Lote_proyecto` — Predio objetivo
   - `00-20-20_Elementos_entorno_urbano` — Polígonos de vías
   - `00-20-30_Ejes_vias` — Ejes de vías (líneas centrales)
   - `70-50-10_Zonas_verdes_publicas` — Parques, plazas y zonas verdes
   - `70-30-20_Andenes_preexistentes` — Andenes y espacio público peatonal
   - `10-20-10_Topografia` — Curvas de nivel y puntos topográficos
   - `70-20-20_Perimetros_vecinos` — Perímetros de predios vecinos
   - `70-20-30_Volumetrias_vecinas` — Morphs de construcciones existentes en predios vecinos (manual)
   - `00-10-20_Elementos_referencia` — Líneas de referencia y ejes auxiliares

### Pipeline Fase 1 — Dos Etapas (v26)

#### ETAPA 1: Datos en bruto → ArchiCAD (clasificación manual)
```
fetch-urban-context-v6 → JSON → F1_ETAPA1_CONTEXTO (GH Python)
  → lot_curve, vecinos_curves, vias_oficiales, espacios_publicos
  → Live Connection: crear layers + enviar geometría a ArchiCAD
  → MANUAL en ArchiCAD: clasificar lotes de vías, ejes, andenes,
    zonas verdes, predios vecinos en layers especiales
  → MANUAL: construir volumetrías existentes de vecinos (Morph)
```

#### ETAPA 2: Geometría clasificada → ocupación y patios
```
ArchiCAD (layers clasificados) → Live Connection GetElements → GH
  → F1_ETAPA2_LADOS: clasificar lados según capas
  → F1_ETAPA2_PATIO: patios según colindancias reales
  → F1_ETAPA2_NORMATIVA: ocupación + envolvente (GFA total = ocupación_real × pisos_finales)
  → F1_OVERRIDE_USO (opcional): override de uso del operador (USO-MULTIPLE)
  → F1_EXPORTAR_GFA: escribe data/fase-2-demanda/<CHIP>-gfa-gh.json (auto, sin toggle)
  → Fase 2: F2_DEMANDA_MOTOR_v03 / F2_RENTA_MOTOR_v03 (leen el GFA si no se pasa --gfa)
```

### Normativa
1. Toda referencia POT debe citar el **Decreto 555 de 2021** y consultar el `.gpkg` de la geobase Bogotá.
2. Toda referencia NSR-10 debe citar el **Título y sección** (ej: NSR-10 A.2.5).
3. Coordenadas: **MAGNA-SIRGAS Origen Bogotá** (EPSG:9377).
4. Aplicar **desfase virtual** si se compara con origen local (0,0,0) de Archicad.

### Clasificación Espacial Híbrida (ADR-008)
5. **NO confiar ciegamente en datos oficiales.** La geodatabase del POT tiene huecos (calles no digitalizadas, alturas de vecinos faltantes).
6. **Regla de clasificación de frentes**: Un borde del lote es "Frontal" si la distancia a CUALQUIER curva de vía es < 15 metros. Si no hay vía cerca, es "Lateral" o "Posterior".
7. **Feedback Loop ArchiCAD ↔ Grasshopper**: Las vías se obtienen de DOS fuentes combinadas con Merge en GH:
   - `vias_oficiales`: del JSON (capa Eje_vial del POT)
   - `vias_manuales`: dibujadas en ArchiCAD en capas `00-20-20_Elementos_entorno_urbano_preexistente`, `70-30-20_Andenes_preexistentes`, `70-50-10_Zonas_verdes_publicas`
8. **Ortofoto de referencia**: Usar `fetch-aerial-photo-v6.py` para obtener imagen satelital. Colocar en capa `00-20-20_Foto_Aerea_Referencia` (50% transparencia) para verificar alineación.
8b. **Curvas con arcos de la Live Connection**: el Deconstruct 2D Polyline emite el tipo del plugin "Planar Curve" (polilínea con segmentos curvos) que NO tiene ClosestPoint y los scripts GHPython lo rechazan (vías/vecinos/EP rectos emiten "Polyline Curve" nativa y funcionan). Normalizar a curva nativa (componente Curve de GH directo tras el Deconstruct, o Divide Curve + Polyline) o dibujar los elementos como polilíneas rectas en ArchiCAD. Los scripts manejan arcos sin problema una vez la curva es nativa de Rhino.

### Grasshopper / GHPython
9. Unidades de Rhino configuradas en METROS. Nunca usar milímetros (mm).
10. Script normativo vigente: `F1_ETAPA2_NORMATIVA_v05.py` + `F1_ETAPA2_LADOS_v04.py` (pipeline modular v26, regla híbrida 15m, regla Posterior N-1, Anexo 5 POT actualizado por Decreto 466/2024, ancho de vía medido entre andenes).
    El linaje legacy (`F1_NORMATIVA_APLICAR_*`, `F1_CONTEXTO_POT_*`, `F1_LADOS_CONFIGURAR_*`,
    `F1_LADOS_CLASIFICAR_*`, patios viejos, `F1_PATIO_DISCONTINUIDAD_*`, `F1_VECINOS_ANALISIS_*`,
    `F1_VALIDADOR_CRUZADO_v01`, `F1_DESPLAZAR_ORIGEN_v01`, `F1_VERTICE_CERCANO_v01`) está
    archivado en `src/fase-1-contexto/_legacy/` (2026-08-15).
    Pipeline Fase 1: `F1_ETAPA1_CONTEXTO_v02` → `F1_ETAPA2_LADOS_v04` → `F1_ETAPA2_PATIO_v02`
    → `F1_ETAPA2_NORMATIVA_v05` → (`F1_OVERRIDE_USO_v01` opcional) → `F1_EXPORTAR_GFA_v02`
    → `data/fase-2-demanda/<CHIP>-gfa-gh.json` → motores F2 v03 (hook `--gfa` opcional).
    v05: retiros por clasificación + tipología (Continua/Aislada) + antejardín por ancho de
    vía (mapa CU-5.5 / regla histórica, override `antejardin_m`) + posterior tabla
    Consolidación por pisos + empate volumétrico (`empate_posterior_pisos`). Capas:
    `F1_LAYERS_XML_v02` (merge defensivo de capas críticas, garantiza
    `00-00-10_Lote_proyecto`) y ETAPA1 v02 expone `layer_lote_ok`.

### PROHIBIDO usar 
11. Rhinoscriptsyntax (rs) en scripts GHPython. Usar exclusivamente Rhino.Geometry (rg).
12. Entradas JSON a GHPython: `No Type Hint` + `Item Access`.
13. Entradas geométricas a GHPython: `List Access` + `Flatten`.
14. Lotes deben ser **polilíneas (LineSegments)**, no NURBS.
15. No usar APIs online dentro de GHPython; usar `data/` local.
16. Si una entrada falla, usar valor por defecto y loggear warning.
17. Prohibido usar coordenadas globales (SIRGAS) como input directo en GH/ArchiCAD.

### Código Python
13. Todo script GHPython nuevo requiere test antes de merge.
14. Todo script va en `src/fase-N-<nombre>/` con fixture en `tests/`.
15. Convención de 命名: `MAYUS_FASE_VERBO_vNN.py` (ej: `F1_CONTEXTO_v09.py`).
16. Python externo: type hints obligatorios, ruff, mypy.
17. GHPython: sin type hints (IronPython 2.7).
18. La adquisición del lote se hace mediante el CHIP del predio usando el script scripts/utilities/fetch-urban-context-v6.py.
19. El script genera un JSON en 'data/pot-cache/<CHIP>-contexto.json' con coordenadas locales (0,0,0) + metadatos SIRGAS + topografía.
20. Los scripts GHPython de la Fase 1 SOLO deben leer este JSON. Si el JSON no existe, el pipeline debe detenerse e indicar al usuario que ejecute el script de fetch primero.
21. La topografía maneja dos estados: 'ESTIMADA' (raster público) y 'REAL' (levantamiento). El sistema debe actualizarse dinámicamente cuando el estado cambie a REAL.

### Datos
22. Archivo POT fuente: `D:\Users\Dario Salas\proyectos\DesParametrico\2-Entradas\Datos_Sitio_GDB\bd_uaecd.gpkg`
23. Caché POT: `data/pot-cache/<predio-id>.json` (generado por `gpkg-to-cache.py`).
24. Whitelist de campos: `config/field-whitelist.json` (~30 campos de 2455 totales).
25. Vecinos: modelado manual en Archicad (Morph), validar con `validate-neighbors.py` antes de pasar a GH.

### Modelos IA
26. Modelo primario: `qwen2.5-coder:14b` (9 GB VRAM).
27. Si Rhino.Compute activo: cambiar a `qwen2.5:7b` (5 GB VRAM) para no saturar.
28. Fallback emergencia: `llama3.2:3b`.
29. Claude Code enruta vía fcc-server en `http://127.0.0.1:8787`.
30. **Ubicación de modelos**: `D:\Users\Work\.ollama\models\` (por defecto de Ollama con perfil Work en D:). Variable `OLLAMA_MODELS` apunta ahí.

## Comandos útiles

```powershell
# Servicios
powershell scripts\rhino-compute\start-compute.ps1
powershell scripts\rhino-compute\stop-compute.ps1
powershell scripts\rhino-compute\health-check.ps1

# POT
python scripts\utilities\gpkg-to-cache.py --lot data\lotes-ejemplo\lote-chapinero.json
python scripts\utilities\gpkg-to-cache.py --list-layers
python scripts\utilities\gpkg-to-cache.py --show-fields <layer_name> --limit 1

# Vecinos
python scripts\utilities\validate-neighbors.py --input data\neighbors\vecinos.3dm

# Tests
pytest src\fase-1-contexto\tests\
pytest --cov=src --cov-report=term-missing

# Git
git add -A
git commit -m "tipo: descripcion"
git push
```

## Estructura del proyecto
```
DiseñoParametrico/
├── README.md / CLAUDE.md      # Overview vivo + reglas (documentación detallada en el vault)
├── config/                    # field-whitelist.json
├── data/                      # Única raíz de datos
│   ├── pot-cache/             # JSON por predio + ortofotos (gitignored parcial)
│   ├── fase-2-demanda/        # JSON de entrada del pipeline (actual + gfa1054)
│   ├── pot-bogota/ nsr-10/    # Normativa estructurada
│   ├── ghx-samples/           # Corpus GHX (regenerable, gitignored)
│   └── lotes-ejemplo/ clima/ ideca-cache/ neighbors/ pot-geojson/
├── gh-definitions/            # F1_Contexto_Base-Editado_v01 (maestro) + referencias; _archive\
├── scripts/                   # rhino-compute/ + utilities/
├── src/                       # Código por fase
│   ├── fase-1-contexto/       # Modular ETAPA1/ETAPA2 vigente + _legacy\
│   ├── fase-2-demanda/        # Pipeline + F2_Modelo_Financiero\ (motor v3.0) + F2_Modelo_Renta\ (motor v3.0) — hook GFA desde F1
│   ├── fase-3-masa/           # VOLUM_GENERADOR v03, ACCESOS, PREP_LADYBUG
│   ├── fase-4-ambiental/      # F4_LADYBUG_ANALISIS v02
│   ├── fase-5-bim/            # Pendiente
│   ├── interfases-archicad/   # F1_Layers_Proyecto_v01.xml (único)
│   └── research/              # Exploración C# (GhDefinitionExplorer) — módulo independiente
├── tests/                     # Pytest (Fase 1)
├── exports/ logs/ LIBRARIES/ inventario_migracion/
└── .venv/ pyproject.toml requirements.txt
```

> **Documentación:** la única fuente de documentación es el vault de Obsidian
> `D:\Work\NOTES\obsidian-vault\` (índice: `00-index\mapa-conocimiento.md`). Ya no existe `docs/`
> en el proyecto; todo se migró al vault el 2026-08-13. El nombre oficial del proyecto es
> `DiseñoParametrico` (con ñ); usarlo consistentemente en toda la documentación.

## Limitaciones conocidas
- **Vecinos**: modelado manual (no hay modelo 3D público de Bogotá).
- **Lotes curvos**: NO soportados en `ANALISIS_VECINOS` (requiere polilínea).
- **POT**: 191 campos en `.gpkg`, solo ~30 relevantes (ver `config/field-whitelist.json`).
- **Altura POT**: El campo `ALTURA` en la capa `Area_elevacion_maxima` del .gdb NO es altura de edificación en metros. Es cota absoluta o código. El script lo deja como `null` y guarda el crudo en `altura_maxima_raw`. La altura real se define en pisos en el Decreto 555/2021.
- **IronPython en GH**: sin `requests`, `fiona`, `geopandas`. Usar `System.Net` para HTTP si imprescindible.
- **Rhino.Compute + Ollama en paralelo**: con 12 GB VRAM, cambiar a `qwen2.5:7b` cuando compute esté activo.
- **IA Local (Nemotron/DeepSeek)**: Tienen memoria corta. Si el contexto de la conversación crece demasiado, alucinan. Usar `/clear` frecuentemente al cambiar de tarea. No confiar en la memoria del chat; toda instrucción crítica debe estar en este archivo (`CLAUDE.md`) o en archivos `.md` que el modelo pueda leer.

## Fases del proyecto
- [x] **Fase 0**: Setup BIM (capas ArchiCAD)
- [x] **Fase 1**: Contexto POT + retiros + vecinos (clasificación híbrida ADR-008, pipeline modular v26)
- [x] **Fase 2**: Motor de demanda + modelo financiero de prefactibilidad (`F2_Modelo_Financiero`, v3.0: KPIs, alertas, sensibilidad, escenarios D/E, flujo de caja, hook GFA desde F1) + **modelo Build-to-Rent** (`F2_Modelo_Renta`, v3.0: construir para arrendar CP/LP, TIR/VPN/cap rate, suelo soportable, hook GFA desde F1)
- [~] **Fase 3**: Generación de masa (`VOLUM_GENERADOR`, `ACCESOS_INTEGRADOR`, `PREP_LADYBUG`)
- [~] **Fase 4**: Análisis ambiental (Ladybug + EPW Bogotá)
- [ ] **Fase 5**: Inyección BIM nativa (ArchiCAD API / protocolo Tapir → ArchiCAD)

## Referencias clave
- **POT Bogotá**: Decreto 555 de 2021
- **NSR-10**: Reglamento Colombiano de Construcción Sismo Resistente
- **Tapir**: protocolo JSON-RPC del ArchiCAD API (archicadapi.graphisoft.com); lo usa el paquete Python `archicad` de Graphisoft. NO es nombre genérico de los componentes de Grasshopper — cada plugin lleva su nombre (Live Connection, LadyBug, etc.).
- **Geobase Bogotá**: https://geobogota.maps.arcgis.com/
- **MAGNA-SIRGAS Origen Bogotá**: EPSG:9377
- **ADR-008**: Clasificación Espacial Híbrida (feedback loop ArchiCAD↔GH, regla 15m)

## Estándar de documentación para scripts GHPython

Todo script Python para Grasshopper debe incluir en su encabezado:

1. **Propósito**: Qué hace el script y por qué existe (2-3 líneas).
2. **Normativa aplicable**: Referencia a decretos, artículos o fichas reglamentarias.
3. **Historial de versiones**: `vXX — qué cambió` en orden cronológico inverso.
4. **Tabla de entradas**: Nombre, Tipo (Curve/String/Number/int), Acceso (Item/List), Descripción y procedencia (de qué componente viene).
5. **Tabla de salidas**: Nombre, Tipo, Descripción.
6. **Tabla de funciones internas**: Nombre, Descripción (qué hace, no cómo).

Formato de versión: `v<major>.<minor>` donde major = cambio de lógica, minor = solo documentación/formato.
Los números de versión en el nombre de archivo reflejan la versión actual (ej: `_v03.py`).

Ejemplo de referencia: `F1_NORMATIVA_APLICAR_v22.py` (v22.6) y `F1_PATIO_VECINO_v04.py` (v04).

## Regla de retiros y patios: lógica vecino vs calle

**Principio fundamental:** Los aislamientos y patios aplican solo a linderos con predios
vecinos, NO a frentes de calle o espacio público. La calle ya provee ventilación.

1. **Clasificación de lados:**
   - Lado "Frontal" = colinda con vía → retiro frontal normativo (3-5m según tipo de vía)
   - Lado "Publico" = colinda con espacio público → sin aislamiento.
   - Lado "Lateral" = colinda con vecino → aislamiento según tipología (0m para Continua, 3m para Aislada)

2. **Patios de aislamiento:**
   - Se generan en vértices donde convergen DOS lados vecinos (no calles)
   - Vértice Calle+Calle → sin patio
   - Vértice Calle+Vecino → sin patio
   - Vértice Vecino+Vecino → PATIO REQUERIDO

3. **Tamaño del patio:**
   - Lotes < 500 m² + Continua + ≤ 5 pisos: 3.0m × 3.0m fijo
   - Regla general: max(3.0, altura_total × 0.25) m por lado

4. **Implementación (pipeline modular actual):**
   - `F1_ETAPA2_LADOS_v04` clasifica lados por colindancia real (vía/EP/vecino),
     asigna Posterior SOLO si todos los lados menos uno colindan con vecinos,
     y mide el ancho de vía entre andenes (capa 70-30-20)
   - `F1_ETAPA2_PATIO_v02` detecta vértices vecino-vecino y genera rectángulos
   - `F1_ETAPA2_NORMATIVA_v05` aplica retiros diferenciados (tipología + antejardín
     por ancho de vía + posterior tabla Consolidación) y resta todos los patios

## Cuándo preguntar al usuario
- Cambios arquitectónicos mayores (nuevo stack, cambiar de plugin).
- Modificar el `.gpkg` fuente o la whitelist de campos.
- Eliminar archivos o carpetas del proyecto.
- Decisiones de licenciamiento de software.

## Cuándo decidir autónomamente
- Refactors internos que no cambian API pública.
- Nuevos tests.
- Ajustes de naming siguiendo convención.
- Mejoras de documentación en el vault.
- Actualización de dependencias menores (patch versions).



