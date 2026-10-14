# -*- coding: utf-8 -*-
"""Extract GUIDs for specific components from F1_CONTEXTO_v13.5.ghx by NickName or Name."""
import os
import xml.etree.ElementTree as ET

BASE = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
GHX_PATH = os.path.join(BASE, "gh-definitions", "F1_CONTEXTO_v13.5.ghx")

# We know the component names (as they appear in the canvas) from previous context:
TARGETS = [
    "F3_DISTRIBUCION_v03.py",
    "F3_VOLUM_GENERADOR_v08.py",
    "F1_ETAPA2_PATIO_v03.py",
]

tree = ET.parse(GHX_PATH)
root = tree.getroot()

guid_map = {}
for obj in root.iter('object'):
    nick = obj.get('nickName', '')
    name = obj.get('name', '')
    guid = obj.get('instanceGuid', '')
    for target in TARGETS:
        if target in nick or target in name:
            guid_map[target] = guid.lower()
            break

print("GUIDs found:")
for target, guid in guid_map.items():
    print(f"{target}: {guid}")

# If we have all three, write a small script to re-embed using these GUIDs.
if len(guid_map) == 3:
    print("\nAll three GUIDs found. Ready to re-embed.")
else:
    print("\nWARNING: Not all GUIDs found. Check the names in the canvas.")