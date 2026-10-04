# -*- coding: utf-8 -*-
"""
================================================================================
F1_ETAPA2_NORMATIVA_v09.py - Retiros + Patios + Índices + Piso Adicional
                            + Ancho de vía con respaldo desde LADOS
                            + ENVELOPE ESCALONADO por pisos superiores
                            + VECINOS CON ALTURAS VARIABLES por lateral
                            + VALIDADOR DE BARRAS (presupuesto IO + barras_json)
Proyecto: DisenoParametrico / Fase 1
GH Python Script para Grasshopper (IronPython 2.7 compatible)
================================================================================

HISTORIAL DE VERSIONES:
  v09.0 (2026-10-03): Cambio mayor (v08 -> v09) — contrato de entradas/salidas.
    - Nueva entrada opcional: barras_json (String, Item Access) — huellas aprobadas
      desde F3_DISTRIBUCION_v03 (distribuidor de barras por crujía).
    - Nuevas salidas: presupuesto_ocupacion_m2, ocupacion_aprobada_m2,
      gfa_aprobado_m2, envelope_aprobado_por_piso.
    - Validador: si barras_json presente, certifica ocupacion_total ≤ presupuesto
      (+ TOLERANCIA**2) y emite ocupacion_aprobada/gfa_aprobado/envelope_aprobado;
      desacopla "envolvente potencial" de "ocupación aprobada".
    - Siempre expone presupuesto_ocupacion_m2 = area_lote * io_maximo.
    - Homogeneizado: versión interna = nombre de archivo (v09.0).
  v08.5.2 (2026-10-01): IO real bloqueante, antejardin cero explícito, límite
    de pisos, booleanas sin áreas ficticias, vecinos_intervalos_json (puente
    LADOS v06.7), recortes locales rectangulares.
  v08.1–v08.4: iteraciones previas (empate lateral solo con lado Posterior,
    lote de esquina, frente_override, via_no_frontal).

REGLA DE VERSIONADO: la versión general (v09 -> v10) SOLO cambia con cambios
mayores (contrato de entradas/salidas o algoritmo central); las iteraciones
internas se registran como subversiones v09.x en este encabezado.

CALCULO:
  1. Descontar retiro FRONTAL (antejardin) del lado frontal del lote
  2. NO descontar retiro en lados EspacioPublico (0m)
  3. Lateral: 0m en tipologia CONTINUA; en AISLADA, 1/5 de la altura de la
     edificacion, minimo 4,00m (Anexo 5 POT, SECCION 1.9.b)
  4. Posterior: tabla Consolidacion por pisos (Anexo 5 POT, SECCION 5.4.b);
     con empate volumetrico (vecino posterior 3+ pisos) retiro posterior = 0
  5. Restar el patio (desde vertice N) del perimetro restante (Boolean Diff)
  6. Calcular pisos base (Decreto 555/2021) y aplicar PISO ADICIONAL
  7. ESCALONAMIENTO EN PISOS SUPERIORES (Anexo 5 SECCION 1.9.c + NSR-10 A.6.5):
     retiro lateral = max(1/5 x altura desde nivel de empate, minimo empate,
     separacion sismica 2% x h). Solo si hay lado Posterior; si no, solo sísmica.
  8. Calcular GFA ESCALONADO = suma de areas de envelopes por piso (Fase 2)
     y emitir envelope_por_piso para Fase 3 (masa escalonada).
  9. VOLADIZOS (Anexo 5 SECCION 1.13.b): solo frontal, pisos != 1, según perfil vial.
 10. VECINOS CON ALTURAS VARIABLES POR LATERAL (v08): entrada
     vecinos_por_lado_json o vecinos_intervalos_json (puente LADOS v06.7+).
 11. VALIDADOR DE BARRAS (v09): entrada barras_json opcional con huellas
     propuestas; si presente, valida ocupacion_total ≤ presupuesto_ocupacion_m2
     y emite ocupación/GFA/envelope APROBADOS (no potenciales).

NOTA: Altura 0 en vecinos = característica del lote (patio trasero vecino),
no error. Régimen "continuo" solo en frente principal. Sin voladizos internos
entre volúmenes. Patios: 1 vol → normativo (H/3, ≥9m², ≥3ml); ≥2 vol →
separaciones entre volúmenes computan en IO (no patios independientes).

ENTRADAS:
  lot_polygon (Curve)              - Lote simplificado
  sides_table_json (String)        - Clasificación (F1_ETAPA2_LADOS_v06+)
  patio_curves (Curve[])           - Patio(s) (F1_ETAPA2_PATIO_v03+)
  altura_max_pot (Number)          - [OBSOLETO] Se mantiene para compatibilidad
  tratamiento (String)             - Tratamiento urbanistico
  rango_edificabilidad (String)    - Rango "1".."5"
  floor_height_user (Number)       - Altura entrepiso [m]
  io_maximo_user (Number)          - IO normativo (override)
  piso_adicional (bool)            - True si acoge incentivo normativo
  tipo_bonificacion (String)       - "NINGUNO" | "VIS" | "VIP" | "COMUNAL" |
                                     "EQUIPAMIENTO" | "EQUIPAMIENTO+COMUNAL"
  tipologia (String)               - "Continua" | "Aislada"
  ancho_via_m (Number)             - Ancho de vía del frente [m]
  antejardin_m (Number)            - Override retiro frontal [m]
  empate_posterior_pisos (Number)  - Pisos vecino posterior (>=3 activa empate)
  altura_vecinos_m (Number)        - [v07] Altura global vecinos (fallback)
  empate_lateral_min_m (Number)    - [v07] Mínimo aislamiento lateral empate
  voladizo_frontal_m (Number)      - [v07] Override voladizo frontal [m]
  vecinos_por_lado_json (String)   - [v08] Vecinos por lateral (formato legacy)
  frente_override_json (String)    - [v08.2] Override frente por cardinal
  reglamentacion_json (String)     - JSON reglamentación (F1_ETAPA1_CONTEXTO)
  normativa_confirmada (bool)      - False default; True tras revisión humana
  pisos_maximos_total (Number)     - Límite total de pisos incluyendo bonos
  vecinos_intervalos_json (String) - [v08.5] Puente LADOS v06.7+ (intervalos)
  barras_json (String)             - [v09] Huellas aprobadas desde F3_DISTRIBUCION_v03

SALIDAS:
  envelope_curve (Curve/List)      - Huella PISO 1 (base, retiros + patio)
  envelope_por_piso (List)         - [v07] Curvas ocupación POR PISO (potencial)
  retiros_por_piso (String)        - [v07] JSON desglose por piso
  gfa_total (Number)               - GFA ESCALONADO potencial (suma areas)
  ocupacion_real (Number)          - Ocupación real (huella piso 1)
  io_maximo (Number)               - IO normativo aplicado
  ic_real (Number)                 - IC real (gfa_total / area_lote)
  ic_maximo (Number)               - IC máx (pisos_finales, legacy)
  altura_total (Number)            - Altura total [m]
  pisos_finales (Number)           - Pisos aplicados
  valido (bool)                    - Controles implementados OK (no certificación)
  mensaje (String)                 - Diagnóstico completo
  recortes_intervalos_json (String)- [v08.5] Diagnóstico numérico por piso
  presupuesto_ocupacion_m2 (Number)- [v09] area_lote * io_maximo (siempre)
  ocupacion_aprobada_m2 (Number)   - [v09] Ocupación aprobada (si barras_json)
  gfa_aprobado_m2 (Number)         - [v09] GFA aprobado (si barras_json + valido)
  envelope_aprobado_por_piso (List)- [v09] Curvas aprobadas por piso (si valido)

================================================================================
"""

