# CLAUDE.md — Proyecto DiseñoParametrico

> **Nota:** Este archivo debe ir en `D:\WORK\PROJECTS\DiseñoParametrico\CLAUDE.md`
> Es generado automáticamente por `init-project.ps1`. Esta es la plantilla maestra.

## Contexto del proyecto
Ecosistema BIM-GIS-AI para diseño arquitectónico paramétrico en Bogotá.
Automatiza: geolocalización POT, matriz de retiros, separaciones NSR-10, motor de demanda, generación de masa y inyección BIM nativa.

## Stack
- **CAD/BIM**: Rhino 8 + Grasshopper + Archicad
- **Puente geométrico**: Rhino.Compute headless (puerto 6001) + Hops
- **Conexión BIM**: Tapir (Grasshopper-Archicad Live Connection)
- **IA local**: Ollama (qwen2.5-coder:14b primario, qwen2.5:7b si compute activo)
- **Orquestador**: Claude Code vía fcc-server (puerto 8787)
- **Conocimiento**: Obsidian + Graphify
- **Python**: 3.12 externo, IronPython 2.7 en GHPython

## Hardware del sistema
- CPU: Intel i5-12600K (10 cores)
- RAM: 64 GB
- GPU: NVIDIA RTX 4070 Ti (12 GB VRAM)
- OS: Windows 11 Pro 25H2
- Usuario: `Work` (administrador local)

## Reglas obligatorias

### Normativa
1. Toda referencia POT debe citar el **Decreto 555 de 2021** y consultar el `.gpkg` de la geobase Bogotá.
2. Toda referencia NSR-10 debe citar el **Título y sección** (ej: NSR-10 A.2.5).
3. Coordenadas: **MAGNA-SIRGAS Origen Bogotá** (EPSG:9377).
4. Aplicar **desfase virtual** si se compara con origen local (0,0,0) de Archicad.

### Grasshopper / GHPython
5b. Unidades de Rhino configuradas en METROS. Nunca usar milímetros (mm) en Grasshopper o el área se calculará 1,000,000 de veces mayor.
5. Entradas JSON a GHPython: `No Type Hint` + `Item Access`.
6. Entradas geométricas a GHPython: `List Access` + `Flatten`.
7. Lotes deben ser **polilíneas (LineSegments)**, no NURBS.
8. No usar APIs online (epsg.io, IDECA) dentro de GHPython; usar `data/` local.
9. Si una entrada falla, usar valor por defecto (retiro 3.0m) y loggear warning.

### Código Python
10. Todo script GHPython nuevo requiere test antes de merge.
11. Todo script va en `src/fase-N-<nombre>/` con fixture en `tests/`.
12. Convención de命名: `MAYUS_FASE_VERBO_vNN.py` (ej: `F1_CONTEXTO_v09.py`).
13. Python externo: type hints obligatorios, ruff, mypy.
14. GHPython: sin type hints (IronPython 2.7).

### Datos
15. Archivo POT fuente: `D:\Users\Dario Salas\proyectos\DesParametrico\2-Entradas\Datos_Sitio_GDB\bd_uaecd.gpkg`
16. Caché POT: `data/pot-cache/<predio-id>.json` (generado por `gpkg-to-cache.py`).
17. Whitelist de campos: `config/field-whitelist.json` (~30 campos de 2455 totales).
18. Vecinos: modelado manual en Archicad (Morph), validar con `validate-neighbors.py` antes de pasar a GH.

### Modelos IA
19. Modelo primario: `qwen2.5-coder:14b` (9 GB VRAM).
20. Si Rhino.Compute activo: cambiar a `qwen2.5:7b` (5 GB VRAM) para no saturar.
21. Fallback emergencia: `llama3.2:3b`.
22. Claude Code enruta vía fcc-server en `http://127.0.0.1:8787`.
23. **Ubicación de modelos**: `D:\Users\Work\.ollama\models\` (por defecto de Ollama con perfil Work en D:). Variable `OLLAMA_MODELS` apunta ahí.

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
├── docs/                  # Documentación técnica y normativa
│   ├── arquitectura/      # ADRs, pipeline general
│   ├── normativa/         # POT, NSR-10
│   └── api-referencia/    # Tapir, GH_IO, rhino3dm
├── scripts/               # Scripts standalone
│   ├── rhino-compute/     # start/stop/health-check
│   ├── ollama/            # pull-models, list-models
│   └── utilities/         # gpkg-to-cache, validate-neighbors
├── src/                   # Código fuente por fase
│   ├── fase-1-contexto/   # CONTEXTO, CONFIGURAR_LADOS, ANALISIS_VECINOS
│   ├── fase-2-demanda/    # MOTOR_DEMANDA (pendiente)
│   ├── fase-3-masa/       # VOLUMEN (pendiente)
│   └── fase-4-bim/        # mapeo-tapir (pendiente)
├── gh-definitions/        # Definiciones .gh
├── data/                  # Datos POT, vecinos, lotes
│   ├── pot-geojson/       # .gpkg original (no commitear)
│   ├── pot-cache/         # JSON por predio (generado)
│   ├── nsr-10/            # Tablas NSR-10
│   ├── neighbors/         # Vecinos .3dm o .json
│   └── lotes-ejemplo/     # Lotes de prueba
├── tests/                 # Tests con fixtures
├── exports/               # Salidas (no commitear)
├── config/                # Config (field-whitelist.json)
└── .vscode/               # Config VS Code
```

## Limitaciones conocidas
- **Vecinos**: modelado manual (no hay modelo 3D público de Bogotá).
- **Lotes curvos**: NO soportados en `ANALISIS_VECINOS` (requiere polilínea).
- **POT**: 191 campos en `.gpkg`, solo ~30 relevantes (ver `config/field-whitelist.json`).
- **Altura POT**: El campo `ALTURA` en la capa `Area_elevacion_maxima` del .gdb NO es altura de edificación en metros. Es cota absoluta o código. El script lo deja como `null` y guarda el crudo en `altura_maxima_raw`. La altura real se define en pisos en el Decreto 555/2021.
- **IronPython en GH**: sin `requests`, `fiona`, `geopandas`. Usar `System.Net` para HTTP si imprescindible.
- **Rhino.Compute + Ollama en paralelo**: con 12 GB VRAM, cambiar a `qwen2.5:7b` cuando compute esté activo.
- **IA Local (Nemotron/DeepSeek)**: Tienen memoria corta. Si el contexto de la conversación crece demasiado, alucinan. Usar `/clear` frecuentemente al cambiar de tarea. No confiar en la memoria del chat; toda instrucción crítica debe estar en este archivo (`CLAUDE.md`) o en archivos `.md` que el modelo pueda leer.

## Fases del proyecto
- [x] **Fase 1**: Contexto POT + retiros + vecinos (en revisión, reforzar tests)
- [ ] **Fase 2**: Motor de demanda (`MOTOR_DEMANDA.py`)
- [ ] **Fase 3**: Generación de masa (`VOLUMEN_v04.py`)
- [ ] **Fase 4**: Inyección BIM nativa (`mapeo-tapir.py`)

## Referencias clave
- **POT Bogotá**: Decreto 555 de 2021
- **NSR-10**: Reglamento Colombiano de Construcción Sismo Resistente
- **Tapir**: https://github.com/ogix/Tapir (verificar URL oficial)
- **Grasshopper-Archicad Live Connection**: Graphisoft
- **Geobase Bogotá**: https://geobogota.maps.arcgis.com/
- **MAGNA-SIRGAS Origen Bogotá**: EPSG:9377

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


