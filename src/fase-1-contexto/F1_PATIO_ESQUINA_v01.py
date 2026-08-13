#! /usr/bin/env python3
"""
F1_PATIO_ESQUINA_v01 - Calculo de patio de aislamiento para lote de esquina.
GH Python Script para Grasshopper (IronPython 2.7 compatible)

PROPOSITO:
En lotes de esquina, la normativa exige un patio de aislamiento en la esquina
INTERIOR (diagonalmente opuesta al cruce de las vias). Este patio garantiza
ventilacion e iluminacion natural al propio edificio y a los vecinos del fondo
de la manzana.

ENTRADAS:
  - lot_polygon: Poligono del lote (polilinea cerrada, Item Access)
  - sides_table_json: JSON string con clasificacion de lados de F1_LADOS_CONFIGURAR
  - building_floors: Numero de pisos proyectados (int)
  - patio_factor: Factor opcional para tamano del patio (default: 1.0 = norma estandar)

SALIDAS:
  - patio_curve: Curva cerrada del patio de aislamiento (para boolean difference)
  - patio_vertex_idx: Indice del vertice interior donde se ubica el patio
  - patio_size_m: Tamano del lado del patio en metros
  - mensaje: String con diagnostico de la operacion

NORMATIVA:
  - Decreto 555/2021: El tamano del patio depende de la altura del edificio.
  - Regla general: patio_min = max(3.0, altura_total * 0.25) metros por lado.
  - Para lotes < 500 m2 con tipologia continua: patio = 3.0m x 3.0m.

v01: Implementacion inicial. Detecta dos frentes adyacentes, localiza la
esquina interior opuesta y genera el rectangulo de patio orientado hacia
el interior del lote.
"""

import Rhino.Geometry as rg
import json
import math

# ============================================================
# FUNCIONES AUXILIARES
# ============================================================

def parse_json_safe(data):
    """Parsear JSON de forma segura (IronPython compatible)."""
    if data is None:
        return {}
    if isinstance(data, str):
        try:
            return json.loads(data)
        except:
            return {}
    if isinstance(data, dict):
        return data
    return {}


def to_float_safe(val, default=0.0):
    """Convertir a float con fallback seguro."""
    if val is None:
        return default
    try:
        return float(val)
    except (ValueError, TypeError):
        return default


def to_int_safe(val, default=4):
    """Convertir a int con fallback seguro."""
    if val is None:
        return default
    try:
        return int(float(val))
    except (ValueError, TypeError):
        return default


def polygon_vertex_count(polyline_curve):
    """Contar vertices unicos de una PolylineCurve cerrada (sin duplicar cierre)."""
    if polyline_curve is None:
        return 0
    success, poly = polyline_curve.TryGetPolyline()
    if not success or poly is None:
        return 0
    # Polilinea cerrada: el ultimo vertice es igual al primero
    count = poly.Count
    if count >= 2:
        first = poly[0]
        last = poly[count - 1]
        if first.DistanceTo(last) < 0.001:
            return count - 1
    return count


def get_polyline_vertices(polyline_curve):
    """Obtener lista de vertices unicos de una PolylineCurve cerrada."""
    success, poly = polyline_curve.TryGetPolyline()
    if not success or poly is None:
        return []
    count = poly.Count
    if count >= 2:
        first = poly[0]
        last = poly[count - 1]
        if first.DistanceTo(last) < 0.001:
            return [poly[i] for i in range(count - 1)]
    return [poly[i] for i in range(count)]


