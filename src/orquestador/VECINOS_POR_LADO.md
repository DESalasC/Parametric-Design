# VECINOS POR LADO — nomenclatura cardinal y tipo de frente

Clasifica, para cada lado de un lote, **qué enfrenta ese lado**, distinguiendo:

- `predio` — predio(s) vecino(s) colindante(s) → requieren empate/altura.
- `via` — calle / vía (NO es predio vecino).
- `espacio_publico` — zona verde / parque / plaza (NO es predio vecino).
- `libre` — sin contacto detectado.

Solo los lados `predio` listan vecinos con sub-índice (`Norte1`, `Norte2`, …).

## Nomenclatura

- **Lado**: `Norte`, `Oriente`, `Sur`, `Occidente` (azimut de la normal saliente).
- **Sub-segmento**: `Norte1`, `Norte2`, … (varios vecinos en el mismo lado, ordenados
  a lo largo de la frontera).
- Un vecino de **esquina** colinda con dos lados: aparece en ambos (p. ej. `Norte2`
  y `Oriente1`).

## Resultado automático vs. realidad (los 3 lotes)

| Lote | Lado | Automático | Realidad (operador) | Estado |
|---|---|---|---|---|
| El Prado | Norte | `via` | vía | ✓ |
| El Prado | Oriente | `predio` | predio | ✓ |
| El Prado | Sur | `predio` | predio | ✓ |
| El Prado | Occidente | `predio` | zona verde / EP | ✗ (dato) |
| Muzú | Norte | `predio` (2) | predio | ✓ |
| Muzú | Oriente | `via` | vía | ✓ |
| Muzú | Sur | `via` | vía | ✓ |
| Muzú | Occidente | `via` | predio | ✗ (esquina) |
| La Candelaria | Norte | `predio` (2) | predio | ✓ |
| La Candelaria | Sur | `predio` (5) | predio | ✓ |
| La Candelaria | Oriente | `predio` | vía (aún no construida) | ✗ (dato) |
| La Candelaria | Occidente | `predio` | vía | ✗ (dato) |

## Limitaciones conocidas (por qué hay errores)

1. **Vías incompletas.** `vias_oficiales` proviene del Eje_vial del POT, que está
   **incompleto** (muchas calles no digitalizadas). La Candelaria (centro histórico)
   es el caso típico: sus vías oriente/occidente no están en el dato → quedan como
   `predio`.
2. **Zonas verdes como "vecinos".** Algunas zonas verdes están en `vecinos` (con
   CHIP de catastro), no en `espacios_publicos`. Sin atributo de uso no se separan
   de predios edificables (El Prado occidente).
3. **Vías en esquina.** Una vía que pasa por la esquina puede marcar un lado
   perpendicular como `via` (Muzú occidente).

## Solución prevista: override manual

La clasificación automática es una **sugerencia**. Cada lado lleva:

```json
{"cardinal": "Norte", "frente": "via", "frente_fuente": "auto", "frente_override": null}
```

El operador fija `frente_override` (y el tipo real) en la interfaz; el dato del
operador manda sobre el automático. Esto resuelve los tres casos anteriores sin
depender de completar la geobase.

## Archivos y CLI

- Generador (shapely): `src/orquestador/vecinos_por_lado.py`
  ```
  python src/orquestador/vecinos_por_lado.py AAA0030JKOE
  # -> data/pot-cache/AAA0030JKOE-vecinos-por-lado.json
  ```
- Endpoint: `GET /api/vecinos-por-lado?chip=<CHIP>` (servidor.py).

## Esquema de salida

```json
{
  "chip": "AAA0030JKOE",
  "crs": "ESRI:102233",
  "n_lados": 4,
  "n_predios_colindantes": 9,
  "nota": "...",
  "lados": [
    {
      "cardinal": "Sur",
      "frente": "predio",
      "frente_fuente": "auto",
      "frente_override": null,
      "segmentos": [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
      "segmentos_vecinos": {"9": ["003103035008", "003103035029"],
                          "10": ["003103035008"]},
      "longitud_m": 51.96,
      "n_vecinos": 5,
      "vecinos": [
        {"chip": "003103035008", "nombre": "Sur1",
         "longitud_colindancia_m": 5.54, "altura_m": null, "pisos": null}
      ]
    }
  ]
}
```

## Interfaz y mapeo a NORMATIVA (v08)

**Punto 1 — UI (index.html, sección 1b "Vecinos por lado"):** lista cada lado con
su `frente` editable (select `predio`/`via`/`espacio_publico`/`libre` → escribe
`frente_override`) y, para lados `predio`, una tabla de vecinos con `altura_m` y
`pisos`. Al guardar, `recolectar()` escribe `proyecto.json['vecinos_por_lado']`
(con `frente_override` y alturas del operador).

**Punto 2 — mapeo cardinal → id_lado:** `a_normativa_vecinos_por_lado()` (Python)
y su port IronPython en `F0_LOAD_PROYECTO_v01` convierten la clasificación a
`{id_lado: [altura_m, ...]}` (id_lado = índice de segmento). El botón "Generar
JSON NORMATIVA" muestra el resultado en vivo; el loader lo emite como
`vecinos_por_lado_json` para cablear directo a `F1_ETAPA2_NORMATIVA_v08`.

Flujo: UI → `proyecto.json['vecinos_por_lado']` → `F0_LOAD_PROYECTO_v01.vecinos_por_lado_json` → NORMATIVA_v08 (lados `Lateral`).

## Confirmación del operador (plantilla dinámica)

El formulario pide al operador confirmar, por lado, si el número de vecinos
detectados corresponde a la realidad. Según la respuesta, la plantilla varía:

| Confirmación | Qué muestra la plantilla |
|---|---|
| `pendiente` (default) | Solo el conteo detectado + aviso de confirmar. |
| `confirmado` | Tabla de vecinos con `altura_m`/`pisos` (todos activos). |
| `faltan` | Tabla + botón "+ Agregar vecino" (filas manuales). |
| `sobran` | Tabla con checkbox `corresponde` por vecino (desmarcar = excluir). |
| `no_es_predio` | Select para re-clasificar el frente; oculta la tabla. |

Modelo de datos (por lado, en `proyecto.json['vecinos_por_lado']['lados'][i]`):
- `confirmacion`: `pendiente|confirmado|faltan|sobran|no_es_predio`.
- por vecino detectado: `corresponde` (bool, default `true`).
- `vecinos_manuales`: filas agregadas a mano (nombre/chip/altura_m/pisos).

El mapeo a NORMATIVA respeta `frente_override`, `confirmacion`, `corresponde` e
incluye los `vecinos_manuales` (asignados al primer segmento del lado, suposición
documentada). La lógica coincide en los tres lugares: `vecinos_por_lado.py`,
`F0_LOAD_PROYECTO_v01.py` (IronPython) y el JS del formulario.

## Estado

- [x] Clasificación `frente` (predio/via/espacio_publico/libre) + sub-índices.
- [x] `frente_override` manual por lado.
- [x] UI del formulario (sección 1b) + botón "Generar JSON NORMATIVA".
- [x] Mapeo cardinal → `id_lado` (`a_normativa_vecinos_por_lado` + salida F0 v01.3).
- [x] Persistencia en `proyecto.json['vecinos_por_lado']`.
- [x] Confirmación del operador con plantilla dinámica (pendiente/confirmado/faltan/sobran/no_es_predio) + vecinos manuales.
- [ ] Cableado manual del canvas en Rhino (F0 → NORMATIVA_v08.vecinos_por_lado_json).
