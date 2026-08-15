# -*- coding: utf-8 -*-
"""
================================================================================
F1_ETAPA2_NORMATIVA_v04.py — Retiros + Patios + Indices + Piso Adicional
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
  metros del POT GDB se ignora como tope absoluto por ser cota/codigo.
  El GFA es TOTAL: gfa_total = ocupacion_real * pisos_finales (NO es por piso).

ENTRADAS:
  lot_polygon (Curve)            - Lote simplificado
  sides_table_json (String)      - Clasificacion (F1_ETAPA2_LADOS_v02)
  patio_curves (Curve[])         - Patio(s) (F1_ETAPA2_PATIO_v02)
  altura_max_pot (Number)        - [OBSOLETO] Se mantiene para no romper canvas
  tratamiento (String)           - Tratamiento urbanistico
  rango_edificabilidad (String)  - Rango "1".."5". v04 tambien acepta
                                   etiquetas ("Rango 3", "3 (4-5 pisos)", "R3").
                                   Si no se puede extraer el rango: default "3"
                                   + aviso en mensaje.
  floor_height_user (Number)     - Altura entrepiso [m]
  io_maximo_user (Number)        - IO normativo (override)
  piso_adicional (bool)          - True si se acoge al incentivo normativo
  tipo_bonificacion (String)     - "NINGUNO" | "VIS" | "VIP" | "COMUNAL" |
                                   "EQUIPAMIENTO" | "EQUIPAMENTO+COMUNAL".
                                   Case-insensitive y tolerante a espacios
                                   (v03 era sensible a mayusculas: "Ninguno"
                                   sumaba +1 piso indebido; corregido en v04).

SALIDAS:
  envelope_curve (Curve/List)    - Huella fisica con retiros y patio restado
  gfa_total (Number)             - Area Bruta Construida TOTAL (incl. piso extra)
  ocupacion_real, io_maximo, ic_real, ic_maximo,
  altura_total, pisos_finales, valido (bool), mensaje

FUNCIONES INTERNAS:
  unwrap(val)            - Extrae el primer elemento si llega lista de GH.
  safe_list(val)         - Normaliza a lista.
  parse_gh_bool(val)     - Lee toggles de GH a prueba de fallos.
  area_curve(crv)        - Area neta de una curva (con huecos restados).
  normalize_rango(val)   - Extrae el digito del rango ("Rango 3" -> "3").
  normalize_bonificacion(val) - Normaliza tipo a mayusculas sin espacios.
  (geometria) extract_segments, centroide_puntos, interseccion_lineas_2d,
               build_footprint_retiros, inward_normal.

VERSIONES:
  v04 (2026-08-15) - Parseo robusto de rango (etiquetas), normalizacion de
                     tipo_bonificacion (case-insensitive, vocabulario
                     alineado: NINGUNO=0, COMUNAL/EQUIPAMIENTO=+1,
                     VIS/VIP/EQUIPAMENTO+COMUNAL=+2), ocupacion_real = suma de
                     fragmentos del boolean diff (estable cuando el patio
                     parte la huella en varias piezas), avisos en mensaje.
  v03 (2026-08-12) - Fix rangos de pisos Decreto 555/2021 (R1=1, R2=2, R3=4,
                     R4=5, R5=7) + toggle piso_adicional (parse_gh_bool) +
                     resta booleana del patio.
  v02 - Predecesor con resta booleana del patio.
  v01 - Primera version modular ETAPA2.
================================================================================
"""

import Rhino.Geometry as rg
import json
import math
import re

# Rangos de edificabilidad corregidos según Decreto 555/2021
RANGO_PISOS = {"1": 1, "2": 2, "3": 4, "4": 5, "5": 7}
# Pisos extra por incentivo (Decreto 555/2021): normalizado a mayusculas
BONIFICACION_PISOS = {
    "NINGUNO": 0,
    "VIS": 2,
    "VIP": 2,
    "EQUIPAMENTO+COMUNAL": 2,
    "EQUIPAMIENTO+COMUNAL": 2,
    "COMUNAL": 1,
    "EQUIPAMIENTO": 1,
}
RANGO_DEFAULT = "3"
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


