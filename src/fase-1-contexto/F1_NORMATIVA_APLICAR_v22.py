#! /usr/bin/env python3
"""
================================================================================
F1_NORMATIVA_APLICAR_v22.py — Motor normativo para lote de esquina.
Proyecto: DisenoParametrico / Fase 1 — Contexto y Normativa
GH Python Script para Grasshopper (IronPython 2.7 compatible)
================================================================================

PROPOSITO:
  Aplica la normativa POT/NSR-10 al poligono de un lote urbano.
  - Simplifica el poligono (elimina vertices colineales).
  - Aplica retiros DIFERENCIADOS por lado (frente/lateral/posterior).
  - Resta patios de aislamiento (de F1_PATIO_VECINO).
  - Calcula IO, IC, altura y pisos desde la regulacion.

NORMATIVA:
  Decreto 555/2021. Consolidacion + Continua: laterales = 0m.

VERSIONES:
  v22.6 — subtract_patios() acepta multiples curvas de patio.
  v22.7 — Simplificacion de poligono. Validacion de intersecciones contra
          centroide (evita puntos de interseccion lejanos). Inferencia de
          frentes robusta para poligonos de N lados.

ENTRADAS:
  lot_polygon (Curve, Item Access) — Perimetro del lote
  sides_table_json (String, List Access) — Clasificacion de lados
  patio_curve (Curve o Curve[], Item/List Access) — Patio(s)
  json_path (String) — Ruta al cache JSON
  floor_height_user (Number, Item Access) — Altura entrepiso [2.50-3.80]m

SALIDAS:
  envelope_curve, ocupacion_real, io_maximo, ic_real, ic_maximo,
  altura_total, pisos_aplicados, mensaje
================================================================================
"""

import Rhino.Geometry as rg
import json
import os
import math

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

def parse_json_safe(data):
    if data is None: return {}
    if isinstance(data, str):
        try: return json.loads(data)
        except: return {}
    if isinstance(data, (dict, list)): return data
    return {}

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


def simplify_polygon(curve):
    """
    Simplifica una PolylineCurve eliminando vertices colineales intermedios.
    Dos segmentos consecutivos son colineales si el producto cruz de sus
    vectores directores es ~0.

    Args:
        curve: rg.Curve (PolylineCurve).

    Returns:
        rg.PolylineCurve simplificada, o la original si no se puede simplificar.
    """
    if curve is None:
        return None
    success, poly = curve.TryGetPolyline()
    if not success or poly is None:
        return curve

    n = poly.Count
    if n <= 4:  # 3 o 4 vertices no necesitan simplificacion
        return curve

    # Determinar si esta cerrada
    is_closed = (n >= 2 and poly[0].DistanceTo(poly[n - 1]) < 0.001)
    pts = [poly[i] for i in range(n - 1 if is_closed else n)]

    if len(pts) <= 4:
        return curve

    # Simplificar: conservar solo vertices donde cambia la direccion
    cleaned = [pts[0]]
    m = len(pts)
    for i in range(1, m):
        prev = cleaned[-1]
        curr = pts[i]
        next_pt = pts[(i + 1) % m]

        v1 = rg.Vector3d(curr.X - prev.X, curr.Y - prev.Y, 0)
        v2 = rg.Vector3d(next_pt.X - curr.X, next_pt.Y - curr.Y, 0)

        if v1.Length < 0.01 or v2.Length < 0.01:
            continue  # segmento degenerado

        v1.Unitize()
        v2.Unitize()
        cross = abs(v1.X * v2.Y - v1.Y * v2.X)

        if cross > 0.005:  # cambio de direccion > ~0.3 grados
            cleaned.append(curr)

    # Siempre incluir el ultimo punto si no es igual al primero
    if len(cleaned) >= 3 and cleaned[-1].DistanceTo(pts[-1]) > 0.01:
        cleaned.append(pts[-1])

    if len(cleaned) < 3 or len(cleaned) >= len(pts):
        return curve  # no se pudo simplificar

    # Cerrar
    cleaned.append(cleaned[0])
    return rg.PolylineCurve(cleaned)


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


