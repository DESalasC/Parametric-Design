#! /usr/bin/env python3
"""
================================================================================
F1_PATIO_DISCONTINUIDAD_v02.py — Generador de patios desde clasificacion
Proyecto: DisenoParametrico / Fase 1
GH Python Script para Grasshopper (IronPython 2.7 compatible)
================================================================================

PROPOSITO:
  UNICA responsabilidad: recibir la clasificacion de lados YA CALCULADA
  (de F1_LADOS_CLASIFICAR_v01) y generar patios en vertices donde convergen
  DOS bordes "Lateral" (esquinas internas entre vecinos).

  NO clasifica lados. NO lee del JSON. Solo GENERA patios.

ENTRADAS:
  lot_vertices  (Point3d[]) — Vertices del lote desde componente Discontinuity
  sides_table_json (String) — Clasificacion de lados (de F1_LADOS_CLASIFICAR_v01)
  altura_max_pot (Number)   — Altura maxima POT (para dimension de patio)

SALIDAS:
  patios_curves   (Curve[])   — Rectangulos de patio para vertices Lateral+Lateral
  patio_count     (int)       — Numero de patios generados
  mensaje         (String)    — Diagnostico

NORMATIVA:
  Decreto 555/2021 — POT Bogota
  ADR-008 — Clasificacion Espacial Hibrida
================================================================================
"""

import Rhino.Geometry as rg
import json
import math

RANGO_PISOS = {"1": 2, "2": 3, "3": 5, "4": 8, "5": 12}
ALTURA_ENTREPISO = 3.0
PATIO_MINIMO_M = 3.0


def unwrap(val):
    if val is None: return None
    if isinstance(val, list): return val[0] if len(val) > 0 else None
    return val


def safe_list(val):
    if val is None: return []
    if isinstance(val, list): return val
    return [val]


def point_in_lot(pt, vertices):
    """Ray casting — verifica si el punto esta dentro del poligono (2D)."""
    n = len(vertices)
    if n < 3: return False
    count = 0
    px, py = pt.X, pt.Y
    for i in range(n):
        v1 = vertices[i]
        v2 = vertices[(i + 1) % n]
        if ((v1.Y > py) != (v2.Y > py)):
            if (v2.Y - v1.Y) != 0:
                x_int = v1.X + (py - v1.Y) * (v2.X - v1.X) / (v2.Y - v1.Y)
                if px < x_int: count += 1
    return (count % 2) == 1


def build_patio_at_vertex(corner_pt, edge1_vec, edge2_vec, size, lot_vertices):
    """
    Construye rectangulo de patio anclado en corner_pt,
    alineado a edge1_vec y edge2_vec, proyectado hacia el interior del lote.
    """
    # Normalizar vectores de borde (hacia el interior)
    v1 = rg.Vector3d(edge1_vec)
    v2 = rg.Vector3d(edge2_vec)
    if v1.Length < 0.001 or v2.Length < 0.001:
        return None

    v1.Unitize()
    v2.Unitize()

    # Proyectar hacia el interior: invertir direccion de cada borde
    v1_in = -v1
    v2_in = -v2

    p0 = rg.Point3d(corner_pt)
    p1 = rg.Point3d(p0.X + v1_in.X * size, p0.Y + v1_in.Y * size, p0.Z)
    p2 = rg.Point3d(p0.X + v1_in.X * size + v2_in.X * size,
                     p0.Y + v1_in.Y * size + v2_in.Y * size, p0.Z)
    p3 = rg.Point3d(p0.X + v2_in.X * size, p0.Y + v2_in.Y * size, p0.Z)

    # Validar: al menos 2 puntos dentro del lote
    inside = sum(1 for p in [p0, p1, p2, p3] if point_in_lot(p, lot_vertices))
    if inside < 2:
        return None

    poly = rg.Polyline()
    poly.Add(p0)
    poly.Add(p1)
    poly.Add(p2)
    poly.Add(p3)
    poly.Add(p0)
    return rg.PolylineCurve(poly)


# ==============================================================================
# MAIN
# ==============================================================================

lot_vertices_raw = globals().get("lot_vertices", None)
sides_raw = globals().get("sides_table_json", None)

lot_vertices = safe_list(lot_vertices_raw if not isinstance(lot_vertices_raw, list) else lot_vertices_raw)
try:
    sides_str = str(unwrap(sides_raw)).strip("[]'\" ")
except:
    sides_str = ""

patios_curves = []
patio_count = 0

if not sides_str or not lot_vertices or len(lot_vertices) < 4:
    mensaje = "PATIO v02 | ERROR: Faltan lot_vertices ({}) o sides_table_json ({})".format(
        len(lot_vertices), "OK" if sides_str else "FALTA")
else:
    try:
        sides_data = json.loads(sides_str)
        sides_list = sides_data.get("lados", [])

        # Determinar lado de patio segun altura
        altura_max_raw = globals().get("altura_max_pot", 11.4)
        altura_max = float(unwrap(altura_max_raw)) if altura_max_raw else 11.4
        pisos = max(1, int(math.ceil(altura_max / ALTURA_ENTREPISO)))
        patio_lado = max(PATIO_MINIMO_M, pisos * 0.25)

        n = len(lot_vertices)
        for i in range(n):
            lado_a = sides_list[i % len(sides_list)] if i < len(sides_list) else {"clasificacion": "Desconocido"}
            lado_b = sides_list[(i + n - 1) % len(sides_list)] if (i + n - 1) < len(sides_list) else {"clasificacion": "Desconocido"}

            cat_a = lado_a.get("clasificacion", "Desconocido")
            cat_b = lado_b.get("clasificacion", "Desconocido")

            # Patio solo si ambos bordes que convergen son Lateral
            if cat_a == "Lateral" and cat_b == "Lateral":
                # Direccion del borde A (desde vertice i hacia i+1)
                va = lot_vertices[(i + 1) % n] - lot_vertices[i]
                # Direccion del borde B (desde vertice i hacia i-1, invertida = entrando)
                vb = lot_vertices[(i + n - 1) % n] - lot_vertices[i]

                patio_crv = build_patio_at_vertex(lot_vertices[i], va, vb, patio_lado, lot_vertices)
                if patio_crv:
                    patios_curves.append(patio_crv)

        patio_count = len(patios_curves)
        mensaje = "PATIO v02 | Vertices: {} | Lados: {} | Patio={:.2f}m | Patios generados: {}".format(
            n, len(sides_list), patio_lado, patio_count)

    except Exception as e:
        mensaje = "PATIO v02 | ERROR: {}".format(str(e))
