#! /usr/bin/env python3
"""
================================================================================
F1_NORMATIVA_APLICAR_v25.py — Aplicador de normativa (retiros + patios + indices)
Proyecto: DisenoParametrico / Fase 1
GH Python Script para Grasshopper (IronPython 2.7 compatible)
================================================================================

PROPOSITO:
  UNICA responsabilidad: recibir la clasificacion de lados YA CALCULADA y
  aplicarle la normativa correspondiente (retiros, patios, IO, IC, altura).

  NO clasifica lados. NO extrae datos del JSON. NO calcula patios.
  Solo APLICA reglas a datos ya determinados.

ENTRADAS:
  lot_polygon (Curve)            — Perimetro del lote
  sides_table_json (String)      — Clasificacion de lados (de F1_LADOS_CLASIFICAR)
  patio_curve (Curve/Curve[])    — Patio(s) YA calculados (de F1_PATIO_DISCONTINUIDAD)
  altura_max_pot (Number)        — Altura maxima segun normativa [m]
  tratamiento (String)           — Tipo de tratamiento (para IO/IC defaults)
  rango_edificabilidad (String)  — Rango "1".."5" → pisos maximos
  floor_height_user (Number)     — Altura entrepiso [2.50-3.80]m

SALIDAS:
  envelope_curve, ocupacion_real, io_maximo, ic_real, ic_maximo,
  altura_total, pisos_aplicados, mensaje

NORMATIVA:
  Decreto 555/2021 — POT Bogota
  NSR-10 Titulo A
  ADR-008 — clasificacion ya viene calculada externamente

VERSIONES:
  v25.0 — Separacion de responsabilidades. Clasificacion → F1_LADOS_CLASIFICAR.
          Sin logica de clasificacion interna. Sin lectura de JSON.
================================================================================
"""

import Rhino.Geometry as rg
import json

# ==============================================================================
# CONSTANTES
# ==============================================================================

ALTURA_MIN_ENTREPISO = 2.5
ALTURA_MAX_ENTREPISO = 3.8
TOLERANCIA = 0.01

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


def parse_json_safe(data):
    if data is None: return {}
    if isinstance(data, str):
        try: return json.loads(data)
        except: return {}
    if isinstance(data, (dict, list)): return data
    return {}


def extract_segments(curve):
    if curve is None: return []
    success, poly = curve.TryGetPolyline()
    if not success or poly is None: return []
    c = poly.Count
    is_closed = (c >= 2 and poly[0].DistanceTo(poly[c-1]) < 0.001)
    n = c - 1 if is_closed else c
    return [rg.Line(poly[i], poly[(i+1) % c]) for i in range(n)]


def build_setback_map(sides_table):
    """
    Convierte clasificacion en mapa de retiros (m).
    Reglas:
      Frontal:        3.0m (o 5.0m si via a < 5m)
      Posterior:      3.0m
      EspacioPublico: 0.0m (sin retiro — linda con parque/plaza/z. verde)
      Lateral:        0.0m (Continua)
    """
    n = len(sides_table) if isinstance(sides_table, list) else 0
    setback_map = {}
    front_indices = []

    if n == 0:
        return setback_map, front_indices

    for side in sides_table:
        # Soportar ambos formatos: v02 (id/clasificacion) y v22 (side_index/classification)
        idx = side.get("id", side.get("side_index", 0))
        cls = side.get("clasificacion", side.get("classification", "Lateral"))
        dist = side.get("distancia_min_a_via", side.get("dist_to_via_m", 99))

        if cls == "Frontal":
            sb = 5.0 if dist < 5.0 else 3.0
            front_indices.append(idx)
        elif cls == "Posterior":
            sb = 3.0
        elif cls == "EspacioPublico":
            sb = 0.0  # Sin retiro sobre parque/zona verde
        else:  # Lateral u otros
            sb = 0.0

        setback_map[idx] = sb

    return setback_map, front_indices


def inward_normal(seg, centroid):
    mid = rg.Point3d((seg.From.X + seg.To.X) / 2.0,
                     (seg.From.Y + seg.To.Y) / 2.0, 0)
    to_ctr = rg.Vector3d(centroid.X - mid.X, centroid.Y - mid.Y, 0)
    sd = rg.Vector3d(seg.To.X - seg.From.X, seg.To.Y - seg.From.Y, 0)
    sd.Unitize()
    n1 = rg.Vector3d(-sd.Y, sd.X, 0)
    n2 = rg.Vector3d(sd.Y, -sd.X, 0)
    return n1 if (n1.X * to_ctr.X + n1.Y * to_ctr.Y) > (n2.X * to_ctr.X + n2.Y * to_ctr.Y) else n2


def build_footprint(segments, centroid, setback_map):
    n = len(segments)
    setbacks = [setback_map.get(i, 0.0) for i in range(n)]
    max_sb = max(setbacks)

    if max_sb < 0.01:
        pts = [seg.From for seg in segments] + [segments[0].From]
        return rg.PolylineCurve(pts), "Sin retiros"

    pts = [seg.From for seg in segments] + [segments[0].From]
    lot_polygon = rg.PolylineCurve(pts)

    offset_curves = None
    for factor in [1.0, 0.7, 0.5]:
        try:
            curves = lot_polygon.Offset(
                rg.Plane.WorldXY, -max_sb * factor, TOLERANCIA, rg.CurveOffsetCornerStyle.Sharp)
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
            strips.append(rg.PolylineCurve([
                orig_seg.From, orig_seg.To,
                off_seg.To, off_seg.From, orig_seg.From
            ]))

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
    if footprint is None or patio_curves is None:
        return footprint

    patios = patio_curves if isinstance(patio_curves, list) else [patio_curves]
    patios = [p for p in patios if p is not None]
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

