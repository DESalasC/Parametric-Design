# -*- coding: utf-8 -*-
"""Re-embeje Z-BASE real: reemplaza el CodeInput de los 5 componentes GHPython
en F1_CONTEXTO_v13.5.ghx con el código fuente de src/.

Estructura del .ghx (verificada):
  <chunk name="Object">
    <items count="3">
      <item name="Name" type_name="gh_string" type_code="10">GhPython Script</item>
      <item name="GUID" ...>...</item>
      <item name="Lib" ...>...</item>
    </items>
    <chunks count="1">
      <chunk name="Container">
        <items count="12">
          <item name="CodeInput" type_name="gh_string" type_code="10">CÓDIGO PYTHON</item>
          <item name="NickName" type_name="gh_string" type_code="10">#NN-...py</item>
          ...
        </items>
      </chunk>
    </chunks>
  </chunk>

Hace backup .bak-zbase-YYYYMMDD-HHMMSS antes de escribir.
"""
import os
import shutil
import xml.etree.ElementTree as ET
from datetime import datetime

BASE = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
GHX_PATH = os.path.join(BASE, "gh-definitions", "F1_CONTEXTO_v13.5.ghx")

BACKUP_DIR = os.path.join(BASE, "gh-definitions", "backups")
os.makedirs(BACKUP_DIR, exist_ok=True)
timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
backup_path = os.path.join(BACKUP_DIR, f"F1_CONTEXTO_v13.5.ghx.bak-zbase-{timestamp}")
shutil.copy2(GHX_PATH, backup_path)
print(f"Backup creado: {backup_path}")

# Mapeo NickName -> (ruta source, descripcion)
# NickNames verificados en el .ghx real (17/10/2026):
EMBEDS = {
    "#45-F1_CONTEXTO50_BUILD_v01.3.py": (
        "src\\fase-1-contexto\\F1_CONTEXTO50_BUILD_v01.2.py",
        "#45 F1_CONTEXTO50_BUILD -> compute_dz return 0.0 (LOCAL Z)"
    ),
    "#80-F1_ETAPA2_PATIO_v03.py": (
        "src\\fase-1-contexto\\F1_ETAPA2_PATIO_v03.py",
        "#80 F1_ETAPA2_PATIO -> v03.4 (regla patio 1 vs >=2 vol)"
    ),
    "#81-F1_ETAPA1_CONTEXTO_v02.py": (
        "src\\fase-1-contexto\\F1_ETAPA1_CONTEXTO_v02.py",
        "#81 F1_ETAPA1_CONTEXTO -> LOCAL Z (Z_abs - Z_base)"
    ),
    "#200-F3_DISTRIBUCION_v03.py": (
        "src\\fase-3-masa\\F3_DISTRIBUCION_v03.py",
        "#200 F3_DISTRIBUCION -> v03.9 (fix marcos escalonamiento)"
    ),
    "#201-F3_VOLUM_GENERADOR_v08.py": (
        "src\\fase-3-masa\\F3_VOLUM_GENERADOR_v08.py",
        "#201 F3_VOLUM_GENERADOR -> v08.2 (entradas LOCAL Z, z_origin=0)"
    ),
}

tree = ET.parse(GHX_PATH)
root = tree.getroot()

total_ghpython = 0
actualizados = []
pendiente = set(EMBEDS.keys())

for obj in root.iter('chunk'):
    if obj.get('name') != 'Object':
        continue

    name_val = None
    for item in obj.iter('item'):
        if item.get('name') == 'Name' and item.text:
            name_val = item.text.strip()
            break

    if name_val != 'GhPython Script':
        continue

    total_ghpython += 1

    nick_name = None
    for item in obj.iter('item'):
        if item.get('name') == 'NickName' and item.text:
            nick_name = item.text.strip()
            break

    if nick_name not in EMBEDS:
        continue

    src_rel, desc = EMBEDS[nick_name]
    src_path = os.path.join(BASE, src_rel)
    try:
        with open(src_path, 'rb') as f:
            source_content = f.read().decode('utf-8')
    except Exception as e:
        print(f"ERROR leyendo {src_path}: {e}")
        continue

    code_input_found = False
    for item in obj.iter('item'):
        if item.get('name') == 'CodeInput' and item.get('type_name') == 'gh_string':
            item.text = source_content
            code_input_found = True
            break

    if code_input_found:
        actualizados.append((nick_name, desc))
        pendiente.discard(nick_name)
        print(f"OK  {nick_name:55s} - {desc}")
    else:
        print(f"WARN  {nick_name}: no se encontro CodeInput")

if actualizados:
    tree.write(GHX_PATH, encoding='utf-8', xml_declaration=True)
    print(f"\nActualizados {len(actualizados)} componente(s) en {GHX_PATH}")
else:
    print("\nNingún componente actualizado.")

if pendiente:
    print(f"\nNO ENCONTRADOS en el .ghx: {sorted(pendiente)}")
    print(f"Total objetos GHPython en el archivo: {total_ghpython}")

print(f"Backup: {backup_path}")