def normalize_rango(val, warnings):
    """Extrae el digito del rango aceptando etiquetas del Value List.

    "3" -> "3" | "Rango 3" -> "3" | "3 (4-5 pisos)" -> "3" | "R3" -> "3"
    Si no hay digito valido: default "3" + aviso (detecta cables invertidos
    que envian un booleano a esta entrada).
    """
    if val is None:
        return RANGO_DEFAULT
    s = str(unwrap(val)).strip()
    if s == "":
        return RANGO_DEFAULT
    m = re.search(r"(\d+)", s)
    if m and m.group(1) in RANGO_PISOS:
        return m.group(1)
    warnings.append(
        "rango_edificabilidad no reconocido ('%s') -> default %s"
        % (s, RANGO_DEFAULT))
    return RANGO_DEFAULT


def normalize_bonificacion(val, warnings):
    """Normaliza tipo_bonificacion a mayusculas sin espacios alrededor de +.

    "Ninguno"->"NINGUNO" | "EQUIPAMENTO + COMUNAL"->"EQUIPAMENTO+COMUNAL"
    Si el valor no esta en el vocabulario: "NINGUNO" + aviso (detecta un
    toggle cableado por error a esta entrada).
    """
    if val is None:
        return "NINGUNO"
    s = str(unwrap(val)).strip()
    if s == "":
        return "NINGUNO"
    s = s.upper()
    s = re.sub(r"\s*\+\s*", "+", s)
    s = re.sub(r"\s+", " ", s)
    s = s.replace("\u00c1", "A").replace("\u00c9", "E").replace("\u00cd", "I")
    s = s.replace("\u00d3", "O").replace("\u00da", "U").replace("\u00d1", "N")
    if s not in BONIFICACION_PISOS:
        warnings.append(
            "tipo_bonificacion desconocido ('%s') -> sin piso extra" % s)
        return "NINGUNO"
    return s


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

warnings = []

# Usamos el parser estricto
piso_adicional = parse_gh_bool(globals().get("piso_adicional", False))

# Para el tipo de bonificacion, aseguramos que sea un string limpio
tipo_bonif_raw = globals().get("tipo_bonificacion", "Ninguno")
tipo_bonificacion = normalize_bonificacion(tipo_bonif_raw, warnings)

rango = normalize_rango(rango_raw, warnings)

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
        # v04: ocupacion = suma de fragmentos netos (cada curva ya descuenta
        # sus huecos). v03 restaba fragmentos (max_a - inner_a) y podia dar
        # ~0 cuando el patio partia la huella en dos piezas similares.
        ocupacion_real = max(0.0, sum([area_curve(c) for c in diff_curves]))
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
ic_maximo_base = RANGO_PISOS.get(rango, RANGO_PISOS[RANGO_DEFAULT])

pisos_extra = 0
if piso_adicional:
    pisos_extra = BONIFICACION_PISOS.get(tipo_bonificacion, 0)

# El número de pisos es directo: rango base + pisos extra por incentivos
ic_maximo = ic_maximo_base + pisos_extra
pisos_finales = ic_maximo
altura_total = pisos_finales * floor_h

# --- 5. GFA (Gross Floor Area) ---
gfa_total = ocupacion_real * pisos_finales
ic_real = (ocupacion_real / area_lote * ic_maximo) if area_lote > 0 else 0.0

if valido:
    mensaje = "NORMATIVA v04 | OK | Lote: {:.1f}m2 | Ocup: {:.1f}m2 | IO {:.2f} | IC {:.2f} (+{}) | Alt {:.1f}m | {} pisos | GFA: {:.1f}m2 | Patios {:.1f}m2".format(
        area_lote, ocupacion_real, io_maximo, ic_real, pisos_extra, altura_total,
        pisos_finales, gfa_total, patio_area_total)
else:
    mensaje = "NORMATIVA v04 | ERROR DE VALIDACION | Ocupacion ({:.1f}) >= Area bruta ({:.1f})".format(
        ocupacion_real, area_lote)

if warnings:
    mensaje += " | AVISOS: " + "; ".join(warnings)
