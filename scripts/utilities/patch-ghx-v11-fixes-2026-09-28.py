# -*- coding: utf-8 -*-
"""Parchea el canvas F1_CONTEXTO_v11 con los fixes de la noche 2026-09-28:

  1) #21  (guid 0d986a36-a41a-429c-8f29-9e2658659e25): CodeInput <-
     src/fase-1-contexto/F1_ETAPA1_CONTEXTO_v04.2.py  (copia canvas-fiel con las
     curvas aplanadas a plano horizontal para la Live Connection).
  2) #113 (guid d4aab682-ad94-40e9-a5b5-eaf20b3350c7): CodeInput <-
     src/fase-1-contexto/F1_ETAPA2_NORMATIVA_v08.py  (restaura la cadena
     envelope/GFA; el componente tenia el contrato de NORMATIVA con codigo de
     ETAPA1).
  3) #48  (guid ad270c61-3268-4dcc-b9e8-dd6e9711f5c8): CodeInput <-
     src/fase-1-contexto/F1_CONTEXTO50_BUILD_v01b.py  (v01d: z_base_m).
  4) Re-cablea #125 input 'io_maximo' (chunk cb180da5-4884-4861-9c9f-a5a74020ed62):
     Source ic_maximo (fb3641a4-...) -> io_maximo (86d781d0-8e25-43ab-9a29-09722103c52f).

Anclado por GUID: la numeracion #NN del canvas es VOLATIL (la asigna el
"Escaner y Etiquetador Dinamico" por posicion; cambia entre corridas).

Idempotente, con backup por timestamp. Tras correrlo, regenerar el .gh:
  pwsh -NoProfile -File scripts/utilities/ghx-to-gh.ps1 -InputGhx gh-definitions/F1_CONTEXTO_v11.ghx -OutputGh gh-definitions/F1_CONTEXTO_v11.gh

Uso:  python scripts/utilities/patch-ghx-v11-fixes-2026-09-28.py
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
    ("#21-ETAPA1", "0d986a36-a41a-429c-8f29-9e2658659e25",
     os.path.join(BASE, "src", "fase-1-contexto", "F1_ETAPA1_CONTEXTO_v04.2.py"),
     ("CAMBIO v04.2", "Live Connection")),
    ("#113-NORMATIVA", "d4aab682-ad94-40e9-a5b5-eaf20b3350c7",
     os.path.join(BASE, "src", "fase-1-contexto", "F1_ETAPA2_NORMATIVA_v08.py"),
     ("NORMATIVA v08", "RANGO_PISOS")),
    ("#48-CONTEXTO50_BUILD", "ad270c61-3268-4dcc-b9e8-dd6e9711f5c8",
     os.path.join(BASE, "src", "fase-1-contexto", "F1_CONTEXTO50_BUILD_v01b.py"),
     ("v01d", "z_base_m")),
]

REWIRES = [
    ("#125.io_maximo", "cb180da5-4884-4861-9c9f-a5a74020ed62",
     "86d781d0-8e25-43ab-9a29-09722103c52f"),
]


def own(el, field):
    its = el.find("items")
    if its is None:
        return ""
    for it in its:
        if it.get("name") == field and it.text:
            return it.text.strip()
    return ""


def find_container(root, guid):
    for el in root.iter():
        if el.tag == "chunk" and el.get("name") == "Container" and own(el, "InstanceGuid") == guid:
            return el
    return None


def find_input_chunk(root, guid):
    for el in root.iter():
        if el.tag == "chunk" and el.get("name") in ("param_input", "InputParam"):
            for d in el.iter():
                if d.get("name") == "InstanceGuid" and d.text and d.text.strip() == guid:
                    return el
    return None


def main():
    ts = datetime.now().strftime("%Y-%m-%d-%H%M")
    backup = GHX + ".bak-" + ts
    shutil.copy2(GHX, backup)
    print("backup:", backup)

    tree = ET.parse(GHX)
    root = tree.getroot()
    patches = 0

    for label, guid, py_path, markers in TARGETS:
        cont = find_container(root, guid)
        if cont is None:
            print("ERROR: no se encontro el componente {0} ({1})".format(label, guid))
            sys.exit(1)
        code_el = None
        for el in cont.iter():
            if el.get("name") == "CodeInput" and el.text and len(el.text) > 1000:
                code_el = el
                break
        if code_el is None:
            print("ERROR: sin CodeInput en {0}".format(label))
            sys.exit(1)
        with io.open(py_path, "r", encoding="utf-8") as f:
            nuevo = f.read()
        actual = code_el.text or ""
        if all(m in actual for m in markers):
            print("{0}: ya parcheado (idempotente)".format(label))
            continue
        code_el.text = nuevo
        patches += 1
        print("{0}: CodeInput {1} -> {2} chars".format(label, len(actual), len(nuevo)))

    for label, chunk_guid, new_src in REWIRES:
        ch = find_input_chunk(root, chunk_guid)
        if ch is None:
            print("ERROR: no se encontro el input {0}".format(label))
            sys.exit(1)
        done = False
        for d in ch.iter():
            if d.get("name") == "Source" and d.text:
                if d.text.strip() == new_src:
                    print("{0}: ya re-cableado (idempotente)".format(label))
                else:
                    print("{0}: Source ...{1} -> ...{2}".format(
                        label, d.text.strip()[-12:], new_src[-12:]))
                    d.text = new_src
                    patches += 1
                done = True
                break
        if not done:
            print("ERROR: sin item Source en {0}".format(label))
            sys.exit(1)

    if patches == 0:
        print("Sin cambios (ya estaba todo parcheado).")
        return

    tree.write(GHX, xml_declaration=True, encoding="utf-8")
    print("escrito:", GHX)

    # Validacion
    tree2 = ET.parse(GHX)
    root2 = tree2.getroot()
    ok = True
    for label, guid, py_path, markers in TARGETS:
        cont = find_container(root2, guid)
        code = ""
        if cont is not None:
            for el in cont.iter():
                if el.get("name") == "CodeInput" and el.text and len(el.text) > 1000:
                    code = el.text
                    break
        res = all(m in code for m in markers)
        ok = ok and res
        print("VALIDACION {0}: {1}".format(label, "OK" if res else "FALLO"))
    for label, chunk_guid, new_src in REWIRES:
        ch = find_input_chunk(root2, chunk_guid)
        res = False
        if ch is not None:
            for d in ch.iter():
                if d.get("name") == "Source" and d.text and d.text.strip() == new_src:
                    res = True
                    break
        ok = ok and res
        print("VALIDACION {0}: {1}".format(label, "OK" if res else "FALLO"))
    if not ok:
        sys.exit(1)


if __name__ == "__main__":
    main()
