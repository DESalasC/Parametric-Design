# -*- coding: utf-8 -*-
"""Parchea F1_CONTEXTO_v11 con el blindaje de codificacion (P0, 2026-09-29).

Reemplaza el CodeInput de los componentes que leen/escriben JSON por las
versiones endurecidas (lector canonico utf-8 estricto -> cp1252 -> latin-1;
escritura ASCII-safe) y actualiza sus NickName a la version vigente.

  #21 <- src/fase-1-contexto/F1_ETAPA1_CONTEXTO_v04.3.py    (LECTOR CANONICO, v04.3)
  #48 <- src/fase-1-contexto/F1_CONTEXTO50_BUILD_v01e.py   (_leer_json_canonico, v01e)
  #99 <- src/fase-1-contexto/F1_ETAPA2_PATIO_v02.py        (_decodificar_cascada, v02.5)
  #89 <- src/orquestador/F0_LOAD_PROYECTO_v01.py           (_leer_json_canonico, v01.5)
  #10 <- src/fase-1-contexto/F1_EXPORTAR_GFA_v02.3.py      (_decodificar_cascada, v02.3)

Anclado por PREFIJO de NickName (la numeracion #NN es volatil; los GUIDs de
instancia no cambian: solo se toca CodeInput/NickName). Idempotente, con
backup por timestamp. Tras correrlo, regenerar el .gh:

  pwsh -NoProfile -File scripts/utilities/ghx-to-gh.ps1 `
    -InputGhx gh-definitions/F1_CONTEXTO_v11.ghx -OutputGh gh-definitions/F1_CONTEXTO_v11.gh
"""
import io
import os
import shutil
import sys
import xml.etree.ElementTree as ET
from datetime import datetime

BASE = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
GHX = os.path.join(BASE, "gh-definitions", "F1_CONTEXTO_v11.ghx")

TARGETS = [
    ("#21-", "src/fase-1-contexto/F1_ETAPA1_CONTEXTO_v04.3.py",
     "#21-F1_ETAPA1_CONTEXTO_v04.3.py", ["LECTOR CANONICO", "v04.3"], None),
    ("#48-", "src/fase-1-contexto/F1_CONTEXTO50_BUILD_v01e.py",
     "#48-F1_CONTEXTO50_BUILD_v01e.py", ["_leer_json_canonico", "v01e"], None),
    ("#99-", "src/fase-1-contexto/F1_ETAPA2_PATIO_v02.py",
     "#99-F1_ETAPA2_PATIO_v02.py", ["_decodificar_cascada", "v02.5"], None),
    ("#89-", "src/orquestador/F0_LOAD_PROYECTO_v01.py",
     "#89-F0_LOAD_PROYECTO_v01.py", ["_leer_json_canonico", "v01.5"], None),
    ("#10-", "src/fase-1-contexto/F1_EXPORTAR_GFA_v02.3.py",
     "#10-F1_EXPORTAR_GFA_v02.3.py", ["_decodificar_cascada", "v02.3"], "derivar_chip"),
]


def find_objects(root, prefix, code_match=None):
    hits = []
    for o in root.iter('chunk'):
        if o.get('name') != 'Object':
            continue
        nick = ''
        code = ''
        for i in o.iter('item'):
            n = i.get('name')
            if n == 'NickName' and i.text and not nick:
                nick = i.text.strip()
            if n == 'CodeInput' and i.text:
                code = i.text
        if not code:
            continue
        if nick.startswith(prefix) or (code_match and code_match in code):
            hits.append((o, nick))
    return hits


def own_item(obj, name, value=None):
    for i in obj.iter('item'):
        if i.get('name') == name:
            if value is not None:
                i.text = value
            return i
    return None


def main():
    tree = ET.parse(GHX)
    root = tree.getroot()
    patched = 0
    for prefix, rel, newnick, markers, code_match in TARGETS:
        hits = find_objects(root, prefix, code_match)
        if len(hits) != 1:
            print("ERROR: prefijo {0} (code_match={1}) -> {2} coincidencias".format(prefix, code_match, len(hits)))
            sys.exit(1)
        obj, nick = hits[0]
        src_path = os.path.join(BASE, rel.replace("/", os.sep))
        with io.open(src_path, "r", encoding="utf-8") as f:
            code = f.read()
        it = own_item(obj, 'CodeInput')
        if it is None:
            print("ERROR: sin CodeInput en {0}".format(nick))
            sys.exit(1)
        if all(m in (it.text or "") for m in markers):
            print("{0}: ya parcheado (idempotente)".format(nick))
        else:
            it.text = code
            own_item(obj, 'NickName', newnick)
            patched += 1
            print("{0} -> {1} ({2} chars)".format(nick, newnick, len(code)))

    if patched == 0:
        print("Sin cambios.")
        return

    ts = datetime.now().strftime("%Y%m%d-%H%M%S")
    bak = GHX + ".bak-" + ts
    shutil.copy2(GHX, bak)
    print("backup:", bak)
    data = ET.tostring(root, encoding="utf-8", xml_declaration=True)
    with open(GHX, "wb") as f:
        f.write(b"\xef\xbb\xbf" + data)
    print("escrito:", GHX)

    root2 = ET.parse(GHX).getroot()
    ok = True
    for prefix, rel, newnick, markers, code_match in TARGETS:
        hits = find_objects(root2, prefix, code_match)
        if len(hits) != 1:
            ok = False
            print("VALIDACION {0}: FALLO (no encuentra)".format(newnick))
            continue
        obj, nick = hits[0]
        it = own_item(obj, 'CodeInput')
        code = it.text or ""
        res = all(m in code for m in markers) and nick == newnick
        ok = ok and res
        print("VALIDACION {0}: {1}".format(newnick, "OK" if res else "FALLO"))
    if not ok:
        sys.exit(1)


if __name__ == "__main__":
    main()
