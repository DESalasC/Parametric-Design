# -*- coding: utf-8 -*-
"""Inventario del canvas GHX + reporte de cableado (zonas/implantacion/stories).

Genera:
  docs/planes/2026-10-11-implantacion-niveles-zonas/INVENTARIO-CANVAS-v13.2.md
  (tabla: # macro, NickName, GUID, tipo, conexiones, clasificacion, notas)

Uso:
  .venv\\Scripts\\python.exe scripts\\utilities\\inventario-canvas.py [ruta.ghx] [salida.md]
"""
import io
import os
import re
import sys
import xml.etree.ElementTree as ET

BASE = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
GHX_DEF = os.path.join(BASE, "gh-definitions", "F1_CONTEXTO_v13.5.ghx")
OUT_DEF = os.path.join(BASE, "docs", "planes", "2026-10-11-implantacion-niveles-zonas",
                       "INVENTARIO-CANVAS-v13.5.md")
NICKS_OLD = os.path.join(os.environ.get("TEMP", "."), "dp_v132_nicks.txt")

LC_NAMES = {
    "2D Polyline", "Layer", "Pen", "Line Type", "Polyline Settings", "2D Viewpoint",
    "Morph Solid", "Morph Curve", "Morph Settings", "Mesh", "CreateMeshes",
    "MeshSkirtTypes", "MeshRidgeTypes", "Deconstruct Mesh", "Zone", "Zone Settings",
    "Deconstruct Zone", "Extract Zone Settings", "PolylineDetails", "2D Curve",
    "End Points",
}
UI_NAMES = {"Number Slider", "Boolean Toggle", "Value List", "File Path", "Text"}
UTIL_NAMES = {"Merge", "Relay", "Text Join", "Addition", "Multiplication", "Division",
              "Subtraction", "Discontinuity", "Bifocals", "Fancy Names", "Curve", "Area",
              "Series", "Construct Point", "Deconstruct", "Sift", "Weave", "Entwine",
              "Item List", "List Item", "Dispatch", "Gate", "Stream Filter", "Stream Gate"}
SCRIPT_HINTS = ("F1_", "F2_", "F3_", "F0_", "GhPython", "Python 3 Script")


def text_of(el):
    return ''.join(el.itertext()) if el is not None else ''


def items_dict(chunk):
    d = {}
    for w in chunk:
        if w.tag == 'items':
            for i in w:
                if i.tag == 'item':
                    d.setdefault(i.get('name'), []).append((i.text or '').strip())
    return d


def get_container(obj):
    for c in obj.iter('chunk'):
        if c.get('name') == 'Container':
            return c
    return None


