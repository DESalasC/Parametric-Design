# -*- coding: utf-8 -*-
"""Parchea el componente F1_ETAPA1_CONTEXTO embebido en el canvas F1_CONTEXTO_v11.ghx.

Reemplaza el CodeInput por el codigo del .py fuente (F1_ETAPA1_CONTEXTO_v03.py).
Idempotente. Despues de correr, regenerar el .gh con:
  GH_IO.dll: ReadFromFile(.ghx) -> WriteToFile(.gh)

Uso:
  python patch-ghx-f1etapa1-v03.py
"""
import io
import os
import shutil
import sys
import xml.etree.ElementTree as ET
from datetime import datetime

BASE = r"D:\Work\PROJECTS\DiseñoParametrico"
GHX = os.path.join(BASE, "gh-definitions", "F1_CONTEXTO_v11.ghx")
PY_FIXED = os.path.join(BASE, "src", "fase-1-contexto", "F1_ETAPA1_CONTEXTO_v03.py")
NICKNAME_TO_FIND = "F1_ETAPA1_CONTEXTO_v02"  # Updated to match actual nickname

ts = datetime.now().strftime("%Y-%m-%d-%H%M")
BACKUP = GHX + ".bak-" + ts

shutil.copy2(GHX, BACKUP)
print("backup:", BACKUP)

with io.open(PY_FIXED, "rb") as f:
    CODIGO_NUEVO = f.read().decode("utf-8")
print("codigo nuevo: {0} chars".format(len(CODIGO_NUEVO)))

tree = ET.parse(GHX)
root = tree.getroot()
parent = {c: p for p in root.iter() for c in p}

# Find the component (Object) with the given nickname
target_obj = None
for obj in root.iter():
    if obj.get("name") == "Object" and obj.get("index") is not None:
        # Look for NickName inside this object
        for child in obj.iter():
            if child.get("name") == "NickName" and (child.text or "").strip() == NICKNAME_TO_FIND:
                target_obj = obj
                break
        if target_obj:
            break

if target_obj is None:
    print("ERROR: no se encontro el componente con nickname '{}'".format(NICKNAME_TO_FIND))
    sys.exit(1)

print("Object index:", target_obj.get("index"))

# Find the CodeInput inside this component
code_el = None
for el in target_obj.iter():
    if el.get("name") == "CodeInput" and el.text and len(el.text) > 1000:  # heuristic for script
        code_el = el
        break

if code_el is None:
    print("ERROR: no se encontro el CodeInput dentro del componente")
    sys.exit(1)

if (code_el.text or "") == CODIGO_NUEVO:
    print("CodeInput ya esta actualizado")
else:
    viejo = len(code_el.text or "")
    code_el.text = CODIGO_NUEVO
    print("CodeInput: {0} -> {1} chars".format(viejo, len(CODIGO_NUEVO)))

# Write the patched GHX
tree.write(GHX, xml_declaration=True, encoding="utf-8")
print("escrito:", GHX)

# Optional: validate by reading back and checking the CodeInput
tree2 = ET.parse(GHX)
root2 = tree2.getroot()
# We could do a more thorough validation, but for now just check that the text is present
for el in root2.iter():
    if el.get("name") == "CodeInput" and el.text and "F1_ETAPA1_CONTEXTO_v03.py" in el.text:
        print("VALIDACION: CodeInput contiene el script actualizado")
        break
else:
    print("ADVERTENCIA: No se pudo validar que el CodeInput tenga el nuevo script")