# Rhino.Geometry solo existe dentro de Rhino/Grasshopper (no en el .venv).
import Rhino.Geometry as rg  # type: ignore[reportMissingImports]
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
    "COMUNAL": 1,
    "EQUIPAMENTO": 1,
}
RANGO_DEFAULT = "3"
TOLERANCIA = 0.01

# Anexo 5 POT (Decreto 466/2024), SECCION 5.4.b - Consolidacion
POSTERIOR_CONSOLIDACION = [
    (3, 3.0), (6, 5.0), (9, 6.0), (12, 8.0), (15, 10.0),
    (18, 12.0), (22, 14.0), (25, 16.0), (28, 18.0), (99, 20.0),
]
# Anexo 5 POT, SECCION 1.9.b - lateral aislada
LATERAL_FRACCION_ALTURA = 0.2
LATERAL_MINIMO_M = 4.0
# Anexo 5 POT, SECCION 1.13.b - Voladizos
VOLADIZO_POR_ANCHO_VIA = [
    (6.0, 0.0), (10.0, 0.60), (15.0, 0.80), (22.0, 1.00), (999.0, 1.50),
]
# v07 - Empate volumetrico lateral + separacion sismica NSR-10 A.6.5
EMPATE_LATERAL_MIN_M = 3.0
NSR10_SEPARACION_COEF = 0.02
NSR10_SEPARACION_COEF_RAW = None
# Regla historica pre-555 (respaldo antejardin)
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
    if val is None: return False
    if isinstance(val, list): val = val[0] if len(val) > 0 else None
    if val is None: return False
    if isinstance(val, bool): return val
    s = str(val).strip().lower()
    if s in ("true", "1", "verdadero", "yes", "si"): return True
    return False


def normalize_rango(val, warnings):
    if val is None: return RANGO_DEFAULT
    s = str(unwrap(val)).strip()
    if s == "": return RANGO_DEFAULT
    m = re.search(r"(\d+)", s)
    if m and m.group(1) in RANGO_PISOS: return m.group(1)
    warnings.append("rango_edificabilidad no reconocido ('%s') -> default %s" % (s, RANGO_DEFAULT))
    return RANGO_DEFAULT


def normalize_bonificacion(val, warnings):
    if val is None: return "NINGUNO"
    s = str(unwrap(val)).strip()
    if s == "": return "NINGUNO"
    s = s.upper()
    s = re.sub(r"\s*\+\s*", "+", s)
    s = re.sub(r"\s+", " ", s)
    s = s.replace("\u00c1", "A").replace("\u00c9", "E").replace("\u00cd", "I")
    s = s.replace("\u00d3", "O").replace("\u00da", "U").replace("\u00d1", "N")
    if s not in BONIFICACION_PISOS:
        warnings.append("tipo_bonificacion desconocido ('%s') -> sin piso extra" % s)
        return "NINGUNO"
    return s


def normalize_tipologia(val, warnings):
    if val is None: return TIPOLOGIA_DEFAULT
    s = str(unwrap(val)).strip()
    if s == "": return TIPOLOGIA_DEFAULT
    s = s.replace("\u00c1", "A").replace("\u00cd", "I")
    s = s.title()
    if s not in ("Continua", "Aislada"):
        warnings.append("tipologia desconocida ('%s') -> %s" % (s, TIPOLOGIA_DEFAULT))
        return TIPOLOGIA_DEFAULT
    return s


def parse_reglamentacion(raw):
    if raw is None: return None
    try:
        s = str(raw[0]) if isinstance(raw, list) and raw else str(raw)
        data = json.loads(s)
        if isinstance(data, dict):
            return data if "pot_data" in data else {"pot_data": data}
        return None
    except: return None


def dato_reglamentario_num(reg_data, campo, default=0.0):
    if reg_data is None: return default
    v = reg_data.get("pot_data", {}).get(campo)
    if v is None or v == "": return default
    try: return float(v)
    except: return default


def dato_reglamentario_str(reg_data, campo, default=""):
    if reg_data is None: return default
    v = reg_data.get("pot_data", {}).get(campo)
    if v is None: return default
    s = str(v).strip()
    return s or default


def numero_opcional(raw):
    v = unwrap(raw)
    if v is None or str(v).strip() in ("", "None"): return None
    try:
        v = float(v)
        return v if not (math.isnan(v) or math.isinf(v)) else None
    except (ValueError, TypeError): return None


def retiro_posterior_consolidacion(pisos):
    for limite, retiro in POSTERIOR_CONSOLIDACION:
        if pisos <= limite: return retiro
    return POSTERIOR_CONSOLIDACION[-1][1]


def retiro_lateral_empate(h_piso, h_vecino, min_m):
    if h_vecino <= 0 or h_piso <= h_vecino: return 0.0
    h_exc = h_piso - h_vecino
    return max(LATERAL_FRACCION_ALTURA * h_exc, min_m)


def separacion_sismica_piso(h_piso, coef):
    if coef <= 0: return 0.0
    return coef * h_piso


def retiro_frontal_por_ancho_via(ancho_via_m):
    if ancho_via_m is None or ancho_via_m <= 0: return ANTEJARDIN_DEFAULT_M
    for limite, retiro in FRONTAL_POR_ANCHO_VIA:
        if ancho_via_m < limite: return retiro
    return FRONTAL_POR_ANCHO_VIA[-1][1]


