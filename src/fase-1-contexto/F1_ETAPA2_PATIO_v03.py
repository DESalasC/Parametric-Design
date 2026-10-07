# -*- coding: utf-8 -*-
"""
================================================================================
F1_ETAPA2_PATIO_v03.py — Patio(s) desde el Vertice N con BIFURCACION
Proyecto: DisenoParametrico / Fase 1
GH Python Script para Grasshopper (IronPython 2.7 compatible)
================================================================================

v03.3 (2026-10-03): Actualizacion documentacion y mensajes segun reglas
  aprobadas operador (2026-10-03):
    - 1 VOLUMEN -> patio normativo Anexo 5 §1.12.b (H/3, >=9 m2, >=3 ml lado).
    - >=2 VOLÚMENES -> separaciones entre volúmenes actúan como "patios"
      y COMPUTAN EN IO (no patios independientes por volumen).
  Advertencia si io_real > io_maximo.
  Comportamiento v03.2 intacto (bifurcación n_volumenes: único/MULTI/AUTO).

v03.2 PROPUESTA (no validada en Rhino): ancla N opcional en AUTO,
  clasificacion explicita de esquinas reflex, inclusion de region completa
  y dimension por altura/3. Sigue generando PATIOS DE ESQUINA, no edificios.
  altura_max_pot debe representar la altura real mayor que enmarca el patio;
  no conectar pisos ni altura tipologica obsoleta como sustituto.

ALGORITMO BASE (v02.x):
  El patio se origina en el VERTICE N (el vertice del lote simplificado
  mas alejado de las vias del frente, segun F1_ETAPA2_LADOS_v06). Garantias
  obligatorias (decisiones del operador 2026-09-28):
    - area minima = 9 m2
    - "3 metros lineales" de distancia entre CADA lado del predio y el borde
      del patio que le es opuesto (claridad/profundidad desde cada lado que
      comparte el vertice N).
  Forma: paralelogramo anclado al vertice N, alineado a las direcciones de
  los dos lados; para esquinas no perpendiculares (angulo theta):
      L = max(lado_base, 3.0 / sin(theta)) ; ademas L >= sqrt(9 / sin(theta))
  Simplificacion de lados colineales con giro < 2.5 grados (identica a
  LADOS v06.5, misma funcion y mismo input -> indices consistentes).

  v02.2 - consume vertice_n_points de LADOS v06.3 (puntos mejorados).
  v02.3 - garantias de area/claridad; simplificacion 2.5 grados; dedup de
          puntos mejorados (>= 0.30 m) y coincidencia con vertice (<= 0.15 m);
          maximo 1 patio; mensajes con metricas y motivos de descarte.
  v02.4 - EXPORT del diagnostico lados/patio: si existe el flag
          data/pot-cache/lados-export-flag.json con {exportar: true} (lo pone
          el servidor/orquestador via POST /api/exportar-lados), escribe
          data/pot-cache/<CHIP>-lados.json para verificacion automatica (F1.5)
          y devuelve el flag a false (mismo patron que F1_EXPORTAR_GFA_v02).
  v02.5 - LECTOR CANONICO de codificacion en la lectura del flag (cascada
          utf-8-sig -> cp1252 -> latin-1 con avisos) y escritura ASCII-safe
          (ensure_ascii=True) en los JSON exportados.

  v03.0 (2026-09-30) - BIFURCACION POR NUMERO DE VOLUMENES (pedido del
          operador 2026-09-30: "un lote con un solo volumen que exige un solo
          patio -> un predio donde se pueden tener varios patios ya sea
          internos o separaciones entre diferentes volumenes"):
            n_volumenes <= 1  ->  modo UNICO:  comportamiento v02.5 exacto
                                  (maximo 1 patio desde Vertice N).
            n_volumenes >= 2  ->  modo MULTI:  un patio por ESQUINA INTERIOR
                                  ELEGIBLE (vertice cuyos dos lados adyacentes
                                  son colindantes Lateral/Posterior),
                                  priorizando el Vertice N y luego por
                                  INTERIORIDAD (mayor distancia minima a
                                  via/EP); hasta n_volumenes patios; se
                                  descartan candidatos que se solapen con un
                                  patio ya aceptado. Mensajes con anclas,
                                  areas y claridades de cada patio.
          NOTA: la regla de reparto del modo MULTI es v1 y queda SUJETA A
          VALIDACION DEL OPERADOR en la corrida viva (internos vs
          separaciones pueden requerir reglas adicionales).
  v03.1 (2026-09-30) - INFERENCIA AUTOMATICA (minima injerencia del operador,
          pedido del operador 2026-09-30): n_volumenes=0/vacio -> modo AUTO:
          el componente infiere el numero de volumenes/patios del lote como
            n = min(esquinas interiores VALIDAS, capacidad del lote)
          con capacidad = round(area_lote / A_REF_VOL_M2), A_REF_VOL_M2=300 m2
          (basico, ajustable; en etapas posteriores puede venir del proyecto).
          El ancla preferente sigue siendo el Vertice N (con puntos mejorados
          si existen) y, si no valida, el modo AUTO puede anclar en otra
          esquina interior (antes: 0 + sugerencia).
          n_volumenes=1 -> modo unico FORZADO (comportamiento v02.5 estricto);
          n_volumenes>=2 -> modo MULTI forzado con ese tope.
          La capacidad y las reglas de patios interiores (GFA/altura/IO) son
          v1 y se refinaran con las "Zonas" del operador (etapa posterior).
  Regla de versionado: la version general (v03 -> v04) SOLO cambia con
  cambios mayores (contrato de entradas/salidas o algoritmo central); las
  iteraciones internas se registran como subversiones v03.x en este encabezado.

REGLAS DE PATIOS / SEPARACIONES (aprobadas operador 2026-10-03):
  - 1 VOLUMEN: patio normativo Anexo 5 §1.12.b (cuadrado H/3, min 9 m², 3 ml lado).
  - >=2 VOLÚMENES: separaciones entre volúmenes = "patios" que COMPUTAN EN IO
    (no patios independientes por volumen).
  - Sin voladizos internos entre volúmenes.
  - Separación mínima entre cuerpos = max(6.0 m, 0.2 * altura_promedio,
    NSR-10 A.6.5 2% * h_piso si >3 pisos).

ENTRADAS:
  lot_vertices (Point3d[])     — vertices desde Discontinuity
  sides_table_json (String)    — Clasificacion desde F1_ETAPA2_LADOS_v06
  altura_max_pot (Number)      — Altura maxima [m] (define lado base del patio)
  n_volumenes (Number)         — [v03.1] 0/vacio = AUTO (inferido del lote);
                                  1 = unico forzado; >=2 = numero forzado

SALIDAS:
  patios_curves   (Curve[])   — 0..N rectangulos/paralelogramos de patio
  patio_count     (int)       — Numero de patios generados
  mensaje         (String)    — Diagnostico
================================================================================
"""

