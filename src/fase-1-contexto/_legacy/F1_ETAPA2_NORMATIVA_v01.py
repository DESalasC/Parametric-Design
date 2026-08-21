"""
================================================================================
F1_ETAPA2_NORMATIVA_v01.py — Etapa 2: Ocupacion + Patios + Indices
Proyecto: DisenoParametrico / Fase 1
GH Python Script para Grasshopper (IronPython 2.7 compatible)
================================================================================

PROPOSITO:
  Etapa 2 final. Recibe la clasificacion de lados (colindancia real),
  los patios generados y la normativa, y calcula:
    - Huella edificable (lote - retiros - patios)
    - Ocupacion real vs IO maximo
    - IC real vs IC maximo
    - Altura total y pisos

  RETIROS por clasificacion:
    Frontal:        3.0m (5.0m si via < 5m)
    EspacioPublico: 0.0m (sin retiro)
    Lateral:        0.0m (continua)
    Posterior:      3.0m

ENTRADAS:
  lot_polygon (Curve)            — Lote simplificado (4 vertices)
  sides_table_json (String)      — Clasificacion de lados
  patio_curves (Curve[])         — Patios de F1_ETAPA2_PATIO
  altura_max_pot (Number)        — Altura maxima [m]
  tratamiento (String)           — Tipo de tratamiento
  rango_edificabilidad (String)  — Rango "1".."5"
  floor_height_user (Number)     — Altura entrepiso [m]
  io_maximo_user (Number)        — IO normativo (opcional, override)

SALIDAS:
  envelope_curve, ocupacion_real, io_maximo, ic_real, ic_maximo,
  altura_total, pisos_aplicados, mensaje
================================================================================
"""

import Rhino.Geometry as rg
import json
import math

RANGO_PISOS = {"1": 2, "2": 3, "3": 5, "4": 8, "5": 12}
ALTURA_MIN_ENTREPISO = 2.5
ALTURA_MAX_ENTREPISO = 3.8
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
    """Area de una curva plana (Areal)."""
    if crv is None:
        return 0.0
    area_props = rg.AreaMassProperties.Compute(crv)
    return area_props.Area if area_props else 0.0


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

# --- Calcular retiros por clasificacion ---
retiros = {}
for lado in lados:
    idx = lado.get("id", 0)
    cls = lado.get("clasificacion", "Lateral")
    dist_via = lado.get("dist_via_m", 999)
    if cls == "Frontal":
        retiros[idx] = 5.0 if dist_via < 5.0 else 3.0
    elif cls == "Posterior":
        retiros[idx] = 3.0
    else:  # Lateral, EspacioPublico
        retiros[idx] = 0.0

# --- Construir huella: offset del lote por retiro ---
envelope_curve = None
ocupacion_real = 0.0

if lot_polygon is not None:
    try:
        offset_dist = -max(retiros.values()) if retiros else 0.0
        if abs(offset_dist) < 0.01:
            # Sin retiros: huella = lote
            offset_curves = [lot_polygon]
        else:
            offset_curves = lot_polygon.Offset(
                rg.Plane.WorldXY, offset_dist, TOLERANCIA,
                rg.CurveOffsetCornerStyle.Sharp)
        if offset_curves:
            envelope_curve = offset_curves[0]
    except:
        envelope_curve = lot_polygon

# --- Restar patios de la huella ---
patios_list = safe_list(patio_raw)
patio_area_total = 0.0
if envelope_curve is not None and patios_list:
    # Area de huella bruta
    huella_bruta = area_curve(envelope_curve)
    for patio in patios_list:
        if patio is not None:
            patio_area_total += area_curve(patio)
    ocupacion_real = max(0.0, huella_bruta - patio_area_total)
else:
    ocupacion_real = area_curve(envelope_curve) if envelope_curve else 0.0

# --- Indices ---
area_lote = area_curve(lot_polygon) if lot_polygon else 0.0
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

mensaje = "NORMATIVA v01 | Area lote: {:.1f}m2 | Ocupacion: {:.1f}m2 | IO max: {:.2f} | IC real: {:.2f} | Altura: {:.1f}m | Pisos: {} | Patios: {:.1f}m2".format(
    area_lote, ocupacion_real, io_maximo, ic_real, altura_total, pisos_aplicados, patio_area_total)
