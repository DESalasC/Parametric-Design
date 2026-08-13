"""
================================================================================
F1_ETAPA2_PATIO_v01.py — Etapa 2: Patios por esquinas Lateral-Lateral
Proyecto: DisenoParametrico / Fase 1
GH Python Script para Grasshopper (IronPython 2.7 compatible)
================================================================================

PROPOSITO:
  Genera patios en vertices donde convergen DOS lados "Lateral"
  (esquinas entre predios vecinos), segun la clasificacion de
  F1_ETAPA2_LADOS_v01.

  Reglas:
    - Patio SOLO en esquina Lateral-Lateral
    - Lado EspacioPublico: sin retiro → sin patio en esa esquina
    - Dimension: max(3m, pisos * 0.25) segun altura

ENTRADAS:
  lot_vertices (Point3d[])     — 4 vertices desde Discontinuity
  sides_table_json (String)    — Clasificacion desde F1_ETAPA2_LADOS
  altura_max_pot (Number)      — Altura maxima POT [m]

SALIDAS:
  patios_curves   (Curve[])   — Rectangulos de patio
  patio_count     (int)       — Numero de patios
  mensaje         (String)    — Diagnostico
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
    """Ray casting 2D."""
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

sides_data = None
if sides_raw is not None:
    try:
        if isinstance(sides_raw, list) and sides_raw:
            s = str(sides_raw[0])
        else:
            s = str(sides_raw)
        sides_data = json.loads(s)
    except:
        sides_data = None

try:
    altura_max = float(unwrap(altura_raw)) if altura_raw else 11.4
except:
    altura_max = 11.4

patios_curves = []
patio_count = 0

if sides_data is None or len(lot_vertices) < 4:
    mensaje = "PATIO v01 | ERROR: vertices={} sides={}".format(
        len(lot_vertices), "OK" if sides_data else "FALTA")
else:
    try:
        lados = sides_data.get("lados", [])
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
        mensaje = "PATIO v01 | Lados: {} | Patio={:.2f}m | Generados: {}".format(
            ", ".join(cats), patio_lado, patio_count)

    except Exception as e:
        mensaje = "PATIO v01 | ERROR: {}".format(str(e))
