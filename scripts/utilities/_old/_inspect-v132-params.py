# -*- coding: utf-8 -*-
"""Dump estructura de params del #75 (para construir patch de salidas zona)."""
import io
import os
import xml.etree.ElementTree as ET
from xml.dom import minidom

BASE = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
GHX = os.path.join(BASE, "gh-definitions", "F1_CONTEXTO_v13.2.ghx")
OUT = os.path.join(os.environ.get('TEMP', '.'), 'dp_v132_estructura.txt')


def items_dict(chunk):
    d = {}
    for w in chunk:
        if w.tag == 'items':
            for i in w:
                if i.tag == 'item':
                    d[i.get('name')] = (i.text or '').strip()
    return d


def pretty(elem):
    s = ET.tostring(elem, encoding='unicode')
    try:
        p = minidom.parseString(s.encode('utf-8')).toprettyxml(indent=' ')
        return '\n'.join(l for l in p.split('\n') if l.strip())
    except Exception:
        return s


root = ET.parse(GHX).getroot()
out = []
for o in root.iter('chunk'):
    if o.get('name') != 'Object':
        continue
    nick = ''
    for c in o.iter('chunk'):
        if c.get('name') == 'Container':
            nick = items_dict(c).get('NickName', '')
            break
    if 'F3_VOLUM' not in nick:
        continue
    out.append('===== OBJETO: {} ====='.format(nick))
    for c in o.iter('chunk'):
        n = c.get('name')
        d = items_dict(c)
        if n == 'ParameterData':
            out.append('----- ParameterData -----')
            out.append(pretty(c)[:6000])
        elif n == 'OutputParam' and d.get('Name') == 'mensaje':
            out.append('----- OutputParam (mensaje) -----')
            out.append(pretty(c)[:4000])
        elif n == 'InputParam' and d.get('Name') == 'salida_zona':
            out.append('----- InputParam (salida_zona) -----')
            out.append(pretty(c)[:4000])
        elif n == 'Container':
            out.append('----- Container items: {} -----'.format(sorted(d.keys())))

io.open(OUT, 'w', encoding='utf-8').write('\n'.join(out))
print('escrito:', OUT)
print('\n'.join(out)[:12000])
