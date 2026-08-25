"""
================================================================================
F1_ETAPA2_LADOS_v06.py — Algoritmo Vertice A / Vertice N + Regla Posterior
                            + Clasificacion por vertices/contacto minimo
                            + Ancho de via TOTAL (perfil vial)
Proyecto: DisenoParametrico / Fase 1
GH Python Script para Grasshopper (IronPython 2.7 compatible)
================================================================================

ALGORITMO (definido por el usuario, 2026-08-15):
  1. Para cada vertice del lote simplificado, calcular la distancia minima
     a las vias que afectan el lote (via A, via B, via C...).
  2. VERTICE A = el vertice con MENOR distancia a las vias (el frente).
  3. VERTICE N = el vertice con MAYOR distancia a las MISMAS vias
     (el punto mas alejado de las vias del frente).
  4. Los lados se clasifican (v06, usuario 2026-08-16):
       a. LATERAL por VERTICES COINCIDENTES con vecinos: si los DOS extremos
          del lado coinciden (< 0.10 m) con vertices de predios vecinos (uno
          o varios vecinos por el mismo lado), el lado es Lateral. La
          medianeria gana aunque haya una via cerca sin contacto fisico.
       b. Los demas lados se clasifican por CONTACTO MINIMO (fraccion del
          lado a < tol >= 0.30) con prioridad:
            - Contacto con via  -> Frontal
            - Contacto con EP   -> EspacioPublico
            - Contacto vecino  -> Lateral
          Una via a 4.75 m separada por zona verde NO genera contacto.
       c. ESQUINA (Esq): 2+ vertices a < 0.10 m de una via o zona verde
          (contacto real; ya NO el umbral de 15 m).
  5. REGLA POSTERIOR (nueva en v03, mantenida en v04/v05):
       El lado Posterior existe SOLAMENTE cuando TODOS los lados menos uno
       colindan con predios vecinos. De ahi sale el patio en esquina.
       - Si el unico lado sin vecino es una via o EP: el Posterior es el
         lado OPUESTO (el lado con vecino mas lejano perpendicularmente
         al frente).
       - Si el unico lado sin vecino no es ni via ni EP (lado libre):
         ese lado es el Posterior.
       - Si hay 2+ lados sin vecino: NO existe lado Posterior
         (caso del lote de prueba: 1 frontal + 1 EP + 2 laterales -> sin
         posterior, confirmado por el usuario 2026-08-15).
  6. ANCHO DE VIA TOTAL DEL PERFIL VIAL (nuevo en v05, usuario 2026-08-16):
       El ancho de via NO es la distancia de la calzada entre andenes: es
       el ancho TOTAL de la via incluyendo los andenes (distancia entre
       paramentos / bordes opuestos del espacio publico de la via).
       Los ANDENES son irrelevantes para el antejardin.
       Medicion: para cada lado FRONTAL, muestrear el lado del lote; en
       cada muestra tomar el POLIGONO DE VIA mas cercano (el que toca el
       lado) y lanzar una linea larga perpendicular hacia AFUERA del lote;
       la primera interseccion con el borde OPUESTO del poligono de via
       (d > MIN_ANCHO_VIA_M) es el ancho total. Promediar las muestras.
       Ventaja: usa las vias (poligonos rectos ya cableados) y NO depende
       de los andenes (polilineas con arcos) -> se elimina esa fuente de
       problemas.

  El vertice N es el ORIGEN del patio (se desarrolla sobre los lados
  laterales que lo comparten).

ENTRADAS:
  lot_vertices (Point3d[])     — vertices desde Discontinuity
  vias_curves (Curve[])        — POLIGONOS de vias (capa 00-20-20 / seleccion
                                 manual; el perfil completo incluye andenes)
  ep_curves (Curve[])          — Zonas verdes (capa 70-50-10)
  vecinos_curves (Curve[])     — Perimetros vecinos (capa 70-20-20)
  andenes_curves (Curve[])     — OBSOLETA para medicion (v05: el ancho es
                                 total de la via, no entre andenes); se
                                 recibe solo con fines informativos
  tol_colindancia_m (Number, OPCIONAL) — Tolerancia de colindancia [m]
                              (default 0.5; bajar p.ej. a 0.2 si hay
                              elementos cercanos que no colindan)
  contacto_min_frac (Number, OPCIONAL) — Fraccion minima del lado con
                              contacto para clasificar (default 0.30)
  lado_via_setback_override_json (String, OPCIONAL) — JSON array de objetos
                              {side_id: int, has_setback: bool} para override
                              manual de setback en lados que limitan con vía
                              (default: ninguno, compatibilidad hacia atrás)

SALIDAS:
  sides_table_json (String) — Clasificacion + vertice_a + vertice_n +
                              ancho_via_m por lado frontal
  lot_simplificado (Curve)  — Poligono de vertices
  es_esquina (bool)         — True si hay 2+ vertices frontales
  ancho_via_m (Number)      — Ancho TOTAL de la via del frente [m]
                              (0.0 si no se pudo medir)
  mensaje (String)          — Diagnostico

VERSIONES:
  v06 (2026-08-16) - Clasificacion por VERTICES COINCIDENTES con vecinos
                     (< 0.10 m) para laterales + CONTACTO MINIMO por longitud
                     (fraccion >= 0.30) para via/EP/vecino + ESQUINA por
                     contacto real (< 0.10 m con via o EP). Entrada
                     contacto_min_frac. Mensaje con detalle por lado
                     (distancias, fracciones, motivo).
  v06.2 (2026-08-23) - Nomenclatura cardinal por lado (Norte/Oriente/Sur/
                       Occidente, normal saliente; misma convencion que
                       NORMATIVA_v08 y vecinos_por_lado.py) en el mensaje y
                       el JSON. Guard de ancho de via absurdo (>100m).
  v06.1 (2026-08-17) - Cada lado emite dx/dy/mx/my (direccion + punto medio)
                       del lado, insumo para F3 (colocacion del nucleo contra
                       la medianera sin depender del orden de lote_vertices).
  v06.3 (2026-08-24) - Override manual de setback por lado que limita con vía
                       para controlar exactamente qué lados tienen retiro
                       según regulaciones UPZ/UPL específicas.
  v05 (2026-08-16) - Ancho de via TOTAL del perfil vial (poligono de via,
                     incluye andenes). Los andenes dejan de usarse para
                     medir. Renombrado desde v04 por cambio de concepto.
  v04 (2026-08-15) - Entrada andenes_curves + medicion del ancho ENTRE
                     andenes (concepto corregido en v05). Type hint Curve,
                     CurveLine, IntersectionEvent.PointA.
  v03 (2026-08-15) - Regla Posterior N-1 (usuario + Anexo 5 POT). El
                     posterior ya NO se asigna por heuristica comparte_n:
                     solo existe cuando todos los lados menos uno colindan
                     con vecinos; lado opuesto por distancia perpendicular
                     a la recta del frente.
  v02 (2026-08-12) - Prioridad colindancia real > heuristica A/N.
  v01 - Primera version.
================================================================================
"""

