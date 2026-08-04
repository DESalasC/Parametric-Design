"""
Script: F1_CONTEXTO_POT_v03.py
Proyecto: DiseñoParametrico
Fase: 1 - Contexto y Lote (Integración ArchiCAD)
Versión: 03
Descripción: 
    Lee el JSON de contexto generado por fetch-urban-context-v1.py.
    Ancla la esquina Sur-Occidente global del conjunto al origen (0,0,0).
    Separa la geometría en: Lote (2D), Vecinos (2D) y Espacio Público (Vías/Andenes).
    Genera una Malla de Terreno 3D nativa de Rhino (Delaunay).
    Entrega curvas planares cerradas listas para los componentes Tapir Polyline.
Directriz: ADR-007
"""

import Rhino
import json
import os
import ghpythonlib.components as ghcomp

# Inputs de Grasshopper:
# json_path: string (Ruta al archivo *-contexto.json)

# 1. Inicializar todas las salidas para evitar <null> o colapsos del componente
lote_curve = None
neighbors_curves = None
public_space_curve = None
topo_mesh = None
metadata_str = "Esperando JSON válido..."

if json_path and os.path.exists(json_path):
    try:
        with open(json_path, 'r') as f:
            data = json.load(f)
            
        # 2. Extraer Metadatos para impresión en consola/panel
        metadata = data.get("metadata", {})
        origen = metadata.get("origen_sirgas", {})
        metadata_str = "CHIP: {}\nOrigen SIRGAS: X={:.2f}, Y={:.2f}, Z={:.2f}\nAzimuth: {:.2f}\nNota: Esquina Sur-Occidente global anclada al (0,0,0).".format(
            metadata.get("chip", "N/A"),
            origen.get('x', 0), origen.get('y', 0), origen.get('z', 0),
            metadata.get("azimuth_norte_grados", 0)
        )
        print(metadata_str)
        
        # 3. Recopilar TODOS los vértices para encontrar el Min X y Min Y global
        # Esto garantiza que todo el contexto (lote + vecinos) quede en el cuadrante positivo.
        lote_verts = data.get("lote_objetivo", {}).get("vertices_3d_local", [])
        vecinos_data = data.get("vecinos", [])
        
        all_x = []
        all_y = []
        for v in lote_verts:
            all_x.append(v[0]); all_y.append(v[1])
        for vecino in vecinos_data:
            for v in vecino.get("vertices_3d_local", []):
                all_x.append(v[0]); all_y.append(v[1])
                
        offset_x = min(all_x) if all_x else 0
        offset_y = min(all_y) if all_y else 0

        # Función auxiliar para crear curva 2D cerrada aplicando el offset
        def create_closed_2d_curve(verts):
            pts = [Rhino.Geometry.Point3d(v[0] - offset_x, v[1] - offset_y, 0.0) for v in verts]
            if len(pts) > 0 and pts[0] != pts[-1]: 
                pts.append(pts[0])
            return Rhino.Geometry.PolylineCurve(pts)

        # 4. Generar curvas del Lote y Vecinos
        lote_curve = create_closed_2d_curve(lote_verts) if lote_verts else None
        
        neighbors_curves = []
        for vecino in vecinos_data:
            verts = vecino.get("vertices_3d_local", [])
            if verts: 
                neighbors_curves.append(create_closed_2d_curve(verts))
                
        # 5. Calcular Área de Contexto (75m) y Separar Vías (Espacio Público)
        # Se usa RhinoCommon puro (CreateBooleanDifference) para evitar conversiones internas a Brep/Surface.
        if lote_curve or neighbors_curves:
            all_pts = []
            if lote_curve:
                for i in range(lote_curve.PointCount): all_pts.append(lote_curve.PointAt(i))
            for nc in neighbors_curves:
                for i in range(nc.PointCount): all_pts.append(nc.PointAt(i))
                
            if all_pts:
                min_x = min(p.X for p in all_pts) - 75
                max_x = max(p.X for p in all_pts) + 75
                min_y = min(p.Y for p in all_pts) - 75
                max_y = max(p.Y for p in all_pts) + 75
                
                bbox_pts = [
                    Rhino.Geometry.Point3d(min_x, min_y, 0),
                    Rhino.Geometry.Point3d(max_x, min_y, 0),
                    Rhino.Geometry.Point3d(max_x, max_y, 0),
                    Rhino.Geometry.Point3d(min_x, max_y, 0),
                    Rhino.Geometry.Point3d(min_x, min_y, 0)
                ]
                context_boundary = Rhino.Geometry.PolylineCurve(bbox_pts)
                
                private_curves = []
                if lote_curve: private_curves.append(lote_curve)
                private_curves.extend(neighbors_curves)
                
                try:
                    diff_result = Rhino.Geometry.Curve.CreateBooleanDifference(context_boundary, private_curves)
                    if diff_result and len(diff_result) > 0:
                        public_space_curve = list(diff_result)
                    else:
                        public_space_curve = [context_boundary]
                except Exception as e:
                    print("Error calculando vías: " + str(e))
                    public_space_curve = [context_boundary]
                        
        # 6. Topografía (Malla Delaunay 3D aplicando el offset en X,Y)
        # Se mantiene la Z original para respetar la topografía estimada.
        topo_pts_data = data.get("topografia", {}).get("malla_terreno", [])
        if topo_pts_data:
            topo_points = [Rhino.Geometry.Point3d(p["x_local"] - offset_x, p["y_local"] - offset_y, p["z_local"]) for p in topo_pts_data]
            topo_mesh = ghcomp.DelaunayMesh(topo_points)
        else:
            topo_mesh = None

    except Exception as e:
        metadata_str = "ERROR GRAVE: " + str(e)
        print("ERROR: " + str(e))

# Salidas en Grasshopper (Asegurar que no tengan Type Hint configurado):
# a -> lote_curve
# b -> neighbors_curves
# c -> public_space_curve
# d -> topo_mesh
# e -> metadata_str
