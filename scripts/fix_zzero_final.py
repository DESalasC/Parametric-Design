# -*- coding: utf-8 -*-
"""Devuelve compute_dz_from_stage1_context a return 0.0 (contexto50 ya normalizado)."""
import os

p = r"C:\Users\Dario Salas\.openclaw-autoclaw\workspace\DWork\PROJECTS\DiseñoParametrico\src\fase-1-contexto\F1_CONTEXTO50_BUILD_v01.2.py"

with open(p, 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

start_marker = "def compute_dz_from_stage1_context(in_json_path, data):"
end_marker = "    except Exception:\n        return 0.0"

start_idx = content.find(start_marker)
if start_idx < 0:
    print("ERROR: No se encontro start_marker")
    exit(1)

end_idx = content.find(end_marker, start_idx)
if end_idx < 0:
    print("ERROR: No se encontro end_marker")
    exit(1)

end_idx = content.find('\n', end_idx) + 1

nueva_funcion = '''def compute_dz_from_stage1_context(in_json_path, data):
    """Calcula el desplazamiento Z (Z_base) desde el contexto de etapa 1.

    El contexto50 (<CHIP>-contexto50.json) YA ESTA normalizado:
    z_base_m = z_MDT - z_ref, con z_ref = origen_sirgas.z + ancla_canvas_local.z.
    Un edificio al nivel del lote queda en z_base_m = 0. El lote objetivo
    (predio) queda en z=0 por construccion del z_ref.

    Por lo tanto desplazamiento_z = 0.0 siempre. No se aplica offset adicional,
    para evitar desajuste doble del ancla_canvas_local.z (14.5176 m en AAA0030JKOE).
    """
    try:
        return 0.0
    except Exception:
        return 0.0'''

content = content[:start_idx] + nueva_funcion + content[end_idx:]

# Normalizar a LF
content = content.replace('\r\n', '\n').replace('\r', '\n')

with open(p, 'w', encoding='utf-8') as f:
    f.write(content)

print("OK: compute_dz_from_stage1_context = return 0.0 (contexto50 ya normalizado)")
print("OK: archivo normalizado a LF")
