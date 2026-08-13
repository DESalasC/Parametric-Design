#! /usr/bin/env python3
"""
F1_PATIO_ESQUINA_v02 - Calculo de patio de aislamiento para lote de esquina.
GH Python Script (IronPython 2.7)

v02 - Correcciones:
  - building_floors YA NO es input externo (rompia el ciclo 119->161->119).
    Los pisos se leen del JSON de regulacion (rango_edificabilidad).
  - sides_table_json acepta List Access (lista de JSON por lado).
  - Geometria del patio: rectangulo alineado con los bordes del lote en la
    esquina interior, sin lineas infinitas.
  - Deteccion robusta del vertice de cruce de calles.

ENTRADAS:
  lot_polygon      — Poligono del lote (Item Access)
  sides_table_json — JSON de F1_LADOS_CONFIGURAR (List Access)
  json_path        — Ruta al cache JSON del lote

SALIDAS:
  patio_curve      — Rectangulo del patio (Curve)
  patio_vertex_idx — Indice del vertice interior donde va el patio
  patio_size_m     — Tamano del lado del patio (m)
  mensaje          — Diagnostico
"""

import Rhino.Geometry as rg
import json
import os

# ============================================================
# HELPERS
# ============================================================
def parse_json_safe(data):
    if data is None: return {}
    if isinstance(data, str):
        try: return json.loads(data)
        except: return {}
    if isinstance(data, (dict, list)): return data
    return {}

def to_int_safe(val, default=4):
    if val is None: return default
    try:
        v = int(float(val))
        if v <= 0: return default
        return v
    except: return default

def get_vertices(curve):
    if curve is None: return []
    success, poly = curve.TryGetPolyline()
    if not success or poly is None: return []
    c = poly.Count
    if c >= 2 and poly[0].DistanceTo(poly[c-1]) < 0.001:
        return [poly[i] for i in range(c-1)]
    return [poly[i] for i in range(c)]


# ============================================================
# MAIN
# ============================================================

lot_polygon_raw  = globals().get("lot_polygon", None)
sides_table_raw  = globals().get("sides_table_json", None)
json_path_raw    = globals().get("json_path", None)

# Unwrap si es lista unitaria
if isinstance(lot_polygon_raw, list) and len(lot_polygon_raw) == 1:
    lot_polygon_raw = lot_polygon_raw[0]
lot_polygon = lot_polygon_raw

json_path = str(json_path_raw).strip("[]'\" ") if json_path_raw else ""

if lot_polygon is None:
    patio_curve = None
    patio_vertex_idx = -1
    patio_size_m = 0.0
    mensaje = "ERROR: lot_polygon es None"
    print(mensaje)
