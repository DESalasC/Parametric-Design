"""
================================================================================
F1_ETAPA2_NORMATIVA_v03.py — Retiros + Patios + Indices + Piso Adicional
Proyecto: DisenoParametrico / Fase 1
GH Python Script para Grasshopper (IronPython 2.7 compatible)
================================================================================

CALCULO:
  1. Descontar retiro FRONTAL del lado frontal del lote
  2. NO descontar retiro en lados EspacioPublico (0m)
  3. Restar el patio (desde vertice N) del perimetro restante (Boolean Diff)
  4. Calcular pisos base (Decreto 555/2021) y aplicar PISO ADICIONAL
  5. Calcular GFA (Gross Floor Area) maximo para Fase 2

NOTA NORMATIVA:
  La altura total se define por el NUMERO DE PISOS permitido (rango + 
  incentivos) multiplicado por la altura de entrepiso. El campo ALTURA en 
  metros del POT GDB se ignora como tope absoluto por ser cota/código.

ENTRADAS:
  lot_polygon (Curve)            — Lote simplificado
  sides_table_json (String)      — Clasificacion (F1_ETAPA2_LADOS_v02)
  patio_curves (Curve[])         — Patio(s) (F1_ETAPA2_PATIO_v02)
  altura_max_pot (Number)        — [OBSOLETO] Se mantiene para no romper canvas
  tratamiento (String)           — Tratamiento urbanistico
  rango_edificabilidad (String)  — Rango "1".."5" (Decreto 555)
  floor_height_user (Number)     — Altura entrepiso [m]
  io_maximo_user (Number)        — IO normativo (override)
  piso_adicional (bool)          — True si se acoge al incentivo normativo
  tipo_bonificacion (String)     — "VIS", "Comunal", "Equipamiento", "Ninguno"

SALIDAS:
  envelope_curve (Curve/List)    — Huella física con retiros y patio restado
  gfa_total (Number)             — Area Bruta Construida (incluye piso extra)
  ocupacion_real, io_maximo, ic_real, ic_maximo,
  altura_total, pisos_finales, valido (bool), mensaje
================================================================================
"""

import Rhino.Geometry as rg
import json
import math

# Rangos de edificabilidad corregidos según Decreto 555/2021
RANGO_PISOS = {"1": 1, "2": 2, "3": 4, "4": 5, "5": 7}
TOLERANCIA = 0.01

def unwrap(val):
    if val is None: return None
    if isinstance(val, list): return val[0] if len(val) > 0 else None
    return val

def safe_list(val):
    if val is None: return []
    if isinstance(val, list): return val
    return [val]

def parse_gh_bool(val):
    """Funcion a prueba de fallos para leer Toggles de Grasshopper"""
    if val is None: return False
    if isinstance(val, list): val = val[0] if len(val) > 0 else None
    if val is None: return False
    if isinstance(val, bool): return val
    s = str(val).strip().lower()
    if s in ("true", "1", "verdadero", "yes", "si"):
        return True
    return False

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
    dx1 = a2.X - a1.X; dy1 = a2.Y - a1.Y
    dx2 = b2.X - b1.X; dy2 = b2.Y - b1.Y
    denom = dx1 * dy2 - dy1 * dx2
    if abs(denom) < 1e-9:
        return None
    t = ((b1.X - a1.X) * dy2 - (b1.Y - a1.Y) * dx2) / denom
    return rg.Point3d(a1.X + t * dx1, a1.Y + t * dy1, 0)

def build_footprint_retiros(lot_polygon, retiros):
    segs = extract_segments(lot_polygon)
    if not segs:
        return lot_polygon

    n = len(segs)
    ctr = centroide_puntos([seg.From for seg in segs])

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

    pts_nuevos = []
    for i in range(n):
        j = (i + 1) % n
        a1, a2 = lineas_desplazadas[i]
        b1, b2 = lineas_desplazadas[j]
        inter = interseccion_lineas_2d(a1, a2, b1, b2)
        if inter is None:
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
altura_raw = globals().get("altura_max_pot", None) # Se ignora, pero se mantiene para no romper el input del canvas
tratamiento_raw = globals().get("tratamiento", None)
rango_raw = globals().get("rango_edificabilidad", None)
floor_h_raw = globals().get("floor_height_user", None)
io_user_raw = globals().get("io_maximo_user", None)

