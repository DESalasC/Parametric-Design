"""
================================================================================
F1_ETAPA2_LADOS_v02.py — Algoritmo Vertice A / Vertice N
Proyecto: DisenoParametrico / Fase 1
GH Python Script para Grasshopper (IronPython 2.7 compatible)
================================================================================

ALGORITMO (definido por el usuario, 2026-08-12):
  1. Para cada vertice del lote simplificado, calcular la distancia minima
     a las vias que afectan el lote (via A, via B, via C...).
  2. VERTICE A = el vertice con MENOR distancia a las vias (el frente).
  3. VERTICE N = el vertice con MAYOR distancia a las MISMAS vias
     (el punto mas alejado de las vias del frente).
  4. Los lados simplificados que comparten el vertice N se clasifican por
     COLINDANCIA con predios vecinos:
       - Colindan con vecino  -> Lateral
       - Colindan con zona verde/EP -> EspacioPublico
       - No colindan con nada -> Posterior
  5. Los lados que comparten el vertice A -> Frontal (si dan a via)
  6. Los lados restantes se clasifican por colindancia real.

  El vertice N es el ORIGEN del patio (se desarrolla sobre los lados
  laterales que lo comparten).

ENTRADAS:
  lot_vertices (Point3d[])     — 4 vertices desde Discontinuity
  vias_curves (Curve[])        — Ejes de vias (capa 00-20-30)
  ep_curves (Curve[])          — Zonas verdes (capa 70-50-10)
  vecinos_curves (Curve[])     — Perimetros vecinos (capa 70-20-20)

SALIDAS:
  sides_table_json (String) — Clasificacion + vertice_a + vertice_n
  lot_simplificado (Curve)  — Poligono de 4 vertices
  es_esquina (bool)         — True si hay 2+ vertices frontales
  mensaje (String)          — Diagnostico
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
    mensaje = "LADOS v02 | ERROR: Se necesitan >= 3 vertices ({} recibidos)".format(
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

        # PASO 4-6: clasificar lados
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

            # Prioridad: colindancia REAL > heuristica de vertices
            if toca_via:
                cat = "Frontal"
            elif toca_ep:
                cat = "EspacioPublico"
            elif toca_vecino:
                cat = "Lateral"
            elif comparte_a:
                cat = "Frontal"   # lado del frente sin colindancia detectada
            elif comparte_n:
                cat = "Posterior"
            else:
                cat = "Lateral"

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

        # Post-procesar: si 1 solo Frontal, el opuesto es Posterior SOLO si
        # no colinda con vecino (si tiene vecino, sigue siendo Lateral)
        categorias = [l["clasificacion"] for l in lados]
        n_frontales = categorias.count("Frontal")
        if n_frontales == 1 and n == 4:
            idx_frontal = categorias.index("Frontal")
            idx_op = (idx_frontal + 2) % 4
            if lados[idx_op]["clasificacion"] == "Lateral" and not lados[idx_op]["toca_vecino"]:
                lados[idx_op]["clasificacion"] = "Posterior"

        sides_data = {
            "lados": lados,
            "total_lados": len(lados),
            "vertice_a": vertice_a,
            "vertice_n": vertice_n,
            "distancias_vertices": [round(d, 2) for d in dist_vertices],
            "es_esquina": es_esquina,
            "regla": "Vertice A/N + colindancia real"
        }
        sides_table_json = json.dumps(sides_data)

        cats_final = [l["clasificacion"] for l in lados]
        mensaje = "LADOS v02 | A=V{} N=V{} | {} | Esq:{} | Vias:{} EP:{} Vec:{}".format(
            vertice_a, vertice_n, ", ".join(cats_final),
            es_esquina, len(vias_list), len(ep_list), len(vecinos_list))

    except Exception as e:
        mensaje = "LADOS v02 | ERROR: {}".format(str(e))
