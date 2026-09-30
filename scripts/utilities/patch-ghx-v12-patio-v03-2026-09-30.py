# -*- coding: utf-8 -*-
"""Parchea F1_CONTEXTO_v12.ghx: PATIO v02.5 -> v03.0 (bifurcacion multi-volumen).

Cambios (2026-09-30):
  1. #99-F1_ETAPA2_PATIO_v02.py -> embebe F1_ETAPA2_PATIO_v03.py,
     nickname "#99-F1_ETAPA2_PATIO_v03.py", descripcion actualizada.
  2. Nuevo InputParam "n_volumenes" (clone de altura_max_pot; TypeHint numero)
     con Source -> slider nuevo. InputCount 3 -> 4.
  3. Nuevo objeto "#166-Number Slider" (clone de #88) Min=1 Max=8 Value=1
     Digits=0 Interval=1; ubicado cerca de #99.
  4. Backup .bak-<ts>, escritura con BOM, validaciones (marcadores, sources
     resueltos, duplicados de chunk, conteo de objetos).

Uso: .venv\\Scripts\\python.exe scripts\\utilities\\patch-ghx-v12-patio-v03-2026-09-30.py
"""
import copy
import io
import os
import shutil
import sys
import uuid
import xml.etree.ElementTree as ET
from datetime import datetime

BASE = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
V12 = os.path.join(BASE, "gh-definitions", "F1_CONTEXTO_v12.ghx")
SRC_V03 = os.path.join(BASE, "src", "fase-1-contexto", "F1_ETAPA2_PATIO_v03.py")

new_guids = []


def nu():
    g = str(uuid.uuid4())
    new_guids.append(g)
    return g


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


def cont_set(obj, name, value):
    i = cont_get(obj, name)
    if i is None:
        raise RuntimeError('sin item ' + name)
    i.text = value
    return i


def parent_of(root, target):
    for p in root.iter():
        for c in p:
            if c is target:
                return p
    return None


def find_obj(root, prefix):
    for o in root.iter('chunk'):
        if o.get('name') == 'Object' and nick_of(o).startswith(prefix):
            return o
    return None


def set_pivot(obj, x, y):
    for it in obj.iter('item'):
        if it.get('name') == 'Pivot':
            for c in it:
                if c.tag == 'X':
                    c.text = str(x)
                if c.tag == 'Y':
                    c.text = str(y)
            break
    for it in obj.iter('item'):
        if it.get('name') == 'Bounds':
            for c in it:
                if c.tag == 'X':
                    c.text = str(x - 90)
                if c.tag == 'Y':
                    c.text = str(y - 40)
            break


def fix_counts(root):
    for w in root.iter():
        if w.tag == 'items':
            w.set('count', str(len([c for c in w if c.tag == 'item'])))
        elif w.tag == 'chunks':
            w.set('count', str(len([c for c in w if c.tag == 'chunk'])))


def count_sibling_dups(rt):
    bad_c = 0
    bad_i = 0
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
        elif w.tag == 'items':
            s2 = set()
            for i2 in w:
                if i2.tag != 'item':
                    continue
                nm2 = i2.get('name')
                if nm2 in s2:
                    bad_i += 1
                s2.add(nm2)
    return bad_c, bad_i


