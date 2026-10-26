# -*- coding: utf-8 -*-
"""Verifica paridad entre el canvas .ghx y los scripts de src/.

Uso:
    python scripts/utilities/verificar-paridad-canvas-src.py
    python scripts/utilities/verificar-paridad-canvas-src.py --ghx gh-definitions/F1_CONTEXTO_v13.6.ghx

Compara linea por linea (ignorando lineas vacias y CR/LF) el CodeInput de cada
componente GHPython contra el archivo vigente de src. Devuelve codigo 1 si hay
diferencias: el canvas es el artefacto vivo y src debe reflejarlo, no al revés.
"""
from __future__ import print_function

import argparse
import difflib
import io
import os
import sys
import xml.etree.ElementTree as ET

RAIZ = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))

TARGETS = {
    "ad270c61": ("F1_CONTEXTO50_BUILD", os.path.join(RAIZ, "src", "fase-1-contexto", "F1_CONTEXTO50_BUILD_v01.2.py")),
    "0d986a36": ("F1_ETAPA1_CONTEXTO", os.path.join(RAIZ, "src", "fase-1-contexto", "F1_ETAPA1_CONTEXTO_v02.py")),
    "03edc848": ("F1_ETAPA2_LADOS", os.path.join(RAIZ, "src", "fase-1-contexto", "F1_ETAPA2_LADOS_v06.py")),
    "d3bed17b": ("F1_ETAPA2_PATIO", os.path.join(RAIZ, "src", "fase-1-contexto", "F1_ETAPA2_PATIO_v03.py")),
    "d4aab682": ("F1_ETAPA2_NORMATIVA", os.path.join(RAIZ, "src", "fase-1-contexto", "F1_ETAPA2_NORMATIVA_v09.1.py")),
    "6eaf2956": ("F3_DISTRIBUCION", os.path.join(RAIZ, "src", "fase-3-masa", "F3_DISTRIBUCION_v03.py")),
    "8c7e8133": ("F3_VOLUM_GENERADOR", os.path.join(RAIZ, "src", "fase-3-masa", "F3_VOLUM_GENERADOR_v08.py")),
}


def limpiar(texto):
    texto = texto.replace("\r\n", "\n").replace("\r", "\n")
    return [l.rstrip() for l in texto.split("\n") if l.strip()]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ghx", default=os.path.join(RAIZ, "gh-definitions", "F1_CONTEXTO_v13.6.ghx"))
    ap.add_argument("--detalle", type=int, default=10)
    args = ap.parse_args()

    root = ET.parse(args.ghx).getroot()
    embebidos = {}
    for o in root.iter("chunk"):
        if o.get("name") != "Object":
            continue
        d = {}
        for w in o.iter("item"):
            d.setdefault(w.get("name"), []).append(w.text or "")
        g = (d.get("InstanceGuid") or [""])[0].strip().lower()
        code = (d.get("CodeInput") or [""])[0]
        if g and code:
            embebidos[g] = ((d.get("NickName") or [""])[0], code)

    print("canvas: %s" % os.path.basename(args.ghx))
    print("%-22s %-34s %s" % ("componente", "archivo src", "resultado"))
    fallos = 0
    for gid, (etiqueta, ruta) in TARGETS.items():
        hit = [(g, v) for g, v in embebidos.items() if g.startswith(gid)]
        if not hit:
            print("%-22s %-34s SIN COMPONENTE" % (etiqueta, os.path.basename(ruta)))
            fallos += 1
            continue
        nick, code = hit[0][1]
        if not os.path.isfile(ruta):
            print("%-22s %-34s SIN ARCHIVO" % (etiqueta, os.path.basename(ruta)))
            fallos += 1
            continue
        src = io.open(ruta, encoding="utf-8-sig").read()
        a, b = limpiar(src), limpiar(code)
        if a == b:
            print("%-22s %-34s IGUAL" % (nick[:22], os.path.basename(ruta)))
            continue
        fallos += 1
        dl = [l for l in difflib.unified_diff(a, b, lineterm="", n=0)
              if l[:1] in "+-" and not l.startswith(("+++", "---"))]
        print("%-22s %-34s %d lineas dif" % (nick[:22], os.path.basename(ruta), len(dl)))
        for l in dl[:args.detalle]:
            print("      %s" % l[:150])

    print("\n%d/%d componentes con paridad" % (len(TARGETS) - fallos, len(TARGETS)))
    return 1 if fallos else 0


if __name__ == "__main__":
    sys.exit(main())
