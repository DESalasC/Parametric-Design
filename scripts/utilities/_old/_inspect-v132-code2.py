# -*- coding: utf-8 -*-
"""Inspeccion v4 SOLO LECTURA: CodeInput como item; dump de toggles #48/#49;
estructura del #75. Uso: .venv\\Scripts\\python.exe scripts\\utilities\\_inspect-v132-code2.py
"""
import difflib
import io
import os
import re
import sys
import tempfile
import xml.etree.ElementTree as ET
from xml.dom import minidom

BASE = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
GHX = os.path.join(BASE, "gh-definitions", "F1_CONTEXTO_v13.2.ghx")
SRCS = {
    'F3_VOLUM_GENERADOR_v08': os.path.join(BASE, 'src', 'fase-3-masa', 'F3_VOLUM_GENERADOR_v08.py'),
    'F1_ETAPA2_NORMATIVA_v09': os.path.join(BASE, 'src', 'fase-1-contexto', 'F1_ETAPA2_NORMATIVA_v09.1.py'),
    'F3_MORPH_ATRIBUTOS_v02': os.path.join(BASE, 'src', 'fase-3-masa', 'F3_MORPH_ATRIBUTOS_v02.py'),
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


def find_item(obj, name):
    for i in obj.iter('item'):
        if i.get('name') == name:
            return i
    return None


def main():
    root = ET.parse(GHX).getroot()
    objects = []
    for o in root.iter('chunk'):
        if o.get('name') != 'Object':
            continue
        for c in o.iter('chunk'):
            if c.get('name') == 'Container':
                d = items_dict(c)
                objects.append((d.get('InstanceGuid', ''), d.get('NickName', ''), o))
                break

    print('== objetos con item CodeInput:')
    for guid, nick, o in objects:
        ci = find_item(o, 'CodeInput')
        if ci is None:
            continue
        code = ci.text or ''
        print('   [{}] {} -> {} chars'.format(guid[:8], nick, len(code)))

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
        ci = find_item(o, 'CodeInput')
        code = (ci.text or '') if ci is not None else None
        print('\n===== {} [{}] ====='.format(nick, guid[:8]))
        print('code chars: {}'.format(len(code or '')))
        if code:
            tfc = os.path.join(tempfile.gettempdir(), 'dp_v132_{}.py'.format(key))
            with io.open(tfc, 'w', encoding='utf-8') as f:
                f.write(code)
            print('dump -> {}'.format(tfc))
            markers = ['v08.0', 'v07.25', 'v07.14', 'salida_zona', 'zonas_perimetros',
                       'zonas_pisos', 'zonas_atributos', 'zonas_alturas',
                       'volumenes_principales_mesh', 'salida_morph', 'nucleo_pisos',
                       'circulacion_pisos', 'volumenes_por_uso', 'usos_pisos',
                       'treehelpers', 'envelope_aprobado_por_piso', '_publicar_por_piso',
                       'v09.2', 'v02.2']
            src_txt = io.open(src, 'r', encoding='utf-8-sig').read() if os.path.exists(src) else ''
            print('markers (canvas | src):')
            for m in markers:
                print('   [{}|{}] {}'.format('x' if m in code else ' ', 'x' if m in src_txt else ' ', m))
            if src_txt:
                a = code.replace('\r\n', '\n').split('\n')
                b = src_txt.replace('\r\n', '\n').split('\n')
                sm = difflib.SequenceMatcher(None, a, b)
                print('similitud: {:.3f} (canvas {} / src {} lineas)'.format(sm.ratio(), len(a), len(b)))
                diff = list(difflib.unified_diff(a, b, 'canvas', 'src', lineterm='', n=1))
                print('diff lineas: {}'.format(len(diff)))
                lim = 200 if len(diff) < 400 else 60
                for dl in diff[:lim]:
                    print('  ' + dl)

    # toggles #48/#49 completos
    for want in ('#48-Boolean Toggle', '#49-Boolean Toggle'):
        for guid, nick, o in objects:
            if nick != want:
                continue
            print('\n===== TOGGLE {} [{}] ====='.format(nick, guid[:8]))
            s = ET.tostring(o, encoding='unicode')
            try:
                pretty = minidom.parseString(s.encode('utf-8')).toprettyxml(indent=' ')
                lines = [l for l in pretty.split('\n') if l.strip()]
                for l in lines[:120]:
                    print('  ' + l.rstrip())
            except Exception:
                print(s[:4000])
            break

    # estructura del #75: items del Container y chunks presentes
    for guid, nick, o in objects:
        if 'F3_VOLUM' not in nick:
            continue
        print('\n===== ESTRUCTURA {} [{}] ====='.format(nick, guid[:8]))
        c = None
        for cc in o.iter('chunk'):
            if cc.get('name') == 'Container':
                c = cc
                break
        print('Container items:', sorted(items_dict(c).keys()))
        chunknames = {}
        for cc in o.iter('chunk'):
            n = cc.get('name')
            chunknames[n] = chunknames.get(n, 0) + 1
        print('chunks bajo el objeto:', chunknames)
        # outputs con nombres
        outs = []
        for cc in o.iter('chunk'):
            if cc.get('name') == 'OutputParam':
                d = items_dict(cc)
                outs.append(d.get('Name', ''))
        print('outputs ({}): {}'.format(len(outs), outs))
        break


if __name__ == '__main__':
    main()
