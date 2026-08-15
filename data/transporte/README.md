# data/transporte — Capas de transporte público de Bogotá (N3 accesibilidad)

Capas descargadas el **2026-08-14** desde fuentes oficiales (Datos Abiertos Bogotá /
TransMilenio S.A. / Secretaría Distrital de Movilidad). Se usan para materializar el
nivel **N3-LEJANO-ACCESIBILIDAD** del alcance de investigación
(`data/fase-2-demanda/alcance-investigacion.json` + `scripts/utilities/alcance_investigacion.py`).

| Archivo | Contenido | Fuente | Formato / CRS |
|---|---|---|---|
| `estaciones_tm.geojson` | 153 estaciones troncales TransMilenio | [Datos Abiertos Bogotá](https://datosabiertos.bogota.gov.co/dataset/estaciones-troncales-de-transmilenio) (servicio `gis.transmilenio.gov.co`) | GeoJSON, WGS84 (reproyectado a EPSG:3116 en el análisis) |
| `paraderos_sitp.geojson` | Paraderos zonales del SITP | [Movilidad Bogotá (ArcGIS Hub)](http://datos-abiertos-sdm-movilidadbogota.hub.arcgis.com/datasets/0df9f176a6ba4da89db428990fd9bc8b_0) | GeoJSON, WGS84 |
| `trazados_tm.geojson` | 20 trazados (corredores) troncales TransMilenio | [Datos Abiertos Bogotá](https://datosabiertos.bogota.gov.co/dataset/trazados-troncales-de-transmilenio) | GeoJSON, WGS84 |

Regenerable con: `python scripts/utilities/descargar_capas_transporte.py`.

## GTFS completo (pendiente)
El GTFS con horarios y rutas (SITP + TransMilenio) está publicado pero el zip es grande y no
tiene descarga directa estable:
- [Especificación GTFS SITP — Datos Abiertos Bogotá](https://datosabiertos.bogota.gov.co/dataset/especificacion-gtfs-general-transport-feed-specification-sitp)
- [GTFS Estático — Movilidad Bogotá](https://datos.movilidadbogota.gov.co/datasets/599751603a494051b15ac3d4f1f38ec5)
- [Portal de Datos Abiertos TransMilenio](https://datosabiertos-transmilenio.hub.arcgis.com/)

Mientras tanto, la **isocrona de 20 min se calcula con método de primer orden** documentado
(velocidad comercial 20 km/h → 6.667 m de red; corredores TM por arclength del trazado; red
zonal con factor de sinuosidad 1,3). Con el GTFS se podrá pasar a isocrona por horarios
(routing), mejora anotada como pendiente en el vault.
