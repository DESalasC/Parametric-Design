# -*- coding: utf-8 -*-
"""Update CodeInput items in specific objects with current source file content."""
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
print("Backup creado: " + backup_path)

# Map InstanceGuid to (source path, description)
# Using ASCII-only descriptions to avoid encoding issues
TARGETS = {
    "d3bed17b-1b6b-4e89-8761-1985327b292b": ("src\\fase-1-contexto\\F1_ETAPA2_PATIO_v03.py", "#78 F1_ETAPA2_PATIO_v03.py -> v03.4 (regla patio confirmada)"),
    "6eaf2956-f649-4540-a900-4b32a10deee4": ("src\\fase-3-masa\\F3_DISTRIBUCION_v03.py", "#200 F3_DISTRIBUCION_v03.py -> v03.9 (fix de marcos)"),
    "8c7e8133-0bbe-401d-9fa0-6c4b761bbc5d": ("src\\fase-3-masa\\F3_VOLUM_GENERADOR_v08.py", "#198 F3_VOLUM_GENERADOR_v08.py -> fix (d) + _safe_json_dumps"),
    "ba3eb3a5-e134-445e-9032-175bee846605": ("src\\fase-1-contexto\\F1_CONTEXTO50_BUILD_v01.2.py", "z_origen F1_CONTEXTO50_BUILD_v01.2.py -> v01.3 (fix dz + output)"),
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
for target_guid, (src_rel, desc) in TARGETS.items():
    # Find the object with this InstanceGuid
    target_obj = None
    for obj in definition_objects.iter('chunk'):
        if obj.get('name') == 'Object':
            # Look for InstanceGuid item
            for item in obj.iter('item'):
                if item.get('name') == 'InstanceGuid' and item.text:
                    guid_text = item.text.strip()
                    if guid_text.lower() == target_guid.lower():
                        target_obj = obj
                        break
            if target_obj:
                break
    
    if target_obj is None:
        print("WARNING: Object with InstanceGuid " + target_guid + " not found")
        continue
    
    # Read source file
    src_path = os.path.join(BASE, src_rel)
    try:
        # Read as binary and decode utf-8 to avoid encoding issues
        with open(src_path, 'rb') as f:
            source_bytes = f.read()
        source_content = source_bytes.decode('utf-8')
        # Normalize line endings: CRLF -> LF (critical for Python explicit line continuations)
        source_content = source_content.replace('\r\n', '\n').replace('\r', '\n')
    except Exception as e:
        print("ERROR reading source file " + src_path + ": " + str(e))
        continue
    
    # Find CodeInput item and replace its text
    codeinput_updated = False
    for item in target_obj.iter('item'):
        if item.get('name') == 'CodeInput':
            # Get nick name for reporting
            nick_name = None
            for item2 in target_obj.iter('item'):
                if item2.get('name') == 'NickName' and item2.text:
                    nick_name = item2.text
                    break
            
            # Update the CodeInput text
            item.text = source_content
            codeinput_updated = True
            # Print without Unicode characters that cause encoding issues
            print("Updated Object with InstanceGuid " + target_guid[:8] + "... (NickName: '" + (nick_name or 'N/A') + "') - " + desc.encode('ascii', 'replace').decode('ascii'))
            print("  CodeInput length: " + str(len(source_content)) + " characters")
            break
    
    if not codeinput_updated:
        print("WARNING: No CodeInput item found in Object with InstanceGuid " + target_guid)
    else:
        updated_count += 1

if updated_count > 0:
    tree.write(GHX_PATH, encoding='utf-8', xml_declaration=True)
    print("\nSuccessfully updated " + str(updated_count) + " component(s).")
else:
    print("\nNo components updated.")