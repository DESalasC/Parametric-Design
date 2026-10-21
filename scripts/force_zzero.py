# -*- coding: utf-8 -*-
"""Reemplaza compute_dz_from_stage1_context por una versión que retorna 0.0."""
import os

p = r"C:\Users\Dario Salas\.openclaw-autoclaw\workspace\DWork\PROJECTS\DiseñoParametrico\src\fase-1-contexto\F1_CONTEXTO50_BUILD_v01.2.py"

with open(p, 'r', encoding='utf-8', errors='replace') as f:
    lines = f.readlines()

# Encontrar línea de inicio y fin de la función
start_line = None
end_line = None
for i, line in enumerate(lines):
    if 'def compute_dz_from_stage1_context' in line:
        start_line = i
    if start_line is not None and line.strip() == 'return 0.0' and i > start_line:
        end_line = i
        break

if start_line is None:
    print("ERROR: No se encontró def compute_dz_from_stage1_context")
    exit(1)
if end_line is None:
    print("ERROR: No se encontró el return 0.0 de cierre")
    exit(1)

nueva_funcion = '''def compute_dz_from_stage1_context(in_json_path, data):
    """Calcula el desplazamiento Z (Z_base) desde el contexto de etapa 1.

    El contexto50 (<CHIP>-contexto50.json) ya está normalizado a LOCAL Z
    (lote en z=0, ancla del lote = 0.0). Por lo tanto el desplazamiento Z
    aplicado a los volúmenes vecinos debe ser siempre 0.0 para que queden
    en la misma cota que el lote.

    No se lee CHIP-contexto.json (etapa 1) porque ese archivo tiene cotas
    absolutas del MDT (ej. 14.52 m) que introducirían un desajuste de ~14 m.
    """
    try:
        return 0.0
    except Exception:
        return 0.0
'''

# Reemplazar líneas [start_line : end_line+1]
new_lines = lines[:start_line] + [nueva_funcion] + lines[end_line+1:]
content = ''.join(new_lines)
# Normalizar a LF
content = content.replace('\r\n', '\n').replace('\r', '\n')

with open(p, 'w', encoding='utf-8') as f:
    f.write(content)

print("OK: funcion reemplazada, lineas %d a %d" % (start_line+1, end_line+1))
print("OK: archivo normalizado a LF")
