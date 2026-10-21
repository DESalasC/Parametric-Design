# -*- coding: utf-8 -*-
"""Corrige compute_dz_from_stage1_context: retorna 0.0 cuando hay z_ref_m (contexto50 ya en LOCAL Z)."""
import os, re

p = r"C:\Users\Dario Salas\.openclaw-autoclaw\workspace\DWork\PROJECTS\DiseñoParametrico\src\fase-1-contexto\F1_CONTEXTO50_BUILD_v01.2.py"

with open(p, 'r', encoding='utf-8') as f:
    content = f.read()

old = '''        # Usar CHIP-contexto50.json (data ya está cargado, contiene z_ref_m en metadata)
        # en lugar de cargar el hermano CHIP-contexto.json.
        z_ref_m = None
        if isinstance(data, dict):
            meta = data.get("metadata", {}) or {}
            zbf = meta.get("z_base_fuente", {}) or {}
            z_ref_m = to_float(zbf.get("z_ref_m"), None)
            if z_ref_m is not None:
                return z_ref_m

        # Fallback: leer CHIP-contexto.json hermano (etapa 1) para min_z/vecinos/ancla'''

new = '''        # Usar CHIP-contexto50.json (data ya está cargado).
        # z_ref_m es una cota ABSOLUTA en SIRGAS (ej. 14.52 m), NO un desplazamiento local.
        # El contexto50 ya está en LOCAL Z (lote en z=0), así que desplazamiento_z = 0.0.
        if isinstance(data, dict):
            meta = data.get("metadata", {}) or {}
            zbf = meta.get("z_base_fuente", {}) or {}
            z_ref_m = to_float(zbf.get("z_ref_m"), None)
            if z_ref_m is not None:
                # Contexto50 ya normalizado a LOCAL Z: el desplazamiento es 0.0
                return 0.0

        # Fallback: leer CHIP-contexto.json hermano (etapa 1) para min_z/vecinos/ancla'''

if old not in content:
    print("ERROR: texto viejo no encontrado")
    print("Buscando patrón similar...")
    if "z_ref_m is not None:" in content:
        print("Se encontró 'z_ref_m is not None:'")
    else:
        print("Ni siquiera se encontró ese patrón")
else:
    content = content.replace(old, new, 1)
    # Normalizar a LF
    content = content.replace('\r\n', '\n').replace('\r', '\n')
    with open(p, 'w', encoding='utf-8') as f:
        f.write(content)
    print("OK: reemplazo aplicado y archivo normalizado a LF")