def main():
    ghx = sys.argv[1] if len(sys.argv) > 1 else GHX_DEF
    out_md = sys.argv[2] if len(sys.argv) > 2 else OUT_DEF
    print('ghx:', ghx)
    root = ET.parse(ghx).getroot()

    objects = []  # dicts
    for o in root.iter('chunk'):
        if o.get('name') != 'Object':
            continue
        cont = get_container(o)
        if cont is None:
            continue
        cd = items_dict(cont)
        guid = cd.get('InstanceGuid', [''])[0]
        nick = cd.get('NickName', [''])[0]
        name = cd.get('Name', [''])[0]
        inputs, outputs = [], []
        for ch in o.iter('chunk'):
            if ch.get('name') in ('InputParam', 'param_input'):
                d = items_dict(ch)
                srcs = d.get('Source', [])
                inputs.append({'name': (d.get('Name') or [''])[0], 'srcs': srcs})
            elif ch.get('name') in ('OutputParam', 'param_output'):
                d = items_dict(ch)
                outputs.append({'name': (d.get('Name') or [''])[0],
                                'pg': (d.get('InstanceGuid') or [''])[0]})
        code_len = 0
        for i in o.iter('item'):
            if i.get('name') == 'CodeInput' and i.text:
                code_len = len(i.text)
        panel_chars = None
        for ch in o.iter('chunk'):
            if ch.get('name') == 'PanelProperties':
                tot = 0
                for w in ch:
                    if w.tag == 'items':
                        for i in w:
                            if i.tag == 'item' and i.text:
                                tot += len(i.text.strip())
                panel_chars = tot
        num = None
        m = re.match(r'^#(\d+)', nick or '')
        if m:
            num = int(m.group(1))
        objects.append({
            'guid': guid, 'nick': nick, 'name': name, 'num': num,
            'inputs': inputs, 'outputs': outputs, 'code_len': code_len,
            'panel_chars': panel_chars, 'obj': o,
        })

    # out-degree map
    pg_out = {}
    for ob in objects:
        for op in ob['outputs']:
            if op['pg']:
                pg_out[op['pg']] = ob['guid']
    for ob in objects:
        ob['outdeg'] = 0
        ob['out_consumers'] = []
    for ob in objects:
        for ip in ob['inputs']:
            for s in ip['srcs']:
                if s in pg_out:
                    src = next((x for x in objects if x['guid'] == pg_out[s]), None)
                    if src:
                        src['outdeg'] += 1
                        src['out_consumers'].append(ob['nick'])

    def classify(ob):
        n = ob['name']
        nick = ob['nick']
        if n == 'Group' or nick.startswith(('01 |', '02 |', '03 |', '04 |', '05 |', '06 |',
                                            '07 |', '08 |', '09 |', '10 |')):
            return 'Grupo'
        if n == 'Panel' or 'Panel' in n:
            if ob.get('panel_chars') == 0:
                return 'Informativo (Panel vacio)'
            return 'Informativo (Panel)'
        if n in LC_NAMES:
            return 'LC -> ArchiCAD'
        if any(h in n for h in ('GhPython', 'Python 3 Script')) or ob['code_len'] > 1000:
            return 'Logica (script)'
        if n in UI_NAMES:
            return 'Entrada (UI)'
        if n in UTIL_NAMES:
            return 'Soporte (util)'
        return 'Otro'

    for ob in objects:
        ob['cls'] = classify(ob)
        conn = 'in {} / out {}'.format(sum(1 for i in ob['inputs'] if i['srcs']), ob['outdeg'])
        ob['conn'] = conn

    objects_sorted = sorted(objects, key=lambda x: (x['num'] is None, x['num'] or 0, x['nick'] or ''))

    # --- diff vs old nicks (Oct-9) ---
    nuevos, desaparecidos, renombrados = [], [], []
    if os.path.isfile(NICKS_OLD):
        old = {}
        for ln in io.open(NICKS_OLD, 'r', encoding='utf-8'):
            parts = ln.strip().split(' ', 1)
            if len(parts) == 2:
                old[parts[0]] = parts[1]
        new = {ob['guid'][:8]: ob['nick'] for ob in objects}
        for g8, nick in new.items():
            if g8 not in old:
                nuevos.append((g8, nick))
            elif old[g8] != nick:
                renombrados.append((g8, old[g8], nick))
        for g8, nick in old.items():
            if g8 not in new:
                desaparecidos.append((g8, nick))

    # --- wiring de zonas/implantacion ---
    wiring = []
    label = {ob['guid']: ob['nick'] for ob in objects}
    pmap = {}
    for ob in objects:
        for ip in ob['inputs']:
            for s in ip['srcs']:
                sl = None
                if s in pg_out:
                    src = next((x for x in objects if x['guid'] == pg_out[s]), None)
                    if src:
                        out_name = next((op['name'] for op in src['outputs'] if op['pg'] == s), '?')
                        sl = '{}.{}'.format(src['nick'], out_name)
                tl = '{}.{}'.format(ob['nick'], ip['name'])
                if re.search(r'zonas_|implanta|bloques|layout_usos|barras|Zone|Story|z_base|malla',
                             (sl or s) + ' ' + tl, re.I):
                    wiring.append('{} -> {}'.format(sl or ('<' + s[:8] + '>'), tl))
    wiring = sorted(set(wiring))

    # --- write MD ---
    os.makedirs(os.path.dirname(out_md), exist_ok=True)
    L = []
    L.append('# Inventario del canvas — F1_CONTEXTO_v13.5 (2026-10-11 22:18)')
    L.append('')
    L.append('Generado por `scripts/utilities/inventario-canvas.py`. '
             'Estado: **inventario vivo** (se actualiza a medida que avanza el canvas; '
             'no implica limpieza — punto 8 reformulado 2026-10-11).')
    L.append('')
    L.append('## Resumen')
    L.append('')
    from collections import Counter
    cc = Counter(ob['cls'] for ob in objects)
    L.append('| Clasificacion | Cuenta |')
    L.append('|---|---|')
    for k, v in cc.most_common():
        L.append('| {} | {} |'.format(k, v))
    L.append('| **TOTAL** | **{}** |'.format(len(objects)))
    L.append('')
    if os.path.isfile(NICKS_OLD):
        L.append('### Cambios vs 2026-10-09 (noche)')
        L.append('')
        L.append('- Nuevos: {}'.format(', '.join('{} {}'.format(g, n) for g, n in nuevos) or '—'))
        L.append('- Renombrados: {}'.format('; '.join('{}: {} -> {}'.format(g, a, b) for g, a, b in renombrados) or '—'))
        L.append('- Desaparecidos: {}'.format(', '.join('{} {}'.format(g, n) for g, n in desaparecidos) or '—'))
        L.append('')
    L.append('## Componentes')
    L.append('')
    L.append('| # | Nick / nombre | GUID | Tipo | Conexiones | Clasificacion | Nota |')
    L.append('|---|---|---|---|---|---|---|')
    for ob in objects_sorted:
        nota = ''
        if ob['cls'].startswith('Informativo') and ob.get('panel_chars') == 0:
            nota = 'PANEL VACIO'
        elif ob['cls'] == 'Logica (script)':
            nota = 'codigo {} chars'.format(ob['code_len'])
        elif ob['cls'] == 'LC -> ArchiCAD':
            nota = 'destino ArchiCAD'
        if ob['outdeg'] == 0 and ob['cls'] in ('Logica (script)', 'LC -> ArchiCAD'):
            nota = (nota + '; ' if nota else '') + 'SIN consumidores (salida no usada)'
        L.append('| {} | {} | `{}` | {} | {} | {} | {} |'.format(
            ob['num'] if ob['num'] is not None else '—',
            (ob['nick'] or '').replace('|', '/') or (ob['name'] or ''),
            ob['guid'], ob['name'], ob['conn'], ob['cls'], nota))
    L.append('')
    L.append('## Cableado clave (zonas / implantacion / stories)')
    L.append('')
    L.append('```')
    for w in wiring:
        L.append(w)
    L.append('```')
    L.append('')
    L.append('## Leyenda')
    L.append('')
    L.append('- **Grupo**: contenedor organizativo. No borrar sin revisar.')
    L.append('- **Informativo (Panel)**: solo muestra texto; no participa en el calculo.')
    L.append('- **LC -> ArchiCAD**: componente de la Live Connection (destino).')
    L.append('- **Logica (script)**: GhPython/Python3; indispensable si tiene consumidores.')
    L.append('- **Entrada (UI)**: sliders/toggles/listas: parametros del operador.')
    L.append('- **Soporte (util)**: merges/relays/joins/curvas: utilidades de cableado.')
    L.append('- **Otro**: revisar caso a caso.')
    io.open(out_md, 'w', encoding='utf-8').write('\n'.join(L))

    print('escrito:', out_md)
    print('objetos:', len(objects))
    print('clasif:', dict(cc))
    if os.path.isfile(NICKS_OLD):
        print('nuevos:', len(nuevos), '| renombrados:', len(renombrados), '| desaparecidos:', len(desaparecidos))
        for g, n in nuevos[:40]:
            print('  + {} {}'.format(g, n))
        for g, a, b in renombrados[:40]:
            print('  ~ {} {} -> {}'.format(g, a, b))
        for g, n in desaparecidos[:40]:
            print('  - {} {}'.format(g, n))
    print('--- cableado clave (primeros 120) ---')
    for w in wiring[:120]:
        print(' ', w)


if __name__ == '__main__':
    main()
