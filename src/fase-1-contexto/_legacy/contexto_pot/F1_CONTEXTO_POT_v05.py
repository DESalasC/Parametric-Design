#! /usr/bin/env python3
"""
================================================================================
F1_CONTEXTO_POT_v05.py — Lector del JSON de contexto v6
Proyecto: DisenoParametrico / Fase 1
GH Python Script para Grasshopper (IronPython 2.7 compatible)
================================================================================

PROPOSITO:
  Leer el JSON de cache v6, convertir datos en geometria Rhino,
  DESPLAZAR todo el sistema a la esquina del lote (0,0,0),
  y generar malla de terreno triangulada.

ENTRADAS:
  json_path (String) — Ruta al archivo <CHIP>-contexto.json

SALIDAS:
  lot_curve (Curve)             — Perimetro del lote desplazado al origen
  neighbors_curves (Curve[])    — Perimetros de vecinos desplazados
  vias_oficiales (Curve[])      — Eje_vial + MallaIntermedia + VialArterial
  topo_mesh (Mesh)              — Malla de terreno triangulada
  altura_max_pot (Number)       — Altura maxima segun POT [m]
  tratamiento (String)          — Tipo de tratamiento urbanistico
  rango_edificabilidad (String) — Rango "1".."5"
  upz (String)                  — Nombre de la UPZ
  area_lote_m2 (Number)         — Area del lote en m2
  origen_x (Number)             — Coordenada X del origen SIRGAS usada
  origen_y (Number)             — Coordenada Y del origen SIRGAS usada
  mensaje (String)              — Diagnostico

VERSIONES:
  v05.1 — Agregado desplazamiento al origen del lote + mesh de terreno
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


def apply_offset(point3d, dx, dy, dz):
    """Aplica desplazamiento a un punto."""
    return rg.Point3d(point3d.X - dx, point3d.Y - dy, point3d.Z - dz)


def vertices_to_polyline(vertices_3d, dx=0, dy=0, dz=0):
    """Convierte [[x,y,z],...] en PolylineCurve cerrada."""
    if not vertices_3d or len(vertices_3d) < 3:
        return None
    poly = rg.Polyline()
    for v in vertices_3d:
        poly.Add(v[0] - dx, v[1] - dy, v[2] - dz)
    if not poly.IsClosed:
        poly.Add(poly[0])
    return rg.PolylineCurve(poly)


def build_terrain_mesh(mesh_points, dx=0, dy=0, dz=0):
    """
    Construye malla de terreno triangulada desde los puntos de topografia.

    Usa los vertices del lote como borde, los puntos medios como refinamiento,
    y el centroide como punto central para triangulacion en abanico.
    """
    if not mesh_points or len(mesh_points) < 3:
        return None

    pts = [rg.Point3d(p["x_local"] - dx, p["y_local"] - dy, p["z_local"] - dz)
           for p in mesh_points]

    mesh = rg.Mesh()

    # Agregar todos los puntos como vertices del mesh
    for pt in pts:
        mesh.Vertices.Add(pt)

    n = len(pts)

    # El ultimo punto es el centroide (generate_lote_topo_points lo pone al final)
    # Los primeros n_verts son los vertices del lote
    # Los siguientes son los puntos medios de cada lado
    # Usamos el centroide para triangular en abanico

    if n >= 4:
        centroid_idx = n - 1

        # Triangular: cada par de vertices consecutivos del lote + centroide
        # Pero como no sabemos cuantos son vertices vs midpoints exactamente,
        # simplemente creamos triangulos entre el centroide y puntos alternados
        for i in range(n - 1):
            j = (i + 1) % (n - 1)
            # Solo triangular si los puntos no son colineales (distancia minima)
            d1 = pts[i].DistanceTo(pts[j])
            d2 = pts[i].DistanceTo(pts[centroid_idx])
            d3 = pts[j].DistanceTo(pts[centroid_idx])
            if min(d1, d2, d3) > 0.01:
                mesh.Faces.AddFace(i, centroid_idx, j)

    # Si no se generaron caras, intentar triangulacion simple secuencial
    if mesh.Faces.Count == 0 and n >= 3:
        for i in range(1, n - 1):
            mesh.Faces.AddFace(0, i, i + 1)

    mesh.Normals.ComputeNormals()
    mesh.Compact()
    return mesh


def build_terrain_mesh_delaunay(mesh_points, lot_vertices, dx=0, dy=0, dz=0):
    """
    Alternativa: triangulacion de Delaunay 2D sobre el plano XY usando 
    los puntos del terreno, proyectando Z.
    
    Como IronPython no tiene scipy, hacemos una aproximacion:
    crear mesh desde componentes nativos de GH es mejor, pero aqui
    damos una malla funcional basada en grilla.
    """
    if not mesh_points or len(mesh_points) < 3:
        return None

    # Crear nube de puntos
    pts = []
    for p in mesh_points:
        x = p["x_local"] - dx
        y = p["y_local"] - dy
        z = p["z_local"] - dz
        pts.append(rg.Point3d(x, y, z))

    # Construir mesh por triangulacion sobre el bounding box
    # Encontramos los limites
    min_x = min(p.X for p in pts)
    max_x = max(p.X for p in pts)
    min_y = min(p.Y for p in pts)
    max_y = max(p.Y for p in pts)

    # Crear una grilla de resolucion ~5m
    res = 5.0
    cols = max(2, int((max_x - min_x) / res) + 1)
    rows = max(2, int((max_y - min_y) / res) + 1)

    mesh = rg.Mesh()

    # Crear vertices de la grilla
    grid_pts = []
    for r in range(rows):
        for c in range(cols):
            gx = min_x + c * (max_x - min_x) / max(1, cols - 1)
            gy = min_y + r * (max_y - min_y) / max(1, rows - 1)

            # Interpolar Z usando los puntos mas cercanos
            gz = 0.0
            total_w = 0.0
            for pt in pts:
                dist = math.sqrt((gx - pt.X)**2 + (gy - pt.Y)**2)
                if dist < 0.01:
                    gz = pt.Z
                    total_w = 1.0
                    break
                w = 1.0 / max(0.1, dist * dist)
                gz += pt.Z * w
                total_w += w

            if total_w > 0:
                gz /= total_w
            else:
                gz = 0.0

            idx = mesh.Vertices.Add(gx, gy, gz)
            grid_pts.append(idx)

    # Crear caras (2 triangulos por celda)
    for r in range(rows - 1):
        for c in range(cols - 1):
            a = grid_pts[r * cols + c]
            b = grid_pts[r * cols + c + 1]
            c_idx = grid_pts[(r + 1) * cols + c]
            d = grid_pts[(r + 1) * cols + c + 1]
            mesh.Faces.AddFace(a, b, d)
            mesh.Faces.AddFace(a, d, c_idx)

    mesh.Normals.ComputeNormals()
    mesh.Compact()
    return mesh


# ==============================================================================
# MAIN
# ==============================================================================

json_path_raw = globals().get("json_path", None)
json_path = str(unwrap(json_path_raw)).strip("[]'\" ") if json_path_raw else ""

if not json_path or not os.path.exists(json_path):
    lot_curve = None
    neighbors_curves = []
    vias_oficiales = []
    espacios_publicos = []
    topo_mesh = None
    altura_max_pot = 11.4
    tratamiento = "Consolidacion"
    rango_edificabilidad = "3"
    sector_normativo = ""
    upz = "N/A"
    area_lote_m2 = 0.0
    origen_x = 0.0
    origen_y = 0.0
    mensaje = "ERROR: No se encontro el JSON en: {}".format(json_path)
else:
    try:
        with io.open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # --- CALCULAR OFFSET: vertice mas al SUR (min Y) y mas al ORIENTE (max X) ---
        lote_verts = data.get("lote_objetivo", {}).get("vertices_3d_local", [])
        if lote_verts and len(lote_verts) >= 3:
            # Buscar el vertice SE: minimo Y (sur), maximo X (oriente)
            anchor = lote_verts[0]
            for v in lote_verts:
                # Prioridad: Y mas pequeno (sur), en caso de empate X mas grande (oriente)
                if v[1] < anchor[1] - 0.01 or (abs(v[1] - anchor[1]) < 0.01 and v[0] > anchor[0]):
                    anchor = v
            dx, dy, dz = anchor[0], anchor[1], anchor[2]
        else:
            dx, dy, dz = 0.0, 0.0, 0.0

        # Guardar origen SIRGAS para referencia
        meta = data.get("metadata", {})
        origen_sirgas = meta.get("origen_sirgas", {})
        origen_x = origen_sirgas.get("x", 0.0)
        origen_y = origen_sirgas.get("y", 0.0)

        # --- LOTE ---
        lot_curve = vertices_to_polyline(lote_verts, dx, dy, dz)
        area_lote_m2 = data.get("lote_objetivo", {}).get("area_m2", 0.0)

        # --- VECINOS ---
        neighbors_curves = []
        for v in data.get("vecinos", []):
            crv = vertices_to_polyline(v.get("vertices_3d_local", []), dx, dy, dz)
            if crv:
                neighbors_curves.append(crv)

        # --- VIAS OFICIALES ---
        vias_oficiales = []
        for via in data.get("vias_oficiales", []):
            coords = via.get("coordenadas_local", [])
            if len(coords) >= 2:
                poly = rg.Polyline()
                for c in coords:
                    poly.Add(c[0] - dx, c[1] - dy, c[2] - dz)
                vias_oficiales.append(rg.PolylineCurve(poly))

        # --- TOPOGRAFIA: MALLA DE TERRENO ---
        topo = data.get("topografia", {})
        mesh_points = topo.get("malla_terreno", [])
        if mesh_points and len(mesh_points) >= 3:
            topo_mesh = build_terrain_mesh_delaunay(mesh_points, lote_verts, dx, dy, dz)
        else:
            topo_mesh = None

        # --- POT DATA ---
        pd = data.get("pot_data", {})
        altura_max_pot = to_float_safe(pd.get("altura_maxima_m"), 11.4)
        tratamiento = str(pd.get("tratamiento", "Consolidacion"))
        rango_edificabilidad = str(pd.get("rango_edificabilidad", "3"))
        sector_normativo = str(pd.get("sector_normativo", ""))
        upz = str(pd.get("upz", "N/A"))

        # --- ESPACIOS PUBLICOS ---
        espacios_publicos = []
        for ep in data.get("espacios_publicos", []):
            coords = ep.get("coordenadas_local", [])
            if len(coords) >= 3:
                poly = rg.Polyline()
                for c in coords:
                    poly.Add(c[0] - dx, c[1] - dy, c[2] - dz)
                if not poly.IsClosed:
                    poly.Add(poly[0])
                espacios_publicos.append(rg.PolylineCurve(poly))

        chip = meta.get("chip", "DESCONOCIDO")

        mensaje = "CONTEXTO v05 | CHIP: {} | UPZ: {} | Sector: {} | Trat: {} | Hmax: {:.1f}m | Rango: {} | Area: {:.1f}m2 | Vecinos: {} | Vias: {} | EP: {} | Origen: ({:.1f}, {:.1f})".format(
            chip, upz, sector_normativo, tratamiento, altura_max_pot, rango_edificabilidad,
            area_lote_m2, len(neighbors_curves), len(vias_oficiales),
            len(espacios_publicos), dx, dy)

        print(mensaje)

    except Exception as e:
        lot_curve = None
        neighbors_curves = []
        vias_oficiales = []
        espacios_publicos = []
        topo_mesh = None
        altura_max_pot = 11.4
        tratamiento = "Consolidacion"
        rango_edificabilidad = "3"
        sector_normativo = ""
        upz = "N/A"
        area_lote_m2 = 0.0
        origen_x = 0.0
        origen_y = 0.0
        mensaje = "ERROR al leer JSON: {}".format(str(e))
        print(mensaje)
