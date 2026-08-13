# ADR-008: Clasificación Espacial Híbrida — Feedback Loop ArchiCAD ↔ Grasshopper

**Fecha:** 2026-08-11
**Estado:** Aceptado
**Contexto**: Fase 1 - Contexto y Normativa (Etapa 2)

---

## Contexto

En el modelado paramétrico de lotes en Bogotá, la geodatabase (GDB) del POT presenta datos incompletos y ruidosos (calles no digitalizadas, ejes perpendiculares que cruzan esquinas, huecos en alturas). 

Al intentar clasificar los lados del lote mediante simple "distancia a vías", el algoritmo sufría de inundación de falsos positivos: las vías que cruzaban perpendicularmente la esquina del lote se consideraban colindantes, marcando todos los lados como "Frontal" o "EspacioPublico". Esto impedía que el sistema identificara el fondo del lote (Vértice N) como un área colindante con vecinos, lo que a su vez hacía imposible generar el patio de aislamiento.

Además, la resta del patio se calculaba matemáticamente, entregando un polígono sin el hueco físico necesario para la extrusión 3D.

## Decisión

Se adopta un modelo de **Clasificación Espacial Híbrida** con las siguientes reglas estrictas en el script F1_ETAPA2_LADOS_v02a.py:

### Regla de Proximidad (Vertice A y Vertice N)

1. Vertice A (Frente): Vértice del lote con la menor distancia a cualquier eje de vía.
2. Vertice N (Fondo): Vértice con la mayor distancia a las vías. Es el origen geométrico del patio.

### Tolerancia y Paralelismo Estricto (Anti-Falsos Positivos)

Para que una curva externa (vía, vecino, espacio público) se considere colindante con un segmento del lote, debe cumplir:

1. **Tolerancia de distancia**: Reducida a 0.15m (estándar catastral).
2. **Validación de paralelismo**: El vector tangente de la curva externa debe formar un ángulo menor a 20° con el segmento del lote. Las curvas perpendiculares (ej. vías que cruzan la esquina) se ignoran.

### Override del Vértice N

Si un lado del lote comparte el Vértice N (fondo) y NO toca vías de manera contundente:

1.  Si el sistema detecta polígonos de vecinos, el lado se fuerza a "Lateral".
2.  Si no hay vecinos, se asume "Posterior". Esto garantiza que el componente F1_ETAPA2_PATIO_v01.py tenga la topología necesaria (dos lados laterales) para generar el rectángulo de aislamiento.

### Resta Booleana de Patios

La envolvente máxima habitable (envelope_curve) se construye aplicando retiros normativos y restando los patios mediante rg.Curve.CreateBooleanDifference. Esto asegura que la curva de salida tenga el hueco físico real, lista para modelado BIM (Morph) o extrusión de masa.

### Feedback Loop ArchiCAD ↔ Grasshopper

La clasificación no depende solo del GDB. Las vías y zonas verdes se obtienen de dos fuentes combinadas:

1. **Oficial**: vias_oficiales del JSON, espacio_publico (capas POT GDB).
2. **Manual**: Dibujadas en ArchiCAD (capas 00-20-20, 70-30-20, 70-50-10) y traídas a Grasshopper vía plugins Archicad/Tapir.

### Capas ArchiCAD para el feedback loop

| Capa | Uniclass | Propósito |
|------|----------|-----------|
| `00-00-10_Lote_proyecto`         | EF_00_00_10 | Predio existente      |
| `00-10-20_Elementos_referencia`  | EF_00_10_20 | Otros elementos a ner en cuenta |
| `10-20-10_Topografia`            | EF_10_10_10 | Topografia existente  |
| `70-30-20_Andenes_preexistentes` | EF_70_30_20 | Andenes existentes    |
| `70-20-30_Volumetrias_vecinas`   | EF_70_20_20 | Morph de volumenes colindantes del predio - Para NSR-10 |
| `70-50-10_Zonas_verdes_publicas` | EF_70_50_10 | Parques, separadores, zonas verdes | 
| `00-20-20_Foto_Aerea_Referencia` | Ac_10_30 | Imagen satelital de referencia (50% transparencia) |
| `00-20-20_Elementos_entorno_urbano` | Ac_10_30 | Calles faltantes | 
| `00-20-20_Foto_Aerea_Referencia` | EF_10_30 | Ortofoto del predio | 

**Nota sobre nomenclatura:** Usar guiones medios `-` en vez de puntos `.` porque
ArchiCAD tiene problemas con la sintaxis `xx.xx.xx`. Formato: `XX-XX-XX_Nombre`.

### Imagen aérea

La ortofoto se obtiene con `fetch-aerial-photo-v6.py` y se coloca en la capa
`00-20-20_Foto_Aerea_Referencia` como fondo de referencia para verificar
alineación de andenes, zonas verdes y calles dibujadas manualmente.

## Consecuencias

**Positivas:**
- Eliminación del ruido topológico en esquinas de lotes.
- Garantía topológica de generación de patios en el fondo del lote.
- La geometría final de la Fase 1 es físicamente exacta para modelado 3D.

**Negativas:**
- Requiere trabajo manual inicial por predio (dibujar calles/andenes faltantes)
- El feedback loop añade un paso al flujo de trabajo
- La ortofoto requiere conexión a servicios IDECA/Catastro
- Requiere que los modelos de vecinos y vías manuales en ArchiCAD estén razonablemente alineados (paralelos) al lote para ser detectados por la tolerancia de 20°.

**Riesgos mitigados:**
- Calles no digitalizadas → se dibujan manualmente
- Alturas de vecinos faltantes → se miden/estiman en ArchiCAD
- Clasificación incorrecta de frentes → reglas colindancia y vertices A y N 

## Referencias

- Decreto 555/2021 — POT Bogotá
- Uniclass 2015 — Sistema de clasificación BIM
- GuBIMclass v3 — Adaptación colombiana de Uniclass
