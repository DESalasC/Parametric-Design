#! /usr/bin/env python3
"""
================================================================================
F1_LADOS_CLASIFICAR_v01.py — Clasificador de lados por regla hibrida 15m
Proyecto: DisenoParametrico / Fase 1
GH Python Script para Grasshopper (IronPython 2.7 compatible)
================================================================================

PROPOSITO:
  UNICA responsabilidad: clasificar cada borde del lote como Frontal/Lateral/Posterior
  usando la regla hibrida de 15m (ADR-008).

  La clasificacion NO depende de normativa, altura, ni patios.
  Solo responde a la pregunta: "hay una via a menos de 15m de este borde?"

ENTRADAS:
  lot_polygon (Curve)       — Perimetro del lote
  vias (Curve[])            — Curvas de via CONSOLIDADAS (oficiales + manuales, pre-merge en GH)

SALIDAS:
  sides_table_json (String) — JSON con clasificacion y distancias
  mensaje (String)          — Diagnostico

NORMATIVA:
  ADR-008 — Clasificacion Espacial Hibrida
  Regla: distancia minima borde→via < 15m → Frontal
================================================================================
"""

import Rhino.Geometry as rg
import json
import math

DISTANCIA_FRENTE_M = 15.0  # ADR-008


def unwrap(val):
    if val is None: return None
    if isinstance(val, list): return val[0] if len(val) > 0 else None
    return val


def extract_segments(curve):
    if curve is None: return []
    success, poly = curve.TryGetPolyline()
    if not success or poly is None: return []
    c = poly.Count
    is_closed = (c >= 2 and poly[0].DistanceTo(poly[c-1]) < 0.001)
    n = c - 1 if is_closed else c
    segs = []
    for i in range(n):
        segs.append(rg.Line(poly[i], poly[(i+1) % c]))
    return segs


def distance_segment_to_curves(seg, curves):
    """Distancia minima de un segmento a un conjunto de curvas (muestreo 5 pts)."""
    if curves is None or len(curves) == 0:
        return float('inf')

    sample_pts = []
    for t in [0.0, 0.25, 0.5, 0.75, 1.0]:
        x = seg.From.X + t * (seg.To.X - seg.From.X)
        y = seg.From.Y + t * (seg.To.Y - seg.From.Y)
        sample_pts.append(rg.Point3d(x, y, 0))

    min_dist = float('inf')
    for pt in sample_pts:
        for crv in curves:
            if crv is None: continue
            try:
                success, t = crv.ClosestPoint(pt)
                if success:
                    d = pt.DistanceTo(crv.PointAt(t))
                    if d < min_dist: min_dist = d
            except:
                continue
    return min_dist


# ==============================================================================
# MAIN
# ==============================================================================

lot_polygon_raw = globals().get("lot_polygon", None)
vias_raw = globals().get("vias", [])

lot_polygon = unwrap(lot_polygon_raw)

if vias_raw is None: vias_raw = []
if not isinstance(vias_raw, list): vias_raw = [vias_raw]
vias = [v for v in vias_raw if v is not None]

if lot_polygon is None:
    sides_table_json = json.dumps([])
    mensaje = "ERROR: lot_polygon es None"
else:
    segments = extract_segments(lot_polygon)
    n = len(segments)

    if n < 3:
        sides_table_json = json.dumps([])
        mensaje = "ERROR: < 3 lados"
    else:
        # Calcular distancia de cada borde a las vias
        distancias = []
        for i, seg in enumerate(segments):
            d = distance_segment_to_curves(seg, vias)
            distancias.append((i, d))

        # Determinar cuales son frontales (< 15m)
        front_indices = []
        for i, d in distancias:
            if d < DISTANCIA_FRENTE_M:
                front_indices.append(i)

        # Si ninguna via cerca, usar el borde mas cercano como frente
        if len(front_indices) == 0 and len(vias) > 0:
            idx_min = min(distancias, key=lambda x: x[1])[0]
            front_indices = [idx_min]

        # El lado opuesto al frente mas cercano es Posterior
        if len(front_indices) > 0:
            frente_principal = min(front_indices, key=lambda fi: distancias[fi][1])
            posterior = (frente_principal + n // 2) % n
        else:
            posterior = -1

        # Construir tabla
        sides_table = []
        for i in range(n):
            d = distancias[i][1]
            if i in front_indices:
                cls = "Frontal"
            elif i == posterior:
                cls = "Posterior"
            else:
                cls = "Lateral"

            sides_table.append({
                "side_index": i,
                "classification": cls,
                "dist_to_via_m": round(d, 2)
            })

        sides_table_json = json.dumps(sides_table)

        nf = sum(1 for s in sides_table if s["classification"] == "Frontal")
        nl = sum(1 for s in sides_table if s["classification"] == "Lateral")
        np_ = sum(1 for s in sides_table if s["classification"] == "Posterior")
        nv = len(vias)

        mensaje = "LADOS v01 (ADR-008, {}m): {} lados | {} vias | {}F {}L {}P".format(
            DISTANCIA_FRENTE_M, n, nv, nf, nl, np_)
        for s in sides_table:
            mensaje += "\n  L{}: {} | dist={:.1f}m".format(
                s["side_index"], s["classification"], s["dist_to_via_m"])

        print(mensaje)
