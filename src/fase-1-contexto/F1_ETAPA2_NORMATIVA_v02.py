"""
================================================================================
F1_ETAPA2_NORMATIVA_v02.py — Retiros + Patios + Indices + Validacion
Proyecto: DisenoParametrico / Fase 1
GH Python Script para Grasshopper (IronPython 2.7 compatible)
================================================================================

CALCULO:
  1. Descontar retiro FRONTAL del lado frontal del lote
  2. NO descontar retiro en lados EspacioPublico (0m)
  3. Restar el patio (desde vertice N) del perimetro restante
  4. La huella resultante = ocupacion real

  VALIDACION CRITICA:
    ocupacion_real NUNCA puede ser >= area bruta del predio.
    Si ocurre, hay error de calculo o de datos de entrada
    (vecinos, vias, zonas verdes, etc.).

ENTRADAS:
  lot_polygon (Curve)            — Lote simplificado
  sides_table_json (String)      — Clasificacion (F1_ETAPA2_LADOS_v02)
  patio_curves (Curve[])         — Patio(s) (F1_ETAPA2_PATIO_v02)
  altura_max_pot (Number)        — Altura maxima [m]
  tratamiento (String)           — Tratamiento urbanistico
  rango_edificabilidad (String)  — Rango "1".."5"
  floor_height_user (Number)     — Altura entrepiso [m]
  io_maximo_user (Number)        — IO normativo (override)

SALIDAS:
  envelope_curve, ocupacion_real, io_maximo, ic_real, ic_maximo,
  altura_total, pisos_aplicados, valido (bool), mensaje
================================================================================
"""

import Rhino.Geometry as rg
import json
import math

RANGO_PISOS = {"1": 2, "2": 3, "3": 5, "4": 8, "5": 12}
TOLERANCIA = 0.01


def unwrap(val):
    if val is None: return None
    if isinstance(val, list): return val[0] if len(val) > 0 else None
    return val


def safe_list(val):
    if val is None: return []
    if isinstance(val, list): return val
    return [val]


def area_curve(crv):
    if crv is None:
        return 0.0
    area_props = rg.AreaMassProperties.Compute(crv)
    return area_props.Area if area_props else 0.0


def extract_segments(curve):
    if curve is None: return []
    success, poly = curve.TryGetPolyline()
    if not success or poly is None: return []
    c = poly.Count
    is_closed = (c >= 2 and poly[0].DistanceTo(poly[c-1]) < 0.001)
    n = c - 1 if is_closed else c
    return [rg.Line(poly[i], poly[(i+1) % c]) for i in range(n)]


def centroide_puntos(puntos):
    sx = sum(p.X for p in puntos)
    sy = sum(p.Y for p in puntos)
    n = len(puntos)
    return rg.Point3d(sx / n, sy / n, 0)


def interseccion_lineas_2d(a1, a2, b1, b2):
    """Interseccion de dos lineas 2D (a1-a2, b1-b2). Retorna Point3d o None."""
    dx1 = a2.X - a1.X; dy1 = a2.Y - a1.Y
    dx2 = b2.X - b1.X; dy2 = b2.Y - b1.Y
    denom = dx1 * dy2 - dy1 * dx2
    if abs(denom) < 1e-9:
        return None  # paralelas
    t = ((b1.X - a1.X) * dy2 - (b1.Y - a1.Y) * dx2) / denom
    return rg.Point3d(a1.X + t * dx1, a1.Y + t * dy1, 0)


def build_footprint_retiros(lot_polygon, retiros):
    """
    Construye la huella desplazando CADA segmento del lote hacia adentro
    segun su retiro (0 si no aplica). Los segmentos desplazados se
    intersectan para formar el poligono de huella.
    """
    segs = extract_segments(lot_polygon)
    if not segs:
        return lot_polygon

    n = len(segs)
    ctr = centroide_puntos([seg.From for seg in segs])

    # Desplazar cada segmento: extremos movidos a lo largo de la normal interior
    lineas_desplazadas = []
    for i, seg in enumerate(segs):
        sb = retiros.get(i, 0.0)
        if sb < 0.01:
            lineas_desplazadas.append((seg.From, seg.To))
            continue
        normal = inward_normal(seg, ctr)
        p1 = rg.Point3d(seg.From.X + normal.X * sb, seg.From.Y + normal.Y * sb, 0)
        p2 = rg.Point3d(seg.To.X + normal.X * sb, seg.To.Y + normal.Y * sb, 0)
        lineas_desplazadas.append((p1, p2))

    # Intersectar segmentos adyacentes desplazados
    pts_nuevos = []
    for i in range(n):
        j = (i + 1) % n
        a1, a2 = lineas_desplazadas[i]
        b1, b2 = lineas_desplazadas[j]
        inter = interseccion_lineas_2d(a1, a2, b1, b2)
        if inter is None:
            # Paralelas: usar el extremo del primer segmento
            inter = a2
        pts_nuevos.append(inter)

    poly = rg.Polyline()
    for p in pts_nuevos:
        poly.Add(p.X, p.Y, p.Z)
    if not poly.IsClosed:
        poly.Add(poly[0])
    return rg.PolylineCurve(poly)


