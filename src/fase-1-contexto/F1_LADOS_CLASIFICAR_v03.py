#! /usr/bin/env python3
"""
================================================================================
F1_LADOS_CLASIFICAR_v03.py — Clasificador 4 categorias (incluye EspacioPublico)
Proyecto: DisenoParametrico / Fase 1
GH Python Script para Grasshopper (IronPython 2.7 compatible)
================================================================================

PROPOSITO:
  Recibe los 4 vertices principales del lote (Discontinuity) y clasifica
  cada lado virtual en UNA de 4 categorias:

    1. Frontal         — lado a < 15m de una VIA → APLICA retiro frontal
    2. EspacioPublico  — lado COLINDANTE DIRECTO con parque/plaza/zona verde
                          (distancia = 0, no hay franja intermedia) → NO APLICA retiro
    3. Lateral         — lado colindante con vecino → APLICA retiro lateral
    4. Posterior       — lado opuesto al Frontal (si 1 solo Frontal) → APLICA retiro posterior

  NOTA: Si entre el lote y el espacio publico hay una franja (via, anden, etc.),
  la distancia sera > 0 y el lado se clasifica como Lateral o Frontal segun
  corresponda — la exencion de retiro NO aplica.

  El lado occidental de AAA0127AZPA esta sobre zona verde publica (entre el lote
  y la Carrera 49). Segun norma: sobre parque/espacio publico NO aplica retiro
  ni aislamiento → clasificacion "EspacioPublico".

ENTRADAS:
  lot_vertices (Point3d[])      — 4 vertices desde Discontinuity
  vias (Curve[])                — Curvas de via (oficiales + manuales)
  espacios_publicos (Curve[])   — Poligonos de parques/plazas/zonas verdes

SALIDAS:
  sides_table_json (String) — JSON con clasificacion (4 lados)
  lot_simplificado (Curve)  — Poligono reconstruido de 4 vertices
  mensaje (String)          — Diagnostico

NORMATIVA:
  ADR-008 — Clasificacion Espacial Hibrida
  Regla: distancia minima lado→via < 15m → Frontal
         distancia minima lado→espacio_publico < 15m → EspacioPublico
         resto → Lateral
         opuesto al Frontal → Posterior
================================================================================
"""

import Rhino.Geometry as rg
import json
import math

DISTANCIA_FRENTE_M = 15.0
TOL_EP_M = 0.01  # Tolerancia para colindancia directa con espacio publico


def unwrap(val):
    if val is None: return None
    if isinstance(val, list): return val[0] if len(val) > 0 else None
    return val


def safe_list(val):
    if val is None: return []
    if isinstance(val, list): return val
    return [val]


def distancia_minima_segmento_polilineas(p1, p2, polylines):
    """
    Distancia minima entre el segmento (p1,p2) y una lista de polilineas.
    Muestrea puntos a lo largo del segmento y busca el mas cercano.
    """
    if not polylines:
        return float('inf')

    longitud = p1.DistanceTo(p2)
    muestras = max(3, int(longitud / 0.5) + 1)

    min_dist = float('inf')
    for i in range(muestras):
        t = float(i) / max(1, muestras - 1)
        pt = rg.Point3d(
            p1.X + t * (p2.X - p1.X),
            p1.Y + t * (p2.Y - p1.Y),
            p1.Z + t * (p2.Z - p1.Z))

        for crv in polylines:
            if crv is None:
                continue
            success, param = crv.ClosestPoint(pt)
            if success:
                closest = crv.PointAt(param)
                d = pt.DistanceTo(closest)
                if d < min_dist:
                    min_dist = d

    return min_dist


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
    mensaje = "CLASIFICAR v03 | ERROR: Se necesitan >= 3 vertices (recibidos: {})".format(
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

        # Clasificar cada lado
        lados = []
        for i in range(n):
            j = (i + 1) % n
            p1 = lot_vertices[i]
            p2 = lot_vertices[j]

            # 1. Distancia a VIAS
            dist_via = distancia_minima_segmento_polilineas(p1, p2, vias_list)

            # 2. Distancia a ESPACIOS PUBLICOS (parques, plazas, zonas verdes)
            dist_ep = distancia_minima_segmento_polilineas(p1, p2, ep_list)

            # 3. Clasificar por prioridad: Via > EspacioPublico directo > Lateral
            if dist_via < DISTANCIA_FRENTE_M:
                cat = "Frontal"
                dist_ref = round(dist_via, 2)
            elif dist_ep <= TOL_EP_M:
                # Solo si el lote es COLINDANTE DIRECTO (distancia ~0)
                cat = "EspacioPublico"
                dist_ref = round(dist_ep, 2)
            else:
                cat = "Lateral"
                dist_ref = round(min(dist_via, dist_ep), 2)

            lados.append({
                "id": i,
                "vertice_inicio": i,
                "vertice_fin": j,
                "distancia_min_a_via": round(dist_via, 2),
                "distancia_min_a_ep": round(dist_ep, 2),
                "clasificacion": cat
            })

        # Post-procesar: si solo 1 lado es Frontal, el opuesto es Posterior
        categorias = [l["clasificacion"] for l in lados]
        n_frontales = categorias.count("Frontal")

        if n_frontales == 1 and n == 4:
            idx_frontal = categorias.index("Frontal")
            idx_posterior = (idx_frontal + 2) % 4
            # Solo convertir si actualmente es Lateral (no EspacioPublico ni Frontal)
            if lados[idx_posterior]["clasificacion"] == "Lateral":
                lados[idx_posterior]["clasificacion"] = "Posterior"

        # Construir JSON de salida
        sides_data = {"lados": lados, "total_lados": len(lados), "regla": "ADR-008 15m + EP"}
        sides_table_json = json.dumps(sides_data)

        cats_final = [l["clasificacion"] for l in lados]
        mensaje = "CLASIFICAR v03 | {} vertices → {} lados | {} | Vias:{} EP:{}".format(
            n, len(lados), ", ".join(cats_final), len(vias_list), len(ep_list))

    except Exception as e:
        mensaje = "CLASIFICAR v03 | ERROR: {}".format(str(e))
