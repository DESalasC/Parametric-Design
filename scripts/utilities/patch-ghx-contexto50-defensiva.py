# -*- coding: utf-8 -*-
"""Parchea el componente F1_CONTEXTO50_BUILD (fix v01c: resolución defensiva
del template case-insensitive + f[:-14]) embebido en gh-definitions/F1_CONTEXTO_v11.ghx.

El CodeInput del componente #49 se sincroniza con el contenido completo del
archivo fuente src/fase-1-contexto/F1_CONTEXTO50_BUILD_v01b.py.
Idempotente, con backup por timestamp. Tras correrlo, regenerar el .gh:
  pwsh -NoProfile -File scripts/utilities/ghx-to-gh.ps1 -InputGhx gh-definitions/F1_CONTEXTO_v11.ghx -OutputGh gh-definitions/F1_CONTEXTO_v11.gh

Uso:  python scripts/utilities/patch-ghx-contexto50-defensiva.py
"""
import io
import os
import shutil
import sys
import xml.etree.ElementTree as ET
from datetime import datetime

BASE = r"D:\Work\PROJECTS\DiseñoParametrico"
GHX = os.path.join(BASE, "gh-definitions", "F1_CONTEXTO_v11.ghx")

TARGETS = [
    ("#49-F1_CONTEXTO50_BUILD_v01b.py",
     os.path.join(BASE, "src", "fase-1-contexto", "F1_CONTEXTO50_BUILD_v01b.py"),
     ('"chip-contexto50.json" in in_json_path.lower()', "f[:-14]")),
]


def main():
    ts = datetime.now().strftime("%Y-%m-%d-%H%M")
    backup = GHX + ".bak-" + ts
    shutil.copy2(GHX, backup)
    print("backup:", backup)

    tree = ET.parse(GHX)
    root = tree.getroot()
    patches = 0

    for nick, py_path, markers in TARGETS:
        with io.open(py_path, "r", encoding="utf-8") as f:
            nuevo = f.read()
        target_obj = None
        for obj in root.iter():
            if obj.get("name") != "Object":
                continue
            for child in obj.iter():
                if child.get("name") == "NickName" and (child.text or "").strip() == nick:
                    target_obj = obj
                    break
            if target_obj is not None:
                break
        if target_obj is None:
            print("ERROR: no se encontro el componente '{}'".format(nick))
            sys.exit(1)
        code_el = None
        for el in target_obj.iter():
            if el.get("name") == "CodeInput" and el.text and len(el.text) > 1000:
                code_el = el
                break
        if code_el is None:
            print("ERROR: sin CodeInput en '{}'".format(nick))
            sys.exit(1)
        actual = code_el.text or ""
        if all(m in actual for m in markers):
            print("{}: ya parcheado (idempotente)".format(nick))
            continue
        viejo_len = len(actual)
        code_el.text = nuevo
        patches += 1
        print("{}: CodeInput {} -> {} chars".format(nick, viejo_len, len(nuevo)))

    if patches == 0:
        print("Sin cambios (ya estaba parcheado).")
        return
    tree.write(GHX, xml_declaration=True, encoding="utf-8")
    print("escrito:", GHX)

    t2 = ET.parse(GHX)
    ok = True
    for nick, py_path, markers in TARGETS:
        found = None
        for obj in t2.getroot().iter():
            if obj.get("name") != "Object":
                continue
            for child in obj.iter():
                if child.get("name") == "NickName" and (child.text or "").strip() == nick:
                    found = obj
                    break
            if found is not None:
                break
        code = ""
        if found is not None:
            for el in found.iter():
                if el.get("name") == "CodeInput" and el.text and len(el.text) > 1000:
                    code = el.text
                    break
        res = all(m in code for m in markers)
        ok = ok and res
        print("VALIDACION {}: {}".format(nick, "OK" if res else "FALLO"))
    if not ok:
        sys.exit(1)


if __name__ == "__main__":
    main()
