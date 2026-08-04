"""
Fetch Urban Context Script (con descarga dinámica de MDE)
Proyecto: DiseñoParametrico
Directriz: ADR-007

Extrae geometría del lote, vecinos (75m) y topografía.
Si no hay MDE local, descarga un recorte dinámico del servicio REST de Catastro Bogotá.
Transforma todo a un origen local (0,0,0) preservando metadatos SIRGAS.
"""

import argparse
import os
import json
import math
import warnings
import requests
import geopandas as gpd
import numpy as np
from shapely.geometry import box, Polygon, LineString, Point, mapping
from shapely.ops import transform
from pyproj import Transformer
import rasterio
from rasterio.features import geometry_mask
from rasterio.io import MemoryFile
from rasterio.warp import calculate_default_transform, reproject, Resampling

# Suprimir warnings
warnings.filterwarnings('ignore', category=UserWarning)

# Configuración global
GPKG_PATH = os.environ.get("POT_GPKG_PATH", "D:/Users/Dario Salas/Documents/bd_uaecd.gpkg")
CRS_TARGET = "ESRI:102233"  # CRS de la geobase local
CRS_METRIC = "EPSG:3116"    # CRS métrico requerido por la API de Catastro
BUFFER_M = 75
REST_DEM_URL = "https://serviciosgis.catastrobogota.gov.co/arcgis/rest/services/topografia/modelodigitalterrenobogotaurbano/MapServer/0/export"

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

def fetch_online_dem_tiff(bbox_poly_102233, out_path):
    """Descarga un recorte del MDE desde la API de Catastro y lo guarda como GeoTIFF."""
    print("Descargando MDE dinámico desde Catastro Bogotá REST API...")
    
    # 1. Reproyectar BBox a EPSG:3116 (Requerido por la API)
    transformer_to_3116 = Transformer.from_crs(CRS_TARGET, CRS_METRIC, always_xy=True)
    minx, miny, maxx, maxy = bbox_poly_102233.bounds
    x1, y1 = transformer_to_3116.transform(minx, miny)
    x2, y2 = transformer_to_3116.transform(maxx, maxy)
    
    bbox_3116 = f"{x1},{y1},{x2},{y2}"
    pixels_x = int((x2 - x1) * 1) # 1 pixel por metro
    pixels_y = int((y2 - y1) * 1)
    
    params = {
        "bbox": bbox_3116,
        "bboxSR": 3116,
        "imageSR": 3116,
        "size": f"{pixels_x},{pixels_y}",
        "format": "tiff",
        "transparent": "false",
        "f": "json"
    }
    
    resp = requests.get(REST_DEM_URL, params=params, timeout=120)
    resp.raise_for_status()
    data = resp.json()
    
    if "href" not in data:
        raise RuntimeError(f"API no devolvió URL de descarga. Respuesta: {json.dumps(data)[:500]}")
    
    img_url = data["href"]
    r = requests.get(img_url, timeout=120)
    r.raise_for_status()
    
    tmp_tif = out_path.replace(".tif", "_raw.tif")
    with open(tmp_tif, "wb") as f:
        f.write(r.content)
        
    # 2. Enmascarar y limpiar el TIFF
    with rasterio.open(tmp_tif) as src:
        profile = src.profile.copy()
        profile.update(driver="GTiff", compress="deflate", tiled=True, count=1)
        
        data_arr = src.read(1)
        
        # Crear máscara del buffer en el raster 3116
        buffer_3116 = box(x1, y1, x2, y2)
        mask = geometry_mask(
            [mapping(buffer_3116)],
            out_shape=data_arr.shape,
            transform=src.transform,
            invert=True
        )
        
        out_data = data_arr.copy()
        out_data[~mask] = src.nodata if src.nodata is not None else 0
        
        with rasterio.open(out_path, "w", **profile) as dst:
            dst.write(out_data, 1)
            
    os.remove(tmp_tif)
    print(f"MDE descargado y guardado en: {out_path}")
    return out_path

def extract_elevation(raster_path, points_xy, points_crs=CRS_TARGET):
    """Extrae cotas Z de puntos [X, Y] desde un GeoTIFF."""
    try:
        transformer_to_raster = Transformer.from_crs(points_crs, CRS_METRIC, always_xy=True)
        points_3116 = [transformer_to_raster.transform(x, y) for x, y in points_xy]
        
        with rasterio.open(raster_path) as src:
            zs = [val[0] for val in src.sample(points_3116)]
            return zs
    except Exception as e:
        print(f"Error leyendo raster: {e}")
        return [0.0] * len(points_xy)

def generate_mesh_points(bbox_poly, spacing=5.0):
    minx, miny, maxx, maxy = bbox_poly.bounds
    xs = np.arange(minx, maxx, spacing)
    ys = np.arange(miny, maxy, spacing)
    points = []
    for x in xs:
        for y in ys:
            pt = Point(x, y)
            if bbox_poly.contains(pt) or bbox_poly.touches(pt):
                points.append((x, y))
    return points