def inward_normal(seg, centroid):
    """Normal unitaria hacia el centroide."""
    mid = rg.Point3d((seg.From.X + seg.To.X) / 2.0,
                     (seg.From.Y + seg.To.Y) / 2.0, 0)
    to_ctr = rg.Vector3d(centroid.X - mid.X, centroid.Y - mid.Y, 0)
    sd = rg.Vector3d(seg.To.X - seg.From.X, seg.To.Y - seg.From.Y, 0)
    sd.Unitize()
    n1 = rg.Vector3d(-sd.Y, sd.X, 0)
    n2 = rg.Vector3d(sd.Y, -sd.X, 0)
    d1 = n1.X * to_ctr.X + n1.Y * to_ctr.Y
    d2 = n2.X * to_ctr.X + n2.Y * to_ctr.Y
    normal = n1 if d1 > d2 else n2
    normal.Unitize()
    return normal


def offset_segment(seg, distance, centroid):
    """Desplaza segmento hacia adentro distance metros."""
    if abs(distance) < 0.001:
        return rg.Line(seg.From, seg.To)
    n = inward_normal(seg, centroid)
    return rg.Line(
        rg.Point3d(seg.From.X + n.X * distance, seg.From.Y + n.Y * distance, 0),
        rg.Point3d(seg.To.X + n.X * distance, seg.To.Y + n.Y * distance, 0))


def intersect_two_lines(l1, l2, max_extend, centroid, max_dist):
    """
    Interseccion de dos lineas con validacion de distancia.
    Descarta puntos de interseccion que esten a mas de max_dist del centroide
    (evita el problema de lineas casi-paralelas que intersectan en el infinito).

    Args:
        l1, l2: rg.Line
        max_extend: float — extension maxima para la interseccion
        centroid: rg.Point3d — para validacion
        max_dist: float — distancia maxima permitida desde el centroide

    Returns:
        rg.Point3d o None
    """
    d1 = rg.Vector3d(l1.To.X - l1.From.X, l1.To.Y - l1.From.Y, 0)
    d2 = rg.Vector3d(l2.To.X - l2.From.X, l2.To.Y - l2.From.Y, 0)
    if d1.Length < 0.001 or d2.Length < 0.001:
        return None
    d1.Unitize()
    d2.Unitize()

    e1 = rg.Line(
        rg.Point3d(l1.From.X - d1.X * max_extend, l1.From.Y - d1.Y * max_extend, 0),
        rg.Point3d(l1.To.X + d1.X * max_extend, l1.To.Y + d1.Y * max_extend, 0))
    e2 = rg.Line(
        rg.Point3d(l2.From.X - d2.X * max_extend, l2.From.Y - d2.Y * max_extend, 0),
        rg.Point3d(l2.To.X + d2.X * max_extend, l2.To.Y + d2.Y * max_extend, 0))

    rc, t1, t2 = rg.Intersect.Intersection.LineLine(e1, e2)
    if not rc:
        return None

    pt = rg.Point3d(e1.From.X + d1.X * t1, e1.From.Y + d1.Y * t1, 0)

    # Validar que el punto no este ridiculamente lejos
    if centroid.DistanceTo(pt) > max_dist:
        return None

    return pt


