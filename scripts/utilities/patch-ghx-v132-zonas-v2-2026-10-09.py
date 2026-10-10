# -*- coding: utf-8 -*-
"""Parchea F1_CONTEXTO_v13.2.ghx: expone las 5 salidas de ZONAS del #75
F3_VOLUM_GENERADOR_v08 (zonas_perimetros, zonas_pisos, zonas_atributos,
zonas_alturas, zonas_nombres).

Contexto (2026-10-09):
  - El canvas v13.2 embebe el codigo v08.0 COMPLETO (verificado: similitud
    1.000 vs src/fase-3-masa/F3_VOLUM_GENERADOR_v08.py) y el toggle
    #49-Boolean Toggle salida_zona esta en TRUE.
  - Pero el componente solo declara 14 salidas: los valores calculados en las
    listas de zonas NO se exponen -> el operador las ve vacias.
  - Este parche AGREGA los 5 OutputParam que faltan. NO toca el CodeInput
    salvo para rellenar la nueva lista zonas_nombres a partir de zonas_atributos.

Uso:
  .venv\\Scripts\\python.exe scripts\\utilities\\patch-ghx-v132-zonas-v2-2026-10-09.py [ruta.ghx]
  (sin argumento: gh-definitions/F1_CONTEXTO_v13.2.ghx; acepta una copia como
   destino para pruebas)

Validaciones: XML re-parseable; CodeInput con parche interno (sha1 nuevo
esperado); salidas 14->19; entradas y su cableado intactos; sin GUIDs
duplicados; conteos consistentes.
Backup .bak-<ts> antes de escribir. Escritura UTF-8 con BOM (misma tecnica
que los patch-ghx-*.py previos).
"""

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

# #75-F3_VOLUM_GENERADOR_v08.py (Container.InstanceGuid)
COMPONENT_GUID = "8c7e8133-0bbe-401d-9fa0-6c4b761bbc5d"
OUTPUT_ID_BASE = "8ec86459-bf01-4409-baee-174d0d2b13d0"

NUEVAS_SALIDAS = [
    ("zonas_perimetros", "Perimetro 2D por zona (por uso y piso) - v08.0"),
    ("zonas_pisos", "Piso de cada zona (paralelo 1:1) - v08.0"),
    ("zonas_atributos", "Atributos JSON de cada zona (uso, area, piso, alturas) - v08.0"),
    ("zonas_alturas", "Altura del centro de cada zona (acumulada desde Z=0) - v08.0"),
    ("zonas_nombres", "Nombre (uso) de cada zona extraido de zonas_atributos - v08.0"),
]


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


def check_outputs(obj):
    names = []
    for c in obj.iter('chunk'):
        if c.get('name') == 'OutputParam':
            names.append(items_dict(c).get('Name', ''))
    return names


def check_inputs(obj):
    out = []
    for c in obj.iter('chunk'):
        if c.get('name') != 'InputParam':
            continue
        d = items_dict(c)
        srcs = []
        for w in c:
            if w.tag == 'items':
                for i in w:
                    if i.tag == 'item' and i.get('name') == 'Source':
                        srcs.append(i.text)
        out.append((d.get('Name', ''), d.get('InstanceGuid', ''), srcs))
    return out


def count_sibling_dups(root):
    bad = 0
    for w in root.iter():
        if w.tag == 'chunks':
            seen = set()
            for c in w:
                if c.tag != 'chunk':
                    continue
                key = (c.get('name'), c.get('index'))
                if key in seen:
                    bad += 1
                seen.add(key)
    return bad