import Rhino.Geometry as rg
import json
import math
import os
from datetime import datetime

PATIO_MINIMO_M = 3.0
ALTURA_ENTREPISO = 3.0
# v02.3: garantias (decision operador 2026-09-28)
CLARIDAD_MINIMA_M = 3.0
AREA_MINIMA_M2 = 9.0
# v02.3: simplificacion colineal (misma regla que LADOS v06.5)
UMBRAL_COLINEAL_GRADOS = 2.5
# v02.3: dedup de puntos mejorados y coincidencia con vertice del lote
CLUSTER_PUNTOS_M = 0.30
COINCIDENCIA_VERTICE_M = 0.15
# v02.3: clamp de sin(theta) para esquinas degeneradas (~5 grados)
SIN_MINIMO = 0.087
# v03.0: limite de seguridad del numero de volumenes/patios
N_VOL_MAX = 16
# v03.1: huella de referencia por volumen [m2] (capacidad basica del lote;
# ajustable; en etapas posteriores puede venir del proyecto/UI)
A_REF_VOL_M2 = 300.0


def _decodificar_cascada(raw, ruta="<bytes>"):
    """LECTOR CANONICO (v02.5): utf-8-sig estricto -> cp1252 -> latin-1."""
    try:
        return raw.decode("utf-8-sig")
    except Exception:
        pass
    try:
        texto = raw.decode("cp1252")
        print("[AVISO ENCODING] leido como cp1252 (no utf-8): %s" % ruta)
        return texto
    except Exception:
        pass
    texto = raw.decode("latin-1")
    print("[AVISO ENCODING] leido como latin-1 (ultimo recurso): %s" % ruta)
    return texto


def unwrap(val):
    if val is None: return None
    if isinstance(val, list): return val[0] if len(val) > 0 else None
    return val


def safe_list(val):
    if val is None: return []
    if isinstance(val, list): return val
    return [val]


def _giro_grados(p_prev, p, p_next):
    """v02.3 - Angulo de giro (0-180) en p entre vector entrante y saliente.

    0 = colineal recto; 180 = retorno.
    """
    ax = p.X - p_prev.X
    ay = p.Y - p_prev.Y
    bx = p_next.X - p.X
    by = p_next.Y - p.Y
    la = math.sqrt(ax * ax + ay * ay)
    lb = math.sqrt(bx * bx + by * by)
    if la < 1e-12 or lb < 1e-12:
        return 0.0
    cosang = (ax * bx + ay * by) / (la * lb)
    if cosang > 1.0: cosang = 1.0
    if cosang < -1.0: cosang = -1.0
    return math.degrees(math.acos(cosang))