# Usamos el parser estricto
piso_adicional = parse_gh_bool(globals().get("piso_adicional", False))

# Para el tipo de bonificacion, aseguramos que sea un string limpio
tipo_bonif_raw = globals().get("tipo_bonificacion", "Ninguno")
tipo_bonificacion = str(unwrap(tipo_bonif_raw)).strip() if tipo_bonif_raw else "Ninguno"

sides_data = None
if sides_raw is not None:
    try:
        s = str(sides_raw[0]) if isinstance(sides_raw, list) and sides_raw else str(sides_raw)
        sides_data = json.loads(s)
    except:
        sides_data = None

lados = sides_data.get("lados", []) if sides_data else []

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
    else:
        retiros[idx] = 0.0

# --- Inicializar outputs ---
envelope_curve = None
ocupacion_real = 0.0
valido = False
area_lote = area_curve(lot_polygon) if lot_polygon else 0.0

# --- 1. Construir huella con retiros ---
huella_retiros = None
if lot_polygon is not None:
    try:
        huella_retiros = build_footprint_retiros(lot_polygon, retiros)
    except:
        huella_retiros = lot_polygon

# --- 2. Restar patios geométricamente (Boolean Difference) ---
patios_list = [p for p in safe_list(patio_raw) if p is not None]
patio_area_total = 0.0
huella_bruta = area_curve(huella_retiros) if huella_retiros else 0.0

if huella_retiros is not None and patios_list:
    for patio in patios_list:
        patio_area_total += area_curve(patio)
    
    diff_curves = rg.Curve.CreateBooleanDifference(huella_retiros, patios_list, TOLERANCIA)
    
    if diff_curves and len(diff_curves) > 0:
        joined = rg.Curve.JoinCurves(diff_curves, TOLERANCIA)
        envelope_curve = joined if len(joined) > 1 else joined[0]
        
        max_a = 0.0
        inner_a = 0.0
        for c in diff_curves:
            a = area_curve(c)
            if a > max_a:
                inner_a += max_a
                max_a = a
            else:
                inner_a += a
        ocupacion_real = max(0.0, max_a - inner_a)
    else:
        envelope_curve = huella_retiros
        ocupacion_real = max(0.0, huella_bruta - patio_area_total)
else:
    envelope_curve = huella_retiros
    ocupacion_real = huella_bruta

# --- 3. Validacion y Indices ---
valido = ocupacion_real < area_lote - 0.01 and ocupacion_real > 0.0

if io_user > 0:
    io_maximo = io_user
elif tratamiento == "Consolidacion":
    io_maximo = 0.70
elif tratamiento in ("Desarrollo", "Mejoramiento"):
    io_maximo = 0.60
else:
    io_maximo = 0.70

# --- 4. PISOS Y ALTURA (Decreto 555/2021 + Incentivos) ---
ic_maximo_base = RANGO_PISOS.get(rango, 4) # Default a 4 si no encuentra el rango

pisos_extra = 0
if piso_adicional and tipo_bonificacion != "NINGUNO":
    pisos_extra = 1
    if tipo_bonificacion in ("VIS", "VIP","EQUIPAMENTO + COMUNAL" ):
        pisos_extra = 2 

# El número de pisos es directo: rango base + pisos extra por incentivos
ic_maximo = ic_maximo_base + pisos_extra
pisos_finales = ic_maximo
altura_total = pisos_finales * floor_h

# --- 5. GFA (Gross Floor Area) ---
gfa_total = ocupacion_real * pisos_finales
ic_real = (ocupacion_real / area_lote * ic_maximo) if area_lote > 0 else 0.0

if valido:
    mensaje = "NORMATIVA v03 | OK | Lote: {:.1f}m2 | Ocup: {:.1f}m2 | IO {:.2f} | IC {:.2f} (+{}) | Alt {:.1f}m | {} pisos | GFA: {:.1f}m2 | Patios {:.1f}m2".format(
        area_lote, ocupacion_real, io_maximo, ic_real, pisos_extra, altura_total,
        pisos_finales, gfa_total, patio_area_total)
else:
    mensaje = "NORMATIVA v03 | ERROR DE VALIDACION | Ocupacion ({:.1f}) >= Area bruta ({:.1f})".format(
        ocupacion_real, area_lote)
    