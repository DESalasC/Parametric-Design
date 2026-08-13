"""
Script: fetch-aerial-photo-v6.py
Proyecto: DiseñoParametrico
Fase: 1 - Contexto y Lote
Versión: 06
Descripción: 
    Descarga imagen satelital de ESRI World Imagery vía REST API.
    Fix: Tamaño de imagen reducido a 1024x1024 para evitar Error 500 del servidor.
"""

import argparse
import os
import json
import requests
from pyproj import Transformer

# Configuración
PROJECT_ROOT = os.environ.get("DISENO_PARAMETRICO_ROOT", os.getcwd())
ESRI_URL = "https://server.arcgisonline.com/arcgis/rest/services/World_Imagery/MapServer/export"

def main(chip, output_dir):
    json_path = os.path.join(output_dir, f"{chip}-contexto.json")
    
    if not os.path.exists(json_path):
        print(f"ERROR: No se encontró el JSON del lote en {json_path}.")
        return

    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 1. Leer Bounding Box del JSON (en ESRI:102233)
    orig = data["metadata"]["origen_sirgas"]
    buffer_m = 200
    
    min_x = orig["x"] - buffer_m
    min_y = orig["y"] - buffer_m
    max_x = orig["x"] + buffer_m
    max_y = orig["y"] + buffer_m

    # 2. Convertir a Web Mercator (EPSG:3857)
    print("Convirtiendo coordenadas a Web Mercator...")
    transformer = Transformer.from_crs("ESRI:102233", "EPSG:3857", always_xy=True)
    x1, y1 = transformer.transform(min_x, min_y)
    x2, y2 = transformer.transform(max_x, max_y)
    
    bbox_str = f"{x1},{y1},{x2},{y2}"

    # 3. Parámetros de la petición a ESRI REST API
    params = {
        "bbox": bbox_str,
        "bboxSR": "3857",
        "imageSR": "3857",
        "size": "1024,1024", # Reducido a 1024 para evitar rechazos del servidor
        "format": "png",
        "transparent": "false",
        "f": "image"
    }

    print("Descargando imagen satelital (ESRI REST API)...")
    
    # 4. Descargar imagen
    try:
        response = requests.get(ESRI_URL, params=params, timeout=60)
        response.raise_for_status()

        content_type = response.headers.get("Content-Type", "")
        if response.status_code == 200 and "image" in content_type:
            out_img = os.path.join(output_dir, f"{chip}-ortofoto.png")
            with open(out_img, "wb") as f:
                f.write(response.content)
            print(f"\n✅ ÉXITO: Imagen guardada en: {out_img}")
            
            # 5. Guardar metadatos de escala para ArchiCAD
            out_meta = os.path.join(output_dir, f"{chip}-ortofoto_meta.txt")
            with open(out_meta, 'w') as f:
                f.write("Para insertar en ArchiCAD (Figure):\n")
                f.write(f"Ancho fisico del elemento: {buffer_m*2} metros\n")
                f.write("La imagen es un cuadrado perfecto de 400x400m.\n")
                f.write("Insertar en la capa: 00-20-20_Foto_Aerea_Referencia\n")
            print(f"Metadatos de escala guardados en: {out_meta}")
        else:
            print("ERROR: El servidor no devolvió una imagen válida.")
            print("Content-Type:", content_type)
    except Exception as e:
        print(f"Error descargando imagen: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Descarga ortofoto aérea para el lote")
    parser.add_argument("--chip", required=True, help="CHIP del predio")
    parser.add_argument("--output-dir", default="data/pot-cache", help="Directorio de salida")
    
    args = parser.parse_args()
    
    out_dir = os.path.join(PROJECT_ROOT, args.output_dir) if not os.path.isabs(args.output_dir) else args.output_dir
    main(args.chip, out_dir)
    