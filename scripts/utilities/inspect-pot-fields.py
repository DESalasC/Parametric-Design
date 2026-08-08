"""
Script: inspect-pot-fields.py
Descripción: Inspecta los campos reales de las capas del POT para el lote objetivo.
"""
import geopandas as gpd
import pyogrio
from shapely.geometry import box
from shapely.ops import transform

# Rutas exactas confirmadas
GPKG_PATH = r"D:\Users\Dario Salas\proyectos\DesParametrico\2-Entradas\Datos_Sitio_GDB\bd_uaecd.gpkg"
POT_GDB_PATH = r"D:\Users\Dario Salas\proyectos\DesParametrico\2-Entradas\Datos_Sitio_GDB\POT\POT_Decreto_555_2021_Bogota_D_C.gdb"
CHIP = "AAA0127AZPA"

def truncate_coords_2d(geom):
    if geom.is_empty: return geom
    if geom.has_z: return transform(lambda x, y, z=None: (x, y), geom)
    return geom

# 1. Buscar el lote dinámicamente
print(f"Buscando lote para CHIP: {CHIP} en bd_uaecd.gpkg...")

layer_info = pyogrio.read_info(GPKG_PATH, layer='Lote')
available_fields = layer_info['fields']
chip_field = 'LotCodigo' if 'LotCodigo' in available_fields else 'Barmanpre'

target_lot_codigo = CHIP
if any(c.isalpha() for c in CHIP):
    predio_info = pyogrio.read_info(GPKG_PATH, layer='Predio')
    predio_fields = predio_info['fields']
    chip_predio_field = next((f for f in ['PreChip', 'CHIP'] if f in predio_fields), None)
    if chip_predio_field:
        predio_gdf = gpd.read_file(GPKG_PATH, layer='Predio', where=f"{chip_predio_field} = '{CHIP}'", engine="pyogrio")
        if not predio_gdf.empty:
            fk_field = next((f for f in ['LotCodigo', 'Barmanpre'] if f in predio_gdf.columns), None)
            if fk_field: 
                target_lot_codigo = str(predio_gdf.iloc[0][fk_field])

print(f"LotCodigo numérico encontrado: {target_lot_codigo}")

lote_gdf = gpd.read_file(GPKG_PATH, layer='Lote', where=f"{chip_field} = '{target_lot_codigo}'", engine="pyogrio")

if lote_gdf.empty:
    print("ERROR: No se encontró el lote.")
    exit()

lote_geom = truncate_coords_2d(lote_gdf.geometry.iloc[0])
bbox = box(*lote_geom.bounds).buffer(100)

# 2. Inspeccionar capas del POT
capas_a_inspectar = [
    'Area_elevacion_maxima',
    'Rango_edificabilidad_desarro',
    'TratamientoUrbanistico',
    'Unidad_planeamento_local'
]

print("\n--- CAMPOS Y VALORES DEL POT PARA EL LOTE ---\n")

for capa in capas_a_inspectar:
    print(f"CAPA: {capa}")
    try:
        gdf = gpd.read_file(POT_GDB_PATH, layer=capa, mask=bbox, engine="pyogrio")
        if not gdf.empty:
            row = gdf.iloc[0].drop('geometry').to_dict()
            for k, v in row.items():
                print(f"  {k}: {v}")
        else:
            print("  (No intersecta con el lote)")
    except Exception as e:
        print(f"  Error: {e}")
    print("-" * 40)
    