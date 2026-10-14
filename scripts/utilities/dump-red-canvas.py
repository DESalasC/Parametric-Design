# -*- coding: utf-8 -*-
"""Volcado de la RED de conexiones del canvas v13.5 (source -> target).

Uso:
  .venv\\Scripts\\python.exe scripts\\utilities\\dump-red-canvas.py [filtro_guid_1 filtro_guid_2 ...]

Sin filtros: imprime TODAS las conexiones (una por linea) a stdout.
Con filtros: imprime solo las lineas que contengan alguno de los filtros (substring, case-insensitive).
Los identificadores se imprimen como '<Nick> <guid8>' para poder filtrar por GUID o por Nick.
"""
import sys
import os
import xml.etree.ElementTree as ET

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
    filt = [a.lower() for a in sys.argv[1:]] if len(sys.argv) > 1 else None
    root = ET.parse(GHX).getroot()
    param_index = {}   # pg guid -> (owner guid, owner nick, param name, dir)
    objects = {}
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
        guid = (cd.get('InstanceGuid') or [''])[0].lower()
        nick = (cd.get('NickName') or [''])[0]
        name = (cd.get('Name') or [''])[0]
        ins = []
        for ch in o.iter('chunk'):
            n = ch.get('name')
            if n in ('InputParam', 'param_input'):
                d = items_dict(ch)
                nm = (d.get('Name') or [''])[0]
                pg = (d.get('InstanceGuid') or [''])[0]
                srcs = d.get('Source', [])
                ins.append((nm, pg, srcs))
                if pg:
                    param_index[pg.lower()] = (guid, nick, nm, 'in')
            elif n in ('OutputParam', 'param_output'):
                d = items_dict(ch)
                nm = (d.get('Name') or [''])[0]
                pg = (d.get('InstanceGuid') or [''])[0]
                if pg:
                    param_index[pg.lower()] = (guid, nick, nm, 'out')
        objects[guid] = {'nick': nick, 'name': name, 'ins': ins}

    for tg, ob in objects.items():
        for nm, pg, srcs in ob['ins']:
            for s in srcs:
                s2 = s.lower()
                if s2 in param_index:
                    og, onick, onm, odir = param_index[s2]
                    line = '{n1} [{g1}] .{p1}  ->  {n2} [{g2}] .{p2}'.format(
                        n1=onick, g1=og[:8], p1=onm, n2=ob['nick'], g2=tg[:8], p2=nm)
                else:
                    line = '?? [{g1}]  ->  {n2} [{g2}] .{p2}'.format(
                        g1=s[:8], n2=ob['nick'], g2=tg[:8], p2=nm)
                if filt and not any(f in line.lower() for f in filt):
                    continue
                print(line)


if __name__ == '__main__':
    main()