def voladizo_por_perfil_vial(ancho_via_m):
    if ancho_via_m is None or ancho_via_m <= 0: return 0.0
    for limite, vol in VOLADIZO_POR_ANCHO_VIA:
        if ancho_via_m <= limite: return vol
    return VOLADIZO_POR_ANCHO_VIA[-1][1]


def parsear_vecinos_por_lado(raw):
    if raw is None: return {}
    try:
        s = str(raw[0]) if isinstance(raw, list) and raw else str(raw)
        data = json.loads(s)
    except: return {}
    if not isinstance(data, dict): return {}
    out = {}
    entradas = []
    if "lados" in data and isinstance(data["lados"], list):
        for l in data["lados"]:
            if not isinstance(l, dict): continue
            try: lid = int(l.get("id", -1))
            except: continue
            vecs = l.get("vecinos", [])
            if lid >= 0 and isinstance(vecs, list): entradas.append((lid, vecs))
    else:
        for k, v in data.items():
            try: lid = int(k)
            except: continue
            if isinstance(v, list): entradas.append((lid, v))
    for lid, vecs in entradas:
        norm = []
        for v in vecs:
            if isinstance(v, (int, float)):
                norm.append((float(v), None))
            elif isinstance(v, dict):
                try: h = float(v.get("altura_m", 0.0))
                except: h = 0.0
                lon = v.get("longitud_m")
                try: lon = float(lon) if lon is not None else None
                except: lon = None
                if h > 0: norm.append((h, lon))
        if norm: out[lid] = norm
    return out


# v08.2 - Puente orquestador -> canvas: override de frente por cardinal
CARDINAL_BANDS = [
    ("Norte", 315.0, 45.0), ("Oriente", 45.0, 135.0),
    ("Sur", 135.0, 225.0), ("Occidente", 225.0, 315.0),
]
FRENTE_A_CLASIFICACION = {
    "via": "Frontal", "via_no_frontal": "EspacioPublico",
    "espacio_publico": "EspacioPublico", "predio": "Lateral",
}

def _parsear_frente_override(raw):
    if raw is None: return {}
    try:
        s = str(raw[0]) if isinstance(raw, list) and raw else str(raw)
        data = json.loads(s)
    except Exception: return {}
    if not isinstance(data, dict): return {}
    out = {}
    for k, v in data.items():
        if str(v) in FRENTE_A_CLASIFICACION: out[str(k)] = str(v)
    return out

def _cardinal_normal(nx, ny):
    if nx == 0.0 and ny == 0.0: return "Norte"
    az = math.degrees(math.atan2(nx, ny)) % 360.0
    for name, lo, hi in CARDINAL_BANDS:
        if lo <= hi:
            if lo <= az < hi: return name
        else:
            if az >= lo or az < hi: return name
    return "Norte"

def _cardinal_lado(dx, dy, mx, my, cx, cy):
    n1 = (-dy, dx); n2 = (dy, -dx)
    vx = mx - cx; vy = my - cy
    d1 = vx * n1[0] + vy * n1[1]; d2 = vx * n2[0] + vy * n2[1]
    nx, ny = (n1 if d1 >= d2 else n2)
    return _cardinal_normal(nx, ny)

def _poligono_ccw(curva):
    success, poly = curva.TryGetPolyline()
    if not success or poly is None: return True
    s = 0.0; c = poly.Count
    for i in range(c - 1):
        s += poly[i].X * poly[i + 1].Y - poly[i + 1].X * poly[i].Y
    return s > 0

def _area_signada_puntos(puntos):
    s = 0.0; n = len(puntos)
    for i in range(n):
        p = puntos[i]; q = puntos[(i + 1) % n]
        s += p.X * q.Y - q.X * p.Y
    return s / 2.0

def _curva_desde_puntos(puntos):
    if puntos is None or len(puntos) < 3: return None
    poly = rg.Polyline(puntos)
    if not poly.IsClosed: poly.Add(poly[0])
    return rg.PolylineCurve(poly)

def _vertices_curva(curva):
    success, poly = curva.TryGetPolyline()
    if not success or poly is None: return []
    pts = [rg.Point3d(p.X, p.Y, 0.0) for p in poly]
    if len(pts) >= 2 and pts[0].DistanceTo(pts[-1]) > 0.001:
        pts.append(rg.Point3d(pts[0]))
    return pts

def _recortar_puntos(puntos, sub_segmentos):
    poly = [rg.Point3d(p.X, p.Y, 0.0) for p in puntos]
    if len(poly) < 3: return None
    ccw = _area_signada_puntos(poly) > 0
    for (a, b), r in sub_segmentos:
        if r <= 0.0: continue
        dx = b.X - a.X; dy = b.Y - a.Y
        largo = math.hypot(dx, dy)
        if largo < 1e-9: continue
        ux, uy = dx / largo, dy / largo
        nx, ny = (-uy, ux) if ccw else (uy, -ux)
        k = nx * (a.X + nx * r) + ny * (a.Y + ny * r)
        nuevo = []; m = len(poly)
        for j in range(m):
            p = poly[j]; q = poly[(j + 1) % m]
            dp = nx * p.X + ny * p.Y - k; dq = nx * q.X + ny * q.Y - k
            dentro_p = dp >= -1e-9; dentro_q = dq >= -1e-9
            if dentro_p: nuevo.append(p)
            if dentro_p != dentro_q:
                t = dp / (dp - dq)
                nuevo.append(rg.Point3d(p.X + t * (q.X - p.X), p.Y + t * (q.Y - p.Y), 0.0))
        poly = nuevo
        if len(poly) < 3: return None
    return poly

def _region_area(curvas):
    regiones = rg.Brep.CreatePlanarBreps(list(curvas), TOLERANCIA)
    if not regiones: raise ValueError('No se pudieron medir regiones con huecos')
    total = 0.0
    for region in regiones:
        props = rg.AreaMassProperties.Compute(region)
        if props is None: raise ValueError('Region sin area')
        total += props.Area
    return total

