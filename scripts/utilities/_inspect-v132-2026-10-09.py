# -*- coding: utf-8 -*-
"""Inspeccion SOLO LECTURA de un .ghx (v2): componentes F3, parametros, cableado
(las conexiones viven como items 'Source' en cada InputParam) y code embebido.

Uso:
  .venv\\Scripts\\python.exe scripts\\utilities\\_inspect-v132-2026-10-09.py [ruta.ghx]
"""
import os
import re
import sys
import xml.etree.ElementTree as ET

DEFAULT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..",
                       "gh-definitions", "F1_CONTEXTO_v13.2.ghx")


def text_of(el):
    return ''.join(el.itertext()) if el is not None else ''


def items_of(chunk):
    """[(name, text, elem)] de los items directos."""
    out = []
    for w in chunk:
        if w.tag == 'items':
            for i in w:
                if i.tag == 'item':
                    out.append((i.get('name'), (i.text or '').strip(), i))
    return out


def items_dict(chunk):
    d = {}
    for n, t, _i in items_of(chunk):
        if n not in d:
            d[n] = t
    return d


def container(obj):
    for c in obj.iter('chunk'):
        if c.get('name') == 'Container':
            return c
    return None


def main():
    ghx = sys.argv[1] if len(sys.argv) > 1 else os.path.normpath(DEFAULT)
    print('ghx:', ghx)
    root = ET.parse(ghx).getroot()

    objects = []
    for o in root.iter('chunk'):
        if o.get('name') != 'Object':
            continue
        c = container(o)
        if c is None:
            continue
        d = items_dict(c)
        objects.append((d.get('InstanceGuid', ''), d.get('NickName', ''), o))
    print('objetos: {}'.format(len(objects)))

    # pmap: param guid -> (owner nick, param name, dir)
    pmap = {}
    params = []  # (owner_guid, owner_nick, dir, name, guid, elem_chunk)
    for guid, nick, o in objects:
        for ch in o.iter('chunk'):
            if ch.get('name') in ('InputParam', 'OutputParam'):
                d = items_dict(ch)
                pg = d.get('InstanceGuid', '')
                direction = 'in' if ch.get('name') == 'InputParam' else 'out'
                if pg:
                    pmap[pg] = (nick, d.get('Name', ''), direction)
                    params.append((guid, nick, direction, d.get('Name', ''), pg, ch))
    print('parametros: {}'.format(len(pmap)))

    def label(pg):
        if pg in pmap:
            return '{}.{}'.format(pmap[pg][0], pmap[pg][1])
        return '<' + pg[:8] + '>'

    # conexiones desde items Source de los InputParam
    conns = []  # (src_guid, tgt_guid)
    for guid, nick, direction, name, pg, ch in params:
        if direction != 'in':
            continue
        for n, t, _i in items_of(ch):
            if n == 'Source' and t:
                conns.append((t, pg))
    print('conexiones (Source): {}'.format(len(conns)))

    for want, tag in (('F3_VOLUM', '#75'), ('NORMATIVA', '#154'), ('F3_MORPH', '#86'),
                      ('F3_UNIDADES', '#92'), ('F3_ACCESOS', '#93'), ('F3_DISTRIBUCION', '#76')):
        obj = None
        for guid, nick, o in objects:
            if want in nick:
                obj = (guid, nick, o)
                break
        if obj is None:
            print('\n== {}: NO ENCONTRADO'.format(want))
            continue
        guid, nick, o = obj
        print('\n===== {} [{}] ====='.format(nick, guid))
        # code
        ci = None
        for w in o:
            for c2 in w:
                if getattr(c2, 'tag', '') == 'chunk' and c2.get('name', '') == 'CodeInput':
                    ci = c2
        code = text_of(ci)
        if code:
            print('code chars: {}'.format(len(code)))
            for mk in ['v08.0', 'salida_zona', 'zonas_perimetros', 'salida_morph',
                       'envelope_por_piso', 'v09.2', '_huella_a_curva', 'v03.5',
                       'v02.2', 'SECCIÓN GRASSHOPPER', 'SECCION GRASSHOPPER']:
                print('  [{}] {}'.format('x' if mk in code else ' ', mk))
        # params
        print('-- entradas:')
        for g2, n2, direction, name, pg, ch in params:
            if g2 != guid or direction != 'in':
                continue
            srcs = [t for n, t, _ in items_of(ch) if n == 'Source' and t]
            srcstr = ' <- ' + ' + '.join(label(s) for s in srcs) if srcs else ''
            persist = ''
            for w in ch:
                for c2 in w:
                    if getattr(c2, 'tag', '') == 'chunk' and c2.get('name', '') == 'PersistentData':
                        t2 = text_of(c2).strip().replace('\n', ' ')
                        persist = ' persist="{}"'.format(t2[:70])
            print('   {}{}{}'.format(name, srcstr, persist))
        print('-- salidas:')
        for g2, n2, direction, name, pg, ch in params:
            if g2 != guid or direction != 'out':
                continue
            # consumidores
            cons = [label(s) for s, t in conns if s == pg]
            consstr = ' -> ' + ', '.join(cons) if cons else ''
            print('   {}{}'.format(name, consstr))

    # cableado general que involucre a F3 partes
    print('\n===== cableado F3 (src -> tgt) =====')
    for s, t in conns:
        sl, tl = label(s), label(t)
        if re.search(r'F3|NORMATIVA|MORPH|UNIDADES|ACCESOS|DISTRIBUCION', sl + tl, re.I):
            print('   {} -> {}'.format(sl, tl))


if __name__ == '__main__':
    main()
