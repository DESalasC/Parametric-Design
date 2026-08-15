#! /usr/bin/env python3
"""
F1_VERTICE_CERCANO_v01.py — Vértice del lote más cercano a una esquina del BBox.
GH Python Script para Grasshopper (IronPython 2.7 compatible)

ENTRADA: lot_polygon (Curve), corner_A (Point3d)
SALIDA:  closest_vertex (Point3d), vertex_index (int)
"""
import Rhino.Geometry as rg

raw_lot = globals().get("lot_polygon", None)
raw_corner = globals().get("corner_A", None)

# Desenvolver listas unitarias (Grasshopper Item Access wrapping)
lot_polygon = raw_lot
if isinstance(lot_polygon, list):
    if len(lot_polygon) > 0:
        lot_polygon = lot_polygon[0]
    else:
        lot_polygon = None

corner_A = raw_corner
if isinstance(corner_A, list):
    if len(corner_A) > 0:
        corner_A = corner_A[0]
    else:
        corner_A = None

closest_vertex = None
vertex_index = -1

if lot_polygon is not None and corner_A is not None:
    try:
        # IronPython: TryGetPolyline retorna (bool, Polyline)
        result = lot_polygon.TryGetPolyline()
        if isinstance(result, tuple):
            success, poly = result
        else:
            success = result is not None
            poly = result
        
        if success and poly is not None and hasattr(poly, 'Count') and poly.Count >= 2:
            # Detectar si está cerrada (último punto = primero)
            n = poly.Count
            if poly[0].DistanceTo(poly[n - 1]) < 0.001:
                n = n - 1
            
            if n > 0:
                min_dist = float('inf')
                for i in range(n):
                    d = poly[i].DistanceTo(corner_A)
                    if d < min_dist:
                        min_dist = d
                        closest_vertex = rg.Point3d(poly[i].X, poly[i].Y, poly[i].Z)
                        vertex_index = i
    except Exception as e:
        print("VERTICE_CERCANO error: " + str(e))