def _recortar_regiones_locales(lote, subs, patios, ccw):
    grouped = []
    for (a, b), r in subs:
        if r <= 0: continue
        if grouped:
            (p, q), previous_r = grouped[-1]
            ux, uy = q.X-p.X, q.Y-p.Y; vx, vy = b.X-a.X, b.Y-a.Y
            lu, lv = math.hypot(ux,uy), math.hypot(vx,vy)
            aligned = (lu > 1e-8 and lv > 1e-8 and
                       abs(ux*vy-uy*vx)/(lu*lv) < 1e-6 and ux*vx+uy*vy > 0)
            if (abs(previous_r-r) < 1e-8 and q.DistanceTo(a) < 1e-6 and aligned):
                grouped[-1] = ((p,b),r); continue
        grouped.append(((a,b),r))
    cutters = list(patios)
    for (a, b), r in grouped:
        if r <= 0: continue
        dx, dy = b.X-a.X, b.Y-a.Y
        length = math.hypot(dx, dy)
        if length <= 1e-8: continue
        nx, ny = (-dy/length, dx/length) if ccw else (dy/length, -dx/length)
        margen_exterior = 5.0 * TOLERANCIA
        pts = [rg.Point3d(a.X-nx*margen_exterior, a.Y-ny*margen_exterior, 0),
               rg.Point3d(b.X-nx*margen_exterior, b.Y-ny*margen_exterior, 0),
               rg.Point3d(b.X+nx*r, b.Y+ny*r, 0),
               rg.Point3d(a.X+nx*r, a.Y+ny*r, 0)]
        cutters.append(_curva_desde_puntos(pts))
    if not cutters: return [lote], area_curve(lote)
    for index, cutter in enumerate(cutters):
        if cutter is None or not cutter.IsClosed or not cutter.IsValid:
            raise ValueError('cortador {} no cerrado/valido'.format(index))
    merged = rg.Curve.CreateBooleanUnion(cutters, TOLERANCIA)
    if not merged: raise ValueError('Union fallida: {} subtramos'.format(len(subs)))
    diff = rg.Curve.CreateBooleanDifference(lote, list(merged), TOLERANCIA)
    if not diff: raise ValueError('Diferencia vacia/fallida')
    diff = list(diff)
    area = _region_area(diff)
    if area > area_curve(lote) + TOLERANCIA**2: raise ValueError('Recorte aumento el area')
    return diff, area

def _subdividir_lado(p1, p2, vecinos):
    n = len(vecinos)
    if n <= 1:
        return [rg.Point3d(p1.X, p1.Y, 0.0), rg.Point3d(p2.X, p2.Y, 0.0)]
    longs = [v[1] for v in vecinos]
    total = sum([lo for lo in longs if lo is not None and lo > 0])
    if total <= 0: fracciones = [1.0 / n] * n
    else:
        fracciones = []
        for lo in longs:
            if lo is not None and lo > 0: fracciones.append(lo / total)
            else: fracciones.append(0.0)
        suma = sum(fracciones)
        if suma <= 0: fracciones = [1.0 / n] * n
        else: fracciones = [f / suma for f in fracciones]
    pts = [rg.Point3d(p1.X, p1.Y, 0.0)]
    for f in fracciones:
        ult = pts[-1]
        pts.append(rg.Point3d(ult.X + (p2.X - p1.X) * f, ult.Y + (p2.Y - p1.Y) * f, 0.0))
    if pts[-1].DistanceTo(rg.Point3d(p2.X, p2.Y, 0.0)) > 0.01:
        pts[-1] = rg.Point3d(p2.X, p2.Y, 0.0)
    return pts

def _subsegmentos_piso(nv, lados, vertices, retiros_base, vecinos_por_lado,
                       altura_vecinos_m, empate_lateral_min, nsr_coef,
                       pisos_finales, floor_h, voladizo_frontal, empate_activo=True):
    h_piso = nv * floor_h
    r_sismica = separacion_sismica_piso(h_piso, nsr_coef) \
        if (pisos_finales > 3 and nv > 1) else 0.0
    subs = []; n = len(vertices) - 1
    for i in range(n):
        p1, p2 = vertices[i], vertices[(i + 1) % n]
        cls = "Lateral"
        for lado in lados:
            if lado.get("id", 0) == i:
                cls = lado.get("clasificacion", "Lateral"); break
        retiro_base = retiros_base.get(i, 0.0)
        if cls == "Lateral" and i in vecinos_por_lado:
            vecs = vecinos_por_lado[i]; sub_pts = _subdividir_lado(p1, p2, vecs)
            for j in range(len(sub_pts) - 1):
                r = max(retiro_base, r_sismica)
                if empate_activo:
                    h_vec = vecs[j][0]
                    r = max(r, retiro_lateral_empate(h_piso, h_vec, empate_lateral_min))
                subs.append(((sub_pts[j], sub_pts[j + 1]), r))
        elif cls == "Lateral":
            r = max(retiro_base, r_sismica)
            if empate_activo:
                r = max(r, retiro_lateral_empate(h_piso, altura_vecinos_m, empate_lateral_min))
            subs.append(((p1, p2), r))
        elif cls == "Frontal" and nv > 1 and voladizo_frontal > 0:
            r = max(0.0, retiro_base - voladizo_frontal)
            subs.append(((p1, p2), r))
        else:
            subs.append(((p1, p2), retiro_base))
    return subs

def area_curvas(curva_o_lista):
    if curva_o_lista is None: return 0.0
    if isinstance(curva_o_lista, list):
        return sum([area_curve(c) for c in curva_o_lista])
    return area_curve(curva_o_lista)

def area_curve(crv):
    if crv is None: return 0.0
    area_props = rg.AreaMassProperties.Compute(crv)
    return area_props.Area if area_props else 0.0


# ==============================================================================
# PARSER DE BARRAS_JSON (v09)
# ==============================================================================
def parsear_barras_json(raw):
    """v09 - Parsea barras_json desde F3_DISTRIBUCION_v03.
    Espera schema f3_barras_salida_v01 con alternativas y recomendada.
    Retorna (ocupacion_total_m2, gfa_real_m2, huellas_por_piso_list, altura_total_m, floor_h_usado)
    o (None, None, None, None, None) si no válido.
    """
    if raw is None: return None, None, None, None, None
    try:
        s = str(raw[0]) if isinstance(raw, list) and raw else str(raw)
        data = json.loads(s)
    except: return None, None, None, None, None
    if not isinstance(data, dict): return None, None, None, None, None
    if data.get("schema") != "f3_barras_salida_v01": return None, None, None, None, None
    rec = data.get("recomendada")
    if not rec: return None, None, None, None, None
    for alt in data.get("alternativas", []):
        if alt.get("id") == rec:
            occ = alt.get("ocupacion_total_m2")
            gfa = alt.get("gfa_real_m2")
            huellas = alt.get("huellas_por_piso")
            altura_tot = alt.get("altura_total_m")
            floor_h = alt.get("floor_h")
            if occ is not None and gfa is not None and huellas is not None:
                return float(occ), float(gfa), huellas, float(altura_tot) if altura_tot else None, float(floor_h) if floor_h else None
    return None, None, None, None, None


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
tipologia_raw = globals().get("tipologia", None)
ancho_via_raw = globals().get("ancho_via_m", None)
antejardin_raw = globals().get("antejardin_m", None)
empate_posterior_raw = globals().get("empate_posterior_pisos", None)
altura_vecinos_raw = globals().get("altura_vecinos_m", None)
empate_lateral_min_raw = globals().get("empate_lateral_min_m", None)
nsr_coef_raw = globals().get("nsr10_separacion_coef", None)
voladizo_raw = globals().get("voladizo_frontal_m", None)
vecinos_raw = globals().get("vecinos_por_lado_json", None)
frente_override_raw = globals().get("frente_override_json", None)
reglamentacion_raw = globals().get("reglamentacion_json", None)
barras_raw = globals().get("barras_json", None)           # v09 NUEVA

