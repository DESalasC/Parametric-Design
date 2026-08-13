#! /usr/bin/env python3
"""
================================================================================
F1_LADOS_CLASIFICAR_v04.py — Clasificador direccional (4 categorias)
Proyecto: DisenoParametrico / Fase 1
GH Python Script para Grasshopper (IronPython 2.7 compatible)
================================================================================

PROPOSITO:
  Recibe los 4 vertices principales del lote (Discontinuity) y clasifica
  cada lado virtual usando CRITERIO DIRECCIONAL:
  - Solo cuenta la via/parque si esta del lado EXTERIOR del lote
  - Evita que vias del otro lado de la manzana clasifiquen un borde

  Categorias:
    1. Frontal         — lado que da a una VIA (exterior, < 15m)
    2. EspacioPublico  — lado COLINDANTE DIRECTO con parque/plaza
    3. Lateral         — lado que da a vecino (sin via/EP proxima)
    4. Posterior       — lado opuesto al Frontal (si hay 1 solo)

ENTRADAS:
  lot_vertices (Point3d[])      — 4 vertices desde Discontinuity
  vias (Curve[])                — Curvas de via (oficiales + manuales)
  espacios_publicos (Curve[])   — Poligonos de parques/plazas/zonas verdes

SALIDAS:
  sides_table_json (String) — JSON con clasificacion (4 lados)
  lot_simplificado (Curve)  — Poligono reconstruido de 4 vertices
  mensaje (String)          — Diagnostico

NORMATIVA:
  ADR-008 — Clasificacion Espacial Hibrida (direccional)
================================================================================
"""

import Rhino.Geometry as rg
import json
import math

DISTANCIA_FRENTE_M = 15.0
TOL_EP_M = 0.01


def unwrap(val):
    if val is None: return None
    if isinstance(val, list): return val[0] if len(val) > 0 else None
    return val


def safe_list(val):
    if val is None: return []
    if isinstance(val, list): return val
    return [val]


def centroide(vertices):
    """Centroide 2D de los vertices."""
    sx = sum(v.X for v in vertices)
    sy = sum(v.Y for v in vertices)
    n = len(vertices)
    return rg.Point3d(sx / n, sy / n, 0)


def normal_exterior(p1, p2, centro):
    """Vector normal unitario apuntando hacia afuera del lote."""
    edge = rg.Vector3d(p2.X - p1.X, p2.Y - p1.Y, 0)
    # Perpendicular (rotar 90 grados antihorario)
    n1 = rg.Vector3d(-edge.Y, edge.X, 0)
    n2 = rg.Vector3d(edge.Y, -edge.X, 0)
    # Vector del punto medio hacia el centro
    mid = rg.Point3d((p1.X + p2.X) / 2, (p1.Y + p2.Y) / 2, 0)
    to_center = rg.Vector3d(centro.X - mid.X, centro.Y - mid.Y, 0)
    # La normal exterior apunta en direccion contraria al centro
    if n1.X * to_center.X + n1.Y * to_center.Y > 0:
        n1.Unitize()
        return n2.Unitize() if n2.Length > 0 else n1
    else:
        n2.Unitize()
        return n1.Unitize() if n1.Length > 0 else n2


def esta_al_exterior(p1, p2, centro, curva):
    """
    Verifica si la curva esta del lado EXTERIOR del segmento (p1,p2).
    Retorna (esta_fuera, distancia_minima).
    """
    if curva is None:
        return False, float('inf')

    mid = rg.Point3d((p1.X + p2.X) / 2, (p1.Y + p2.Y) / 2, 0)
    normal_ext = normal_exterior(p1, p2, centro)

    # Punto mas cercano de la curva al segmento
    # Muestrear el segmento
    long_seg = p1.DistanceTo(p2)
    muestras = max(3, int(long_seg / 0.5) + 1)
    min_dist = float('inf')
    mejor_dot = -1

    for i in range(muestras):
        t = float(i) / max(1, muestras - 1)
        pt = rg.Point3d(
            p1.X + t * (p2.X - p1.X),
            p1.Y + t * (p2.Y - p1.Y),
            p1.Z + t * (p2.Z - p1.Z))

        success, param = curva.ClosestPoint(pt)
        if success:
            closest = curva.PointAt(param)
            d = pt.DistanceTo(closest)
            if d < min_dist:
                min_dist = d
                # Vector desde el punto medio del lado hacia el punto en la via
                vec_to_via = rg.Vector3d(closest.X - mid.X, closest.Y - mid.Y, 0)
                if vec_to_via.Length > 0.01:
                    vec_to_via.Unitize()
                    mejor_dot = vec_to_via.X * normal_ext.X + vec_to_via.Y * normal_ext.Y

    # Esta al exterior si el vector hacia la via apunta en direccion de la normal
    esta_fuera = mejor_dot > 0.3  # ~72 grados de tolerancia
    return esta_fuera, min_dist


