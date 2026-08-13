#! /usr/bin/env python3
"""
================================================================================
F1_DESPLAZAR_ORIGEN_v01.py — Desplaza toda la geometría al origen (0,0,0)
GH Python Script para Grasshopper (IronPython 2.7 compatible)

PROPÓSITO:
  Toma el polígono del lote, encuentra la esquina inferior de su BoundingBox
  (mínimo X, mínimo Y), calcula un vector desde esa esquina hacia (0,0,0),
  y aplica ese vector a TODA la geometría de entrada.

  Esto asegura que el lote, vecinos, vías y zonas verdes queden anclados al
  origen de coordenadas de Rhino/ArchiCAD, eliminando problemas de escala y
  precisión al trabajar con coordenadas SIRGAS (~1'000,000 m).

UBICACIÓN EN EL CANVAS:
  Colocar INMEDIATAMENTE después de Tapir ReceiveGeometry, antes de cualquier
  otro procesamiento.

ENTRADAS (8):
  ┌──────────────────┬──────────┬──────────────────────────────────────────┐
  │ Nombre           │ Tipo     │ Descripción                              │
  ├──────────────────┼──────────┼──────────────────────────────────────────┤
  │ lot_polygon      │ Curve    │ Polígono del lote (Item Access)          │
  │ lot_segments     │ Curve[]  │ Segmentos del lote (List Access)         │
  │ lot_midpoints    │ Point3d[]│ Puntos medios de segmentos (List Access) │
  │ lot_centroid     │ Point3d  │ Centroide del lote                       │
  │ vecinos_curves   │ Curve[]  │ Polígonos de predios vecinos             │
  │ street_curves    │ Curve[]  │ Curvas de vías                           │
  │ green_curves     │ Curve[]  │ Zonas verdes / espacio público           │
  │ topo_mesh        │ Mesh     │ Malla topográfica (opcional)             │
  └──────────────────┴──────────┴──────────────────────────────────────────┘

SALIDAS (8 + diagnóstico):
  Mismas entradas pero desplazadas al origen, más:
  ┌──────────────────┬──────────┬──────────────────────────────────────────┐
  │ Nombre           │ Tipo     │ Descripción                              │
  ├──────────────────┼──────────┼──────────────────────────────────────────┤
  │ offset_vector    │ Vector3d │ Vector de desplazamiento aplicado        │
  │ offset_magnitude │ Number   │ Magnitud del desplazamiento en metros    │
  │ mensaje          │ String   │ Diagnóstico de la operación              │
  └──────────────────┴──────────┴──────────────────────────────────────────┘
================================================================================
"""

import Rhino.Geometry as rg

# ==============================================================================
# ENTRADAS
# ==============================================================================
lot_polygon   = globals().get("lot_polygon", None)
lot_segments  = globals().get("lot_segments", [])
lot_midpoints = globals().get("lot_midpoints", [])
lot_centroid  = globals().get("lot_centroid", None)
vecinos_curves = globals().get("vecinos_curves", [])
street_curves  = globals().get("street_curves", [])
green_curves   = globals().get("green_curves", None) or []
topo_mesh      = globals().get("topo_mesh", None)

# Normalizar listas
if lot_segments is None: lot_segments = []
if not isinstance(lot_segments, list): lot_segments = [lot_segments]
if lot_midpoints is None: lot_midpoints = []
if not isinstance(lot_midpoints, list): lot_midpoints = [lot_midpoints]
if vecinos_curves is None: vecinos_curves = []
if not isinstance(vecinos_curves, list): vecinos_curves = [vecinos_curves]
if street_curves is None: street_curves = []
if not isinstance(street_curves, list): street_curves = [street_curves]
if green_curves is None: green_curves = []
if not isinstance(green_curves, list): green_curves = [green_curves]

# ==============================================================================
# CÁLCULO DEL DESPLAZAMIENTO
# ==============================================================================

offset_vector = rg.Vector3d(0, 0, 0)
offset_magnitude = 0.0
mensaje = ""

if lot_polygon is None:
    mensaje = "ERROR: lot_polygon es None. No se puede calcular desplazamiento."
    print(mensaje)
else:
    try:
        # Obtener BoundingBox del lote
        bbox = lot_polygon.GetBoundingBox(rg.Plane.WorldXY)
        min_corner = bbox.Min
        
        print("=== DESPLAZAR_ORIGEN v01 ===")
        print("BoundingBox lote: Min=({:.1f}, {:.1f}) Max=({:.1f}, {:.1f})".format(
            bbox.Min.X, bbox.Min.Y, bbox.Max.X, bbox.Max.Y))
        
        # Calcular vector: desde esquina SW del bbox hacia (0,0,0)
        offset_vector = rg.Vector3d(-min_corner.X, -min_corner.Y, -min_corner.Z)
        offset_magnitude = offset_vector.Length
        
        print("Vector desplazamiento: ({:.1f}, {:.1f}, {:.1f}) | {:.1f} m".format(
            offset_vector.X, offset_vector.Y, offset_vector.Z, offset_magnitude))
        
        # Si ya estamos cerca del origen, no hacer nada
        if offset_magnitude < 0.01:
            mensaje = "Geometría ya está en el origen (offset < 1cm). Sin cambios."
            print(mensaje)
        else:
            # Crear transformación de traslación
            xform = rg.Transform.Translation(offset_vector)
            
            # Aplicar a todas las geometrías
            count = 0
            
            # Lote
            if lot_polygon is not None:
                lot_polygon.Transform(xform)
                count += 1
            
            # Segmentos
            for seg in lot_segments:
                if seg is not None:
                    seg.Transform(xform)
                    count += 1
            
            # Puntos medios
            for pt in lot_midpoints:
                if pt is not None:
                    pt.Transform(xform)
                    count += 1
            
            # Centroide
            if lot_centroid is not None:
                lot_centroid.Transform(xform)
                count += 1
            
            # Vecinos
            for v in vecinos_curves:
                if v is not None:
                    v.Transform(xform)
                    count += 1
            
            # Calles
            for s in street_curves:
                if s is not None:
                    s.Transform(xform)
                    count += 1
            
            # Zonas verdes
            for g in green_curves:
                if g is not None:
                    g.Transform(xform)
                    count += 1
            
            # Malla topográfica
            if topo_mesh is not None:
                topo_mesh.Transform(xform)
                count += 1
            
            mensaje = "Desplazamiento OK: {} objetos movidos {:.1f}m al origen (0,0,0). BBox original: ({:.1f},{:.1f})".format(
                count, offset_magnitude, min_corner.X, min_corner.Y)
            print(mensaje)
            
            # Verificar resultado
            new_bbox = lot_polygon.GetBoundingBox(rg.Plane.WorldXY)
            print("BoundingBox lote DESPUÉS: Min=({:.1f}, {:.1f}) Max=({:.1f}, {:.1f})".format(
                new_bbox.Min.X, new_bbox.Min.Y, new_bbox.Max.X, new_bbox.Max.Y))
    
    except Exception as e:
        mensaje = "ERROR en desplazamiento: {}".format(str(e))
        print(mensaje)
        # Si falla, al menos devolver geometría sin modificar

print("=== FIN DESPLAZAR_ORIGEN ===")
