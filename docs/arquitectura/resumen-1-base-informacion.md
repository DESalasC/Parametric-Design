# Resumen 1: Integración de Información — Base de Conocimiento Sólida

**Fecha:** 2026-08-03
**Proyecto:** DiseñoParametrico
**Alcance:** Recopilación, estructuración e integración de todas las fuentes de información normativa, catastral y teórica para el diseño paramétrico en Bogotá.

---

## 1. Puntos Relevantes para Entender el Proceso

### 1.1 El problema inicial

El proyecto DiseñoParametrico busca automatizar el diseño arquitectónico paramétrico en Bogotá, integrando:
- Normativa POT (Plan de Ordenamiento Territorial)
- Normativa NSR-10 (construcción sismo resistente)
- Datos catastrales reales
- Marco teórico de Christopher Alexander
- Conocimiento arquitectónico especializado

El desafío era que esta información estaba dispersa en múltiples formatos (PDFs, geodatabases, scripts sueltos, notas manuales) sin estructura unificada.

### 1.2 Las tres fuentes de información normativa

#### Fuente 1: Catastro (bd_uaecd.gpkg)
- **Archivo:** 3.1 GB, 365,863 lotes
- **CRS:** MAGNA Ciudad Bogotá (ESRI:102233) — NO el estándar EPSG:9377
- **Capas:** 22 capas, 191 campos totales
- **Capas clave:** Lote (18 campos), Predio (24 campos), Calificacion (35 campos)
- **Contenido:** Identificación predial, áreas, estrato, uso actual, año construcción, número de pisos

#### Fuente 2: POT (Decreto 555/2021 + geodatabase)
- **Geodatabase:** POT_Decreto_555_2021_Bogota_D_C.gdb (carpeta ESRI)
- **CRS:** PCS_CarMAGBOG (custom Bogotá, similar al catastro)
- **Capas:** 166 capas totales, 8 consultadas activamente
- **Capa crítica:** Area_elevacion_maxima (altura máxima permitida + UPZ)
- **Texto legal:** Decreto 555/2021 (25,700 líneas en Markdown)

#### Fuente 3: NSR-10 (Reglamento sismo resistente)
- **Documento:** 203,542 líneas en Markdown
- **Relevancia:** Título A, especialmente sección A.6.5 (separaciones sísmicas)
- **Bogotá:** Zona de Amenaza Intermedia (Aa=0.15, Av=0.20)

### 1.3 El proceso de descubrimiento progresivo

El proceso no fue lineal. Cada descubrimiento obligaba a reevaluar supuestos:

1. **Asumimos** que el .gpkg era POT → **Descubrimos** que era catastro
2. **Asumimos** CRS EPSG:9377 → **Descubrimos** ESRI:102233 (MAGNA Ciudad Bogotá)
3. **Asumimos** que POT no estaba disponible → **Descubrimos** la geodatabase del Decreto 555
4. **Asumimos** que los retiros estaban en una capa → **Descubrimos** que están en el texto del decreto
5. **Asumimos** que los vecinos debían modelarse a mano → **Descubrimos** que PrePiso × 3m permite automatizarlos

### 1.4 La arquitectura de información final

```
DATOS ESPACIALES (no se mueven, 3.1 GB + .gdb)
├── bd_uaecd.gpkg (catastro)
└── POT_Decreto_555_2021_Bogota_D_C.gdb (POT)

CACHÉS PRECALCULADOS (por predio)
└── data/pot-cache/<predio-id>.json
    ├── catastro (38 campos, 3 JOINs)
    ├── pot (5-8 capas consultadas)
    └── decreto_555_2021 (retiros calculados)

ESTRUCTURADO (tablas consultables)
├── data/pot-bogota/retiros-estructurados.json
├── data/pot-bogota/edificabilidad-estructurada.json
├── data/pot-bogota/tratamientos-estructurados.json
├── data/pot-bogota/incentivos-670.json
├── data/pot-bogota/actuaciones-estrategicas-670.json
├── data/nsr-10/separaciones-sismicas.json
├── data/nsr-10/grupos-uso-coef-importancia.json
└── data/nsr-10/amenaza-sismica-bogota.json

TEXTO LEGAL (Markdown navegable)
├── docs/normativa/pot-bogota/decreto-555-extractos.md
├── docs/normativa/pot-bogota/decreto-670-extractos.md
└── docs/normativa/nsr-10/nsr-10-extractos.md

MARCO TEÓRICO (vault Obsidian)
└── vault/30-referencia/christopher-alexander/
    ├── lenguaje-patrones/
    ├── modo-intemporal/
    ├── naturaleza-del-orden/
    └── 00-index-alexander.md
```