import Rhino.Geometry as rg
import json
import math

TOL_COLINDANCIA_M = 0.5
RADIO_VIA_M = 50.0
# v06: coincidencia de vertices con vecinos (laterales) y contacto real
# de esquina con via/EP
TOL_VERTICES_COINC_M = 0.10
# v06: fraccion minima del lado con contacto para clasificar
CONTACTO_MIN_FRACCION = 0.30
# Intersecciones de linea mas cercanas que esto se ignoran (borde propio/ruido)
MIN_ANCHO_VIA_M = 0.5
# v06.2: ancho de via absurdo (>100m) indica geometria en otro frame de
# coordenadas; se descarta la muestra para no propagar el error a NORMATIVA.
MAX_ANCHO_VIA_M = 100.0
MUESTRAS_ANCHO = 7

# v06.2 - Nomenclatura cardinal (misma convencion que NORMATIVA_v08 y
# vecinos_por_lado.py): Norte/Oriente/Sur/Occidente desde la normal saliente.
CARDINAL_BANDS = [
    ("Norte", 315.0, 45.0),
    ("Oriente", 45.0, 135.0),
    ("Sur", 135.0, 225.0),
    ("Occidente", 225.0, 315.0),
]


def _cardinal_normal(nx, ny):
    """v06.2 - Cardinal desde una normal (azimut = atan2(nx,ny) % 360)."""
    if nx == 0.0 and ny == 0.0:
        return "Norte"
    az = math.degrees(math.atan2(nx, ny)) % 360.0
    for name, lo, hi in CARDINAL_BANDS:
        if lo <= hi:
            if lo <= az < hi:
                return name
        else:
            if az >= lo or az < hi:
                return name
    return "Norte"


def _cardinal_lado(dx, dy, mx, my, cx, cy):
    """v06.2 - Cardinal de un lado (normal saliente respecto al centroide)."""
    n1 = (-dy, dx)
    n2 = (dy, -dx)
    vx = mx - cx
    vy = my - cy
    d1 = vx * n1[0] + vy * n1[1]
    d2 = vx * n2[0] + vy * n2[1]
    nx, ny = (n1 if d1 >= d2 else n2)
    return _cardinal_normal(nx, ny)


def safe_list(val):
    if val is None: return []
    if isinstance(val, list): return val
    return [val]


def es_curva(obj):
    """True si el objeto parece una curva de Rhino (tiene ClosestPoint)."""
    return obj is not None and hasattr(obj, "ClosestPoint")


