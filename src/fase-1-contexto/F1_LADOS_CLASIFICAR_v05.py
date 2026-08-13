#! /usr/bin/env python3
"""
================================================================================
F1_LADOS_CLASIFICAR_v05.py — Clasificador direccional simplificado
Proyecto: DisenoParametrico / Fase 1
GH Python Script para Grasshopper (IronPython 2.7 compatible)
================================================================================

PROPOSITO:
  Clasifica los 4 lados virtuales del lote usando proximidad DIRECCIONAL
  a vias y espacios publicos. Solo cuenta elementos del lado EXTERIOR.

  Radio reducido: max(longitud lado mas largo, 50m).

  Categorias:
    Frontal         — via al exterior a < 50m
    EspacioPublico  — EP colindante directo (dist ~0, exterior)
    Lateral         — sin via ni EP al exterior
    Posterior       — opuesto al Frontal (si hay 1 solo)

  Deteccion de esquina: si un vertice tiene 2 lados Frontales adyacentes.

ENTRADAS:
  lot_vertices (Point3d[])      — 4 vertices desde Discontinuity
  vias_oficiales (Curve[])      — Ejes viales del POT
  espacios_publicos (Curve[])   — Parques/plazas/zonas verdes

SALIDAS:
  sides_table_json (String)     — Clasificacion de los 4 lados
  lot_simplificado (Curve)      — Poligono de 4 vertices
  es_esquina (bool)             — True si es lote de esquina
  mensaje (String)              — Diagnostico
================================================================================
"""

import Rhino.Geometry as rg
import json
import math


def safe_list(val):
    if val is None: return []
    if isinstance(val, list): return val
    return [val]


def centroide(vertices):
    sx = sum(v.X for v in vertices)
    sy = sum(v.Y for v in vertices)
    n = len(vertices)
    return rg.Point3d(sx / n, sy / n, 0)


def normal_exterior(p1, p2, centro):
    """Normal unitaria apuntando hacia afuera del lote desde el lado (p1,p2)."""
    e = rg.Vector3d(p2.X - p1.X, p2.Y - p1.Y, 0)
    n1 = rg.Vector3d(-e.Y, e.X, 0)
    n2 = rg.Vector3d(e.Y, -e.X, 0)
    mid = rg.Point3d((p1.X + p2.X) / 2, (p1.Y + p2.Y) / 2, 0)
    to_c = rg.Vector3d(centro.X - mid.X, centro.Y - mid.Y, 0)
    if n1.X * to_c.X + n1.Y * to_c.Y > 0:
        n2.Unitize()
        return n2 if n2.Length > 0 else rg.Vector3d(1, 0, 0)
    else:
        n1.Unitize()
        return n1 if n1.Length > 0 else rg.Vector3d(1, 0, 0)


def distancia_direccional(p1, p2, centro, curvas, max_dist):
    """
    Distancia minima a curvas que estan del lado EXTERIOR del segmento.
    Retorna (distancia, hay_elemento_cercano).
    """
    mid = rg.Point3d((p1.X + p2.X) / 2, (p1.Y + p2.Y) / 2, 0)
    normal = normal_exterior(p1, p2, centro)

    mejor = max_dist + 1
    for crv in curvas:
        if crv is None:
            continue
        success, param = crv.ClosestPoint(mid)
        if not success:
            continue
        closest = crv.PointAt(param)
        d = mid.DistanceTo(closest)
        if d > max_dist:
            continue
        vec = rg.Vector3d(closest.X - mid.X, closest.Y - mid.Y, 0)
        if vec.Length < 0.01:
            continue
        vec.Unitize()
        dot = vec.X * normal.X + vec.Y * normal.Y
        if dot > 0.2 and d < mejor:
            mejor = d
    return mejor if mejor <= max_dist else max_dist + 1