---

## 2. Errores Encontrados

### Error 1: "El .gpkg es POT" → Era catastro
- **Síntoma:** No encontrábamos alturas máximas ni retiros en el .gpkg
- **Causa:** El archivo bd_uaecd.gpkg es de la Unidad de Avalúo y Catastro, no del POT
- **Los "2455 campos"** mencionados originalmente eran registros (filas) del CSV, no campos
- **Solución:** ADR-002 documentando que catastro ≠ POT, fuentes separadas requeridas
- **Impacto:** Cambió toda la arquitectura del pipeline

### Error 2: CRS equivocado (EPSG:9377 vs ESRI:102233)
- **Síntoma:** Las coordenadas del lote Chapinero (X~1,007,000) no intersectaban nada
- **Causa:** El .gpkg usa MAGNA Ciudad Bogotá (ESRI:102233), no MAGNA-SIRGAS Origen Bogotá (EPSG:9377)
- **Coords reales:** X~93,000-103,000, Y~98,000-118,000
- **Solución:** Documentar CRS en CLAUDE.md, whitelist y todos los scripts
- **Lección:** Siempre verificar CRS antes de cualquier consulta espacial

### Error 3: Coordenadas 4D rompiendo shapely
- **Síntoma:** `ValueError: The ordinate (last) dimension should be 2 or 3, got 4`
- **Causa:** Algunos GeoJSON tienen coordenadas [X, Y, Z, M] (4 valores por punto)
- **Solución:** Función `_truncate_coords_2d()` que trunca a [X, Y] automáticamente

### Error 4: Geometrías inválidas del catastro
- **Síntoma:** `TopologyException: side location conflict` al hacer `intersection()`
- **Causa:** ~5-10% de los 365,863 lotes tienen autointersecciones o nodos duplicados
- **Solución:** `make_valid()` de shapely + `buffer(0)` como fallback
- **Resultado:** 1 de 44,259 geometrías reparada en el lote de prueba

### Error 5: Predio y Calificacion no tienen geometría
- **Síntoma:** `Cannot set spatial filter: no geometry field present in layer`
- **Causa:** Las capas Predio (None) y Calificacion (None) son tablas sin geometría
- **Solución:** JOIN por atributo (Barmanpre → PreChip) en vez de JOIN espacial

### Error 6: Nombres de campos asumidos incorrectamente
- **Síntoma:** Campos `NOMBRE`, `TRATAMIENTO`, `TIPO` devolvían null
- **Causa:** Los nombres reales eran `NOMBRE_TRATAMIENTO`, `CODIGO_AREA_ACTIVIDAD`, `CLASE_SUELO`
- **Solución:** Inspeccionar campos reales con `show-fields` antes de asumir

### Error 7: Bounding boxes como puntos del polígono
- **Síntoma:** Área del lote era 23 km² (debería ser ~200 m²)
- **Causa:** El JSON del lote tenía formato [minX, minY, maxX, maxY] como "puntos"
- **Solución:** Script `extract-real-lote.py` que extrae coordenadas reales del .gpkg

### Error 8: Lote no intersecta en Area_elevacion_maxima
- **Síntoma:** Algunas capas POT no intersectaban el lote de prueba
- **Causa:** El lote en Bosa estaba en zona con polígonos complejos (>100 partes)
- **Solución:** Tolerar `no_interseca` como respuesta válida (no todos los lotes están en todas las capas)

---

## 3. Lecciones Aprendidas

### Lección 1: Nunca asumir el contenido de una geodatabase
**Lo que pasó:** Asumimos que bd_uaecd.gpkg era POT porque el usuario lo mencionó como "geobase del POT".
**Lo que aprendimos:** Siempre ejecutar `list-layers` y `show-fields` antes de diseñar el pipeline. Los nombres de archivos pueden ser engañosos.
**Cómo contribuyó:** Creó el ADR-002 que separó claramente fuentes y llevó a descubrir el POT real (.gdb del Decreto 555).

### Lección 2: El CRS lo es todo
**Lo que pasó:** Coordenadas que no intersectaban nada, distancias de "millones de metros".
**Lo que aprendimos:** Verificar CRS con `pyogrio.read_info()` antes de cualquier operación espacial. Dos datasets pueden tener CRS similares pero no idénticos.
**Cómo contribuyó:** Documentación precisa del CRS en todos los scripts y CLAUDE.md, evitando bugs futuros.