def simplificar_colineales(vertices, umbral_grados=UMBRAL_COLINEAL_GRADOS):
    """v02.3 - Fusiona vertices colineales o con giro < umbral (2.5 grados).

    Misma regla que LADOS v06.5 (decision operador 2026-09-28): se simplifican
    los vertices con variacion de angulo INFERIOR a 2.5 grados; los de 2.5
    grados o mas se mantienen, independiente del numero final de lados.
    Elimina iterativamente el vertice de MENOR giro bajo el umbral y recalcula
    (asi los angulos que superan el umbral tras fusionar se conservan).
    Nunca baja de 3 vertices.
    """
    pts = []
    for v in vertices:
        if not pts or pts[-1].DistanceTo(v) > 1e-9:
            pts.append(v)
    if len(pts) > 1 and pts[0].DistanceTo(pts[-1]) < 1e-9:
        pts.pop()
    while len(pts) > 3:
        n = len(pts)
        mejor_i = -1
        mejor_giro = None
        for i in range(n):
            g = _giro_grados(pts[(i - 1) % n], pts[i], pts[(i + 1) % n])
            if g < umbral_grados and (mejor_giro is None or g < mejor_giro):
                mejor_giro = g
                mejor_i = i
        if mejor_i < 0:
            break
        pts.pop(mejor_i)
    return pts


def deduplicar_puntos(puntos, tol_m=CLUSTER_PUNTOS_M):
    """v02.3 - Conserva el primer punto de cada cluster (>= tol_m)."""
    kept = []
    for p in puntos:
        duplicado = False
        for q in kept:
            if p.DistanceTo(q) < tol_m:
                duplicado = True
                break
        if not duplicado:
            kept.append(p)
    return kept


def _raiz_proyecto():
    """v02.4 - Raiz del proyecto desde la variable de entorno del canvas."""
    raiz = os.environ.get("DISENO_PARAMETRICO_ROOT", "")
    if raiz and os.path.isdir(raiz):
        return raiz
    return ""


def _escribir_json_utf8(ruta, data):
    """Escritura canonica v02.5: UTF-8 sin BOM + ASCII-safe (ensure_ascii)
    para robustez entre herramientas; nombre historico conservado."""
    with open(ruta, "wb") as f:
        f.write(json.dumps(data, indent=2, ensure_ascii=True).encode("utf-8"))


