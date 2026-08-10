"""
Script: fetch-urban-context-v5.py
Proyecto: DiseñoParametrico
Fase: 1 - Contexto y Lote
Versión: 05
Descripción: 
    Extrae datos reales del POT usando los campos exactos descubiertos:
    UPZ (NOMBRE_UPI), Tratamiento (NOMBRE_TRATAMIENTO), Altura (ALTURA_MAXIMA).
"""

import argparse
import os
import json
import math
import warnings
import requests
import geopandas as gpd
import numpy as np
import pyogrio
from shapely.geometry import box, Polygon, Point, mapping
from shapely.ops import transform
from pyproj import Transformer

warnings.filterwarnings('ignore', category=UserWarning)

GPKG_PATH = r"D:\Users\Dario Salas\proyectos\DesParametrico\2-Entradas\Datos_Sitio_GDB\bd_uaecd.gpkg"
POT_GDB_PATH = r"D:\Users\Dario Salas\proyectos\DesParametrico\2-Entradas\Datos_Sitio_GDB\POT\POT_Decreto_555_2021_Bogota_D_C.gdb"

CRS_TARGET = "ESRI:102233"
CRS_METRIC = "EPSG:3116"
BUFFER_M = 75
ALTURA_PISO_M = 3.80
REST_IDENTIFY_URL = "https://serviciosgis.catastrobogota.gov.co/arcgis/rest/services/topografia/modelodigitalterrenobogotaurbano/MapServer/identify"

def truncate_coords_2d(geom):
    if geom.is_empty: return geom
    if geom.has_z: return transform(lambda x, y, z=None: (x, y), geom)
    return geom

def make_geom_valid(geom):
    if not geom.is_valid: geom = geom.buffer(0)
    return truncate_coords_2d(geom)

def calculate_azimuth(poly):
    if not isinstance(poly, Polygon) or poly.is_empty: return 0.0
    coords = list(poly.exterior.coords)
    if len(coords) < 2: return 0.0
    x1, y1 = coords[0]; x2, y2 = coords[1]
    dx = x2 - x1; dy = y2 - y1
    if dx == 0 and dy == 0: return 0.0
    angulo_rad = math.atan2(dx, dy)
    angulo_deg = math.degrees(angulo_rad)
    return angulo_deg if angulo_deg >= 0 else angulo_deg + 360

def get_elevation_from_api(x_3116, y_3116):
    geometry = {"x": x_3116, "y": y_3116, "spatialReference": {"wkid": 3116}}
    params = {
        "geometry": json.dumps(geometry), "geometryType": "esriGeometryPoint",
        "sr": 3116, "tolerance": 0, "mapExtent": f"{x_3116-1},{y_3116-1},{x_3116+1},{y_3116+1}",
        "imageDisplay": "1,1,96", "returnGeometry": "false", "f": "json"
    }
    try:
        resp = requests.get(REST_IDENTIFY_URL, params=params, timeout=10)
        data = resp.json()
        if "results" in data and len(data["results"]) > 0:
            val = data["results"][0].get("value", "0")
            if isinstance(val, str):
                if ":" in val: val = val.split(":")[-1]
                return float(val.strip())
            return float(val)
    except: pass
    return 0.0

def extract_elevations_online(points_xy, points_crs=CRS_TARGET):
    transformer = Transformer.from_crs(points_crs, CRS_METRIC, always_xy=True)
    zs = []
    print(f"Consultando {len(points_xy)} puntos topográficos a la API...")
    for x, y in points_xy:
        x3116, y3116 = transformer.transform(x, y)
        z = get_elevation_from_api(x3116, y3116)
        zs.append(z)
    return zs

def generate_lote_topo_points(poly):
    points = list(poly.exterior.coords)[:-1]
    for i in range(len(points)):
        p1 = points[i]; p2 = points[(i+1)%len(points)]
        points.append(((p1[0]+p2[0])/2, (p1[1]+p2[1])/2))
    centroid = poly.centroid
    points.append((centroid.x, centroid.y))
    return points

