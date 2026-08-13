#! /usr/bin/env python3
"""
================================================================================
F1_NORMATIVA_APLICAR_v24.py — Motor normativo hibrido con feedback loop
Proyecto: DisenoParametrico / Fase 1 — Contexto y Normativa
GH Python Script para Grasshopper (IronPython 2.7 compatible)
================================================================================

PROPOSITO:
  Aplica normativa POT/NSR-10 al poligono del lote usando clasificacion
  espacial hibrida (datos oficiales + retroalimentacion manual desde ArchiCAD).

  REGLA DE CLASIFICACION (ADR-008):
  - Un borde es "Frontal" si la distancia minima desde CUALQUIER punto del
    segmento hasta ALGUNA curva de via es < 15 metros.
  - Si no hay via cerca, es "Lateral" o "Posterior".
  - Las curvas de via provienen de DOS fuentes combinadas via Merge en GH:
    a) vias_oficiales: del JSON (capa Eje_vial del POT)
    b) vias_manuales: dibujadas en ArchiCAD en capas de contexto urbano
       (00-20-20_Elementos_entorno_urbano_preexistente, 70-30-20_Andenes)

  La clasificacion NO depende de adyacencia con vecinos ni de heuristicas
  angulares. Es una regla fisica simple, determinista y auditable.

ENTRADAS:
  lot_polygon (Curve)            — Perimetro del lote
  vias_oficiales (Curve[])       — Curvas del JSON / Eje_vial POT
  vias_manuales (Curve[])        — Curvas dibujadas en ArchiCAD (capas 00-20-20, 70-30-20)
  patio_curve (Curve/Curve[])    — Patio(s) de aislamiento
  json_path (String)             — Ruta al cache JSON (datos POT: altura, tratamiento)
  floor_height_user (Number)     — Altura entrepiso [2.50-3.80]m

SALIDAS:
  envelope_curve, ocupacion_real, io_maximo, ic_real, ic_maximo,
  altura_total, pisos_aplicados, sides_table_json, mensaje

NORMATIVA:
  Decreto 555/2021 — POT Bogota
  NSR-10 Titulo A — Sismo Resistencia
  ADR-008 — Clasificacion Espacial Hibrida

VERSIONES:
  v24.0 — Regla hibrida de 15m. Entrada vias_manuales. Sin adyacencia vecinos.
          Reemplaza v22 (clasificacion por sides_table_json con adyacencia).
================================================================================
"""

import Rhino.Geometry as rg
import json
import os
import math

# ==============================================================================
# CONSTANTES
# ==============================================================================

ALTURA_MIN_ENTREPISO = 2.5
ALTURA_MAX_ENTREPISO = 3.8
TOLERANCIA = 0.01
DISTANCIA_FRENTE_M = 15.0  # ADR-008: umbral para clasificar borde como Frontal

RANGO_PISOS = {"1": 2, "2": 3, "3": 5, "4": 8, "5": 12}

# ==============================================================================
# HELPERS
# ==============================================================================

def unwrap(val):
    if val is None: return None
    if isinstance(val, list): return val[0] if len(val) > 0 else None
    return val

def to_float_safe(val, default=0.0, min_val=None):
    if val is None: return default
    try:
        v = float(val)
        if min_val is not None and v < min_val: return default
        return v
    except: return default

def to_int_safe(val, default=1):
    if val is None: return default
    try:
        v = int(float(val))
        if v <= 0: return default
        return v
    except: return default


def extract_segments(curve):
    """Extrae segmentos de linea de una PolylineCurve."""
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
    """
    Distancia minima desde un segmento a un conjunto de curvas.
    Muestrea 5 puntos del segmento y toma la distancia minima.
    """
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
            if crv is None:
                continue
            try:
                success, t = crv.ClosestPoint(pt)
                if success:
                    cp = crv.PointAt(t)
                    d = pt.DistanceTo(cp)
                    if d < min_dist:
                        min_dist = d
            except:
                continue

    return min_dist


