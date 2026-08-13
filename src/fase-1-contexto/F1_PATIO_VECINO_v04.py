#! /usr/bin/env python3
"""
================================================================================
F1_PATIO_VECINO_v04.py — Patios de aislamiento en vertices colindantes con vecinos.
Proyecto: DisenoParametrico / Fase 1 — Contexto y Normativa
GH Python Script para Grasshopper (IronPython 2.7 compatible)
================================================================================

PROPOSITO:
  Detecta vertices del lote donde convergen DOS lados colindantes con predios
  vecinos (NO con vias ni espacio publico). En cada uno de esos vertices se
  genera un patio de aislamiento que garantiza ventilacion e iluminacion
  natural al propio edificio y a los predios vecinos.

  Esta logica reemplaza el enfoque anterior de "esquina opuesta al cruce de
  calles" porque:
  - Un lote de esquina tiene 2 frentes de calle y 2 linderos vecinos.
  - Los vertices entre calle y vecino NO necesitan patio (la calle ventila).
  - Los vertices entre vecino y vecino SI necesitan patio.
  - Funciona para lotes irregulares con multiples segmentos no alineados.

NORMATIVA APLICABLE:
  - Decreto 555/2021, Art. 281
  - Lotes < 500 m2 con tipologia Continua: patio fijo de 3.0m x 3.0m
  - Regla general: patio_min = max(3.0, altura_total * 0.25) m por lado

ENTRADAS (Inputs de Grasshopper):
  ┌──────────────────┬──────────┬──────────────────────────────────────────────┐
  │ Nombre           │ Tipo     │ Descripcion                                  │
  ├──────────────────┼──────────┼──────────────────────────────────────────────┤
  │ lot_polygon      │ Curve    │ Poligono cerrado del perimetro del lote.     │
  │                  │          │ Item Access. Proviene de F1_CONTEXTO_POT.    │
  ├──────────────────┼──────────┼──────────────────────────────────────────────┤
  │ sides_table_json │ String   │ JSON con clasificacion de cada lado.         │
  │                  │          │ List Access. Proviene de F1_LADOS_CONFIGURAR.│
  │                  │          │ Los lados "Frontal" = colindan con via.      │
  │                  │          │ Los lados NO "Frontal" = colindan con vecino.│
  ├──────────────────┼──────────┼──────────────────────────────────────────────┤
  │ json_path        │ String   │ Ruta al archivo JSON de cache del lote.      │
  │                  │          │ Para leer rango_edificabilidad -> pisos.     │
  └──────────────────┴──────────┴──────────────────────────────────────────────┘

SALIDAS (Outputs de Grasshopper):
  ┌──────────────────┬──────────┬──────────────────────────────────────────────┐
  │ Nombre           │ Tipo     │ Descripcion                                  │
  ├──────────────────┼──────────┼──────────────────────────────────────────────┤
  │ patios_curves    │ Curve[]  │ Lista de polilineas de patios (puede ser     │
  │                  │          │ vacia si no aplican). El componente downstream│
  │                  │          │ debe restarlos todos de la huella.           │
  ├──────────────────┼──────────┼──────────────────────────────────────────────┤
  │ patio_vertices   │ int[]    │ Indices de vertices donde se genero patio.   │
  ├──────────────────┼──────────┼──────────────────────────────────────────────┤
  │ patio_count      │ int      │ Numero de patios generados.                  │
  ├──────────────────┼──────────┼──────────────────────────────────────────────┤
  │ mensaje          │ String   │ Diagnostico detallado de la operacion.       │
  └──────────────────┴──────────┴──────────────────────────────────────────────┘

FUNCIONES INTERNAS:
  ┌─────────────────────────┬──────────────────────────────────────────────────┐
  │ Nombre                  │ Descripcion                                      │
  ├─────────────────────────┼──────────────────────────────────────────────────┤
  │ parse_json_safe(data)   │ Convierte string/dict/list a dict sin errores.  │
  ├─────────────────────────┼──────────────────────────────────────────────────┤
  │ to_int_safe(val,def)    │ Convierte a int con fallback (>0).              │
  ├─────────────────────────┼──────────────────────────────────────────────────┤
  │ get_vertices(curve)     │ Extrae vertices unicos de PolylineCurve.         │
  ├─────────────────────────┼──────────────────────────────────────────────────┤
  │ point_in_lot(pt,verts)  │ Ray casting para inclusion en poligono.          │
  ├─────────────────────────┼──────────────────────────────────────────────────┤
  │ build_patio_at_vertex(  │ Construye rectangulo de patio en un vertice      │
  │   v, e1, e2, sz, verts) │ alineado con los bordes del lote, verificando    │
  │                         │ inclusion de las 4 esquinas.                      │
  └─────────────────────────┴──────────────────────────────────────────────────┘

VERSIONES:
  v01 — Primera version. Buscaba esquina opuesta al cruce de calles.
  v02 — Eliminado input building_floors. Geometria alineada con bordes.
  v03 — Prueba 4 orientaciones y elige la que cabe dentro del lote.
  v04 — Logica redefinida: patio en vertices donde convergen lados VECINOS
        (no calles). Soporta multiples patios. Sin lineas infinitas.
================================================================================
"""

