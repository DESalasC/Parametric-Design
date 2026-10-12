# -*- coding: utf-8 -*-
"""Parchea F1_CONTEXTO_v13.2.ghx: re-embebe **F3_DISTRIBUCION v03.7** en #116.

v03.7 (ajustes del operador 2026-10-11 noche):
  (a) anclaje a frentes (frente/fondo) + separaciones ajustadas uniformes;
  (b) pisos por bloque (`pisos_por_bloque` / `limites_pisos_json`).

Uso:
  .venv\\Scripts\\python.exe scripts\\utilities\\patch-ghx-v132-f3dist-v037-2026-10-11.py [ruta.ghx]
  (sin argumento: gh-definitions/F1_CONTEXTO_v13.2.ghx; probado sobre copia)

Validaciones: XML re-parseable; code v03.7; entradas/salidas intactas; backup.
"""
import io
import os
import shutil
import sys
import time
import xml.etree.ElementTree as ET

BASE = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
GHX_DEF = os.path.join(BASE, "gh-definitions", "F1_CONTEXTO_v13.2.ghx")
SRC = os.path.join(BASE, "src", "fase-3-masa", "F3_DISTRIBUCION_v03.py")
COMPONENT_GUID = "6eaf2956-f649-4540-a900-4b32a10deee4"  # #116


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
    code = io.open(SRC, 'r', encoding='utf-8-sig').read().replace('\r\n', '\n')

    parser = ET.XMLParser(target=ET.TreeBuilder(insert_comments=True))
    tree = ET.parse(ghx, parser=parser)
    root = tree.getroot()

    obj = find_obj(root, COMPONENT_GUID)
    if obj is None:
        print('ERROR: no encontrado #116-F3_DISTRIBUCION_v03.py')
        sys.exit(1)
    ins0, outs0 = count_params(obj)
    ci = None
    for i in obj.iter('item'):
        if i.get('name') == 'CodeInput':
            ci = i
            break
    if ci is None:
        print('ERROR: sin CodeInput')
        sys.exit(1)
    old = ci.text or ''
    ci.text = code
    print('#116: CodeInput {} -> {} chars'.format(len(old), len(code)))

    txt = ET.tostring(root, encoding='unicode')
    ok = True
    try:
        ET.fromstring(txt)
        xml_ok = True
    except Exception:
        xml_ok = False
    obj2 = find_obj(root, COMPONENT_GUID)
    code2 = ''
    for i in obj2.iter('item'):
        if i.get('name') == 'CodeInput':
            code2 = i.text or ''
    checks = [
        ('XML re-parseable', xml_ok),
        ('code cambiado', code2 != old),
        ('code v03.7', 'v03.7' in code2),
        ('code pisos_por_bloque', 'pisos_por_bloque' in code2),
        ('code anclaje_frentes', 'anclaje_frentes' in code2),
        ('entradas/salidas intactas', (ins0, outs0) == count_params(obj2)),
    ]
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
    print('OK PATCH F3_DISTRIBUCION v03.7 aplicado')
    print('Siguiente: regenerar .gh ->  pwsh -NoProfile -File scripts/utilities/ghx-to-gh.ps1 -InputGhx "{}"'.format(ghx))


if __name__ == '__main__':
    main()
