"""
Script: generate-archicad-layers-xml-v3.py
Proyecto: DiseñoParametrico
Fase: 0 - Setup BIM
Versión: 03
Descripción: 
    Lee el archivo CSV de capas (incluyendo extensiones) y genera un XML
    con el formato exacto (AttributeFile) requerido por el Administrador 
    de Atributos de ArchiCAD.
"""

import csv
import os
import sys
import uuid
from xml.sax.saxutils import escape

# Configuración de rutas
CSV_PATH = r"D:\Users\Dario Salas\proyectos\DesParametrico\2-Entradas\Plantillas_ArchiCAD\Layers.csv"
PROJECT_ROOT = os.environ.get("DISENO_PARAMETRICO_ROOT", os.getcwd())
OUTPUT_XML = os.path.join(PROJECT_ROOT, "data", "GuBIMclass_Layers_v3.xml")

def main():
    if not os.path.exists(CSV_PATH):
        print(f"ERROR: No se encontró el CSV en {CSV_PATH}")
        sys.exit(1)

    print(f"Leyendo CSV: {CSV_PATH}")
    
    layers = []
    try:
        with open(CSV_PATH, 'r', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            for row in reader:
                name = row.get('name') or row.get('Name') or row.get('gubimclass_name') or ""
                code = row.get('code') or row.get('gubimclass_code') or ""
                ext = row.get('extension') or row.get('Extension') or row.get('ext') or ""
                
                name = name.strip()
                code = code.strip()
                ext = ext.strip()[:4] # ArchiCAD limita a 4 caracteres
                
                if name:
                    final_name = f"{code} - {name}" if code else name
                    # Guardamos nombre y extensión juntos
                    layers.append({"name": final_name, "ext": ext})
    except Exception as e:
        print(f"Error leyendo el CSV: {e}")
        sys.exit(1)

    if not layers:
        print("ERROR: No se extrajeron capas del CSV.")
        sys.exit(1)

    print(f"Capas extraídas: {len(layers)}. Generando XML nativo de ArchiCAD...")

    os.makedirs(os.path.dirname(OUTPUT_XML), exist_ok=True)
    
    with open(OUTPUT_XML, 'w', encoding='utf-8') as f:
        # Cabecera exacta requerida por ArchiCAD
        f.write('<?xml version="1.0" encoding="UTF-8" standalone="no" ?>\n')
        f.write('<AttributeFile Mv="1" Sv="2">\n')
        f.write('\t<PlatformSign>22359</PlatformSign>\n')
        f.write('\t<RegisteredAttributes>\n')
        f.write('\t\t<NumberOfRegisteredAttributes>1</NumberOfRegisteredAttributes>\n')
        
        # Sección de Capas
        f.write('\t\t<Attributes Type="Layers">\n')
        f.write('\t\t\t<RefID>1279351090</RefID>\n')
        
        for idx, layer in enumerate(layers, start=1):
            guid = str(uuid.uuid4()).upper()
            name_escaped = escape(layer["name"])
            ext_escaped = escape(layer["ext"]) if layer["ext"] else ""
            
            f.write(f'\t\t\t<Layer Idx="{idx}" Name="{name_escaped}">\n')
            f.write('\t\t\t\t<OdbObj Mv="2" Sv="0">\n')
            f.write('\t\t\t\t\t<OdbRef>\n')
            f.write(f'\t\t\t\t\t\t<guid>{guid}</guid>\n')
            f.write('\t\t\t\t\t</OdbRef>\n')
            f.write('\t\t\t\t\t<CreaTime>23970</CreaTime>\n')
            f.write('\t\t\t\t\t<ModiTime>23972</ModiTime>\n')
            f.write('\t\t\t\t</OdbObj>\n')
            
            # Nombre y Extensión
            f.write(f'\t\t\t\t<Name>{name_escaped}</Name>\n')
            if ext_escaped:
                f.write(f'\t\t\t\t<Extension>{ext_escaped}</Extension>\n')
                
            f.write(f'\t\t\t\t<Index>{idx}</Index>\n')
            f.write('\t\t\t\t<Flags/>\n')
            f.write('\t\t\t\t<ModiTime>1164398284</ModiTime>\n')
            f.write('\t\t\t\t<RegMemoTable MemoNumber="0" Mv="1" Sv="0"/>\n')
            f.write('\t\t\t\t<ReadOnly>false</ReadOnly>\n')
            f.write('\t\t\t\t<ConnectionClassId>1</ConnectionClassId>\n')
            f.write('\t\t\t</Layer>\n')
            
        f.write('\t\t</Attributes>\n')
        
        # Cerrar estructura de atributos vacíos
        empty_attrs = [
            "Composites", "Dimension Standards", "Fills", "Layer Combinations", 
            "Lines", "Surfaces", "Pens", "Zone Categories", "Issue Styles", 
            "Profiles", "MEP Systems", "Operation Profiles", 
            "Renovation Override Styles", "Building Materials"
        ]
        ref_ids = {
            "Composites": "1129791794", "Dimension Standards": "1398033970",
            "Fills": "1179208755", "Layer Combinations": "1279479602",
            "Lines": "1279872562", "Surfaces": "1296127026",
            "Pens": "1347699276", "Zone Categories": "1380795186",
            "Issue Styles": "1297306713", "Profiles": "1347571526",
            "MEP Systems": "1296388179", "Operation Profiles": "1162104656",
            "Renovation Override Styles": "1196381778", "Building Materials": "1112359252"
        }
        
        for attr in empty_attrs:
            f.write(f'\t\t<Attributes Type="{attr}">\n')
            f.write(f'\t\t\t<RefID>{ref_ids[attr]}</RefID>\n')
            f.write('\t\t</Attributes>\n')
            
        f.write('\t</RegisteredAttributes>\n')
        f.write('\t<Folders>\n')
        f.write('\t\t<TypeRoot RefID="1279351090"/>\n')
        f.write('\t</Folders>\n')
        f.write('</AttributeFile>\n')

    print(f"\n✅ ÉXITO: Archivo XML nativo guardado en: {OUTPUT_XML}")
    print("   Impórtalo desde ArchiCAD: Opciones > Atributos de Elemento > Administrador de Atributos > Importar")

if __name__ == "__main__":
    main()