lot_polygon_raw     = globals().get("lot_polygon", None)
sides_table_raw     = globals().get("sides_table_json", None)
patio_curve_raw     = globals().get("patio_curve", None)
altura_max_raw      = globals().get("altura_max_pot", None)
tratamiento_raw     = globals().get("tratamiento", None)
rango_edif_raw      = globals().get("rango_edificabilidad", None)
floor_height_raw    = globals().get("floor_height_user", None)

lot_polygon   = unwrap(lot_polygon_raw)
patio_curve   = patio_curve_raw
altura_pot    = to_float_safe(unwrap(altura_max_raw), 11.4, min_val=0.5)
tratamiento   = str(unwrap(tratamiento_raw) or "Consolidacion")
rango_edif    = str(unwrap(rango_edif_raw) or "3")
floor_height  = to_float_safe(unwrap(floor_height_raw),
                               ALTURA_MIN_ENTREPISO, min_val=ALTURA_MIN_ENTREPISO)
if floor_height > ALTURA_MAX_ENTREPISO:
    floor_height = ALTURA_MAX_ENTREPISO

# Parametros normativos por tratamiento
tlow = tratamiento.lower()
io_maximo, ic_maximo = 0.70, 2.0  # defaults Consolidacion
if "desarrollo" in tlow:     io_maximo, ic_maximo = 0.50, 3.0
elif "renovacion" in tlow:   io_maximo, ic_maximo = 0.60, 5.0
elif "conservacion" in tlow: io_maximo, ic_maximo = 0.50, 2.0

floors_norm = RANGO_PISOS.get(rango_edif, 5)

if lot_polygon is None:
    envelope_curve = None
    mensaje = "ERROR: lot_polygon es None"
else:
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
        mensaje = "ERROR: < 3 lados"
    else:
        # Clasificacion YA VIENE calculada
        sides_table = parse_json_safe(sides_table_raw)
        if isinstance(sides_table, dict):
            sides_table = sides_table.get("sides", sides_table.get("lados", []))
        if not isinstance(sides_table, list):
            sides_table = []

        setback_map, front_indices = build_setback_map(sides_table)

        # Huella
        footprint, offset_diag = build_footprint(segments, centroid, setback_map)
        if footprint is None:
            footprint = lot_polygon
            offset_diag = "build_footprint devolvio None"

        # Patios
        patio_count = 0
        if patio_curve is not None and footprint is not None:
            footprint = subtract_patios(footprint, patio_curve)
            if isinstance(patio_curve, list):
                patio_count = len([p for p in patio_curve if p is not None])
            else:
                patio_count = 1

        # Area huella
        try:
            area_env = rg.AreaMassProperties.Compute(footprint).Area
        except:
            area_env = area_lote

        if area_env <= 0: area_env = 1.0
        if area_env > area_lote * 1.5:
            footprint = lot_polygon
            area_env = area_lote

        ocupacion_real = area_env / area_lote if area_lote > 0 else 0

        # Pisos y altura
        altura_solicitada = floors_norm * floor_height
        if altura_solicitada > altura_pot and altura_pot > 0:
            pisos_aplicados = max(1, int(altura_pot / floor_height))
            altura_total = pisos_aplicados * floor_height
        else:
            pisos_aplicados = floors_norm
            altura_total = altura_solicitada

        ic_real = (area_env * pisos_aplicados) / area_lote if area_lote > 0 else 0
        envelope_curve = footprint

        # Mensaje
        nf = len(front_indices)
        partes = [
            "=== NORMATIVA v25 ===",
            "Tratamiento: {} | Rango: {} | Pisos max: {}".format(tratamiento, rango_edif, floors_norm),
            "Lote: {} lados | Area: {:.1f}m2 | Huella: {:.1f}m2".format(n_sides, area_lote, area_env),
            "Frentes: {}/{} | Altura POT: {:.1f}m".format(nf, n_sides, altura_pot),
            "IO: {:.2f}/Max {:.2f} | IC: {:.2f}/Max {:.2f}".format(
                ocupacion_real, io_maximo, ic_real, ic_maximo),
            "Pisos: {} x {:.2f}m = {:.2f}m".format(pisos_aplicados, floor_height, altura_total),
            "Offset: {} | Patios: {}".format(offset_diag, patio_count),
        ]

        for i in sorted(setback_map.keys()):
            tag = "F" if i in front_indices else "L"
            partes.append("  L{}({}): retiro={:.1f}m".format(i, tag, setback_map[i]))

        if ocupacion_real > io_maximo:
            partes.append("ALERTA: IO excede maximo")
        if ic_real > ic_maximo:
            partes.append("ALERTA: IC excede maximo")

        mensaje = "\n".join(partes)
        print(mensaje)
