# -*- coding: utf-8 -*-
"""Renombra los componentes lectores de ArchiCAD en v12 (nombres reconocibles).

Mapeo verificado por trazado (2026-09-30):
  #36-Deconstruct 2D Polyline  -> Predio (-> #50-Discontinuity -> #61-Relay -> LADOS/PATIO)
  #43-Deconstruct 2D Polyline  -> Vias     (-> LADOS.vias_curves + #70-Merge)
  #44-Deconstruct 2D Polyline  -> Verdes   (-> #58-Relay -> #69-Curve -> LADOS.ep_curves)
  #45-Deconstruct 2D Polyline  -> Vecinos  (-> #55-Relay -> #66-Curve -> LADOS.vecinos_curves)
  #46-Deconstruct 2D Polyline  -> andenes  (-> #54-Relay -> #68-Curve -> LADOS.andenes_curves)

Uso: .venv\\Scripts\\python.exe scripts\\utilities\\patch-ghx-v12-readers-rename-2026-09-30.py
"""
import os
import shutil
import sys
import xml.etree.ElementTree as ET
from datetime import datetime

BASE = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
V12 = os.path.join(BASE, "gh-definitions", "F1_CONTEXTO_v12.ghx")

RENAMES = [
    ("#36-Deconstruct 2D Polyline", "#36-Predio"),
    ("#43-Deconstruct 2D Polyline", "#43-Vias"),
    ("#44-Deconstruct 2D Polyline", "#44-Verdes"),
    ("#45-Deconstruct 2D Polyline", "#45-Vecinos"),
    ("#46-Deconstruct 2D Polyline", "#46-andenes"),
]


def nick_of(obj):
    for i in obj.iter('item'):
        if i.get('name') == 'NickName' and i.text:
            return i.text.strip()
    return ''


def set_nick(obj, value):
    for i in obj.iter('item'):
        if i.get('name') == 'NickName':
            i.text = value
            return True
    return False


def main():
    tree = ET.parse(V12)
    root = tree.getroot()
    objs = [c for c in root.iter('chunk') if c.get('name') == 'Object']

    done = []
    for old, new in RENAMES:
        hit = None
        for o in objs:
            if nick_of(o) == old:
                hit = o
                break
        if hit is None:
            print("ERROR: no se encontro '{}'".format(old))
            sys.exit(1)
        set_nick(hit, new)
        done.append((old, new))
        print("  renombrado: '{}' -> '{}'".format(old, new))

    for w in root.iter():
        if w.tag == 'items':
            w.set('count', str(len([c for c in w if c.tag == 'item'])))
        elif w.tag == 'chunks':
            w.set('count', str(len([c for c in w if c.tag == 'chunk'])))

    root2 = ET.fromstring(ET.tostring(root, encoding='utf-8'))
    txt = ET.tostring(root2, encoding='unicode')
    ok = True
    for old, new in RENAMES:
        if old in txt:
            print("  [FAIL] viejo nombre aun presente:", old)
            ok = False
        if new not in txt:
            print("  [FAIL] falta nuevo nombre:", new)
            ok = False
    # guardias: nombres clave intactos
    for guard in ("#99-F1_ETAPA2_PATIO_v03.py", "#166-Number Slider", "#81-F1_ETAPA2_LADOS_v06.py"):
        if guard not in txt:
            print("  [FAIL] falta guardia:", guard)
            ok = False
    if ok:
        print("  [OK] renombres validados")
    else:
        sys.exit(1)

    ts = datetime.now().strftime('%Y%m%d-%H%M%S')
    bak = V12 + '.bak-' + ts
    shutil.copy2(V12, bak)
    data = ET.tostring(root, encoding='utf-8', xml_declaration=True)
    with open(V12, 'wb') as f:
        f.write(b'\xef\xbb\xbf' + data)
    print('backup:', bak)
    print('escrito:', V12)
    print('OK renombres aplicados')


if __name__ == '__main__':
    main()