def main(chip, output_dir="data/pot-cache"):
    print(f"--- Iniciando fetch de contexto para CHIP: {chip} ---")
    
    if not os.path.exists(GPKG_PATH): raise FileNotFoundError(f"No se encontró la geobase en: {GPKG_PATH}")

    target_lot_codigo = chip
    if any(c.isalpha() for c in chip):
        try:
            predio_info = pyogrio.read_info(GPKG_PATH, layer='Predio')
            predio_fields = predio_info['fields']
            chip_predio_field = next((f for f in ['PreChip', 'CHIP'] if f in predio_fields), None)
            if chip_predio_field:
                predio_gdf = gpd.read_file(GPKG_PATH, layer='Predio', where=f"{chip_predio_field} = '{chip}'", engine="pyogrio")
                if not predio_gdf.empty:
                    fk_field = next((f for f in ['LotCodigo', 'Barmanpre'] if f in predio_gdf.columns), None)
                    if fk_field: target_lot_codigo = str(predio_gdf.iloc[0][fk_field])
        except Exception as e:
            print(f"Advertencia: No se pudo hacer JOIN con Predio ({e}).")

    layer_info = pyogrio.read_info(GPKG_PATH, layer='Lote')
    available_fields = layer_info['fields']
    chip_field = 'LotCodigo' if 'LotCodigo' in available_fields else 'Barmanpre'
    lote_gdf = gpd.read_file(GPKG_PATH, layer='Lote', where=f"{chip_field} = '{target_lot_codigo}'", engine="pyogrio")
    
    if lote_gdf.empty: raise ValueError(f"No se encontró el lote con {chip_field}: {target_lot_codigo}")

    lote_geom = make_geom_valid(lote_gdf.geometry.iloc[0])
    print(f"Lote encontrado. Área: {lote_geom.area:.2f} m2")

    bbox = box(*lote_geom.bounds)
    buffer_poly = bbox.buffer(BUFFER_M)

    vecinos_gdf = gpd.read_file(GPKG_PATH, layer='Lote', mask=buffer_poly, engine="pyogrio")
    if chip_field in vecinos_gdf.columns:
        vecinos_gdf = vecinos_gdf[vecinos_gdf[chip_field] != target_lot_codigo]

    # --- LÓGICA DE POT EXACTA ---
    pot_data = {"upz": "N/A", "altura_maxima_m": None, "rango_edificabilidad": None, "tratamiento": "N/A"}
    if os.path.exists(POT_GDB_PATH):
        print("Consultando Geodatabase del POT (.gdb)...")
        try:
            # 1. Alturas y UPZ
            alt_gdf = gpd.read_file(POT_GDB_PATH, layer='Area_elevacion_maxima', mask=lote_geom, engine="pyogrio")
            if not alt_gdf.empty:
                pot_data["upz"] = str(alt_gdf.iloc[0].get('NOMBRE_UPI', 'N/A'))
            
            # 2. Tratamiento y Altura en pisos
            trat_gdf = gpd.read_file(POT_GDB_PATH, layer='TratamientoUrbanistico', mask=lote_geom, engine="pyogrio")
            if not trat_gdf.empty:
                pot_data["tratamiento"] = str(trat_gdf.iloc[0].get('NOMBRE_TRATAMIENTO', 'N/A'))
                alt_pisos = trat_gdf.iloc[0].get('ALTURA_MAXIMA')
                if alt_pisos is not None:
                    pot_data["altura_maxima_m"] = float(alt_pisos) * ALTURA_PISO_M
                    
            # 3. Edificabilidad
            edif_gdf = gpd.read_file(POT_GDB_PATH, layer='Rango_edificabilidad_desarro', mask=lote_geom, engine="pyogrio")
            if not edif_gdf.empty:
                pot_data["rango_edificabilidad"] = str(edif_gdf.iloc[0].get('RANGO', 'N/A'))
                
            print(f"Datos POT extraídos: {pot_data}")
        except Exception as e:
            print(f"Advertencia: No se pudo leer el POT .gdb ({e}).")
    else:
        print(f"Advertencia: No se encontró el POT .gdb en {POT_GDB_PATH}")

    # Topografía optimizada
    topo_lote_xy = generate_lote_topo_points(lote_geom)
    zs_lote = extract_elevations_online(topo_lote_xy)
    lote_verts_xy = list(lote_geom.exterior.coords)
    lote_verts_3d = [(x, y, z) for (x, y), z in zip(lote_verts_xy, zs_lote[:len(lote_verts_xy)])]
    mesh_points = [{"id": f"P{i}", "x": x, "y": y, "z": z} for i, ((x, y), z) in enumerate(zip(topo_lote_xy, zs_lote))]
    
    all_zs = [z for _, _, z in lote_verts_3d] + [p["z"] for p in mesh_points if p["z"] is not None]
    min_z = min(all_zs) if all_zs else 0.0

    vecinos_data = []
    for idx, row in vecinos_gdf.iterrows():
        v_geom = make_geom_valid(row.geometry)
        v_xy = list(v_geom.exterior.coords)
        vecinos_data.append({"chip": str(row.get(chip_field, 'N/A')), "vertices_3d": [(x, y, 0.0) for x, y in v_xy]})

    minx, miny, maxx, maxy = buffer_poly.bounds
    lote_local = [(x - minx, y - miny, z - min_z) for x, y, z in lote_verts_3d]
    vecinos_local = [{"chip": v["chip"], "vertices_3d_local": [(x - minx, y - miny, 0.0 - min_z) for x, y, z in v["vertices_3d"]]} for v in vecinos_data]
    mesh_local = [{"id": p["id"], "x_local": p["x"] - minx, "y_local": p["y"] - miny, "z_local": (p["z"] or 0.0) - min_z} for p in mesh_points]
    azimuth = calculate_azimuth(lote_geom)

    # ── CLASIFICACIÓN DE LADOS: Frontal vs Lateral por adyacencia real ──
    # Un borde del lote es "Frontal" si NO colinda con ningún vecino (da a vía),
    # "Lateral" si SÍ hay un vecino adyacente en ese lado.
    print("Clasificando lados del lote por adyacencia con vecinos...")
    from shapely.geometry import LineString, Polygon as ShapelyPolygon
    
    lote_coords = list(lote_geom.exterior.coords)
    lados_clasificados = []
    PROXIMIDAD_M = 2.0  # distancia máxima para considerar "colindante"
    
    for i in range(len(lote_coords) - 1):
        p1 = lote_coords[i]
        p2 = lote_coords[i + 1]
        edge = LineString([p1, p2])
        edge_length = edge.length
        mid = edge.interpolate(0.5, normalized=True)
        
        # Crear zona de búsqueda: buffer estrecho hacia afuera del segmento
        search_zone = edge.buffer(PROXIMIDAD_M, single_sided=True)
        # El buffer single_sided apunta en una dirección; si no intersecta,
        # probar la otra dirección (misma geometría pero invertida)
        
        tiene_vecino = False
        vecino_colindante = None
        
        for idx2, row2 in vecinos_gdf.iterrows():
            vg = make_geom_valid(row2.geometry)
            # Verificar si el vecino está próximo al borde
            if vg.distance(edge) < PROXIMIDAD_M:
                # Verificar intersección real o cercanía
                if search_zone.intersects(vg):
                    tiene_vecino = True
                    vecino_colindante = str(row2.get(chip_field, 'N/A'))
                    break
                # Probar zona invertida (single_sided puede apuntar al lado equivocado)
                search_zone_inv = edge.buffer(PROXIMIDAD_M, single_sided=True)
                # invertir dirección: usar negative buffer + original
                # Simplificación: si distance < PROXIMIDAD_M, considerar colindante
                tiene_vecino = True
                vecino_colindante = str(row2.get(chip_field, 'N/A'))
                break
        
        clasificacion = "Lateral" if tiene_vecino else "Frontal"
        lados_clasificados.append({
            "lado_idx": i,
            "clasificacion": clasificacion,
            "longitud_m": round(edge_length, 2),
            "vecino_colindante": vecino_colindante
        })
        print(f"  Lado {i}: {clasificacion} ({edge_length:.1f}m)"
              + (f" — vecino: {vecino_colindante}" if vecino_colindante else ""))
    
    n_frontal = sum(1 for l in lados_clasificados if l["clasificacion"] == "Frontal")
    n_lateral = sum(1 for l in lados_clasificados if l["clasificacion"] == "Lateral")
    print(f"  Resultado: {n_frontal} frentes, {n_lateral} laterales")
    
    print(f"  Vías de referencia generadas: {len(vias_data)} segmentos desde {len(lote_coords)-1} bordes")
    
    # Versión local para Grasshopper
    vias_local = []
    for via in vias_data:
        verts_local = [(x - minx, y - miny, 0.0 - min_z) for x, y, z in via["vertices_3d"]]
        vias_local.append({
            "lado_lote_idx": via["lado_lote_idx"],
            "tipo": via["tipo"],
            "vertices_3d_local": verts_local
        })

    output_data = {
        "metadata": {"chip": chip, "origen_sirgas": {"crs": CRS_TARGET, "x": minx, "y": miny, "z": min_z}, "azimuth_norte_grados": azimuth, "buffer_metros": BUFFER_M},
        "pot_data": pot_data, 
        "topografia": {"estado": "ESTIMADA", "fuente": "Catastro_REST_API", "malla_terreno": mesh_local},
        "lote_objetivo": {"vertices_3d_local": lote_local, "area_m2": round(lote_geom.area, 2)},
        "vecinos": vecinos_local,
        "lados": lados_clasificados
    }

    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f"{chip}-contexto.json")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)
    print(f"\n✅ ÉXITO: Contexto guardado en {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--chip", required=True)
    parser.add_argument("--output-dir", default="data/pot-cache")
    args = parser.parse_args()
    project_root = os.environ.get("DISENO_PARAMETRICO_ROOT", os.getcwd())
    out_dir = os.path.join(project_root, args.output_dir) if not os.path.isabs(args.output_dir) else args.output_dir
    main(args.chip, out_dir)
    