# Metodos de conversion candidatos para objetos de la Live Connection
# (p.ej. 'Planar Curve' con arcos) que no exponen ClosestPoint directo.
METODOS_CONVERSION = ("ToCurve", "ToNurbsCurve", "ToPolylineCurve",
                      "ToGeometryBase", "AsCurve", "GetGeometry",
                      "ToCurveWithArcs", "ToPolyline")


def convertir_a_curva(obj):
    """Intenta convertir un objeto de la Live Connection a curva nativa.

    El Deconstruct de la Live Connection emite clases del plugin (p.ej.
    'Planar Curve' para polilineas con arcos) que pueden no exponer
    ClosestPoint directamente pero si un metodo de conversion.
    Retorna la curva nativa o None si no se pudo convertir.
    """
    if es_curva(obj):
        return obj
    for nombre in METODOS_CONVERSION:
        fn = getattr(obj, nombre, None)
        if callable(fn):
            try:
                r = fn()
                if es_curva(r):
                    return r
            except Exception:
                pass
    return None


def filtrar_curvas(items, nombre, avisos):
    """Filtra/valida curvas; intenta convertir objetos del plugin; reporta.

    Los componentes de la Grasshopper-ArchiCAD Live Connection
    (AC_PolylineDeconstruct, AC_GetElements) emiten clases propias (p.ej.
    'Planar Curve' cuando la polilinea trae arcos) que pueden no ser curvas
    nativas de Rhino. Se intenta la conversion automatica; si falla, se
    reporta el tipo .NET del primer item descartado.
    """
    ok = []
    descartados = 0
    tipo_1er = ""
    for it in safe_list(items):
        c = convertir_a_curva(it)
        if c is not None:
            ok.append(c)
        else:
            descartados += 1
            if not tipo_1er:
                try:
                    tipo_1er = it.GetType().Name
                except Exception:
                    tipo_1er = type(it).__name__
    if descartados:
        avisos.append(
            "entrada %s: %d item(s) NO convertibles a curva nativa; tipo del 1er "
            "item: %s. Solucion: conectar la salida C del Deconstruct DIRECTO a la "
            "entrada del script con Type hint = Curve + List Access + Flatten "
            "(GHPython convierte a Rhino.Geometry.Curve); NO reconstruir con "
            "Explode/PolyLine (el parametro Polyline de Params produce "
            "Rhino.Geometry.Polyline sin ClosestPoint)"
            % (nombre, descartados, tipo_1er))
    return ok


def distancia_vertice_a_curvas(vertice, curvas, max_dist):
    """Distancia minima del vertice a las curvas (si < max_dist)."""
    mejor = max_dist + 1
    for crv in curvas:
        if crv is None:
            continue
        success, param = crv.ClosestPoint(vertice)
        if success:
            d = vertice.DistanceTo(crv.PointAt(param))
            if d < mejor:
                mejor = d
    return mejor


def dist_min_lado_a_curvas(p1, p2, curvas):
    """Distancia minima del lado a las curvas (mismo muestreo de colindancia).

    -1.0 si no hay curvas en esa categoria. Sirve de diagnostico para saber
    POR QUE un lado se marca (o no) como colindante.
    """
    mejor = None
    long_seg = p1.DistanceTo(p2)
    muestras = max(5, int(long_seg / 0.2) + 1)
    for i in range(muestras):
        t = float(i) / max(1, muestras - 1)
        pt = rg.Point3d(p1.X + t * (p2.X - p1.X),
                        p1.Y + t * (p2.Y - p1.Y), 0)
        for crv in curvas:
            if crv is None:
                continue
            ok, param = crv.ClosestPoint(pt)
            if ok:
                d = pt.DistanceTo(crv.PointAt(param))
                if mejor is None or d < mejor:
                    mejor = d
    return mejor if mejor is not None else -1.0


def min_dist_pt_a_curvas(pt, curvas):
    """Distancia minima del punto a la categoria (None si no hay curvas)."""
    mejor = None
    for crv in curvas:
        if crv is None:
            continue
        ok, t0 = crv.ClosestPoint(pt)
        if ok:
            d = pt.DistanceTo(crv.PointAt(t0))
            if mejor is None or d < mejor:
                mejor = d
    return mejor


def vertices_de_curva(crv):
    """Vertices de una curva (ToPolyline; fallback TryGetPolyline)."""
    pts = []
    try:
        poly = crv.ToPolyline(0.01)
        if poly is not None:
            for i in range(poly.Count):
                pts.append(poly[i])
    except Exception:
        pts = []
    if not pts:
        try:
            ok, poly = crv.TryGetPolyline()
            if ok and poly is not None:
                for i in range(poly.Count):
                    pts.append(poly[i])
        except Exception:
            pts = []
    return pts


