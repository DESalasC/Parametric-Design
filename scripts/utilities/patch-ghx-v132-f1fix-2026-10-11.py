# -*- coding: utf-8 -*-
"""Parchea F1_CONTEXTO_v13.2.ghx: fix F1 "Huella invalida" (2026-10-11 21:1x).

Re-embebe en el canvas:
  - #116-F3_DISTRIBUCION_v03.py  <- src v03.6.1 (huella_xy CERRADA)
  - #114-F3_VOLUM_GENERADOR_v08.py <- src v08.0.1 (cierre defensivo en
    bloque "Implantacion dinamica")

Uso:
  .venv\\Scripts\\python.exe scripts\\utilities\\patch-ghx-v132-f1fix-2026-10-11.py [ruta.ghx]
  (sin argumento: gh-definitions/F1_CONTEXTO_v13.2.ghx; probado sobre copia)

Validaciones: XML re-parseable; cambios aplicados (markers); entradas intactas;
CodeInput distintos a los previos. Backup .bak-<ts>. Escritura UTF-8 con BOM.
"""
import io
import os
import shutil
import sys
import time
import xml.etree.ElementTree as ET

BASE = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
GHX_DEF = os.path.join(BASE, "gh-definitions", "F1_CONTEXTO_v13.2.ghx")

TARGETS = [
    {
        "guid": "6eaf2956-f649-4540-a900-4b32a10deee4",
        "desc": "#116-F3_DISTRIBUCION_v03.py",
        "src": os.path.join(BASE, "src", "fase-3-masa", "F3_DISTRIBUCION_v03.py"),
        "markers": ["_pts_r", "cierre explicito"],
    },
    {
        "guid": "8c7e8133-0bbe-401d-9fa0-6c4b761bbc5d",
        "desc": "#114-F3_VOLUM_GENERADOR_v08.py",
        "src": os.path.join(BASE, "src", "fase-3-masa", "F3_VOLUM_GENERADOR_v08.py"),
        "markers": ["cierre defensivo"],
    },
]
# (markers: _pts_r + comentario de cierre en F3_DISTRIBUCION; cierre defensivo en VOLUM)


def items_multi(chunk):
    d = {}
    for w in chunk:
        if w.tag == 'items':
            for i in w:
                if i.tag == 'item':
                    d.setdefault(i.get('name'), []).append(i)
    return d


def find_obj(root, guid):
    for o in root.iter('chunk'):
        if o.get('name') != 'Object':
            continue
        for c in o.iter('chunk'):
            if c.get('name') == 'Container':
                d = items_multi(c)
                g = (d.get('InstanceGuid') or [None])[0]
                if g is not None and g.text and g.text.strip() == guid:
                    return o
    return None


def count_params(obj):
    ins = outs = 0
    for c in obj.iter('chunk'):
        if c.get('name') == 'InputParam':
            ins += 1
        elif c.get('name') == 'OutputParam':
            outs += 1
    return ins, outs


def main():
    ghx = os.path.normpath(sys.argv[1]) if len(sys.argv) > 1 else GHX_DEF
    print('ghx:', ghx)
    parser = ET.XMLParser(target=ET.TreeBuilder(insert_comments=True))
    tree = ET.parse(ghx, parser=parser)
    root = tree.getroot()

    previos = {}
    for t in TARGETS:
        obj = find_obj(root, t['guid'])
        if obj is None:
            print('ERROR: no encontrado', t['desc'])
            sys.exit(1)
        ci = None
        for i in obj.iter('item'):
            if i.get('name') == 'CodeInput':
                ci = i
                break
        if ci is None:
            print('ERROR: sin CodeInput en', t['desc'])
            sys.exit(1)
        code = io.open(t['src'], 'r', encoding='utf-8-sig').read().replace('\r\n', '\n')
        previos[t['guid']] = {
            'ins_outs': count_params(obj),
            'old_len': len(ci.text or ''),
            'old_text': ci.text or '',
        }
        ci.text = code
        print('{}: CodeInput {} -> {} chars'.format(t['desc'], previos[t['guid']]['old_len'], len(code)))

    txt = ET.tostring(root, encoding='unicode')
    ok = True
    try:
        ET.fromstring(txt)
        xml_ok = True
    except Exception:
        xml_ok = False
    checks = [('XML re-parseable', xml_ok)]
    for t in TARGETS:
        obj = find_obj(root, t['guid'])
        code = ''
        for i in obj.iter('item'):
            if i.get('name') == 'CodeInput':
                code = i.text or ''
        checks.append((t['desc'] + ': cambiado', code != previos[t['guid']]['old_text']))
        for mk in t['markers']:
            checks.append((t['desc'] + ': marker ' + mk, mk in code))
        checks.append((t['desc'] + ': entradas/salidas intactas',
                       count_params(obj) == previos[t['guid']]['ins_outs']))
    for nm, okc in checks:
        print('  [{}] {}'.format('OK' if okc else 'FAIL', nm))
        ok = ok and okc
    if not ok:
        print('VALIDACION FALLIDA - no se escribe')
        sys.exit(1)

    ts = time.strftime('%Y%m%d-%H%M%S')
    bak = ghx + '.bak-' + ts
    shutil.copy2(ghx, bak)
    data = ET.tostring(root, encoding='utf-8', xml_declaration=True)
    with open(ghx, 'wb') as f:
        f.write(b'\xef\xbb\xbf' + data)
    print('backup :', bak)
    print('escrito:', ghx)
    print('OK PATCH F1-fix Huella aplicado (#116 v03.6.1 + #114 v08.0.1)')
    print('Siguiente: regenerar .gh ->  pwsh -NoProfile -File scripts/utilities/ghx-to-gh.ps1 -InputGhx "{}"'.format(ghx))


if __name__ == '__main__':
    main()