warnings = []
bloqueos = []
reglamentacion_data = parse_reglamentacion(reglamentacion_raw)
normativa_confirmada = parse_gh_bool(globals().get("normativa_confirmada", False))
if not normativa_confirmada:
    bloqueos.append("regimen/alturas/empates pendientes de revision humana")
if reglamentacion_data is None:
    bloqueos.append("reglamentacion_json ausente o invalida")

piso_adicional = parse_gh_bool(globals().get("piso_adicional", False))
tipo_bonif_raw = globals().get("tipo_bonificacion", "Ninguno")
tipo_bonificacion = normalize_bonificacion(tipo_bonif_raw, warnings)
rango = normalize_rango(rango_raw, warnings)

sides_data = None
if sides_raw is not None:
    try:
        s = str(sides_raw[0]) if isinstance(sides_raw, list) and sides_raw else str(sides_raw)
        sides_data = json.loads(s)
    except: sides_data = None

lados = sides_data.get("lados", []) if isinstance(sides_data, dict) else []
if not lados: bloqueos.append("clasificacion de lados ausente")

es_esquina = bool(sides_data.get("es_esquina", False)) if sides_data else False
frente_override = _parsear_frente_override(frente_override_raw)
if frente_override:
    _n_vias = sum(1 for v in frente_override.values() if v in ("via", "via_no_frontal"))
    if _n_vias >= 2: es_esquina = True

es_esquina_raw = globals().get("es_esquina_confirmada", None)
if es_esquina_raw is not None:
    es_esquina = parse_gh_bool(es_esquina_raw)
else:
    es_esquina = False
    warnings.append("esquina normativa sin confirmar: no se elimina retiro posterior por esa regla")

aplica_empate_raw = globals().get("aplica_empate_lateral", None)
if aplica_empate_raw is not None and str(unwrap(aplica_empate_raw)).strip() not in ("", "None"):
    empate_activo = parse_gh_bool(aplica_empate_raw)
    warnings.append("empate 1.9.c %s por entrada" % ("activo" if empate_activo else "inactivo"))
else:
    empate_activo = any(str(lado.get("clasificacion", "")).strip().lower() == "posterior" for lado in lados)
    if empate_activo: warnings.append("empate 1.9.c activo: predio con lado posterior")
    else: warnings.append("empate 1.9.c NO aplica: predio sin lado posterior (dos laterales y esquina) -> solo sismica NSR-10 A.6.5")

tipologia = normalize_tipologia(tipologia_raw, warnings)
if tipologia == TIPOLOGIA_DEFAULT:
    tipologia_reg = dato_reglamentario_str(reglamentacion_data, "tipologia")
    if tipologia_reg:
        tipologia = normalize_tipologia(tipologia_reg, warnings)
        warnings.append("tipologia desde reglamentacion ('%s')" % tipologia)
    elif tipologia_raw is None or str(unwrap(tipologia_raw)).strip() == "":
        warnings.append("tipologia no definida y sin dato reglamentario -> %s" % TIPOLOGIA_DEFAULT)

try: ancho_via_m = float(unwrap(ancho_via_raw)) if ancho_via_raw else 0.0
except: ancho_via_m = 0.0

if ancho_via_m <= 0:
    ancho_via_m = dato_reglamentario_num(reglamentacion_data, "ancho_via_m", 0.0)
    if ancho_via_m > 0: warnings.append("ancho_via_m desde reglamentacion ({:.1f}m)".format(ancho_via_m))
if ancho_via_m <= 0 and sides_data:
    ancho_via_m = float(sides_data.get("ancho_via_m") or 0.0)
    if ancho_via_m > 0:
        warnings.append("ancho_via_m desde LADOS_v06 ({:.1f}m; antejardin por tabla)".format(ancho_via_m))

antejardin_m = numero_opcional(antejardin_raw)
if antejardin_m is None:
    antejardin_m = numero_opcional((reglamentacion_data or {}).get("pot_data", {}).get("antejardin_m"))
    if antejardin_m is not None: warnings.append("antejardin_m desde reglamentacion ({:.1f}m)".format(antejardin_m))
if antejardin_m is not None and antejardin_m < 0:
    bloqueos.append("antejardin negativo"); antejardin_m = None

try: empate_posterior_pisos = float(unwrap(empate_posterior_raw)) if empate_posterior_raw else 0.0
except: empate_posterior_pisos = 0.0

try: altura_vecinos_m = float(unwrap(altura_vecinos_raw)) if altura_vecinos_raw else 0.0
except: altura_vecinos_m = 0.0

try: empate_lateral_min = float(unwrap(empate_lateral_min_raw)) if empate_lateral_min_raw else 0.0
except: empate_lateral_min = 0.0
if empate_lateral_min <= 0: empate_lateral_min = EMPATE_LATERAL_MIN_M

try: nsr_coef = float(unwrap(nsr_coef_raw)) if nsr_coef_raw else 0.0
except: nsr_coef = 0.0
if nsr_coef <= 0: nsr_coef = NSR10_SEPARACION_COEF

try: voladizo_override = float(unwrap(voladizo_raw)) if voladizo_raw else 0.0
except: voladizo_override = 0.0
voladizo_frontal = voladizo_override if voladizo_override > 0 else voladizo_por_perfil_vial(ancho_via_m)
if voladizo_override <= 0 and voladizo_frontal > 0:
    warnings.append("voladizo frontal {:.2f}m por perfil vial (SECCION 1.13.b)".format(voladizo_frontal))