def lado_lateral_por_vertices(p1, p2, vecinos_list):
    """True si AMBOS extremos del lado coinciden (< 0.10 m) con vertices
    de predios vecinos (uno o varios vecinos por el mismo lado: cada extremo
    puede coincidir con un vecino distinto).

    v06 (usuario 2026-08-16): la colindancia con vecino se decide por la
    coincidencia de los vertices del predio con los vertices del vecino
    (distancia < 0.10 m), sin muestreo.
    """
    p1_ok = False
    p2_ok = False
    for crv in vecinos_list:
        for v in vertices_de_curva(crv):
            if not p1_ok and p1.DistanceTo(v) < TOL_VERTICES_COINC_M:
                p1_ok = True
            if not p2_ok and p2.DistanceTo(v) < TOL_VERTICES_COINC_M:
                p2_ok = True
            if p1_ok and p2_ok:
                return True
    return False


def fracciones_contacto(p1, p2, vias, eps, vecinos, tol=None):
    """Fraccion (0..1) del lado a menos de tol de cada categoria.

    Muestreo cada ~0.2 m (una sola pasada para las tres categorias).
    Retorna (frac_via, frac_ep, frac_vec).
    """
    if tol is None:
        tol = TOL_COLINDANCIA_M
    long_seg = p1.DistanceTo(p2)
    muestras = max(5, int(long_seg / 0.2) + 1)
    c_v = 0
    c_e = 0
    c_n = 0
    total = 0
    for i in range(muestras):
        t = float(i) / max(1, muestras - 1)
        pt = rg.Point3d(p1.X + t * (p2.X - p1.X),
                        p1.Y + t * (p2.Y - p1.Y), 0)
        d_v = min_dist_pt_a_curvas(pt, vias)
        d_e = min_dist_pt_a_curvas(pt, eps)
        d_n = min_dist_pt_a_curvas(pt, vecinos)
        if d_v is not None and d_v < tol:
            c_v += 1
        if d_e is not None and d_e < tol:
            c_e += 1
        if d_n is not None and d_n < tol:
            c_n += 1
        total += 1
    if total == 0:
        return 0.0, 0.0, 0.0
    return (float(c_v) / total, float(c_e) / total, float(c_n) / total)


def vertice_toca_via_o_ep(v, vias, eps):
    """True si el vertice esta a < 0.10 m de una via o zona verde
    (contacto real; reemplaza el umbral de 15 m para ESQUINA)."""
    for crv in vias:
        ok, t0 = crv.ClosestPoint(v)
        if ok and v.DistanceTo(crv.PointAt(t0)) < TOL_VERTICES_COINC_M:
            return True
    for crv in eps:
        ok, t0 = crv.ClosestPoint(v)
        if ok and v.DistanceTo(crv.PointAt(t0)) < TOL_VERTICES_COINC_M:
            return True
    return False


def punto_medio_lado(vertices, i):
    """Punto medio del lado i (vertices en orden, cerrado)."""
    n = len(vertices)
    j = (i + 1) % n
    p1 = vertices[i]
    p2 = vertices[j]
    return rg.Point3d((p1.X + p2.X) / 2.0, (p1.Y + p2.Y) / 2.0, 0)


def distancia_punto_medio_a_recta_lado(vertices, iu, k):
    """Distancia del punto medio del lado k a la RECTA del lado iu (el frente).

    Identifica el lado de fondo: el mas lejano PERPENDICULARMENTE al frente.
    Mas robusto que la distancia entre puntos medios: en lotes con frente
    largo, los laterales quedan mas lejos del punto medio del frente que el
    fondo (rectangulo 26x12: laterales a 14.3m vs fondo a 12m), y la
    distancia punto-recta elige correctamente el fondo (12m).
    """
    n = len(vertices)
    a = vertices[iu]
    b = vertices[(iu + 1) % n]
    pm = punto_medio_lado(vertices, k)
    dx = b.X - a.X
    dy = b.Y - a.Y
    L = math.sqrt(dx * dx + dy * dy)
    if L < 1e-9:
        return pm.DistanceTo(a)
    # distancia perpendicular del punto a la recta: |cruz| / |dir|
    return abs(dx * (a.Y - pm.Y) - dy * (a.X - pm.X)) / L


def punto_interseccion(ev):
    """Punto del evento de interseccion, compatible con Rhino 7 y 8.

    Rhino 8: IntersectionEvent.PointA (y PointB).
    Rhino 7 / clases legacy: CurveIntersection.IntersectionPoint.
    Retorna None si no se pudo extraer.
    """
    for nombre in ("PointA", "IntersectionPoint"):
        try:
            p = getattr(ev, nombre)
            if p is not None:
                return p
        except Exception:
            pass
    return None


