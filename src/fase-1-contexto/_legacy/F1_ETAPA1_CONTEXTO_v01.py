"""
================================================================================
F1_ETAPA1_CONTEXTO_v01.py — Etapa 1: Datos en bruto → Geometria + Capas
Proyecto: DisenoParametrico / Fase 1
GH Python Script para Grasshopper (IronPython 2.7 compatible)
================================================================================

PROPOSITO:
  Etapa 1 del pipeline v26. Lee el JSON de contexto v6 y entrega TODA la
  geometria en bruto organizada por CAPA DESTINO, lista para enviar a
  ArchiCAD via Tapir.

  El flujo posterior es MANUAL en ArchiCAD: se clasifican los poligonos
  (vias, andenes, zonas verdes, predios vecinos) en los layers creados,
  y se construyen los Morphs de volumetrias vecinas.

ENTRADAS:
  json_path (String) — Ruta al <CHIP>-contexto.json

SALIDAS (agrupadas por capa destino):
  LOTE:        lot_curve (Curve) + lot_area (Number)
  VECINOS:     vecinos_curves (Curve[]) — capa "predios vecinos"
  VIAS:        vias_oficiales (Curve[]) — capa 00-20-20_Elementos_entorno_urbano
  ESPACIOS:    espacios_publicos (Curve[]) — capa 70-50-10_Zonas_verdes_publicas
  TOPO:        topo_mesh (Mesh) — capa 10-20-10_Topografia
  NORMATIVA:   altura_max_pot, tratamiento, rango_edificabilidad,
               sector_normativo, upz, io_normativo
  ORIGEN:      origen_x, origen_y (SIRGAS del anclaje SE)
  LAYERS:      layers_json (String) — lista de capas a crear en ArchiCAD
  MENSAJE:     mensaje (String)

CAPAS ARCHICAD (creadas via Tapir):
  00-00-10_Lote_proyecto
  00-20-20_Elementos_entorno_urbano   (vias)
  70-50-10_Zonas_verdes_publicas      (parques/plazas)
  70-30-20_Andenes_preexistentes
  10-20-10_Topografia
  70-20-30_Volumetrias_vecinas        (Morphs manuales)
  00-10-20_Elementos_referencia
  00-20-20_Foto_Aerea_Referencia
================================================================================
"""

import Rhino.Geometry as rg
import json
import io
import os
import math


def unwrap(val):
    if val is None: return None
    if isinstance(val, list): return val[0] if len(val) > 0 else None
    return val


def to_float_safe(val, default=0.0):
    if val is None: return default
    try: return float(val)
    except: return default


def polyline_from_coords(coords, dx, dy, dz):
    """Convierte [[x,y,z],...] en PolylineCurve con offset."""
    if not coords or len(coords) < 3:
        return None
    poly = rg.Polyline()
    for c in coords:
        poly.Add(c[0] - dx, c[1] - dy, c[2] - dz)
    if not poly.IsClosed:
        poly.Add(poly[0])
    return rg.PolylineCurve(poly)


def build_terrain_mesh(mesh_points, dx, dy, dz):
    """Malla de terreno por interpolacion IDW sobre grilla ~5m."""
    if not mesh_points or len(mesh_points) < 3:
        return None

    pts = []
    for p in mesh_points:
        pts.append((p["x_local"] - dx, p["y_local"] - dy, p["z_local"] - dz))

    min_x = min(p[0] for p in pts)
    max_x = max(p[0] for p in pts)
    min_y = min(p[1] for p in pts)
    max_y = max(p[1] for p in pts)

    res = 5.0
    cols = max(2, int((max_x - min_x) / res) + 1)
    rows = max(2, int((max_y - min_y) / res) + 1)

    mesh = rg.Mesh()
    grid_pts = []
    for r in range(rows):
        for c in range(cols):
            gx = min_x + c * (max_x - min_x) / max(1, cols - 1)
            gy = min_y + r * (max_y - min_y) / max(1, rows - 1)
            gz = 0.0
            total_w = 0.0
            for px, py, pz in pts:
                dist = math.sqrt((gx - px) ** 2 + (gy - py) ** 2)
                if dist < 0.01:
                    gz = pz
                    total_w = 1.0
                    break
                w = 1.0 / max(0.1, dist * dist)
                gz += pz * w
                total_w += w
            if total_w > 0:
                gz /= total_w
            idx = mesh.Vertices.Add(gx, gy, gz)
            grid_pts.append(idx)

    for r in range(rows - 1):
        for c in range(cols - 1):
            a = grid_pts[r * cols + c]
            b = grid_pts[r * cols + c + 1]
            cc = grid_pts[(r + 1) * cols + c]
            d = grid_pts[(r + 1) * cols + c + 1]
            mesh.Faces.AddFace(a, b, d)
            mesh.Faces.AddFace(a, d, cc)

    mesh.Normals.ComputeNormals()
    mesh.Compact()
    return mesh


# ==============================================================================
# MAIN
# ==============================================================================

