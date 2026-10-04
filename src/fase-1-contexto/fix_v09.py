import re

with open(r'D:\Work\PROJECTS\DiseñoParametrico\src\fase-1-contexto\F1_ETAPA2_NORMATIVA_v09.py', 'r', encoding='utf-8') as f:
    content = f.read()

old = """try: floor_h = float(unwrap(floor_h_raw)) if floor_h_raw else 3.0
except: floor_h = 3.0

try: io_user = float(unwrap(io_user_raw)) if io_user_raw else 0.0
except: io_user = 0.0

tratamiento = str(unwrap(tratamiento_raw)) if tratamiento_raw else "Consolidacion"

# --- PISOS Y ALTURA ---
ic_maximo_base = RANGO_PISOS.get(rango, RANGO_PISOS[RANGO_DEFAULT])
pisos_extra = BONIFICACION_PISOS.get(tipo_bonificacion, 0) if piso_adicional else 0
pisos_propuestos = ic_maximo_base + pisos_extra"""

new = """try: floor_h = float(unwrap(floor_h_raw)) if floor_h_raw else 3.0
except: floor_h = 3.0
if floor_h <= 0: floor_h = 3.0

try: io_user = float(unwrap(io_user_raw)) if io_user_raw else 0.0
except: io_user = 0.0

tratamiento = str(unwrap(tratamiento_raw)) if tratamiento_raw else "Consolidacion"

# --- IO MÁXIMO (inicialización temprana para presupuesto_ocupacion_m2) ---
if io_user > 0: io_maximo = io_user
elif tratamiento == "Consolidacion": io_maximo = 0.70
elif tratamiento in ("Desarrollo", "Mejoramiento"): io_maximo = 0.60
else: io_maximo = 0.70

# --- PISOS Y ALTURA ---
ic_maximo_base = RANGO_PISOS.get(rango, RANGO_PISOS[RANGO_DEFAULT])
pisos_extra = BONIFICACION_PISOS.get(tipo_bonificacion, 0) if piso_adicional else 0
pisos_propuestos = ic_maximo_base + pisos_extra"""

if old in content:
    content = content.replace(old, new)
    with open(r'D:\Work\PROJECTS\DiseñoParametrico\src\fase-1-contexto\F1_ETAPA2_NORMATIVA_v09.py', 'w', encoding='utf-8') as f:
        f.write(content)
    print('Reemplazo exitoso')
else:
    print('No se encontró el patrón exacto')
    idx = content.find('try: floor_h = float(unwrap(floor_h_raw))')
    if idx >= 0:
        print('Encontrado en índice', idx)
        print(repr(content[idx:idx+400]))