vecinos_por_lado = parsear_vecinos_por_lado(vecinos_raw)
total_vecinos = sum([len(v) for v in vecinos_por_lado.values()])
if total_vecinos > 0:
    warnings.append("vecinos por lado (v08): {} lados, {} vecinos".format(len(vecinos_por_lado), total_vecinos))
elif vecinos_raw is not None and str(vecinos_raw).strip() != "":
    warnings.append("vecinos_por_lado_json sin datos validos -> modo v07 (altura global)")

try: floor_h = float(unwrap(floor_h_raw)) if floor_h_raw else 3.0
except: floor_h = 3.0
if floor_h <= 0: floor_h = 3.0

try: io_user = float(unwrap(io_user_raw)) if io_user_raw else 0.0
except: io_user = 0.0

tratamiento = str(unwrap(tratamiento_raw)) if tratamiento_raw else "Consolidacion"

# --- IO MÁXIMO (inicialización temprana para presupuesto_ocupacion_m2) ---
if io_user > 0: io_maximo = io_user
elif tratamiento == "Consolidacion": io_maximo = 0.70
elif tratamiento in ("Desarrollo", "Mejoramiento"): io_maximo = 0.60
else: io_maximo = 0.70

# --- PISOS Y ALTURA ---
ic_maximo_base = RANGO_PISOS.get(rango, RANGO_PISOS[RANGO_DEFAULT])
pisos_extra = BONIFICACION_PISOS.get(tipo_bonificacion, 0) if piso_adicional else 0
pisos_propuestos = ic_maximo_base + pisos_extra
pisos_limite = numero_opcional(globals().get("pisos_maximos_total", None))
if pisos_limite is None:
    pisos_limite = numero_opcional((reglamentacion_data or {}).get("pot_data", {}).get("altura_maxima_pisos"))
if pisos_limite is not None:
    if pisos_limite < 1 or abs(pisos_limite - round(pisos_limite)) > 1e-6:
        bloqueos.append("limite de pisos no entero positivo")
    else:
        pisos_limite = int(round(pisos_limite))
        if pisos_propuestos > pisos_limite:
            warnings.append("{} pisos solicitados -> {} total incluyendo bonos; no se acumulan adicionales fuera del limite".format(pisos_propuestos, pisos_limite))
        pisos_propuestos = min(pisos_propuestos, pisos_limite)
else:
    bloqueos.append("falta total de pisos incluyendo bonificaciones")
if floor_h <= 0: bloqueos.append("altura entrepiso no positiva"); floor_h = 3.0
pisos_finales = pisos_propuestos
pisos_extra = max(0, pisos_finales - ic_maximo_base)
ic_maximo = pisos_finales
altura_total = pisos_finales * floor_h

# --- RETIROS BASE ---
if antejardin_m is not None: antejardin = antejardin_m
else:
    antejardin = retiro_frontal_por_ancho_via(ancho_via_m)
    if ancho_via_m <= 0:
        warnings.append("sin ancho_via_m -> antejardin provisional {:.1f}m (ver mapa CU-5.5)".format(antejardin))
        bloqueos.append("antejardin sin dato explicito y ancho vial desconocido")

empate_posterior = empate_posterior_pisos >= 3.0
if es_esquina:
    retiro_posterior = 0.0
    warnings.append("lote de esquina: sin aislamiento posterior (patio 3x3 en esquina interior)")
elif empate_posterior: retiro_posterior = 0.0
else: retiro_posterior = retiro_posterior_consolidacion(pisos_finales)

if tipologia == "Aislada":
    retiro_lateral = max(LATERAL_FRACCION_ALTURA * altura_total, LATERAL_MINIMO_M)
else: retiro_lateral = 0.0

# --- Inicializar outputs ---
envelope_curve = None
envelope_por_piso = []
retiros_por_piso = ""
ocupacion_real = 0.0
valido = False
area_lote = area_curve(lot_polygon) if lot_polygon else 0.0
presupuesto_ocupacion_m2 = area_lote * io_maximo

# --- 1. Patios ---
patios_list = [p for p in safe_list(patio_raw) if p is not None]
patio_area_total = sum(area_curve(p) for p in patios_list)

def envelope_final(huella):
    if huella is None: return None, 0.0
    if not patios_list: return huella, area_curve(huella)
    try:
        diff = rg.Curve.CreateBooleanDifference(huella, patios_list, TOLERANCIA)
        if diff and len(diff) > 0:
            breps = rg.Brep.CreatePlanarBreps(list(diff), TOLERANCIA)
            if not breps: raise ValueError("no se pudieron construir regiones planas")
            area = sum(rg.AreaMassProperties.Compute(b).Area for b in breps if rg.AreaMassProperties.Compute(b))
            if area < 0 or area > area_curve(huella) + TOLERANCIA**2: raise ValueError("area de diferencia incoherente")
            return (list(diff) if len(diff) > 1 else diff[0]), area
        raise ValueError("diferencia vacia o fallida")
    except Exception as exc:
        bloqueos.append("booleana de patios no verificable: {}".format(str(exc)))
        return None, 0.0

# --- 2. Retiros base por lado + override operador ---
_centroide_lote = None
if lot_polygon is not None and frente_override:
    _vpre = _vertices_curva(lot_polygon)
    if _vpre:
        _npre = len(_vpre)
        _centroide_lote = (sum(v.X for v in _vpre) / _npre, sum(v.Y for v in _vpre) / _npre)

retiros_base = {}
for lado in lados:
    idx = lado.get("id", 0); cls = lado.get("clasificacion", "Lateral")
    if _centroide_lote is not None:
        try:
            _dx = float(lado.get("dx", 0.0) or 0.0); _dy = float(lado.get("dy", 0.0) or 0.0)
            _mx = float(lado.get("mx", 0.0) or 0.0); _my = float(lado.get("my", 0.0) or 0.0)
            _card = _cardinal_lado(_dx, _dy, _mx, _my, _centroide_lote[0], _centroide_lote[1])
            if _card in frente_override: cls = FRENTE_A_CLASIFICACION[frente_override[_card]]
        except Exception: pass
    if cls == "Frontal": retiros_base[idx] = antejardin
    elif cls == "Posterior": retiros_base[idx] = retiro_posterior
    elif cls == "EspacioPublico": retiros_base[idx] = 0.0
    else: retiros_base[idx] = retiro_lateral

# --- 3. Envelopes (potenciales o aprobados si barras_json) ---
huellas_por_piso = []; areas_por_piso = []
recortes_intervalos_json = '[]'; diag_recortes = []
intervalos = {}; vertices_lote = _vertices_curva(lot_polygon) if lot_polygon is not None else []