json_path_raw = globals().get("json_path", None)
json_path = str(unwrap(json_path_raw)).strip("[]'\" ") if json_path_raw else ""

# Inicializar salidas
lot_curve = None
lot_area = 0.0
vecinos_curves = []
vias_oficiales = []
espacios_publicos = []
topo_mesh = None
altura_max_pot = 11.4
tratamiento = "Consolidacion"
rango_edificabilidad = "3"
sector_normativo = ""
upz = "N/A"
io_normativo = 0.70
origen_x = 0.0
origen_y = 0.0
layers_json = ""

LAYERS_ARCHICAD = [
    {"nombre": "00-00-10_Lote_proyecto", "color": 1, "visible": True},
    {"nombre": "00-20-20_Elementos_entorno_urbano", "color": 2, "visible": True},
    {"nombre": "00-20-30_Ejes_vias", "color": 8, "visible": True},
    {"nombre": "70-50-10_Zonas_verdes_publicas", "color": 3, "visible": True},
    {"nombre": "70-30-20_Andenes_preexistentes", "color": 4, "visible": True},
    {"nombre": "10-20-10_Topografia", "color": 5, "visible": True},
    {"nombre": "70-20-20_Perimetros_vecinos", "color": 9, "visible": True},
    {"nombre": "70-20-30_Volumetrias_vecinas", "color": 6, "visible": True},
    {"nombre": "00-10-20_Elementos_referencia", "color": 7, "visible": True},
    {"nombre": "00-20-20_Foto_Aerea_Referencia", "color": 5, "visible": True},
]

if not json_path or not os.path.exists(json_path):
    mensaje = "ETAPA1 | ERROR: No se encontro el JSON: {}".format(json_path)
else:
    try:
        with io.open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # --- Anclaje: vertice SE del lote (min Y, max X) ---
        lote_verts = data.get("lote_objetivo", {}).get("vertices_3d_local", [])
        if lote_verts and len(lote_verts) >= 3:
            anchor = lote_verts[0]
            for v in lote_verts:
                if v[1] < anchor[1] - 0.01 or (abs(v[1] - anchor[1]) < 0.01 and v[0] > anchor[0]):
                    anchor = v
            dx, dy, dz = anchor[0], anchor[1], anchor[2]
        else:
            dx, dy, dz = 0.0, 0.0, 0.0

        meta = data.get("metadata", {})
        origen_sirgas = meta.get("origen_sirgas", {})
        origen_x = origen_sirgas.get("x", 0.0)
        origen_y = origen_sirgas.get("y", 0.0)

        # --- LOTE ---
        lot_curve = polyline_from_coords(lote_verts, dx, dy, dz)
        lot_area = to_float_safe(data.get("lote_objetivo", {}).get("area_m2"), 0.0)

        # --- VECINOS ---
        vecinos_curves = []
        for v in data.get("vecinos", []):
            crv = polyline_from_coords(v.get("vertices_3d_local", []), dx, dy, dz)
            if crv:
                vecinos_curves.append(crv)

        # --- VIAS ---
        vias_oficiales = []
        for via in data.get("vias_oficiales", []):
            coords = via.get("coordenadas_local", [])
            if len(coords) >= 2:
                poly = rg.Polyline()
                for c in coords:
                    poly.Add(c[0] - dx, c[1] - dy, c[2] - dz)
                vias_oficiales.append(rg.PolylineCurve(poly))

        # --- ESPACIOS PUBLICOS ---
        espacios_publicos = []
        for ep in data.get("espacios_publicos", []):
            coords = ep.get("coordenadas_local", [])
            crv = polyline_from_coords(coords, dx, dy, dz)
            if crv:
                espacios_publicos.append(crv)

        # --- TOPOGRAFIA ---
        topo = data.get("topografia", {})
        mesh_points = topo.get("malla_terreno", [])
        topo_mesh = build_terrain_mesh(mesh_points, dx, dy, dz) if mesh_points else None

        # --- NORMATIVA ---
        pd = data.get("pot_data", {})
        altura_max_pot = to_float_safe(pd.get("altura_maxima_m"), 11.4)
        tratamiento = str(pd.get("tratamiento", "Consolidacion"))
        rango_edificabilidad = str(pd.get("rango_edificabilidad", "3"))
        sector_normativo = str(pd.get("sector_normativo", ""))
        upz = str(pd.get("upz", "N/A"))
        io_normativo = to_float_safe(pd.get("io_maximo"), 0.70)

        # --- LAYERS JSON (para Tapir) ---
        layers_json = json.dumps(LAYERS_ARCHICAD)

        chip = meta.get("chip", "DESCONOCIDO")
        mensaje = "ETAPA1 v01 | CHIP: {} | Area: {:.1f}m2 | Vecinos: {} | Vias: {} | EP: {} | Origen: ({:.1f}, {:.1f})".format(
            chip, lot_area, len(vecinos_curves), len(vias_oficiales),
            len(espacios_publicos), dx, dy)

    except Exception as e:
        mensaje = "ETAPA1 | ERROR al leer JSON: {}".format(str(e))
