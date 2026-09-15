# -*- coding: utf-8 -*-
"""Apaga el Boolean Toggle que alimenta `bake` y `exportar` del componente
F1_CONTEXTO50_BUILD en el canvas v03 (F1_Contexto_Base-Editado_v03.ghx).

Efecto: `in_bake = False` y `in_exportar = False` -> el componente ya NO crea
objetos en el documento Rhino (ni bake a capa ni export .3dm). El resto del
componente (salida `volumenes` para los Morphs de ArchiCAD) queda intacto.

Idempotente y con backup por timestamp. Tras correrlo, regenerar el .gh con
GH_IO (scripts/utilities/ghx-to-gh.ps1).

Uso:
  python patch-ghx-bake-exportar-off.py
"""
import os
import shutil
import sys
import xml.etree.ElementTree as ET
from datetime import datetime

BASE = r"D:\Work\PROJECTS\DiseñoParametrico"
GHX = os.path.join(BASE, "gh-definitions", "F1_Contexto_Base-Editado_v03.ghx")

OBJ_INDEX = "152"                                        # Object del toggle
TOGGLE_GUID = "3f45df55-582b-48e8-98b1-992b6a0321d8"     # InstanceGuid del toggle
NEW_VALUE = "false"

ts = datetime.now().strftime("%Y-%m-%d-%H%M")
backup = GHX + ".bak-" + ts
shutil.copy2(GHX, backup)
print("backup:", backup)

tree = ET.parse(GHX)
root = tree.getroot()

obj = None
for el in root.iter():
    if el.get("name") == "Object" and el.get("index") == OBJ_INDEX:
        for s in el.iter():
            if s.get("name") == "InstanceGuid" and (s.text or "").strip() == TOGGLE_GUID:
                obj = el
                break
    if obj is not None:
        break

if obj is None:
    print("ERROR: no se encontro Object index {0} con GUID {1}".format(OBJ_INDEX, TOGGLE_GUID))
    sys.exit(1)

tv = None
for el in obj.iter():
    if el.get("name") == "ToggleValue":
        tv = el
        break
if tv is None:
    print("ERROR: ToggleValue no encontrado en el objeto {0}".format(OBJ_INDEX))
    sys.exit(1)

actual = (tv.text or "").strip().lower()
if actual == NEW_VALUE:
    print("ToggleValue ya esta en '{0}' (idempotente, sin cambios)".format(NEW_VALUE))
else:
    print("ToggleValue: '{0}' -> '{1}'".format(tv.text, NEW_VALUE))
    tv.text = NEW_VALUE
    tree.write(GHX, xml_declaration=True, encoding="utf-8")
    print("escrito:", GHX)

# --- validacion por re-lectura ---
t2 = ET.parse(GHX)
for el in t2.getroot().iter():
    if el.get("name") == "Object" and el.get("index") == OBJ_INDEX:
        for s in el.iter():
            if s.get("name") == "ToggleValue":
                print("VALIDACION: Object {0} ToggleValue = {1}".format(OBJ_INDEX, s.text))
