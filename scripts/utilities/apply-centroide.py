# -*- coding: utf-8 -*-
"""Apply zona centroide patch to F1_CONTEXTO_v13.2.ghx."""
import hashlib
import io
import os
import shutil
import sys
import uuid
import xml.etree.ElementTree as ET
from datetime import datetime

BASE = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
GHX_DEFAULT = os.path.join(BASE, "gh-definitions", "F1_CONTEXTO_v13.2.ghx")

COMPONENT_GUID = "8c7e8133-0bbe-401d-9fa0-6c4b761bbc5d"
OUTPUT_ID_BASE = "8ec86459-bf01-4409-baee-174d0d2b13d0"

NUEVA_SALIDA = (
    "zonas_centroides",
    "Centroide (Point3d) de cada zona - para Stamp Position del componente Zone - v08.0",
)


def items_dict(chunk):
    d = {}
    for w in chunk:
        if w.tag == 'items':
            for i in w:
                if i.tag == 'item':
                    d[i.get('name')] = (i.text or '').strip()
    return d


def find_item(chunk, name):
    for i in chunk.iter('item'):
        if i.get('name') == name:
            return i
    return None


def find_object(root, guid):
    for o in root.iter('chunk'):
        if o.get('name') != 'Object':
            continue
        for c in o.iter('chunk'):
            if c.get('name') == 'Container':
                if items_dict(c).get('InstanceGuid', '') == guid:
                    return o
    return None


def make_item(name, type_name, type_code, text=None, index=None):
    i = ET.Element('item')
    i.set('name', name)
    if index is not None:
        i.set('index', str(index))
    i.set('type_name', type_name)
    i.set('type_code', str(type_code))
    if text is not None:
        i.text = text
    return i


def nuevo_output_chunk(index, name, desc, y):
    ch = ET.Element('chunk')
    ch.set('name', 'OutputParam')
    ch.set('index', str(index))
    items = ET.SubElement(ch, 'items')
    items.set('count', '6')
    items.append(make_item('Description', 'gh_string', 10, desc))
    items.append(make_item('InstanceGuid', 'gh_guid', 9, str(uuid.uuid4())))
    items.append(make_item('Name', 'gh_string', 10, name))
    items.append(make_item('NickName', 'gh_string', 10, name))
    items.append(make_item('Optional', 'gh_bool', 1, 'false'))
    items.append(make_item('SourceCount', 'gh_int32', 3, '0'))
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
    for tag, val in (('X', '2653'), ('Y', str(y)), ('W', '119'), ('H', '20')):
        e = ET.SubElement(b, tag)
        e.text = val
    p = ET.SubElement(ai, 'item')
    p.set('name', 'Pivot')
    p.set('type_name', 'gh_drawing_pointf')
    p.set('type_code', '31')
    for tag, val in (('X', '2712.5'), ('Y', str(y + 10))):
        e = ET.SubElement(p, tag)
        e.text = val
    return ch


