# -*- coding: utf-8 -*-
"""F0_CENSO_ELEMENTOS_v01.py — Censo (SOLO LECTURA) de elementos del proyecto abierto en ArchiCAD.

Uso:
    .venv\\Scripts\\python.exe src\\interfases-archicad\\F0_CENSO_ELEMENTOS_v01.py
    .venv\\Scripts\\python.exe src\\interfases-archicad\\F0_CENSO_ELEMENTOS_v01.py --sel --bbox=Morph,Slab

Notas:
- Usa SOLO comandos Get* del API JSON (lectura; no modifica el proyecto).
- --bbox imprime bounding boxes por tipo (ordenados por huella descendente).
- --sel lista la seleccion actual (tipos por elemento).
"""
import sys
from collections import Counter

from archicad import ACConnection

TIPOS_DEF = ['Morph', 'Zone', 'Mesh', 'Slab', 'Object', 'Wall', 'Column', 'Beam',
             'Shell', 'Roof', 'Stair', 'CurtainWall', 'Door', 'Window']


def _dict(x):
    try:
        return x.to_dict()
    except Exception:
        return {'repr': repr(x)}


def main(argv):
    puerto = None
    tipos = TIPOS_DEF
    bbox_tipos = []
    con_sel = False
    i = 0
    while i < len(argv):
        a = argv[i]
        if a.startswith('--puerto='):
            puerto = int(a.split('=', 1)[1]); i += 1; continue
        if a == '--puerto':
            puerto = int(argv[i + 1]); i += 2; continue
        if a.startswith('--tipos='):
            tipos = a.split('=', 1)[1].split(','); i += 1; continue
        if a.startswith('--bbox='):
            bbox_tipos = a.split('=', 1)[1].split(','); i += 1; continue
        if a == '--sel':
            con_sel = True; i += 1; continue
        i += 1

    conn = ACConnection.connect(puerto)
    try:
        print('ProductInfo:', conn.commands.GetProductInfo())
    except Exception as e:
        print('ProductInfo ERROR:', e)

    by_type = {}
    for t in tipos:
        try:
            els = conn.commands.GetElementsByType(t)
            by_type[t] = els
            print('{:12s}: {}'.format(t, len(els)))
        except Exception as e:
            print('{:12s}: ERROR {}'.format(t, e))

    for t in bbox_tipos:
        els = by_type.get(t) or []
        if not els:
            print('--- bboxes {}: (sin elementos)'.format(t))
            continue
        try:
            bbs = conn.commands.Get3DBoundingBoxes(els)
        except Exception as e:
            print('--- bboxes {}: ERROR {}'.format(t, e))
            continue
        rows = []
        for k, bb in enumerate(bbs):
            d = _dict(bb)
            b = d.get('boundingBox3D') if isinstance(d, dict) else None
            if b:
                xmin, xmax = b.get('xMin'), b.get('xMax')
                ymin, ymax = b.get('yMin'), b.get('yMax')
                zmin, zmax = b.get('zMin'), b.get('zMax')
                area = (xmax - xmin) * (ymax - ymin)
                rows.append((area, k, xmin, xmax, ymin, ymax, zmin, zmax))
            else:
                rows.append((-1.0, k, None, None, None, None, None, None))
        rows.sort(key=lambda r: r[0], reverse=True)
        print('--- bboxes {} ({} elementos; top 50 por huella):'.format(t, len(rows)))
        for r in rows[:50]:
            print('  i={:4d} area~{:10.1f}  X[{:.2f},{:.2f}] Y[{:.2f},{:.2f}] Z[{:.2f},{:.2f}]'.format(
                r[1], r[0], r[2], r[3], r[4], r[5], r[6], r[7]))
        if len(rows) > 50:
            print('  ... {} mas'.format(len(rows) - 50))

    if con_sel:
        try:
            sel = conn.commands.GetSelectedElements()
            print('--- Seleccionados: {}'.format(len(sel)))
            if sel:
                try:
                    tt = conn.commands.GetTypesOfElements(sel)
                    c = Counter()
                    for x in tt:
                        d = _dict(x)
                        t2 = (d.get('typeOfElement') or {}).get('elementType')
                        c[t2] += 1
                    print('  tipos:', dict(c))
                except Exception as e:
                    print('  (tipos fallo: {})'.format(e))
        except Exception as e:
            print('--- Seleccionados ERROR:', e)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
