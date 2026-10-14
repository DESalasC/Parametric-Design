# -*- coding: utf-8 -*-
"""Re-embed updated source files into F1_CONTEXTO_v13.5.ghx using known GUIDs from dump-red-canvas."""
import os
import shutil
import xml.etree.ElementTree as ET
from datetime import datetime

BASE = r'D:\Work\PROJECTS\DiseñoParametrico'
GHX_PATH = os.path.join(BASE, "gh-definitions", "F1_CONTEXTO_v13.5.ghx")
BACKUP_DIR = os.path.join(BASE, "gh-definitions", "backups")
os.makedirs(BACKUP_DIR, exist_ok=True)
timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
backup_path = os.path.join(BACKUP_DIR, f"F1_CONTEXTO_v13.5.ghx.bak-{timestamp}")
shutil.copy2(GHX_PATH, backup_path)
print(f"Backup created: {backup_path}")

# Mapping from GUID (lowercase) to (source file path, description)
EMBEDS = {
    "6eaf2956": (os.path.join(BASE, "src", "fase-3-masa", "F3_DISTRIBUCION_v03.py"),
                 "#200 F3_DISTRIBUCION_v03.py → v03.9 (fix marcos)"),
    "8c7e8133": (os.path.join(BASE, "src", "fase-3-masa", "F3_VOLUM_GENERADOR_v08.py"),
                 "#198 F3_VOLUM_GENERADOR_v08.py → fix (d) + _safe_json_dumps"),
    "d3bed17b": (os.path.join(BASE, "src", "fase-1-contexto", "F1_ETAPA2_PATIO_v03.py"),
                 "#78 F1_ETAPA2_PATIO_v03.py → v03.4 (regla patio confirmada)"),
}

tree = ET.parse(GHX_PATH)
root = tree.getroot()

updated = []
for obj in root.iter('object'):
    guid = obj.get('instanceGuid')
    if guid:
        guid_lower = guid.lower()
        if guid_lower in EMBEDS:
            src_path, desc = EMBEDS[guid_lower]
            with open(src_path, 'r', encoding='utf-8') as f:
                source_text = f.read()
            # Find ScriptFile -> script
            for chunk in obj.iter('chunk'):
                if chunk.get('name') == 'ScriptFile':
                    for sub in chunk.iter('chunk'):
                        if sub.get('name') == 'script':
                            # Clear and set new text
                            sub.clear()
                            sub.text = source_text
                            updated.append((obj.get('nickName', ''), guid[:8], desc))
                            break
                    break

if updated:
    tree.write(GHX_PATH, encoding='utf-8', xml_declaration=True)
    print("Updated components:")
    for nick, guid8, desc in updated:
        print(f"  {nick} [{guid8}] - {desc}")
else:
    print("No components updated (check GUIDs).")

print(f"Patch re-embed completed. Backup: {backup_path}")