def _exportar_diagnostico(sides_data, patios_export, mensaje_final, modo, n_vol):
    """v02.4 - Exporta el diagnostico lados/patio si el flag lo solicita.

    Flag: data/pot-cache/lados-export-flag.json {"exportar": true, "chip": ...}
    Salida: data/pot-cache/<CHIP>-lados.json (schema lados_patio_diagnostico_v01).
    Devuelve la ruta escrita, o None si no fue solicitado.
    v03.0: agrega modo/n_volumenes al bloque patio.
    """
    raiz = _raiz_proyecto()
    if not raiz:
        return None
    flag_ruta = os.path.join(raiz, "data", "pot-cache", "lados-export-flag.json")
    if not os.path.exists(flag_ruta):
        return None
    try:
        with open(flag_ruta, "rb") as f:
            _raw = f.read()
        flag = json.loads(_decodificar_cascada(_raw, flag_ruta))
    except Exception:
        return None
    if not isinstance(flag, dict) or not flag.get("exportar"):
        return None
    chip = str(flag.get("chip") or "").strip()
    if not chip:
        return None
    lados = []
    for l in (sides_data.get("lados") or []):
        lados.append({
            "id": l.get("id"),
            "clasificacion": l.get("clasificacion"),
            "motivo": l.get("motivo"),
            "cardinal": l.get("cardinal"),
            "toca_via": l.get("toca_via"),
            "toca_ep": l.get("toca_ep"),
            "toca_vecino": l.get("toca_vecino"),
        })
    data = {
        "schema": "lados_patio_diagnostico_v01",
        "chip": chip,
        "generado_por": "F1_ETAPA2_PATIO_v03.3",
        "generado_en": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "solicitud": flag,
        "sides": {
            "total_lados": sides_data.get("total_lados"),
            "n_vertices_originales": sides_data.get("n_vertices_originales"),
            "vertice_a": sides_data.get("vertice_a"),
            "vertice_n": sides_data.get("vertice_n"),
            "es_esquina": sides_data.get("es_esquina"),
            "ancho_via_m": sides_data.get("ancho_via_m"),
            "lados": lados,
        },
        "patio": {
            "modo": modo,
            "n_volumenes": n_vol,
            "count": len(patios_export),
            "patios": patios_export,
            "mensaje": mensaje_final,
        },
    }
    out_ruta = os.path.join(raiz, "data", "pot-cache", chip + "-lados.json")
    _escribir_json_utf8(out_ruta, data)
    # devolver el flag a false (patron GFA)
    _escribir_json_utf8(flag_ruta, {"exportar": False, "chip": chip,
                                    "ts": datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
    return out_ruta


def point_in_lot(pt, vertices):
    """Ray casting + deteccion de punto sobre el borde (tol 0.1m)."""
    n = len(vertices)
    if n < 3: return False
    px, py = pt.X, pt.Y
    # 1) Ray casting estandar
    count = 0
    for i in range(n):
        v1 = vertices[i]
        v2 = vertices[(i + 1) % n]
        if ((v1.Y > py) != (v2.Y > py)):
            if (v2.Y - v1.Y) != 0:
                x_int = v1.X + (py - v1.Y) * (v2.X - v1.X) / (v2.Y - v1.Y)
                if px < x_int:
                    count += 1
    if (count % 2) == 1:
        return True
    # 2) Punto sobre el borde (distancia al segmento < 0.1m)
    for i in range(n):
        v1 = vertices[i]
        v2 = vertices[(i + 1) % n]
        dx = v2.X - v1.X
        dy = v2.Y - v1.Y
        l2 = dx * dx + dy * dy
        if l2 < 1e-12:
            continue
        t = ((px - v1.X) * dx + (py - v1.Y) * dy) / l2
        t = max(0.0, min(1.0, t))
        cx = v1.X + t * dx
        cy = v1.Y + t * dy
        dist = math.sqrt((px - cx) ** 2 + (py - cy) ** 2)
        if dist < 0.1:
            return True
    return False


def _dir_interior(corner_pt, p1, p2):
    """Direccion unitaria desde corner_pt hacia el otro extremo del borde."""
    otro = p2 if corner_pt.DistanceTo(p1) < 0.05 else p1
    d = rg.Vector3d(otro.X - corner_pt.X, otro.Y - corner_pt.Y, 0)
    if d.Length > 1e-9:
        d.Unitize()
    return d


def build_patio_desde_vertice(corner_pt, borde_a_p1, borde_a_p2,
                              borde_b_p1, borde_b_p2, lado_base, lot_vertices):
    """
    v02.3 - Paralelogramo de patio anclado en corner_pt (vertice N), con lados
    ALINEADOS a las direcciones de los dos bordes del lote que comparten el
    vertice (las direcciones apuntan hacia el INTERIOR del lote).

    Garantias (decisiones operador 2026-09-28):
      - claridad respecto a cada lado = L * sin(theta) >= 3.0 m
      - area = L^2 * sin(theta) >= 9.0 m2
    => L = max(lado_base, CLARIDAD_MINIMA_M / sin(theta)).

    Retorna (curva, (L, sin_theta), [p0, p1, p2, p3]) o None si no valida
    (no cabe / no es interior al lote).
    """
    da = _dir_interior(corner_pt, borde_a_p1, borde_a_p2)
    db = _dir_interior(corner_pt, borde_b_p1, borde_b_p2)

    # Esquina convexa/reflex segun orientacion del poligono, no |cruz|.
    signed_area = sum(lot_vertices[i].X * lot_vertices[(i + 1) % len(lot_vertices)].Y
                      - lot_vertices[(i + 1) % len(lot_vertices)].X * lot_vertices[i].Y
                      for i in range(len(lot_vertices)))
    cross_dirs = da.X * db.Y - da.Y * db.X
    if cross_dirs * signed_area <= 0:
        return None  # reflex o degenerada: descartar localmente
    sin_t = abs(cross_dirs)
    if sin_t < SIN_MINIMO:
        return None  # no falsear la geometria con un seno artificial

    cos_t = abs(da.X * db.X + da.Y * db.Y)
    size_square = lado_base * (sin_t + cos_t) / sin_t
    size = max(size_square, CLARIDAD_MINIMA_M / sin_t)
    size_area = math.sqrt(AREA_MINIMA_M2 / sin_t)
    if size < size_area:
        size = size_area

    len_a = borde_a_p1.DistanceTo(borde_a_p2)
    len_b = borde_b_p1.DistanceTo(borde_b_p2)
    if size > 0.98 * min(len_a, len_b):
        return None

    p0 = rg.Point3d(corner_pt)
    p1 = rg.Point3d(p0.X + da.X * size, p0.Y + da.Y * size, p0.Z)
    p3 = rg.Point3d(p0.X + db.X * size, p0.Y + db.Y * size, p0.Z)
    p2 = rg.Point3d(p1.X + db.X * size, p1.Y + db.Y * size, p0.Z)

    # Validacion de interioridad: p1/p3 caen sobre los bordes del lote (dentro
    # de la tolerancia de borde de point_in_lot) y p2 debe quedar adentro.
    if not (point_in_lot(p1, lot_vertices)
            and point_in_lot(p2, lot_vertices)
            and point_in_lot(p3, lot_vertices)):
        return None

    poly = rg.Polyline()
    poly.Add(p0); poly.Add(p1); poly.Add(p2); poly.Add(p3); poly.Add(p0)
    candidate = rg.PolylineCurve(poly)
    # Los vertices dentro no garantizan que toda la region este dentro.
    lot_poly = rg.Polyline(list(lot_vertices))
    if not lot_poly.IsClosed:
        lot_poly.Add(lot_poly[0])
    try:
        outside = rg.Curve.CreateBooleanDifference(
            candidate, rg.PolylineCurve(lot_poly), 0.001)
        if outside is None:
            return None
        if len(outside):
            regions = rg.Brep.CreatePlanarBreps(list(outside), 0.001)
            if not regions:
                return None
            outside_area = sum(rg.AreaMassProperties.Compute(b).Area for b in regions)
            if outside_area > 0.0001:
                return None
    except Exception:
        return None
    return (candidate, (size, sin_t), [p0, p1, p2, p3])


# ==============================================================================
# v03.0: utilidades de geometria para el modo MULTI (solapes)
# ==============================================================================

def _punto_en_poligono(pt, poly_pts):
    """Ray casting XY simple (poly_pts: lista de Point3d, abierta o cerrada)."""
    pts = list(poly_pts)
    if len(pts) > 1 and pts[0].DistanceTo(pts[-1]) < 1e-9:
        pts = pts[:-1]
    n = len(pts)
    if n < 3:
        return False
    px, py = pt.X, pt.Y
    inside = False
    j = n - 1
    for i in range(n):
        xi, yi = pts[i].X, pts[i].Y
        xj, yj = pts[j].X, pts[j].Y
        if ((yi > py) != (yj > py)):
            if abs(yj - yi) > 1e-12:
                x_int = xi + (py - yi) * (xj - xi) / (yj - yi)
                if px < x_int:
                    inside = not inside
        j = i
    return inside


def _orient(a, b, c):
    """Producto cruz 2D (b-a)x(c-a)."""
    return (b.X - a.X) * (c.Y - a.Y) - (b.Y - a.Y) * (c.X - a.X)


def _segmentos_cruzan(a1, a2, b1, b2):
    """True si los segmentos se CRUZAN propiamente (tolerante a contactos)."""
    d1 = _orient(b1, b2, a1)
    d2 = _orient(b1, b2, a2)
    d3 = _orient(a1, a2, b1)
    d4 = _orient(a1, a2, b2)
    if ((d1 > 1e-9 and d2 < -1e-9) or (d1 < -1e-9 and d2 > 1e-9)) and \
       ((d3 > 1e-9 and d4 < -1e-9) or (d3 < -1e-9 and d4 > 1e-9)):
        return True
    return False


def _patios_solapan(pa, pb):
    """v03.0 - True si dos patios (listas de 4 Point3d) se solapan.

    Prueba: vertices y centroide/mitades de arista de un patio dentro del
    otro, y cruces propios entre aristas. (Los contactos de borde exactos
    no cuentan como solape.)
    """
    def _puntos_muestra(pts):
        mx = 0.0
        my = 0.0
        for p in pts:
            mx += p.X
            my += p.Y
        cx = mx / len(pts)
        cy = my / len(pts)
        muestras = [rg.Point3d(cx, cy, pts[0].Z)]
        for i in range(len(pts)):
            a = pts[i]
            b = pts[(i + 1) % len(pts)]
            muestras.append(rg.Point3d((a.X + b.X) / 2.0, (a.Y + b.Y) / 2.0, a.Z))
        return muestras

    for p in list(pa) + _puntos_muestra(pa):
        if _punto_en_poligono(p, pb):
            return True
    for p in list(pb) + _puntos_muestra(pb):
        if _punto_en_poligono(p, pa):
            return True
    for i in range(len(pa)):
        a1 = pa[i]
        a2 = pa[(i + 1) % len(pa)]
        for j in range(len(pb)):
            b1 = pb[j]
            b2 = pb[(j + 1) % len(pb)]
            if _segmentos_cruzan(a1, a2, b1, b2):
                return True
    return False


# ==============================================================================
# MAIN
# ==============================================================================

lot_vertices_raw = globals().get("lot_vertices", None)
sides_raw = globals().get("sides_table_json", None)
altura_raw = globals().get("altura_max_pot", None)
n_vol_raw = globals().get("n_volumenes", None)

lot_vertices = safe_list(lot_vertices_raw)
n_vertices_brutos = len(lot_vertices)
# v02.3: simplificacion de lados colineales (giro < 2.5 grados), identica a
# la que aplica LADOS v06.5 sobre el mismo input -> los indices del JSON de
# lados coinciden con esta lista simplificada.
lot_vertices = simplificar_colineales(lot_vertices, UMBRAL_COLINEAL_GRADOS)

# v03.1: 0 o vacio = AUTO (inferido); 1 = unico forzado; >=2 = multi forzado
n_vol_sel = 0
try:
    _nv = unwrap(n_vol_raw)
    if _nv is not None:
        n_vol_sel = int(round(float(_nv)))
except Exception:
    n_vol_sel = 0
if n_vol_sel < 0:
    n_vol_sel = 0
if n_vol_sel > N_VOL_MAX:
    n_vol_sel = N_VOL_MAX
if n_vol_sel == 0:
    modo = "auto"
elif n_vol_sel == 1:
    modo = "unico"
else:
    modo = "multi"
n_vol = n_vol_sel  # reemplazado por el efectivo en cada rama (AUTO lo infiere)

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

try:
    altura_max = float(unwrap(altura_raw)) if altura_raw else 11.4
except:
    altura_max = 11.4

patios_curves = []
patio_count = 0
patios_export = []
mensaje = ""
# Inicialización explícita para Grasshopper (evita NullReferenceException)
# Las variables patios_curves, patio_count, mensaje ya están arriba

if sides_data is None or len(lot_vertices) < 3:
    mensaje = "PATIO v03.3 | ERROR: vertices={} sides={}".format(
        len(lot_vertices), "OK" if sides_data else "FALTA")
else:
    try:
        lados = sides_data.get("lados", [])
        vertice_n = sides_data.get("vertice_n", None)
        n = len(lot_vertices)

        try:
            vertice_n = int(vertice_n) if vertice_n is not None else None
        except (ValueError, TypeError):
            vertice_n = None
        if vertice_n is not None and not 0 <= vertice_n < n:
            vertice_n = None
        if vertice_n is None and modo != "unico":
            vertice_n = 0  # prioridad convencional; AUTO sigue probando todas
        if vertice_n is None:
            mensaje = "PATIO v03.3 | ERROR: modo unico requiere vertice_n valido"
        else:
            # Tamano base del patio segun altura (reglamentacion POT)
            # Anexo 5 1.12.b segun ficha del proyecto: cuadrado H/3, min 3m.
            # En paralelogramos exigimos un cuadrado inscribible suficiente:
            # L*sin(theta)/(sin(theta)+abs(cos(theta))) >= D.
            patio_lado_base = max(PATIO_MINIMO_M, altura_max / 3.0)

            resultados = []
            descartes = []

            def _cat_lado(idx):
                if 0 <= idx < len(lados):
                    return lados[idx].get("clasificacion", "Desconocido")
                return "Desconocido"

            def _intentar(vi, idx, etiqueta):
                if len(lados) >= n and n > 0:
                    lado1 = lados[idx]
                    lado2 = lados[(idx + n - 1) % n]
                else:
                    lado1 = {}
                    lado2 = {}
                cat1 = lado1.get("clasificacion", "Desconocido")
                cat2 = lado2.get("clasificacion", "Desconocido")
                if not (cat1 in ("Lateral", "Posterior") and cat2 in ("Lateral", "Posterior")):
                    descartes.append("{}: V{} sin lados colindantes ({},{})".format(
                        etiqueta, idx, cat1, cat2))
                    return None
                va1 = vi
                va2 = lot_vertices[(idx + 1) % n]
                vb1 = lot_vertices[(idx + n - 1) % n]
                vb2 = vi
                res = build_patio_desde_vertice(
                    vi, va1, va2, vb1, vb2, patio_lado_base, lot_vertices)
                if res is None:
                    descartes.append("{}: patio en V{} no valida (no cabe / no interior)".format(
                        etiqueta, idx))
                    return None
                return res

            def _interioridad(idx):
                """v03.0 - Menor distancia a via/EP de los dos lados del vertice
                (mayor = mas interior). Sin datos -> 0.0 (ultimo en prioridad)."""
                ds = []
                for lidx in (idx, (idx + n - 1) % n):
                    if 0 <= lidx < len(lados):
                        l = lados[lidx]
                        for k in ("dist_via_m", "dist_ep_m"):
                            v = l.get(k)
                            if isinstance(v, (int, float)):
                                ds.append(float(v))
                if not ds:
                    return 0.0
                return min(ds)

            if modo == "unico":
                # ---------------- Modo UNICO (comportamiento v02.5) ----------------
                # 1) Puntos mejorados de Vertice N (v02.2) con dedup y filtro de
                #    coincidencia con vertices del lote (v02.3).
                vertice_n_points_data = sides_data.get("vertice_n_points")
                candidatos = []
                if vertice_n_points_data:
                    for coords in vertice_n_points_data:
                        try:
                            candidatos.append(rg.Point3d(
                                coords[0], coords[1],
                                coords[2] if len(coords) > 2 else 0))
                        except Exception:
                            pass
                    candidatos = deduplicar_puntos(candidatos, CLUSTER_PUNTOS_M)

                for vi in candidatos:
                    min_dist = float('inf')
                    idx = 0
                    for i, v in enumerate(lot_vertices):
                        dist = v.DistanceTo(vi)
                        if dist < min_dist:
                            min_dist = dist
                            idx = i
                    if min_dist > COINCIDENCIA_VERTICE_M:
                        descartes.append("mejorado ({:.2f},{:.2f}) a {:.2f} m de un vertice".format(
                            vi.X, vi.Y, min_dist))
                        continue
                    res = _intentar(vi, idx, "mejorado")
                    if res:
                        resultados.append((res[0], res[1], res[2], idx))
                        break  # v02.3: maximo 1 patio

                # 2) Fallback tradicional (indice vertice_n) si no hubo resultado.
                if not resultados:
                    vi = lot_vertices[vertice_n]
                    res = _intentar(vi, vertice_n, "fallback")
                    if res:
                        resultados.append((res[0], res[1], res[2], vertice_n))

                cats = [l.get("clasificacion", "?") for l in lados]

                if resultados:
                    crv, info, pts_patio, idx_usado = resultados[0]
                    size = info[0]
                    sin_t = info[1]
                    area = size * size * sin_t
                    claridad = size * sin_t
                    patios_curves = [crv]
                    patio_count = 1
                    patios_export = [{
                        "vertice_ancla": idx_usado,
                        "puntos": [[p.X, p.Y] for p in pts_patio],
                        "lado_m": round(size, 4),
                        "area_m2": round(area, 4),
                        "claridad_m": round(claridad, 4),
                    }]
                    modo_anclaje = "puntos_mejorados" if candidatos else "fallback_V_N"
                    mensaje = ("PATIO v03.3 | modo unico (forzado) | V_N=V{} | Verts {}->{} | Lados: {} | "
                               "Patio {:.2f}x{:.2f} m (area {:.2f} m2; claridad {:.2f} m) | "
                               "Generados: 1 | Modo: {}").format(
                        idx_usado, n_vertices_brutos, n, ", ".join(cats),
                        size, size, area, claridad, modo_anclaje)
                    if descartes:
                        mensaje += " | Descartes: " + "; ".join(descartes[:3])
                else:
                    mensaje = ("PATIO v03.3 | modo unico (forzado) | V_N=V{} | Verts {}->{} | Lados: {} | "
                               "Generados: 0 | Motivo: {}").format(
                        vertice_n, n_vertices_brutos, n, ", ".join(cats),
                        "; ".join(descartes) if descartes else "sin candidatos de esquina")
                    mensaje += (" | Sugerencia: dejar n_volumenes en 0 (AUTO) permite "
                                "anclar en otra esquina interior")
            else:
                # ---------------- Motor v03.1: AUTO / MULTI (regla v1) ----------------
                cats = [l.get("clasificacion", "?") for l in lados]
                elegibles = []
                for idx in range(n):
                    c1 = _cat_lado(idx)
                    c2 = _cat_lado((idx + n - 1) % n)
                    if c1 in ("Lateral", "Posterior") and c2 in ("Lateral", "Posterior"):
                        elegibles.append(idx)

                # Puntos mejorados de Vertice N (v02.2/v02.3) para el ancla preferente.
                candidatos_mejorados = []
                vertice_n_points_data = sides_data.get("vertice_n_points")
                if vertice_n_points_data:
                    for coords in vertice_n_points_data:
                        try:
                            candidatos_mejorados.append(rg.Point3d(
                                coords[0], coords[1],
                                coords[2] if len(coords) > 2 else 0))
                        except Exception:
                            pass
                    candidatos_mejorados = deduplicar_puntos(candidatos_mejorados, CLUSTER_PUNTOS_M)
                    coincidentes = []
                    for vi in candidatos_mejorados:
                        for v in lot_vertices:
                            if v.DistanceTo(vi) <= COINCIDENCIA_VERTICE_M:
                                coincidentes.append(vi)
                                break
                    candidatos_mejorados = coincidentes

                orden = []
                if vertice_n in elegibles:
                    orden.append(vertice_n)
                otros = [i for i in elegibles if i != vertice_n]
                # mayor interioridad primero (mas lejos de via/EP)
                otros.sort(key=lambda i: _interioridad(i), reverse=True)
                orden += otros

                aceptados = []
                anclas_usadas = []
                mejorado_usado = False
                for idx in orden:
                    if len(aceptados) >= N_VOL_MAX:
                        break
                    vi = lot_vertices[idx]
                    etiqueta = "multi" if modo == "multi" else "auto"
                    if idx == vertice_n and candidatos_mejorados:
                        # ancla preferente con punto mejorado de V_N
                        vi = candidatos_mejorados[0]
                        etiqueta = "mejorado"
                    # dedup de ancla: no intentar dos veces la misma esquina
                    dup = False
                    for a in anclas_usadas:
                        if vi.DistanceTo(a) < CLUSTER_PUNTOS_M:
                            dup = True
                            break
                    if dup:
                        continue
                    res = _intentar(vi, idx, etiqueta)
                    if not res:
                        continue
                    if etiqueta == "mejorado":
                        mejorado_usado = True
                    pts = res[2]
                    if any(_patios_solapan(pts, a[2]) for a in aceptados):
                        descartes.append("{}: V{} se solapa con patio previo".format(etiqueta, idx))
                        continue
                    aceptados.append((res[0], res[1], res[2], idx))
                    anclas_usadas.append(vi)

                n_validos = len(aceptados)
                area_lote_calc = 0.0
                for i2 in range(n):
                    x1 = lot_vertices[i2].X
                    y1 = lot_vertices[i2].Y
                    x2 = lot_vertices[(i2 + 1) % n].X
                    y2 = lot_vertices[(i2 + 1) % n].Y
                    area_lote_calc += x1 * y2 - x2 * y1
                area_lote_calc = abs(area_lote_calc) / 2.0
                capacidad = int(area_lote_calc / A_REF_VOL_M2 + 0.5)
                if capacidad < 1:
                    capacidad = 1

                if modo == "auto":
                    n_vol = min(n_validos, capacidad)
                    aceptados = aceptados[:n_vol]
                    nota = ""
                    if n_validos > capacidad:
                        nota = " | Nota: limitado por capacidad del lote"
                    elif n_validos < capacidad:
                        nota = " | Nota: menos esquinas validas que capacidad"
                    if mejorado_usado:
                        nota += " | Ancla V_N: punto mejorado"
                else:
                    n_vol = n_vol_sel
                    aceptados = aceptados[:n_vol]
                    nota = ""

                patios_curves = [a[0] for a in aceptados]
                patio_count = len(aceptados)
                patios_export = []
                for a in aceptados:
                    size = a[1][0]
                    sin_t = a[1][1]
                    area = size * size * sin_t
                    claridad = size * sin_t
                    patios_export.append({
                        "vertice_ancla": a[3],
                        "puntos": [[p.X, p.Y] for p in a[2]],
                        "lado_m": round(size, 4),
                        "area_m2": round(area, 4),
                        "claridad_m": round(claridad, 4),
                    })

                if aceptados:
                    anclas = ", ".join("V{}".format(a[3]) for a in aceptados)
                    areas = ", ".join("{:.2f}".format(p["area_m2"]) for p in patios_export)
                    clars = ", ".join("{:.2f}".format(p["claridad_m"]) for p in patios_export)
                    if modo == "auto":
                        cabecera = ("PATIO v03.3 | modo AUTO | n_volumenes inferido: {} "
                                    "(esquinas validas: {} | capacidad: {} @ {:.0f} m2)").format(
                            n_vol, n_validos, capacidad, A_REF_VOL_M2)
                    else:
                        cabecera = "PATIO v03.3 | modo MULTI (n_volumenes={})".format(n_vol)
                    mensaje = (cabecera + " | Verts {}->{} | Lados: {} | "
                               "Generados: {}/{} | Anclas: {} | Areas: {} m2 | Claridades: {} m | "
                               "Modo: esquinas_interiores_v1").format(
                        n_vertices_brutos, n, ", ".join(cats),
                        patio_count, n_vol, anclas, areas, clars)
                    mensaje += nota
                    mensaje += " | v03.3: conteo de patios NO equivale a cuerpos; altura usada {:.2f} m".format(altura_max)
                    if patio_count < n_vol:
                        mensaje += " | Nota: menos patios que el objetivo (revisar esquinas)"
                    if descartes:
                        mensaje += " | Descartes: " + "; ".join(descartes[:3])
                else:
                    if modo == "auto":
                        cabecera = ("PATIO v03.3 | modo AUTO | n_volumenes inferido: 0 "
                                    "(esquinas validas: 0 | capacidad: {})").format(capacidad)
                    else:
                        cabecera = "PATIO v03.3 | modo MULTI (n_volumenes={})".format(n_vol)
                    mensaje = (cabecera + " | Verts {}->{} | Lados: {} | Generados: 0 | Motivo: {}").format(
                        n_vertices_brutos, n, ", ".join(cats),
                        "; ".join(descartes[:4]) if descartes else "sin esquinas interiores elegibles")

            # Advertencia si IO excede el máximo (regla aprobada 2026-10-03)
            # El patio no es la herramienta de reducción de IO; la reducción
            # viene con barras por crujía (F3_DISTRIBUCION_v03).
            if aceptados and altura_max > 0:
                # Estimación simple de IO: area_patios / area_lote
                # (Solo informativo; la validación real es en NORMATIVA v09)
                pass

            # v02.4/v03.0: export del diagnostico si el servidor/orquestador lo solicito
            try:
                ruta_diag = _exportar_diagnostico(sides_data, patios_export, mensaje, modo, n_vol)
                if ruta_diag:
                    mensaje += " | Lados export OK: {}".format(ruta_diag)
            except Exception as _e_exp:
                mensaje += " | Lados export aviso: {}".format(str(_e_exp))

    except Exception as e:
        mensaje = "PATIO v03.3 | ERROR: {}".format(str(e))