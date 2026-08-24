# Instructivo — cableado del canvas Grasshopper (una sola vez)

> Aplica a la regla de **archivos ACTIVOS**: dentro del canvas los componentes
> leen/escriben nombres **literales** `CHIP` / `CASO`. El orquestador sobreescribe
> esos activos al seleccionar el predio/caso; el canvas no se edita entre predios.

## 1. Componentes que hay que (re)exportar

Editar el `.py` **no** actualiza el canvas: el `.gh`/`.ghx` embebe el código. Tras
cada cambio hay que **re-exportar el componente GHPython** (componente clásico
"Script", lenguaje **IronPython 2.7**; nunca "Python 3 Script").

| Componente (`.py`) | Qué cambió / a cablear |
|---|---|
| `F0_LOAD_PROYECTO_v01.py` | lee `proyecto.json` y emite `vecinos_por_lado_json` + `frente_override_json` (ya v01.4) |
| `F1_ETAPA1_CONTEXTO_v02.py` | input `json_path` → **`CHIP-contexto.json`** (literal) |
| `F1_ETAPA2_LADOS_v06.py` | entrada geométrica (sin JSON propio; lee curvas de ArchiCAD) |
| `F1_ETAPA2_PATIO_v02.py` | entrada geométrica (sin JSON propio) |
| `F1_ETAPA2_NORMATIVA_v08.py` | inputs `vecinos_por_lado_json` y `frente_override_json` (strings de F0) |
| `F1_EXPORTAR_GFA_v02.py` | **v02.2**: disparador por flag `gfa-export-flag.json`; escribe `<CHIP>-gfa-gh.json` + `CHIP-gfa-gh.json` (salida programada) |
| `F3_VOLUM_GENERADOR_v08.py` | input `json_path` → **`casos/CASO/programa-areas.json`** (literal) |

## 2. Nombres canónicos de los JSON de ENTRADA (los que el canvas LEE)

| JSON de entrada | Nombre literal | Lo lee (input) |
|---|---|---|
| Contexto F1 | `data/pot-cache/CHIP-contexto.json` | `F1_ETAPA1_CONTEXTO_v02.json_path` · `F1_EXPORTAR_GFA_v02.json_path` |
| Proyecto (variables + vecinos + frentes) | `src/orquestador/proyectos/<PROYECTO>/proyecto.json` | `F0_LOAD_PROYECTO_v01.ruta_json` |
| Programa de áreas F3 | `src/fase-3-masa/casos/CASO/programa-areas.json` | `F3_VOLUM_GENERADOR_v08.json_path` |

> `proyecto.json` es por **proyecto** (no por CHIP): se cablea una vez por proyecto.
> `vecinos_por_lado_json` y `frente_override_json` **no son archivos**: son salidas
> *string* de `F0_LOAD_PROYECTO_v01` (convertidas desde `proyecto.json`).

**Salidas programadas (no se cablean como archivo):**
- `F1_EXPORTAR_GFA_v02` escribe por ruta programada: `data/fase-2-demanda/<CHIP>-gfa-gh.json`
  (historial/F2) y `data/fase-2-demanda/CHIP-gfa-gh.json` (activo literal). Se dispara
  con `gfa-export-flag.json` (`{"exportar": true}` → exporta → `false`).

## 3. Conexiones (paso a paso)

1. **F0 → variables**: `F0_LOAD_PROYECTO_v01.ruta_json` → `<proyecto>.json`.
   Sus salidas se cablean a NORMATIVA: `tipologia`, `antejardin_m`, `voladizo_frontal_m`,
   `empate_posterior_pisos`, `floor_height_user`, `piso_adicional`, `tipo_bonificacion`,
   `tratamiento`, `rango_edificabilidad`, `vecinos_por_lado_json`, `frente_override_json`.
2. **F1_ETAPA1**: `json_path` → `data/pot-cache/CHIP-contexto.json`. Salidas: `lot_curve`,
   `vecinos_curves`, `vias_oficiales`, `espacios_publicos`, `reglamentacion_json`, `layers_json`.
3. **F1_ETAPA2_LADOS**: `lot_vertices` (Discontinuity del lote) + `vias_curves`/`ep_curves`/
   `vecinos_curves` (capas clasificadas de ArchiCAD). Salida `sides_table_json`.
4. **F1_ETAPA2_PATIO**: patios desde colindancias reales. Salida `patio_curves`.
5. **F1_ETAPA2_NORMATIVA**: `lot_polygon` (lote) + `sides_table_json` (LADOS) + `patio_curves`
   (PATIO) + `reglamentacion_json` (ETAPA1) + variables de F0 + `vecinos_por_lado_json` +
   `frente_override_json`. Salidas: `envelope_curve`, `envelope_por_piso`, `gfa_total`, etc.
6. **F1_EXPORTAR_GFA**: `json_path` → `CHIP-contexto.json`; `area_envelope` ←
   `Area(envelope_curve)`; `gfa_total`, `ocupacion_real`, `io_maximo`, `ic_real`,
   `ic_maximo`, `altura_total`, `pisos_finales`, `valido`, `mensaje` ← NORMATIVA.
   (Escribe GFA solo cuando `gfa-export-flag.json` está en `true`.)
7. **F3_VOLUM_GENERADOR**: `json_path` → `casos/CASO/programa-areas.json`;
   `envelope_por_piso` ← NORMATIVA. Salidas de masa → componentes `AC_*` (Morphs).

## 4. Reglas de entorno (recordar)

- GHPython = **IronPython 2.7**: sin f-strings/pathlib/type hints; entradas SIEMPRE con
  `globals().get(...)`; componente "Script" clásico.
- Entradas geométricas: **List Access + Flatten** y **Type hint = Curve**.
- Orden de arranque del puerto 19723: **ArchiCAD → Grasshopper → AutoClaw**.
- El área del lote sale de los **vértices** (shoelace), no del `area_m2` de mercado.
