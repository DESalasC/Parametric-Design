# Fase 1 — Contexto Normativo y Lote

Establece el contexto normativo completo del lote (POT Decreto 555/2021 + NSR-10), clasifica los
lados, aplica retiros y patios, y genera la envolvente edificable máxima para Fase 2.

## Pipeline modular vigente (v26, dos etapas)

### ETAPA 1 — Datos en bruto → ArchiCAD (clasificación manual)
```
fetch-urban-context-v6 (scripts/utilities) → data/pot-cache/<CHIP>-contexto.json
  → F1_ETAPA1_CONTEXTO_v01.py (GH: geometría + layers ArchiCAD vía Tapir)
  → MANUAL en ArchiCAD: clasificar vías, ejes, andenes, zonas verdes, vecinos (Morph)
```

### ETAPA 2 — Geometría clasificada → ocupación y patios
```
ArchiCAD (layers) → Tapir GetElements → GH
  → F1_ETAPA2_LADOS_v02.py      (clasificación de lados: regla 15m + paralelismo)
  → F1_ETAPA2_PATIO_v01.py      (patios de aislamiento en vértices vecino-vecino)
  → F1_ETAPA2_NORMATIVA_v02a.py (retiros diferenciados + resta booleana de patio + IO/IC/altura)
  → envelope_curve → Fase 3 (VOLUM_GENERADOR)
```

**Vigentes:** `F1_ETAPA1_CONTEXTO_v01` · `F1_ETAPA2_LADOS_v02` · `F1_ETAPA2_PATIO_v01` ·
`F1_ETAPA2_NORMATIVA_v02a`. Utilidades: `F1_DESPLAZAR_ORIGEN_v01`, `F1_VECINOS_ANALISIS_*`,
`F1_VALIDADOR_CRUZADO_v01`, `F1_PATIO_DISCONTINUIDAD_v*` (variantes de patio).

## Archivo

El linaje anterior (`F1_CONTEXTO_POT_*`, `F1_LADOS_CONFIGURAR_*`, `F1_LADOS_CLASIFICAR_*`,
`F1_NORMATIVA_APLICAR_*`, `F1_NORMATIVA_DIRECTA_*`, `F1_NORMATIVA_LEER_*`, `F1_PATIO_ESQUINA_*`,
`F1_PATIO_VECINO_*`, `F1_PATIO_DIRECTO_*`, `F1_NEW_LAYERS_*`) se archivó en **`_legacy/`**
(2026-08-13) y **no debe usarse** en definiciones nuevas. No eliminar: contiene el historial.

## Tests

```powershell
pytest tests\   # tests/test_fetch_contexto.py, test_normativa_calculos.py, test_patio_esquina.py
```

## Resultados lote AAA0127AZPA (Fase 1)

| Parámetro | Valor |
|---|---|
| CHIP / UPZ | AAA0127AZPA · El Prado |
| Tratamiento | Consolidación |
| Área lote | 315–450 m² (según fuente) |
| Altura POT | 11,4 m · 4 pisos (entrepiso 2,85 m) |
| GFA Fase 1 | 632,7 m² (verificado) — **alternativa curaduría: 1054,49 m²** (ver `data/fase-2-demanda/`) |
| Patio de esquina | 3,0 × 3,0 m (lotes < 500 m², Continua, ≤ 5 pisos) |

## Documentación

Vault de Obsidian → `20-fases\fase-1-contexto\` (especificaciones del canvas, resúmenes de sesión)
y `10-arquitectura\` (pipeline-modular-fase1-v25, guías GHX, ADR-008).