def medir_ancho_via_total(lot_vertices, lados, vias_list, muestras=MUESTRAS_ANCHO):
    """Mide el ANCHO TOTAL de la via (perfil vial completo) para cada lado FRONTAL.

    Concepto (usuario 2026-08-16): el ancho de via NO es la calzada entre
    andenes; es el ancho total incluyendo los andenes (distancia entre los
    bordes opuestos del espacio publico de la via). Los andenes son
    irrelevantes para el antejardin.

    Algoritmo:
      1. Muestrear el lado frontal del lote.
      2. Para cada muestra: el POLIGONO DE VIA mas cercano (el que toca el
         lado) y su punto q1.
      3. Desde q1, linea larga perpendicular al poligono orientado hacia
         AFUERA del lote (alejandose del centroide); la primera interseccion
         con d > MIN_ANCHO_VIA_M es el borde OPUESTO del poligono de via =
         ancho total.
      4. Promediar las muestras.

    Retorna (anchos_por_lado {id_lado: ancho}, ancho_promedio_frentes).
    """
    anchos_por_lado = {}
    if not vias_list:
        return anchos_por_lado, 0.0

    n = len(lot_vertices)
    if n == 0:
        return anchos_por_lado, 0.0
    cx = sum(v.X for v in lot_vertices) / n
    cy = sum(v.Y for v in lot_vertices) / n

    for lado in lados:
        if lado.get("clasificacion") != "Frontal":
            continue
        i = lado["id"]
        j = (i + 1) % n
        p1 = lot_vertices[i]
        p2 = lot_vertices[j]
        long_seg = p1.DistanceTo(p2)
        if long_seg < 0.01:
            continue

        muestras_ok = max(3, muestras)
        anchos_lado = []
        for k in range(muestras_ok):
            t = float(k) / max(1, muestras_ok - 1)
            p = rg.Point3d(p1.X + t * (p2.X - p1.X),
                           p1.Y + t * (p2.Y - p1.Y), 0)

            # POLIGONO DE VIA mas cercano (el que toca el lado)
            mejor_d = 1e18
            mejor_crv = None
            mejor_t = 0.0
            for crv in vias_list:
                ok, t0 = crv.ClosestPoint(p)
                if ok:
                    d = p.DistanceTo(crv.PointAt(t0))
                    if d < mejor_d:
                        mejor_d = d
                        mejor_crv = crv
                        mejor_t = t0

            # La via debe estar pegada al lote (borde del poligono ~ en el lote)
            if mejor_crv is None or mejor_d > max(TOL_COLINDANCIA_M * 2.0, 1.0):
                continue

            tang = mejor_crv.TangentAt(mejor_t)
            if tang.Length < 0.001:
                continue

            # NORMAL al poligono, orientada hacia AFUERA del lote
            nrm = rg.Vector3d(-tang.Y, tang.X, 0)
            nrm.Unitize()
            hacia_fuera = rg.Vector3d(p.X - cx, p.Y - cy, 0)
            if nrm.X * hacia_fuera.X + nrm.Y * hacia_fuera.Y < 0:
                nrm = rg.Vector3d(-nrm.X, -nrm.Y, 0)

            pt_fin = rg.Point3d(p.X + nrm.X * 500.0, p.Y + nrm.Y * 500.0, 0)
            linea = rg.Line(p, pt_fin)

            ancho_muestra = None
            eventos = rg.Intersect.Intersection.CurveLine(
                mejor_crv, linea, 0.001, 0.001)
            if eventos:
                distancias = []
                for ev in eventos:
                    pt_int = punto_interseccion(ev)
                    if pt_int is None:
                        continue
                    d = p.DistanceTo(pt_int)
                    if d > MIN_ANCHO_VIA_M:  # Only consider intersections sufficiently far from p
                        distancias.append(d)
                # We need at least two intersection points to measure width (entry and exit)
                if len(distancias) >= 2:
                    distancias.sort()
                    # Width = distance between first and second intersection (entry and exit)
                    ancho_muestra = distancias[1] - distancias[0]
                # If we have 0 or 1 intersection, we can't measure width
            if ancho_muestra is not None and ancho_muestra <= MAX_ANCHO_VIA_M:
                # Also check that the measured width is reasonable
                anchos_lado.append(ancho_muestra)

        if anchos_lado:
            anchos_por_lado[lado["id"]] = sum(anchos_lado) / len(anchos_lado)

    if not anchos_por_lado:
        return anchos_por_lado, 0.0
    promedio = sum(anchos_por_lado.values()) / len(anchos_por_lado)
    return anchos_por_lado, promedio


# ==============================================================================
# MAIN
# ==============================================================================

lot_vertices_raw = globals().get("lot_vertices", None)
vias_raw = globals().get("vias_curves", None)
ep_raw = globals().get("ep_curves", None)
vecinos_raw = globals().get("vecinos_curves", None)
andenes_raw = globals().get("andenes_curves", None)

# Tolerancia de colindancia configurable (entrada opcional; default 0.5 m)
_tol_in = globals().get("tol_colindancia_m", None)
try:
    TOL_COLINDANCIA_M = float(_tol_in) if _tol_in else 0.5
except Exception:
    TOL_COLINDANCIA_M = 0.5

