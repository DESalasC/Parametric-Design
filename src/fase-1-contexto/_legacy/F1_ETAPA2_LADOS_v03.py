"""
================================================================================
F1_ETAPA2_LADOS_v03.py — Algoritmo Vertice A / Vertice N + Regla Posterior
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
  5. REGLA POSTERIOR v03 (nueva):
       El lado Posterior existe SOLAMENTE cuando TODOS los lados menos uno
       colindan con predios vecinos. De ahi sale el patio en esquina.
       - Si el unico lado sin vecino es una via o EP: el Posterior es el
         lado OPUESTO (el lado con vecino mas lejano a ese frente).
       - Si el unico lado sin vecino no es ni via ni EP (lado libre):
         ese lado es el Posterior.
       - Si hay 2+ lados sin vecino: NO existe lado Posterior
         (caso del lote de prueba: 1 frontal + 1 EP + 2 laterales -> sin
         posterior, confirmado por el usuario 2026-08-15).
  6. Fallback: lado que comparte el vertice A sin colindancia detectada
     -> Frontal (heuristica residual de v02).

  El vertice N es el ORIGEN del patio (se desarrolla sobre los lados
  laterales que lo comparten).

ENTRADAS:
  lot_vertices (Point3d[])     — vertices desde Discontinuity
  vias_curves (Curve[])        — Ejes de vias (capa 00-20-30 / seleccion manual)
  ep_curves (Curve[])          — Zonas verdes (capa 70-50-10)
  vecinos_curves (Curve[])     — Perimetros vecinos (capa 70-20-20)

SALIDAS:
  sides_table_json (String) — Clasificacion + vertice_a + vertice_n
  lot_simplificado (Curve)  — Poligono de vertices
  es_esquina (bool)         — True si hay 2+ vertices frontales
  mensaje (String)          — Diagnostico

VERSIONES:
  v03 (2026-08-15) - Regla Posterior nueva (N-1 lados con vecino). El
                     posterior ya NO se asigna por heuristica comparte_n:
                     solo existe cuando todos los lados menos uno colindan
                     con vecinos (definido por el usuario + Anexo 5 POT).
  v02 (2026-08-12) - Prioridad colindancia real > heuristica A/N.
  v01 - Primera version.
================================================================================
"""

import Rhino.Geometry as rg
import json
import math

TOL_COLINDANCIA_M = 0.5
RADIO_VIA_M = 50.0


def safe_list(val):
    if val is None: return []
    if isinstance(val, list): return val
    return [val]


def curva_toca_segmento(p1, p2, curva, tol=TOL_COLINDANCIA_M):
    """Verifica si una curva toca el segmento (muestreo denso)."""
    if curva is None:
        return False
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


def distancia_entre_lados(vertices, i, k):
    """Distancia entre los puntos medios de los lados i y k."""
    return punto_medio_lado(vertices, i).DistanceTo(punto_medio_lado(vertices, k))


# ==============================================================================
# MAIN
# ==============================================================================

lot_vertices_raw = globals().get("lot_vertices", None)
vias_raw = globals().get("vias_curves", None)
ep_raw = globals().get("ep_curves", None)
vecinos_raw = globals().get("vecinos_curves", None)

lot_vertices = safe_list(lot_vertices_raw)
vias_list = safe_list(vias_raw)
ep_list = safe_list(ep_raw)
vecinos_list = safe_list(vecinos_raw)

sides_table_json = ""
lot_simplificado = None
es_esquina = False

if len(lot_vertices) < 3:
    mensaje = "LADOS v03 | ERROR: Se necesitan >= 3 vertices ({} recibidos)".format(
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
        UMBRAL_FRONTAL = 15.0
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
                "dist_v_m": round(dist_vertices[i], 2),
                "comparte_a": comparte_a,
                "comparte_n": comparte_n
            })

        # PASO 5: REGLA POSTERIOR v03
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

        sides_data = {
            "lados": lados,
            "total_lados": len(lados),
            "vertice_a": vertice_a,
            "vertice_n": vertice_n,
            "distancias_vertices": [round(d, 2) for d in dist_vertices],
            "es_esquina": es_esquina,
            "regla": "Vertice A/N + colindancia real + Posterior N-1 (v03)"
        }
        sides_table_json = json.dumps(sides_data)

        cats_final = [l["clasificacion"] for l in lados]
        mensaje = "LADOS v03 | A=V{} N=V{} | {} | Esq:{} | Posterior:{} ({}) | Vias:{} EP:{} Vec:{}".format(
            vertice_a, vertice_n, ", ".join(cats_final),
            es_esquina,
            "SI" if idx_posterior is not None else "NO",
            motivo_posterior if idx_posterior is not None else "regla N-1 no aplica",
            len(vias_list), len(ep_list), len(vecinos_list))

    except Exception as e:
        mensaje = "LADOS v03 | ERROR: {}".format(str(e))
