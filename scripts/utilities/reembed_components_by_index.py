# -*- coding: utf-8 -*-
"""Parche de re-embebido por índice de objeto: actualiza componentes en F1_CONTEXTO_v13.5.ghx a versiones de source.
Actualiza basado en el índice del objeto en lugar del GUID (que parecía estar incorrecto en el mapeo original):
- Índice 191: F3_DISTRIBUCION_v03.py → v03.9 (fix de marcos) 
- Índice 194: F3_VOLUM_GENERADOR_v08.py → fix (d) + _safe_json_dumps
- Índice 2: F1_ETAPA2_PATIO_v03.py → v03.4 (regla patio confirmada)
Guarda backup .bak-YYYYMMDD-HHMMSS antes de escribir.
"""
import os
import shutil
import xml.etree.ElementTree as ET
from datetime import datetime

BASE = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
GHX_PATH = os.path.join(BASE, "gh-definitions", "F1_CONTEXTO_v13.5.ghx")
BACKUP_DIR = os.path.join(BASE, "gh-definitions", "backups")
os.makedirs(BACKUP_DIR, exist_ok=True)
timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
backup_path = os.path.join(BACKUP_DIR, f"F1_CONTEXTO_v13.5.ghx.bak-{timestamp}")
shutil.copy2(GHX_PATH, backup_path)
print(f"Backup creado: {backup_path}")

# Mapeo de índice de objeto a (ruta source, descripción)
EMBEDS_BY_INDEX = {
    "191": ("src\\fase-3-masa\\F3_DISTRIBUCION_v03.py", "#200 F3_DISTRIBUCION_v03.py → v03.9 (fix marcos)"),
    "194": ("src\\fase-3-masa\\F3_VOLUM_GENERADOR_v08.py", "#198 F3_VOLUM_GENERADOR_v08.py → fix (d) + _safe_json_dumps"),
    "2": ("src\\fase-1-contexto\\F1_ETAPA2_PATIO_v03.py", "#78 F1_ETAPA2_PATIO_v03.py → v03.4 (regla patio confirmada)"),
}

tree = ET.parse(GHX_PATH)
root = tree.getroot()

actualizados = []
# Buscar el chunk DefinitionObjects
definition_objects = None
for chunk in root.iter('chunk'):
    if chunk.get('name') == 'DefinitionObjects':
        definition_objects = chunk
        break

if definition_objects is not None:
    # Buscar todos los Object chunks dentro de DefinitionObjects
    for obj in definition_objects.iter('chunk'):
        if obj.get('name') == 'Object':
            obj_index = obj.get('index')
            if obj_index in EMBEDS_BY_INDEX:
                src_rel, desc = EMBEDS_BY_INDEX[obj_index]
                src_path = os.path.join(BASE, src_rel)
                try:
                    with open(src_path, 'r', encoding='utf-8') as f:
                        source_content = f.read()
                    
                    # Buscar el archivo embebido dentro del objeto (custom user object)
                    for chunk in obj.iter('chunk'):
                        if chunk.get('name') == 'ScriptFile':
                            # Reemplazar el contenido del script
                            for sub in chunk.iter('chunk'):
                                if sub.get('name') == 'script':
                                    # Asumimos que el primer child es el texto
                                    sub.clear()
                                    sub.text = source_content
                                    # Obtener el nickName para el reporte
                                    nick_name = None
                                    for item in obj.iter('item'):
                                        if item.get('name') == 'NickName' and item.text:
                                            nick_name = item.text
                                            break
                                    actualizados.append((nick_name or f'Object[{obj_index}]', obj_index, desc))
                                    break
                            break
                except FileNotFoundError:
                    print(f"Advertencia: Archivo fuente no encontrado: {src_path}")
                except Exception as e:
                    print(f"Error leyendo archivo fuente {src_path}: {e}")

if actualizados:
    tree.write(GHX_PATH, encoding='utf-8', xml_declaration=True)
    print("Actualizados:")
    for nick, idx, desc in actualizados:
        print(f"  {nick} [índice:{idx}] - {desc}")
else:
    print("No se actualizó ningún componente.")

print(f"Parche de re-embebido completado. Backup: {backup_path}")