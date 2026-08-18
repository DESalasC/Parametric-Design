# VECINOS POR LADO — nomenclatura cardinal y empate lateral

Clasifica los predios **inmediatamente vecinos** de un lote por lado, para el
caso en que por uno o varios lados haya **dos o más lotes colindantes, cada uno
con una altura distinta** (p. ej. La Candelaria).

## Nomenclatura

- **Lado**: `Norte`, `Oriente`, `Sur`, `Occidente` (por el azimut de la normal
  saliente de cada lado, a partir de `azimuth_norte_grados`).
- **Sub-segmento** (varios vecinos por el mismo lado): `Norte1`, `Norte2`, …,
  `Oriente1`, `Oriente2`, … (ordenados a lo largo del lado, en el sentido de la
  frontera del polígono).
- Un vecino de **esquina** colinda con dos lados: aparece en ambos con nombre
  distinto (p. ej. `Norte2` y `Oriente1`).

## Resultado real (La Candelaria, `AAA0030JKOE`)

| Lado | Vecinos |
|---|---|
| Norte | `Norte1` (003103035020), `Norte2` (003103035021) |
| Oriente | `Oriente1` (003103035029) |
| Sur | `Sur1`…`Sur5` (5 lotes colindantes) |
| Occidente | `Occidente1` (003103035020) |

## Archivos

- Generador (shapely): `src/orquestador/vecinos_por_lado.py`
  ```
  python src/orquestador/vecinos_por_lado.py AAA0030JKOE
  # -> data/pot-cache/AAA0030JKOE-vecinos-por-lado.json
  ```
- Salida por lote: `data/pot-cache/<CHIP>-vecinos-por-lado.json`

## Esquema de salida

```json
{
  "chip": "AAA0030JKOE",
  "crs": "ESRI:102233",
  "azimuth_norte_grados": 189.4,
  "n_lados": 4,
  "n_vecinos_colindantes": 9,
  "lados": [
    {
      "cardinal": "Norte",
      "azimut_grados": 36.0,
      "segmentos": [0, 2, 3, 4, 5, 6, 27, 28, 29],
      "longitud_m": 51.96,
      "n_vecinos": 2,
      "vecinos": [
        {"chip": "003103035020", "nombre": "Norte1",
         "longitud_colindancia_m": 24.16, "altura_m": null, "pisos": null}
      ]
    }
  ]
}
```

- `segmentos`: índices de los segmentos originales del polígono, para mapear a
  `sides_table_json` (F1_ETAPA2_LADOS) y a `vecinos_por_lado_json`
  (F1_ETAPA2_NORMATIVA_v08, que usa `id_lado` = índice de segmento).
- `altura_m` / `pisos`: quedan en `null` para que el operador las complete.

## Convenciones geométricas

- Las coordenadas `vertices_3d_local` son SIRGAS trasladadas **sin rotación**:
  `+X = Este`, `+Y = Norte`. Azimut desde el norte, sentido horario.
- Colindancia: un vecino pertenece a un lado si una fracción (≥ 0.25) del lado
  está a ≤ 0.15 m del polígono del vecino.
- Los segmentos consecutivos y no consecutivos del **mismo cardinal se fusionan**
  en un único lado (los polígonos SIG traen vértices colineales que partirían un
  mismo lado real en varios).

## Integración

- **Interfaz**: endpoint `GET /api/vecinos-por-lado?chip=<CHIP>` (servidor.py)
  devuelve la clasificación para que el formulario liste los predios por lado y
  el operador asigne `altura_m` / `pisos` por cada `Norte1`, `Sur3`, etc.
- **Fase 1 / NORMATIVA**: NORMATIVA_v08 ya consume `vecinos_por_lado_json`
  (`{id_lado: [altura_m, ...]}`), aplicado a lados `Lateral`. Falta mapear la
  nomenclatura cardinal → `id_lado` (usando `segmentos`) y propagar los valores
  que ingrese el operador.
- **F0_LOAD_PROYECTO**: pendiente exponer la nomenclatura + alturas por lado como
  salidas del canvas (o un JSON de empate lateral).

## Pendientes

1. UI del formulario (index.html) para listar vecinos por lado e ingresar alturas.
2. Mapeo cardinal → `id_lado` para alimentar `vecinos_por_lado_json` de NORMATIVA_v08.
3. Persistencia de las alturas ingresadas (proyecto.json o contexto.json).