def main():
    ghx = os.path.normpath(sys.argv[1]) if len(sys.argv) > 1 else GHX_DEFAULT
    print('ghx:', ghx)
    parser = ET.XMLParser(target=ET.TreeBuilder(insert_comments=True))
    tree = ET.parse(ghx, parser=parser)
    root = tree.getroot()

    obj = find_object(root, COMPONENT_GUID)
    if obj is None:
        print('ERROR: no se encontro #75-F3_VOLUM_GENERADOR_v08 ({}).'.format(COMPONENT_GUID))
        sys.exit(1)

    # estado previo
    salidas_previas = check_outputs(obj)
    entradas_previas = check_inputs(obj)
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
    print('salidas previas: {}'.format(len(salidas_previas)))
    print('CodeInput: {} chars | sha1 {}'.format(len(code_txt_prev), code_sha_prev))

    ya = [n for n in salidas_previas if n in [x[0] for x in NUEVAS_SALIDAS]]
    if ya:
        print('AVISO: ya existen salidas {}'.format(ya))
    if len(salidas_previas) == 14 and not ya:
        pass
    elif set(salidas_previas) >= {x[0] for x in NUEVAS_SALIDAS}:
        print('Las 5 salidas ya existen. Nada que hacer.')
        sys.exit(0)

    # ---------- 1. Insertar las 5 salidas nuevas al final del ParameterData ----------
    chunks_pd = None
    for w in pd:
        if w.tag == 'chunks':
            chunks_pd = w
            break
    if chunks_pd is None:
        print('ERROR: ParameterData sin chunks.')
        sys.exit(1)

    idx_base = len([c for c in chunks_pd if c.tag == 'chunk' and c.get('name') == 'OutputParam'])
    y = 6438 + 20  # despues de 'mensaje' (Y=6438, H=20)
    nuevos = []
    for k, (nombre, desc) in enumerate(NUEVAS_SALIDAS):
        ch = nuevo_output_chunk(idx_base + k, nombre, desc, y + k * 20)
        chunks_pd.append(ch)
        nuevos.append(ch)
    print('insertadas {} salidas nuevas (indices {}..{}).'.format(
        len(nuevos), idx_base, idx_base + len(nuevos) - 1))

    # ---------- 2. Parchear el CodeInput para rellenar zonas_nombres ----------
    # Buscamos la zona donde se llenan las 4 listas de zonas (dentro del try de salida_zona)
    # y añadimos la lógica para extraer el campo "uso" de cada JSON en zonas_atributos.
    # Formato esperado de cada item en zonas_atributos: JSON con llave "uso".
    # Si falta, usamos cadena vacia.
    try:
        import json as _pyjson
    except Exception:
        _pyjson = None

    lines = code_txt_prev.splitlines()
    # Buscamos la linea que empieza con "zonas_atributos.append(py_json.dumps(...))"
    # para insertar justo después la extraccion del nombre.
    insert_idx = -1
    for i, ln in enumerate(lines):
        if ln.strip().startswith('zonas_atributos.append') and 'py_json.dumps' in ln:
            insert_idx = i + 1
            break
    if insert_idx == -1:
        # Como alternativa, buscamos el bloque de zona y añadimos al final de él
        for i in range(len(lines)-1, -1, -1):
            if lines[i].strip() == '# Incrementar altura acumulada para el siguiente piso':
                insert_idx = i + 1
                break
    if insert_idx == -1:
        print('ADVERTENCIA: no se encontro el punto de insercion esperado en CodeInput; se append al final del bloque zona.')
        # Ultimo recurso: colocar justo antes de la línea que incrementa altura_acumulada
        for i, ln in enumerate(lines):
            if ln.strip().startswith('altura_acumulada += h_piso'):
                insert_idx = i
                break
    if insert_idx == -1:
        print('ERROR: no se pudo determinar donde insertar la logica de zonas_nombres.')
        sys.exit(1)

    # Construimos las lineas a insertar (8 espacios de sangria como en el bloque)
    indent = '        '  # 8 espacios
    new_lines = [
        indent + '# Extraer nombre (uso) de cada zona para la salida zonas_nombres',
        indent + 'if _pyjson is not None:',
        indent + '    try:',
        indent + '        _obj = _pyjson.loads(atributos)',
        indent + '        _nombre = _obj.get(\"uso\", \"\") if isinstance(_obj, dict) else \"\"',
        indent + '    except Exception:',
        indent + '        _nombre = \"\"',
        indent + 'else:',
        indent + '    _nombre = \"\"',
        indent + 'zonas_nombres.append(_nombre)',
        '',
    ]
    # Insertamos
    for nl in new_lines:
        lines.insert(insert_idx, nl)
        insert_idx += 1

    code_txt_new = '\n'.join(lines)
    code_sha_new = hashlib.sha1(code_txt_new.encode('utf-8')).hexdigest()
    print('CodeInput parcheado: {} chars | sha1 {}'.format(len(code_txt_new), code_sha_new))

    # ---------- 3. ParameterData: OutputCount + OutputId nuevos ----------
    oc = find_item(pd, 'OutputCount')
    if oc is None:
        print('ERROR: sin OutputCount.')
        sys.exit(1)
    oc.text = str(int(oc.text) + len(nuevos))
    items_pd = None
    for w in pd:
        if w.tag == 'items':
            items_pd = w
            break
    for k in range(len(nuevos)):
        it = make_item('OutputId', 'gh_guid', 9, OUTPUT_ID_BASE, index=idx_base + k)
        items_pd.append(it)

    # ---------- 4. Conteos globales ----------
    for w in root.iter():
        if w.tag == 'items':
            w.set('count', str(len([c for c in w if c.tag == 'item'])))
        elif w.tag == 'chunks':
            w.set('count', str(len([c for c in w if c.tag == 'chunk'])))

    # ---------- 5. Validaciones ----------
    txt = ET.tostring(root, encoding='unicode')
    ok = True
    try:
        ET.fromstring(txt)
        xml_ok = True
    except Exception:
        xml_ok = False
    obj2 = find_object(root, COMPONENT_GUID)
    salidas2 = check_outputs(obj2)
    entradas2 = check_inputs(obj2)
    ci2 = find_item(obj2, 'CodeInput')
    code_txt_new2 = ci2.text or ''
    code_sha_new2 = hashlib.sha1(code_txt_new2.encode('utf-8')).hexdigest()

    seen = set()
    dups_guid = 0
    for i in root.iter('item'):
        if i.get('name') == 'InstanceGuid' and i.text:
            g = i.text.strip()
            if g in seen:
                dups_guid += 1
            seen.add(g)

    checks = [
        ('XML serializado re-parseable', xml_ok),
        ('CodeInput presente (>1000 chars)', len(code_txt_new2) > 1000),
        ('CodeInput parcheado correctamente (sha1 nuevo)', code_sha_new2 == code_sha_new),
        ('salidas 14 -> 19', len(salidas2) == 19),
        ('las 5 salidas nuevas presentes', all(n in salidas2 for n, _d in NUEVAS_SALIDAS)),
        ('nombres previos conservados', set(salidas_previas) <= set(salidas2)),
        ('entradas intactas', entradas2 == entradas_previas),
        ('sin duplicados de InstanceGuid', dups_guid == 0),
        ('sin duplicados de chunk hermano', count_sibling_dups(root) == 0),
        ('OutputParam total 161->170', sum(1 for c in root.iter('chunk') if c.get('name') == 'OutputParam') == 170),
    ]
    for nm, okc in checks:
        print('  [{}] {}'.format('OK' if okc else 'FAIL', nm))
        ok = ok and okc
    if not ok:
        print('VALIDACION FALLIDA - no se escribe')
        sys.exit(1)

    # ---------- 6. Escritura con backup ----------
    ts = datetime.now().strftime('%Y%m%d-%H%M%S')
    bak = ghx + '.bak-' + ts
    shutil.copy2(ghx, bak)
    data = ET.tostring(root, encoding='utf-8', xml_declaration=True)
    with open(ghx, 'wb') as f:
        f.write(b'\xef\xbb\xbf' + data)
    print('backup:', bak)
    print('escrito:', ghx)
    print('OK PATCH ZONAS v13.2 v2 aplicado (14 -> 19 salidas del #75)')
    print('Siguiente: regenerar .gh ->  pwsh -NoProfile -File scripts/utilities/ghx-to-gh.ps1 -InputGhx "{}"'.format(ghx))


if __name__ == '__main__':
    main()
