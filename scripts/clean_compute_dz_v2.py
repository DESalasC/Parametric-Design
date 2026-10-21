# -*- coding: utf-8 -*-
"""Reemplaza todo el bloque compute_dz_from_stage1_context hasta _es_horario."""
import os

p = r"C:\Users\Dario Salas\.openclaw-autoclaw\workspace\DWork\PROJECTS\DiseñoParametrico\src\fase-1-contexto\F1_CONTEXTO50_BUILD_v01.2.py"

with open(p, 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

start_marker = "def compute_dz_from_stage1_context"
end_marker = "def _es_horario"

start_idx = content.find(start_marker)
if start_idx < 0:
    print("ERROR: No se encontro start_marker")
    exit(1)

end_idx = content.find(end_marker, start_idx)
if end_idx < 0:
    print("ERROR: No se encontro end_marker (_es_horario)")
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

content = content[:start_idx] + nueva_funcion + content[end_idx:]

# Normalizar a LF
content = content.replace('\r\n', '\n').replace('\r', '\n')

with open(p, 'w', encoding='utf-8') as f:
    f.write(content)

print("OK: bloque reemplazado desde compute_dz_from_stage1_context hasta _es_horario")
print("OK: archivo normalizado a LF")

# Verificar no hay duplicados de return 0.0 seguidos
count_return0 = content.count('return 0.0        return 0.0')
if count_return0 > 0:
    print("WARN: aun hay return 0.0 duplicados: %d" % count_return0)
else:
    print("OK: no hay return 0.0 duplicados")
