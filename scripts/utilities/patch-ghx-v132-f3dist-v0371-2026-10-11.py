# -*- coding: utf-8 -*-
"""Parchea F1_CONTEXTO_v13.2.ghx: v03.7.1 sobre #116-F3_DISTRIBUCION_v03.

  (a) Re-embebe el CodeInput con src v03.7 corregido (mensajes "F3 v03.7 |").
  (b) AGREGA dos entradas opcionales al componente:
        `pisos_por_bloque`  y  `limites_pisos_json`
      (para no tener que agregarlas a mano en el canvas).
  (c) Actualiza el NickName del componente (v03.6 -> v03.7) si aplica.

Uso:
  .venv\\Scripts\\python.exe scripts\\utilities\\patch-ghx-v132-f3dist-v0371-2026-10-11.py [ruta.ghx]
  (sin argumento: gh-definitions/F1_CONTEXTO_v13.2.ghx; probado sobre copia)
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
SRC = os.path.join(BASE, "src", "fase-3-masa", "F3_DISTRIBUCION_v03.py")
COMPONENT_GUID = "6eaf2956-f649-4540-a900-4b32a10deee4"  # #116 (F3_DISTRIBUCION)
INPUT_ID_BASE = "84fa917c-1ed8-4db3-8be1-7bdc4a6495a2"
TYPE_HINT_ID = "37261734-eec7-4f50-b6a8-b8d1f3c4396b"

NUEVAS_ENTRADAS = [
    ("pisos_por_bloque", "Pisos por bloque (ej. '4,4,6'); v03.7 - F1"),
    ("limites_pisos_json", "Bandas desde el frente + redistribucion al ultimo bloque; v03.7 - F1"),
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


def get_param_names(obj, kind):
    names = []
    for c in obj.iter('chunk'):
        if c.get('name') == kind:
            d = items_multi(c)
            names.append((d.get('Name') or [''])[0].text if False else (d.get('Name') or [None])[0])
    return names


def param_name(c):
    for w in c:
        if w.tag == 'items':
            for i in w:
                if i.tag == 'item' and i.get('name') == 'Name':
                    return (i.text or '').strip()
    return ''


def last_input_y(pd):
    best = None
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
        if best is None or idx >= best[0]:
            best = (idx, y)
    return best  # (idx, y)


def make_input_chunk(index, name, desc, y):
    ch = ET.Element('chunk')
    ch.set('name', 'InputParam')
    ch.set('index', str(index))
    items = ET.SubElement(ch, 'items')
    items.set('count', '10')

    def it(n, tn, tc, txt=None, idx=None):
        e = ET.Element('item')
        e.set('name', n)
        if idx is not None:
            e.set('index', str(idx))
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
    code = io.open(SRC, 'r', encoding='utf-8-sig').read().replace('\r\n', '\n')

    parser = ET.XMLParser(target=ET.TreeBuilder(insert_comments=True))
    tree = ET.parse(ghx, parser=parser)
    root = tree.getroot()
    nobj0 = sum(1 for o in root.iter('chunk') if o.get('name') == 'Object')

    obj = find_obj(root, COMPONENT_GUID)
    if obj is None:
        print('ERROR: no encontrado #116-F3_DISTRIBUCION_v03.py')
        sys.exit(1)

    # nick
    nick_el = None
    for c in obj.iter('chunk'):
        if c.get('name') == 'Container':
            for w in c:
                if w.tag == 'items':
                    for i in w:
                        if i.tag == 'item' and i.get('name') == 'NickName':
                            nick_el = i
    print('nick previo:', (nick_el.text if nick_el is not None else None))
    if nick_el is not None and nick_el.text and 'v03.6' in nick_el.text:
        nick_el.text = nick_el.text.replace('v03.6', 'v03.7')

    # inputs actuales
    ins0 = [param_name(c) for c in obj.iter('chunk') if c.get('name') == 'InputParam']
    outs0 = [param_name(c) for c in obj.iter('chunk') if c.get('name') == 'OutputParam']
    print('inputs previos ({}): {}'.format(len(ins0), ins0))

    # CodeInput
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
    print('CodeInput: {} -> {} chars'.format(len(old), len(code)))

    # --- agregar entradas nuevas ---
    pd = None
    for c in obj.iter('chunk'):
        if c.get('name') == 'ParameterData':
            pd = c
            break
    if pd is None:
        print('ERROR: sin ParameterData')
        sys.exit(1)
    idx_last, y_last = last_input_y(pd)
    if y_last is None:
        y_last = 7410.0
    ch_container = None
    for w in pd:
        if w.tag == 'chunks':
            ch_container = w
            break
    nuevas = 0
    for k, (nombre, desc) in enumerate(NUEVAS_ENTRADAS):
        if nombre in ins0:
            print('  aviso: entrada {} ya existe (se omite)'.format(nombre))
            continue
        ch_container.append(make_input_chunk(idx_last + 1 + nuevas, nombre, desc,
                                             y_last + 20.0 * (nuevas + 1)))
        nuevas += 1
    print('entradas agregadas:', nuevas)

    # ParameterData: InputCount + InputId nuevos
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

    # conteos globales
    for w in root.iter():
        if w.tag == 'items':
            w.set('count', str(len([c for c in w if c.tag == 'item'])))
        elif w.tag == 'chunks':
            w.set('count', str(len([c for c in w if c.tag == 'chunk'])))

    # validaciones
    txt = ET.tostring(root, encoding='unicode')
    ok = True
    try:
        ET.fromstring(txt)
        xml_ok = True
    except Exception:
        xml_ok = False
    obj2 = find_obj(root, COMPONENT_GUID)
    ins1 = [param_name(c) for c in obj2.iter('chunk') if c.get('name') == 'InputParam']
    outs1 = [param_name(c) for c in obj2.iter('chunk') if c.get('name') == 'OutputParam']
    code2 = ''
    for i in obj2.iter('item'):
        if i.get('name') == 'CodeInput':
            code2 = i.text or ''
    nick2 = ''
    for c2 in obj2.iter('chunk'):
        if c2.get('name') == 'Container':
            for w in c2:
                if w.tag == 'items':
                    for i in w:
                        if i.tag == 'item' and i.get('name') == 'NickName':
                            nick2 = (i.text or '').strip()
    nobj1 = sum(1 for o in root.iter('chunk') if o.get('name') == 'Object')
    checks = [
        ('XML re-parseable', xml_ok),
        ('code con F3 v03.7', 'F3 v03.7' in code2),
        ('code sin F3 v03.6', 'F3 v03.6' not in code2),
        ('entradas 13 -> 15', len(ins1) == 15),
        ('nuevas entradas presentes', all(n in ins1 for n, _d in NUEVAS_ENTRADAS)),
        ('entradas previas conservadas', set(ins0) <= set(ins1)),
        ('salidas intactas (8)', len(outs1) == len(outs0) == 8),
        ('nick v03.7', 'v03.7' in nick2),
        ('objetos preservados', nobj0 == nobj1),
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
    print('OK PATCH v03.7.1 aplicado (mensajes v03.7 + 2 entradas nuevas + nick)')
    print('Siguiente: regenerar .gh ->  pwsh -NoProfile -File scripts/utilities/ghx-to-gh.ps1 -InputGhx "{}"'.format(ghx))


if __name__ == '__main__':
    main()
