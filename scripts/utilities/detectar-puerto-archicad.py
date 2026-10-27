# -*- coding: utf-8 -*-
"""Detecta en qué puerto escucha la JSON/Tapir API de ArchiCAD.

Contexto (2026-10-26): en la versión nueva de AutoClaw el puerto **19723 quedó
libre** para ArchiCAD; el 19724 ya no responde. Antes de lanzar el MCP (o
cualquier script de `src/interfases-archicad/`) conviene confirmar el puerto en
vez de asumirlo.

Uso:
    python scripts/utilities/detectar-puerto-archicad.py
    python scripts/utilities/detectar-puerto-archicad.py --json
    python scripts/utilities/detectar-puerto-archicad.py --puertos 19723,19724,19725

Salida: puerto detectado + versión de ArchiCAD. Código 0 si encontró la API,
1 si ningún puerto responde.
"""
from __future__ import print_function

import argparse
import json
import socket
import sys


def puerto_abierto(host, puerto, timeout=1.0):
    try:
        s = socket.create_connection((host, puerto), timeout=timeout)
        s.close()
        return True
    except Exception:
        return False


def probar_tapir(host, puerto):
    """(ok, detalle) usando el cliente oficial archicad (Tapir)."""
    try:
        from archicad import ACConnection
    except Exception as e:
        return False, "falta el paquete 'archicad' (%s)" % e
    try:
        try:
            conn = ACConnection(host=host, port=puerto)      # variantes nuevas
        except TypeError:
            conn = ACConnection(port=puerto)                 # Tapir 1.5.x (solo port)
        if not conn.commands.IsAlive():
            return False, "conexion abierta pero IsAlive=False"
        try:
            prod = conn.commands.GetProductInfo()
            detalle = "ArchiCAD %s build %s %s" % (prod[0], prod[1], prod[2])
        except Exception:
            detalle = "IsAlive OK (sin GetProductInfo)"
        return True, detalle
    except Exception as e:
        return False, "%s: %s" % (type(e).__name__, e)


def main():
    ap = argparse.ArgumentParser(description="Detecta el puerto de la API de ArchiCAD")
    ap.add_argument("--host", default="127.0.0.1")
    ap.add_argument("--puertos", default="19723,19724,19725")
    ap.add_argument("--json", action="store_true", help="salida JSON (para el orquestador)")
    args = ap.parse_args()

    puertos = [int(p) for p in args.puertos.split(",") if p.strip()]
    resultados = []
    detectado = None
    for p in puertos:
        if not puerto_abierto(args.host, p):
            resultados.append({"puerto": p, "estado": "cerrado"})
            continue
        ok, detalle = probar_tapir(args.host, p)
        resultados.append({"puerto": p, "estado": "tapir" if ok else "abierto_sin_tapir",
                           "detalle": detalle})
        if ok and detectado is None:
            detectado = p

    if args.json:
        print(json.dumps({"host": args.host, "puerto": detectado, "resultados": resultados},
                         ensure_ascii=False))
    else:
        for r in resultados:
            if r["estado"] == "cerrado":
                print("  %d  cerrado" % r["puerto"])
            else:
                print("  %d  %s%s" % (r["puerto"], r["estado"],
                                      ("  (%s)" % r["detalle"]) if r.get("detalle") else ""))
        if detectado:
            print("\nAPI de ArchiCAD en el puerto %d" % detectado)
        else:
            print("\nNo hay API de ArchiCAD escuchando en %s" % args.puertos)
    return 0 if detectado else 1


if __name__ == "__main__":
    sys.exit(main())
