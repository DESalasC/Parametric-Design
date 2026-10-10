# -*- coding: utf-8 -*-
"""Inspeccion v3 SOLO LECTURA: code embebido de F3_VOLUM / F1_NORMATIVA en el
canvas, resolucion de fuentes no mapeadas (toggles/sliders), y dump de nicks.

Uso:
  .venv\\Scripts\\python.exe scripts\\utilities\\_inspect-v132-code.py
"""
import difflib
import io
import os
import re
import sys
import tempfile
import xml.etree.ElementTree as ET

BASE = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
GHX = os.path.join(BASE, "gh-definitions", "F1_CONTEXTO_v13.2.ghx")
SRCS = {
    'F3_VOLUM_GENERADOR_v08': os.path.join(BASE, 'src', 'fase-3-masa', 'F3_VOLUM_GENERADOR_v08.py'),
    'F1_ETAPA2_NORMATIVA_v09': os.path.join(BASE, 'src', 'fase-1-contexto', 'F1_ETAPA2_NORMATIVA_v09.1.py'),
}


def text_of(el):
    return ''.join(el.itertext()) if el is not None else ''


def items_dict(chunk):
    d = {}
    for w in chunk:
        if w.tag == 'items':
            for i in w:
                if i.tag == 'item':
                    d[i.get('name')] = (i.text or '').strip()
    return d


