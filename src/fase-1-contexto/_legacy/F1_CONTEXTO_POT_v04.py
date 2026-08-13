"""
Script: F1_CONTEXTO_POT_v04.py
Proyecto: DiseñoParametrico
Fase: 1 - Contexto y Lote (Integración ArchiCAD)
Versión: 04
Descripción:
    Ancla la esquina Sur-Occidente del lote al origen (0,0,0).
    Añade tolerancia a la separación de vías.
    Entrega curvas 2D y strings de capas listos para Tapir.
"""

import Rhino
import json
import os
import ghpythonlib.components as ghcomp

# Inputs:
# json_path: string (Ruta al archivo *-contexto.json)

lote_curve = None
neighbors_curves = None
public_space_curve = None
topo_mesh = None
metadata_str = "Esperando JSON válido..."

if json_path and os.path.exists(json_path):
    try:
        with open(json_path, 'r') as f:
            data = json.load(f)

        metadata = data.get("metadata", {})
        origen = metadata.get("origen_sirgas", {})
        metadata_str = "CHIP: {}\nOrigen SIRGAS: X={:.2f}, Y={:.2f}, Z={:.2f}\nAzimuth: {:.2f}\nNota: Origen (0,0,0) anclado en esquina SW del lote.".format(
            metadata.get("chip", "N/A"),
            origen.get('x', 0), origen.get('y', 0), origen.get('z', 0),
            metadata.get("azimuth_norte_grados", 0)
        )
        print(metadata_str)

        lote_verts = data.get("lote_objetivo", {}).get("vertices_3d_local", [])
        vecinos_data = data.get("vecinos", [])

        # Calculate offset using the LOT VERTEX closest to the BBox southwest corner.
        # OLD BUG: min(lote_xs) and min(lote_ys) could come from DIFFERENT vertices,
        # producing a ghost point that doesn't exist on the lot.
        if lote_verts:
            bbox_min_x = min(v[0] for v in lote_verts)
            bbox_min_y = min(v[1] for v in lote_verts)
            # Find the ACTUAL lot vertex closest to (bbox_min_x, bbox_min_y)
            min_dist = float('inf')
            offset_x = bbox_min_x
            offset_y = bbox_min_y
            for v in lote_verts:
                d = (v[0] - bbox_min_x)**2 + (v[1] - bbox_min_y)**2
                if d < min_dist:
                    min_dist = d
                    offset_x = v[0]
                    offset_y = v[1]
            print("BBox SW: ({:.2f}, {:.2f}) | Vértice ancla: ({:.2f}, {:.2f}) | Dist: {:.3f}m".format(
                bbox_min_x, bbox_min_y, offset_x, offset_y, min_dist**0.5))
        else:
            # Fallback: no lote vertices (shouldn't happen)
            offset_x = 0
            offset_y = 0

        def create_closed_2d_curve(verts):
            pts = [Rhino.Geometry.Point3d(v[0] - offset_x, v[1] - offset_y, 0.0) for v in verts]
            if len(pts) > 0 and pts[0] != pts[-1]:
                pts.append(pts[0])
            return Rhino.Geometry.PolylineCurve(pts)

        lote_curve = create_closed_2d_curve(lote_verts) if lote_verts else None

        neighbors_curves = []
        for vecino in vecinos_data:
            verts = vecino.get("vertices_3d_local", [])
            if verts:
                neighbors_curves.append(create_closed_2d_curve(verts))

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
                    Rhino.Geometry.Point3d(min_x, min_y, 0), Rhino.Geometry.Point3d(max_x, min_y, 0),
                    Rhino.Geometry.Point3d(max_x, max_y, 0), Rhino.Geometry.Point3d(min_x, max_y, 0),
                    Rhino.Geometry.Point3d(min_x, min_y, 0)
                ]
                context_boundary = Rhino.Geometry.PolylineCurve(bbox_pts)

                private_curves = []
                if lote_curve: private_curves.append(lote_curve)
                private_curves.extend(neighbors_curves)

                try:
                    # Añadimos tolerancia 0.01 para evitar micro-huecos
                    diff_result = Rhino.Geometry.Curve.CreateBooleanDifference(context_boundary, private_curves, 0.01)
                    if diff_result and len(diff_result) > 0:
                        public_space_curve = list(diff_result)
                    else:
                        public_space_curve = [context_boundary]
                except Exception as e:
                    print("Error calculando vías: " + str(e))
                    public_space_curve = [context_boundary]

        # Topografía optimizada (pocos puntos)
        topo_pts_data = data.get("topografia", {}).get("malla_terreno", [])
        if topo_pts_data:
            topo_points = [Rhino.Geometry.Point3d(p["x_local"] - offset_x, p["y_local"] - offset_y, p["z_local"]) for p in topo_pts_data]
            topo_mesh = ghcomp.DelaunayMesh(topo_points)
        else:
            topo_mesh = None

        # Salida de clasificación de lados (del backend)
        lados_data = data.get("lados", [])
        lados_json = json.dumps(lados_data)

    except Exception as e:
        metadata_str = "ERROR GRAVE: " + str(e)
        print("ERROR: " + str(e))