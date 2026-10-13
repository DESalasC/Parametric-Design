#!/usr/bin/env python3
"""
Script para extraer cotas de arranque (z_base_m) de zonas por bloque
y generar niveles_deseados.json para F3_StorySync v02

Este script busca en el directorio del chip cualquier archivo JSON que contenga datos de zonas
con z_base_m, extrae las cotas por bloque y crea niveles_deseados.json.

Ubicacion de entrada: 
  {CHIP_DIR}/**/*.json (se busca recursivamente)
Salida: 
  {CHIP_DIR}/niveles_deseados.json
"""

import json
import os
import sys
from pathlib import Path

def json_contains_z_base(data):
    """Recursively check if a JSON object (dict/list) contains a z_base_m or z_base key."""
    if isinstance(data, dict):
        for key, value in data.items():
            if key in ('z_base_m', 'z_base', 'base_z', 'altura_base'):
                if isinstance(value, (int, float)) or (isinstance(value, str) and value.replace('.','',1).isdigit()):
                    return True
            if json_contains_z_base(value):
                return True
    elif isinstance(data, list):
        for item in data:
            if json_contains_z_base(item):
                return True
    return False

def extract_z_base_from_json(filepath):
    """
    Given a JSON file, try to extract z_base_m by block.
    Returns a dict {block: z_base_min} or None if not found.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"  Error leyendo {filepath.name}: {e}")
        return None

    # If the data itself contains z_base_m at top level (single zone)
    if isinstance(data, dict) and ('z_base_m' in data or 'z_base' in data):
        z_key = 'z_base_m' if 'z_base_m' in data else 'z_base'
        try:
            z_base = float(data[z_key])
            # Try to get block identifier
            bloque = data.get('bloque', data.get('block', 'default'))
            return {bloque: z_base}
        except (ValueError, TypeError):
            pass

    # If data is a list of zones
    if isinstance(data, list):
        zonas = data
    elif isinstance(data, dict):
        # Look for a key that holds a list of zones
        for key in ('zonas', 'zones', 'features', 'items', 'data'):
            if key in data and isinstance(data[key], list):
                zonas = data[key]
                break
        else:
            zonas = None
    else:
        zonas = None

    if zonas is not None:
        bloques_z_base = {}
        for zona in zonas:
            if not isinstance(zona, dict):
                continue
            z_base = None
            for z_key in ('z_base_m', 'z_base', 'base_z', 'altura_base'):
                if z_key in zona:
                    try:
                        z_base = float(zona[z_key])
                        break
                    except (ValueError, TypeError):
                        continue
            if z_base is None:
                continue
            bloque = zona.get('bloque', zona.get('block', 'default'))
            if bloque not in bloques_z_base:
                bloques_z_base[bloque] = []
            bloques_z_base[bloque].append(z_base)
        if bloques_z_base:
            return {bloque: min(z_list) for bloque, z_list in bloques_z_base.items()}

    # If we get here, we couldn't extract z_base from known structures
    return None

def main():
    if len(sys.argv) < 2:
        print("Error: Se requiere especificar el CHIP_ID como argumento")
        print("Uso: python extraer_z_base.py [CHIP_ID]")
        print("Ejemplo: python extraer_z_base.py B")
        print("         python extraer_z_base.py AAA0030JKOE")
        sys.exit(1)

    chip_id = sys.argv[1]
    print(f"Procesando chip: {chip_id}")

    # Build paths - using the junction to access D:\Work
    base_path = Path(r"C:\Users\Dario Salas\.openclaw-autoclaw\workspace\DWork\PROJECTS\DiseñoParametrico")
    chip_data_path = base_path / "data" / "fase-3-masa" / "casos" / chip_id

    if not chip_data_path.exists():
        print(f"Error: No se encuentra el directorio del chip: {chip_data_path}")
        print("Verifique que el CHIP_ID sea correcto")
        sys.exit(1)

    # Search for JSON files recursively
    json_files = list(chip_data_path.rglob("*.json"))
    if not json_files:
        print(f"Error: No se encontraron archivos JSON en {chip_data_path} ni subdirectorios")
        sys.exit(1)

    print(f"Encontrados {len(json_files)} archivos JSON. Buscando uno con datos de z_base...")

    # Try to find a JSON file that contains z_base data
    selected_file = None
    extracted_data = None

    for jfile in json_files:
        # First, quick check: does the file contain the string "z_base"?
        try:
            content = jfile.read_text(encoding='utf-8', errors='ignore')
            if 'z_base' in content.lower():
                print(f"  Candidato: {jfile.relative_to(chip_data_path)} (contiene 'z_base' en texto)")
                # Try to extract
                data = extract_z_base_from_json(jfile)
                if data is not None:
                    selected_file = jfile
                    extracted_data = data
                    break
        except Exception as e:
            print(f"  Error leyendo {jfile.name}: {e}")
            continue

    # If not found by content, try the most recent JSON file
    if selected_file is None:
        print("  No se encontró archivo con 'z_base' en contenido. Probando el más reciente...")
        json_files.sort(key=lambda f: f.stat().st_mtime, reverse=True)
        for jfile in json_files[:3]:  # Try the 3 most recent
            print(f"  Probando: {jfile.relative_to(chip_data_path)}")
            data = extract_z_base_from_json(jfile)
            if data is not None:
                selected_file = jfile
                extracted_data = data
                break

    if selected_file is None or extracted_data is None:
        print(f"Error: No se pudo extraer datos de z_base de ningún archivo JSON en {chip_data_path}")
        print("Archivos JSON encontrados:")
        for jfile in json_files:
            print(f"  {jfile.relative_to(chip_data_path)} ({jfile.stat().st_size} bytes)")
        print("\nPosibles soluciones:")
        print("1. Ejecutar primero el script F3_DISTRIBUCION para generar las zonas con z_base")
        print("2. Verificar que el archivo de salida de zonas se genere en este directorio")
        print("3. Revisar que las zonas tengan el atributo 'z_base_m' o similar")
        sys.exit(1)

    print(f"Archivo seleccionado: {selected_file.relative_to(chip_data_path)}")

    # Create output data
    output_data = {
        "chip": chip_id,
        "timestamp": str(Path().absolute()),
        "fuente": selected_file.name,
        "niveles_deseados_m": extracted_data,
        "descripcion": "Cotas de arranque (z_base_m) por bloque para stories en ArchiCAD",
        "instrucciones": "Copiar estos valores a los stories correspondientes en ArchiCAD usando la herramienta de stories",
        "metadata": {
            "total_bloques": len(extracted_data),
            "rango_z_base": f"{min(extracted_data.values()):.3f} - {max(extracted_data.values()):.3f} m"
        }
    }

    # Save output in the chip's directory
    niveles_output_path = chip_data_path / "niveles_deseados.json"
    with open(niveles_output_path, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)

    print(f"\nExito: Se generó {niveles_output_path}")
    print("Niveles deseados por bloque:")
    for bloque, nivel in sorted(extracted_data.items()):
        print(f"  Bloque {bloque}: {nivel:.3f} m")

    print(f"\nMetadata:")
    print(f"  Total bloques: {len(extracted_data)}")
    print(f"  Rango z_base: {min(extracted_data.values()):.3f} - {max(extracted_data.values()):.3f} m")

    print("\nProximos pasos para el operador:")
    print("1. Abrir ArchiCAD y navegar al archivo del proyecto")
    print("2. Usar la herramienta de Stories para crear stories en cada bloque")
    print("3. Asignar la z_base correspondiente (en metros) a cada story")
    print("4. Ejecutar F3_StorySync v02 --check para verificar")
    print("5. Continuar con la generación de volumenes en Grasshopper")

if __name__ == "__main__":
    main()