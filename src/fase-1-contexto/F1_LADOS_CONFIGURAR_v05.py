#! /usr/bin/env python3
"""
================================================================================
F1_LADOS_CONFIGURAR_v05.py — Clasificacion de lados del lote + diagnostico.
Proyecto: DisenoParametrico / Fase 1 — Contexto y Normativa
GH Python Script para Grasshopper (IronPython 2.7 compatible)
================================================================================

PROPOSITO:
  Clasifica lados como "Frontal" (calle) o "Lateral" (vecino) midiendo
  distancia a street_curves. Incluye diagnostico de coordenadas para
  detectar mismatches entre lote y calles.

ENTRADAS:
  lot_polygon   (Curve, Item Access)  — Perimetro del lote
  lot_segments  (Line[], List Access)  — Segmentos del Explode
  lot_midpoints (Point[], List Access) — Puntos medios de cada segmento
  street_curves (Curve[], List Access) — Curvas de vias (desde CONTEXTO_POT)

SALIDAS:
  sides_table_json (String) — JSON array de clasificacion

VERSIONES:
  v04 — Sin centroid externo. Clasificacion por distancia. Advertencia >50m.
  v05 — Diagnostico de coordenadas de lote vs calles. Muestra bounding box
        de street_curves y lot_polygon para detectar mismatches.
================================================================================
"""

import Rhino.Geometry as rg
import json
import math


def to_int_safe(val, default=0):
    if val is None: return default
    try: return int(float(val))
    except: return default


def to_float_safe(val, default=0.0):
    if val is None: return default
    try: return float(val)
    except: return default


def get_bbox_info(curve, label):
    """Obtiene bounding box de una curva para diagnostico."""
    if curve is None:
        return None
    try:
        bbox = curve.GetBoundingBox(rg.Plane.WorldXY)
        return {
            "label": label,
            "min_x": round(bbox.Min.X, 1),
            "min_y": round(bbox.Min.Y, 1),
            "max_x": round(bbox.Max.X, 1),
            "max_y": round(bbox.Max.Y, 1),
        }
    except:
        return None


# ==============================================================================
# MAIN
# ==============================================================================

lot_polygon   = globals().get("lot_polygon", None)
lot_segments  = globals().get("lot_segments", [])
lot_midpoints = globals().get("lot_midpoints", [])
street_curves = globals().get("street_curves", [])

# Normalizar listas
if lot_segments is None: lot_segments = []
if not isinstance(lot_segments, list): lot_segments = [lot_segments]
if lot_midpoints is None: lot_midpoints = []
if not isinstance(lot_midpoints, list): lot_midpoints = [lot_midpoints]
if street_curves is None: street_curves = []
if not isinstance(street_curves, list): street_curves = [street_curves]

lot_segments  = [s for s in lot_segments if s is not None]
lot_midpoints = [p for p in lot_midpoints if p is not None]
street_curves = [c for c in street_curves if c is not None]

# --- DIAGNOSTICO DE COORDENADAS ---
diag_parts = []
diag_parts.append("=== DIAGNOSTICO LADOS v05 ===")

# Bounding box del lote
lot_bbox = get_bbox_info(lot_polygon, "LOTE")
if lot_bbox:
    diag_parts.append("LOTE bbox: X[{:.1f}..{:.1f}] Y[{:.1f}..{:.1f}]".format(
        lot_bbox["min_x"], lot_bbox["max_x"],
        lot_bbox["min_y"], lot_bbox["max_y"]))

# Bounding box de street_curves
if len(street_curves) > 0:
    all_streets_bbox = None
    for i, sc in enumerate(street_curves):
        sb = get_bbox_info(sc, "CALLE_{}".format(i))
        if sb:
            diag_parts.append("CALLE_{} bbox: X[{:.1f}..{:.1f}] Y[{:.1f}..{:.1f}]".format(
                i, sb["min_x"], sb["max_x"], sb["min_y"], sb["max_y"]))
    diag_parts.append("Total street_curves: {} curvas".format(len(street_curves)))
else:
    diag_parts.append("ADVERTENCIA: street_curves vacia (0 curvas).")
    diag_parts.append("Verifique que F1_CONTEXTO_POT esta emitiendo street_curves")
    diag_parts.append("y que estan en el MISMO sistema de coordenadas que el lote.")

