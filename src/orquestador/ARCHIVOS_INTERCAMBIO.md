# Archivos de intercambio (nombres canónicos)

Única fuente de verdad para cablear el canvas Grasshopper **una sola vez**.

## Regla del canvas

Dentro del canvas, los componentes GH **siempre** leen/escriben el archivo **ACTIVO**,
cuyo nombre es literal (`CHIP`, `CASO`), **nunca** el CHIP real. Al seleccionar un predio
(o un caso F3) en el orquestador, éste **sobreescribe** el activo con los datos elegidos y
conserva el archivo por-CHIP/caso como historial. Así el canvas no se edita jamás entre predios.

- `CHIP` / `CASO` = literal (el canvas apunta a `CHIP-contexto.json`, no a `AAA0240ZXJH-contexto.json`).
- `<CHIP>` / `<CASO>` = se sustituye por el valor real; lo usa el orquestador/scripts (fuera del canvas).

## Activos (el canvas lee/escribe estos — nombre literal)

| ID | Activo (canvas) | Archivo por CHIP/CASO (historial) | Produce | Consume |
|---|---|---|---|---|
| `contexto` | `data/pot-cache/CHIP-contexto.json` | `data/pot-cache/<CHIP>-contexto.json` | `fetch-urban-context-v7.py` (escribe `<CHIP>-contexto.json`) → orquestador copia al activo | `F1_ETAPA1_CONTEXTO_v02` (lee el activo) |
| `vecinos_por_lado` | `data/pot-cache/CHIP-vecinos-por-lado.json` | `data/pot-cache/<CHIP>-vecinos-por-lado.json` | `vecinos_por_lado.py` (escribe `<CHIP>-vecinos-por-lado.json`) → orquestador copia al activo (con confirmaciones) | `F1_ETAPA2_NORMATIVA_v08` (lee el activo: `vecinos_por_lado_json`) |
| `gfa_gh` | `data/fase-2-demanda/CHIP-gfa-gh.json` | `data/fase-2-demanda/<CHIP>-gfa-gh.json` | `F1_EXPORTAR_GFA_v02` (disparado por `gfa-export-flag.json`; escribe activo + archivo) | `F2_DEMANDA_MOTOR_v03` / `F2_RENTA_MOTOR_v03` (leen el archivo por CHIP) |
| `programa_areas` | `src/fase-3-masa/casos/CASO/programa-areas.json` | `src/fase-3-masa/casos/<CASO>/programa-areas.json` | `F3_DISTRIBUCION_v01.py` (escribe `<CASO>`) → orquestador copia al activo | `F3_VOLUM_GENERADOR_v08` (lee el activo: `json_path`) |
| `accesos` | `src/fase-3-masa/casos/CASO/accesos.json` | `src/fase-3-masa/casos/<CASO>/accesos.json` | `F3_ACCESOS_INTEGRADOR_v02.py` (escribe `<CASO>`) → orquestador copia al activo | orquestador (resultados) |

## Fuera del canvas (el orquestador los mantiene por CHIP)

| ID | Archivo | Produce | Consume |
|---|---|---|---|
| `gfa_flag` | `data/fase-2-demanda/gfa-export-flag.json` | orquestador (`POST /api/exportar-gfa`) | `F1_EXPORTAR_GFA_v02` (dispara la exportación y la devuelve a false) |
| `vecinos_override` | `data/pot-cache/<CHIP>-vecinos-por-lado-override.json` | orquestador (`POST /api/vecinos-por-lado`) | orquestador (`GET`) — confirmaciones del operador |
| `norma_override` | `data/pot-bogota/norma-override.json` | orquestador (`POST /api/norma-override`) | `fetch-urban-context-v7.py` (fusiona en `pot_data`, gana sobre la geobase) |
| `financiero_override` | `data/pot-bogota/financiero-override.json` | orquestador (`POST /api/financiero`) | orquestador + generación de `parametros_<CHIP>_mercado2026.json` |
| `parametros_f2_venta` | `src/fase-2-demanda/F2_Modelo_Financiero/parametros_<CHIP>_mercado2026.json` | orquestador (`POST /api/financiero`) o manual | `F2_DEMANDA_MOTOR_v03.py` (`--parametros`) |
| `resultados_f2` | `src/fase-2-demanda/F2_Modelo_Financiero/resultados/resultados_<CHIP>.json` | `F2_DEMANDA_MOTOR_v03.py` | orquestador + F3 |

## Activación automática

- `POST /api/activar-chip` (`{chip}`): sobreescribe `CHIP-contexto.json` y
  `CHIP-vecinos-por-lado.json` (con confirmaciones) a partir del CHIP seleccionado.
  El formulario lo llama automáticamente al cambiar de CHIP.
- `POST /api/activar-caso` (`{caso}`): sobreescribe `casos/CASO/programa-areas.json`,
  `casos/CASO/accesos.json` y `casos/CASO/layout_espacial.json` a partir del caso
  seleccionado. El formulario lo llama automáticamente al cambiar de caso F3.
- `POST /api/vecinos-por-lado`: además de guardar el override por-CHIP, refresca el
  activo `CHIP-vecinos-por-lado.json` para que el canvas reciba las alturas/frentes
  confirmadas.
- `POST /api/exportar-gfa`: pone `gfa-export-flag.json` en `{"exportar": true}`; el
  componente `F1_EXPORTAR_GFA_v02` exporta y lo devuelve a `false` por omisión.

## Reglas de flujo

- **Fase 1 solo lee** el activo `data/pot-cache/CHIP-contexto.json`. Si no existe, ejecutar
  `fetch-urban-context-v7.py --chip <CHIP>` y luego activar el CHIP en el orquestador.
- El **área del lote** se calcula SIEMPRE desde `vertices_3d_local` (shoelace), no del
  `area_m2` de los parámetros financieros (que es valor de referencia de mercado).
- Los **overrides del operador** (`norma-override.json`, `financiero-override.json`,
  `<CHIP>-vecinos-por-lado-override.json`) **ganan** sobre los datos automáticos/geobase.
- El **GFA** se exporta solo bajo demanda (flag `true`), no en cada recomputación del canvas.
- El orquestador expone estos nombres en `GET /api/archivos` (tarjeta "Archivos de intercambio").