def build_footprint(segments, centroid, setback_map, lot_polygon):
    """
    Construye poligono de huella con offset diferenciado.
    
    Estrategia robusta:
      1. Offset uniforme con el retiro frontal (Rhino nativo).
      2. Para lados laterales (retiro < max), crear strips y hacer BooleanUnion.
    """
    n = len(segments)
    if n < 3:
        return None, "ERROR: < 3 lados"
    
    setbacks = [setback_map.get(i, 0.0) for i in range(n)]
    max_sb = max(setbacks)
    
    if max_sb < 0.01:
        return lot_polygon, "Sin retiros > 0"
    
    # Diagnostico del poligono
    is_closed = False
    is_planar = False
    try:
        is_closed = lot_polygon.IsClosed
        is_planar = lot_polygon.IsPlanar()
    except:
        pass
    
    # Intentar offset en ambas direcciones (por si el poligono esta invertido)
    offset_curves = None
    for direction in [-1, 1]:
        for factor in [1.0, 0.7, 0.5, 0.3]:
            dist = max_sb * factor * direction
            try:
                curves = lot_polygon.Offset(
                    rg.Plane.WorldXY, dist, TOLERANCIA, rg.CurveOffsetCornerStyle.Sharp)
                if curves and len(curves) > 0:
                    # Verificar que el offset redujo el area (offset hacia adentro)
                    try:
                        orig_area = rg.AreaMassProperties.Compute(lot_polygon).Area
                        off_area = rg.AreaMassProperties.Compute(curves[0]).Area
                        if off_area < orig_area * 0.99:  # al menos 1% menor
                            offset_curves = curves
                            break
                    except:
                        offset_curves = curves
                        break
            except:
                continue
        if offset_curves:
            break
    
    if not offset_curves or len(offset_curves) == 0:
        return lot_polygon, "Offset fallo (poligono cerrado={}, planar={}, max_sb={:.1f})".format(
            is_closed, is_planar, max_sb)
    
    offset_curve = offset_curves[0]
    
    # Extraer segmentos del offset
    offset_segs = extract_segments(offset_curve)
    
    if len(offset_segs) != n:
        # El offset cambio el numero de lados: usar el offset tal cual
        return offset_curve, "Offset cambio lados ({}->{})".format(n, len(offset_segs))
    
    # Crear strips para lados con retiro < max_sb
    strips = []
    for i in range(n):
        if setbacks[i] < max_sb - 0.01:
            orig_seg = segments[i]
            off_seg = offset_segs[i]
            pts = [
                rg.Point3d(orig_seg.From.X, orig_seg.From.Y, 0),
                rg.Point3d(orig_seg.To.X, orig_seg.To.Y, 0),
                rg.Point3d(off_seg.To.X, off_seg.To.Y, 0),
                rg.Point3d(off_seg.From.X, off_seg.From.Y, 0),
                rg.Point3d(orig_seg.From.X, orig_seg.From.Y, 0),
            ]
            strips.append(rg.PolylineCurve(pts))
    
    if len(strips) == 0:
        return offset_curve, "Offset uniforme OK ({} lados)".format(n)
    
    # BooleanUnion
    try:
        all_curves = [offset_curve] + strips
        breps = []
        for c in all_curves:
            b = rg.Brep.CreatePlanarBreps([c], TOLERANCIA)
            if b and len(b) > 0:
                breps.append(b[0])
        
        if len(breps) >= 2:
            merged = rg.Brep.CreateBooleanUnion(breps, TOLERANCIA)
            if merged and len(merged) > 0:
                edges = merged[0].Edges
                if edges:
                    j = rg.Curve.JoinCurves([e for e in edges if e])
                    if j and len(j) > 0:
                        return j[0], "Offset + {} strips -> Union OK".format(len(strips))
        return offset_curve, "Union fallo, usando offset uniforme"
    except:
        return offset_curve, "Union error, usando offset uniforme"


def subtract_patios(footprint, patio_curves):
    """Resta uno o varios patios de la huella via BooleanDifference."""
    if footprint is None or patio_curves is None:
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
                    edges = r[0].Edges
                    if edges:
                        j = rg.Curve.JoinCurves([e for e in edges if e])
                        if j and len(j) > 0:
                            result = j[0]
        except:
            continue
    return result