diag_parts.append("Segmentos del lote: {} (midpoints: {})".format(
    len(lot_segments), len(lot_midpoints)))

if lot_polygon is None or len(lot_segments) == 0:
    diag_parts.append("ERROR: Falta lot_polygon o lot_segments.")
    sides_table_json = json.dumps([])
    print("\n".join(diag_parts))
else:
    # --- CALCULAR DISTANCIAS ---
    segment_data = []
    
    for i, seg in enumerate(lot_segments):
        if i < len(lot_midpoints):
            mid = lot_midpoints[i]
        else:
            mid = rg.Point3d((seg.From.X + seg.To.X) / 2,
                             (seg.From.Y + seg.To.Y) / 2, 0)
        
        min_dist = float('inf')
        closest_idx = -1
        
        for j, crv in enumerate(street_curves):
            try:
                # Validar que la curva tenga metodo ClosestPoint
                if not hasattr(crv, 'ClosestPoint'):
                    continue
                success, t = crv.ClosestPoint(mid)
                if success:
                    pt_on_crv = crv.PointAt(t)
                    dist = mid.DistanceTo(pt_on_crv)
                    if dist < min_dist:
                        min_dist = dist
                        closest_idx = j
            except:
                continue
        
        segment_data.append({
            "idx": i,
            "dist": min_dist,
            "street_idx": closest_idx
        })
    
    # --- CLASIFICAR ---
    if len(segment_data) == 0:
        sides_table = []
        diag_parts.append("ERROR: 0 segmentos procesados.")
    elif len(street_curves) == 0:
        # Sin calles: todo Lateral
        sides_table = []
        for d in segment_data:
            sides_table.append({
                "side_index": d["idx"],
                "classification": "Lateral",
                "setback_m": 0.0,
                "road_type": "Vecino",
                "dist_to_street_m": 999.0
            })
        diag_parts.append("Sin street_curves: todos los lados -> Lateral (vecino).")
    else:
        min_dist_overall = min(d["dist"] for d in segment_data)
        max_dist_overall = max(d["dist"] for d in segment_data)
        
        diag_parts.append("Distancias a calles: min={:.1f}m, max={:.1f}m".format(
            min_dist_overall, max_dist_overall))
        
        if min_dist_overall > 50.0:
            diag_parts.append("ADVERTENCIA: Distancia minima > 50m.")
            diag_parts.append("Las street_curves NO estan en el mismo sistema")
            diag_parts.append("de coordenadas que el lote. Aplique el vector")
            diag_parts.append("de traslacion del lote a las street_curves.")
            # Todo Lateral (vecino) como fallback seguro
            sides_table = []
            for d in segment_data:
                sides_table.append({
                    "side_index": d["idx"],
                    "classification": "Lateral",
                    "setback_m": 0.0,
                    "road_type": "Vecino",
                    "dist_to_street_m": round(d["dist"], 2)
                })
        else:
            # Clasificacion normal
            front_threshold = min_dist_overall + 8.0  # margen generoso
            
            sides_table = []
            for d in segment_data:
                is_front = d["dist"] <= front_threshold
                
                if is_front:
                    classification = "Frontal"
                    setback = 3.0
                    road_type = "Local"
                else:
                    classification = "Lateral"
                    setback = 0.0
                    road_type = "Vecino"
                
                sides_table.append({
                    "side_index": d["idx"],
                    "classification": classification,
                    "setback_m": setback,
                    "road_type": road_type,
                    "dist_to_street_m": round(d["dist"], 2)
                })
            
            # Mostrar distancias por lado
            for d in segment_data:
                cls = "F" if d["dist"] <= front_threshold else "L"
                diag_parts.append("  Lado {}: {:.1f}m -> {}".format(d["idx"], d["dist"], cls))
    
    # --- SALIDA ---
    sides_table_json = json.dumps(sides_table)
    
    n_fronts = sum(1 for s in sides_table if s["classification"] == "Frontal")
    n_lats = sum(1 for s in sides_table if s["classification"] == "Lateral")
    diag_parts.append("RESULTADO: {} Frontales, {} Laterales de {} lados".format(
        n_fronts, n_lats, len(sides_table)))
    
    print("\n".join(diag_parts))
