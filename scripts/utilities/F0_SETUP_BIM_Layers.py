"""
Script: F0_SETUP_BIM_Layers.py
Proyecto: DiseñoParametrico
Fase: 0 - Setup BIM
Versión: 01
Descripción:
    Lee el CSV de GuBIMclass y devuelve una lista de nombres de capas
    y una lista de puntos correspondientes para inyectarlos a ArchiCAD
    vía Tapir.
"""

import csv
import os
import io

# Flake8/Pylance fix: Rhino se importa implícitamente en GHPython.
try:
    import Rhino
except ImportError:
    Rhino = None

# Inputs de Grasshopper (se definen como None para el linter)
# csv_path: string (Ruta a GuBIMclass_v12_ES_clean.csv)
csv_path = None  # type: ignore

layer_names = []
injection_points = []

if csv_path and os.path.exists(csv_path):
    try:
        with open(csv_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            if lines and lines[0].startswith("0 |"):
                lines = lines[1:]

            reader = csv.reader(
                io.StringIO(''.join(lines)),
                delimiter='|'
            )

            x = 0
            y = 0
            for row in reader:
                if len(row) >= 3:
                    code = row[1].strip()
                    name = row[2].strip()

                    if code and name:
                        layer_name = "{} - {}".format(code, name)
                        layer_names.append(layer_name)

                        if Rhino:
                            # Generar un punto en una cuadrícula
                            pt = Rhino.Geometry.Point3d(x, y, 0)
                            injection_points.append(pt)

                        x += 1
                        if x > 50:  # Cuadrícula de 50xN
                            x = 0
                            y += 1

        msg = "Capas extraidas: {}. Puntos generados: {}"
        print(msg.format(len(layer_names), len(injection_points)))

    except Exception as e:
        print("Error leyendo CSV: " + str(e))
else:
    print("Ruta del CSV no valida o no definida.")

# Salidas en Grasshopper:
# a -> layer_names (Lista de strings)
# b -> injection_points (Lista de Point3d)
