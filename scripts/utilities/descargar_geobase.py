#!/usr/bin/env python3
"""Descarga las geobases base del proyecto DisenoParametrico desde Datos Abiertos Bogota.

  * Catastro  : bd_uaecd.gpkg   -> dataset "Base de Datos Catastral para Bogota D.C."
  * POT       : POT_Decreto_555_2021_Bogota_D_C.gdb -> dataset "POT- Decreto 555 de 2021"

Uso:
    python scripts/utilities/descargar_geobase.py --catastro    # bd_uaecd.gpkg (22 capas)
    python scripts/utilities/descargar_geobase.py --pot         # geodatabase POT (166 capas)
    python scripts/utilities/descargar_geobase.py --catastro2026  # GPKG "Version Actual" (single-layer Cons)
    python scripts/utilities/descargar_geobase.py --all         # ambas geobases
    python scripts/utilities/descargar_geobase.py --list        # lista recursos del dataset de catastro

Salidas por defecto en data/geobase/. Descarga con reanudacion (-C -) via curl.
"""
import argparse
import json
import os
import subprocess
import sys
import urllib.request
import zipfile

CATASTRO_ID = "base-de-datos-catastral-para-bogota-d-c"
POT_ID = "pot-decreto-555-de-2021-bogota-d-c"
CKAN = "https://datosabiertos.bogota.gov.co/api/3/action/package_show?id="
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT_DIR = os.path.join(ROOT, "data", "geobase")

# recursos directos (verificados 2026-09-27)
URL_CATASTRO_MULTI = ("https://datosabiertos.bogota.gov.co/dataset/"
                      "e4f2dba4-d0a1-4ddc-a47b-a1adc6ef8b48/resource/"
                      "b1cbfecd-d723-4565-ba9c-91e4cc6540bb/download/gpkg_bd_uaecd_2025.zip")
URL_CATASTRO_2026 = ("https://datosabiertos.bogota.gov.co/dataset/"
                     "e4f2dba4-d0a1-4ddc-a47b-a1adc6ef8b48/resource/"
                     "66567ce6-bb0d-4a69-b1a8-674669dff05c/download/bd_uaecd_2026.gpkg")


def list_resources(dataset_id):
    with urllib.request.urlopen(CKAN + dataset_id, timeout=60) as r:
        data = json.load(r)
    for res in data["result"]["resources"]:
        mb = round(res["size"] / 1e6, 1) if res.get("size") else "?"
        print(f'{res["name"]:42s} | {res["format"]:12s} | {mb} MB')
        print(f'    {res["url"]}')


def pot_url():
    """Resuelve el recurso GDB del dataset POT via CKAN (por si cambia el enlace)."""
    with urllib.request.urlopen(CKAN + POT_ID, timeout=60) as r:
        data = json.load(r)
    for res in data["result"]["resources"]:
        if res.get("format") == "GDB" and res["url"].endswith(".gdb.zip"):
            return res["url"]
    raise SystemExit("No se encontro recurso GDB en el dataset POT")


def curl(url, dest):
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    cmd = ["curl.exe", "-L", "--fail", "--retry", "3", "--retry-delay", "5",
           "-C", "-", "-o", dest, url]
    print("curl:", " ".join(cmd))
    subprocess.run(cmd, check=True)


def unzip_first(zip_path, out_dir, inner):
    with zipfile.ZipFile(zip_path) as z:
        with z.open(inner) as src, open(out_dir, "wb") as dst:
            while True:
                chunk = src.read(8 * 1024 * 1024)
                if not chunk:
                    break
                dst.write(chunk)


def do_catastro(multi=True):
    target = os.path.join(OUT_DIR, "bd_uaecd.gpkg")
    if multi:
        tmp = os.path.join(OUT_DIR, "_tmp_gpkg.zip")
        curl(URL_CATASTRO_MULTI, tmp)
        print("extrayendo bd_uaecd.gpkg ...")
        unzip_first(tmp, target, "bd_uaecd.gpkg")
        os.remove(tmp)
    else:
        curl(URL_CATASTRO_2026, target)
    print("OK ->", target, os.path.getsize(target), "bytes")


def do_pot():
    url = pot_url()
    tmp = os.path.join(OUT_DIR, "_tmp_pot.gdb.zip")
    curl(url, tmp)
    print("extrayendo geodatabase POT ...")
    with zipfile.ZipFile(tmp) as z:
        z.extractall(OUT_DIR)
    os.remove(tmp)
    print("OK ->", os.path.join(OUT_DIR, "POT_Decreto_555_2021_Bogota_D_C.gdb"))


def main():
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--catastro", action="store_true", help="bd_uaecd.gpkg multicapa (22 capas)")
    g.add_argument("--catastro2026", action="store_true", help="GPKG 'Version Actual' (single-layer)")
    g.add_argument("--pot", action="store_true", help="geodatabase POT Decreto 555/2021")
    g.add_argument("--all", action="store_true", help="catastro multicapa + POT")
    g.add_argument("--list", action="store_true", help="lista recursos del dataset de catastro")
    args = ap.parse_args()

    if args.list:
        list_resources(CATASTRO_ID)
        print("-" * 60)
        list_resources(POT_ID)
        return
    if args.pot:
        do_pot()
    elif args.catastro2026:
        do_catastro(multi=False)
    elif args.all:
        do_catastro(multi=True)
        do_pot()
    else:  # default / --catastro
        do_catastro(multi=True)


if __name__ == "__main__":
    sys.exit(main())
