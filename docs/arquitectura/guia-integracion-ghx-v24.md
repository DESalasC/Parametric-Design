# Guía de Integración — Canvas F1_Contexto para v24 (ADR-008)

**Fecha:** 2026-08-10
**Archivo base:** `gh-definitions/F1_Contexto_v07a.gh`

---

## Cambios requeridos en el canvas de Grasshopper

### 1. Agregar entrada: vias_manuales desde ArchiCAD

Usar un componente **Tapir > Get Elements from Layer** para cada capa de contexto:

```
Get Elements from Layer (70-30-20_Andenes_preexistentes) ─┐
Get Elements from Layer (70-50-10_Zonas_verdes_publicas)  ─┤
Get Elements from Layer (00-20-20_Elementos_entorno...)   ─┤
                                                           ├─ Merge ─→ vias_manuales
```

### 2. Conectar vias_oficiales (desde F1_CONTEXTO_POT)

El script `F1_CONTEXTO_POT_v04.py` debe exponer una salida `vias_oficiales` con
las curvas de la capa Eje_vial del POT extraídas del JSON de contexto.

### 3. Reemplazar F1_NORMATIVA_APLICAR

| Componente | Entrada anterior (v22) | Entrada nueva (v24) |
|------------|----------------------|---------------------|
| lot_polygon | lot_curve | lot_curve |
| vias_oficiales | *(no existía)* | desde F1_CONTEXTO_POT |
| vias_manuales | *(no existía)* | desde Merge Tapir |
| patio_curve | patios_curves | patios_curves |
| json_path | json_path | json_path |
| floor_height_user | floor_height | floor_height |
| ~~sides_table_json~~ | desde LADOS_CONFIGURAR | **ELIMINADO** |

### 4. Pipeline resultante en el canvas

```
json_path ─→ F1_CONTEXTO_POT_v04
               ├─ lot_curve
               ├─ neighbors_curves
               ├─ topo_mesh
               └─ vias_oficiales ──────────────────┐
                                                     │
Tapir: Get Elements (70-30-20) ─┐                    │
Tapir: Get Elements (70-50-10) ─┼─ Merge ────────────┼─→ vias_manuales
Tapir: Get Elements (00-20-20) ─┘                    │
                                                     │
               lot_curve ────────────────────────────┤
                                                     │
               ┌─────────────────────────────────────┘
               ▼
          Merge (vias_oficiales + vias_manuales)
               │
               ▼
          F1_NORMATIVA_APLICAR_v24
               │
               ├─ envelope_curve ──→ Tapir → ArchiCAD
               ├─ sides_table_json (diagnóstico)
               └─ mensaje
```

### 5. Validación esperada

Con vías manuales dibujadas (Carrera 49 + calles faltantes), se espera:
- AAA0127AZPA: 3-4 frentes detectados (los que dan a la Carrera 49 y calle transversal)
- El resto clasificados como Lateral (retiro 0m) o Posterior (retiro 3m)
- IO calculado coherente con los resultados anteriores (~0.41)

---

## Notas

- El archivo `F1_Contexto_v07a.gh` es la base recomendada (avance significativo sobre v07)
- Probar primero con el lote AAA0127AZPA que ya tiene resultados validados
- La ortofoto en capa `00-20-20_Foto_Aerea_Referencia` sirve para verificar que las vías dibujadas coinciden con la realidad