import Rhino.Geometry as rg
import json
import os


# ==============================================================================
# FUNCIONES AUXILIARES
# ==============================================================================

def parse_json_safe(data):
    """Convierte string/dict/list a dict sin lanzar excepciones."""
    if data is None:
        return {}
    if isinstance(data, str):
        try:
            return json.loads(data)
        except:
            return {}
    if isinstance(data, (dict, list)):
        return data
    return {}


def to_int_safe(val, default=4):
    """Convierte a int con fallback. Valores <= 0 retornan default."""
    if val is None:
        return default
    try:
        v = int(float(val))
        if v <= 0:
            return default
        return v
    except (ValueError, TypeError):
        return default


def get_vertices(curve):
    """
    Extrae vertices unicos de una PolylineCurve cerrada.
    Si el poligono esta cerrado (primer vertice = ultimo), omite la duplicacion.
    """
    if curve is None:
        return []
    success, poly = curve.TryGetPolyline()
    if not success or poly is None:
        return []
    c = poly.Count
    if c >= 2 and poly[0].DistanceTo(poly[c - 1]) < 0.001:
        return [poly[i] for i in range(c - 1)]
    return [poly[i] for i in range(c)]


def point_in_lot(pt, vertices):
    """
    Determina si un punto esta dentro del poligono del lote (ray casting).
    IronPython 2.7 compatible.
    """
    n = len(vertices)
    if n < 3:
        return False
    count = 0
    px, py = pt.X, pt.Y
    for i in range(n):
        v1 = vertices[i]
        v2 = vertices[(i + 1) % n]
        if ((v1.Y > py) != (v2.Y > py)):
            x_int = v1.X + (py - v1.Y) * (v2.X - v1.X) / (v2.Y - v1.Y)
            if px < x_int:
                count += 1
    return (count % 2) == 1


def build_patio_at_vertex(corner_vertex, edge_to_prev, edge_to_next, size, vertices):
    """
    Construye un rectangulo de patio en un vertice del lote, alineado con
    los dos bordes que convergen en ese vertice.

    Prueba las 4 combinaciones de signos de los vectores de borde y elige
    la orientacion donde las 4 esquinas del rectangulo quedan dentro del lote.

    Args:
        corner_vertex: rg.Point3d — vertice donde anclar el patio.
        edge_to_prev: rg.Vector3d — direccion del borde hacia el vertice anterior.
        edge_to_next: rg.Vector3d — direccion del borde hacia el vertice siguiente.
        size: float — longitud del lado del patio (m).
        vertices: list[rg.Point3d] — todos los vertices del lote.

    Returns:
        rg.PolylineCurve o None.
    """
    e1 = rg.Vector3d(edge_to_prev.X, edge_to_prev.Y, 0)
    e2 = rg.Vector3d(edge_to_next.X, edge_to_next.Y, 0)

    if e1.Length < 0.001 or e2.Length < 0.001:
        return None

    e1.Unitize()
    e2.Unitize()

    signs = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    best_count = -1
    best_pts = None

    for sx, sy in signs:
        s1 = rg.Vector3d(sx * e1.X, sx * e1.Y, 0)
        s2 = rg.Vector3d(sy * e2.X, sy * e2.Y, 0)

        p0 = rg.Point3d(corner_vertex.X, corner_vertex.Y, 0)
        p1 = rg.Point3d(p0.X + s1.X * size, p0.Y + s1.Y * size, 0)
        p2 = rg.Point3d(p1.X + s2.X * size, p1.Y + s2.Y * size, 0)
        p3 = rg.Point3d(p0.X + s2.X * size, p0.Y + s2.Y * size, 0)

        test_pts = [p0, p1, p2, p3]
        inside_count = sum(1 for p in test_pts if point_in_lot(p, vertices))

        if inside_count > best_count:
            best_count = inside_count
            best_pts = [p0, p1, p2, p3]

    if best_count >= 4 and best_pts is not None:
        pts = best_pts + [best_pts[0]]
        return rg.PolylineCurve(pts)

    return None


# ==============================================================================
# PROGRAMA PRINCIPAL
# ==============================================================================

# --- 1. LECTURA DE ENTRADAS ---
lot_polygon_raw = globals().get("lot_polygon", None)
sides_table_raw = globals().get("sides_table_json", None)
json_path_raw   = globals().get("json_path", None)

if isinstance(lot_polygon_raw, list) and len(lot_polygon_raw) == 1:
    lot_polygon_raw = lot_polygon_raw[0]

