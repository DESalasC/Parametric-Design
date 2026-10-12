# -*- coding: utf-8 -*-
"""Parchea F1_CONTEXTO_v13.5.ghx — "parche cotas" + zonas BEP + stories v08.1.

  #198-F3_VOLUM_GENERADOR_v08.py -> v08.1 (CodeInput <- src; nick v08 -> v08.1):
     (a) mensaje "Implantacion" con las cotas de arranque reales ("cotas B1..Bn")
         + resumen del plan de stories;
     (b) zonas con nomenclatura BEP: Number = GF-Z1-COM-001 / Name descriptivo;
     (c) export de stories por flag (data/fase-3-masa/stories-export-flag.json
         -> casos/<chip>/cotas-arranque.json + niveles_deseados.json).
  #200-F3_DISTRIBUCION_v03.8.py: resincroniza CodeInput <- src (cabecera
     "genérica v03" + últimas 3 subversiones; el cuerpo ya era 1:1).

Uso:
  .venv\\Scripts\\python.exe scripts\\utilities\\patch-ghx-v135-cotas-stories-2026-10-12.py [ruta.ghx]
"""
import io
import os
import shutil
import sys
import time
import uuid
import xml.etree.ElementTree as ET

BASE = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
GHX_DEF = os.path.join(BASE, "gh-definitions", "F1_CONTEXTO_v13.5.ghx")
INPUT_ID_BASE = "84fa917c-1ed8-4db3-8be1-7bdc4a6495a2"
TYPE_HINT_ID = "37261734-eec7-4f50-b6a8-b8d1f3c4396b"

TARGETS = [
    {
        "guid": "8c7e8133-0bbe-401d-9fa0-6c4b761bbc5d",
        "desc": "#198-F3_VOLUM_GENERADOR_v08.py",
        "src": os.path.join(BASE, "src", "fase-3-masa", "F3_VOLUM_GENERADOR_v08.py"),
        "add_inputs": [],
        "nick_replaces": [("F3_VOLUM_GENERADOR_v08.0.2.py", "F3_VOLUM_GENERADOR_v08.1.py"),
                          ("F3_VOLUM_GENERADOR_v08.py", "F3_VOLUM_GENERADOR_v08.1.py")],
        "markers": ["v08.1", "CATEGORIAS_BEP", "def _plan_stories",
                    "cotas B1..B{}", "stories-export-flag.json",
                    "niveles_deseados.json"],
        "absent": ['-P"+str(fi+1)'],
    },
    {
        "guid": "6eaf2956-f649-4540-a900-4b32a10deee4",
        "desc": "#200-F3_DISTRIBUCION_v03.8.py",
        "src": os.path.join(BASE, "src", "fase-3-masa", "F3_DISTRIBUCION_v03.py"),
        "add_inputs": [],
        "nick_replaces": [],
        "markers": ["v03.8 (genérica v03)", "sep_lateral_json"],
        "absent": [],
    },
]


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


def param_name(c):
    for w in c:
        if w.tag == 'items':
            for i in w:
                if i.tag == 'item' and i.get('name') == 'Name':
                    return (i.text or '').strip()
    return ''


def main():
    ghx = os.path.normpath(sys.argv[1]) if len(sys.argv) > 1 else GHX_DEF
    print('ghx:', ghx)
    parser = ET.XMLParser(target=ET.TreeBuilder(insert_comments=True))
    tree = ET.parse(ghx, parser=parser)
    root = tree.getroot()
    nobj0 = sum(1 for o in root.iter('chunk') if o.get('name') == 'Object')
    print('objetos:', nobj0)

    old_codes = {}
    ins_outs0 = {}
    for t in TARGETS:
        obj = find_obj(root, t['guid'])
        if obj is None:
            print('ERROR: no encontrado', t['desc'])
            sys.exit(1)
        ins = [param_name(c) for c in obj.iter('chunk') if c.get('name') == 'InputParam']
        outs = [param_name(c) for c in obj.iter('chunk') if c.get('name') == 'OutputParam']
        ins_outs0[t['guid']] = (ins, outs)
        # nick
        for c in obj.iter('chunk'):
            if c.get('name') == 'Container':
                for w in c:
                    if w.tag == 'items':
                        for i in w:
                            if i.tag == 'item' and i.get('name') == 'NickName' and i.text:
                                for a, b in t['nick_replaces']:
                                    if a in i.text:
                                        i.text = i.text.replace(a, b)
        # code
        code = io.open(t['src'], 'r', encoding='utf-8-sig').read().replace('\r\n', '\n')
        ci = None
        for i in obj.iter('item'):
            if i.get('name') == 'CodeInput':
                ci = i
                break
        old_codes[t['guid']] = ci.text or ''
        ci.text = code
        print('{}: code {} -> {} chars'.format(t['desc'], len(old_codes[t['guid']]), len(code)))

    for w in root.iter():
        if w.tag == 'items':
            w.set('count', str(len([c for c in w if c.tag == 'item'])))
        elif w.tag == 'chunks':
            w.set('count', str(len([c for c in w if c.tag == 'chunk'])))

    txt = ET.tostring(root, encoding='unicode')
    ok = True
    try:
        ET.fromstring(txt)
        xml_ok = True
    except Exception:
        xml_ok = False
    checks = [('XML re-parseable', xml_ok)]
    for t in TARGETS:
        obj2 = find_obj(root, t['guid'])
        code2 = ''
        for i in obj2.iter('item'):
            if i.get('name') == 'CodeInput':
                code2 = i.text or ''
        checks.append((t['desc'] + ': cambiado', code2 != old_codes[t['guid']]))
        for mk in t['markers']:
            checks.append((t['desc'] + ': marker ' + mk, mk in code2))
        for mk in t['absent']:
            checks.append((t['desc'] + ': ausente ' + mk, mk not in code2))
        ins1 = [param_name(c) for c in obj2.iter('chunk') if c.get('name') == 'InputParam']
        outs1 = [param_name(c) for c in obj2.iter('chunk') if c.get('name') == 'OutputParam']
        ins0, outs0 = ins_outs0[t['guid']]
        checks.append((t['desc'] + ': entradas previas conservadas', set(ins0) <= set(ins1)))
        checks.append((t['desc'] + ': nuevas entradas', all(n in ins1 for n, _d in t['add_inputs'])))
        checks.append((t['desc'] + ': salidas intactas', outs1 == outs0))
    nobj1 = sum(1 for o in root.iter('chunk') if o.get('name') == 'Object')
    checks.append(('objetos preservados', nobj0 == nobj1))
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
    print('OK PATCH v08.1 (cotas + zonas BEP + stories export) + F3D header aplicado')
    print('Siguiente: regenerar .gh ->  pwsh -NoProfile -File scripts/utilities/ghx-to-gh.ps1 -InputGhx "{}"'.format(ghx))


if __name__ == '__main__':
    main()
