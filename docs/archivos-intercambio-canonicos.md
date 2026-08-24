# Archivos de intercambio canónicos (canvas Grasshopper ↔ orquestador ↔ motores)

Versión: 2026-08-23. Fuente: cabeceras ENTRADAS/SALIDAS de los scripts F0–F3 +
`servidor.py`. `<CHIP>` = código catastral (p.ej. `AAA0240ZXJH`); `<CASO>` =
A | B | B_SALUD | C.

## F1 (contexto → normativa → GFA)

| Archivo | Dirección | Productor | Consumidor |
|---|---|---|---|
| `data/pot-cache/<CHIP>-contexto.json` | entrada | `fetch-urban-context-v6.py` | `F1_ETAPA1_CONTEXTO_v02.json_path` |
| `data/pot-cache/<CHIP>-vecinos-por-lado.json` | entrada | `vecinos_por_lado.py` | NORMATIVA/LADOS (vecinos por cardinal) |
| `data/pot-bogota/norma-override.json` | entrada | orquestador (`/api/norma-override`) | `fetch-urban-context-v6.py` (fusiona en `pot_data`) |
| `data/predios/<CHIP>/proyecto.json` | entrada | orquestador (proyecto) | `F0_LOAD_PROYECTO_v01.py` (→ `vecinos_por_lado`, variables) |
| `data/fase-2-demanda/<CHIP>-gfa-gh.json` | salida | `F1_EXPORTAR_GFA_v02.output_path` | motor F2 (`--gfa` o default) |

## F2 (financiero venta)

| Archivo | Dirección | Productor | Consumidor |
|---|---|---|---|
| `src/fase-2-demanda/F2_Modelo_Financiero/parametros_<CHIP>_mercado2026.json` | entrada | operador/curaduría | `F2_DEMANDA_MOTOR_v03.py --parametros` |
| `src/fase-2-demanda/F2_Modelo_Financiero/parametros_<CHIP>_venta.json` | entrada (alt) | operador | ídem |
| `src/fase-2-demanda/F2_Modelo_Financiero/parametros_entrada.json` | entrada (default) | plantilla | ídem (si no hay por CHIP) |
| `src/fase-2-demanda/F2_Modelo_Financiero/resultados/resultados_<CHIP>.json` | salida | `F2_DEMANDA_MOTOR` | `servidor.py` (resumen) + F3 |
| `src/fase-2-demanda/F2_Modelo_Financiero/resultados/resultados_completos.json` | salida | ídem | ídem |
| `data/activo/f2_entrada.json` | entrada | orquestador (`_persistir_modalidad_f2_entrada`) | F2 (modalidad_dueno_lote) |

## F3 (masa)

| Archivo | Dirección | Productor | Consumidor |
|---|---|---|---|
| `src/fase-3-masa/casos/<CASO>/programa-areas.json` | salida/entrada | `F3_DISTRIBUCION_v01` | `F3_VOLUM_GENERADOR_v07`, `servidor.py` |
| `src/fase-3-masa/casos/<CASO>/accesos.json` | salida | `F3_ACCESOS_INTEGRADOR_v02` | `servidor.py` |
| `src/fase-3-masa/casos/<CASO>/layout_espacial.json` | salida | `F3_DISTRIBUCION_v01` | `F3_ACCESOS_INTEGRADOR_v02` |
| `src/fase-3-masa/casos/<CASO>/matriz_adyacencias.json` | entrada | (curaduría) | `F3_ACCESOS_INTEGRADOR_v02` |

## Otros (estado activo / pipeline)

| Archivo | Uso |
|---|---|
| `data/activo/contexto.json` | estado F1 activo |
| `data/activo/f2_resultado.json` | estado F2 activo |
| `data/activo/f3_masa.json` | estado F3 activo |
| `data/activo/mercado_zonal.json` | mercado por zona |
| `data/activo/predio.json` | predio activo |
| `src/orquestador/parametros_pipeline.json` | chip/caso/modo por defecto del pipeline |

## Convenciones
- Los archivos `<CHIP>-*` se regeneran y **no se commitean** (gitignore). Sí se
  commitean: `norma-override.json`, `data/predios/<CHIP>/proyecto.json` y los
  `parametros_<CHIP>_*.json` **validados** de F2.
- `output_path` de `F1_EXPORTAR_GFA_v02` por defecto = `data/fase-2-demanda/`.
- El CHIP se deriva del nombre del `-contexto.json` (no se pasa explícito al canvas).
- El cableado componente↔input está en `src/orquestador/CABLEADO_F0.md`.