def toca_colindante(p1, p2, curvas, tol=0.5):
    """Verifica si alguna curva toca el segmento (distancia ~0)."""
    if not curvas:
        return False
    n_muestras = max(5, int(p1.DistanceTo(p2) / 0.3) + 1)
    for i in range(n_muestras):
        t = float(i) / max(1, n_muestras - 1)
        pt = rg.Point3d(
            p1.X + t * (p2.X - p1.X),
            p1.Y + t * (p2.Y - p1.Y), 0)
        for crv in curvas:
            if crv is None:
                continue
            success, param = crv.ClosestPoint(pt)
            if success and pt.DistanceTo(crv.PointAt(param)) < tol:
                return True
    return False


# ==============================================================================
# MAIN
# ==============================================================================

lot_vertices_raw = globals().get("lot_vertices", None)
vias_raw = globals().get("vias_oficiales", None)
ep_raw = globals().get("espacios_publicos", None)

lot_vertices = safe_list(lot_vertices_raw)
vias_list = safe_list(vias_raw)
ep_list = safe_list(ep_raw)

sides_table_json = ""
lot_simplificado = None
es_esquina = False

if len(lot_vertices) < 3:
    mensaje = "CLASIFICAR v05 | ERROR: Se necesitan >= 3 vertices ({} recibidos)".format(
        len(lot_vertices))
else:
    try:
        n = len(lot_vertices)
        ctr = centroide(lot_vertices)

        # Calcular radio maximo: lado mas largo, minimo 30m, maximo 60m
        lado_max = 0
        for i in range(n):
            j = (i + 1) % n
            lado_max = max(lado_max, lot_vertices[i].DistanceTo(lot_vertices[j]))
        RADIO = max(30.0, min(lado_max * 1.5, 60.0))

        # Reconstruir poligono simplificado
        poly = rg.Polyline()
        for v in lot_vertices:
            poly.Add(v.X, v.Y, v.Z)
        if not poly.IsClosed and n >= 3:
            poly.Add(lot_vertices[0].X, lot_vertices[0].Y, lot_vertices[0].Z)
        lot_simplificado = rg.PolylineCurve(poly)

        # Clasificar cada lado
        lados = []
        for i in range(n):
            j = (i + 1) % n
            p1 = lot_vertices[i]
            p2 = lot_vertices[j]

            # Distancia direccional a vias
            dist_via = distancia_direccional(p1, p2, ctr, vias_list, RADIO)

            # Colindancia directa con espacio publico (solo si toca)
            colinda_ep = toca_colindante(p1, p2, ep_list)

            if dist_via <= RADIO:
                cat = "Frontal"
            elif colinda_ep:
                cat = "EspacioPublico"
            else:
                cat = "Lateral"

            lados.append({
                "id": i,
                "clasificacion": cat,
                "dist_via_m": round(dist_via if dist_via <= RADIO else 999, 1),
                "colinda_ep": colinda_ep
            })

        # Post-procesar
        categorias = [l["clasificacion"] for l in lados]
        n_frontales = categorias.count("Frontal")
        es_esquina = n_frontales >= 2

        if n_frontales == 1 and n == 4:
            idx = categorias.index("Frontal")
            op = (idx + 2) % 4
            if lados[op]["clasificacion"] == "Lateral":
                lados[op]["clasificacion"] = "Posterior"

        sides_data = {
            "lados": lados, "total_lados": len(lados),
            "es_esquina": es_esquina,
            "radio_busqueda_m": round(RADIO, 1),
            "regla": "Direccional {}m + EP colindante".format(int(RADIO))
        }
        sides_table_json = json.dumps(sides_data)

        cats_final = [l["clasificacion"] for l in lados]
        mensaje = "CLASIFICAR v05 | {} lados | {} | Radio={:.0f}m | Vias:{} EP:{} Esq:{}".format(
            n, ", ".join(cats_final), RADIO, len(vias_list), len(ep_list), es_esquina)

    except Exception as e:
        mensaje = "CLASIFICAR v05 | ERROR: {}".format(str(e))