def find_corner_vertices(front_indices, num_vertices):
    """
    Encontrar los vertices de esquina donde convergen dos frentes.
    
    En un lote con segmentos etiquetados, el vertice de esquina (cruce de vias)
    es el vertice compartido por dos segmentos marcados como 'Frontal' que son
    adyacentes en el poligono.
    
    Retorna: (street_corner_idx, interior_corner_idx)
      - street_corner_idx: vertice donde convergen los dos frentes (esquina de calles)
      - interior_corner_idx: vertice diagonalmente opuesto (donde va el patio)
    """
    if len(front_indices) < 2:
        return None, None
    
    # Ordenar los indices frontales
    sorted_fronts = sorted(front_indices)
    
    street_corner = None
    
    # Buscar pares de frentes adyacentes (incluyendo wrap-around)
    for i in range(len(sorted_fronts)):
        a = sorted_fronts[i]
        b = sorted_fronts[(i + 1) % len(sorted_fronts)]
        
        # Verificar adyacencia circular
        diff = abs(a - b)
        if diff == 1 or diff == num_vertices - 1:
            # Encontrados dos frentes adyacentes
            # El vertice compartido es el que esta entre ellos
            # Para segmentos a y a+1, el vertice compartido es (a+1)
            if diff == 1:
                street_corner = max(a, b)  # El vertice final del segmento menor
            else:
                # Wrap-around: segmentos 0 y n-1, el vertice compartido es 0
                street_corner = 0
            break
    
    if street_corner is None:
        # Fallback: dos frentes no adyacentes - buscar la esquina mas probable
        # Usar el vertice donde los dos segmentos frontales estan mas cerca
        if len(sorted_fronts) >= 2:
            street_corner = sorted_fronts[1]  # Asumir que el segundo frente empieza donde termina el primero
    
    # Calcular la esquina interior opuesta (diagonalmente opuesta)
    # Es el vertice a aproximadamente num_vertices/2 posiciones de distancia
    interior_corner = (street_corner + num_vertices // 2) % num_vertices
    
    return street_corner, interior_corner


def calculate_patio_size(building_floors, floor_height=3.0, lot_area=None):
    """
    Calcular el tamano del patio de aislamiento segun normativa.
    
    Regla general (Decreto 555/2021):
    - Para edificios de hasta 5 pisos: patio_min = 3.0m x 3.0m
    - Para edificios mas altos: patio_min = max(3.0, altura_total * 0.25)
    
    Lotes pequenos (< 500 m2) con tipologia continua:
    - Patio fijo de 3.0m x 3.0m independientemente de la altura (max 5 pisos)
    """
    building_height = building_floors * floor_height
    
    # Lotes pequenos: patio fijo
    if lot_area is not None and lot_area < 500.0 and building_floors <= 5:
        return 3.0
    
    # Regla general
    patio_size = max(3.0, building_height * 0.25)
    
    # Redondear a 0.5m mas cercano
    patio_size = round(patio_size * 2.0) / 2.0
    
    return patio_size


def calculate_inward_direction(vertices, corner_idx):
    """
    Calcular el vector hacia el interior del lote desde la esquina interior.
    
    Usa la bisectriz del angulo interior del poligono en ese vertice,
    orientada hacia adentro.
    """
    n = len(vertices)
    if n < 3:
        return rg.Vector3d(1.0, 0.0, 0.0)
    
    # Vertice actual y sus vecinos
    prev_idx = (corner_idx - 1 + n) % n
    next_idx = (corner_idx + 1) % n
    
    v_prev = vertices[prev_idx]
    v_corner = vertices[corner_idx]
    v_next = vertices[next_idx]
    
    # Vectores desde la esquina hacia los vecinos
    vec_to_prev = rg.Vector3d(v_prev.X - v_corner.X, v_prev.Y - v_corner.Y, 0.0)
    vec_to_next = rg.Vector3d(v_next.X - v_corner.X, v_next.Y - v_corner.Y, 0.0)
    
    # Normalizar
    if vec_to_prev.Length > 0.001:
        vec_to_prev.Unitize()
    if vec_to_next.Length > 0.001:
        vec_to_next.Unitize()
    
    # Bisectriz del angulo (promedio de los dos vectores)
    bisector = rg.Vector3d(
        vec_to_prev.X + vec_to_next.X,
        vec_to_prev.Y + vec_to_next.Y,
        0.0
    )
    
    if bisector.Length < 0.001:
        # Angulo muy agudo o colineal - usar perpendicular
        bisector = rg.Vector3d(-vec_to_prev.Y, vec_to_prev.X, 0.0)
    
    bisector.Unitize()
    
    # Verificar que el bisector apunte hacia adentro del poligono
    # Muestrear un punto a lo largo del bisector y verificar inclusion
    test_point = rg.Point3d(
        v_corner.X + bisector.X * 0.5,
        v_corner.Y + bisector.Y * 0.5,
        0.0
    )
    
    # Crear poligono para prueba de inclusion
    poly_pts = [rg.Point3d(v.X, v.Y, 0.0) for v in vertices]
    poly_pts.append(poly_pts[0])  # Cerrar
    test_poly = rg.Polyline(poly_pts)
    
    # Verificar usando punto dentro de poligono (varias aproximaciones)
    inside = point_in_polygon_approx(test_point, vertices)
    
    if not inside:
        # Invertir direccion
        bisector = rg.Vector3d(-bisector.X, -bisector.Y, 0.0)
    
    return bisector


def point_in_polygon_approx(point, vertices):
    """
    Verificar si un punto esta aproximadamente dentro de un poligono.
    Usa ray casting simplificado (IronPython compatible, sin shapely).
    """
    n = len(vertices)
    if n < 3:
        return False
    
    count = 0
    px, py = point.X, point.Y
    
    for i in range(n):
        v1 = vertices[i]
        v2 = vertices[(i + 1) % n]
        
        x1, y1 = v1.X, v1.Y
        x2, y2 = v2.X, v2.Y
        
        # Verificar si el rayo horizontal intersecta el segmento
        if ((y1 > py) != (y2 > py)):
            x_intersect = x1 + (py - y1) * (x2 - x1) / (y2 - y1)
            if px < x_intersect:
                count += 1
    
    return (count % 2) == 1


def create_patio_rectangle(corner_vertex, inward_dir, patio_size):
    """
    Crear un rectangulo de patio centrado en la esquina interior,
    orientado hacia adentro del lote.
    
    El rectangulo se posiciona de modo que:
    - Dos lados son paralelos a los lados del lote que convergen en la esquina
    - El rectangulo se proyecta hacia el interior desde la esquina
    """
    # Vector perpendicular al inward_dir (en plano XY)
    perp = rg.Vector3d(-inward_dir.Y, inward_dir.X, 0.0)
    perp.Unitize()
    
    half = patio_size / 2.0
    
    # Centro del patio: desplazado hacia adentro desde la esquina
    center = rg.Point3d(
        corner_vertex.X + inward_dir.X * half,
        corner_vertex.Y + inward_dir.Y * half,
        0.0
    )
    
    # Cuatro esquinas del rectangulo
    p1 = rg.Point3d(center.X - perp.X * half, center.Y - perp.Y * half, 0.0)
    p2 = rg.Point3d(center.X + perp.X * half, center.Y + perp.Y * half, 0.0)
    p3 = rg.Point3d(
        center.X + inward_dir.X * patio_size + perp.X * half,
        center.Y + inward_dir.Y * patio_size + perp.Y * half,
        0.0
    )
    p4 = rg.Point3d(
        center.X + inward_dir.X * patio_size - perp.X * half,
        center.Y + inward_dir.Y * patio_size - perp.Y * half,
        0.0
    )
    
    # Crear rectangulo (polilinea cerrada)
    pts = [p1, p2, p3, p4, p1]
    return rg.PolylineCurve(pts)


# ============================================================
# MAIN EXECUTION
# ============================================================

# --- OBTENCION SEGURA DE INPUTS ---
lot_polygon = globals().get("lot_polygon", None)
sides_table_raw = globals().get("sides_table_json", None)
building_floors_raw = globals().get("building_floors", 4)

if lot_polygon is None:
    raise ValueError("F1_PATIO_ESQUINA: Falta lot_polygon. Conecte el poligono del lote.")

# Parsear inputs
sides_data = parse_json_safe(sides_table_raw)
building_floors = to_int_safe(building_floors_raw, 4)

# --- 1. EXTRAER CLASIFICACION DE LADOS ---
# El JSON puede venir como lista directa o como dict con clave 'sides'
sides_list = []
if isinstance(sides_data, list):
    sides_list = sides_data
elif isinstance(sides_data, dict):
    sides_list = sides_data.get("sides", sides_data.get("lados", []))

if not sides_list:
    # Sin clasificacion - posiblemente no es esquina o LADOS_CONFIGURAR no conectado
    patio_curve = None
    patio_vertex_idx = -1
    patio_size_m = 0.0
    mensaje = "F1_PATIO_ESQUINA: Sin datos de lados. Conecte sides_table_json desde F1_LADOS_CONFIGURAR."
    # GH outputs: patio_curve, patio_vertex_idx, patio_size_m, mensaje
    raise SystemExit(mensaje)

# Identificar frentes
front_indices = []
for side in sides_list:
    if isinstance(side, dict):
        classification = str(side.get("classification", "")).strip()
        if classification.lower() == "frontal":
            idx = to_int_safe(side.get("side_index", -1))
            if idx >= 0:
                front_indices.append(idx)

mensaje = "F1_PATIO_ESQUINA: "

if len(front_indices) < 2:
    # No es lote de esquina - no se necesita patio
    patio_curve = None
    patio_vertex_idx = -1
    patio_size_m = 0.0
    mensaje += "Solo {} frente(s) detectado(s). No aplica patio de esquina.".format(len(front_indices))
    # GH outputs
    print(mensaje)
else:
    # --- 2. LOTE DE ESQUINA DETECTADO ---
    mensaje += "Lote de esquina detectado ({} frentes). ".format(len(front_indices))
    
    # Obtener vertices del poligono
    vertices = get_polyline_vertices(lot_polygon)
    n_verts = len(vertices)
    
    if n_verts < 4:
        patio_curve = None
        patio_vertex_idx = -1
        patio_size_m = 0.0
        mensaje += "ERROR: Poligono con menos de 4 vertices (n={}).".format(n_verts)
        print(mensaje)
    else:
        # --- 3. LOCALIZAR ESQUINAS ---
        street_corner, interior_corner = find_corner_vertices(front_indices, n_verts)
        
        if street_corner is None or interior_corner is None:
            patio_curve = None
            patio_vertex_idx = -1
            patio_size_m = 0.0
            mensaje += "ERROR: No se pudo identificar la esquina de cruce de vias."
            print(mensaje)
        else:
            mensaje += "Esquina de calles: vertice {}. Esquina interior (patio): vertice {}.".format(
                street_corner, interior_corner)
            
            # --- 4. CALCULAR TAMANO DEL PATIO ---
            # Estimar area del lote
            try:
                amp = rg.AreaMassProperties.Compute(lot_polygon)
                lot_area = amp.Area if amp else None
            except:
                lot_area = None
            
            patio_size_m = calculate_patio_size(building_floors, lot_area=lot_area)
            mensaje += " Patio: {:.1f}m x {:.1f}m ({} pisos).".format(
                patio_size_m, patio_size_m, building_floors)
            
            # --- 5. CALCULAR DIRECCION HACIA ADENTRO ---
            interior_vertex = vertices[interior_corner]
            inward_dir = calculate_inward_direction(vertices, interior_corner)
            
            # --- 6. GENERAR GEOMETRIA DEL PATIO ---
            patio_curve = create_patio_rectangle(interior_vertex, inward_dir, patio_size_m)
            patio_vertex_idx = interior_corner
            
            mensaje += " Direccion interior: ({:.2f}, {:.2f}).".format(
                inward_dir.X, inward_dir.Y)
            
            print(mensaje)

# ============================================================
# OUTPUTS para Grasshopper
# ============================================================
# patio_curve (Curve) - geometria del patio para sustraer
# patio_vertex_idx (int) - indice del vertice interior
# patio_size_m (float) - tamano del patio en metros
# mensaje (str) - diagnostico