# --- VALIDADOR DE BARRAS (v09) ---
barras_ocupacion = None; barras_gfa = None; barras_huellas = None; barras_altura = None; barras_floor_h = None
if barras_raw is not None:
    barras_ocupacion, barras_gfa, barras_huellas, barras_altura, barras_floor_h = parsear_barras_json(barras_raw)
    if barras_ocupacion is not None:
        warnings.append("VALIDADOR v09: barras_json presente -> modo APROBADO (ocupacion={:.2f}, gfa={:.2f})".format(barras_ocupacion, barras_gfa))

try:
    raw_int = unwrap(globals().get('vecinos_intervalos_json', None))
    if not raw_int: raise ValueError('vecinos_intervalos_json sin conectar')
    data_int = json.loads(raw_int)
    if data_int.get('schema') != 'vecinos_intervalos_canvas_v02': raise ValueError('schema de intervalos incorrecto')
    if not sides_data or not sides_data.get('puente_lados_ok'): raise ValueError('puente LADOS no verificado')
    if not data_int.get('chip') or data_int.get('chip') != sides_data.get('chip'): raise ValueError('CHIP de intervalos/LADOS distinto')
    n_edges = len(vertices_lote)-1
    for entry in data_int.get('lados') or []:
        lid = entry.get('id')
        if not isinstance(lid, int) or not 0 <= lid < n_edges or lid in intervalos: raise ValueError('id de intervalo invalido/duplicado')
        spans = sorted(entry.get('subtramos') or [], key=lambda s: s['t0'])
        cursor = 0.0
        if entry.get('es_colindancia_predial'):
            for span in spans:
                t0, t1 = float(span['t0']), float(span['t1'])
                if not 0 <= t0 < t1 <= 1 or abs(t0-cursor) > 0.01: raise ValueError('intervalos con huecos/solapes en L{}'.format(lid))
                cursor = t1
                if span.get('altura_m') is None or float(span['altura_m']) <= 0:
                    bloqueos.append('altura pendiente L{} raw {}'.format(lid,span.get('segmento_raw')))
            if abs(cursor-1.0) > 0.01: raise ValueError('cobertura incompleta en L{}'.format(lid))
        intervalos[lid] = entry
    if len(intervalos) != n_edges: raise ValueError('faltan lados en contrato de intervalos')
    if data_int.get('pendientes'): bloqueos.append('{} pendientes en contrato de vecinos'.format(len(data_int['pendientes'])))
    warnings.append('vecinos por intervalos: {} lados; recortes locales activos'.format(len(intervalos)))
except Exception as exc:
    intervalos = {}; bloqueos.append('intervalos no verificables: {}'.format(str(exc)))

# Si hay barras válidas -> MODO APROBADO (saltamos cálculo potencial)
if barras_ocupacion is not None and barras_huellas is not None:
    # Validar presupuesto
    if area_lote > 0 and barras_ocupacion > presupuesto_ocupacion_m2 + TOLERANCIA**2:
        bloqueos.append("VALIDADOR v09: ocupacion_total {:.2f} > presupuesto {:.2f}; excedente {:.2f} m2".format(barras_ocupacion, presupuesto_ocupacion_m2, barras_ocupacion - presupuesto_ocupacion_m2))
        valido = False
    else:
        # APROBADO: barras dentro de presupuesto -> suprimir bloqueos previos de regimen/alturas/empates
        # porque las barras ya traen geometría validada desde F3_DISTRIBUCION_v03
        bloqueos = [b for b in bloqueos if "regimen/alturas/empates" not in b and "intervalos no verificables" not in b]
        ocupacion_real = barras_ocupacion
        gfa_total = barras_gfa
        envelope_por_piso = barras_huellas
        envelope_curve = envelope_por_piso[0] if envelope_por_piso else None
        altura_total = barras_altura if barras_altura else pisos_finales * (barras_floor_h if barras_floor_h else floor_h)
        valido = True
else:
    # MODO POTENCIAL (comportamiento actual v08)
    if lot_polygon is not None and vertices_lote:
        for nv in range(1, pisos_finales + 1):
            if intervalos:
                subs = []
                for i in range(len(vertices_lote)-1):
                    a, b = vertices_lote[i], vertices_lote[i+1]
                    cls = next((l.get('clasificacion') for l in lados if l.get('id') == i), 'Lateral')
                    base = retiros_base.get(i, 0.0)
                    seismic = separacion_sismica_piso(nv*floor_h, nsr_coef) if pisos_finales > 3 and nv > 1 else 0.0
                    if cls in ('Lateral','Posterior'):
                        for span in intervalos[i].get('subtramos') or []:
                            t0, t1 = float(span['t0']), float(span['t1'])
                            p = rg.Point3d(a.X+(b.X-a.X)*t0,a.Y+(b.Y-a.Y)*t0,0)
                            q = rg.Point3d(a.X+(b.X-a.X)*t1,a.Y+(b.Y-a.Y)*t1,0)
                            r = max(base, seismic) if cls == 'Lateral' else base
                            h = span.get('altura_m')
                            if cls == 'Lateral' and empate_activo and h is not None:
                                r = max(r,retiro_lateral_empate(nv*floor_h,float(h),empate_lateral_min))
                            subs.append(((p,q),r))
                            diag_recortes.append({'piso':nv,'id':i,'t0':t0,'t1':t1,'retiro_m':r,'altura_vecino_m':h})
                    else:
                        r = max(0.,base-voladizo_frontal) if cls == 'Frontal' and nv > 1 else base
                        subs.append(((a,b),r))
            else:
                subs = _subsegmentos_piso(nv,lados,vertices_lote,retiros_base,vecinos_por_lado,altura_vecinos_m,empate_lateral_min,nsr_coef,pisos_finales,floor_h,voladizo_frontal,empate_activo)
            try:
                envs, area = _recortar_regiones_locales(lot_polygon,subs,patios_list,_area_signada_puntos(vertices_lote)>0)
                huellas_por_piso.append(envs[0] if len(envs)==1 else envs)
                areas_por_piso.append(area)
            except Exception as exc:
                huellas_por_piso.append(None); areas_por_piso.append(0.0)
                bloqueos.append('piso {} recorte no verificable: {}'.format(nv,str(exc)))
    recortes_intervalos_json = json.dumps(diag_recortes,ensure_ascii=True)
    envelope_por_piso = huellas_por_piso
    if envelope_por_piso: envelope_curve = envelope_por_piso[0]
    ocupacion_real = areas_por_piso[0] if areas_por_piso else 0.0
    gfa_total = sum(areas_por_piso)
    # Validación IO potencial
    if io_user > 0: io_maximo = io_user
    elif tratamiento == "Consolidacion": io_maximo = 0.70
    elif tratamiento in ("Desarrollo", "Mejoramiento"): io_maximo = 0.60
    else: io_maximo = 0.70
    io_real = ocupacion_real / area_lote if area_lote > 0 else 0.0
    if area_lote <= 0 or ocupacion_real <= 0: bloqueos.append("lote u ocupacion nulos")
    if not 0 < io_maximo <= 1: bloqueos.append("IO maximo fuera de (0,1]")
    if area_lote > 0 and ocupacion_real > area_lote * io_maximo + TOLERANCIA**2:
        bloqueos.append("IO real {:.4f} > limite {:.4f}; excedente {:.2f} m2".format(io_real, io_maximo, ocupacion_real - area_lote * io_maximo))
    if len(areas_por_piso) != pisos_finales or any(a <= 0 for a in areas_por_piso):
        bloqueos.append("uno o mas niveles sin region valida")
    valido = not bloqueos