def main():
    raw = io.open(GHX, 'r', encoding='utf-8-sig', errors='ignore').read()
    print('ghx chars: {}'.format(len(raw)))
    for pat in ('zonas_perimetros', 'salida_zona', 'envelope_por_piso',
                'volumenes_por_uso', 'meshes'):
        print('  raw count "{}": {}'.format(pat, raw.count(pat)))

    root = ET.fromstring(raw.encode('utf-8'))
    objects = []
    for o in root.iter('chunk'):
        if o.get('name') != 'Object':
            continue
        for c in o.iter('chunk'):
            if c.get('name') == 'Container':
                d = items_dict(c)
                objects.append((d.get('InstanceGuid', ''), d.get('NickName', ''), o))
                break
    print('objetos: {}'.format(len(objects)))

    # guid -> info (param/object level)
    guid2info = {}
    for guid, nick, o in objects:
        for c in o.iter('chunk'):
            d = items_dict(c)
            g = d.get('InstanceGuid')
            if g and g not in guid2info:
                guid2info[g] = (c.get('name', ''), d, nick)
    # params map
    pmap = {}
    for guid, nick, o in objects:
        for c in o.iter('chunk'):
            if c.get('name') in ('InputParam', 'OutputParam'):
                d = items_dict(c)
                g = d.get('InstanceGuid')
                if g:
                    pmap[g] = (nick, d.get('Name', ''), c.get('name'))
    print('gui2info: {} | params: {}'.format(len(guid2info), len(pmap)))

    # conexiones
    conns = []
    for guid, nick, o in objects:
        for c in o.iter('chunk'):
            if c.get('name') != 'InputParam':
                continue
            d = items_dict(c)
            tgt = d.get('InstanceGuid', '')
            for w in c:
                if w.tag == 'items':
                    for i in w:
                        if i.tag == 'item' and i.get('name') == 'Source' and (i.text or '').strip():
                            conns.append(((i.text or '').strip(), tgt))

    def label(pg):
        if pg in pmap:
            return '{}.{}'.format(pmap[pg][0], pmap[pg][1])
        if pg in guid2info:
            return '{}[{}].{}'.format(guid2info[pg][2], guid2info[pg][0], guid2info[pg][1].get('Name', '?'))
        return '<' + pg[:8] + '>'

    # 0. dump de nicks
    tf = os.path.join(tempfile.gettempdir(), 'dp_v132_nicks.txt')
    with io.open(tf, 'w', encoding='utf-8') as f:
        for guid, nick, o in objects:
            f.write('{} {}\n'.format(guid[:8], nick))
    print('nicks -> {}'.format(tf))

    # 1. code embebido
    for key, src in SRCS.items():
        obj = None
        for guid, nick, o in objects:
            if key in nick:
                obj = (guid, nick, o)
                break
        if obj is None:
            print('\n== {}: no encontrado'.format(key))
            continue
        guid, nick, o = obj
        code = None
        for c in o.iter('chunk'):
            if c.get('name') == 'CodeInput':
                code = text_of(c)
        print('\n== code de {} [{}]: {} chars'.format(nick, guid[:8], len(code or '')))
        if code is not None:
            tfc = os.path.join(tempfile.gettempdir(), 'dp_v132_{}.py'.format(key))
            with io.open(tfc, 'w', encoding='utf-8') as f:
                f.write(code)
            print('   code dump -> {}'.format(tfc))
            markers = ['v08.0', 'v07.25', 'v07.14', 'salida_zona', 'zonas_perimetros',
                       'zonas_pisos', 'zonas_atributos', 'zonas_alturas',
                       'volumenes_principales_mesh', 'salida_morph', 'nucleo_pisos',
                       'circulacion_pisos', 'volumenes_por_uso', 'usos_pisos',
                       'treehelpers', 'envelope_aprobado_por_piso', '_publicar_por_piso']
            src_txt = io.open(src, 'r', encoding='utf-8-sig').read() if os.path.exists(src) else ''
            print('   markers (canvas | src):')
            for m in markers:
                print('    [{}|{}] {}'.format('x' if m in (code or '') else ' ',
                                              'x' if m in src_txt else ' ', m))
            if src_txt:
                a = (code or '').replace('\r\n', '\n').split('\n')
                b = src_txt.replace('\r\n', '\n').split('\n')
                sm = difflib.SequenceMatcher(None, a, b)
                print('   similitud canvas vs src: {:.3f} (canvas {} lineas, src {} lineas)'.format(
                    sm.ratio(), len(a), len(b)))
                diff = list(difflib.unified_diff(a, b, 'canvas', 'src', lineterm='', n=1))
                print('   diff lineas: {}'.format(len(diff)))
                if len(diff) < 400:
                    for dl in diff[:120]:
                        print('     ' + dl)
                else:
                    for dl in diff[:40]:
                        print('     ' + dl)
        # fuente desconocida de cada input
        for c in o.iter('chunk'):
            if c.get('name') != 'InputParam':
                continue
            d = items_dict(c)
            for w in c:
                if w.tag == 'items':
                    for i in w:
                        if i.tag == 'item' and i.get('name') == 'Source' and (i.text or '').strip():
                            pg = (i.text or '').strip()
                            if pg not in pmap:
                                info = guid2info.get(pg)
                                print('   input "{}" <- SIN MAPA {}'.format(d.get('Name', ''), pg[:8]))
                                if info:
                                    print('      owner: {} | chunk {} | items: {}'.format(
                                        info[2], info[0], {k: v for k, v in info[1].items() if k in ('Name', 'NickName')}))
                                    # persistent data dentro del chunk
                                    ch = None
                                    for cc in root.iter('chunk'):
                                        dd = items_dict(cc)
                                        if dd.get('InstanceGuid', '') == pg:
                                            ch = cc
                                            break
                                    if ch is not None:
                                        for w2 in ch:
                                            for c2 in w2:
                                                if getattr(c2, 'tag', '') == 'chunk' and c2.get('name', '') == 'PersistentData':
                                                    t2 = text_of(c2).replace('\n', ' ')
                                                    print('      persist: {}'.format(t2[-160:]))
                                else:
                                    print('      no resuelto en guid2info')

    # 2. consumidores de #86 (F3_MORPH) y #75 salidas
    for target in ('F3_MORPH_ATRIBUTOS_v02',):
        for guid, nick, o in objects:
            if target in nick:
                print('\n== consumidores de {}:'.format(nick))
                for c in o.iter('chunk'):
                    if c.get('name') != 'OutputParam':
                        continue
                    d = items_dict(c)
                    pg = d.get('InstanceGuid', '')
                    cons = [label(s) for s, t in conns if False]
                break

    def consumers_of(nick_sub):
        out = []
        for guid, nick, o in objects:
            if nick_sub not in nick:
                continue
            outs = {}
            for c in o.iter('chunk'):
                if c.get('name') == 'OutputParam':
                    d = items_dict(c)
                    outs[d.get('InstanceGuid', '')] = d.get('Name', '')
            for pg, nm in outs.items():
                for s, t in conns:
                    if s == pg:
                        out.append('{}.{} -> {}'.format(nick, nm, label(t)))
        return out

    print('\n== consumidores #75 salidas:')
    for x in consumers_of('F3_VOLUM_GENERADOR_v08'):
        print('   ' + x)
    print('== consumidores #86 salidas:')
    for x in consumers_of('F3_MORPH_ATRIBUTOS_v02'):
        print('   ' + x)
    print('== consumidores #154 salidas (solo envelope/aprobado):')
    for x in consumers_of('F1_ETAPA2_NORMATIVA_v09'):
        if 'envelope' in x or 'aprobado' in x:
            print('   ' + x)

    # 3. contextos de 'zona' en el texto (para ver si algo mas lo menciona)
    print('\n== ocurrencias de "zona" (case-insensitive, primeros 30, contexto 70):')
    n = 0
    start = 0
    low = raw.lower()
    while n < 30:
        idx = low.find('zona', start)
        if idx < 0:
            break
        seg = raw[max(0, idx - 40):idx + 70].replace('\n', ' ')
        print('   ...{}...'.format(seg))
        n += 1
        start = idx + 4


if __name__ == '__main__':
    main()
