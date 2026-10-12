# -*- coding: utf-8 -*-
"""Sincroniza src/ con el codigo embebido en el canvas F1_CONTEXTO_v13.2.ghx.

F0 (2026-10-11). Lee los CodeInput (GhPython) y los Script/Text base64
(Python 3 Script) del canvas y compara con los archivos de src/. Para los que
difieren: backup .bak-sync-<ts> + escritura del codigo EXACTO del canvas.

Uso: .venv\\Scripts\\python.exe scripts\\utilities\sync-canvas-to-src.py [--write]
     (sin --write: solo reporte)
"""
import base64
import difflib
import io
import os
import shutil
import sys
import time
import xml.etree.ElementTree as ET

BASE = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
GHX = os.path.join(BASE, "gh-definitions", "F1_CONTEXTO_v13.5.ghx")

MAPA = [
    # (guid[:8], ruta src relativa, descripcion)
    ("8c7e8133", "src/fase-3-masa/F3_VOLUM_GENERADOR_v08.py", "F3_VOLUM (#114)"),
    ("6eaf2956", "src/fase-3-masa/F3_DISTRIBUCION_v03.py", "F3_DISTRIBUCION (#116)"),
    ("d4aab682", "src/fase-1-contexto/F1_ETAPA2_NORMATIVA_v09.1.py", "NORMATIVA v09.1 (#151)"),
    ("dcca63ed", "src/fase-1-contexto/F1_ETAPA2_NORMATIVA_v10.py", "NORMATIVA v10 (#199)"),
    ("d3bed17b", "src/fase-1-contexto/F1_ETAPA2_PATIO_v03.py", "PATIO v03 (#75)"),
    ("03edc848", "src/fase-1-contexto/F1_ETAPA2_LADOS_v06.py", "LADOS v06 (#67)"),
    ("0d986a36", "src/fase-1-contexto/F1_ETAPA1_CONTEXTO_v04.4.1.py", "ETAPA1 v04.4.1 (#59)"),
    ("880d9e49", "src/fase-1-contexto/F1_LAYERS_XML_v02.py", "LAYERS XML (#154)"),
    ("f7f1bd10", "src/fase-1-contexto/F0_LOAD_PROYECTO_v01.py", "F0 LOAD (#16)"),
    ("4d6fba96", "src/fase-1-contexto/F1_EXPORTAR_GFA_v02.4.py", "EXPORTAR GFA (#238)"),
    ("37bf9948", "src/fase-3-masa/F3_UNIDADES_TIPOLOGIAS_v02.py", "UNIDADES v02 (#139)"),
    ("768ebdc8", "src/fase-3-masa/F3_ACCESOS_INTEGRADOR_v02.py", "ACCESOS v02 (#149)"),
    ("7aadd219", "src/fase-1-contexto/F1_OVERRIDE_USO_v01.py", "OVERRIDE USO (#231)"),
    ("ad270c61", "src/fase-1-contexto/F1_CONTEXTO50_BUILD_v01.2.py", "CONTEXTO50 BUILD (#51)"),
]


def items_multi(chunk):
    d = {}
    for w in chunk:
        if w.tag == 'items':
            for i in w:
                if i.tag == 'item':
                    d.setdefault(i.get('name'), []).append(i.text or '')
    return d


def main():
    do_write = '--write' in sys.argv
    root = ET.parse(GHX).getroot()
    objs = {}
    for o in root.iter('chunk'):
        if o.get('name') != 'Object':
            continue
        for c in o.iter('chunk'):
            if c.get('name') == 'Container':
                d = items_multi(c)
                g = (d.get('InstanceGuid') or [''])[0]
                objs[g[:8]] = o
                break

    print('modo:', 'ESCRITURA' if do_write else 'solo reporte')
    print('{:<22} {:<46} {:>7} {:>7} {:>6} {}'.format('componente', 'archivo src', 'canvas', 'src', 'sim', 'accion'))
    results = []
    for g8, rel, desc in MAPA:
        o = objs.get(g8)
        if o is None:
            results.append((desc, rel, '-', '-', '-', 'NO ENCONTRADO en canvas'))
            continue
        code = None
        for i in o.iter('item'):
            if i.get('name') == 'CodeInput' and i.text:
                code = i.text
        if code is None:
            for ch in o.iter('chunk'):
                if ch.get('name') == 'Script':
                    dd = items_multi(ch)
                    t = (dd.get('Text') or [''])[0]
                    if t:
                        try:
                            code = base64.b64decode(t).decode('utf-8', 'replace')
                        except Exception as e:
                            print('b64 fail', g8, e)
        if code is None:
            results.append((desc, rel, '-', '-', '-', 'sin codigo'))
            continue
        path = os.path.join(BASE, rel.replace('/', os.sep))
        src = ''
        if os.path.isfile(path):
            src = io.open(path, 'r', encoding='utf-8-sig').read()
        a = code.replace('\r\n', '\n').split('\n')
        b = src.replace('\r\n', '\n').split('\n') if src else []
        sim = difflib.SequenceMatcher(None, a, b).ratio() if b else 0.0
        accion = 'igual'
        if not src:
            accion = 'src inexistente'
        elif sim < 0.99999:
            accion = 'ACTUALIZAR'
        results.append((desc, rel, len(code), len(src), '{:.4f}'.format(sim), accion))
        print('{:<22} {:<46} {:>7} {:>7} {:>6} {}'.format(desc, rel, len(code), len(src), '-', accion) if False else
              '{:<22} {:<46} {:>7} {:>7} {:>6} {}'.format(desc, rel, len(code), len(src), '{:.4f}'.format(sim), accion))
        if do_write and (accion in ('ACTUALIZAR', 'src inexistente')):
            ts = time.strftime('%Y%m%d-%H%M%S')
            if os.path.isfile(path):
                shutil.copy2(path, path + '.bak-sync-' + ts)
            io.open(path, 'w', encoding='utf-8', newline='\n').write(code.replace('\r\n', '\n'))
            print('   -> escrito: {} (backup .bak-sync-{})'.format(rel, ts))

    print()
    print('resumen:')
    for r in results:
        print('  ', r)


if __name__ == '__main__':
    main()
