#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fetch-contexto-completo.py  — Orquestador unificado de Contexto (Fase 1)
======================================================================
Proyecto: DiseñoParametrico
Propósito: Ejecuta en secuencia los dos pasos necesarios para obtener
           tanto el contexto base como el contexto 50 m (volumetrías
           de vecinos) en una sola invocación.

PASO 1: fetch-urban-context-v6.py
  → genera data/pot-cache/<CHIP>-contexto.json
  → lote, vecinos (linderos), vías oficiales, espacios públicos, POT, topografía

PASO 2: F1_CONTEXTO50_FETCH_v01.py
  → lee el JSON del Paso 1 (--ctx) para conocer marco local y ancla
  → extrae construcciones de bd_uaecd.gpkg#Cons en radio 50 m
  → genera data/pot-cache/<CHIP>-contexto50.json + .geojson

USO (desde la raíz del proyecto o vía orquestador):
  python scripts/utilities/fetch-contexto-completo.py --chip AAA0240ZXJH
  python scripts/utilities/fetch-contexto-completo.py --chip AAA0240ZXJH --radio 75 --out data/pot-cache
"""

import argparse
import os
import sys
import subprocess


def run_step(cmd, cwd, label):
    """Ejecuta un subcomando y propaga el código de salida."""
    print(f"\n{'='*60}")
    print(f"▶ {label}")
    print(f"   Comando: {' '.join(cmd)}")
    print(f"{'='*60}")
    result = subprocess.run(cmd, cwd=cwd)
    if result.returncode != 0:
        print(f"\n❌ FALLO en {label} (código {result.returncode})")
    else:
        print(f"\n✅ OK: {label}")
    return result.returncode


def main():
    parser = argparse.ArgumentParser(
        description="Orquestador unificado: contexto base + contexto 50m"
    )
    parser.add_argument("--chip", required=True, help="CHIP del predio objetivo")
    parser.add_argument(
        "--radio", type=float, default=50.0, help="Radio en metros para contexto50 (default: 50)"
    )
    parser.add_argument(
        "--altura-piso", type=float, default=3.80, help="Altura por piso en metros (default: 3.80)"
    )
    parser.add_argument(
        "--out", default="data/pot-cache", help="Carpeta de salida (default: data/pot-cache)"
    )
    parser.add_argument(
        "--fuente", choices=["gpkg", "rest"], default="gpkg", help="Fuente para contexto50 (default: gpkg)"
    )
    parser.add_argument(
        "--marco", choices=["canvas", "json"], default="canvas", help="Marco de salida contexto50 (default: canvas)"
    )
    parser.add_argument(
        "--solo-base", action="store_true", help="Solo ejecutar Paso 1 (contexto base)"
    )
    parser.add_argument(
        "--solo-50", action="store_true", help="Solo ejecutar Paso 2 (requiere CHIP-contexto.json previo)"
    )
    args = parser.parse_args()

    project_root = os.environ.get("DISENO_PARAMETRICO_ROOT", os.getcwd())
    out_dir_abs = os.path.join(project_root, args.out) if not os.path.isabs(args.out) else args.out

    # Rutas a los scripts
    script_base = os.path.join(project_root, "scripts", "utilities", "fetch-urban-context-v6.py")
    script_50 = os.path.join(project_root, "src", "fase-1-contexto", "F1_CONTEXTO50_FETCH_v01.py")

    # Verificar que existen
    for s, name in [(script_base, "fetch-urban-context-v6.py"), (script_50, "F1_CONTEXTO50_FETCH_v01.py")]:
        if not os.path.exists(s):
            print(f"ERROR: No se encuentra {name} en {s}")
            return 1

    # Archivo de contexto base que generará el Paso 1
    ctx_base = os.path.join(out_dir_abs, f"{args.chip}-contexto.json")

    # ── PASO 1: Contexto base ──────────────────────────────────────────────
    if not args.solo_50:
        cmd1 = [
            sys.executable, script_base,
            "--chip", args.chip,
            "--output-dir", out_dir_abs,
        ]
        rc = run_step(cmd1, project_root, "PASO 1: fetch-urban-context-v6 (contexto base)")
        if rc != 0:
            return rc

    # ── PASO 2: Contexto 50m ───────────────────────────────────────────────
    if not args.solo_base:
        if not os.path.exists(ctx_base):
            print(f"\n❌ ERROR: No existe el contexto base requerido: {ctx_base}")
            print("   Ejecuta primero sin --solo-50 o genera el contexto base por separado.")
            return 1

        cmd2 = [
            sys.executable, script_50,
            "--chip", args.chip,
            "--radio", str(args.radio),
            "--altura-piso", str(args.altura_piso),
            "--ctx", ctx_base,
            "--out", out_dir_abs,
            "--fuente", args.fuente,
            "--marco", args.marco,
        ]
        rc = run_step(cmd2, project_root, "PASO 2: F1_CONTEXTO50_FETCH_v01 (contexto 50m)")
        if rc != 0:
            return rc

    print(f"\n{'='*60}")
    print(f"🎯 CONTEXTO COMPLETO GENERADO para CHIP {args.chip}")
    print(f"   📁 {ctx_base}")
    print(f"   📁 {os.path.join(out_dir_abs, f'{args.chip}-contexto50.json')}")
    print(f"   📁 {os.path.join(out_dir_abs, f'{args.chip}-contexto50.geojson')}")
    print(f"{'='*60}")
    return 0


if __name__ == "__main__":
    sys.exit(main())