# -*- coding: utf-8 -*-
"""Parchea F1_CONTEXTO_v12.ghx: PATIO v03.0 -> v03.1 (inferencia AUTO).

Cambios (2026-09-30, tarde):
  1. #99-F1_ETAPA2_PATIO_v03.py -> embebe F1_ETAPA2_PATIO_v03.py actualizado
     (modo AUTO: n_volumenes=0/vacio -> inferido; 1=unico forzado; >=2=multi).
  2. Slider #166: Min=0, Value=0 (0 = AUTO; el operador no necesita tocar nada).
  3. Backup .bak-<ts>, validaciones (marcadores v03.1 / A_REF_VOL_M2 / modo AUTO,
     valores del slider, duplicados), escritura con BOM.

Uso: .venv\\Scripts\\python.exe scripts\\utilities\\patch-ghx-v12-patio-v031-2026-09-30.py
"""
import io
import os
import shutil
import sys
import xml.etree.ElementTree as ET
from datetime import datetime

BASE = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
V12 = os.path.join(BASE, "gh-definitions", "F1_CONTEXTO_v12.ghx")
SRC = os.path.join(BASE, "src", "fase-1-contexto", "F1_ETAPA2_PATIO_v03.py")


def nick_of(obj):
    for i in obj.iter('item'):
        if i.get('name') == 'NickName' and i.text:
            return i.text.strip()
    return ''


def cont_get(obj, name):
    for c in obj.iter('chunk'):
        if c.get('name') == 'Container':
            for w in c:
                if w.tag == 'items':
                    for i in w:
                        if i.tag == 'item' and i.get('name') == name:
                            return i
    return None


def find_obj(root, prefix):
    for o in root.iter('chunk'):
        if o.get('name') == 'Object' and nick_of(o).startswith(prefix):
            return o
    return None


def count_sibling_dups(rt):
    bad_c = 0
    for w in rt.iter():
        if w.tag == 'chunks':
            s = {}
            for c in w:
                if c.tag != 'chunk':
                    continue
                key = (c.get('name'), c.get('index'))
                if key in s:
                    bad_c += 1
                s[key] = 1
    return bad_c


def main():
    tree = ET.parse(V12)
    root = tree.getroot()

    o99 = find_obj(root, '#99-F1_ETAPA2_PATIO')
    if o99 is None:
        print('ERROR: no se encontro #99'); sys.exit(1)
    o166 = find_obj(root, '#166-Number Slider')
    if o166 is None:
        print('ERROR: no se encontro #166'); sys.exit(1)

    code_new = io.open(SRC, 'r', encoding='utf-8').read().replace('\r\n', '\n')
    ci = cont_get(o99, 'CodeInput')
    print('CodeInput previo: {} chars | nuevo: {} chars'.format(len(ci.text or ''), len(code_new)))
    ci.text = code_new

    # slider: Min=0, Value=0 (0 = AUTO)
    for ch in o166.iter('chunk'):
        if ch.get('name') == 'Slider':
            for i in ch.iter('item'):
                if i.get('name') == 'Min':
                    i.text = '0'
                elif i.get('name') == 'Value':
                    i.text = '0'

    for w in root.iter():
        if w.tag == 'items':
            w.set('count', str(len([c for c in w if c.tag == 'item'])))
        elif w.tag == 'chunks':
            w.set('count', str(len([c for c in w if c.tag == 'chunk'])))

    root2 = ET.fromstring(ET.tostring(root, encoding='utf-8'))
    txt = ET.tostring(root2, encoding='unicode')

    # valores del slider tras el cambio
    mn = vl = None
    o166b = find_obj(root2, '#166-Number Slider')
    for ch in o166b.iter('chunk'):
        if ch.get('name') == 'Slider':
            for i in ch.iter('item'):
                if i.get('name') == 'Min':
                    mn = i.text
                elif i.get('name') == 'Value':
                    vl = i.text

    seen = {}
    dups = 0
    for i in root2.iter('item'):
        if i.get('name') == 'InstanceGuid' and i.text:
            g = i.text.strip()
            if g in seen:
                dups += 1
            seen[g] = True
    dups_chunk = count_sibling_dups(root2)

    ok = True
    checks = [
        ('codigo v03.1', 'v03.1' in txt and 'A_REF_VOL_M2' in txt and 'modo AUTO' in txt),
        ('slider Min=0', mn == '0'),
        ('slider Value=0', vl == '0'),
        ('sin duplicados de chunk', dups_chunk == 0),
        ('sin InstanceGuid duplicados', dups == 0),
    ]
    for nm, okc in checks:
        print('  [{}] {}'.format('OK' if okc else 'FAIL', nm))
        ok = ok and okc
    if not ok:
        print('VALIDACION FALLIDA - no se escribe'); sys.exit(1)

    ts = datetime.now().strftime('%Y%m%d-%H%M%S')
    bak = V12 + '.bak-' + ts
    shutil.copy2(V12, bak)
    data = ET.tostring(root, encoding='utf-8', xml_declaration=True)
    with open(V12, 'wb') as f:
        f.write(b'\xef\xbb\xbf' + data)
    print('backup:', bak)
    print('escrito:', V12)
    print('OK PATCH v03.1 aplicado')


if __name__ == '__main__':
    main()
