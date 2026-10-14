# -*- coding: utf-8 -*-
"""Final re-embedding script for the three components."""
import os
import shutil
import xml.etree.ElementTree as ET

BASE = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
GHX_PATH = os.path.join(BASE, "gh-definitions", "F1_CONTEXTO_v13.5.ghx")

# Create backup
BACKUP_DIR = os.path.join(BASE, "gh-definitions", "backups")
os.makedirs(BACKUP_DIR, exist_ok=True)
from datetime import datetime
timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
backup_path = os.path.join(BACKUP_DIR, f"F1_CONTEXTO_v13.5.ghx.bak-{timestamp}")
shutil.copy2(GHX_PATH, backup_path)
print(f"Backup creado: {backup_path}")

# Define what to embed: index -> (source path, description)
EMBEDS = {
    "191": ("src\\fase-3-masa\\F3_DISTRIBUCION_v03.py", "#200 F3_DISTRIBUCION_v03.py → v03.9 (fix de marcos)"),
    "194": ("src\\fase-3-masa\\F3_VOLUM_GENERADOR_v08.py", "#198 F3_VOLUM_GENERADOR_v08.py → fix (d) + _safe_json_dumps"),
    "2": ("src\\fase-1-contexto\\F1_ETAPA2_PATIO_v03.py", "#78 F1_ETAPA2_PATIO_v03.py → v03.4 (regla patio confirmada)"),
}

tree = ET.parse(GHX_PATH)
root = tree.getroot()

# Find DefinitionObjects
definition_objects = None
for chunk in root.iter('chunk'):
    if chunk.get('name') == 'DefinitionObjects':
        definition_objects = chunk
        break

if definition_objects is None:
    print("ERROR: No DefinitionObjects chunk found")
    exit(1)

updated_count = 0
for obj_index, (src_rel, desc) in EMBEDS.items():
    # Find the object with this index
    target_obj = None
    for obj in definition_objects.iter('chunk'):
        if obj.get('name') == 'Object' and obj.get('index') == obj_index:
            target_obj = obj
            break
    
    if target_obj is None:
        print(f"WARNING: Object with index {obj_index} not found")
        continue
    
    # Read source file
    src_path = os.path.join(BASE, src_rel)
    try:
        # Read as binary and decode utf-8 to avoid encoding issues
        with open(src_path, 'rb') as f:
            source_bytes = f.read()
        source_content = source_bytes.decode('utf-8')
    except Exception as e:
        print(f"ERROR reading source file {src_path}: {e}")
        continue
    
    # Find ScriptFile and replace script content
    script_updated = False
    for chunk in target_obj.iter('chunk'):
        if chunk.get('name') == 'ScriptFile':
            for sub in chunk.iter('chunk'):
                if sub.get('name') == 'script':
                    # Clear and set new text
                    sub.clear()
                    sub.text = source_content
                    script_updated = True
                    # Get nick name for reporting
                    nick_name = None
                    for item in target_obj.iter('item'):
                        if item.get('name') == 'NickName' and item.text:
                            nick_name = item.text
                            break
                    print(f"Updated Object[{obj_index}] (NickName: '{nick_name or 'N/A'}') - {desc}")
                    print(f"  Script length: {len(source_content)} characters")
                    break
            if script_updated:
                break
    
    if not script_updated:
        print(f"WARNING: No ScriptFile/script found in Object[{obj_index}]")
    else:
        updated_count += 1

if updated_count > 0:
    tree.write(GHX_PATH, encoding='utf-8', xml_declaration=True)
    print(f"\nSuccessfully updated {updated_count} component(s).")
else:
    print("\nNo components were updated.")

print(f"Backup saved to: {backup_path}")