# Fraccion minima de contacto configurable (entrada opcional; default 0.30)
_frac_in = globals().get("contacto_min_frac", None)
try:
    CONTACTO_MIN_FRACCION = float(_frac_in) if _frac_in else 0.30
except Exception:
    CONTACTO_MIN_FRACCION = 0.30

# Lado via setback override (opcional) - JSON array de objetos {side_id: int, has_setback: bool}
_lado_override_in = globals().get("lado_via_setback_override_json", None)
lado_override_dict = {}
if _lado_override_in is not None:
    try:
        override_list = json.loads(_lado_override_in)
        if isinstance(override_list, list):
            for item in override_list:
                if isinstance(item, dict) and "side_id" in item and "has_setback" in item:
                    side_id = int(item["side_id"])
                    has_setback = bool(item["has_setback"])
                    lado_override_dict[side_id] = has_setback
                # Ignore items malformados
    except Exception:
        # Si falla el parsing JSON, ignorar overrides (compatibilidad hacia atrás)
        pass

lot_vertices = safe_list(lot_vertices_raw)

# v04: filtrar Guids / no-curvas (cables de Tapir mal conectados) sin crashear
avisos = []
vias_list = filtrar_curvas(vias_raw, "vias_curves", avisos)
ep_list = filtrar_curvas(ep_raw, "ep_curves", avisos)
vecinos_list = filtrar_curvas(vecinos_raw, "vecinos_curves", avisos)
# v05: andenes OBSOLETOS para la medicion (el ancho es total de la via);
# se reciben solo con fines informativos (conteo), sin filtrar.
andenes_list = safe_list(andenes_raw)

sides_table_json = ""
lot_simplificado = None
es_esquina = False
ancho_via_m = 0.0

# Guarda defensiva (v04): detecta Access Type incorrecto en el canvas.
# Con 'Item Access', GH ejecuta el script UNA vez por item -> mensaje repetido
# y salidas null. Las entradas geometricas deben ir en List Access + Flatten
# (regla 13 de CLAUDE.md).
if lot_vertices_raw is not None and not isinstance(lot_vertices_raw, list):
    mensaje = ("LADOS v06 | CONFIG: entradas en 'Item Access'. Clic derecho en "
               "CADA input geometrico (lot_vertices, vias_curves, ep_curves, "
               "vecinos_curves, andenes_curves) -> List Access + Flatten.")
elif len(lot_vertices) < 3:
    mensaje = "LADOS v06.2 | ERROR: Se necesitan >= 3 vertices ({} recibidos)".format(
        len(lot_vertices))
