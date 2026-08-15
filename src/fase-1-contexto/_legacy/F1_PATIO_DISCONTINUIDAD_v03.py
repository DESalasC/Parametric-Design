#! /usr/bin/env python3
"""
================================================================================
F1_PATIO_DISCONTINUIDAD_v03.py — Patios desde vertices simplificados (4 lados)
Proyecto: DisenoParametrico / Fase 1
GH Python Script para Grasshopper (IronPython 2.7 compatible)
================================================================================

PROPOSITO:
  Recibe los 4 vertices principales del lote (desde Discontinuity) y la
  clasificacion de lados (desde F1_LADOS_CLASIFICAR_v02). Genera patios en
  vertices donde convergen DOS bordes "Lateral" (esquinas entre vecinos).

  Con el lote simplificado a 4 lados virtuales, la logica de patio es trivial:
  - Si hay 1 Frontal + 1 Posterior + 2 Laterales → patio en vertices Lateral-Lateral
  - Si hay 2+ Frontales (esquina) → sin patio (da a via)

ENTRADAS:
  lot_vertices (Point3d[])   — 4 vertices desde Discontinuity
  sides_table_json (String)  — Clasificacion desde F1_LADOS_CLASIFICAR_v02
  altura_max_pot (Number)    — Altura maxima POT [m]

SALIDAS:
  patios_curves   (Curve[])  — Rectangulos de patio (0, 1 o 2)
  patio_count     (int)      — Numero de patios generados
  mensaje         (String)   — Diagnostico

NORMATIVA:
  POT Bogota — patio >= 3m, >= pisos*0.25
================================================================================
"""

import Rhino.Geometry as rg
import json
import math

PATIO_MINIMO_M = 3.0
ALTURA_ENTREPISO = 3.0


def unwrap(val):
    if val is None: return None
    if isinstance(val, list): return val[0] if len(val) > 0 else None
    return val


def safe_list(val):
    if val is None: return []
    if isinstance(val, list): return val
    return [val]


def point_in_lot(pt, vertices):
    """Ray casting 2D — verifica si el punto esta dentro del poligono."""
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
                if px < x_int:
                    count += 1
    return (count % 2) == 1


def build_patio_at_vertex(corner_pt, edge1_out, edge2_out, size, lot_vertices):
    """
    Construye rectangulo de patio anclado en el vertice de esquina,
    proyectado hacia el interior del lote usando los dos bordes.
    edge1_out: vector del borde 1 desde corner (saliente)
    edge2_out: vector del borde 2 desde corner (saliente)
    """
    v1 = rg.Vector3d(edge1_out)
    v2 = rg.Vector3d(edge2_out)
    if v1.Length < 0.001 or v2.Length < 0.001:
        return None

    v1.Unitize()
    v2.Unitize()

    v1_in = -v1
    v2_in = -v2

    p0 = rg.Point3d(corner_pt)
    p1 = rg.Point3d(p0.X + v1_in.X * size, p0.Y + v1_in.Y * size, p0.Z)
    p2 = rg.Point3d(p0.X + v1_in.X * size + v2_in.X * size,
                     p0.Y + v1_in.Y * size + v2_in.Y * size, p0.Z)
    p3 = rg.Point3d(p0.X + v2_in.X * size, p0.Y + v2_in.Y * size, p0.Z)

    inside = sum(1 for p in [p0, p1, p2, p3] if point_in_lot(p, lot_vertices))
    if inside < 2:
        return None

    poly = rg.Polyline()
    poly.Add(p0); poly.Add(p1); poly.Add(p2); poly.Add(p3); poly.Add(p0)
    return rg.PolylineCurve(poly)


# ==============================================================================
# MAIN
# ==============================================================================

lot_vertices_raw = globals().get("lot_vertices", None)
sides_raw = globals().get("sides_table_json", None)
altura_raw = globals().get("altura_max_pot", None)

lot_vertices = safe_list(lot_vertices_raw)

# Parse sides_table_json — GH puede entregarlo como lista multibranch
sides_str = ""
sides_data = None
try:
    raw = unwrap(sides_raw)
    if isinstance(raw, basestring):
        sides_str = raw
    elif raw is not None:
        sides_str = str(raw)
except:
    pass

# Intentar parsear JSON directamente; si falla extraer primer objeto valido
if sides_str:
    try:
        sides_data = json.loads(sides_str)
    except:
        # Puede venir con datos extra concatenados (multibranch GH)
        idx = sides_str.find('}{')
        if idx > 0:
            sides_data = json.loads(sides_str[:idx+1])
        else:
            sides_data = None

try:
    altura_max = float(unwrap(altura_raw)) if altura_raw else 11.4
except:
    altura_max = 11.4

patios_curves = []
patio_count = 0

if sides_data is None or len(lot_vertices) < 4:
    mensaje = "PATIO v03 | ERROR: vertices={} sides={}".format(
        len(lot_vertices), "OK" if sides_data else "FALTA")

elif len(lot_vertices) != 4:
    mensaje = "PATIO v03 | ADVERTENCIA: Se esperan 4 vertices, recibidos {}".format(
        len(lot_vertices))

else:
    try:
        lados = sides_data.get("lados", [])

        # Calcular tamano de patio segun altura
        pisos = max(1, int(math.ceil(altura_max / ALTURA_ENTREPISO)))
        patio_lado = max(PATIO_MINIMO_M, pisos * 0.25)

        n = len(lot_vertices)
        for i in range(n):
            lado_a = lados[i] if i < len(lados) else {"clasificacion": "Desconocido"}
            lado_b = lados[(i + n - 1) % n] if (i + n - 1) < len(lados) else {"clasificacion": "Desconocido"}

            cat_a = lado_a.get("clasificacion", "Desconocido")
            cat_b = lado_b.get("clasificacion", "Desconocido")

            if cat_a == "Lateral" and cat_b == "Lateral":
                vi = lot_vertices[i]
                v_next = lot_vertices[(i + 1) % n]
                edge_a = rg.Vector3d(v_next.X - vi.X, v_next.Y - vi.Y, 0)
                v_prev = lot_vertices[(i + n - 1) % n]
                edge_b = rg.Vector3d(v_prev.X - vi.X, v_prev.Y - vi.Y, 0)

                patio_crv = build_patio_at_vertex(vi, edge_a, edge_b, patio_lado, lot_vertices)
                if patio_crv:
                    patios_curves.append(patio_crv)

        patio_count = len(patios_curves)
        cats = [l.get("clasificacion", "?") for l in lados]
        mensaje = "PATIO v03 | {} vertices | Lados: {} | Patio={:.2f}m | Generados: {}".format(
            n, ", ".join(cats), patio_lado, patio_count)

    except Exception as e:
        mensaje = "PATIO v03 | ERROR: {}".format(str(e))
