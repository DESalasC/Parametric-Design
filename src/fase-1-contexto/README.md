# Fase 1 - Contexto

Establece el contexto normativo del lote.

## Scripts oficiales (v01)

- **F1_CONTEXTO_POT_v01.py** (530 líneas) - base del sistema layer0
- **F1_LADOS_CONFIGURAR_v01.py** (303 líneas) - base del sistema layer1
- **F1_VALIDADOR_CRUZADO_v01.py** (329 líneas) - único, del sistema

## Scripts para comparar (referencia)

- _reference_CONTEXTO_POT_v09_desparam.py (251 líneas)
- _reference_LADOS_CONFIGURAR_v04_desparam.py (95 líneas)

## VECINOS_ANALISIS - REVISAR

⚠️ **Atención:** Hay dos versiones con tamaños muy diferentes:
- F1_VECINOS_ANALISIS_v01_sistema.py (**58 líneas** - verificar si está completo)
- F1_VECINOS_ANALISIS_v01_desparam.py (130 líneas - más completo)

**Acción:** abrir ambos y decidir cuál es la base oficial.

## Adaptación pendiente

Después de consolidar, los scripts oficiales deben actualizarse para leer:
- `data/pot-cache/<predio-id>.json` (caché precalculado)
- `data/pot-bogota/retiros-estructurados.json`
- `data/nsr-10/separaciones-sismicas.json`