def main():
    # ---- carga ----
    tree = ET.parse(V12)
    root = tree.getroot()

    o99 = find_obj(root, '#99-F1_ETAPA2_PATIO_v02.py')
    if o99 is None:
        print('ERROR: no se encontro #99 PATIO v02'); sys.exit(1)
    o88 = find_obj(root, '#88-Number Slider')
    if o88 is None:
        print('ERROR: no se encontro #88 slider'); sys.exit(1)

    # ---- 1) CodeInput / nickname / descripcion ----
    code_new = io.open(SRC_V03, 'r', encoding='utf-8').read().replace('\r\n', '\n')
    ci = cont_get(o99, 'CodeInput')
    txt_prev = (ci.text or '')
    print('CodeInput previo: {} chars | nuevo: {} chars'.format(len(txt_prev), len(code_new)))
    ci.text = code_new
    cont_set(o99, 'NickName', '#99-F1_ETAPA2_PATIO_v03.py')
    dsc = cont_get(o99, 'Description')
    if dsc is not None:
        dsc.text = 'F1_ETAPA2_PATIO_v03.py - Patio(s) desde el Vertice N con bifurcacion (n_volumenes: unico/multi). Garantias area>=9 m2 y claridad>=3 m.'

    # ---- 2) nuevo InputParam n_volumenes ----
    altura_chunk = None
    for ch in o99.iter('chunk'):
        if ch.get('name') in ('param_input', 'InputParam'):
            nm = None
            for i in ch.iter('item'):
                if i.get('name') == 'Name':
                    nm = (i.text or '').strip()
            if nm == 'altura_max_pot':
                altura_chunk = ch
    if altura_chunk is None:
        print('ERROR: sin chunk altura_max_pot'); sys.exit(1)

    nv_chunk = copy.deepcopy(altura_chunk)
    for i in nv_chunk.iter('item'):
        if i.get('name') == 'Name':
            i.text = 'n_volumenes'
        if i.get('name') == 'NickName':
            i.text = 'n_volumenes'
        if i.get('name') == 'InstanceGuid':
            i.text = nu()
        if i.get('name') == 'SourceCount':
            i.text = '1'
    src_item = None
    for i in nv_chunk.iter('item'):
        if i.get('name') == 'Source':
            src_item = i
    # ---- 3) slider nuevo ----
    slider = copy.deepcopy(o88)
    cont_set(slider, 'InstanceGuid', nu())
    cont_set(slider, 'NickName', '#166-Number Slider')
    set_pivot(slider, 2280, 620)
    for ch in slider.iter('chunk'):
        if ch.get('name') == 'Slider':
            for i in ch.iter('item'):
                nm = i.get('name')
                if nm == 'Min':
                    i.text = '1'
                elif nm == 'Max':
                    i.text = '8'
                elif nm == 'Value':
                    i.text = '1'
                elif nm == 'Interval':
                    i.text = '1'
                elif nm == 'Digits':
                    i.text = '0'
                elif nm == 'SnapCount':
                    i.text = '0'
    g_slider = cont_get(slider, 'InstanceGuid').text.strip()

    # cablear n_volumenes -> slider
    if src_item is not None:
        src_item.text = g_slider
    else:
        raise RuntimeError('el clon de altura_max_pot no tiene item Source')

    # insertar el chunk tras altura_max_pot entre sus hermanos
    par = parent_of(root, altura_chunk)
    pos = list(par).index(altura_chunk) + 1
    par.insert(pos, nv_chunk)
    # indices secuenciales por nombre entre hermanos
    def reindex(parent):
        seq = {}
        for c in parent:
            if c.tag != 'chunk':
                continue
            nm = c.get('name')
            c.set('index', str(seq.get(nm, 0)))
            seq[nm] = seq.get(nm, 0) + 1
    reindex(par)

    # InputCount 4 (buscarlo en cualquier nivel del objeto)
    ic = None
    for it in o99.iter('item'):
        if it.get('name') == 'InputCount':
            ic = it
            break
    if ic is None:
        print('AVISO: sin InputCount en #99 (no se actualiza)')
    else:
        ic.text = '4'

    # ---- 4) insertar slider en DefinitionObjects ----
    def_objs = None
    wrapper = None
    for c in root.iter('chunk'):
        if c.get('name') == 'DefinitionObjects':
            def_objs = c
            break
    for w in def_objs.iter():
        if w.tag == 'chunks' and any(x.get('name') == 'Object' for x in w):
            wrapper = w
            break
    base_count = len([x for x in wrapper if x.tag == 'chunk' and x.get('name') == 'Object'])
    max_idx = -1
    for x in wrapper:
        if x.tag == 'chunk' and x.get('name') == 'Object':
            try:
                max_idx = max(max_idx, int(x.get('index')))
            except Exception:
                pass
    slider.set('index', str(max_idx + 1))
    wrapper.append(slider)

    fix_counts(root)

    # ---- validaciones ----
    root2 = ET.fromstring(ET.tostring(root, encoding='utf-8'))
    n_obj = len([x for x in wrapper if x.tag == 'chunk' and x.get('name') == 'Object'])
    seen = {}
    dups = 0
    for i in root2.iter('item'):
        if i.get('name') == 'InstanceGuid' and i.text:
            g = i.text.strip()
            if g in seen:
                dups += 1
            seen[g] = True
    dups_chunk, dups_item = count_sibling_dups(root2)
    txt = ET.tostring(root2, encoding='unicode')
    ok = True
    checks = [
        ('nickname v03', '#99-F1_ETAPA2_PATIO_v03.py' in txt),
        ('codigo v03 embebido', 'F1_ETAPA2_PATIO_v03.py' in txt and 'n_volumenes' in txt),
        ('slider #166', '#166-Number Slider' in txt),
        ('param n_volumenes presente', 'n_volumenes' in txt),
        ('objetos = base+1', n_obj == base_count + 1),
        ('sin duplicados de chunk', dups_chunk == 0),
        ('sin InstanceGuid duplicados', dups == 0),
    ]
    for nm, okc in checks:
        print('  [{}] {}'.format('OK' if okc else 'FAIL', nm))
        ok = ok and okc
    print('objetos:', n_obj, '| dups chunk/item:', dups_chunk, dups_item)

    if not ok:
        print('VALIDACION FALLIDA - no se escribe'); sys.exit(1)

    # ---- escritura con backup ----
    ts = datetime.now().strftime('%Y%m%d-%H%M%S')
    bak = V12 + '.bak-' + ts
    shutil.copy2(V12, bak)
    data = ET.tostring(root, encoding='utf-8', xml_declaration=True)
    with open(V12, 'wb') as f:
        f.write(b'\xef\xbb\xbf' + data)
    print('backup:', bak)
    print('escrito:', V12)
    print('OK PATCH v03 aplicado')


if __name__ == '__main__':
    main()