else:
    # --- 1. PISOS DESDE REGULACION (no input externo, rompe ciclo) ---
    building_floors = 4  # default
    rango_edif = "3"
    
    if json_path and os.path.exists(json_path):
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            pd = data.get("pot_data", {})
            rango_edif = str(pd.get("rango_edificabilidad", "3"))
        except:
            pass
    
    RANGO_PISOS = {"1": 2, "2": 3, "3": 5, "4": 8, "5": 12}
    building_floors = RANGO_PISOS.get(rango_edif, 5)
    
    # --- 2. CLASIFICACION DE LADOS ---
    sides_data = parse_json_safe(sides_table_raw)
    sides_list = []
    
    if isinstance(sides_data, list):
        # List Access: puede ser lista de dicts o lista de strings JSON
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
        sides_list = sides_data.get("sides", sides_data.get("lados", []))
        if not isinstance(sides_list, list):
            sides_list = []
    
    # --- 3. IDENTIFICAR FRENTES ---
    front_indices = []
    for side in sides_list:
        if isinstance(side, dict):
            cls = str(side.get("classification", "")).strip().lower()
            if cls == "frontal":
                idx = to_int_safe(side.get("side_index", -1))
                if idx >= 0:
                    front_indices.append(idx)
    
    vertices = get_vertices(lot_polygon)
    n_verts = len(vertices)
    
    if len(front_indices) < 2:
        patio_curve = None
        patio_vertex_idx = -1
        patio_size_m = 0.0
        mensaje = "Solo {} frente(s). No aplica patio de esquina.".format(len(front_indices))
        print(mensaje)
    elif n_verts < 4:
        patio_curve = None
        patio_vertex_idx = -1
        patio_size_m = 0.0
        mensaje = "ERROR: < 4 vertices (n={})".format(n_verts)
        print(mensaje)
    else:
        # --- 4. BUSCAR ESQUINA DE CALLES ---
        # Dos frentes adyacentes: el vertice entre ellos es la esquina de calles
        sorted_fr = sorted(front_indices)
        street_corner = None
        
        for i in range(len(sorted_fr)):
            a = sorted_fr[i]
            b = sorted_fr[(i+1) % len(sorted_fr)]
            diff = abs(a - b)
            if diff == 1:
                street_corner = b  # vertice entre segmentos a y a+1
                break
            elif diff == n_verts - 1:
                street_corner = 0  # wrap-around: segmentos 0 y n-1
                break
        
        if street_corner is None and len(sorted_fr) >= 2:
            # Fallback: usar el vertice al final del primer frente
            street_corner = (sorted_fr[0] + 1) % n_verts
        
        if street_corner is None:
            patio_curve = None
            patio_vertex_idx = -1
            patio_size_m = 0.0
            mensaje = "ERROR: no se pudo identificar esquina de calles"
            print(mensaje)
        else:
            # --- 5. ESQUINA INTERIOR (opuesta) ---
            interior_corner = (street_corner + n_verts // 2) % n_verts
            
            # --- 6. TAMANO DEL PATIO ---
            # Lotes < 500 m2, tipologia continua, <= 5 pisos: patio fijo 3x3m
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
            
            # --- 7. GEOMETRIA DEL PATIO ---
            # Rectangulo alineado con los DOS bordes que convergen en la esquina interior.
            # Los bordes del patio son paralelos a los lados del lote.
            
            v_interior = vertices[interior_corner]
            v_prev = vertices[(interior_corner - 1 + n_verts) % n_verts]
            v_next = vertices[(interior_corner + 1) % n_verts]
            
            # Direccion de los bordes del lote en la esquina interior
            edge1 = rg.Vector3d(v_prev.X - v_interior.X, v_prev.Y - v_interior.Y, 0)
            edge2 = rg.Vector3d(v_next.X - v_interior.X, v_next.Y - v_interior.Y, 0)
            
            len1 = edge1.Length
            len2 = edge2.Length
            if len1 < 0.001 or len2 < 0.001:
                edge1 = rg.Vector3d(1, 0, 0)
                edge2 = rg.Vector3d(0, 1, 0)
            else:
                edge1.Unitize()
                edge2.Unitize()
            
            # Determinar hacia donde esta el interior del lote
            # Muestrear un punto a poca distancia en ambas direcciones posibles
            # y verificar cual cae dentro del poligono
            
            test_dist = patio_size_m * 1.5
            
            # Direccion candidata: bisectriz del angulo interior
            bisector = rg.Vector3d(edge1.X + edge2.X, edge1.Y + edge2.Y, 0)
            if bisector.Length < 0.001:
                bisector = rg.Vector3d(-edge1.Y, edge1.X, 0)
            bisector.Unitize()
            
            test_pt = rg.Point3d(
                v_interior.X + bisector.X * test_dist,
                v_interior.Y + bisector.Y * test_dist, 0)
            
            # Ray casting para ver si test_pt esta dentro del lote
            inside = False
            count = 0
            px, py = test_pt.X, test_pt.Y
            for j in range(n_verts):
                v1 = vertices[j]
                v2 = vertices[(j+1) % n_verts]
                x1, y1 = v1.X, v1.Y
                x2, y2 = v2.X, v2.Y
                if ((y1 > py) != (y2 > py)):
                    x_int = x1 + (py - y1) * (x2 - x1) / (y2 - y1)
                    if px < x_int:
                        count += 1
            inside = (count % 2) == 1
            
            if not inside:
                bisector = rg.Vector3d(-bisector.X, -bisector.Y, 0)
            
            # Construir rectangulo del patio
            # Esquina del patio en el vertice interior
            # El rectangulo se extiende hacia adentro a lo largo del bisector
            # y tiene lados paralelos a los bordes del lote
            
            perp = rg.Vector3d(-bisector.Y, bisector.X, 0)
            perp.Unitize()
            
            s = patio_size_m
            
            # Cuatro esquinas del patio, alineado con los bordes del lote
            # Usamos edge1 y edge2 como ejes locales
            # El patio es un cuadrado de s x s
            
            # Punto de partida: vertice interior
            p0 = rg.Point3d(v_interior.X, v_interior.Y, 0)
            
            # Determinar cual edge es mas horizontal y cual mas vertical
            # para orientar el rectangulo correctamente
            dot = edge1.X * edge2.X + edge1.Y * edge2.Y
            if abs(dot) < 0.99:
                # No son colineales: usar ambos edges como ejes
                # El rectangulo se alinea con los bordes del lote
                
                # Proyectar s a lo largo de cada edge
                p1 = rg.Point3d(p0.X + edge1.X * s, p0.Y + edge1.Y * s, 0)
                p2 = rg.Point3d(p1.X + edge2.X * s, p1.Y + edge2.Y * s, 0)
                p3 = rg.Point3d(p0.X + edge2.X * s, p0.Y + edge2.Y * s, 0)
                
                pts = [p0, p1, p2, p3, p0]
            else:
                # Colineales: usar bisector + perpendicular
                p1 = rg.Point3d(p0.X + bisector.X * s, p0.Y + bisector.Y * s, 0)
                p2 = rg.Point3d(p1.X + perp.X * s, p1.Y + perp.Y * s, 0)
                p3 = rg.Point3d(p0.X + perp.X * s, p0.Y + perp.Y * s, 0)
                pts = [p0, p1, p2, p3, p0]
            
            patio_curve = rg.PolylineCurve(pts)
            patio_vertex_idx = interior_corner
            
            mensaje = "Esquina calles: v{}. Interior: v{}. Patio: {:.1f}x{:.1f}m ({} pisos, rango {})".format(
                street_corner, interior_corner, patio_size_m, patio_size_m, building_floors, rango_edif)
            print(mensaje)
