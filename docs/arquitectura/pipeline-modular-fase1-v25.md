# Pipeline Fase 1 v25 — Arquitectura Simplificada (4 lados virtuales)

---

## Concepto clave

El lote tiene 9+ vertices topograficos pero solo 4 esquinas reales.
El componente **Discontinuity** de Grasshopper detecta cambios bruscos de direccion
y devuelve solo las 4 esquinas principales → 4 "lados virtuales".

Esto simplifica drasticamente la clasificacion y el calculo de patios.

---

## Pipeline

```
                            ┌─────────────────────────────────┐
                            │     F1_CONTEXTO_POT_v05         │
                            │  Entrada: json_path             │
                            │                                 │
                            │  Salidas:                       │
                            │  ├─ lot_curve (9 vertices)      │
                            │  ├─ vias_oficiales (42)         │
                            │  ├─ topo_mesh                   │
                            │  ├─ altura_max_pot              │
                            │  ├─ tratamiento                 │
                            │  ├─ rango_edificabilidad        │
                            │  ├─ sector_normativo            │
                            │  ├─ espacios_publicos (12)      │
                            │  └─ ...                         │
                            └───────────┬─────────────────────┘
                                        │
                      ┌─────────────────┼─────────────────┐
                      │                 │                  │
                      ▼                 ▼                  │
              ┌──────────────┐  ┌──────────────┐          │
              │ Discontinuity │  │  Merge Vias   │          │
              │  (GH nativo)  │  │  (GH nativo)  │          │
              │               │  │               │          │
              │ lot_curve → D │  │ D0: oficiales │          │
              │ 4 esquinas    │  │ D1: manuales  │          │
              └───────┬───────┘  └───────┬───────┘          │
                      │                  │                  │
                      │    ┌─────────────┘                  │
                      │    │                                │
                      ▼    ▼                                │
              ┌─────────────────────────┐                   │
              │ F1_LADOS_CLASIFICAR_v02 │                   │
              │                         │                   │
              │ lot_vertices (4 pts)    │                   │
              │ vias (oficial+manual)   │                   │
              │                         │                   │
              │ → sides_table_json      │                   │
              │ → lot_simplificado (4v) │                   │
              └───────────┬─────────────┘                   │
                          │                                 │
              ┌───────────┴───────────┐                     │
              │                       │                     │
              ▼                       ▼                     │
    ┌────────────────────┐  ┌──────────────────────┐        │
    │ F1_PATIO_v03       │  │ F1_NORMATIVA_v25     │        │
    │                    │  │                      │        │
    │ lot_vertices (4)   │  │ lot_simplificado (4v)│        │
    │ sides_table_json   │  │ sides_table_json     │        │
    │ altura_max_pot     │  │ patio_curve          │        │
    │                    │  │ altura_max_pot       │        │
    │ → patios_curves    │  │ tratamiento          │        │
    └────────────────────┘  │ rango_edificabilidad │        │
                            │ floor_height_user    │        │
                            │                      │        │
                            │ → envelope_curve     │        │
                            └──────────────────────┘        │
```

---

## Instrucciones en Grasshopper

### Paso 1: CONTEXTO_POT_v05
- GhPython con `F1_CONTEXTO_POT_v05.py`
- Entrada: `json_path` (Panel) → ruta del JSON

### Paso 2: Discontinuity
- Componente nativo GH: **Discontinuity**
- Entrada: `lot_curve` (desde CONTEXTO_POT)
- Salida `D` (Discontinuity points) → 4 vertices principales

### Paso 3: Merge de vías
- Componente **Merge**
- D0: `vias_oficiales` (desde CONTEXTO_POT)
- D1: vías manuales desde Tapir (ArchiCAD)

### Paso 4: LADOS_CLASIFICAR_v02
- GhPython con `F1_LADOS_CLASIFICAR_v02.py`
- `lot_vertices` ← Discontinuity `D`
- `vias` ← Merge `R`

### Paso 5: PATIO_DISCONTINUIDAD_v03
- GhPython con `F1_PATIO_DISCONTINUIDAD_v03.py`
- `lot_vertices` ← Discontinuity `D` (mismos 4 puntos)
- `sides_table_json` ← LADOS_CLASIFICAR `sides_table_json`
- `altura_max_pot` ← CONTEXTO_POT `altura_max_pot`

### Paso 6: NORMATIVA_APLICAR_v25
- GhPython con `F1_NORMATIVA_APLICAR_v25.py`
- `lot_polygon` ← LADOS_CLASIFICAR `lot_simplificado` (4 vertices)
- `sides_table_json` ← LADOS_CLASIFICAR
- `patio_curve` ← PATIO `patios_curves`
- `altura_max_pot`, `tratamiento`, `rango_edificabilidad` ← CONTEXTO_POT
- `floor_height_user` ← Slider (ej. 3.0)

---

## Archivos del Pipeline

| Archivo | Versión | Propósito |
|---------|---------|-----------|
| F1_CONTEXTO_POT_v05.py | v05.1 | Leer JSON → geometría Rhino (15 salidas) |
| F1_LADOS_CLASIFICAR_v02.py | **v02** | Clasificar 4 lados virtuales (regla 15m) |
| F1_PATIO_DISCONTINUIDAD_v03.py | **v03** | Patios en esquinas Lateral-Lateral |
| F1_NORMATIVA_APLICAR_v25.py | v25 | Aplicar retiros + IO/IC + envolvente |
