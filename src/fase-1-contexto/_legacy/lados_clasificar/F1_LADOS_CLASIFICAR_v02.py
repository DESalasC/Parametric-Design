#! /usr/bin/env python3
"""
================================================================================
F1_LADOS_CLASIFICAR_v02.py — Clasificador de lados por regla hibrida 15m
Proyecto: DisenoParametrico / Fase 1
GH Python Script para Grasshopper (IronPython 2.7 compatible)
================================================================================

PROPOSITO:
  Recibe los 4 vertices principales del lote (desde componente Discontinuity
  de Grasshopper, que filtra los vertices topograficos intermedios y solo
  devuelve las esquinas reales). Con esos 4 vertices reconstruye el poligono
  simplificado y clasifica cada lado como Frontal/Lateral/Posterior usando
  la regla hibrida de 15m (ADR-008).

  Ventaja: 4 lados virtuales vs 9+ segmentos reales → clasificacion mas
  limpia, patios mas predecibles, normativa mas directa.

ENTRADAS:
  lot_vertices (Point3d[]) — 4 vertices principales desde Discontinuity
  vias (Curve[])            — Curvas de via CONSOLIDADAS (oficiales + manuales)

SALIDAS:
  sides_table_json (String) — JSON con clasificacion (4 lados)
  lot_simplificado (Curve)  — Poligono reconstruido de 4 lados
  mensaje (String)          — Diagnostico

NORMATIVA:
  ADR-008 — Clasificacion Espacial Hibrida
  Regla: distancia minima lado→via < 15m → Frontal
================================================================================
"""

import Rhino.Geometry as rg
import json
import math

DISTANCIA_FRENTE_M = 15.0


def unwrap(val):
    if val is None: return None
    if isinstance(val, list): return val[0] if len(val) > 0 else None
    return val


def safe_list(val):
    if val is None: return []
    if isinstance(val, list): return val
    return [val]


def punto_medio(p1, p2):
    """Punto medio entre dos puntos."""
    return rg.Point3d((p1.X + p2.X) / 2, (p1.Y + p2.Y) / 2, (p1.Z + p2.Z) / 2)


def distancia_minima_segmento_polilinea(p1, p2, polyline_curve):
    """
    Distancia minima entre el segmento (p1,p2) y una PolylineCurve.
    Muestrea puntos a lo largo del segmento y busca el mas cercano a la via.
    """
    if polyline_curve is None:
        return float('inf')

    # Muestrear el segmento cada ~0.5m
    longitud = p1.DistanceTo(p2)
    muestras = max(3, int(longitud / 0.5) + 1)

    min_dist = float('inf')
    for i in range(muestras):
        t = float(i) / max(1, muestras - 1)
        px = p1.X + t * (p2.X - p1.X)
        py = p1.Y + t * (p2.Y - p1.Y)
        pz = p1.Z + t * (p2.Z - p1.Z)
        pt = rg.Point3d(px, py, pz)

        # Distancia minima del punto a la curva de via
        success, param = polyline_curve.ClosestPoint(pt)
        if success:
            closest = polyline_curve.PointAt(param)
            d = pt.DistanceTo(closest)
            if d < min_dist:
                min_dist = d

    return min_dist


# ==============================================================================
# MAIN
# ==============================================================================

lot_vertices_raw = globals().get("lot_vertices", None)
vias_raw = globals().get("vias", None)

# Parse inputs
if isinstance(lot_vertices_raw, list) and len(lot_vertices_raw) > 0:
    lot_vertices = lot_vertices_raw
else:
    lot_vertices = safe_list(lot_vertices_raw)

vias_list = safe_list(vias_raw)

# Initialize outputs
sides_table_json = ""
lot_simplificado = None

if len(lot_vertices) < 3:
    mensaje = "CLASIFICAR v02 | ERROR: Se necesitan al menos 3 vertices (recibidos: {})".format(len(lot_vertices))
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
        categorias = []
        for i in range(n):
            j = (i + 1) % n
            p1 = lot_vertices[i]
            p2 = lot_vertices[j]

            # Distancia minima del lado a todas las vias
            mejor_dist = float('inf')
            for via in vias_list:
                if via is None:
                    continue
                d = distancia_minima_segmento_polilinea(p1, p2, via)
                if d < mejor_dist:
                    mejor_dist = d

            # Clasificar
            if mejor_dist < DISTANCIA_FRENTE_M:
                cat = "Frontal"
            else:
                cat = "Lateral"

            lados.append({
                "id": i,
                "vertice_inicio": i,
                "vertice_fin": j,
                "distancia_min_a_via": round(mejor_dist, 2),
                "clasificacion": cat
            })
            categorias.append(cat)

        # Post-procesar: si solo 1 lado es Frontal, el opuesto es Posterior
        n_frontales = categorias.count("Frontal")
        if n_frontales == 1 and n == 4:
            idx_frontal = categorias.index("Frontal")
            idx_posterior = (idx_frontal + 2) % 4
            if lados[idx_posterior]["clasificacion"] == "Lateral":
                lados[idx_posterior]["clasificacion"] = "Posterior"
                lados[idx_posterior]["distancia_min_a_via"] = "N/A"

        # Construir JSON de salida
        sides_data = {"lados": lados, "total_lados": len(lados), "regla": "ADR-008 15m"}
        sides_table_json = json.dumps(sides_data)

        cats_final = [l["clasificacion"] for l in lados]
        mensaje = "CLASIFICAR v02 | {} vertices → {} lados | {} | Vias: {}".format(
            n, len(lados), ", ".join(cats_final), len(vias_list))

    except Exception as e:
        mensaje = "CLASIFICAR v02 | ERROR: {}".format(str(e))
