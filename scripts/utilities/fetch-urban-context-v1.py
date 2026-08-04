"""
Script: fetch-urban-context-v1.py
Proyecto: DiseñoParametrico
Fase: 1 - Contexto y Lote
Versión: 01
Descripción: 
    Extrae la geometría del lote, vecinos (75m) y topografía de la geobase catastral.
    Consulta la topografía punto a punto vía API REST de Catastro (Identify).
    Transforma las coordenadas a un origen local (0,0,0) preservando los metadatos SIRGAS.
Directriz: ADR-007
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

# Suprimir warnings de pyogrio/geopandas sobre geometrías inválidas temporales
warnings.filterwarnings('ignore', category=UserWarning)

# =========================
# CONFIGURACIÓN GLOBAL
# =========================
GPKG_PATH = os.environ.get("POT_GPKG_PATH", "D:/Users/Dario Salas/Documents/bd_uaecd.gpkg")
CRS_TARGET = "ESRI:102233"  # CRS de la geobase local
CRS_METRIC = "EPSG:3116"    # CRS métrico requerido por la API de Catastro
BUFFER_M = 75
REST_IDENTIFY_URL = "https://serviciosgis.catastrobogota.gov.co/arcgis/rest/services/topografia/modelodigitalterrenobogotaurbano/MapServer/identify"

def truncate_coords_2d(geom):
    """Trunca coordenadas 4D (X,Y,Z,M) a 2D (X,Y) para evitar errores en shapely."""
    if geom.is_empty: return geom
    if geom.has_z: return transform(lambda x, y, z=None: (x, y), geom)
    return geom

def make_geom_valid(geom):
    """Repara geometrías inválidas usando buffer(0) y las trunca a 2D."""
    if not geom.is_valid: geom = geom.buffer(0)
    return truncate_coords_2d(geom)

def calculate_azimuth(poly):
    """Calcula el azimuth del primer segmento del polígono respecto al Norte."""
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
    """Consulta la cota Z de un punto individual en la API REST de Catastro."""
    geometry = {"x": x_3116, "y": y_3116, "spatialReference": {"wkid": 3116}}
    params = {
        "geometry": json.dumps(geometry),
        "geometryType": "esriGeometryPoint",
        "sr": 3116,
        "tolerance": 0,
        "mapExtent": f"{x_3116-1},{y_3116-1},{x_3116+1},{y_3116+1}",
        "imageDisplay": "1,1,96",
        "returnGeometry": "false",
        "f": "json"
    }
    try:
        resp = requests.get(REST_IDENTIFY_URL, params=params, timeout=10)
        data = resp.json()
        if "results" in data and len(data["results"]) > 0:
            val = data["results"][0].get("value", "0")
            if isinstance(val, str):
                # Limpiar string si viene en formato "Value: 2538.5"
                if ":" in val: val = val.split(":")[-1]
                return float(val.strip())
            return float(val)
    except:
        pass
    return 0.0

def extract_elevations_online(points_xy, points_crs=CRS_TARGET):
    """Extrae cotas Z de una lista de puntos consultando la API uno por uno."""
    transformer = Transformer.from_crs(points_crs, CRS_METRIC, always_xy=True)
    zs = []
    print(f"Consultando {len(points_xy)} puntos a la API de Catastro (puede tardar unos segundos)...")
    for i, (x, y) in enumerate(points_xy):
        x3116, y3116 = transformer.transform(x, y)
        z = get_elevation_from_api(x3116, y3116)
        zs.append(z)
        if (i+1) % 20 == 0:
            print(f"  ...{i+1}/{len(points_xy)} puntos consultados")
    return zs

def generate_mesh_points(bbox_poly, spacing=10.0):
    """Genera una grilla de puntos cada N metros dentro del Bounding Box."""
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

    # 1. Resolver CHIP alfanumérico a LotCodigo numérico si es necesario
    target_lot_codigo = chip
    if any(c.isalpha() for c in chip):
        print(f"CHIP alfanumérico detectado. Buscando LotCodigo en capa 'Predio'...")
        try:
            predio_info = pyogrio.read_info(GPKG_PATH, layer='Predio')
            predio_fields = predio_info['fields']
            chip_predio_field = next((f for f in ['PreChip', 'CHIP'] if f in predio_fields), None)
            if chip_predio_field:
                predio_gdf = gpd.read_file(GPKG_PATH, layer='Predio', where=f"{chip_predio_field} = '{chip}'", engine="pyogrio")
                if not predio_gdf.empty:
                    fk_field = next((f for f in ['LotCodigo', 'Barmanpre'] if f in predio_gdf.columns), None)
                    if fk_field:
                        target_lot_codigo = str(predio_gdf.iloc[0][fk_field])
                        print(f"LotCodigo numérico encontrado: {target_lot_codigo}")
        except Exception as e:
            print(f"Advertencia: No se pudo hacer JOIN con Predio ({e}).")

    # 2. Leer capa Lote y filtrar
    print("Leyendo capa Lote del .gpkg...")
    layer_info = pyogrio.read_info(GPKG_PATH, layer='Lote')
    available_fields = layer_info['fields']
    chip_field = 'LotCodigo' if 'LotCodigo' in available_fields else 'Barmanpre'
    lote_gdf = gpd.read_file(GPKG_PATH, layer='Lote', where=f"{chip_field} = '{target_lot_codigo}'", engine="pyogrio")
    
    if lote_gdf.empty:
        raise ValueError(f"No se encontró el lote con {chip_field}: {target_lot_codigo}")

    lote_geom = make_geom_valid(lote_gdf.geometry.iloc[0])
    print(f"Lote encontrado. Área: {lote_geom.area:.2f} m2")

    # 3. Buffer y BBox
    bbox = box(*lote_geom.bounds)
    buffer_poly = bbox.buffer(BUFFER_M)
    print(f"Buffer de contexto generado: {BUFFER_M}m")

    # 4. Vecinos
    print("Buscando lotes vecinos...")
    vecinos_gdf = gpd.read_file(GPKG_PATH, layer='Lote', mask=buffer_poly, engine="pyogrio")
    if chip_field in vecinos_gdf.columns:
        vecinos_gdf = vecinos_gdf[vecinos_gdf[chip_field] != target_lot_codigo]
    print(f"Vecinos encontrados: {len(vecinos_gdf)}")

    # 5. Topografía (Consulta API Punto a Punto)
    topo_estado = "ESTIMADA"
    topo_fuente = "Catastro_REST_API"
    
    lote_verts_xy = list(lote_geom.exterior.coords)
    vecinos_data = []
    
    # Consultar Z para Lote
    zs_lote = extract_elevations_online(lote_verts_xy)
    lote_verts_3d = [(x, y, z) for (x, y), z in zip(lote_verts_xy, zs_lote)]
    
    # Consultar Z para Vecinos
    for idx, row in vecinos_gdf.iterrows():
        v_geom = make_geom_valid(row.geometry)
        v_xy = list(v_geom.exterior.coords)
        v_zs = extract_elevations_online(v_xy)
        vecinos_data.append({
            "chip": str(row.get(chip_field, 'N/A')),
            "vertices_3d": [(x, y, z) for (x, y), z in zip(v_xy, v_zs)],
            "altura_estimada_m": 0.0,
            "num_pisos": 0
        })
        
    # Consultar Z para Malla Topográfica
    print("Generando malla de puntos topográficos (10m x 10m)...")
    mesh_xy = generate_mesh_points(buffer_poly, spacing=10.0)
    mesh_zs = extract_elevations_online(mesh_xy)
    mesh_points = [{"id": f"M{i}", "x": x, "y": y, "z": z} for i, ((x, y), z) in enumerate(zip(mesh_xy, mesh_zs))]
    
    all_zs = [z for _, _, z in lote_verts_3d] + [p["z"] for p in mesh_points if p["z"] is not None]
    min_z = min(all_zs) if all_zs else 0.0

    # 6. Transformación a Coordenadas Locales (0,0,0)
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

    # 7. JSON Output
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

    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f"{chip}-contexto.json")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)

    print(f"\n✅ ÉXITO: Contexto guardado en {output_file}")
    print(f"   - Topografía: {topo_estado}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch Urban Context for Parametric Design")
    parser.add_argument("--chip", required=True, help="CHIP o Barmanpre del predio")
    parser.add_argument("--output-dir", default="data/pot-cache", help="Directorio de salida")
    
    args = parser.parse_args()
    project_root = os.environ.get("DISENO_PARAMETRICO_ROOT", os.getcwd())
    out_dir = os.path.join(project_root, args.output_dir) if not os.path.isabs(args.output_dir) else args.output_dir
    
    main(args.chip, out_dir)
    