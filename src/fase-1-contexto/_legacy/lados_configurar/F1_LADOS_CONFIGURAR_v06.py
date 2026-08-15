#! /usr/bin/env python3
"""
================================================================================
F1_LADOS_CONFIGURAR_v06.py — Clasificacion con diagnostico de coordenadas.
GH Python Script para Grasshopper (IronPython 2.7 compatible)

PROPOSITO:
  Imprime coordenadas del lote y las street_curves para verificar que
  esten en el mismo sistema. Clasifica lados por distancia a calles.

ENTRADAS: lot_polygon, lot_segments, lot_midpoints, street_curves
SALIDA: sides_table_json (String)
================================================================================
"""

import Rhino.Geometry as rg
import json


def to_int_safe(val, default=0):
    if val is None: return default
    try: return int(float(val))
    except: return default


# ==============================================================================
# MAIN
# ==============================================================================

lot_polygon   = globals().get("lot_polygon", None)
lot_segments  = globals().get("lot_segments", [])
lot_midpoints = globals().get("lot_midpoints", [])
street_curves = globals().get("street_curves", [])

if lot_segments is None: lot_segments = []
if not isinstance(lot_segments, list): lot_segments = [lot_segments]
if lot_midpoints is None: lot_midpoints = []
if not isinstance(lot_midpoints, list): lot_midpoints = [lot_midpoints]
if street_curves is None: street_curves = []
if not isinstance(street_curves, list): street_curves = [street_curves]

lot_segments  = [s for s in lot_segments if s is not None]
lot_midpoints = [p for p in lot_midpoints if p is not None]
street_curves = [c for c in street_curves if c is not None]

# --- DIAGNOSTICO DE COORDENADAS (punto medio del primer segmento del lote) ---
print("=== DIAG LADOS v06 ===")
if len(lot_segments) > 0:
    s0 = lot_segments[0]
    print("Lote seg[0]: From=({:.1f},{:.1f}) To=({:.1f},{:.1f})".format(
        s0.From.X, s0.From.Y, s0.To.X, s0.To.Y))

if len(lot_midpoints) > 0:
    mp0 = lot_midpoints[0]
    print("Lote mid[0]: ({:.1f}, {:.1f})".format(mp0.X, mp0.Y))

print("street_curves count: {}".format(len(street_curves)))
for i, sc in enumerate(street_curves[:3]):  # solo primeros 3
    try:
        bbox = sc.GetBoundingBox(rg.Plane.WorldXY)
        print("  CALLE[{}] bbox: ({:.1f},{:.1f}) -> ({:.1f},{:.1f})".format(
            i, bbox.Min.X, bbox.Min.Y, bbox.Max.X, bbox.Max.Y))
    except:
        print("  CALLE[{}]: sin bbox".format(i))

if lot_polygon is None or len(lot_segments) == 0:
    sides_table_json = json.dumps([])
    print("ERROR: falta geometria")
else:
    segment_data = []
    
    for i, seg in enumerate(lot_segments):
        if i < len(lot_midpoints):
            mid = lot_midpoints[i]
        else:
            mid = rg.Point3d((seg.From.X + seg.To.X) / 2,
                             (seg.From.Y + seg.To.Y) / 2, 0)
        
        min_dist = float('inf')
        for j, crv in enumerate(street_curves):
            try:
                if not hasattr(crv, 'ClosestPoint'):
                    continue
                success, t = crv.ClosestPoint(mid)
                if success:
                    pt = crv.PointAt(t)
                    dist = mid.DistanceTo(pt)
                    if dist < min_dist:
                        min_dist = dist
            except:
                continue
        
        segment_data.append({"idx": i, "dist": min_dist})
    
    if len(street_curves) == 0:
        print("ADVERTENCIA: street_curves VACIA. Todo Lateral.")
        sides_table = []
        for d in segment_data:
            sides_table.append({
                "side_index": d["idx"],
                "classification": "Lateral",
                "setback_m": 0.0,
                "road_type": "Vecino",
                "dist_to_street_m": 0.0
            })
    else:
        min_d = min(d["dist"] for d in segment_data)
        max_d = max(d["dist"] for d in segment_data)
        print("Dist a calles: min={:.1f}m max={:.1f}m".format(min_d, max_d))
        
        if min_d > 50:
            print("ADVERTENCIA: min > 50m. Calles en otro sist. de coord.?")
            print("  Lote mid[0]=({:.1f},{:.1f})  Calle bbox ver arriba.".format(
                lot_midpoints[0].X if lot_midpoints else 0,
                lot_midpoints[0].Y if lot_midpoints else 0))
        
        threshold = min_d + 8.0
        sides_table = []
        for d in segment_data:
            is_front = d["dist"] <= threshold
            cls = "Frontal" if is_front else "Lateral"
            sb = 3.0 if is_front else 0.0
            sides_table.append({
                "side_index": d["idx"],
                "classification": cls,
                "setback_m": sb,
                "road_type": "Calle" if is_front else "Vecino",
                "dist_to_street_m": round(d["dist"], 2)
            })
            print("  Lado {}: {:.1f}m -> {}".format(d["idx"], d["dist"], cls))
    
    sides_table_json = json.dumps(sides_table)
    nf = sum(1 for s in sides_table if s["classification"] == "Frontal")
    nl = sum(1 for s in sides_table if s["classification"] == "Lateral")
    print("RESULTADO: {}F {}L de {} lados".format(nf, nl, len(sides_table)))
