# ADR-005: Corrección de interpretación del campo ALTURA en POT

**Fecha:** 2026-08-03
**Estado:** Aceptado

## Contexto

Durante la validación de datos del POT para el lote 002407033006 (UPZ Venecia), se detectó que el script `gpkg-to-cache-v4.py` estaba extrayendo un valor de `altura_maxima_m = 150.0`. 

Una revisión manual reveló que 150 metros de altura máxima (equivalente a ~50 pisos) es incoherente para un lote residencial de 193 m² en Bosa. 

Al consultar directamente la geodatabase del POT (`Area_elevacion_maxima`), se encontró que los valores del campo `ALTURA` van de 0.0 a 150.0. 

## Decisión

El campo `ALTURA` de la capa `Area_elevacion_maxima` **NO representa la altura máxima de edificación en metros**. Representa una cota absoluta de coronamiento (elevación sobre el nivel del mar, AMSL) o un código de rango, no una altura relativa de edificación.

La altura máxima de edificación en el POT de Bogotá se define en el Decreto 555/2021 principalmente en **número de pisos** (Artículos 281, 310), y está asociada al `TratamientoUrbanistico` y al `Rango_edificabilidad`, no a una capa de elevación absoluta.

### Acciones tomadas en el código

1. Se modificó `scripts/utilities/gpkg-to-cache-v4.py`:
   - El campo `altura_maxima_m` en el JSON de salida se establece como `null` cuando el valor crudo supera umbrales razonables (ej. > 60m).
   - Se agregó el campo `altura_maxima_raw` que conserva el valor original extraído de la capa POT para fines de trazabilidad y revisión manual.
   - Se extrajeron los campos `NORMATIVA` y `RESTRICCION` de la capa POT para proporcionar contexto legal.

2. Se documentó en `data/pot-bogota/decreto-555-extractos.md` que la altura se define en pisos según el rango de edificabilidad (Art. 281).

## Consecuencias

### Positivas
- Se evita propagar un error crítico de interpretación normativa a las fases de Masa (F3) y BIM (F5).
- Se sienta el precedente de validar los datos crudos contra la lógica urbana antes de integrarlos al pipeline.
- El pipeline es ahora más robusto y consciente de las limitaciones de los datos crudos.

### Negativas
- El pipeline de Fase 1 queda temporalmente sin un valor automático de `altura_maxima_m`.
- Se requerirá una futura iteración para mapear correctamente los "rangos de edificabilidad" y "tratamientos" a un número de pisos, y luego a metros (pisos × 3.0m).

## Referencias
- [[adr-002-catastro-vs-pot]]
- [[resumen-1-base-informacion]]
- Artículo 281 del Decreto 555/2021
