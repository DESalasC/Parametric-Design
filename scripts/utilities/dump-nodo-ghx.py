# -*- coding: utf-8 -*-
"""Dump de objetos del canvas por GUID (paneles, fuentes, consumidores).

Uso:
  .venv\\Scripts\\python.exe scripts\\utilities\\_tmp-dump-nodo.py <guids...>
"""
import sys
import xml.etree.ElementTree as ET
import os

BASE = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
GHX = os.path.join(BASE, "gh-definitions", "F1_CONTEXTO_v13.5.ghx")


def items_dict(chunk):
    d = {}
    for w in chunk:
        if w.tag == 'items':
            for i in w:
                if i.tag == 'item':
                    d.setdefault(i.get('name'), []).append((i.text or '').strip())
    return d


def main():
    guids = [a.lower() for a in sys.argv[1:]]
    root = ET.parse(GHX).getroot()

    # index: param guid -> (owner guid, owner nick, param name, direction)
    param_index = {}
    objects = []
    for o in root.iter('chunk'):
        if o.get('name') != 'Object':
            continue
        cont = None
        for c in o.iter('chunk'):
            if c.get('name') == 'Container':
                cont = c
                break
        if cont is None:
            continue
        cd = items_dict(cont)
        guid = (cd.get('InstanceGuid') or [''])[0]
        nick = (cd.get('NickName') or [''])[0]
        name = (cd.get('Name') or [''])[0]
        inputs = []
        outputs = []
        panel_texts = []
        for ch in o.iter('chunk'):
            n = ch.get('name')
            if n in ('InputParam', 'param_input'):
                d = items_dict(ch)
                nm = (d.get('Name') or [''])[0]
                srcs = d.get('Source', [])
                pg = (d.get('InstanceGuid') or [''])[0]
                inputs.append({'name': nm, 'srcs': srcs, 'pg': pg})
                if pg:
                    param_index[pg.lower()] = (guid, nick, nm, 'in')
            elif n in ('OutputParam', 'param_output'):
                d = items_dict(ch)
                nm = (d.get('Name') or [''])[0]
                pg = (d.get('InstanceGuid') or [''])[0]
                outputs.append({'name': nm, 'pg': pg})
                if pg:
                    param_index[pg.lower()] = (guid, nick, nm, 'out')
            elif n == 'PanelProperties':
                d = items_dict(ch)
                for k, vals in d.items():
                    panel_texts.extend(vals)
        objects.append({'guid': guid.lower(), 'nick': nick, 'name': name,
                        'inputs': inputs, 'outputs': outputs, 'panel': panel_texts,
                        'obj': o})

    by_guid = {x['guid']: x for x in objects}

    for g in guids:
        ob = by_guid.get(g)
        if not ob:
            print('NO ENCONTRADO:', g)
            continue
        print('=' * 100)
        print('{}  [{}]  guid={}'.format(ob['nick'], ob['name'], ob['guid']))
        if ob['panel']:
            print('--- PanelProperties ---')
            for t in ob['panel']:
                print(t)
        print('--- Inputs ---')
        for ip in ob['inputs']:
            desc = []
            for s in ip['srcs']:
                s2 = s.lower()
                if s2 in param_index:
                    og, onick, onm, odir = param_index[s2]
                    desc.append('{} · {}({})'.format(onick, onm, odir))
                else:
                    desc.append(s + ' ???')
            print('  in[{}] <- {}'.format(ip['name'], '; '.join(desc) or '(sin fuente)'))
        print('--- Outputs ---')
        for op in ob['outputs']:
            print('  out[{}] pg={}'.format(op['name'], op['pg']))


if __name__ == '__main__':
    main()
