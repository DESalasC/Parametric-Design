# Guía de Integración GHX — Pipeline Fase 1 (v25)

---

## Pipeline completo

```
┌─────────────────────────────────────────────────────────────┐
│                   F1_CONTEXTO_POT_v05                       │
│  Entrada: json_path (String)                                │
│                                                             │
│  Salidas:                                                   │
│  ├─ lot_curve             → poligono del lote (0,0 anclado) │
│  ├─ neighbors_curves      → vecinos desplazados             │
│  ├─ vias_oficiales        → 3 capas POT GDB, buffer 500m    │
│  ├─ espacios_publicos     → parques/plazas/z. verdes        │
│  ├─ topo_mesh             → malla terreno triangulada       │
│  ├─ altura_max_pot        → Number                          │
│  ├─ tratamiento           → String                          │
│  ├─ rango_edificabilidad  → String "1".."5"                 │
│  ├─ sector_normativo      → String                          │
│  ├─ upz                   → String                          │
│  ├─ area_lote_m2          → Number                          │
│  ├─ origen_x, origen_y    → referencia SIRGAS               │
│  └─ mensaje               → diagnostico                     │
└───────┬───────────────────────────┬─────────────────────────┘
        │                           │
        ▼                           ▼
┌───────────────────────┐   ┌───────────────────────────────┐
│ F1_LADOS_CLASIFICAR   │   │ F1_PATIO_DISCONTINUIDAD       │
│ _v01                  │   │ _v02                          │
│                       │   │                               │
│ Entradas:             │   │ Entradas:                     │
│  lot_curve            │   │  lot_vertices (Discontinuity) │
│  vias (Merge oficial  │   │  sides_table_json ◄────┐      │
│   + manual Tapir)     │   │  altura_max_pot         │      │
│                       │   │                          │      │
│ Salidas:              │   │ Salidas:                 │      │
│  sides_table_json ────┼───┼──────────────────────────┘      │
│  mensaje              │   │  patios_curves                  │
└───────────────────────┘   │  patio_count                    │
                            │  mensaje                        │
                            └───────────┬───────────────────┘
                                        │
                    ┌───────────────────┘
                    ▼
┌───────────────────────────────────────────────────────────┐
│                F1_NORMATIVA_APLICAR_v25                    │
│                                                           │
│ Entradas:                                                 │
│  lot_polygon              ← lot_curve (CONTEXTO)          │
│  sides_table_json         ← LADOS_CLASIFICAR              │
│  patio_curve              ← patios_curves (PATIO)         │
│  altura_max_pot           ← CONTEXTO                      │
│  tratamiento              ← CONTEXTO                      │
│  rango_edificabilidad     ← CONTEXTO                      │
│  floor_height_user        ← Number (slider)               │
│                                                           │
│ Salidas:                                                  │
│  envelope_curve, ocupacion_real, io_maximo, ic_real,      │
│  ic_maximo, altura_total, pisos_aplicados, mensaje        │
└───────────────────────────────────────────────────────────┘
```

---

## Instrucciones en Grasshopper

### Paso 1: Bloque A — CONTEXTO_POT_v05

1. Agregar **GhPython** al canvas
2. Cargar `F1_CONTEXTO_POT_v05.py`
3. Conectar un **Panel** con la ruta al JSON → entrada `json_path`
   - Ej: `D:\Work\PROJECTS\DiseñoParametrico\data\pot-cache\AAA0127AZPA-contexto.json`
4. **Salidas a cablear:**
   - `lot_curve` → Tapir (o al Merge del paso 2)
   - `vias_oficiales`, `neighbors_curves`, `espacios_publicos` → Preview (opcional)
   - `topo_mesh` → Preview (malla de terreno 3D)

### Paso 2: Merge de vías (GH nativo, sin Python)

1. **Merge** component → entradas:
   - `D0`: `vias_oficiales` (desde CONTEXTO_POT_v05)
   - `D1`: curvas de vías manuales desde Tapir (capas ArchiCAD: ej. `70-30-20_Andenes`)
2. Salida `R` del Merge contiene todas las vías combinadas

### Paso 3: Bloque B — LADOS_CLASIFICAR_v01

1. Agregar **GhPython**
2. Cargar `F1_LADOS_CLASIFICAR_v01.py`
3. Conectar:
   - `lot_polygon` ← `lot_curve` (desde CONTEXTO_POT_v05)
   - `vias` ← salida `R` del Merge (vías oficiales + manuales)
4. Salidas:
   - `sides_table_json` → Panel (verificar clasificación)
   - Conectar a entrada `sides_table_json` de PATIO y NORMATIVA

### Paso 4: Bloque C — PATIO_DISCONTINUIDAD_v02

1. Agregar componente **Discontinuity** nativo de GH
   - Conectar `lot_curve` como geometría de entrada
   - Salida `D` (discontinuity points) → `lot_vertices` del script

2. Agregar **GhPython**
3. Cargar `F1_PATIO_DISCONTINUIDAD_v02.py`
4. Conectar:
   - `lot_vertices` ← Discontinuity `D`
   - `sides_table_json` ← LADOS_CLASIFICAR `sides_table_json`
   - `altura_max_pot` ← CONTEXTO_POT `altura_max_pot`
5. Salidas:
   - `patios_curves` → Preview + entrada de NORMATIVA

### Paso 5: Bloque D — NORMATIVA_APLICAR_v25

1. Agregar **GhPython**
2. Cargar `F1_NORMATIVA_APLICAR_v25.py`
3. Conectar todas las entradas desde los bloques anteriores más un slider para `floor_height_user`
4. Salida `envelope_curve` → Tapir → ArchiCAD

---

## Notas

- Las vías manuales se dibujan en ArchiCAD y se traen a GH vía Tapir (capa `00-20-20_Elementos_entorno_urbano`)
- Si no hay vías manuales todavía, el Merge solo recibe `vias_oficiales` — la clasificación usará solo datos del POT
- `espacios_publicos` es informativo por ahora — no interviene en la clasificación
- El `topo_mesh` usa IDW para interpolar Z — se puede mejorar después con Delaunay nativo de GH