# ==============================================================================
# MAIN
# ==============================================================================

lot_vertices_raw = globals().get("lot_vertices", None)
vias_raw = globals().get("vias", None)
ep_raw = globals().get("espacios_publicos", None)

lot_vertices = safe_list(lot_vertices_raw)
vias_list = safe_list(vias_raw)
ep_list = safe_list(ep_raw)

sides_table_json = ""
lot_simplificado = None

if len(lot_vertices) < 3:
    mensaje = "CLASIFICAR v04 | ERROR: Se necesitan >= 3 vertices (recibidos: {})".format(
        len(lot_vertices))
else:
    try:
        n = len(lot_vertices)
        ctr = centroide(lot_vertices)

        # Reconstruir poligono simplificado
        poly = rg.Polyline()
        for v in lot_vertices:
            poly.Add(v.X, v.Y, v.Z)
        if not poly.IsClosed and n >= 3:
            poly.Add(lot_vertices[0].X, lot_vertices[0].Y, lot_vertices[0].Z)
        lot_simplificado = rg.PolylineCurve(poly)

        # Clasificar cada lado con criterio direccional
        lados = []
        for i in range(n):
            j = (i + 1) % n
            p1 = lot_vertices[i]
            p2 = lot_vertices[j]

            # 1. Vias: solo si estan al exterior
            dist_via = float('inf')
            for via in vias_list:
                fuera, d = esta_al_exterior(p1, p2, ctr, via)
                if fuera and d < dist_via:
                    dist_via = d

            # 2. Espacios publicos: solo si estan al exterior
            dist_ep = float('inf')
            for ep in ep_list:
                fuera, d = esta_al_exterior(p1, p2, ctr, ep)
                if fuera and d < dist_ep:
                    dist_ep = d

            # 3. Clasificar
            if dist_via < DISTANCIA_FRENTE_M:
                cat = "Frontal"
            elif dist_ep <= TOL_EP_M:
                cat = "EspacioPublico"
            else:
                cat = "Lateral"

            lados.append({
                "id": i,
                "vertice_inicio": i,
                "vertice_fin": j,
                "distancia_min_a_via": round(dist_via if dist_via != float('inf') else 999, 2),
                "distancia_min_a_ep": round(dist_ep if dist_ep != float('inf') else 999, 2),
                "clasificacion": cat
            })

        # Post-procesar: si solo 1 lado es Frontal, el opuesto es Posterior
        categorias = [l["clasificacion"] for l in lados]
        n_frontales = categorias.count("Frontal")
        if n_frontales == 1 and n == 4:
            idx_frontal = categorias.index("Frontal")
            idx_posterior = (idx_frontal + 2) % 4
            if lados[idx_posterior]["clasificacion"] == "Lateral":
                lados[idx_posterior]["clasificacion"] = "Posterior"

        sides_data = {"lados": lados, "total_lados": len(lados), "regla": "ADR-008 15m + EP (direccional)"}
        sides_table_json = json.dumps(sides_data)

        cats_final = [l["clasificacion"] for l in lados]
        mensaje = "CLASIFICAR v04 | {} vertices -> {} lados | {} | Vias:{} EP:{}".format(
            n, len(lados), ", ".join(cats_final), len(vias_list), len(ep_list))

    except Exception as e:
        mensaje = "CLASIFICAR v04 | ERROR: {}".format(str(e))
