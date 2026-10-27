# -*- coding: utf-8 -*-
"""Sincroniza el CodeInput de los componentes del canvas con los scripts de src/.

El canvas (.ghx) es el artefacto vivo: este script escribe en el .ghx el codigo
vigente de src/ SOLO para los componentes cuyo texto difiere (ignorando lineas
vacias y el fin de linea), usando el mismo mapa de componentes que
`verificar-paridad-canvas-src.py`. Escribe el <item CodeInput> in situ, sin
reserializar el XML: el resto del archivo queda byte a byte igual.

Uso:
    python scripts/utilities/sincronizar-codeinput-ghx.py --dry-run
    python scripts/utilities/sincronizar-codeinput-ghx.py
    python scripts/utilities/sincronizar-codeinput-ghx.py --ghx gh-definitions/F1_CONTEXTO_v13.6.ghx

Despues de escribir: cerrar y reabrir el .ghx en Grasshopper (o File > Open) para
que el componente ejecute el codigo nuevo. Verificar con:
    python scripts/utilities/verificar-paridad-canvas-src.py
"""
from __future__ import print_function

import argparse
import importlib.util
import io
import os
import re
import shutil
import sys
import time
import xml.etree.ElementTree as ET
from xml.sax.saxutils import escape

RAIZ = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
PARIDAD = os.path.join(RAIZ, "scripts", "utilities", "verificar-paridad-canvas-src.py")


def cargar_targets():
    """Reutiliza el mapa guid -> (nombre, archivo src) del verificador de paridad."""
    spec = importlib.util.spec_from_file_location("verificar_paridad", PARIDAD)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.TARGETS


def norm_lineas(texto):
    texto = texto.replace("\r\n", "\n").replace("\r", "\n")
    return [l.rstrip() for l in texto.split("\n") if l.strip()]


def desescapar(texto):
    return (texto.replace("&lt;", "<").replace("&gt;", ">")
            .replace("&quot;", '"').replace("&apos;", "'").replace("&amp;", "&"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ghx", default=os.path.join(RAIZ, "gh-definitions", "F1_CONTEXTO_v13.6.ghx"))
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    with io.open(args.ghx, "r", encoding="utf-8", newline="") as f:
        texto = f.read()
    if not texto:
        print("[ERROR] .ghx vacio")
        return 2
    nl = "\r\n" if "\r\n" in texto else "\n"

    targets = cargar_targets()
    cambios = []
    sin_componente = []

    for guid, (etiqueta, ruta_src) in targets.items():
        if not os.path.isfile(ruta_src):
            print("[AVISO] sin archivo src: %s" % ruta_src)
            continue
        pos = None
        for m in re.finditer(r'<item name="InstanceGuid" type_name="gh_guid" type_code="9">', texto):
            fin = texto.find("</item>", m.end())
            if texto[m.end():fin].strip().lower().startswith(guid):
                pos = m.start()
                break
        if pos is None:
            sin_componente.append(etiqueta)
            continue

        ini = texto.rfind('<chunk name="Object"', 0, pos)
        fin_obj = texto.find('<chunk name="Object"', pos)
        if fin_obj < 0:
            fin_obj = len(texto)
        sub = texto[ini:fin_obj]
        m_ci = re.search(r'<item name="CodeInput"[^>]*>', sub)
        if not m_ci:
            sin_componente.append(etiqueta + " (sin CodeInput)")
            continue
        ini_ci = ini + m_ci.end()
        fin_ci = texto.find("</item>", ini_ci)

        cuerpo = texto[ini_ci:fin_ci]
        with io.open(ruta_src, "r", encoding="utf-8", newline="") as f:
            src = f.read()
        if norm_lineas(desescapar(cuerpo)) == norm_lineas(src):
            continue
        nuevo = escape(src.replace("\r\n", "\n").replace("\r", "\n")).replace("\n", nl)
        cambios.append((etiqueta, os.path.basename(ruta_src), len(cuerpo), len(nuevo), ini_ci, fin_ci, nuevo))

    if sin_componente:
        for e in sin_componente:
            print("[AVISO] componente no encontrado en el .ghx: %s" % e)
    if not cambios:
        print("Sin cambios: los %d componentes ya coinciden con src/." % len(targets))
        return 0

    print("%-34s %-32s %s" % ("componente", "archivo src", "bytes"))
    for etiqueta, archivo, n0, n1, _, _, _ in cambios:
        print("%-34s %-32s %d -> %d" % (etiqueta[:34], archivo[:32], n0, n1))
    if args.dry_run:
        print("\n[dry-run] no se escribe el .ghx")
        return 0

    backup_dir = os.path.join(RAIZ, "gh-definitions", "backups")
    if not os.path.isdir(backup_dir):
        os.makedirs(backup_dir)
    sello = time.strftime("%Y%m%d-%H%M%S")
    backup = os.path.join(backup_dir, os.path.basename(args.ghx) + ".bak-" + sello)
    shutil.copy2(args.ghx, backup)
    print("\nBackup: %s" % backup)

    # De atras hacia adelante para no desplazar los offsets ya calculados.
    for _, _, _, _, ini_ci, fin_ci, nuevo in sorted(cambios, key=lambda c: c[4], reverse=True):
        texto = texto[:ini_ci] + nuevo + texto[fin_ci:]

    with io.open(args.ghx, "w", encoding="utf-8", newline="") as f:
        f.write(texto)

    try:
        ET.parse(args.ghx)
    except Exception as e:
        shutil.copy2(backup, args.ghx)
        print("[ERROR] el .ghx quedo mal formado (%s). Restaurado desde el backup." % e)
        return 3

    print("\n%d componente(s) actualizados. Reabre el .ghx en Grasshopper." % len(cambios))
    return 0


if __name__ == "__main__":
    sys.exit(main())