def classify_sides_hybrid(segments, all_vias, distancia_frente=DISTANCIA_FRENTE_M):
    """
    Clasifica cada lado del lote usando la regla hibrida de 15m (ADR-008).

    Args:
        segments: lista de rg.Line (bordes del lote)
        all_vias: lista de rg.Curve (vias oficiales + manuales combinadas)
        distancia_frente: umbral en metros (default 15m)

    Returns:
        list[dict] con side_index, classification, setback_m, dist_to_via_m
    """
    n = len(segments)

    # Calcular distancia minima de cada borde a las vias
    distancias = []
    for i, seg in enumerate(segments):
        d = distance_segment_to_curves(seg, all_vias)
        distancias.append((i, d))

    # Si no hay vias, todo es Lateral
    if len(all_vias) == 0:
        sides = []
        for i in range(n):
            sides.append({
                "side_index": i,
                "classification": "Lateral",
                "setback_m": 0.0,
                "dist_to_via_m": 0.0,
                "road_type": "Sin datos de via"
            })
        return sides

    min_dist = min(d for _, d in distancias)

    # Si la via mas cercana esta a mas de 15m, todo es Lateral
    if min_dist >= distancia_frente:
        sides = []
        for i in range(n):
            sides.append({
                "side_index": i,
                "classification": "Lateral",
                "setback_m": 0.0,
                "dist_to_via_m": round(distancias[i][1], 2),
                "road_type": "Sin via cercana (<15m)"
            })
        return sides

    # Identificar cuales lados estan a < 15m de alguna via
    front_indices = []
    for i, d in distancias:
        if d < distancia_frente:
            front_indices.append(i)

    # Si ningun lado califica, usar el mas cercano como frente
    if len(front_indices) == 0:
        idx_min = min(distancias, key=lambda x: x[1])[0]
        front_indices = [idx_min]

    # El lado opuesto al frente principal es el Posterior
    frente_principal = min(front_indices, key=lambda fi: distancias[fi][1])
    posterior = (frente_principal + n // 2) % n

    # Clasificar cada lado
    sides = []
    for i in range(n):
        d = distancias[i][1]
        if i in front_indices:
            cls = "Frontal"
            sb = 5.0 if d < 5.0 else 3.0
            road = "Calle (hibrida)"
        elif i == posterior:
            cls = "Posterior"
            sb = 3.0
            road = "Vecino (posterior)"
        else:
            cls = "Lateral"
            sb = 0.0
            road = "Vecino (lateral)"

        sides.append({
            "side_index": i,
            "classification": cls,
            "setback_m": sb,
            "dist_to_via_m": round(d, 2),
            "road_type": road
        })

    return sides


def inward_normal(seg, centroid):
    """Normal unitaria hacia el centroide del lote."""
    mid = rg.Point3d((seg.From.X + seg.To.X) / 2.0,
                     (seg.From.Y + seg.To.Y) / 2.0, 0)
    to_ctr = rg.Vector3d(centroid.X - mid.X, centroid.Y - mid.Y, 0)
    sd = rg.Vector3d(seg.To.X - seg.From.X, seg.To.Y - seg.From.Y, 0)
    sd.Unitize()
    n1 = rg.Vector3d(-sd.Y, sd.X, 0)
    n2 = rg.Vector3d(sd.Y, -sd.X, 0)
    normal = n1 if (n1.X * to_ctr.X + n1.Y * to_ctr.Y) > (n2.X * to_ctr.X + n2.Y * to_ctr.Y) else n2
    normal.Unitize()
    return normal


def offset_segment(seg, distance, centroid):
    """Desplaza segmento hacia adentro."""
    if abs(distance) < 0.001:
        return rg.Line(seg.From, seg.To)
    n = inward_normal(seg, centroid)
    return rg.Line(
        rg.Point3d(seg.From.X + n.X * distance, seg.From.Y + n.Y * distance, 0),
        rg.Point3d(seg.To.X + n.X * distance, seg.To.Y + n.Y * distance, 0))


def build_footprint(segments, centroid, setback_map):
    """
    Construye huella edificable aplicando retiros diferenciados.
    Estrategia: offset uniforme con el maximo retiro + strips para laterales.
    """
    n = len(segments)
    setbacks = [setback_map.get(i, 0.0) for i in range(n)]
    max_sb = max(setbacks)

    if max_sb < 0.01:
        pts = [seg.From for seg in segments]
        pts.append(pts[0])
        return rg.PolylineCurve(pts), "Sin retiros"

    pts = [seg.From for seg in segments]
    pts.append(pts[0])
    lot_polygon = rg.PolylineCurve(pts)

    offset_curves = None
    for factor in [1.0, 0.7, 0.5]:
        dist = max_sb * factor
        try:
            curves = lot_polygon.Offset(
                rg.Plane.WorldXY, -dist, TOLERANCIA, rg.CurveOffsetCornerStyle.Sharp)
            if curves and len(curves) > 0:
                try:
                    orig_area = rg.AreaMassProperties.Compute(lot_polygon).Area
                    off_area = rg.AreaMassProperties.Compute(curves[0]).Area
                    if off_area < orig_area * 0.99:
                        offset_curves = curves
                        break
                except:
                    offset_curves = curves
                    break
        except:
            continue

    if not offset_curves:
        return lot_polygon, "Offset fallo"

    offset_curve = offset_curves[0]
    off_segs = extract_segments(offset_curve)

    if len(off_segs) != n:
        return offset_curve, "Offset cambio lados ({}->{})".format(n, len(off_segs))

    strips = []
    for i in range(n):
        if setbacks[i] < max_sb - 0.01:
            orig_seg = segments[i]
            off_seg = off_segs[i]
            strip_pts = [
                orig_seg.From, orig_seg.To,
                off_seg.To, off_seg.From,
                orig_seg.From
            ]
            strips.append(rg.PolylineCurve(strip_pts))

    if len(strips) == 0:
        return offset_curve, "Offset uniforme"

    try:
        all_curves = [offset_curve] + strips
        breps = [rg.Brep.CreatePlanarBreps([c], TOLERANCIA)[0]
                 for c in all_curves
                 if rg.Brep.CreatePlanarBreps([c], TOLERANCIA)]

        if len(breps) >= 2:
            merged = rg.Brep.CreateBooleanUnion(breps, TOLERANCIA)
            if merged and len(merged) > 0:
                edges = [e for e in merged[0].Edges if e]
                j = rg.Curve.JoinCurves(edges)
                if j and len(j) > 0:
                    return j[0], "Offset + {} strips -> Union".format(len(strips))
        return offset_curve, "Union fallo, usando offset"
    except:
        return offset_curve, "Union error, usando offset"


def subtract_patios(footprint, patio_curves):
    """Resta patios de la huella via BooleanDifference."""
    if footprint is None:
        return None
    if patio_curves is None:
        return footprint

    if not isinstance(patio_curves, list):
        patios = [patio_curves]
    else:
        patios = [p for p in patio_curves if p is not None]

    if len(patios) == 0:
        return footprint

    result = footprint
    for patio in patios:
        try:
            fb = rg.Brep.CreatePlanarBreps([result], TOLERANCIA)
            pb = rg.Brep.CreatePlanarBreps([patio], TOLERANCIA)
            if fb and pb and len(fb) > 0 and len(pb) > 0:
                r = rg.Brep.CreateBooleanDifference([fb[0]], [pb[0]], TOLERANCIA)
                if r and len(r) > 0:
                    edges = [e for e in r[0].Edges if e]
                    j = rg.Curve.JoinCurves(edges)
                    if j and len(j) > 0:
                        result = j[0]
        except:
            continue

    return result


# ==============================================================================
# MAIN
# ==============================================================================

lot_polygon_raw  = globals().get("lot_polygon", None)
vias_oficiales_raw = globals().get("vias_oficiales", [])
vias_manuales_raw  = globals().get("vias_manuales", [])
patio_curve_raw  = globals().get("patio_curve", None)
json_path_raw    = globals().get("json_path", None)
floor_height_raw = globals().get("floor_height_user", None)

lot_polygon   = unwrap(lot_polygon_raw)
patio_curve   = patio_curve_raw
json_path     = str(json_path_raw).strip("[]'\" ") if json_path_raw else ""
floor_height  = to_float_safe(unwrap(floor_height_raw),
                               ALTURA_MIN_ENTREPISO, min_val=ALTURA_MIN_ENTREPISO)
if floor_height > ALTURA_MAX_ENTREPISO:
    floor_height = ALTURA_MAX_ENTREPISO

if vias_oficiales_raw is None: vias_oficiales_raw = []
if vias_manuales_raw is None: vias_manuales_raw = []
if not isinstance(vias_oficiales_raw, list): vias_oficiales_raw = [vias_oficiales_raw]
if not isinstance(vias_manuales_raw, list): vias_manuales_raw = [vias_manuales_raw]

vias_oficiales = [v for v in vias_oficiales_raw if v is not None]
vias_manuales  = [v for v in vias_manuales_raw if v is not None]
all_vias = vias_oficiales + vias_manuales

if lot_polygon is None:
    envelope_curve = None
    mensaje = "ERROR: lot_polygon es None."
    print(mensaje)
else:
    altura_pot = 11.4
    tratamiento = "Consolidacion"
    ic_maximo = 2.0
    io_maximo = 0.70
    rango_edif = "3"

    if json_path and os.path.exists(json_path):
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                jdata = json.load(f)
            pd = jdata.get("pot_data", {})
            altura_pot = to_float_safe(pd.get("altura_maxima_m"), 11.4, min_val=0.5)
            tratamiento = str(pd.get("tratamiento", "Consolidacion"))
            rango_edif = str(pd.get("rango_edificabilidad", "3"))
        except:
            pass

    tlow = tratamiento.lower()
    if "desarrollo" in tlow:     io_maximo, ic_maximo = 0.50, 3.0
    elif "renovacion" in tlow:   io_maximo, ic_maximo = 0.60, 5.0
    elif "conservacion" in tlow: io_maximo, ic_maximo = 0.50, 2.0

    floors_norm = RANGO_PISOS.get(rango_edif, 5)

    try:
        amp = rg.AreaMassProperties.Compute(lot_polygon)
        area_lote = amp.Area if amp else 315.0
        centroid = amp.Centroid
    except:
        area_lote, centroid = 315.0, rg.Point3d(0, 0, 0)

    segments = extract_segments(lot_polygon)
    n_sides = len(segments)

    if n_sides < 3:
        envelope_curve = lot_polygon
        mensaje = "ERROR: < 3 lados."
    else:
        sides_table = classify_sides_hybrid(segments, all_vias)

        setback_map = {}
        front_indices = []
        for side in sides_table:
            idx = side["side_index"]
            setback_map[idx] = side["setback_m"]
            if side["classification"] == "Frontal":
                front_indices.append(idx)

        footprint, offset_diag = build_footprint(segments, centroid, setback_map)
        if footprint is None:
            footprint = lot_polygon
            offset_diag = "build_footprint devolvio None"

        patio_count = 0
        if patio_curve is not None and footprint is not None:
            footprint = subtract_patios(footprint, patio_curve)
            if isinstance(patio_curve, list):
                patio_count = len([p for p in patio_curve if p is not None])
            else:
                patio_count = 1

        try:
            area_env = rg.AreaMassProperties.Compute(footprint).Area
        except:
            area_env = area_lote

        if area_env <= 0: area_env = 1.0
        if area_env > area_lote * 1.5:
            footprint = lot_polygon
            area_env = area_lote

        ocupacion_real = area_env / area_lote if area_lote > 0 else 0

        altura_solicitada = floors_norm * floor_height
        if altura_solicitada > altura_pot and altura_pot > 0:
            pisos_aplicados = max(1, int(altura_pot / floor_height))
            altura_total = pisos_aplicados * floor_height
        else:
            pisos_aplicados = floors_norm
            altura_total = altura_solicitada

        ic_real = (area_env * pisos_aplicados) / area_lote if area_lote > 0 else 0
        envelope_curve = footprint

        n_vias_of = len(vias_oficiales)
        n_vias_man = len(vias_manuales)
        n_fronts = sum(1 for s in sides_table if s["classification"] == "Frontal")
        n_lats = sum(1 for s in sides_table if s["classification"] == "Lateral")
        n_posts = sum(1 for s in sides_table if s["classification"] == "Posterior")

        partes = [
            "=== NORMATIVA v24 (Hibrida ADR-008) ===",
            "Tratamiento: {} | Rango: {} | Pisos max: {}".format(
                tratamiento, rango_edif, floors_norm),
            "Lote: {} lados | Area: {:.1f}m2 | Huella: {:.1f}m2".format(
                n_sides, area_lote, area_env),
            "Vias: {} oficiales + {} manuales = {} total".format(
                n_vias_of, n_vias_man, len(all_vias)),
            "Clasificacion (umbral {}m): {}F {}L {}P".format(
                DISTANCIA_FRENTE_M, n_fronts, n_lats, n_posts),
            "IO: {:.2f}/Max {:.2f} | IC: {:.2f}/Max {:.2f}".format(
                ocupacion_real, io_maximo, ic_real, ic_maximo),
            "Pisos: {} x {:.2f}m = {:.2f}m (max POT: {:.1f}m)".format(
                pisos_aplicados, floor_height, altura_total, altura_pot),
            "Offset: {}".format(offset_diag),
            "Patios restados: {}".format(patio_count),
        ]

        for s in sides_table:
            partes.append("  L{}: {} | dist={:.1f}m | retiro={:.1f}m".format(
                s["side_index"], s["classification"],
                s["dist_to_via_m"], s["setback_m"]))

        if ocupacion_real > io_maximo:
            partes.append("ALERTA: IO excede maximo")
        if ic_real > ic_maximo:
            partes.append("ALERTA: IC excede maximo")

        mensaje = "\n".join(partes)
        print(mensaje)

    sides_table_json = json.dumps(sides_table) if 'sides_table' in dir() else "[]"
