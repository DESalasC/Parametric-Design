# Fase 1 - Contexto Normativo y Lote

Establece el contexto normativo completo del lote, aplica retiros,
y gestiona condiciones especiales como lotes de esquina.

## Pipeline de scripts (orden de ejecucion en Grasshopper)

```
                    ┌─────────────────────┐
                    │  Datos del cache    │
                    │  (fetch-urban-      │
                    │   context.py)       │
                    └────────┬────────────┘
                             │ JSON
                             ▼
┌────────────────┐  ┌───────────────────┐  ┌──────────────────┐
│ F1_CONTEXTO_   │  │ F1_LADOS_         │  │ F1_VECINOS_      │
│ POT_v04        │  │ CONFIGURAR_v03    │  │ ANALISIS_v01     │
│ (normativa)    │  │ (clasificacion    │  │ (alturas         │
│                │  │  de lados)        │  │  vecinos)        │
└───────┬────────┘  └────────┬──────────┘  └────────┬─────────┘
        │                    │                       │
        │         sides_table_json                   │
        │                    │                       │
        ▼                    ▼                       ▼
┌──────────────────────────────────────────────────────────┐
│                   F1_PATIO_ESQUINA_v01                    │
│  Si hay 2+ frentes adyacentes:                           │
│  - Detecta esquina de calles (donde convergen los frentes)│
│  - Localiza esquina interior opuesta (donde va el patio)  │
│  - Calcula tamano del patio segun altura (3x3m default)   │
│  - Genera geometria del patio orientada hacia adentro     │
└──────────────────────────┬───────────────────────────────┘
                           │ patio_curve
                           ▼
┌──────────────────────────────────────────────────────────┐
│                 F1_NORMATIVA_APLICAR_v22                  │
│  - Aplica retiros diferenciados por lado (no uniforme)    │
│  - Reconstruye huella edificable por segmento             │
│  - Sustrae patio de esquina de la huella                  │
│  - Calcula IO, IC, altura, pisos                          │
└──────────────────────────┬───────────────────────────────┘
                           │ envelope_curve
                           ▼
                    ┌──────────────────┐
                    │ F3_VOLUM_        │
                    │ GENERADOR_v04    │
                    │ (extrusion 3D)   │
                    └──────────────────┘
```

## Scripts oficiales

### Principales

| Script | Lineas | Funcion |
|--------|--------|---------|
| [F1_CONTEXTO_POT_v04_sistema.py](F1_CONTEXTO_POT_v04_sistema.py) | 530 | Analisis normativo POT desde GeoJSONs |
| [F1_LADOS_CONFIGURAR_v03_sistema.py](F1_LADOS_CONFIGURAR_v03_sistema.py) | 303 | Clasificacion automatica de lados del lote |
| [F1_PATIO_ESQUINA_v01.py](F1_PATIO_ESQUINA_v01.py) | ~320 | **NUEVO** - Patio de aislamiento para lotes de esquina |
| [F1_NORMATIVA_APLICAR_v22.py](F1_NORMATIVA_APLICAR_v22.py) | ~400 | **ACTUALIZADO** - Motor normativo con soporte esquina |
| [F1_VECINOS_ANALISIS_v02_sistema.py](F1_VECINOS_ANALISIS_v02_sistema.py) | 58 | Analisis de alturas vecinas (pendiente de revision) |
| [F1_VALIDADOR_CRUZADO_v01.py](F1_VALIDADOR_CRUZADO_v01.py) | 329 | Validacion cruzada de parametros normativos |

### De referencia (no usar directamente)

| Script | Lineas | Nota |
|--------|--------|------|
| _reference_CONTEXTO_POT_v09_desparam.py | 251 | Version antigua, usa rhinoscriptsyntax (prohibido) |
| _reference_LADOS_CONFIGURAR_v04_desparam.py | 95 | Version antigua |

## Tests

| Archivo | Tipo | Estado |
|---------|------|--------|
| [tests/test_patio_esquina.py](../../tests/test_patio_esquina.py) | Unitario (logica pura) | ✅ 8/8 pasan |

Ejecutar:
```powershell
python tests\test_patio_esquina.py
```

## Resultados para lote AAA0127AZPA

| Parametro | Valor |
|-----------|-------|
| CHIP | AAA0127AZPA |
| UPZ | El Prado |
| Tratamiento | Consolidacion |
| Area lote | 315.0 m² |
| Altura maxima POT | 11.4 m |
| Pisos permitidos | 4 (entrepiso 2.85 m) |
| Frentes detectados | 4 (segmentos 5, 6, 7, 8) |
| Esquina de calles | Vertice 6 |
| Esquina interior (patio) | Vertice 1 |
| Tamano patio | 3.0 × 3.0 m |
| Retiro promedio | 2.4 m |
| Area edificable est. | 130.7 m² |
| IO estimado | 0.41 (max 0.70) ✅ |

## Proximo lote: La Candelaria

- Direccion: KR 1 12 D 54
- Codigo lote: 0031033519
- Codigo catastral: AAA0030JKOE
- Area: 900+ m²
- Pendiente: significativa
- Accesos: 2 carreras diferentes
- Normativa: Centro Historico (restricciones especiales)
