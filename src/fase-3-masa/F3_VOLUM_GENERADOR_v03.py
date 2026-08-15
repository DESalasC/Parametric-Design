#! /usr/bin/env python3
"""
F3_VOLUM_GENERADOR_v03 - Generacion Envolvente Edificio para ArchiCAD
Blindado contra nulls usando Listas de .NET
"""

import Rhino.Geometry as rg
import math
import json
import System
from System.Collections.Generic import List

# ============================================================
# FUNCIONES AUXILIARES
# ============================================================
def unwrap(val):
    if isinstance(val, list):
        return val[0] if len(val) > 0 else None
    return val

def to_int(val, default=0):
    try: return int(float(val))
    except (ValueError, TypeError): return default

def to_float(val, default=0.0):
    try: return float(val)
    except (ValueError, TypeError): return default

def parse_json_input(data):
    if not data: return {}
    if isinstance(data, str):
        try: return json.loads(data)
        except: return {}
    return data if isinstance(data, dict) else {}

def flatten(lst):
    result = []
    for i in lst:
        if isinstance(i, (list, tuple, System.Array)):
            result.extend(flatten(i))
        else:
            result.append(i)
    return result

def offset_polygon_inward(polygon, distances):
    if not polygon: return None
    vals = list(distances.values())
    avg_d = sum(vals) / len(vals) if vals else 3.0
    
    amp = rg.AreaMassProperties.Compute(polygon)
    if not amp: return polygon
    pt_inside = amp.Centroid
    plane = rg.Plane(pt_inside, rg.Vector3d.ZAxis)
    
    offset_crvs = rg.Curve.Offset(polygon, plane, -avg_d, 0.001, rg.CurveOffsetCornerStyle.Sharp)
    if offset_crvs and len(offset_crvs) > 0:
        joined = rg.Curve.JoinCurves(offset_crvs)
        if joined and len(joined) > 0:
            return joined[0]
        return offset_crvs[0]
    return polygon

def to_polyline(curve):
    if not curve: return None
    rc, pline = curve.TryGetPolyline()
    if rc and pline:
        return rg.PolylineCurve(pline)
    return curve

# ============================================================
# MAIN EXECUTION
# ============================================================
lot_polygon = unwrap(globals().get("lot_polygon", None))
sides_table = unwrap(globals().get("sides_table", None))
pot_conclusions = unwrap(globals().get("pot_conclusions", None))

slab_thickness = to_float(unwrap(globals().get("slab_thickness", 0.25)), 0.25)
has_parking_ground = unwrap(globals().get("has_parking_ground", False))
has_communal_ground = unwrap(globals().get("has_communal_ground", False))
has_basement = unwrap(globals().get("has_basement", False))

if lot_polygon is None: raise ValueError("Falta lot_polygon")
if sides_table is None: raise ValueError("Falta sides_table (CONFIGURAR_LADOS_v03)")
if pot_conclusions is None: raise ValueError("Falta pot_conclusions (CONTEXTO_v04)")

pot_dict = parse_json_input(pot_conclusions)

if isinstance(sides_table, str):
    try: sides_list = json.loads(sides_table)
    except: sides_list = []
else:
    sides_list = sides_table if isinstance(sides_table, list) else []

# --- AJUSTE TIPOLOGÍA CONTINUA ---
for s in sides_list:
    if isinstance(s, dict):
        if s.get("classification") in ["Lateral", "Posterior"]:
            s["setback_m"] = 0.0
            s["balcony_allowed"] = False

height_limits = pot_dict.get("height_limits", {})
max_height_pot = to_float(height_limits.get("altura_efectiva_m", 12.0), 12.0)

# 1. CALCULAR PISOS PERMITIDOS POR EL POT
temp_fh = 3.0
floors = max(1, int(max_height_pot / temp_fh)) if max_height_pot > 0 else 4

# 2. CALCULAR ALTURA DE PISO DEFINITIVA (fh)
fh = max_height_pot / floors if floors > 0 else 3.0 

# 3. CALCULAR ALTURA DE MURO
wall_height = fh - slab_thickness

print(f"=== VOLUMEN_v03 (Máximo POT) ===")
print(f"Altura POT: {max_height_pot}m | Pisos a construir: {floors}")

slabs_out = []
walls_out = []

start_level = -1 if has_basement else 0

base_setbacks = {}
if sides_list:
    for s in sides_list:
        if not isinstance(s, dict): continue
        idx = s.get("side_index", 0)
        base_setbacks[idx] = s.get("setback_m", 3.0)
else:
    base_setbacks = {0: 3.0, 1: 0.0, 2: 0.0, 3: 0.0, 4: 3.0, 5: 3.0}

footprint_raw = offset_polygon_inward(lot_polygon, base_setbacks)
if footprint_raw:
    footprint = to_polyline(footprint_raw)
    
    for fl in range(start_level, floors):
        floor_z = fl * fh
        xform_z = rg.Transform.Translation(0, 0, floor_z)
        
        slab_geo = footprint.Duplicate()
        slab_geo.Transform(xform_z)
        slabs_out.append(slab_geo)
        
        segments = footprint.DuplicateSegments()
        for seg in segments:
            wall_geo = seg.Duplicate()
            wall_geo.Transform(xform_z)
            walls_out.append(wall_geo)

# ============================================================
# APLANAR Y ASIGNAR SALIDAS GEOMÉTRICAS
# ============================================================
slab_polygons = flatten(slabs_out)
wall_curves = flatten(walls_out)
balcony_polygons = []

out_floor_height = fh
out_slab_thickness = slab_thickness
out_wall_height = wall_height

# ============================================================
# GENERACIÓN DE NIVELES E ÍNDICES (Listas de Python puras)
# ============================================================
story_names = []
story_elevations = []
floor_indices = []

if has_basement:
    story_names.append("Nivel Sotano")
    story_elevations.append(round(-fh, 2))
    floor_indices.append(0)

for i in range(1, floors + 1):
    nivel_str = f"Nivel {i:02d}" if i < 10 else f"Nivel {i}"
    story_names.append(nivel_str)
    elev = 0.0 if i == 1 else round((i - 1) * fh, 2)
    story_elevations.append(elev)
    
    # Generar un índice (0, 1, 2, 3...) por cada losa construida
    if not has_basement:
        floor_indices.append(i - 1)
    else:
        floor_indices.append(i)

story_names.append("Nivel Cubierta")
story_elevations.append(round(max_height_pot, 2))

# ASIGNACIÓN DE SALIDAS
# story_names y story_elevations van a Tapir SetStories
# floor_indices va al AC Slab Settings (si lo usas)
print(f"Niveles: {story_names}")
print(f"Alturas: {story_elevations}")
print(f"Índices de losas: {floor_indices}")