def inward_normal(seg, centroid):
    mid = rg.Point3d((seg.From.X + seg.To.X) / 2.0,
                     (seg.From.Y + seg.To.Y) / 2.0, 0)
    to_ctr = rg.Vector3d(centroid.X - mid.X, centroid.Y - mid.Y, 0)
    sd = rg.Vector3d(seg.To.X - seg.From.X, seg.To.Y - seg.From.Y, 0)
    sd.Unitize()
    n1 = rg.Vector3d(-sd.Y, sd.X, 0)
    n2 = rg.Vector3d(sd.Y, -sd.X, 0)
    return n1 if (n1.X * to_ctr.X + n1.Y * to_ctr.Y) > (n2.X * to_ctr.X + n2.Y * to_ctr.Y) else n2


# ==============================================================================
# MAIN
# ==============================================================================

lot_polygon = globals().get("lot_polygon", None)
sides_raw = globals().get("sides_table_json", None)
patio_raw = globals().get("patio_curves", None)
altura_raw = globals().get("altura_max_pot", None)
tratamiento_raw = globals().get("tratamiento", None)
rango_raw = globals().get("rango_edificabilidad", None)
floor_h_raw = globals().get("floor_height_user", None)
io_user_raw = globals().get("io_maximo_user", None)

# --- Parse clasificacion ---
sides_data = None
if sides_raw is not None:
    try:
        if isinstance(sides_raw, list) and sides_raw:
            s = str(sides_raw[0])
        else:
            s = str(sides_raw)
        sides_data = json.loads(s)
    except:
        sides_data = None

lados = sides_data.get("lados", []) if sides_data else []

# --- Parse normativa ---
try:
    altura_max = float(unwrap(altura_raw)) if altura_raw else 11.4
except:
    altura_max = 11.4

try:
    floor_h = float(unwrap(floor_h_raw)) if floor_h_raw else 3.0
except:
    floor_h = 3.0

try:
    io_user = float(unwrap(io_user_raw)) if io_user_raw else 0.0
except:
    io_user = 0.0

tratamiento = str(unwrap(tratamiento_raw)) if tratamiento_raw else "Consolidacion"
rango = str(unwrap(rango_raw)) if rango_raw else "3"

# --- Retiros por clasificacion ---
retiros = {}
for lado in lados:
    idx = lado.get("id", 0)
    cls = lado.get("clasificacion", "Lateral")
    dist_via = lado.get("dist_v_m", 999)
    if cls == "Frontal":
        retiros[idx] = 5.0 if dist_via < 5.0 else 3.0
    elif cls == "Posterior":
        retiros[idx] = 3.0
    else:  # Lateral, EspacioPublico
        retiros[idx] = 0.0

# --- Construir huella por offsets individuales por lado ---
envelope_curve = None
ocupacion_real = 0.0
valido = False
area_lote = area_curve(lot_polygon) if lot_polygon else 0.0

if lot_polygon is not None:
    try:
        # Huella con retiros POR SEGMENTO (frontal 3-5m, EP/lateral 0m)
        envelope_curve = build_footprint_retiros(lot_polygon, retiros)
    except:
        envelope_curve = lot_polygon

# --- Restar patios de la huella ---
patios_list = safe_list(patio_raw)
patio_area_total = 0.0
huella_bruta = area_curve(envelope_curve) if envelope_curve else 0.0

if envelope_curve is not None and patios_list:
    for patio in patios_list:
        if patio is not None:
            patio_area_total += area_curve(patio)
    ocupacion_real = max(0.0, huella_bruta - patio_area_total)
else:
    ocupacion_real = huella_bruta

# --- VALIDACION CRITICA: ocupacion < area bruta ---
valido = ocupacion_real < area_lote - 0.01

# --- Indices ---
if io_user > 0:
    io_maximo = io_user
elif tratamiento == "Consolidacion":
    io_maximo = 0.70
elif tratamiento in ("Desarrollo", "Mejoramiento"):
    io_maximo = 0.60
else:
    io_maximo = 0.70

ic_maximo = RANGO_PISOS.get(rango, 5)
ic_real = (ocupacion_real / area_lote * ic_maximo) if area_lote > 0 else 0.0

# --- Altura y pisos ---
altura_total = min(altura_max, ic_maximo * floor_h) if altura_max > 0 else ic_maximo * floor_h
pisos_aplicados = max(1, int(round(altura_total / max(floor_h, 0.1))))

if valido:
    mensaje = "NORMATIVA v02 | OK | Lote: {:.1f}m2 | Ocup: {:.1f}m2 | IO {:.2f} | IC {:.2f} | Alt {:.1f}m | {} pisos | Patios {:.1f}m2".format(
        area_lote, ocupacion_real, io_maximo, ic_real, altura_total,
        pisos_aplicados, patio_area_total)
else:
    mensaje = "NORMATIVA v02 | ERROR DE VALIDACION | Ocupacion ({:.1f}) >= Area bruta ({:.1f}) | Revisar datos de entrada".format(
        ocupacion_real, area_lote)
