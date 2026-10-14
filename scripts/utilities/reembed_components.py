# -*- coding: utf-8 -*-
"""Parche de re-embebido: actualiza componentes en F1_CONTEXTO_v13.5.ghx a versiones de source.
Actualiza:
- #200 F3_DISTRIBUCION_v03.py → v03.9 (fix de marcos)
- #198 F3_VOLUM_GENERADOR_v08.py → fix (d) + _safe_json_dumps
- #78  F1_ETAPA2_PATIO_v03.py   → v03.4 ( crater rule confirmada)
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

# Mapeo de GUID a (ruta source, descripción) obtenidos de dump-red-canvas
EMBEDS = {
    "6eaf2956": ("src\\fase-3-masa\\F3_DISTRIBUCION_v03.py", "#200 F3_DISTRIBUCION_v03.py → v03.9 (fix marcos)"),
    "8c7e8133": ("src\\fase-3-masa\\F3_VOLUM_GENERADOR_v08.py", "#198 F3_VOLUM_GENERADOR_v08.py → fix (d) + _safe_json_dumps"),
    "d3bed17b": ("src\\fase-1-contexto\\F1_ETAPA2_PATIO_v03.py", "#78 F1_ETAPA2_PATIO_v03.py → v03.4 (regla patio confirmada)"),
}

tree = ET.parse(GHX_PATH)
root = tree.getroot()

actualizados = []
for obj in root.iter('object'):
    guid = obj.get('instanceGuid', '')
    if guid:
        guid_lower = guid.lower()
        if guid_lower in EMBEDS:
            src_rel, desc = EMBEDS[guid_lower]
            src_path = os.path.join(BASE, src_rel)
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
                            actualizados.append((obj.get('nickName', ''), guid[:8], desc))
                            break
                    break

if actualizados:
    tree.write(GHX_PATH, encoding='utf-8', xml_declaration=True)
    print("Actualizados:")
    for nick, guid8, desc in actualizados:
        print(f"  {nick} [{guid8}] - {desc}")
else:
    print("No se actualizó ningún componente (revisar GUIDs).")

print(f"Parche de re-embebido completado. Backup: {backup_path}")