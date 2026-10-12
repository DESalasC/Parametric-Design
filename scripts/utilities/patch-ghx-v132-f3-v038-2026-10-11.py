# -*- coding: utf-8 -*-
"""Parchea F1_CONTEXTO_v13.2.ghx: v03.8 (escalonamiento lateral 1/5) + v08.0.2.

  #116-F3_DISTRIBUCION: CodeInput <- src v03.8; AGREGA entrada
     `sep_lateral_json`; nick v03.7 -> v03.8.
  #114-F3_VOLUM_GENERADOR: CodeInput <- src v08.0.2 (usa huella_xy_por_piso);
     nick v08.0 -> v08.0.2 (si aplica).

Uso:
  .venv\\Scripts\\python.exe scripts\\utilities\\patch-ghx-v132-f3-v038-2026-10-11.py [ruta.ghx]
"""
import io
import os
import shutil
import sys
import time
import uuid
import xml.etree.ElementTree as ET

BASE = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
GHX_DEF = os.path.join(BASE, "gh-definitions", "F1_CONTEXTO_v13.2.ghx")
INPUT_ID_BASE = "84fa917c-1ed8-4db3-8be1-7bdc4a6495a2"
TYPE_HINT_ID = "37261734-eec7-4f50-b6a8-b8d1f3c4396b"

TARGETS = [
    {
        "guid": "6eaf2956-f649-4540-a900-4b32a10deee4",
        "desc": "#200-F3_DISTRIBUCION_v03.py",
        "src": os.path.join(BASE, "src", "fase-3-masa", "F3_DISTRIBUCION_v03.py"),
        "add_inputs": [("sep_lateral_json",
                        "Escalonamiento lateral (1/5 sobre empate). Ej: {\"lado\":\"xmax\",\"h_vecino_m\":6.0}; v03.8 - F1")],
        "nick_replaces": [("v03.7", "v03.8")],
        "markers": ["v03.8", "sep_lateral_json", "huella_xy_por_piso"],
        "absent": ["F3 v03.7"],
    },
    {
        "guid": "8c7e8133-0bbe-401d-9fa0-6c4b761bbc5d",
        "desc": "#F3_VOLUM_GENERADOR_v08.py",
        "src": os.path.join(BASE, "src", "fase-3-masa", "F3_VOLUM_GENERADOR_v08.py"),
        "add_inputs": [],
        "nick_replaces": [("v08.0", "v08.0.2")],
        "markers": ["huella_xy_por_piso"],
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


def last_input(pd):
    best = (-1, None)
    for c in pd.iter('chunk'):
        if c.get('name') != 'InputParam':
            continue
        idx = int(c.get('index', '0'))
        y = None
        for ch in c.iter('chunk'):
            if ch.get('name') == 'Attributes':
                for w in ch:
                    if w.tag == 'items':
                        for i in w:
                            if i.tag == 'item' and i.get('name') == 'Bounds':
                                for e in i:
                                    if e.tag == 'Y':
                                        y = float(e.text)
        if idx >= best[0]:
            best = (idx, y)
    return best


def make_input_chunk(index, name, desc, y):
    ch = ET.Element('chunk')
    ch.set('name', 'InputParam')
    ch.set('index', str(index))
    items = ET.SubElement(ch, 'items')
    items.set('count', '10')

    def it(n, tn, tc, txt=None):
        e = ET.Element('item')
        e.set('name', n)
        e.set('type_name', tn)
        e.set('type_code', tc)
        if txt is not None:
            e.text = txt
        return e

    items.append(it('AllowTreeAccess', 'gh_bool', '1', 'true'))
    items.append(it('Description', 'gh_string', '10', desc))
    items.append(it('InstanceGuid', 'gh_guid', '9', str(uuid.uuid4())))
    items.append(it('Name', 'gh_string', '10', name))
    items.append(it('NickName', 'gh_string', '10', name))
    items.append(it('Optional', 'gh_bool', '1', 'true'))
    items.append(it('ScriptParamAccess', 'gh_int32', '3', '0'))
    items.append(it('ShowTypeHints', 'gh_bool', '1', 'true'))
    items.append(it('SourceCount', 'gh_int32', '3', '0'))
    items.append(it('TypeHintID', 'gh_guid', '9', TYPE_HINT_ID))
    chunks = ET.SubElement(ch, 'chunks')
    chunks.set('count', '1')
    attr = ET.SubElement(chunks, 'chunk')
    attr.set('name', 'Attributes')
    ai = ET.SubElement(attr, 'items')
    ai.set('count', '2')
    b = ET.SubElement(ai, 'item')
    b.set('name', 'Bounds')
    b.set('type_name', 'gh_drawing_rectanglef')
    b.set('type_code', '35')
    for tag, val in (('X', '10102'), ('Y', str(y)), ('W', '142'), ('H', '20')):
        e = ET.SubElement(b, tag)
        e.text = val
    p = ET.SubElement(ai, 'item')
    p.set('name', 'Pivot')
    p.set('type_name', 'gh_drawing_pointf')
    p.set('type_code', '31')
    for tag, val in (('X', '10174.5'), ('Y', str(y + 10))):
        e = ET.SubElement(p, tag)
        e.text = val
    return ch


def main():
    ghx = os.path.normpath(sys.argv[1]) if len(sys.argv) > 1 else GHX_DEF
    print('ghx:', ghx)
    parser = ET.XMLParser(target=ET.TreeBuilder(insert_comments=True))
    tree = ET.parse(ghx, parser=parser)
    root = tree.getroot()
    nobj0 = sum(1 for o in root.iter('chunk') if o.get('name') == 'Object')

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
        # inputs nuevos
        pd = None
        for c in obj.iter('chunk'):
            if c.get('name') == 'ParameterData':
                pd = c
                break
        nuevas = 0
        if t['add_inputs']:
            idx_last, y_last = last_input(pd)
            if y_last is None:
                y_last = 7410.0
            ch_container = None
            for w in pd:
                if w.tag == 'chunks':
                    ch_container = w
                    break
            for k, (nombre, desc) in enumerate(t['add_inputs']):
                if nombre in ins:
                    print('  aviso: {} ya existe'.format(nombre))
                    continue
                ch_container.append(make_input_chunk(idx_last + 1 + nuevas, nombre, desc,
                                                     y_last + 20.0 * (nuevas + 1)))
                nuevas += 1
            items_pd = None
            for w in pd:
                if w.tag == 'items':
                    items_pd = w
                    break
            for w in items_pd:
                if w.tag == 'item' and w.get('name') == 'InputCount':
                    w.text = str(int(w.text) + nuevas)
            for k in range(nuevas):
                e = ET.Element('item')
                e.set('name', 'InputId')
                e.set('index', str(idx_last + 1 + k))
                e.set('type_name', 'gh_guid')
                e.set('type_code', '9')
                e.text = INPUT_ID_BASE
                items_pd.append(e)
            print('  entradas agregadas:', nuevas)

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
    print('OK PATCH v03.8 + v08.0.2 aplicado (escalonamiento lateral 1/5)')
    print('Siguiente: regenerar .gh ->  pwsh -NoProfile -File scripts/utilities/ghx-to-gh.ps1 -InputGhx "{}"'.format(ghx))


if __name__ == '__main__':
    main()
