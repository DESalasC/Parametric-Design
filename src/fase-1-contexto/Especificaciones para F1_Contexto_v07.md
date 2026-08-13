Especificaciones para F1_Contexto_v07.gh

Basado en el análisis de las versiones anteriores (v03-v06) y la nueva componente Python F1_LADOS_CONFIGURAR_v07.py, aquí tienes las especificaciones detalladas para crear la definición de Grasshopper F1_Contexto_v07.gh:

Visión General

F1_Contexto_v07.gh debe ser una evolución directa de F1_Contexto_v06.gh, manteniendo la misma estructura general pero actualizando el componente de clasificación de lados para usar la nueva lógica mejorada que combina distancia y alineación angular.

Componentes Necesarios

1. Entradas (Igual que v06)

- lot_polygon (Curve): Polígono cerrado del lote (Item Access)
- lot_segments (Curve[]): Segmentos que forman el perímetro del lote (List Access)
- lot_midpoints (Point3d[]): Puntos medios de cada segmento (List Access)
- street_curves (Curve[]): Curvas de las vías cercanas (List Access)
- magna_eastings (Number): Coordenada Este en sistema MAGNA-SIRGAS
- magna_northings (Number): Coordenada Norte en sistema MAGNA-SIRGAS
- json_path (String): Ruta al JSON de cache del lote (opcional, para datos de altura)

2. Nueva Incorporación: F1_LADOS_CONFIGURAR_v07.py

Reemplazar el componente F1_LADOS_CONFIGURAR_v06.py por el nuevo F1_LADOS_CONFIGURAR_v07.py que acabo de crear.

Entradas del componente de clasificación:
- lot_polygon (Curve, Item Access)
- lot_segments (Curve[], List Access)
- lot_midpoints (Point3d[], List Access)
- street_curves (Curve[], List Access)

Salida del componente de clasificación:
- sides_table_json (String): JSON con clasificación de cada lado

3. Componentes Subsecuentes (Mantenercompatibilidad)

Los componentes que siguen al clasificador de lados deben mantener las mismas entradas/salidas:
- F1_PATIO_VECINO_v04.py (o versiones posteriores)
- F1_NORMATIVA_APLICAR_v22.py (o versiones posteriores)
- Otros componentes de la fase 1 según el flujo existente

Estructura del Flujo de Trabajo

[Entradas]
    │
    ├──── lot_polygon ────► F1_LADOS_CONFIGURAR_v07.py ────► sides_table_json
    │
    ├──── lot_segments ───┘
    │
    ├──── lot_midpoints ─┘
    │
    └──── street_curves ─┘
    │
    │
    ▼
sides_table_json ◄──────────────────────────────┐
    │                                          │
    │                                          ▼
    │                                  F1_PATIO_VECINO_v04.py
    │                                          │
    ▼                                          │
[Otros datos de contexto] ◄───────────────────┘
    │
    ▼
F1_NORMATIVA_APLICAR_v22.py
    │
    ▼
[Salidas finales: volumetría, retiros, etc.]

Detalles de Implementación del Nuevo Clasificador

El componente F1_LADOS_CONFIGURAR_v07.py implementa esta lógica mejorada:

1. Cálculo de distancias (igual que v06):
  - Para cada segmento del lote, calcular distancia mínima a cualquier calle
  - Obtener min_d y max_d de todas las distancias
2. Umbral adaptativo:
lot_width = max_d - min_d
adaptive_threshold = min_d + max(3.0, lot_width * 0.15)
3. Criterio de alineación angular (NUEVO en v07):
  - Calcular centroide del lote
  - Para cada segmento, calcular vector desde centroide al punto medio del segmento
  - Para cada calle cercana, obtener tangente en punto más cercano al segmento
  - Calcular ángulo entre el vector lote→segmento y la tangente de la calle
  - Si el ángulo mínimum es < 45°, el segmento está "mirando hacia" la calle
4. Clasificación final:
  - Un segmento es "Frontal" SOLO si cumple AMBOS criterios:
      - Está dentro del umbral de distancia (dist <= adaptive_threshold)
    - Está alineado suficientemente con alguna calle (ángulo < 45°)
  - De lo contrario, es "Lateral"

Beneficios Esperados

Esta solución resuelve específicamente el problema reportado:
- En lotes rectangulares: El lado frontal (mirando a la calle) será clasificado como frontal, mientras que el lado posterior (aunque esté a similar distancia) será clasificado como lateral porque mira en dirección opuesta a la calle
- Elimina falsos positivos: Ya no clasificaremos incorrectamente segmentos traseros o laterales como frontales simplemente porque estén a una distancia similar a la calle
- Mantiene compatibilidad: Las entradas y salidas son idénticas a v06, por lo que no se rompe el flujo existente

Validación Sugerida

Después de crear F1_Contexto_v07.gh, probar con:
1. lote-chapinero.json (ejemplo proporcionado)
2. Lotes rectangulares simples donde se sabe cuál lado debería ser frontal
3. Lotes en esquina para verificar que se detecten múltiples frentes correctamente
4. Comparar resultados con F1_Contexto_v06.gh para ver la mejora en clasificación

Próximos Pasos

1. En Rhino/Grasshopper, abre F1_Contexto_v06.gh
2. Usa "File > Save As..." para crear F1_Contexto_v07.gh
3. Reemplaza el componente F1_LADOS_CONFIGURAR_v06.py por F1_LADOS_CONFIGURAR_v07.py
4. Verifica que todas las conexiones se mantengan correctamente
5. Guarda y prueba con datos de ejemplo
6. Una vez validado, puedes considerar avanzar a F1_Contexto_v08.gh si se necesitan más mejoras