else:
    try:
        n = len(lot_vertices)
        cx = sum(v.X for v in lot_vertices) / n
        cy = sum(v.Y for v in lot_vertices) / n

        # Reconstruir poligono simplificado
        poly = rg.Polyline()
        for v in lot_vertices:
            poly.Add(v.X, v.Y, v.Z)
        if not poly.IsClosed and n >= 3:
            poly.Add(lot_vertices[0].X, lot_vertices[0].Y, lot_vertices[0].Z)
        lot_simplificado = rg.PolylineCurve(poly)

        # PASO 1: distancia de cada vertice a las vias
        dist_vertices = []
        for v in lot_vertices:
            d = distancia_vertice_a_curvas(v, vias_list, RADIO_VIA_M)
            dist_vertices.append(d)

        # PASO 2 y 3: Vertice A (min distancia) y Vertice N (max distancia)
        idx_a = dist_vertices.index(min(dist_vertices))
        idx_n = dist_vertices.index(max(dist_vertices))
        vertice_a = idx_a
        vertice_n = idx_n

        # Detectar esquina: vertices con CONTACTO REAL (< 0.10 m) con via o EP
        # (v06: ya NO el umbral de 15 m — una via a 4.75 m separada por zona
        # verde no genera esquina)
        vertices_contacto = [i for i, v in enumerate(lot_vertices)
                             if vertice_toca_via_o_ep(v, vias_list, ep_list)]
        es_esquina = len(vertices_contacto) >= 2

        # PASO 4: clasificar lados — v06: laterales por VERTICES COINCIDENTES
        # con vecinos (< 0.10 m) + contacto por LONGITUD MINIMA (fraccion >= 0.30)
        lados = []
        for i in range(n):
            j = (i + 1) % n
            p1 = lot_vertices[i]
            p2 = lot_vertices[j]

            comparte_a = (i == idx_a or j == idx_a)
            comparte_n = (i == idx_n or j == idx_n)

            # Diagnostico: distancia minima del lado a cada categoria
            d_v = dist_min_lado_a_curvas(p1, p2, vias_list)
            d_e = dist_min_lado_a_curvas(p1, p2, ep_list)
            d_n = dist_min_lado_a_curvas(p1, p2, vecinos_list)

            motivo_lado = ""
            # 4a) Lateral por VERTICES COINCIDENTES con vecinos (< 0.10 m):
            #     la medianeria gana aunque haya una via cerca sin contacto
            if lado_lateral_por_vertices(p1, p2, vecinos_list):
                toca_via = False
                toca_ep = False
                toca_vecino = True
                cat = "Lateral"
                motivo_lado = "vertices coincidentes con vecino"
                f_v = 0.0
                f_e = 0.0
                f_n = 1.0
            else:
                # 4b) Contacto por LONGITUD MINIMA (fraccion del lado)
                f_v, f_e, f_n = fracciones_contacto(
                    p1, p2, vias_list, ep_list, vecinos_list)
                toca_via = f_v >= CONTACTO_MIN_FRACCION
                toca_ep = f_e >= CONTACTO_MIN_FRACCION
                toca_vecino = f_n >= CONTACTO_MIN_FRACCION
                if toca_via:
                    cat = "Frontal"
                    motivo_lado = "contacto via {:.0%}".format(f_v)
                elif toca_ep:
                    cat = "EspacioPublico"
                    motivo_lado = "contacto EP {:.0%}".format(f_e)
                elif toca_vecino:
                    cat = "Lateral"
                    motivo_lado = "contacto vecino {:.0%}".format(f_n)
                else:
                    cat = "Lateral"  # provisional; la regla posterior puede reclasificar
                    motivo_lado = "sin contacto minimo"

            lados.append({
                "id": i,
                "clasificacion": cat,
                "motivo": motivo_lado,
                "frac_via_m": round(f_v, 3),
                "frac_ep_m": round(f_e, 3),
                "frac_vec_m": round(f_n, 3),
                "f_v": f_v,
                "f_e": f_e,
                "f_n": f_n,
                "toca_via": toca_via,
                "toca_ep": toca_ep,
                "toca_vecino": toca_vecino,
                "dist_via_m": round(d_v, 2) if d_v >= 0 else None,
                "dist_ep_m": round(d_e, 2) if d_e >= 0 else None,
                "dist_vec_m": round(d_n, 2) if d_n >= 0 else None,
                "dist_v_m": round(dist_vertices[i], 2),
                "comparte_a": comparte_a,
                "comparte_n": comparte_n,
                # v06.2: cardinal del lado (normal saliente, nomenclatura
                # orquestador); v06.1: direccion + punto medio (insumo F3)
                "cardinal": _cardinal_lado(p2.X - p1.X, p2.Y - p1.Y,
                                           (p1.X + p2.X) / 2.0,
                                           (p1.Y + p2.Y) / 2.0, cx, cy),
                "dx": round(p2.X - p1.X, 4),
                "dy": round(p2.Y - p1.Y, 4),
                "mx": round((p1.X + p2.X) / 2.0, 4),
                "my": round((p1.Y + p2.Y) / 2.0, 4)
            })

        # PASO 5: REGLA POSTERIOR
        # El Posterior existe SOLO cuando TODOS los lados menos uno colindan
        # con vecinos (usuario 2026-08-15 + Anexo 5 POT).
        lados_sin_vecino = [i for i, l in enumerate(lados) if not l["toca_vecino"]]
        idx_posterior = None
        motivo_posterior = ""

        if len(lados_sin_vecino) == 1:
            iu = lados_sin_vecino[0]
            if not (lados[iu]["toca_via"] or lados[iu]["toca_ep"]):
                # Unico lado sin vecino y sin via/EP: es el Posterior
                idx_posterior = iu
                motivo_posterior = "unico lado libre"
            else:
                # Unico lado sin vecino es via o EP (el frente): el Posterior
                # es el lado con vecino MAS LEJANO del frente (perpendicular)
                mejor_d = -1.0
                for i, l in enumerate(lados):
                    if l["toca_vecino"]:
                        d = distancia_punto_medio_a_recta_lado(lot_vertices, iu, i)
                        if d > mejor_d:
                            mejor_d = d
                            idx_posterior = i
                motivo_posterior = "opuesto al unico frente (N-1 vecinos)"
        elif len(lados_sin_vecino) > 1:
            # Varios lados sin vecino: posterior solo si hay UN lado libre
            libres = [i for i in lados_sin_vecino
                      if not (lados[i]["toca_via"] or lados[i]["toca_ep"])]
            if len(libres) == 1:
                idx_posterior = libres[0]
                motivo_posterior = "unico lado libre entre varios sin vecino"

        # CORRECCION ESQUINA (2026-08-23): en lote de esquina NO existe
        # lado Posterior. Solo el frente lleva antejardin; la esquina
        # interior (union de dos colindantes) lleva patio 3x3 (PATIO).
        # Se anula el posterior que la regla N-1 hubiera asignado.
        if es_esquina:
            idx_posterior = None
        if idx_posterior is not None:
            lados[idx_posterior]["clasificacion"] = "Posterior"

        # APLICAR OVERRIDES DE SETBACK PARA LADOS QUE LIMITAN CON VIA
        # Solo aplica a lados que tienen toca_via = True (limitan con via)
        for l in lados:
            side_id = l["id"]
            # Solo considerar overrides para lados que limitan con via
            if l.get("toca_via", False) and side_id in lado_override_dict:
                override_has_setback = lado_override_dict[side_id]
                if override_has_setback:
                    # Forzar que el lado tenga setback
                    # Si ya es Frontal o Posterior, mantener su tipo de setback
                    # Si no, asignar como Frontal para setback (antejardin)
                    current_tipo = l["aislamiento_tipo"]
                    if current_tipo not in ["antejardin", "posterior"]:
                        l["aislamiento_tipo"] = "antejardin"
                        # También actualizar clasificacion a Frontal para consistencia
                        l["clasificacion"] = "Frontal"
                        l["motivo"] = l["motivo"] + " (override: setback forcado)"
                else:
                    # Forzar que el lado NO tenga setback
                    l["aislamiento_tipo"] = "lateral"
                    # Cambiar clasificacion a Lateral (a menos que sea EP, pero si toca via, probablemente no es EP)
                    l["clasificacion"] = "Lateral"
                    l["motivo"] = l["motivo"] + " (override: setback desactivado)"

        # ETAPA v02 (2026-08-15): Etiqueta de aislamiento normativo por clasificacion
        # (insumo NORMATIVA)
        for l in lados:
            c = l["clasificacion"]
            if c == "Frontal":
                l["aislamiento_tipo"] = "antejardin"
            elif c == "Lateral":
                l["aislamiento_tipo"] = "lateral"
            elif c == "Posterior":
                l["aislamiento_tipo"] = "posterior"
            else:
                l["aislamiento_tipo"] = "cero"

        # PASO 6 (v05): ANCHO TOTAL DE LA VIA (perfil vial completo)
        anchos_por_lado, ancho_promedio = medir_ancho_via_total(
            lot_vertices, lados, vias_list)

        # El ancho del frente principal (el que comparte el vertice A) manda;
        # si no hay, el promedio de los frentes.
        ancho_via_m = 0.0
        if anchos_por_lado:
            principal = None
            for l in lados:
                if l["clasificacion"] == "Frontal" and l["comparte_a"]:
                    principal = l["id"]
                    break
            if principal is not None and principal in anchos_por_lado:
                ancho_via_m = anchos_por_lado[principal]
            else:
                ancho_via_m = ancho_promedio

        # Volcar ancho por lado al JSON
        for l in lados:
            l["ancho_via_m"] = round(anchos_por_lado.get(l["id"], 0.0), 2)

        sides_data = {
            "lados": lados,
            "total_lados": len(lados),
            "vertice_a": vertice_a,
            "vertice_n": vertice_n,
            "distancias_vertices": [round(d, 2) for d in dist_vertices],
            "distancias_por_lado": [
                {"id": l["id"], "via_m": l.get("dist_via_m"),
                 "ep_m": l.get("dist_ep_m"), "vec_m": l.get("dist_vec_m")}
                for l in lados],
            "es_esquina": es_esquina,
            "ancho_via_m": round(ancho_via_m, 2),
            "regla": "Vertice A/N + laterales por vertices coincidentes + contacto minimo + Posterior N-1 + ancho total de via (v06)"
        }
        sides_table_json = json.dumps(sides_data)

        cats_final = [l["clasificacion"] for l in lados]

        def fmt_dist(x):
            return "na" if x is None else "{:.2f}".format(x)

        detalle = "; ".join(
            "{}[L{}]=[{} aisl:{} v:{} ep:{} vec:{} fr:{}/{}/{} ({})]".format(
                l.get("cardinal", "?"), l["id"], l["clasificacion"], l["aislamiento_tipo"],
                fmt_dist(l.get("dist_via_m")),
                fmt_dist(l.get("dist_ep_m")),
                fmt_dist(l.get("dist_vec_m")),
                l.get("frac_via_m"), l.get("frac_ep_m"), l.get("frac_vec_m"),
                l.get("motivo", ""))
            for l in lados)

        mensaje = "LADOS v06.2 | A=V{} N=V{} | {} | Esq:{} | Posterior:{} ({}) | Vias:{} EP:{} Vec:{} Andenes:{} | Ancho via: {:.2f}m | Detalle: {}".format(
            vertice_a, vertice_n, ", ".join(cats_final),
            es_esquina,
            "SI" if idx_posterior is not None else "NO",
            motivo_posterior if idx_posterior is not None else "regla N-1 no aplica; patio en V{} via PATIO_v02".format(vertice_n),
            len(vias_list), len(ep_list), len(vecinos_list), len(andenes_list),
            ancho_via_m, detalle)

        if avisos:
            mensaje += " | AVISOS: " + "; ".join(avisos)

    except Exception as e:
        mensaje = "LADOS v06.2 | ERROR: {}".format(str(e))