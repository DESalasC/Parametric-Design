"""
Script: F1_NORMATIVA_LEER_v09.py
Proyecto: DiseñoParametrico
Fase: 1 - Contexto y Lote (Normativa)
Versión: 09
Descripción: 
    Ajuste normativo: Altura máxima por piso actualizada a 3.80m.
    Parser inteligente para textos como "no exigido".
"""

import json
import os
import re

# Inputs:
# json_path: string
# tratamiento: string
# tipologia: string

# Constante normativa de Bogotá
ALTURA_PISO_M = 3.80

retiro_frontal = 0.0
retiro_lateral = 0.0
retiro_posterior = 0.0
altura_maxima = 0.0
ic_maximo = 2.0
io_maximo = 0.0
mensaje = "Esperando datos..."
raw_data_str = "Sin datos"

path_str = ""
if isinstance(json_path, list):
    if len(json_path) > 0:
        path_str = str(json_path[0])
else:
    path_str = str(json_path)

path_str = path_str.strip("[]'\" ")

def extract_numbers_recursive(d, keys, is_pisos=False):
    found_vals = []
    if isinstance(d, dict):
        for k, v in d.items():
            if k in keys:
                if isinstance(v, (int, float)):
                    val = float(v) * ALTURA_PISO_M if is_pisos else float(v)
                    found_vals.append(val)
                elif isinstance(v, str):
                    if "no exigido" in v.lower():
                        found_vals.append(0.0)
                    else:
                        nums = re.findall(r"[-+]?\d*\.\d+|\d+", v)
                        if nums:
                            val = float(nums[0]) * ALTURA_PISO_M if is_pisos else float(nums[0])
                            found_vals.append(val)
            else:
                found_vals.extend(extract_numbers_recursive(v, keys, is_pisos))
    elif isinstance(d, list):
        for item in d:
            found_vals.extend(extract_numbers_recursive(item, keys, is_pisos))
    return found_vals

if path_str and os.path.exists(path_str):
    try:
        with open(path_str, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        t_key = str(tratamiento).lower().strip()
        tip_key = "tipologia_" + str(tipologia).lower().strip()
        
        tipologia_dict = None
        
        if "tratamientos" in data and isinstance(data["tratamientos"], dict):
            tratamientos = data["tratamientos"]
            for t, t_val in tratamientos.items():
                if t_key in t:
                    if isinstance(t_val, dict):
                        for tip, tip_val in t_val.items():
                            if tip_key in tip:
                                tipologia_dict = tip_val
                                break
                    break

        if tipologia_dict:
            raw_data_str = json.dumps(tipologia_dict, indent=2, ensure_ascii=False)
            if len(raw_data_str) > 5000:
                raw_data_str = raw_data_str[:5000] + "\n... (Texto cortado)"
            
            posteriores = extract_numbers_recursive(tipologia_dict, ["aislamiento_posterior_m", "retiro_posterior"])
            laterales = extract_numbers_recursive(tipologia_dict, ["aislamiento_lateral_m", "retiro_lateral"])
            frontales = extract_numbers_recursive(tipologia_dict, ["retiro_frontal", "antejardin"])
            alturas = extract_numbers_recursive(tipologia_dict, ["altura_max_pisos", "altura_maxima"], is_pisos=True)
            ics = extract_numbers_recursive(tipologia_dict, ["indice_construccion_efectivo_max_directo", "ic"])
            
            retiro_posterior = max(posteriores) if posteriores else 0.0
            retiro_lateral = max(laterales) if laterales else 0.0
            retiro_frontal = max(frontales) if frontales else 3.0 # Default 3m si no está
            altura_maxima = max(alturas) if alturas else (4 * ALTURA_PISO_M) # Default 4 pisos = 15.2m
            ic_maximo = max(ics) if ics else 2.0
            
            mensaje = "Norma Encontrada:\n"
            mensaje += "Tratamiento: {} | Tipología: {}\n".format(tratamiento, tipologia)
            mensaje += "Retiro Frontal: {:.1f}m\n".format(retiro_frontal)
            mensaje += "Retiro Lateral: {:.1f}m\n".format(retiro_lateral)
            mensaje += "Retiro Posterior: {:.1f}m\n".format(retiro_posterior)
            mensaje += "Altura Máxima: {:.1f}m (Basado en {}m/piso)\n".format(altura_maxima, ALTURA_PISO_M)
            mensaje += "IC Máximo: {:.1f}\n".format(ic_maximo)
            print(mensaje)
        else:
            mensaje = "No se encontró la rama para {} - {}".format(tratamiento, tipologia)
            print(mensaje)
            
    except Exception as e:
        mensaje = "Error leyendo JSON: " + str(e)
        print(mensaje)
else:
    mensaje = "Ruta no encontrada o inválida."
    print(mensaje)

# Salidas:
a = retiro_frontal
b = retiro_lateral
c = retiro_posterior
d = altura_maxima
e = ic_maximo
f = io_maximo
g = mensaje
h = raw_data_str
