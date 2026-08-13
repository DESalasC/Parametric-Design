# Guía Canvas Limpio — Pipeline Dos Etapas (v26)

---

## Arquitectura

```
┌────────────────────────────────────────────────────────────────────┐
│ ETAPA 1: Datos en bruto → ArchiCAD                                   │
│                                                                    │
│ F1_ETAPA1_CONTEXTO_v01 (GH Python)                                  │
│   json_path → lot_curve, vecinos_curves, vias_oficiales,           │
│               espacios_publicos, topo_mesh, normativa, layers_json │
│       │                                                            │
│       ▼ Tapir (componentes nativos GH)                             │
│   Create Layers (desde layers_json)                                │
│   Send Geometry a layers ArchiCAD                                  │
│       │                                                            │
│       ▼ MANUAL en ArchiCAD                                          │
│   - Clasificar polígonos en layers: vías, andenes, zonas verdes,   │
│     predios vecinos                                                 │
│   - Construir volumetrías vecinas (Morph) en 70-20-30               │
└────────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────────┐
│ ETAPA 2: Geometría clasificada → Ocupación                          │
│                                                                    │
│ Tapir GetElements (por capa ArchiCAD)                              │
│   vias_curves ← 00-20-20                                           │
│   ep_curves ← 70-50-10                                             │
│   vecinos_curves ← capa predios vecinos                            │
│   construcciones_curves ← 70-20-30 (Morph)                         │
│       │                                                            │
│       ▼                                                            │
│ Discontinuity (lot_curve → 4 vértices)                             │
│       │                                                            │
│       ▼                                                            │
│ F1_ETAPA2_LADOS_v01 → sides_table_json, es_esquina                 │
│       │                                                            │
│       ├──→ F1_ETAPA2_PATIO_v01 → patios_curves                     │
│       │                                                            │
│       ▼                                                            │
│ F1_ETAPA2_NORMATIVA_v01 → envelope_curve, IO, IC, altura           │
└────────────────────────────────────────────────────────────────────┘
```

---

## Canvas Etapa 1

### Bloque A1: CONTEXTO (GH Python)
- Script: `F1_ETAPA1_CONTEXTO_v01.py`
- Input: `json_path` (Panel con ruta al JSON)
- Outputs: `lot_curve`, `vecinos_curves`, `vias_oficiales`, `espacios_publicos`, `topo_mesh`, `layers_json`, normativa, `origen_x/y`, `mensaje`

### Bloque A2: Layers en ArchiCAD (Tapir nativo)
- Componente Tapir **Create Layer** → conectar cada capa de `layers_json` (o crear manualmente):
  - `00-00-10_Lote_proyecto`
  - `00-20-20_Elementos_entorno_urbano`
  - `70-50-10_Zonas_verdes_publicas`
  - `70-30-20_Andenes_preexistentes`
  - `10-20-10_Topografia`
  - `70-20-30_Volumetrias_vecinas`
  - `00-10-20_Elementos_referencia`

### Bloque A3: Envío de geometría (Tapir nativo)
- **Send Polygon** → `vecinos_curves` → capa predios vecinos
- **Send Polygon** → `vias_oficiales` → capa `00-20-20_Elementos_entorno_urbano`
- **Send Polygon** → `espacios_publicos` → capa `70-50-10_Zonas_verdes_publicas`
- **Send Mesh/Morph** → `topo_mesh` → capa `10-20-10_Topografia`
- **Send Polygon** → `lot_curve` → capa `00-00-10_Lote_proyecto`

### Trabajo manual en ArchiCAD (entre etapas)
1. Verificar los polígonos enviados y moverlos a las capas correctas
2. Corregir clasificaciones erróneas (ej: el predio al occidente que es zona verde)
3. Construir volumetrías existentes de vecinos como **Morph** en `70-20-30_Volumetrias_vecinas`
4. Dibujar andenes en `70-30-20_Andenes_preexistentes` si aplica

---

## Canvas Etapa 2

### Bloque B1: Lectura desde ArchiCAD (Tapir nativo)
- **Get Elements by Type** con filtro por capa:
  - `vias_curves` ← capa `00-20-20` (elementos Polygon)
  - `ep_curves` ← capa `70-50-10`
  - `vecinos_curves` ← capa predios vecinos
  - `construcciones_curves` ← capa `70-20-30` (Morph)
- **Get Details** para convertir a curvas Rhino

### Bloque B2: Vértices (Discontinuity nativo)
- `lot_curve` → **Discontinuity** → salida `D` (4 vértices principales)
- Conectar `D` → `lot_vertices` de LADOS y PATIO (type hint: Point3d, List Access)

### Bloque B3: LADOS (GH Python)
- Script: `F1_ETAPA2_LADOS_v01.py`
- Inputs: `lot_vertices`, `vias_curves`, `ep_curves`, `vecinos_curves`
- Outputs: `sides_table_json`, `lot_simplificado`, `es_esquina`, `mensaje`

### Bloque B4: PATIO (GH Python)
- Script: `F1_ETAPA2_PATIO_v01.py`
- Inputs: `lot_vertices`, `sides_table_json`, `altura_max_pot`
- Outputs: `patios_curves`, `patio_count`, `mensaje`

### Bloque B5: NORMATIVA (GH Python)
- Script: `F1_ETAPA2_NORMATIVA_v01.py`
- Inputs: `lot_polygon` (de LADOS), `sides_table_json`, `patio_curves`, `altura_max_pot`, `tratamiento`, `rango_edificabilidad`, `floor_height_user` (slider), `io_maximo_user` (opcional)
- Outputs: `envelope_curve`, `ocupacion_real`, `io_maximo`, `ic_real`, `ic_maximo`, `altura_total`, `pisos_aplicados`, `mensaje`

---

## Archivos

| Script | Rol |
|--------|-----|
| `F1_ETAPA1_CONTEXTO_v01.py` | JSON → geometría + capas destino |
| `F1_ETAPA2_LADOS_v02.py` | Clasificación por colindancia real |
| `F1_ETAPA2_PATIO_v01.py` | Patios en esquinas Lateral-Lateral |
| `F1_ETAPA2_NORMATIVA_v02a.py` | Retiros + ocupación + IO/IC + envolvente |
