# ADR-002: Catastro (bd_uaecd.gpkg) NO es POT — fuentes separadas requeridas

**Fecha:** 2026-08-01
**Estado:** Aceptado

## Contexto

Inicialmente (Doc 2) se asumía que el archivo `bd_uaecd.gpkg` de la geobase Bogotá era la fuente del POT (Plan de Ordenamiento Territorial). El usuario mencionó "2455 campos disponibles para seleccionar" basado en `gdb_layer_fields_report.csv`.

Al ejecutar `setup-test-lot.py` e inspeccionar el .gpkg, se descubrió:

1. **El .gpkg tiene 191 campos en 22 capas, no 2455.** Los "2455" del CSV eran registros (filas), no campos.
2. **Las capas son de CATASTRO (avalúo y catastro), no de POT.** Contienen:
   - Identificación predial (Chip, cédula catastral, NUPRE)
   - Áreas (terreno, construcción)
   - Uso actual (no permitido)
   - Estrato socioeconómico
   - Año de construcción, número de pisos
   - Calificación de construcciones
3. **NO contiene normativa POT**: alturas máximas permitidas, retiros obligatorios, tratamientos urbanísticos, edificabilidad, ocupación.

Adicionalmente, se identificó el sistema de coordenadas:

- **CRS del .gpkg:** MAGNA Ciudad Bogotá (ESRI:102233)
- **Coords típicas:** X ~ 93,000-103,000, Y ~ 98,000-118,000
- **No es EPSG:9377** (MAGNA-SIRGAS Origen Bogotá, coords X ~ 1,007,000)
- Es un sistema local de Bogotá con falso este y falso norte específicos.

## Decisión

1. **Separar fuentes de datos:**
   - **Catastro:** `bd_uaecd.gpkg` (existente, operativo).
   - **POT:** fuente separada pendiente de integrar (ver opciones abajo).

2. **Mantener CONTEXTO_v09.py con valores por defecto** (retiro 3.0m, altura 12m) hasta integrar POT real. No propagar valores inventados.

3. **Documentar el CRS en todo el pipeline:**
   - `config/field-whitelist.json` incluye metadata del CRS.
   - `CLAUDE.md` del proyecto incluye regla de transformación.
   - Cuando se consulte APIs externas, transformar coords con `pyproj.Transformer`.

4. **Aprovechar el descubrimiento para automatizar vecinos:**
   - La capa `Calificacion` tiene `PrePiso` (número de pisos) de cada vecino.
   - Heurística inicial: `altura_vecino_m = PrePiso × 3.0`
   - Refinamiento futuro: ajustar por `PreVetustz` (año de construcción).
   - **Esto elimina la dependencia de modelar vecinos a mano** (que era la justificación original).

## Alternativas consideradas

### Para fuente POT

- **Opción A — IDECA Bogotá**: descargar capas GeoJSON del POT desde https://geobogota.maps.arcgis.com/. Buscar "Plan de Ordenamiento Territorial" o "Normativa Urbanística".
- **Opción B — Decreto 555/2021 PDF**: convertir tablas por UPZ a `data/pot-bogota/upz-normativa.json` estructurado.
- **Opción C — Otra geobase**: si el usuario tiene otro .gpkg específicamente POT, integrarlo como segunda fuente.

### Para CRS

- **Opción A — Trabajar en ESRI:102233**: todas las coords del .gpkg se usan tal cual. Archicad también se modela en este CRS.
- **Opción B — Transformar todo a EPSG:9377**: estándar nacional moderno. Requiere `pyproj.Transformer.from_crs('ESRI:102233', 'EPSG:9377', always_xy=True)`.
- **Recomendación**: **Opción A** para datos internos (más simple), transformar a WGS84 solo para APIs externas.

## Consecuencias

**Positivas:**
- Separación clara de concerns: catastro vs normativa.
- Vecinos automatizables (breakthrough que elimina trabajo manual).
- CRS documentado evita bugs de distancia (como los "millones de metros" del Doc 2).
- Whitelist reducida a 32 campos relevantes (de 191 totales).

**Negativas:**
- POT requiere fuente adicional pendiente de identificar.
- CONTEXTO_v09.py no puede entregar normativas reales todavía.
- Coords del .gpkg no son estándar nacional (requieren transformación para APIs externas).

**Neutrales:**
- Pipeline general (Fase 1→4) se mantiene igual.
- Tapir/Rhino.Compute/Ollama no se ven afectados.

## Próximos pasos

1. **Inmediato:** integrar `make_valid`/`buffer(0)` en `gpkg-to-cache.py` para manejar geometrías inválidas (365,863 lotes, ~5-10% con problemas topológicos).
2. **Corto plazo:** generar primer caché JSON exitoso para un lote real.
3. **Corto plazo:** construir `extract-neighbors-from-gpkg.py` que use `PrePiso × 3m` para automatizar vecinos.
4. **Mediano plazo:** identificar y descargar fuente POT real (IDECA o Decreto 555/2021).
5. **Mediano plazo:** integrar POT en `CONTEXTO_v09.py` reemplazando los valores por defecto.

## Referencias

- Doc 2 (arquitectura técnica original)
- `data/gdb_fields_inventory.json` (inventario completo del .gpkg)
- `config/field-whitelist.json` (whitelist actualizada con notas del CRS)
- ESRI:102233 — https://epsg.io/102233
- IDECA Bogotá — https://geobogota.maps.arcgis.com/
