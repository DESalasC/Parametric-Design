# -*- coding: utf-8 -*-
"""Debug script to see what GUIDs are in the GHX file"""
import os
import xml.etree.ElementTree as ET

BASE = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
GHX_PATH = os.path.join(BASE, "gh-definitions", "F1_CONTEXTO_v13.5.ghx")

print(f"Reading: {GHX_PATH}")

tree = ET.parse(GHX_PATH)
root = tree.getroot()

# Find all objects
objects = list(root.iter('object'))
print(f"Found {len(objects)} object elements")

for i, obj in enumerate(objects):
    guid = obj.get('instanceGuid', '')
    nickname = obj.get('nickName', '')
    if guid:
        print(f"Object {i}: nickName='{nickname}', instanceGuid='{guid}'")
        
        # Look for ScriptFile to see what's currently embedded
        for chunk in obj.iter('chunk'):
            if chunk.get('name') == 'ScriptFile':
                for sub in chunk.iter('chunk'):
                    if sub.get('name') == 'script':
                        if len(sub) > 0 and sub[0].text:
                            # Get first 100 chars to see what's there
                            text_preview = sub[0].text[:100].replace('\n', '\\n')
                            print(f"    Script preview: {text_preview}...")
                        break
                break

# Now check what our script is looking for
EMBEDS = {
    "6eaf2956": ("src\\fase-3-masa\\F3_DISTRIBUCION_v03.py", "#200 F3_DISTRIBUCION_v03.py -> v03.9 (fix marcos)"),
    "8c7e8133": ("src\\fase-3-masa\\F3_VOLUM_GENERADOR_v08.py", "#198 F3_VOLUM_GENERADOR_v08.py -> fix (d) + _safe_json_dumps"),
    "d3bed17b": ("src\\fase-1-contexto\\F1_ETAPA2_PATIO_v03.py", "#78 F1_ETAPA2_PATIO_v03.py -> v03.4 (regla patio confirmada)"),
}

print("\nLooking for these GUIDs:")
for guid_lower, (src_rel, desc) in EMBEDS.items():
    print(f"  {guid_lower} -> {desc}")