def main(chip, output_dir="data/pot-cache"):
    print(f"--- Iniciando fetch de contexto para CHIP: {chip} ---")
    
    if not os.path.exists(GPKG_PATH):
        raise FileNotFoundError(f"No se encontró la geobase en: {GPKG_PATH}")

    # 1. Leer capa Lote y filtrar
    print("Leyendo capa Lote del .gpkg...")
    lote_gdf = gpd.read_file(GPKG_PATH, layer='Lote', where=f"PreChip = '{chip}'", engine="pyogrio")
    if lote_gdf.empty:
        lote_gdf = gpd.read_file(GPKG_PATH, layer='Lote', where=f"Barmanpre = '{chip}'", engine="pyogrio")
    if lote_gdf.empty:
        raise ValueError(f"No se encontró el lote con CHIP/Barmanpre: {chip}")

    lote_geom = make_geom_valid(lote_gdf.geometry.iloc[0])
    print(f"Lote encontrado. Área: {lote_geom.area:.2f} m2")

    # 2. Buffer y BBox
    bbox = box(*lote_geom.bounds)
    buffer_poly = bbox.buffer(BUFFER_M)
    print(f"Buffer de contexto generado: {BUFFER_M}m")

    # 3. Vecinos
    print("Buscando lotes vecinos...")
    vecinos_gdf = gpd.read_file(GPKG_PATH, layer='Lote', mask=buffer_poly, engine="pyogrio")
    vecinos_gdf = vecinos_gdf[vecinos_gdf['PreChip'] != chip]
    print(f"Vecinos encontrados: {len(vecinos_gdf)}")

    # 4. Topografía (Descarga Dinámica)
    os.makedirs(output_dir, exist_ok=True)
    dem_path = os.path.join(output_dir, f"{chip}-dem.tif")
    
    topo_estado = "ESTIMADA"
    topo_fuente = "Catastro_REST_API"
    
    try:
        fetch_online_dem_tiff(buffer_poly, dem_path)
    except Exception as e:
        print(f"Fallo la descarga del MDE: {e}. Usando Z=0.")
        topo_estado = "PENDIENTE"
        topo_fuente = None
        dem_path = None

    lote_verts_xy = list(lote_geom.exterior.coords)
    vecinos_data = []
    
    if dem_path and os.path.exists(dem_path):
        zs_lote = extract_elevation(dem_path, lote_verts_xy)
        lote_verts_3d = [(x, y, z) for (x, y), z in zip(lote_verts_xy, zs_lote)]
        
        for idx, row in vecinos_gdf.iterrows():
            v_geom = make_geom_valid(row.geometry)
            v_xy = list(v_geom.exterior.coords)
            v_zs = extract_elevation(dem_path, v_xy)
            vecinos_data.append({
                "chip": str(row.get('PreChip', 'N/A')),
                "vertices_3d": [(x, y, z) for (x, y), z in zip(v_xy, v_zs)],
                "altura_estimada_m": 0.0,
                "num_pisos": 0
            })
            
        print("Generando malla de puntos topográficos (5m x 5m)...")
        mesh_xy = generate_mesh_points(buffer_poly, spacing=5.0)
        mesh_zs = extract_elevation(dem_path, mesh_xy)
        mesh_points = [{"id": f"M{i}", "x": x, "y": y, "z": z} for i, ((x, y), z) in enumerate(zip(mesh_xy, mesh_zs))]
        
        all_zs = [z for _, _, z in lote_verts_3d] + [p["z"] for p in mesh_points if p["z"] is not None]
        min_z = min(all_zs) if all_zs else 0.0
    else:
        lote_verts_3d = [(x, y, 0.0) for x, y in lote_verts_xy]
        mesh_points = []
        for idx, row in vecinos_gdf.iterrows():
            v_geom = make_geom_valid(row.geometry)
            v_xy = list(v_geom.exterior.coords)
            vecinos_data.append({
                "chip": str(row.get('PreChip', 'N/A')),
                "vertices_3d": [(x, y, 0.0) for x, y in v_xy],
                "altura_estimada_m": 0.0,
                "num_pisos": 0
            })
        min_z = 0.0

    # 5. Transformación a Coordenadas Locales
    minx, miny, maxx, maxy = buffer_poly.bounds
    print(f"Origen Local: MinX: {minx}, MinY: {miny}, MinZ: {min_z}")
    
    lote_local = [(x - minx, y - miny, z - min_z) for x, y, z in lote_verts_3d]
    vecinos_local = []
    for v in vecinos_data:
        v_local = [(x - minx, y - miny, z - min_z) for x, y, z in v["vertices_3d"]]
        vecinos_local.append({
            "chip": v["chip"], "vertices_3d_local": v_local,
            "altura_estimada_m": v["altura_estimada_m"], "num_pisos": v["num_pisos"]
        })
    mesh_local = [{"id": p["id"], "x_local": p["x"] - minx, "y_local": p["y"] - miny, "z_local": (p["z"] or 0.0) - min_z} for p in mesh_points]

    azimuth = calculate_azimuth(lote_geom)

    # 6. JSON Output
    output_data = {
        "metadata": {
            "chip": chip,
            "origen_sirgas": {"crs": CRS_TARGET, "x": minx, "y": miny, "z": min_z},
            "azimuth_norte_grados": azimuth,
            "buffer_metros": BUFFER_M
        },
        "topografia": {"estado": topo_estado, "fuente": topo_fuente, "malla_terreno": mesh_local},
        "lote_objetivo": {"vertices_3d_local": lote_local, "area_m2": round(lote_geom.area, 2)},
        "vecinos": vecinos_local,
        "vias": []
    }

    output_file = os.path.join(output_dir, f"{chip}-contexto.json")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)

    print(f"\n✅ ÉXITO: Contexto guardado en {output_file}")
    print(f"   - Topografía: {topo_estado}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch Urban Context")
    parser.add_argument("--chip", required=True, help="CHIP del predio")
    parser.add_argument("--output-dir", default="data/pot-cache", help="Directorio de salida")
    
    args = parser.parse_args()
    project_root = os.environ.get("DISENO_PARAMETRICO_ROOT", os.getcwd())
    out_dir = os.path.join(project_root, args.output_dir) if not os.path.isabs(args.output_dir) else args.output_dir
    
    main(args.chip, out_dir)
    