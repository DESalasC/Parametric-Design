# -*- coding: utf-8 -*-
"""Compara CodeInput embebido en el canvas .ghx vs archivos src (hash + cola)."""
import hashlib
import os
import xml.etree.ElementTree as ET

BASE = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
GHX = os.path.join(BASE, "gh-definitions", "F1_CONTEXTO_v13.5.ghx")
TARGETS = {
    "8c7e8133-0bbe-401d-9fa0-6c4b761bbc5d": os.path.join(BASE, "src", "fase-3-masa", "F3_VOLUM_GENERADOR_v08.py"),
    "6eaf2956-f649-4540-a900-4b32a10deee4": os.path.join(BASE, "src", "fase-3-masa", "F3_DISTRIBUCION_v03.py"),
}


def items_dict(chunk):
    d = {}
    for w in chunk:
        if w.tag == 'items':
            for i in w:
                if i.tag == 'item':
                    d.setdefault(i.get('name'), []).append((i.text or ''))
    return d


def main():
    root = ET.parse(GHX).getroot()
    nobj = sum(1 for o in root.iter('chunk') if o.get('name') == 'Object')
    print('objetos en el canvas:', nobj)
    found = {}
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
        guid = (cd.get('InstanceGuid') or [''])[0].strip().lower()
        if guid in TARGETS:
            code = ''
            for i in o.iter('item'):
                if i.get('name') == 'CodeInput' and i.text:
                    code = i.text
            found[guid] = code

    for guid, ruta in TARGETS.items():
        emb = found.get(guid, '')
        with open(ruta, 'rb') as f:
            src = f.read().decode('utf-8-sig')
        emb_n = emb.replace('\r\n', '\n')
        src_n = src.replace('\r\n', '\n')
        h_emb = hashlib.sha1(emb_n.encode('utf-8')).hexdigest()
        h_src = hashlib.sha1(src_n.encode('utf-8')).hexdigest()
        print(os.path.basename(ruta))
        print('  embedded: {} chars  sha1={}'.format(len(emb_n), h_emb[:12]))
        print('  src     : {} chars  sha1={}'.format(len(src_n), h_src[:12]))
        print('  IGUALES: {}'.format(h_emb == h_src))
        i_e = emb_n.find('\nimport ')
        i_s = src_n.find('\nimport ')
        if i_e >= 0 and i_s >= 0:
            t_e = emb_n[i_e:]
            t_s = src_n[i_s:]
            h_e = hashlib.sha1(t_e.encode('utf-8')).hexdigest()
            h_s = hashlib.sha1(t_s.encode('utf-8')).hexdigest()
            print('  cola (desde primer import): iguales = {}'.format(h_e == h_s))
            if h_e != h_s:
                for k in range(min(len(t_e), len(t_s))):
                    if t_e[k] != t_s[k]:
                        print('  primera diff cola en char {}:\n    {!r}\n    {!r}'.format(
                            k, t_e[max(0, k - 60):k + 60], t_s[max(0, k - 60):k + 60]))
                        break
                else:
                    print('  cola: difieren solo en longitud ({} vs {})'.format(len(t_e), len(t_s)))


if __name__ == '__main__':
    main()