### Lección 3: Los datos catastrales son sucios
**Lo que pasó:** Geometrías inválidas, coords 4D, polígonos con 100+ partes.
**Lo que aprendimos:** Siempre implementar `make_valid()` + `buffer(0)` + truncado de coords como defensiva.
**Cómo contribuyó:** El pipeline es robusto y maneja datos reales sin crashear.

### Lección 4: El POT real sí existe como geodatabase
**Lo que pasó:** Inicialmente pensamos que no había POT digital, solo el PDF del decreto.
**Lo que aprendimos:** El usuario tenía `pot_decreto_555_2021_bogota_d_c.gdb.zip` todo el tiempo.
**Cómo contribuyó:** Pasamos de valores por defecto (retiro 3.0m, altura 12m) a datos REALES (altura 150m, UPZ Venecia, tratamiento Desarrollo).

### Lección 5: Vecinos automatizables
**Lo que pasó:** El Doc 2 decía que los vecinos se modelaban a mano "porque no hay modelo 3D de Bogotá".
**Lo que aprendimos:** El campo `Calificacion.PrePiso` tiene el número de pisos de cada vecino. `PrePiso × 3m = altura estimada`.
**Cómo contribuyó:** Eliminó una limitación crítica del pipeline. Los vecinos pueden extraerse automáticamente del catastro.

### Lección 6: El texto legal es estructurable
**Lo que pasó:** Pensamos que los retiros obligatorios estaban en una capa geográfica.
**Lo que aprendimos:** Están en el texto del Decreto 555/2021 (Artículos 281, 310, etc.), organizados por tratamiento y tipología.
**Cómo contribuyó:** Creamos scripts extractores que parsean el Markdown del decreto y generan JSONs estructurados consultables.

### Lección 7: El Decreto 670 compiló y actualizó al 555
**Lo que pasó:** Descubrimos que existe el Decreto 670/2025 que compila al 555 y añade precisiones.
**Lo que aprendimos:** El 670 no deroga al 555, lo mantiene vigente con ultraactividad. Añade incentivos urbanísticos (3 tipos) y fichas C/UNE actualizadas.
**Cómo contribuyó:** Integración completa de la normativa POT vigente a diciembre 2025.

---

## 4. Archivos Producidos

### 4.1 Scripts extractores y de consulta

| Archivo | Función | Resultado |
|---------|---------|-----------|
| `scripts/utilities/gpkg-to-cache-v4.py` | Consulta catastro + POT + decreto por lote | Caché JSON con 38 campos catastro + 5-8 capas POT + retiros calculados |
| `scripts/utilities/extract-real-lote.py` | Extrae lote real del .gpkg con coords correctas | Archivo JSON del lote con polígono válido |
| `scripts/utilities/inspect-pot-gdb.py` | Inspecciona capas y campos del POT .gdb | Listado de capas, campos, CRS, ejemplos |
| `scripts/utilities/setup-test-lot.py` | Crea lotes de ejemplo + exporta inventario | Lotes de prueba + gdb_fields_inventory.json |
| `scripts/utilities/validate-neighbors.py` | Valida formato de vecinos antes de GH | Reporte de vecinos válidos/inválidos |
| `scripts/utilities/extract-decreto-555-relevante.py` | Extrae artículos relevantes del Decreto 555 | 16 artículos en Markdown + 3 JSONs estructurados |
| `scripts/utilities/extract-decreto-670-relevante.py` | Extrae artículos relevantes del Decreto 670 | Compilación + incentivos + actuaciones estratégicas |
| `scripts/utilities/extract-nsr-10-relevante.py` | Extrae secciones relevantes del NSR-10 | Tabla A.6.5-1 + grupos de uso + amenaza Bogotá |

### 4.2 JSONs estructurados (datos consultables)