lot_polygon = lot_polygon_raw
json_path   = str(json_path_raw).strip("[]'\" ") if json_path_raw else ""

# --- 2. GUARDIA ---
if lot_polygon is None:
    patios_curves  = []
    patio_vertices = []
    patio_count    = 0
    mensaje        = "ERROR: lot_polygon es None."
    print(mensaje)
else:
    # --- 3. PISOS DESDE REGULACION ---
    building_floors = 4
    rango_edif = "3"

    if json_path and os.path.exists(json_path):
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                jdata = json.load(f)
            pd = jdata.get("pot_data", {})
            rango_edif = str(pd.get("rango_edificabilidad", "3"))
        except:
            pass

    RANGO_PISOS = {"1": 2, "2": 3, "3": 5, "4": 8, "5": 12}
    building_floors = RANGO_PISOS.get(rango_edif, 5)

    # --- 4. CLASIFICACION DE LADOS ---
    sides_data = parse_json_safe(sides_table_raw)
    sides_list = []

    if isinstance(sides_data, list):
        for item in sides_data:
            if isinstance(item, dict):
                sides_list.append(item)
            elif isinstance(item, str):
                try:
                    d = json.loads(item)
                    if isinstance(d, dict):
                        sides_list.append(d)
                except:
                    pass
    elif isinstance(sides_data, dict):
        inner = sides_data.get("sides", sides_data.get("lados", []))
        if isinstance(inner, list):
            sides_list = inner

    # --- 5. IDENTIFICAR LADOS VECINOS ---
    # Un lado es "vecino" si NO esta clasificado como "Frontal".
    # Los lados frontales colindan con via/espacio publico -> no necesitan patio.
    neighbor_indices = []
    for side in sides_list:
        if isinstance(side, dict):
            cls = str(side.get("classification", "")).strip().lower()
            idx = to_int_safe(side.get("side_index", -1))
            if idx >= 0 and cls != "frontal":
                neighbor_indices.append(idx)

    neighbor_set = set(neighbor_indices)

    vertices = get_vertices(lot_polygon)
    n_verts  = len(vertices)

    # --- 6. DETECTAR VERTICES ENTRE DOS LADOS VECINOS ---
    # Un vertice i es "vertice de patio" si:
    #   - El lado (i-1) es vecino  Y  el lado i es vecino
    # Los lados se indexan igual que los vertices de origen.
    # Lado i va de vertice i a vertice i+1.

    patio_vertices = []
    for i in range(n_verts):
        lado_anterior = (i - 1 + n_verts) % n_verts
        lado_actual   = i % n_verts

        if lado_anterior in neighbor_set and lado_actual in neighbor_set:
            patio_vertices.append(i)

    # --- 7. TAMANO DEL PATIO ---
    try:
        amp = rg.AreaMassProperties.Compute(lot_polygon)
        lot_area = amp.Area if amp else 315.0
    except:
        lot_area = 315.0

    if lot_area < 500.0 and building_floors <= 5:
        patio_size_m = 3.0
    else:
        altura_total = building_floors * 3.0
        patio_size_m = max(3.0, altura_total * 0.25)
        patio_size_m = round(patio_size_m * 2.0) / 2.0

    # --- 8. CONSTRUIR PATIOS ---
    patios_curves = []
    for vi in patio_vertices:
        v_corner = vertices[vi]
        v_prev   = vertices[(vi - 1 + n_verts) % n_verts]
        v_next   = vertices[(vi + 1) % n_verts]

        edge_to_prev = rg.Vector3d(v_prev.X - v_corner.X, v_prev.Y - v_corner.Y, 0)
        edge_to_next = rg.Vector3d(v_next.X - v_corner.X, v_next.Y - v_corner.Y, 0)

        curve = build_patio_at_vertex(v_corner, edge_to_prev, edge_to_next,
                                      patio_size_m, vertices)
        if curve is not None:
            patios_curves.append(curve)

    patio_count = len(patios_curves)

    # --- 9. MENSAJE ---
    partes = [
        "=== PATIO VECINO v04 ===",
        "Lote: {} vertices | {} lados vecinos de {}".format(
            n_verts, len(neighbor_indices), n_verts),
        "Vertices vecino-vecino: {} -> {} patios generados".format(
            patio_vertices, patio_count),
        "Tamano patio: {:.1f}x{:.1f}m ({} pisos, rango {})".format(
            patio_size_m, patio_size_m, building_floors, rango_edif),
    ]

    if patio_count == 0 and len(neighbor_indices) >= 2:
        partes.append("NOTA: Hay lados vecinos pero no comparten vertices adyacentes.")
    elif len(neighbor_indices) < 2:
        partes.append("Sin suficientes lados vecinos adyacentes para patio.")

    mensaje = "\n".join(partes)
    print(mensaje)

# ==============================================================================
# OUTPUTS: patios_curves, patio_vertices, patio_count, mensaje
# ==============================================================================
