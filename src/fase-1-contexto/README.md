# Fase 1 - Contexto

Scripts para establecer el contexto normativo del lote.

## Scripts migrados (base de referencia)

### CONTEXTO_POT (dos versiones - revisar y consolidar)
- F1_CONTEXTO_POT_v04_sistema.py - del sistema (layer0_territorial_base)
- F1_CONTEXTO_POT_v09_desparam.py - de DesParametrico (más reciente)

**Acción pendiente:** comparar ambas versiones y consolidar en F1_CONTEXTO_POT_v01.py
que use los JSONs estructurados (data/pot-bogota/, data/nsr-10/).

### LADOS_CONFIGURAR (dos versiones - revisar y consolidar)
- F1_LADOS_CONFIGURAR_v03_sistema.py - del sistema
- F1_LADOS_CONFIGURAR_v04_desparam.py - de DesParametrico (más reciente)

**Acción pendiente:** comparar y consolidar en F1_LADOS_CONFIGURAR_v01.py
que use data/pot-bogota/retiros-estructurados.json.

### VECINOS_ANALISIS (dos versiones - revisar y consolidar)
- F1_VECINOS_ANALISIS_v01_desparam.py - de DesParametrico
- F1_VECINOS_ANALISIS_v02_sistema.py - del sistema (más reciente)

**Acción pendiente:** comparar y consolidar en F1_VECINOS_ANALISIS_v01.py
que use data/nsr-10/separaciones-sismicas.json.

### VALIDADOR_CRUZADO
- F1_VALIDADOR_CRUZADO_v01.py - solo existe en sistema

## Próximos pasos

1. Comparar versiones duplicadas (CONTEXTO, LADOS, VECINOS)
2. Consolidar cada par en una versión oficial F1_*_v01.py
3. Adaptar para leer de los JSONs estructurados en data/
4. Crear tests en 	ests/fase-1-contexto/

## JSONs disponibles para alimentar estos scripts

- data/pot-cache/<predio-id>.json - caché precalculado por gpkg-to-cache-v4.py
- data/pot-bogota/retiros-estructurados.json - retiros por tratamiento
- data/pot-bogota/edificabilidad-estructurada.json - edificabilidad por rango
- data/nsr-10/separaciones-sismicas.json - separaciones NSR-10 A.6.5
- data/nsr-10/amenaza-sismica-bogota.json - valores Aa/Av Bogotá