def main():
    ghx = os.path.normpath(sys.argv[1]) if len(sys.argv) > 1 else GHX_DEFAULT
    print('ghx:', ghx)
    # Read raw text for CodeInput extraction later
    raw_text = io.open(ghx, 'r', encoding='utf-8-sig', errors='ignore').read()
    parser = ET.XMLParser(target=ET.TreeBuilder(insert_comments=True))
    tree = ET.parse(ghx, parser=parser)
    root = tree.getroot()

    obj = find_object(root, COMPONENT_GUID)
    if obj is None:
        print('ERROR: no se encontro #75-F3_VOLUM_GENERADOR_v08 ({}).'.format(COMPONENT_GUID))
        sys.exit(1)

    # estado previo
    pd = None
    for c in obj.iter('chunk'):
        if c.get('name') == 'ParameterData':
            pd = c
            break
    if pd is None:
        print('ERROR: sin ParameterData en el componente.')
        sys.exit(1)

    ci = find_item(obj, 'CodeInput')
    if ci is None:
        print('ERROR: no se encontro CodeInput en el objeto.')
        sys.exit(1)
    code_txt_prev = ci.text or ''
    code_sha_prev = hashlib.sha1(code_txt_prev.encode('utf-8')).hexdigest()
    print('CodeInput: {} chars | sha1 {}'.format(len(code_txt_prev), code_sha_prev))

    # ---------- 1. Parchear el CodeInput ----------
    lines = code_txt_prev.splitlines()
    # Find where zonas_alturas is initialized (inside if salida_zona: block)
    init_idx = -1
    for i, ln in enumerate(lines):
        if ln.strip().startswith('zonas_alturas = []') and 'List[float]' in ln:
            init_idx = i
            break
    if init_idx == -1:
        print('ERROR: no se encontro la inicialización de zonas_alturas.')
        sys.exit(1)
    # Determine indent of that line
    line_init = lines[init_idx]
    indent = ''
    for ch in line_init:
        if ch == ' ':
            indent += ' '
        else:
            break
    # Insert initialization for zonas_centroides right after
    new_line = indent + 'zonas_centroides = []         # List[Point3d] - centroid of each zone (for Stamp Position)'
    lines.insert(init_idx + 1, new_line)
    init_idx += 1  # account for inserted line

    # Find where we append to zonas_atributos
    zona_append_idx = -1
    for i, ln in enumerate(lines):
        if ln.strip().startswith('zonas_atributos.append') and 'py_json.dumps' in ln:
            zona_append_idx = i
            break
    if zona_append_idx == -1:
        print('ERROR: no se encontro la linea donde se appende a zonas_atributos.')
        sys.exit(1)
    # Determine indent of that line
    line_zone = lines[zona_append_idx]
    indent_zone = ''
    for ch in line_zone:
        if ch == ' ':
            indent_zone += ' '
        else:
            break
    # Block to insert after the append line
    block_lines = [
        indent_zone + '# Calcular centroide de la zona (para Stamp Position)',
        indent_zone + 'zona_centroide = None',
        indent_zone + 'try:',
        indent_zone + '    ap_zona = rg.AreaMassProperties.Compute(curva_zona)',
        indent_zone + '    if ap_zona is not None:',
        indent_zone + '        zona_centroide = ap_zona.Centroid',
        indent_zone + 'except Exception:',
        indent_zone + '    zona_centroide = None',
        indent_zone + 'if zona_centroide is None:',
        indent_zone + '    zona_centroide = rg.Point3d(0,0,0)',
        indent_zone + 'zonas_centroides.append(zona_centroide)',
    ]
    # Insert in reverse order so line numbers stay correct
    for bl in reversed(block_lines):
        lines.insert(zona_append_idx + 1, bl)
        zona_append_idx += 1

    code_txt_new = '\n'.join(lines)
    code_sha_new = hashlib.sha1(code_txt_new.encode('utf-8')).hexdigest()
    print('CodeInput parcheado: {} chars | sha1 {}'.format(len(code_txt_new), code_sha_new))

    # ---------- 2. Agregar la nueva salida al ParameterData ----------
    # We'll just add it; assume it's not present (we can check but for simplicity we add)
    chunks_pd = None
    for w in pd:
        if w.tag == 'chunks':
            chunks_pd = w
            break
    if chunks_pd is None:
        print('ERROR: ParameterData sin chunks.')
        sys.exit(1)

    idx_base = len([c for c in chunks_pd if c.tag == 'chunk' and c.get('name') == 'OutputParam'])
    y = 6438 + 20  # after 'mensaje' (Y=6438, H=20)
    ch = nuevo_output_chunk(idx_base, NUEVA_SALIDA[0], NUEVA_SALIDA[1], y)
    chunks_pd.append(ch)
    print('insertada salida nueva en indice {}'.format(idx_base))

    # Update OutputCount and add OutputId
    oc = find_item(pd, 'OutputCount')
    if oc is None:
        print('ERROR: sin OutputCount.')
        sys.exit(1)
    oc.text = str(int(oc.text) + 1)
    items_pd = None
    for w in pd:
        if w.tag == 'items':
            items_pd = w
            break
    it = make_item('OutputId', 'gh_guid', 9, OUTPUT_ID_BASE, index=idx_base)
    items_pd.append(it)

    # ---------- 3. Conteos globales ----------
    for w in root.iter():
        if w.tag == 'items':
            w.set('count', str(len([c for c in w if c.tag == 'item'])))
        elif w.tag == 'chunks':
            w.set('count', str(len([c for c in w if c.tag == 'chunk'])))

    # ---------- 4. Escritura con backup ----------
    ts = datetime.now().strftime('%Y%m%d-%H%M%S')
    bak = ghx + '.bak-' + ts
    shutil.copy2(ghx, bak)
    data = ET.tostring(root, encoding='utf-8', xml_declaration=True)
    with open(ghx, 'wb') as f:
        f.write(b'\xef\xbb\xbf' + data)
    print('backup:', bak)
    print('escrito:', ghx)
    print('OK PATCH ZONAS v13.2 CENTROIDE aplicado (1 output nueva + CodeInput)')
    print('Siguiente: regenerar .gh ->  pwsh -NoProfile -File scripts/utilities/ghx-to-gh.ps1 -InputGhx "{}"'.format(ghx))


if __name__ == '__main__':
    main()
