"""
================================================================================
F1_ETAPA2_LADOS_v04.py — Algoritmo Vertice A / Vertice N + Regla Posterior
                            + Ancho de via entre andenes
Proyecto: DisenoParametrico / Fase 1
GH Python Script para Grasshopper (IronPython 2.7 compatible)
================================================================================

ALGORITMO (definido por el usuario, 2026-08-15):
  1. Para cada vertice del lote simplificado, calcular la distancia minima
     a las vias que afectan el lote (via A, via B, via C...).
  2. VERTICE A = el vertice con MENOR distancia a las vias (el frente).
  3. VERTICE N = el vertice con MAYOR distancia a las MISMAS vias
     (el punto mas alejado de las vias del frente).
  4. Los lados se clasifican por COLINDANCIA REAL con prioridad:
       - Toca via            -> Frontal
       - Toca espacio publico-> EspacioPublico
       - Toca vecino         -> Lateral
  5. REGLA POSTERIOR (nueva en v03, mantenida en v04):
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
  6. ANCHO DE VIA ENTRE ANDENES (nuevo en v04, usuario 2026-08-15):
       Entrada nueva: andenes_curves (Curve[], capa 70-30-20_Andenes_
       preexistentes). Para cada lado FRONTAL:
         a. Muestrear el lado del lote.
         b. Para cada muestra: el ANDEN MAS CERCANO al predio (el anden del
            lado del lote) y su punto q1.
         c. En q1, la NORMAL al anden (perpendicular); lanzar un rayo en
            ambas direcciones y tomar la interseccion mas cercana con OTRO
            anden (el anden opuesto).
         d. distancia(q1, q2) = ancho de via en esa muestra.
         e. Promediar las muestras por lado frontal.
       Salida: ancho_via_m (Number) = ancho del frente principal (el lado
       que comparte el vertice A) o el promedio de los frentes.

  El vertice N es el ORIGEN del patio (se desarrolla sobre los lados
  laterales que lo comparten).

ENTRADAS:
  lot_vertices (Point3d[])     — vertices desde Discontinuity
  vias_curves (Curve[])        — Ejes de vias (capa 00-20-30 / seleccion manual)
  ep_curves (Curve[])          — Zonas verdes (capa 70-50-10)
  vecinos_curves (Curve[])     — Perimetros vecinos (capa 70-20-20)
  andenes_curves (Curve[])     — Andenes (capa 70-30-20_Andenes_preexistentes)
  tol_colindancia_m (Number, OPCIONAL) — Tolerancia de colindancia [m]
                              (default 0.5; bajar p.ej. a 0.2 si hay
                              elementos cercanos que no colindan)

SALIDAS:
  sides_table_json (String) — Clasificacion + vertice_a + vertice_n +
                              ancho_via_m por lado frontal
  lot_simplificado (Curve)  — Poligono de vertices
  es_esquina (bool)         — True si hay 2+ vertices frontales
  ancho_via_m (Number)      — Ancho de via del frente entre andenes [m]
                              (0.0 si no se pudo medir)
  mensaje (String)          — Diagnostico

VERSIONES:
  v04 (2026-08-15) - Entrada andenes_curves + medicion del ancho de via
                     entre andenes (puntos de la via mas cercanos al predio
                     + puntos perpendiculares al anden opuesto). Salida
                     ancho_via_m para NORMATIVA_v05 (antejardin por ancho).
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
UMBRAL_FRONTAL = 15.0
# Si el anden mas cercano queda a mas de este umbral, no es el anden del lote
MAX_DIST_ANDEN_LOTE_M = 15.0
# Intersecciones de rayo mas cercanas que esto se ignoran (mismo anden/ruido)
MIN_ANCHO_VIA_M = 0.5
MUESTRAS_ANCHO = 7


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


def curva_toca_segmento(p1, p2, curva, tol=None):
    """Verifica si una curva toca el segmento (muestreo denso)."""
    if curva is None:
        return False
    if tol is None:
        tol = TOL_COLINDANCIA_M
    long_seg = p1.DistanceTo(p2)
    muestras = max(5, int(long_seg / 0.2) + 1)
    for i in range(muestras):
        t = float(i) / max(1, muestras - 1)
        pt = rg.Point3d(p1.X + t * (p2.X - p1.X),
                        p1.Y + t * (p2.Y - p1.Y), 0)
        success, param = curva.ClosestPoint(pt)
        if success:
            closest = curva.PointAt(param)
            if pt.DistanceTo(closest) < tol:
                return True
    return False


def lado_colindante(p1, p2, curvas):
    for crv in curvas:
        if crv is not None and curva_toca_segmento(p1, p2, crv):
            return True
    return False


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


def medir_ancho_via_andenes(lot_vertices, lados, andenes_list, muestras=MUESTRAS_ANCHO):
    """Mide el ancho de via entre andenes para cada lado FRONTAL.

    Algoritmo (usuario 2026-08-15):
      1. Muestrear el lado frontal del lote.
      2. Para cada muestra: el ANDEN MAS CERCANO (el del lado del lote) y
         su punto q1.
      3. En q1, la NORMAL al anden (perpendicular); lanzar rayo en ambas
         direcciones y tomar la interseccion mas cercana con OTRO anden.
      4. distancia(q1, q2) = ancho de via en esa muestra; promediar.

    Retorna (anchos_por_lado {id_lado: ancho}, ancho_promedio_frentes).
    """
    anchos_por_lado = {}
    if not andenes_list or len(andenes_list) < 2:
        return anchos_por_lado, 0.0

    n = len(lot_vertices)
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

            # ANDEN MAS CERCANO al predio (el anden del lado del lote)
            mejor_d = 1e18
            mejor_crv = None
            mejor_t = 0.0
            for crv in andenes_list:
                ok, t0 = crv.ClosestPoint(p)
                if ok:
                    d = p.DistanceTo(crv.PointAt(t0))
                    if d < mejor_d:
                        mejor_d = d
                        mejor_crv = crv
                        mejor_t = t0

            if mejor_crv is None or mejor_d > MAX_DIST_ANDEN_LOTE_M:
                continue  # no hay anden junto al lote en esta muestra

            q1 = mejor_crv.PointAt(mejor_t)
            tang = mejor_crv.TangentAt(mejor_t)
            if tang.Length < 0.001:
                continue

            # NORMAL al anden (perpendicular 2D); probar ambas direcciones
            nrm = rg.Vector3d(-tang.Y, tang.X, 0)
            nrm.Unitize()
            nrm_op = rg.Vector3d(tang.Y, -tang.X, 0)
            dists = []
            for dirv in (nrm, nrm_op):
                # Linea suficientemente larga en la direccion de la normal
                # (equivalente al rayo, mas robusto en IronPython GH)
                pt_fin = q1 + dirv * 500.0
                linea = rg.Line(q1, pt_fin)
                for crv in andenes_list:
                    if crv is mejor_crv:
                        continue
                    eventos = rg.Intersect.Intersection.CurveLine(
                        crv, linea, 0.001, 0.001)
                    if eventos:
                        pt_int = punto_interseccion(eventos[0])
                        if pt_int is not None:
                            d = q1.DistanceTo(pt_int)
                            if d > MIN_ANCHO_VIA_M:
                                dists.append(d)
            if dists:
                anchos_lado.append(min(dists))

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

lot_vertices = safe_list(lot_vertices_raw)

# v04: filtrar Guids / no-curvas (cables de Tapir mal conectados) sin crashear
avisos = []
vias_list = filtrar_curvas(vias_raw, "vias_curves", avisos)
ep_list = filtrar_curvas(ep_raw, "ep_curves", avisos)
vecinos_list = filtrar_curvas(vecinos_raw, "vecinos_curves", avisos)
andenes_list = filtrar_curvas(andenes_raw, "andenes_curves", avisos)

sides_table_json = ""
lot_simplificado = None
es_esquina = False
ancho_via_m = 0.0

# Guarda defensiva (v04): detecta Access Type incorrecto en el canvas.
# Con 'Item Access', GH ejecuta el script UNA vez por item -> mensaje repetido
# y salidas null. Las entradas geometricas deben ir en List Access + Flatten
# (regla 13 de CLAUDE.md).
if lot_vertices_raw is not None and not isinstance(lot_vertices_raw, list):
    mensaje = ("LADOS v04 | CONFIG: entradas en 'Item Access'. Clic derecho en "
               "CADA input geometrico (lot_vertices, vias_curves, ep_curves, "
               "vecinos_curves, andenes_curves) -> List Access + Flatten.")
elif len(lot_vertices) < 3:
    mensaje = "LADOS v04 | ERROR: Se necesitan >= 3 vertices ({} recibidos)".format(
        len(lot_vertices))
else:
    try:
        n = len(lot_vertices)

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

        # Detectar esquina: vertices con distancia < umbral frontal
        vertices_frontales = [i for i, d in enumerate(dist_vertices) if d < UMBRAL_FRONTAL]
        es_esquina = len(vertices_frontales) >= 2

        # PASO 4: clasificar lados por colindancia real
        lados = []
        for i in range(n):
            j = (i + 1) % n
            p1 = lot_vertices[i]
            p2 = lot_vertices[j]

            comparte_a = (i == idx_a or j == idx_a)
            comparte_n = (i == idx_n or j == idx_n)

            toca_via = lado_colindante(p1, p2, vias_list)
            toca_ep = lado_colindante(p1, p2, ep_list)
            toca_vecino = lado_colindante(p1, p2, vecinos_list)

            # Diagnostico: distancia minima del lado a cada categoria
            d_v = dist_min_lado_a_curvas(p1, p2, vias_list)
            d_e = dist_min_lado_a_curvas(p1, p2, ep_list)
            d_n = dist_min_lado_a_curvas(p1, p2, vecinos_list)

            if toca_via:
                cat = "Frontal"
            elif toca_ep:
                cat = "EspacioPublico"
            elif toca_vecino:
                cat = "Lateral"
            else:
                cat = "Lateral"  # provisional; la regla posterior puede reclasificar

            lados.append({
                "id": i,
                "clasificacion": cat,
                "toca_via": toca_via,
                "toca_ep": toca_ep,
                "toca_vecino": toca_vecino,
                "dist_via_m": round(d_v, 2) if d_v >= 0 else None,
                "dist_ep_m": round(d_e, 2) if d_e >= 0 else None,
                "dist_vec_m": round(d_n, 2) if d_n >= 0 else None,
                "dist_v_m": round(dist_vertices[i], 2),
                "comparte_a": comparte_a,
                "comparte_n": comparte_n
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

        if idx_posterior is not None:
            lados[idx_posterior]["clasificacion"] = "Posterior"

        # PASO 6: fallback v02 — lado del frente sin colindancia detectada
        for l in lados:
            if l["clasificacion"] == "Lateral" and l["comparte_a"] and not l["toca_vecino"]:
                l["clasificacion"] = "Frontal"

        # PASO 7 (v04): ANCHO DE VIA ENTRE ANDENES (capa 70-30-20)
        anchos_por_lado, ancho_promedio = medir_ancho_via_andenes(
            lot_vertices, lados, andenes_list)

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
            "regla": "Vertice A/N + colindancia real + Posterior N-1 + ancho entre andenes (v04)"
        }
        sides_table_json = json.dumps(sides_data)

        cats_final = [l["clasificacion"] for l in lados]
        mensaje = "LADOS v04 | A=V{} N=V{} | {} | Esq:{} | Posterior:{} ({}) | Vias:{} EP:{} Vec:{} Andenes:{} | Ancho via: {:.2f}m".format(
            vertice_a, vertice_n, ", ".join(cats_final),
            es_esquina,
            "SI" if idx_posterior is not None else "NO",
            motivo_posterior if idx_posterior is not None else "regla N-1 no aplica; patio en V{} via PATIO_v02".format(vertice_n),
            len(vias_list), len(ep_list), len(vecinos_list), len(andenes_list),
            ancho_via_m)

        if avisos:
            mensaje += " | AVISOS: " + "; ".join(avisos)

    except Exception as e:
        mensaje = "LADOS v04 | ERROR: {}".format(str(e))