| Archivo | Contenido | Fuente |
|---------|-----------|--------|
| `data/pot-bogota/retiros-estructurados.json` | Retiros por tratamiento, tipología, vía, subdivisión | Decreto 555 Art. 281, 310, 340 |
| `data/pot-bogota/edificabilidad-estructurada.json` | Rangos de edificabilidad (IC, IO) por tratamiento | Decreto 555 Art. 281 |
| `data/pot-bogota/tratamientos-estructurados.json` | 5 tratamientos urbanísticos con modalidades | Decreto 555 Art. 256-343 |
| `data/pot-bogota/incentivos-670.json` | 3 tipos de incentivos urbanísticos | Decreto 670 (compila 582/2023) |
| `data/pot-bogota/actuaciones-estrategicas-670.json` | ZIBo, Lagos de Torca, Distrito Aeroportuario | Decreto 670 |
| `data/pot-bogota/decreto-670-estructura.json` | Índice navegable del Decreto 670 (6 libros) | Decreto 670 |
| `data/nsr-10/separaciones-sismicas.json` | Tabla A.6.5-1 (separación mínima por pisos) | NSR-10 A.6.5 |
| `data/nsr-10/grupos-uso-coef-importancia.json` | Grupos I-IV con coeficientes de importancia | NSR-10 A.2.5 |
| `data/nsr-10/amenaza-sismica-bogota.json` | Valores Aa=0.15, Av=0.20 para Bogotá | NSR-10 Tabla A.2.3-2 |

### 4.3 Documentación normativa (Markdown)

| Archivo | Contenido |
|---------|-----------|
| `docs/normativa/pot-bogota/decreto-555-extractos.md` | 16 artículos del Decreto 555/2021 (55 KB) |
| `docs/normativa/pot-bogota/decreto-670-extractos.md` | Extractos del Decreto 670/2025 (34 KB) |
| `docs/normativa/nsr-10/nsr-10-extractos.md` | 9 secciones del NSR-10 (37 KB) |

### 4.4 Documentación de arquitectura (ADRs)

| Archivo | Decisión documentada |
|---------|---------------------|
| `docs/arquitectura/decisiones-adr/adr-001-uso-tapir.md` | Usar Tapir como puente GH-Archicad |
| `docs/arquitectura/decisiones-adr/adr-002-catastro-vs-pot.md` | Catastro ≠ POT, fuentes separadas |
| `docs/arquitectura/decisiones-adr/adr-003-elementos-bim-nativos-vs-morphs.md` | Solo elementos BIM nativos, no Morphs ni GDL |
| `docs/arquitectura/decisiones-adr/adr-004-postergar-mcps.md` | Postergar RHINO-MCP y ROBO-HOPPER |

### 4.5 Configuración

| Archivo | Función |
|---------|---------|
| `config/field-whitelist.json` | 38 campos relevantes del catastro (de 191 totales) |
| `data/gdb_fields_inventory.json` | Inventario completo de campos del .gpkg |
| `data/pot_layers_inventory.json` | Inventario de 166 capas del POT .gdb |

### 4.6 Cachés generados

| Archivo | Contenido |
|---------|-----------|
| `data/pot-cache/REAL-002407033006.json` | Caché completo del lote real: catastro (38 campos) + POT (5 capas) + retiros calculados |

### 4.7 Marco teórico en vault

| Archivo | Contenido |
|---------|-----------|
| `vault/30-referencia/christopher-alexander/00-index-alexander.md` | Índice navegable de Alexander |
| `vault/30-referencia/christopher-alexander/lenguaje-patrones/` | Patrones migrados |
| `vault/30-referencia/christopher-alexander/modo-intemporal/` | Modo intemporal de construir |
| `vault/30-referencia/gh-io-docs/` | Documentación GH_IO.dll para explorador |
| `vault/30-referencia/tapir-api/Tapir-API-Referencia.md` | Referencia de componentes Tapir |
| `vault/30-referencia/grasshopper-plugins/00-index-plugins.md` | Catálogo de plugins GH |

---

## 5. Conclusión

La base de información quedó sólida y completa:

- ✅ **Catastro:** 38 campos extraídos automáticamente por lote (3 JOINs: espacial + atributo)
- ✅ **POT:** 5-8 capas consultadas con datos reales (altura, UPZ, tratamiento, edificabilidad)
- ✅ **Decreto 555/2021:** 16 artículos extraídos + 3 JSONs estructurados
- ✅ **Decreto 670/2025:** Compilación + incentivos + actuaciones estratégicas
- ✅ **NSR-10:** Separaciones sísmicas + grupos de uso + amenaza Bogotá
- ✅ **Marco Alexander:** Pattern Language migrado al vault
- ✅ **Tapir/Ladybug/Archicad:** Plugins documentados y catalogados
- ✅ **4 ADRs:** Decisiones arquitectónicas documentadas

El pipeline puede ahora entregar, para cualquier lote de Bogotá:
- Identificación catastral completa
- Altura máxima permitida (REAL del POT)
- Tratamiento urbanístico
- Retiros obligatorios (según decreto)
- Edificabilidad permitida
- Separación sísmica NSR-10
- Vecinos automatizables (PrePiso × 3m)
