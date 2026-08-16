# -*- coding: utf-8 -*-
"""
================================================================================
F1_ETAPA2_NORMATIVA_v06.py - Retiros + Patios + Indices + Piso Adicional
                            + Ancho de via con respaldo desde LADOS
Proyecto: DisenoParametrico / Fase 1
GH Python Script para Grasshopper (IronPython 2.7 compatible)
================================================================================

CALCULO:
  1. Descontar retiro FRONTAL (antejardin) del lado frontal del lote
  2. NO descontar retiro en lados EspacioPublico (0m)
  3. Lateral: 0m en tipologia CONTINUA; en AISLADA, 1/5 de la altura de la
     edificacion, minimo 4,00m (Anexo 5 POT, SECCION 1.9.b) - se exige desde
     el segundo piso; el modelo de huella unica lo aplica en toda la huella
     (aproximacion conservadora documentada)
  4. Posterior: tabla Consolidacion por pisos (Anexo 5 POT, SECCION 5.4.b);
     con empate volumetrico (vecino posterior de 3+ pisos sin aislamiento,
     SECCION 5.4.c) el retiro posterior = 0 en la huella
  5. Restar el patio (desde vertice N) del perimetro restante (Boolean Diff)
  6. Calcular pisos base (Decreto 555/2021) y aplicar PISO ADICIONAL
  7. Calcular GFA (Gross Floor Area) maximo para Fase 2

NOTA NORMATIVA (antejardin / retiro frontal):
  En Consolidacion el antejardin se exige segun el mapa CU-5.5
  "Dimensionamiento de Antejardines" (Resolucion SDP 1631/2023). Cuando el
  mapa no determina la dimension, aplica la norma vigente antes del Decreto
  555/2021 (regla historica: vias < 12m -> 3,00m; 12-20m -> 5,00m; >=20m ->
  7,00m, parametrizable en FRONTAL_POR_ANCHO_VIA). La entrada antejardin_m
  permite fijar el valor oficial del mapa CU-5.5 por sector.
  En esquineros el mapa permite reducir a 2,00m por el lado de mayor
  dimension (usar antejardin_m para casos puntuales).

NOTA NORMATIVA (tipologia aislada):
  La tipologia aislada y su aislamiento lateral dependen de la
  reglamentacion (mapas CU-5.4.2 a CU-5.4.33 - Edificabilidad): lateral =
  1/5 de la altura en metros, minimo 4,00m (3,00m solo en Mejoramiento
  Integral). Se exige desde el segundo piso o el nivel de empate.

NOTA NORMATIVA (empate volumetrico posterior):
  "En predios que colinden posteriormente con predios en los que a la fecha
  de entrada en vigencia del Decreto Distrital 555 de 2021, existan
  edificaciones de tres (3) o mas pisos sin aislamiento posterior, se
  permite prever empate volumetrico con la altura de dichas edificaciones,
  a partir de cuyo nivel se exige aislamiento posterior reglamentario
  aplicado a la altura maxima de la edificacion." (Anexo 5, SECCION 5.4.c)
  Entrada empate_posterior_pisos: pisos del vecino posterior existente.
  Si >= 3: retiro posterior = 0 en la huella (el aislamiento se exige solo
  por encima de la altura del vecino).

ENTRADAS:
  lot_polygon (Curve)            - Lote simplificado
  sides_table_json (String)      - Clasificacion (F1_ETAPA2_LADOS_v03)
  patio_curves (Curve[])         - Patio(s) (F1_ETAPA2_PATIO_v02)
  altura_max_pot (Number)        - [OBSOLETO] Se mantiene para no romper canvas
  tratamiento (String)           - Tratamiento urbanistico
  rango_edificabilidad (String)  - Rango "1".."5" (tolerante a etiquetas)
  floor_height_user (Number)     - Altura entrepiso [m]
  io_maximo_user (Number)        - IO normativo (override)
  piso_adicional (bool)          - True si se acoge al incentivo normativo
  tipo_bonificacion (String)     - "NINGUNO" | "VIS" | "VIP" | "COMUNAL" |
                                   "EQUIPAMIENTO" | "EQUIPAMENTO+COMUNAL"
  tipologia (String)             - "Continua" (default) | "Aislada". Si es nula
                                   o vacia, se deriva de reglamentacion_json.
  ancho_via_m (Number)           - Ancho de via del frente [m] (medido entre
                                   bordes opuestos del perfil vial TOTAL;
                                   entrada del operador). Precedencia v06:
                                   operador > LADOS_v06 (sides_data) >
                                   reglamentacion > 0 (default).
  antejardin_m (Number)          - Override del retiro frontal [m] (valor
                                   oficial del mapa CU-5.5 si se conoce).
                                   Si 0/nulo, se deriva de reglamentacion_json
                                   o de la regla por ancho de via.
  empate_posterior_pisos (Number)- Pisos del vecino posterior existente
                                   (>=3 activa empate volumetrico)
  reglamentacion_json (String)   - JSON de reglamentacion (salida de
                                   F1_ETAPA1_CONTEXTO_v02: pot_data con
                                   tipologia/ancho_via_m/antejardin_m).
                                   Cadena de derivacion: operador >
                                   reglamentacion > default + aviso.

SALIDAS:
  envelope_curve (Curve/List)    - Huella fisica con retiros y patio restado
  gfa_total (Number)             - Area Bruta Construida TOTAL (incl. piso extra)
  ocupacion_real, io_maximo, ic_real, ic_maximo,
  altura_total, pisos_finales, valido (bool), mensaje

VERSIONES:
  VERSIONES:
  v06 (2026-08-16) - Respaldo del ancho de via desde sides_data del
                     LADOS_v06 (operador > LADOS > reglamentacion > 0).
                     Corrige antejardin en 3.0 m por ancho 0 (la entrada
                     ancho_via_m sin cablear ya no deja el antejardin en
                     default). Mensaje con prefijo v06.
  v05 (2026-08-15) - Retiros por clasificacion + tratamiento + tipologia:
                     antejardin por ancho de via (CU-5.5 / regla historica)
                     con override; lateral 0 continua / 1/5 altura min 4m
                     aislada; posterior tabla Consolidacion por pisos con
                     empate volumetrico (SECCION 5.4.c). Entradas nuevas:
                     tipologia, ancho_via_m, antejardin_m,
                     empate_posterior_pisos.
                     Ampliado (2026-08-15): entrada reglamentacion_json
                     (salida de ETAPA1_v02) para derivar tipologia /
                     ancho_via_m / antejardin_m de la reglamentacion cuando
                     las entradas del operador son nulas o 0. La fuente POT
                     actual no provee esos campos (mapas raster CU-5.4.2-33
                     y CU-5.5) -> avisos + defaults reglamentarios.
  v04 (2026-08-15) - Parseo robusto de rango, normalizacion de
                     tipo_bonificacion, ocupacion_real = suma de fragmentos.
  v03 - Fix rangos + toggle piso adicional + resta booleana del patio.
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

# Anexo 5 POT (Decreto 466/2024), SECCION 5.4.b - Consolidacion
# Altura maxima (pisos) -> dimension minima del aislamiento posterior [m]
POSTERIOR_CONSOLIDACION = [
    (3, 3.0), (6, 5.0), (9, 6.0), (12, 8.0), (15, 10.0),
    (18, 12.0), (22, 14.0), (25, 16.0), (28, 18.0), (99, 20.0),
]
# Anexo 5 POT, SECCION 1.9.b - lateral aislada: 1/5 altura, minimo
LATERAL_FRACCION_ALTURA = 0.2
LATERAL_MINIMO_M = 4.0
# Regla historica pre-555 (respaldo cuando el mapa CU-5.5 no senala):
# ancho de via [m] -> antejardin [m]
FRONTAL_POR_ANCHO_VIA = [
    (12.0, 3.0), (20.0, 5.0), (999.0, 7.0),
]
ANTEJARDIN_DEFAULT_M = 3.0
TIPOLOGIA_DEFAULT = "Continua"


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
    """Extrae el digito del rango aceptando etiquetas del Value List."""
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
    """Normaliza tipo_bonificacion a mayusculas sin espacios alrededor de +."""
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


def normalize_tipologia(val, warnings):
    """Normaliza tipologia: 'Continua' (default) | 'Aislada'."""
    if val is None:
        return TIPOLOGIA_DEFAULT
    s = str(unwrap(val)).strip()
    if s == "":
        return TIPOLOGIA_DEFAULT
    s = s.replace("\u00c1", "A").replace("\u00cd", "I")
    s = s.title()
    if s not in ("Continua", "Aislada"):
        warnings.append(
            "tipologia desconocida ('%s') -> %s" % (s, TIPOLOGIA_DEFAULT))
        return TIPOLOGIA_DEFAULT
    return s


def parse_reglamentacion(raw):
    """Parsea la reglamentacion_json (salida de ETAPA1_v02).

    Retorna dict con pot_data o None si no es JSON valido.
    """
    if raw is None:
        return None
    try:
        s = str(raw[0]) if isinstance(raw, list) and raw else str(raw)
        data = json.loads(s)
        if isinstance(data, dict) and "pot_data" in data:
            return data
        return None
    except:
        return None


def dato_reglamentario_num(reg_data, campo, default=0.0):
    """Lee un numero de reglamentacion_json (pot_data)."""
    if reg_data is None:
        return default
    v = reg_data.get("pot_data", {}).get(campo)
    if v is None or v == "":
        return default
    try:
        return float(v)
    except:
        return default


def dato_reglamentario_str(reg_data, campo, default=""):
    """Lee un string de reglamentacion_json (pot_data)."""
    if reg_data is None:
        return default
    v = reg_data.get("pot_data", {}).get(campo)
    if v is None:
        return default
    s = str(v).strip()
    return s or default


def retiro_posterior_consolidacion(pisos):
    """Tabla Consolidacion (Anexo 5 SECCION 5.4.b): pisos -> retiro [m]."""
    for limite, retiro in POSTERIOR_CONSOLIDACION:
        if pisos <= limite:
            return retiro
    return POSTERIOR_CONSOLIDACION[-1][1]


def retiro_frontal_por_ancho_via(ancho_via_m):
    """Regla historica pre-555: ancho de via [m] -> antejardin [m]."""
    if ancho_via_m is None or ancho_via_m <= 0:
        return ANTEJARDIN_DEFAULT_M
    for limite, retiro in FRONTAL_POR_ANCHO_VIA:
        if ancho_via_m < limite:
            return retiro
    return FRONTAL_POR_ANCHO_VIA[-1][1]


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
tipologia_raw = globals().get("tipologia", None)
ancho_via_raw = globals().get("ancho_via_m", None)
antejardin_raw = globals().get("antejardin_m", None)
empate_posterior_raw = globals().get("empate_posterior_pisos", None)
reglamentacion_raw = globals().get("reglamentacion_json", None)

warnings = []
reglamentacion_data = parse_reglamentacion(reglamentacion_raw)

piso_adicional = parse_gh_bool(globals().get("piso_adicional", False))

tipo_bonif_raw = globals().get("tipo_bonificacion", "Ninguno")
tipo_bonificacion = normalize_bonificacion(tipo_bonif_raw, warnings)

rango = normalize_rango(rango_raw, warnings)

# sides_data se parsea ANTES del ancho: en v06 es respaldo de ancho_via_m
# (la salida del LADOS_v06 ya transporta ancho_via_m dentro del JSON)
sides_data = None
if sides_raw is not None:
    try:
        s = str(sides_raw[0]) if isinstance(sides_raw, list) and sides_raw else str(sides_raw)
        sides_data = json.loads(s)
    except:
        sides_data = None

lados = sides_data.get("lados", []) if sides_data else []

# --- Tipologia: operador > reglamentacion > Continua ---
tipologia = normalize_tipologia(tipologia_raw, warnings)
if tipologia == TIPOLOGIA_DEFAULT:
    tipologia_reg = dato_reglamentario_str(reglamentacion_data, "tipologia")
    if tipologia_reg:
        tipologia = normalize_tipologia(tipologia_reg, warnings)
        warnings.append("tipologia desde reglamentacion ('%s')" % tipologia)
    elif tipologia_raw is None or str(unwrap(tipologia_raw)).strip() == "":
        warnings.append(
            "tipologia no definida y sin dato reglamentario -> %s" % TIPOLOGIA_DEFAULT)

# --- Entradas numericas nuevas (v06) ---
try:
    ancho_via_m = float(unwrap(ancho_via_raw)) if ancho_via_raw else 0.0
except:
    ancho_via_m = 0.0

# --- Ancho de via: operador > LADOS_v06 (sides_data) > reglamentacion > 0 ---
if ancho_via_m <= 0:
    ancho_via_m = dato_reglamentario_num(reglamentacion_data, "ancho_via_m", 0.0)
    if ancho_via_m > 0:
        warnings.append("ancho_via_m desde reglamentacion ({:.1f}m)".format(ancho_via_m))
if ancho_via_m <= 0 and sides_data:
    ancho_via_m = float(sides_data.get("ancho_via_m") or 0.0)
    if ancho_via_m > 0:
        warnings.append(
            "ancho_via_m desde LADOS_v06 ({:.1f}m; antejardin por tabla)".format(ancho_via_m))

try:
    antejardin_m = float(unwrap(antejardin_raw)) if antejardin_raw else 0.0
except:
    antejardin_m = 0.0

# --- Antejardin: operador > reglamentacion > regla por ancho de via ---
if antejardin_m <= 0:
    antejardin_m = dato_reglamentario_num(reglamentacion_data, "antejardin_m", 0.0)
    if antejardin_m > 0:
        warnings.append("antejardin_m desde reglamentacion ({:.1f}m)".format(antejardin_m))

try:
    empate_posterior_pisos = float(unwrap(empate_posterior_raw)) if empate_posterior_raw else 0.0
except:
    empate_posterior_pisos = 0.0

try:
    floor_h = float(unwrap(floor_h_raw)) if floor_h_raw else 3.0
except:
    floor_h = 3.0

try:
    io_user = float(unwrap(io_user_raw)) if io_user_raw else 0.0
except:
    io_user = 0.0

tratamiento = str(unwrap(tratamiento_raw)) if tratamiento_raw else "Consolidacion"

# --- PISOS Y ALTURA (antes que retiros: el posterior/lateral dependen de pisos) ---
ic_maximo_base = RANGO_PISOS.get(rango, RANGO_PISOS[RANGO_DEFAULT])

pisos_extra = 0
if piso_adicional:
    pisos_extra = BONIFICACION_PISOS.get(tipo_bonificacion, 0)

ic_maximo = ic_maximo_base + pisos_extra
pisos_finales = ic_maximo
altura_total = pisos_finales * floor_h

# --- RETIROS POR CLASIFICACION (v06) ---
# Antejardin frontal: override del mapa CU-5.5 > regla por ancho de via
if antejardin_m > 0:
    antejardin = antejardin_m
else:
    antejardin = retiro_frontal_por_ancho_via(ancho_via_m)
    if ancho_via_m <= 0:
        warnings.append(
            "sin ancho_via_m -> antejardin default {:.1f}m (ver mapa CU-5.5)".format(antejardin))

# Posterior: empate volumetrico (SECCION 5.4.c) si el vecino tiene 3+ pisos
empate_posterior = empate_posterior_pisos >= 3.0
if empate_posterior:
    retiro_posterior = 0.0
else:
    retiro_posterior = retiro_posterior_consolidacion(pisos_finales)

# Lateral: 0 en continua; 1/5 altura min 4m en aislada (SECCION 1.9.b)
if tipologia == "Aislada":
    retiro_lateral = max(LATERAL_FRACCION_ALTURA * altura_total, LATERAL_MINIMO_M)
else:
    retiro_lateral = 0.0

retiros = {}
for lado in lados:
    idx = lado.get("id", 0)
    cls = lado.get("clasificacion", "Lateral")
    if cls == "Frontal":
        retiros[idx] = antejardin
    elif cls == "Posterior":
        retiros[idx] = retiro_posterior
    elif cls == "EspacioPublico":
        retiros[idx] = 0.0
    else:
        retiros[idx] = retiro_lateral

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

# --- 4. GFA (Gross Floor Area) ---
gfa_total = ocupacion_real * pisos_finales
ic_real = (ocupacion_real / area_lote * ic_maximo) if area_lote > 0 else 0.0

if valido:
    mensaje = "NORMATIVA v06 | OK | Lote: {:.1f}m2 | Ocup: {:.1f}m2 | IO {:.2f} | IC {:.2f} (+{}) | Alt {:.1f}m | {} pisos | GFA: {:.1f}m2 | Patios {:.1f}m2 | Tipo:{} | Antejardin {:.1f}m (via {:.1f}m) | Lat {:.1f}m | Post {:.1f}m{}".format(
        area_lote, ocupacion_real, io_maximo, ic_real, pisos_extra, altura_total,
        pisos_finales, gfa_total, patio_area_total, tipologia, antejardin,
        ancho_via_m, retiro_lateral, retiro_posterior,
        " (empate)" if empate_posterior else "")
else:
    mensaje = "NORMATIVA v06 | ERROR DE VALIDACION | Ocupacion ({:.1f}) >= Area bruta ({:.1f})".format(
        ocupacion_real, area_lote)

if warnings:
    mensaje += " | AVISOS: " + "; ".join(warnings)
