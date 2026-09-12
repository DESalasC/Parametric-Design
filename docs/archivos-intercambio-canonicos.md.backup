# Archivos de intercambio canónicos (canvas ↔ orquestador ↔ motores)

Versión: 2026-08-23 (madrugada). Regla del canvas: **nombres literales `CHIP`/`CASO`**
para los archivos que el canvas lee/escribe; el orquestador sobreescribe el activo al
seleccionar y conserva el archivo por-CHIP como historial. `<CHIP>` = código catastral
(p. ej. `AAA0240ZXJH`); `<CASO>` = A | B | B_SALUD | C.

## Activos (el canvas lee/escribe estos — nombre literal)

| ID | Activo (canvas) | Archivo por CHIP/CASO (historial) | Productor → Consumidor |
|---|---|---|---|
| `contexto` | `data/pot-cache/CHIP-contexto.json` | `data/pot-cache/<CHIP>-contexto.json` | `fetch-urban-context-v6.py` → orquestador copia → `F1_ETAPA1_CONTEXTO_v02.json_path` |
| `vecinos_por_lado` | `data/pot-cache/CHIP-vecinos-por-lado.json` | `data/pot-cache/<CHIP>-vecinos-por-lado.json` | `vecinos_por_lado.py` → orquestador copia (con confirmaciones) → NORMATIVA |
| `gfa_gh` | `data/fase-2-demanda/CHIP-gfa-gh.json` | `data/fase-2-demanda/<CHIP>-gfa-gh.json` | `F1_EXPORTAR_GFA_v02` (disparado por flag) → F2 |
| `programa_areas` | `src/fase-3-masa/casos/CASO/programa-areas.json` | `src/fase-3-masa/casos/<CASO>/programa-areas.json` | `F3_DISTRIBUCION_v01` → orquestador copia → `F3_VOLUM_GENERADOR_v08.json_path` |
| `accesos` | `src/fase-3-masa/casos/CASO/accesos.json` | `src/fase-3-masa/casos/<CASO>/accesos.json` | `F3_ACCESOS_INTEGRADOR_v02` → orquestador copia |

## Fuera del canvas (el orquestador los mantiene por CHIP)

| ID | Archivo | Productor → Consumidor |
|---|---|---|
| `gfa_flag` | `data/fase-2-demanda/gfa-export-flag.json` | orquestador (`POST /api/exportar-gfa`) → `F1_EXPORTAR_GFA_v02` (true→false) |
| `vecinos_override` | `data/pot-cache/<CHIP>-vecinos-por-lado-override.json` | orquestador (`POST /api/vecinos-por-lado`) |
| `norma_override` | `data/pot-bogota/norma-override.json` | orquestador → `fetch-urban-context-v6.py` (fusiona en `pot_data`) |
| `financiero_override` | `data/pot-bogota/financiero-override.json` | orquestador → `parametros_<CHIP>_mercado2026.json` |
| `parametros_f2_venta` | `src/fase-2-demanda/F2_Modelo_Financiero/parametros_<CHIP>_mercado2026.json` | orquestador/manual → `F2_DEMANDA_MOTOR_v03.py` |
| `resultados_f2` | `src/fase-2-demanda/F2_Modelo_Financiero/resultados/resultados_<CHIP>.json` | `F2_DEMANDA_MOTOR_v03.py` → orquestador + F3 |
| `proyecto` | `src/orquestador/proyectos/<PROYECTO>/proyecto.json` | orquestador → `F0_LOAD_PROYECTO_v01.ruta_json` |

## Convenciones
- Los archivos `<CHIP>-*` y los activos (`CHIP-*`, `casos/CASO/`, `gfa-export-flag.json`)
  se regeneran y **no se commitean** (gitignore). Sí se commitean: `norma-override.json`,
  `financiero-override.json`, `data/predios/<CHIP>/proyecto.json`, los `.py` y los docs.
- El detalle del cableado: ver [[instructivo-cableado-canvas]] /
  `docs/instructivo-cableado-canvas.md`.