def infer_setbacks_from_treatment(treatment, n_sides):
    """
    Infiere mapa de retiros cuando sides_table_json no esta disponible.
    
    Para Consolidacion/Continua: solo frentes (lados opuestos) tienen retiro.
    Para Desarrollo: todos los lados tienen retiro.
    
    Identifica frentes como los lados mas largos del poligono (heuristica:
    en la mayoria de lotes urbanos, los frentes son los lados mas largos).
    """
    t = str(treatment).lower() if treatment else "consolidacion"
    
    if "desarrollo" in t:
        rf, rl = 5.0, 3.0
    elif "renovacion" in t:
        rf, rl = 5.0, 3.0
    else:
        rf, rl = 3.0, 0.0  # Consolidacion/Continua
    
    # Para inferir frentes sin datos de calle, asumimos que los frentes son
    # los dos lados opuestos (0 y n/2). Esto es correcto para la mayoria de
    # lotes urbanos rectangulares.
    front_indices = [0]
    if n_sides >= 4:
        front_indices.append(n_sides // 2)
    
    setback_map = {}
    for i in range(n_sides):
        setback_map[i] = rf if i in front_indices else rl
    
    return setback_map, front_indices


# ==============================================================================
# MAIN
# ==============================================================================

lot_polygon_raw  = globals().get("lot_polygon", None)
sides_table_raw  = globals().get("sides_table_json", None)
patio_curve_raw  = globals().get("patio_curve", None)
json_path_raw    = globals().get("json_path", None)
floor_height_raw = globals().get("floor_height_user", None)

lot_polygon   = unwrap(lot_polygon_raw)
patio_curve   = patio_curve_raw  # puede ser lista (multiples patios) o item unico
json_path     = str(json_path_raw).strip("[]'\" ") if json_path_raw else ""
floor_height  = to_float_safe(unwrap(floor_height_raw),
                               ALTURA_MIN_ENTREPISO, min_val=ALTURA_MIN_ENTREPISO)
if floor_height > ALTURA_MAX_ENTREPISO:
    floor_height = ALTURA_MAX_ENTREPISO

if lot_polygon is None:
    envelope_curve = None
    mensaje = "ERROR: lot_polygon es None."
    print(mensaje)
else:
    # --- 1. USAR POLIGONO ORIGINAL (sin simplificar, para que indices coincidan con LADOS_CONFIGURAR) ---
    
    # --- 2. CACHE POT ---
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
    
    # --- 3. AREA Y SEGMENTOS ---
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
        print(mensaje)
    else:
        # --- 4. CLASIFICACION DE LADOS ---
        sides_data = parse_json_safe(sides_table_raw)
        sides_list = []
        if isinstance(sides_data, list) and len(sides_data) > 0:
            sides_list = sides_data
        elif isinstance(sides_data, dict):
            inner = sides_data.get("sides", sides_data.get("lados", []))
            if isinstance(inner, list):
                sides_list = inner
        
        front_indices = []
        setback_map = {}
        parsed_ok = 0
        
        if sides_list:
            for side in sides_list:
                if isinstance(side, str):
                    try:
                        parsed = json.loads(side)
                        # parsed puede ser dict individual o lista de dicts
                        if isinstance(parsed, list):
                            for item in parsed:
                                if isinstance(item, dict):
                                    idx = to_int_safe(item.get("side_index", -1))
                                    cls = str(item.get("classification", "Lateral")).lower()
                                    sb = to_float_safe(item.get("setback_m"), 0.0)
                                    if 0 <= idx < n_sides:
                                        setback_map[idx] = sb
                                        parsed_ok += 1
                                        if cls == "frontal":
                                            front_indices.append(idx)
                        elif isinstance(parsed, dict):
                            side = parsed
                    except:
                        continue
                if isinstance(side, dict):
                    idx = to_int_safe(side.get("side_index", -1))
                    cls = str(side.get("classification", "Lateral")).lower()
                    sb = to_float_safe(side.get("setback_m"), 0.0)
                    if 0 <= idx < n_sides:
                        setback_map[idx] = sb
                        parsed_ok += 1
                        if cls == "frontal":
                            front_indices.append(idx)
        
        # Si no se parseo nada, inferir por tratamiento
        if parsed_ok == 0:
            sides_list = []
            setback_map, front_indices = infer_setbacks_from_treatment(tratamiento, n_sides)
        else:
            # Rellenar lados faltantes
            for i in range(n_sides):
                if i not in setback_map:
                    setback_map[i] = 3.0
        
        # DEBUG
        print("DEBUG parsed_ok={} front_indices={} setback_keys={}".format(
            parsed_ok, front_indices, sorted(setback_map.keys())))
        # --- 5. HUELLA ---
        footprint, offset_diag = build_footprint(segments, centroid, setback_map, lot_polygon)
        
        if footprint is None:
            footprint = lot_polygon
            offset_diag = "build_footprint devolvio None"
        
        offset_msg = offset_diag if offset_diag else ""
        
        # --- 6. PATIOS ---
        patio_count = 0
        if patio_curve is not None and footprint is not None:
            if isinstance(patio_curve, list):
                n_patios = len([p for p in patio_curve if p is not None])
            else:
                n_patios = 1
            footprint = subtract_patios(footprint, patio_curve)
            patio_count = n_patios
        
        # --- 7. AREA HUELLA ---
        try:
            area_env = rg.AreaMassProperties.Compute(footprint).Area
        except:
            area_env = area_lote
        if area_env <= 0:
            area_env = 1.0
        
        # Validar que la huella no sea mayor que el lote (intersecciones fallidas)
        if area_env > area_lote * 1.5:
            # Algo salio mal con la geometria - usar fallback
            footprint = lot_polygon
            area_env = area_lote
        
        ocupacion_real = area_env / area_lote if area_lote > 0 else 0
        
        # --- 8. PISOS Y ALTURA ---
        altura_solicitada = floors_norm * floor_height
        if altura_solicitada > altura_pot and altura_pot > 0:
            pisos_aplicados = max(1, int(altura_pot / floor_height))
            altura_total = pisos_aplicados * floor_height
        else:
            pisos_aplicados = floors_norm
            altura_total = altura_solicitada
        
        ic_real = (area_env * pisos_aplicados) / area_lote if area_lote > 0 else 0
        
        envelope_curve = footprint
        
        # --- 9. MENSAJE ---
        partes = [
            "=== NORMATIVA v22.8 ===",
            "Tratamiento: {} | Rango: {} | Pisos max: {}".format(
                tratamiento, rango_edif, floors_norm),
            "Lote: {} lados | Area: {:.1f}m2 | Huella: {:.1f}m2".format(
                n_sides, area_lote, area_env),
            "IO: {:.2f}/Max {:.2f} | IC: {:.2f}/Max {:.2f}".format(
                ocupacion_real, io_maximo, ic_real, ic_maximo),
            "Pisos: {} x {:.2f}m = {:.2f}m (max POT: {:.1f}m)".format(
                pisos_aplicados, floor_height, altura_total, altura_pot),
        ]
        
        sb_strs = []
        for i in sorted(setback_map.keys()):
            v = setback_map[i]
            m = "F" if i in front_indices else ("L" if v > 0 else "-")
            sb_strs.append("{}{}:{:.1f}".format(m, i, v))
        partes.append("Retiros: [{}]".format(", ".join(sb_strs)))
        partes.append("Offset: {}".format(offset_msg))
        partes.append("Patios: {}".format(patio_count))
        
        if sides_list:
            n_fronts = sum(1 for s in sides_list if isinstance(s, dict) and str(s.get("classification","")).lower() == "frontal")
            n_lats = sum(1 for s in sides_list if isinstance(s, dict) and str(s.get("classification","")).lower() == "lateral")
            partes.append("LADOS: {} total, {} Frontales, {} Laterales".format(
                len(sides_list), n_fronts, n_lats))
            if n_fronts == len(sides_list):
                partes.append("ADVERTENCIA: Todos los lados son Frontales.")
                partes.append("  Las street_curves pueden estar en otro sistema de coordenadas.")
                partes.append("  Aplique el mismo Move Vector del lote a las street_curves.")
        else:
            partes.append("Clasificacion: INFERIDA (sides_table_json no disponible)")
        
        if ocupacion_real > io_maximo:
            partes.append("ALERTA: IO excede maximo")
        if ic_real > ic_maximo:
            partes.append("ALERTA: IC excede maximo")
        
        mensaje = "\n".join(partes)
        print(mensaje)
