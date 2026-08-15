#! /usr/bin/env python3
"""
F1_NORMATIVA_LEER_v10 — Lector de parametros normativos desde cache POT.
GH Python Script para Grasshopper (IronPython 2.7 compatible)

v10: Correccion — entrega PISOS maximos (no altura en metros).
     La altura total depende de pisos_norma × entrepiso_usuario (variable 2.50-3.80m)

ENTRADAS:
  json_path — Ruta al cache JSON del lote

SALIDAS:
  floors_from_norm — Pisos maximos segun rango de edificabilidad
  tratamiento      — Tratamiento urbanistico (string)
  retiro_frontal   — Retiro frontal por defecto (m)
  retiro_lateral   — Retiro lateral por defecto (m)
  retiro_posterior — Retiro posterior por defecto (m)
  ic_maximo        — Indice de construccion maximo
  io_maximo        — Indice de ocupacion maximo
  mensaje          — Diagnostico
"""

import json
import os

# Mapeo rango edificabilidad → pisos maximos (Decreto 555/2021)
RANGO_PISOS = {
    "1": 2,
    "2": 3,
    "3": 5,
    "4": 8,
    "5": 12,
}

# --- INPUT ---
json_path_raw = globals().get("json_path", None)
json_path = str(json_path_raw).strip("[]'\" ") if json_path_raw else ""

# --- VALORES DEFAULT ---
floors_from_norm = 5
tratamiento_out = "Consolidacion"
retiro_frontal = 3.0
retiro_lateral = 0.0
retiro_posterior = 0.0
ic_maximo = 2.0
io_maximo = 0.70
mensaje = "OK"

if json_path and os.path.exists(json_path):
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        pd = data.get("pot_data", {})
        
        rango = str(pd.get("rango_edificabilidad", "3"))
        floors_from_norm = RANGO_PISOS.get(rango, 5)
        
        tratamiento_out = str(pd.get("tratamiento", "Consolidacion"))
        
        # Retiros segun tratamiento
        t = tratamiento_out.lower()
        if "desarrollo" in t:
            retiro_frontal, retiro_lateral, retiro_posterior = 5.0, 3.0, 3.0
            ic_maximo, io_maximo = 3.0, 0.50
        elif "renovacion" in t:
            retiro_frontal, retiro_lateral, retiro_posterior = 5.0, 3.0, 3.0
            ic_maximo, io_maximo = 5.0, 0.60
        elif "conservacion" in t:
            retiro_frontal, retiro_lateral, retiro_posterior = 3.0, 3.0, 3.0
            ic_maximo, io_maximo = 2.0, 0.50
        else:
            # Consolidacion + Continua (default)
            retiro_frontal, retiro_lateral, retiro_posterior = 3.0, 0.0, 0.0
            ic_maximo, io_maximo = 2.0, 0.70
        
        mensaje = "Rango {} -> {} pisos max | {}".format(rango, floors_from_norm, tratamiento_out)
        
    except Exception as e:
        mensaje = "ERROR JSON: {}".format(str(e))
else:
    mensaje = "json_path no valido: {}".format(json_path)
    # Valores default ya asignados arriba

print(mensaje)
