# -*- coding: utf-8 -*-
"""Limpia compute_dz_from_stage1_context: retorna -ancla_z, elimina codigo muerto."""
import os

p = r"C:\Users\Dario Salas\.openclaw-autoclaw\workspace\DWork\PROJECTS\DiseñoParametrico\src\fase-1-contexto\F1_CONTEXTO50_BUILD_v01.2.py"

with open(p, 'r', encoding='utf-8', errors='replace') as f:
    lines = f.readlines()

# Encontrar inicio y fin de la función
start_line = None
end_line = None
for i, line in enumerate(lines):
    if 'def compute_dz_from_stage1_context' in line:
        start_line = i
    if start_line is not None and line.strip() == 'return 0.0' and i > start_line:
        end_line = i
        break

if start_line is None:
    print("ERROR: No se encontro def compute_dz_from_stage1_context")
    exit(1)
if end_line is None:
    print("ERROR: No se encontro el primer return 0.0 de cierre")
    exit(1)

nueva_funcion = '''def compute_dz_from_stage1_context(in_json_path, data):
    """Calcula el desplazamiento Z (Z_base) desde el contexto de etapa 1.

    El contexto50 (<CHIP>-contexto50.json) tiene z_base_m = z_MDT - z_ref,
    con z_ref = origen_sirgas.z + ancla_canvas_local.z. Un edificio al nivel
    del lote queda en z_base_m = -ancla_canvas_local.z (ej. -14.518).
    Para que el lote quede en z=0, el desplazamiento debe ser -ancla_z,
    asi z_base_ajustado = z_base - (-ancla_z) = z_base + ancla_z ~ 0.

    No se lee CHIP-contexto.json (etapa 1) porque tiene cotas absolutas del MDT.
    """
    try:
        ancla_z = None
        if isinstance(data, dict):
            meta = data.get("metadata", {}) or {}
            ancla = meta.get("ancla_canvas_local", {}) or {}
            ancla_z = to_float(ancla.get("z"), None)
        if ancla_z is not None:
            return -ancla_z
        return 0.0
    except Exception:
        return 0.0
'''

new_lines = lines[:start_line] + [nueva_funcion] + lines[end_line+1:]
content = ''.join(new_lines)
# Normalizar a LF
content = content.replace('\r\n', '\n').replace('\r', '\n')

with open(p, 'w', encoding='utf-8') as f:
    f.write(content)

print("OK: funcion limpia, lineas %d a %d" % (start_line+1, end_line+1))
print("OK: archivo normalizado a LF")
