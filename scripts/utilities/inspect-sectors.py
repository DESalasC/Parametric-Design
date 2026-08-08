"""
Script: inspect-sectors.py
Descripción: Busca a qué sector normativo pertenece el lote.
"""
import geopandas as gpd
import pyogrio
from shapely.geometry import box
from shapely.ops import transform

GPKG_PATH = r"D:\Users\Dario Salas\proyectos\DesParametrico\2-Entradas\Datos_Sitio_GDB\bd_uaecd.gpkg"
POT_GDB_PATH = r"D:\Users\Dario Salas\proyectos\DesParametrico\2-Entradas\Datos_Sitio_GDB\POT\POT_Decreto_555_2021_Bogota_D_C.gdb"
LOT_CODIGO = "009130083016"

def truncate_coords_2d(geom):
    if geom.is_empty: return geom
    if geom.has_z: return transform(lambda x, y, z=None: (x, y), geom)
    return geom

lote_gdf = gpd.read_file(GPKG_PATH, layer='Lote', where=f"LotCodigo = '{LOT_CODIGO}'", engine="pyogrio")
lote_geom = truncate_coords_2d(lote_gdf.geometry.iloc[0])
bbox = box(*lote_geom.bounds).buffer(10)

capas = ['Sector_uso_residencial', 'Sector_interes_urbanistico']

for capa in capas:
    print(f"\n--- CAPA: {capa} ---")
    try:
        gdf = gpd.read_file(POT_GDB_PATH, layer=capa, mask=bbox, engine="pyogrio")
        if not gdf.empty:
            row = gdf.iloc[0].drop('geometry').to_dict()
            for k, v in row.items():
                print(f"  {k}: {v}")
        else:
            print("  (No intersecta)")
    except Exception as e:
        print(f"  Error: {e}")