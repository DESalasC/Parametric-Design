#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
verificar-gfa.py — Chequeo post-run del GFA exportado por F1_EXPORTAR_GFA_v02.

Lee data/fase-2-demanda/<CHIP>-gfa-gh.json y valida pisos, huella, IO y GFA
contra los valores esperados del override de norma (Muzu 41 / AAA0240ZXJH).

Uso:
  .venv\\Scripts\\python.exe scripts\\utilities\\verificar-gfa.py
  .venv\\Scripts\\python.exe scripts\\utilities\\verificar-gfa.py --chip AAA0240ZXJH
"""
import argparse
import io
import json
import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


def _json(ruta):
    with io.open(ruta, "r", encoding="utf-8") as f:
        return json.load(f)


def main():
    ap = argparse.ArgumentParser(description="Verifica el GFA exportado por el canvas F1.")
    ap.add_argument("--chip", default="AAA0240ZXJH")
    ap.add_argument("--pisos", type=int, default=4, help="pisos esperados")
    ap.add_argument("--io", type=float, default=0.70, help="IO normativo esperado")
    ap.add_argument("--huella-min", type=float, default=55.0, help="huella minima (m2)")
    ap.add_argument("--huella-max", type=float, default=78.0, help="huella maxima (m2)")
    args = ap.parse_args()

    ruta = os.path.join(ROOT, "data", "fase-2-demanda", args.chip + "-gfa-gh.json")
    if not os.path.exists(ruta):
        print("NO HAY ARCHIVO: %s" % ruta)
        print("  -> corre el canvas F1 (EXPORTAR_GFA_v02) y reintenta.")
        sys.exit(2)

    d = _json(ruta)
    fallos = []

    def check(nombre, ok, detalle):
        print("[%s] %-24s %s" % ("OK " if ok else "FAIL", nombre, detalle))
        if not ok:
            fallos.append(nombre)

    valido = d.get("valido")
    check("valido", valido is True, "valido=%r" % valido)

    pisos = d.get("pisos_finales")
    check("pisos_finales", pisos == args.pisos, "esperado=%d, real=%s" % (args.pisos, pisos))

    io = d.get("io_maximo")
    ok_io = (io is not None) and abs(float(io) - args.io) < 0.001
    check("io_maximo", ok_io,
          "esperado=%.2f, real=%s%s" % (args.io, io,
          "  <-- cableado: conecta io_maximo (NO ic_maximo) en EXPORTAR_GFA" if not ok_io else ""))

    huella = d.get("ocupacion_real")
    if isinstance(huella, (int, float)):
        ok_huella = args.huella_min <= huella <= args.huella_max
        check("ocupacion (huella)", ok_huella,
              "real=%.1f m2 (esperado ~64.5, rango %.0f-%.0f)" % (huella, args.huella_min, args.huella_max))
        if not ok_huella and abs(huella - 46.3) < 2:
            print("      -> huella ~46.3 = LADOS con 2 frontales (conexion GH<->ArchiCAD). Reabre Live Connection.")
    else:
        check("ocupacion (huella)", False, "real=%r" % huella)

    gfa = d.get("gfa_total_m2")
    if isinstance(gfa, (int, float)) and isinstance(huella, (int, float)) and huella > 0:
        ratio = gfa / huella
        check("gfa_total_m2", 3.0 <= ratio <= 4.8,
              "real=%.1f m2 (%.2fx huella; esperado ~4x)" % (gfa, ratio))

    ctx = os.path.join(ROOT, "data", "pot-cache", args.chip + "-contexto.json")
    if os.path.exists(ctx):
        c = _json(ctx).get("pot_data", {})
        rango = c.get("rango_edificabilidad")
        check("contexto.rango", rango == "3", "rango=%r (esperado '3' -> 4 pisos)" % rango)
        aj = c.get("antejardin_m")
        check("contexto.antejardin", aj == 3.5, "antejardin=%r (esperado 3.5)" % aj)
    else:
        print("[WARN] sin contexto: %s" % ctx)

    print("-" * 64)
    if fallos:
        print("RESULTADO: %d chequeo(s) FALLARON -> %s" % (len(fallos), ", ".join(fallos)))
        sys.exit(1)
    print("RESULTADO: todo OK. GFA listo para F2.")


if __name__ == "__main__":
    main()
