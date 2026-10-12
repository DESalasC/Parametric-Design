# -*- coding: utf-8 -*-
"""Volcado dirigido: #114 VOLUM, #116 DISTRIBUCION, #197 Zone, #189 Zone Settings,
#199 Python3, cadenas LC de zonas. Solo lectura."""
import io
import os
import re
import sys
import xml.etree.ElementTree as ET

BASE = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
GHX = os.path.join(BASE, "gh-definitions", "F1_CONTEXTO_v13.2.ghx")
TEMP = os.environ.get("TEMP", ".")

def text_of(el):
    return ''.join(el.itertext()) if el is not None else ''

def items_dict_multi(chunk):
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
            cd = items_dict_multi(c)
            objects.append({
                'guid': cd.get('InstanceGuid', [''])[0],
                'nick': cd.get('NickName', [''])[0],
                'name': cd.get('Name', [''])[0],
                'obj': o,
            })
            break

pmap = {}
for ob in objects:
    o = ob['obj']
    ins, outs = [], []
    for ch in o.iter('chunk'):
        if ch.get('name') == 'InputParam':
            d = items_dict_multi(ch)
            g = (d.get('InstanceGuid') or [''])[0]
            ins.append({'name': (d.get('Name') or [''])[0], 'guid': g, 'srcs': d.get('Source', [])})
        elif ch.get('name') == 'OutputParam':
            d = items_dict_multi(ch)
            g = (d.get('InstanceGuid') or [''])[0]
            outs.append({'name': (d.get('Name') or [''])[0], 'guid': g})
            pmap[g] = (ob['nick'], (d.get('Name') or [''])[0])
    ob['inputs'] = ins
    ob['outputs'] = outs

def label_pg(g):
    return '{}.{}'.format(pmap[g][0], pmap[g][1]) if g in pmap else '<' + g[:8] + '>'

def find(nick_sub):
    return [ob for ob in objects if nick_sub in ob['nick']]

def dump_ob(ob):
    o = ob['obj']
    print('\n===== {} [{}] ====='.format(ob['nick'], ob['guid']))
    ci = None
    for i in o.iter('item'):
        if i.get('name') == 'CodeInput':
            ci = i
    if ci is not None and ci.text:
        code = ci.text
        print('  code: {} chars'.format(len(code)))
        for mk in ['barras_implantadas_json', 'layout_usos_json', 'huella_xy', 'cota_arranque_m',
                   'bloques', 'niveles', 'Implantacion', 'IMPLANTACION']:
            print('    [{}] {}'.format('x' if mk in code else ' ', mk))
        p = os.path.join(TEMP, 'dump_{}.py'.format(ob['guid'][:8]))
        io.open(p, 'w', encoding='utf-8').write(code)
        print('    dump ->', p)
    print('  -- entradas:')
    for ip in ob['inputs']:
        srcs = ' + '.join(label_pg(s) for s in ip['srcs']) if ip['srcs'] else ''
        print('    {} <- {}'.format(ip['name'], srcs or '(sin cable)'))
    print('  -- salidas:')
    for op in ob['outputs']:
        cons = [label_pg2(t) for s, t in CONNS if s == op['guid']]
        print('    {} -> {}'.format(op['name'], ', '.join(cons) if cons else '(sin consumidores)'))

# conexiones
CONNS = []
for ob in objects:
    for ip in ob['inputs']:
        for s in ip['srcs']:
            CONNS.append((s, ip['guid']))
tgt_map = {}
for ob in objects:
    for ip in ob['inputs']:
        tgt_map[ip['guid']] = '{}.{}'.format(ob['nick'], ip['name'])
def label_pg2(g):
    return tgt_map.get(g, '<' + g[:8] + '>')

# 1) los tres componentes clave + #199
for sub in ('F3_VOLUM_GENERADOR_v08', 'F3_DISTRIBUCION_v03', 'Zone Settings', '-Zone', 'Python 3 Script'):
    for ob in find(sub)[:4]:
        if ob['name'] in ('Group',):
            continue
        dump_ob(ob)

# 2) cadenas LC nuevas (Polyline/Layer/Pen/Viewpoint/Slider/Boolean) con wiring
print('\n\n===== CADENAS LC (2D Polyline y vecinos) =====')
for ob in objects:
    if ob['name'] in ('2D Polyline', 'Layer', 'Pen', '2D Viewpoint', 'Line Type', 'Polyline Settings'):
        cons = [label_pg2(t) for s, t in CONNS if s in [op['guid'] for op in ob['outputs']]]
        srcs = []
        for ip in ob['inputs']:
            srcs.extend(label_pg(s) for s in ip['srcs'])
        if cons or srcs:
            print('  {} [{}]: in[{}] out[{}]'.format(ob['nick'], ob['guid'][:8], '; '.join(srcs), '; '.join(cons)))
