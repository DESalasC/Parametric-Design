# -*- coding: utf-8 -*-
"""Dump LC-aware: incluye param_input/param_output (componentes Live Connection).
Solo lectura."""
import io
import os
import re
import sys
import xml.etree.ElementTree as ET

BASE = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
GHX = os.path.join(BASE, "gh-definitions", "F1_CONTEXTO_v13.2.ghx")
TEMP = os.environ.get("TEMP", ".")


def items_multi(chunk):
    d = {}
    for w in chunk:
        if w.tag == 'items':
            for i in w:
                if i.tag == 'item':
                    d.setdefault(i.get('name'), []).append((i.text or '').strip())
    return d


root = ET.parse(GHX).getroot()
objects = []
for o in root.iter('chunk'):
    if o.get('name') != 'Object':
        continue
    for c in o.iter('chunk'):
        if c.get('name') == 'Container':
            cd = items_multi(c)
            objects.append({'guid': cd.get('InstanceGuid', [''])[0],
                            'nick': cd.get('NickName', [''])[0],
                            'name': cd.get('Name', [''])[0], 'obj': o})
            break

pmap = {}
for ob in objects:
    ins, outs = [], []
    for ch in ob['obj'].iter('chunk'):
        n = ch.get('name')
        if n in ('InputParam', 'param_input'):
            d = items_multi(ch)
            ins.append({'name': (d.get('Name') or [''])[0],
                        'guid': (d.get('InstanceGuid') or [''])[0],
                        'srcs': d.get('Source', [])})
        elif n in ('OutputParam', 'param_output'):
            d = items_multi(ch)
            outs.append({'name': (d.get('Name') or [''])[0],
                         'guid': (d.get('InstanceGuid') or [''])[0]})
            pmap[(d.get('InstanceGuid') or [''])[0]] = (ob['nick'], (d.get('Name') or [''])[0])
    ob['inputs'], ob['outputs'] = ins, outs

tgt_map = {}
for ob in objects:
    for ip in ob['inputs']:
        tgt_map[ip['guid']] = '{}.{}'.format(ob['nick'], ip['name'])


def lbl(g):
    return '{}.{}'.format(pmap[g][0], pmap[g][1]) if g in pmap else '<' + g[:8] + '>'


def lbl_t(g):
    return tgt_map.get(g, '<' + g[:8] + '>')


def dump(ob):
    print('\n===== {} [{}] ({}) ====='.format(ob['nick'], ob['guid'][:8], ob['name']))
    for ip in ob['inputs']:
        srcs = ' + '.join(lbl(s) for s in ip['srcs']) if ip['srcs'] else '(sin cable)'
        print('   IN  {} <- {}'.format(ip['name'], srcs))
    for op in ob['outputs']:
        cons = ', '.join(lbl_t(s) for s, t in CONNS if s == op['guid'])
        print('   OUT {} -> {}'.format(op['name'], cons or '(sin consumidores)'))


CONNS = []
for ob in objects:
    for ip in ob['inputs']:
        for s in ip['srcs']:
            CONNS.append((s, ip['guid']))

want = re.compile(r'Zone|Morph|Story|CONTEXTO50|Polyline|Implanta|2D Curve|Area$', re.I)
print('===== COMPONENTES DE INTERES (con wiring) =====')
for ob in objects:
    if not ob['nick']:
        continue
    if not want.search(ob['nick']):
        continue
    if not (ob['inputs'] or ob['outputs']):
        continue
    haswire = any(ip['srcs'] for ip in ob['inputs']) or any(
        any(s == op['guid'] for s, t in CONNS) for op in ob['outputs'])
    if haswire or re.search(r'Zone|Morph|Story|CONTEXTO50|Implanta', ob['nick']):
        dump(ob)

print('\n===== todas las conexiones con "zonas_" o "Zone" o "Polyline" =====')
seen = set()
for s, t in CONNS:
    a, b = lbl(s), lbl_t(t)
    if re.search(r'zonas_|Zone|Polyline', a + ' ' + b, re.I):
        line = '{} -> {}'.format(a, b)
        if line not in seen:
            seen.add(line)
            print(' ', line)

# dump del codigo de F1_CONTEXTO50_BUILD si existe
for ob in objects:
    if 'CONTEXTO50' in ob['nick']:
        for i in ob['obj'].iter('item'):
            if i.get('name') == 'CodeInput' and i.text:
                p = os.path.join(TEMP, 'dump_contexto50.py')
                io.open(p, 'w', encoding='utf-8').write(i.text)
                print('\ncode contexto50 ->', p, len(i.text), 'chars')
                for mk in ['z_base', 'z_base_m']:
                    print('   [{}] {}'.format('x' if mk in i.text else ' ', mk))
