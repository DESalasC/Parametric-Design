#!/usr/bin/env python3
"""
Convert File Geodatabase (GDB) to GeoPackage (GPKG) using geopandas.
Requires: geopandas, fiona (with GDB support), pyogrio
"""

import geopandas as gpd
import os
import zipfile
import tempfile
import shutil

GDB_ZIP = r"C:\Users\Dario Salas\Downloads\pot_decreto_555_2021_bogota_d_c.gdb.zip"
OUTPUT_DIR = r"C:\Users\Dario Salas\proyectos\2-Entradas\Datos_Sitio_GDB"
GPKG_OUTPUT = os.path.join(OUTPUT_DIR, "pot_bogota.gpkg")
GEOJSON_DIR = os.path.join(OUTPUT_DIR, "geojson_layers")

def main():
    print(f"=== Conversión GDB -> GPKG/GeoJSON ===")
    print(f"Entrada: {GDB_ZIP}")
    print(f"Salida GPKG: {GPKG_OUTPUT}")
    print(f"Salida GeoJSON: {GEOJSON_DIR}")

    # Crear directorios
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(GEOJSON_DIR, exist_ok=True)

    # Descomprimir GDB a temp
    with tempfile.TemporaryDirectory() as tmpdir:
        # El GDB dentro del zip tiene nombre específico
        gdb_folder_name = "POT_Decreto_555_2021_Bogota_D_C.gdb"
        gdb_path = os.path.join(tmpdir, gdb_folder_name)

        print("\n[1/3] Descomprimiendo GDB...")
        with zipfile.ZipFile(GDB_ZIP, 'r') as zf:
            zf.extractall(tmpdir)

        # Listar capas
        print("\n[2/3] Leyendo capas del GDB...")
        try:
            layers = gpd.list_layers(gdb_path)
            print(f"Capas encontradas ({len(layers)}):")
            for idx, layer in layers.iterrows():
                print(f"  - {layer['name']}: {layer['geometry_type']}")
        except Exception as e:
            print(f"Error listando capas: {e}")
            return

        # Convertir cada capa
        print("\n[3/3] Convirtiendo capas...")
        success_count = 0
        for idx, layer in layers.iterrows():
            layer_name = layer['name']
            safe_name = layer_name.replace(' ', '_').replace('/', '_').replace('\\', '_')

            try:
                print(f"  -> {layer_name}...", end=" ")
                gdf = gpd.read_file(gdb_path, layer=layer_name)

                # Guardar en GPKG (todas las capas en un archivo)
                gdf.to_file(GPKG_OUTPUT, layer=safe_name, driver="GPKG")

                # Guardar también como GeoJSON individual
                geojson_path = os.path.join(GEOJSON_DIR, f"{safe_name}.geojson")
                gdf.to_file(geojson_path, driver="GeoJSON")

                print(f"OK ({len(gdf)} features, CRS: {gdf.crs})")
                success_count += 1

            except Exception as e:
                print(f"ERROR: {e}")

        print(f"\n=== Completado: {success_count}/{len(layers)} capas convertidas ===")
        print(f"GPKG: {GPKG_OUTPUT}")
        print(f"GeoJSON: {GEOJSON_DIR}/")

        # Generar reporte de campos por capa
        print("\n=== Reporte de campos por capa ===")
        report_path = os.path.join(OUTPUT_DIR, "gdb_layer_fields_report.csv")
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write("layer_name,field_name,field_type\n")
            for idx, layer in layers.iterrows():
                layer_name = layer['name']
                safe_name = layer_name.replace(' ', '_').replace('/', '_').replace('\\', '_')
                try:
                    gdf = gpd.read_file(gdb_path, layer=layer_name)
                    for col in gdf.columns:
                        if col != gdf.geometry.name:
                            dtype = str(gdf[col].dtype)
                            f.write(f"{layer_name},{col},{dtype}\n")
                except Exception as e:
                    f.write(f"{layer_name},ERROR_READING,{e}\n")
        print(f"Reporte guardado: {report_path}")

if __name__ == "__main__":
    main()