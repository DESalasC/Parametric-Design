# -*- coding: utf-8 -*-
"""Parchea los componentes F1_ETAPA2_LADOS (v06.5) y F1_ETAPA2_PATIO (v02.3)
embebidos en el canvas gh-definitions/F1_CONTEXTO_v11.ghx.

Reemplaza el CodeInput de cada componente por el codigo fuente actualizado:
  - F1_ETAPA2_LADOS_v06.py  -> hotfix point_in_lot + simplificacion 2.5 grados
  - F1_ETAPA2_PATIO_v02.py  -> garantias 9 m2 / claridad 3 m + dedup

Idempotente y con backup por timestamp. Tras correrlo, regenerar el .gh:
  pwsh -NoProfile -File scripts/utilities/ghx-to-gh.ps1 -InputGhx gh-definitions/F1_CONTEXTO_v11.ghx -OutputGh gh-definitions/F1_CONTEXTO_v11.gh

Uso:  python scripts/utilities/patch-ghx-lados065-patio023.py
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
    ("#81-F1_ETAPA2_LADOS_v06.py",
     os.path.join(BASE, "src", "fase-1-contexto", "F1_ETAPA2_LADOS_v06.py"),
     ("def point_in_lot", "LADOS v06.5", "simplificar_colineales")),
    ("#99-F1_ETAPA2_PATIO_v02.py",
     os.path.join(BASE, "src", "fase-1-contexto", "F1_ETAPA2_PATIO_v02.py"),
     ("CLARIDAD_MINIMA_M", "PATIO v02.3", "deduplicar_puntos")),
]


def _code_of(path):
    with io.open(path, "r", encoding="utf-8") as f:
        return f.read()


def main():
    ts = datetime.now().strftime("%Y-%m-%d-%H%M")
    backup = GHX + ".bak-" + ts
    shutil.copy2(GHX, backup)
    print("backup:", backup)

    tree = ET.parse(GHX)
    root = tree.getroot()

    patches = 0
    already = 0
    for nick, py_path, markers in TARGETS:
        nuevo = _code_of(py_path)
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
            already += 1
            continue

        viejo_len = len(actual)
        code_el.text = nuevo
        patches += 1
        print("{}: CodeInput {} -> {} chars (markers: {})".format(
            nick, viejo_len, len(nuevo), ", ".join(markers)))

    if patches == 0:
        print("Sin cambios (ya estaba todo parcheado).")
        return

    tree.write(GHX, xml_declaration=True, encoding="utf-8")
    print("escrito:", GHX)

    # validacion por re-lectura
    t2 = ET.parse(GHX)
    ok = {}
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
        ok[nick] = all(m in code for m in markers)
    for nick, res in ok.items():
        print("VALIDACION {}: {}".format(nick, "OK" if res else "FALLO"))
    if not all(ok.values()):
        sys.exit(1)


if __name__ == "__main__":
    main()