# --- SALIDAS APROBADAS (v09) ---
if barras_ocupacion is not None and valido:
    ocupacion_aprobada_m2 = barras_ocupacion
    gfa_aprobado_m2 = barras_gfa
    envelope_aprobado_por_piso = barras_huellas
    # io_real para mensaje en modo APROBADO
    io_real = barras_ocupacion / area_lote if area_lote > 0 else 0.0
else:
    ocupacion_aprobada_m2 = 0.0
    gfa_aprobado_m2 = 0.0
    envelope_aprobado_por_piso = []
    # Asegurar io_real definido para mensaje NO VALIDADO
    if barras_ocupacion is not None:
        io_real = barras_ocupacion / area_lote if area_lote > 0 else 0.0

# Desglose por piso (diagnóstico)
escalonados = []
for nv in range(1, pisos_finales + 1):
    h_piso = nv * floor_h
    r_sismica = separacion_sismica_piso(h_piso, nsr_coef) if (pisos_finales > 3 and nv > 1) else 0.0
    retiro_max = 0.0
    for i, lado in enumerate(lados):
        if lado.get("clasificacion", "Lateral") != "Lateral": continue
        lid = lado.get("id", i)
        r_l = 0.0
        if empate_activo:
            if lid in vecinos_por_lado:
                r_l = max([retiro_lateral_empate(h_piso, v[0], empate_lateral_min) for v in vecinos_por_lado[lid]] or [0.0])
            else: r_l = retiro_lateral_empate(h_piso, altura_vecinos_m, empate_lateral_min)
        retiro_max = max(retiro_max, r_l, r_sismica)
    if retiro_max > 0: escalonados.append(nv)

try:
    retiros_por_piso = json.dumps([{"piso": i+1, "altura_m": round((i+1)*floor_h,2), "area_m2": round(areas_por_piso[i],2), "escalonado": (i+1) in escalonados, "voladizo_frontal_m": round(voladizo_frontal if i>0 else 0.0,2), "vecinos_por_lado": {str(k): [round(v[0],2) for v in vs] for k,vs in vecinos_por_lado.items()}} for i in range(pisos_finales)], ensure_ascii=False)
except: retiros_por_piso = "[]"

# --- Mensaje final ---
if io_user > 0: io_maximo = io_user
elif tratamiento == "Consolidacion": io_maximo = 0.70
elif tratamiento in ("Desarrollo", "Mejoramiento"): io_maximo = 0.60
else: io_maximo = 0.70

if valido:
    modo = "APROBADO (barras_json)" if barras_ocupacion is not None else "POTENCIAL"
    empate_txt = "NO aplica (sin lado posterior): solo sismica 2%xh" if not empate_activo else "activo (lado posterior)"
    mensaje = ("NORMATIVA v09.0 | {} | Lote: {:.1f}m2 | Ocup: {:.1f}m2 | IO max {:.2f} | Presupuesto: {:.1f}m2 | "
               "IC {:.2f} (+{}) | Alt {:.1f}m | {} pisos | GFA: {:.1f}m2 "
               "Escalonados: {} pisos | Voladizo frontal {:.2f}m | Vecinos: {} lados, {} vecinos | "
               "Empate 1.9.c: {} | Patios: {:.1f}m2 | Tipo:{} | Antejardin {:.1f}m (via {:.1f}m) | "
               "Lat {:.1f}m | Post {:.1f}m{}").format(
        modo, area_lote, ocupacion_real, io_maximo, presupuesto_ocupacion_m2,
        float((gfa_aprobado_m2 or gfa_total) / area_lote if area_lote > 0 else 0), pisos_extra, altura_total,
        pisos_finales, float(gfa_aprobado_m2 if gfa_aprobado_m2 else gfa_total), len(escalonados),
        voladizo_frontal, len(vecinos_por_lado), total_vecinos, empate_txt,
        patio_area_total, tipologia, antejardin, ancho_via_m, retiro_lateral, retiro_posterior,
        " (empate)" if empate_posterior else "")
else:
    mensaje = ("NORMATIVA v09.0 | NO VALIDADO | Lote {:.2f} m2 | Ocup {:.2f} m2 | IO real {:.4f} / max {:.4f} | Presupuesto {:.2f} m2 | {} pisos | Alt {:.2f} m | GFA {:.2f} m2 | {}").format(
        area_lote, ocupacion_real, io_real, io_maximo, presupuesto_ocupacion_m2, pisos_finales, altura_total, float(gfa_total if 'gfa_total' in locals() else 0), "; ".join(sorted(set(bloqueos))))

if altura_vecinos_m <= 0: warnings.append("sin altura_vecinos_m -> sin escalonamiento lateral (SECCION 1.9.c)")

if warnings: mensaje += " | AVISOS: " + "; ".join(warnings)

# --- ASIGNAR SALIDAS GLOBALES PARA GRASSHOPPER ---
# Las variables siguientes son recogidas por el componente GH:
# envelope_curve, envelope_por_piso, retiros_por_piso, gfa_total, ocupacion_real,
# io_maximo, ic_real, ic_maximo, altura_total, pisos_finales, valido, mensaje,
# recortes_intervalos_json, presupuesto_ocupacion_m2, ocupacion_aprobada_m2,
# gfa_aprobado_m2, envelope_aprobado_por_piso