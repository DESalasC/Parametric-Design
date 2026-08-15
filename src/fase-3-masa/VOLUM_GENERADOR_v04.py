"""
================================================================================
VOLUM_GENERADOR_v04.py — Generación de Masa por Pisos y Usos
Proyecto: DisenoParametrico / Fase 3
GH Python Script para Grasshopper (IronPython 2.7 compatible)
================================================================================

OBJETIVO:
  Leer el JSON de programa de áreas y la huella física (envelope_curve) para
  subdividir la masa en pisos, generando los slabs (losas) y diferenciando
  el volumen del Núcleo de circulación del volumen de áreas útiles.

ENTRADAS:
  envelope_curve (Curve)   — Huella física con retiros y patio restado (F1)
  json_path (String)       — Ruta al archivo programa-areas.json
  floor_height (Number)    — Altura de entrepiso [m]

SALIDAS:
  volumenes_principales (List of Brep) — Masa por piso (área útil)
  volumenes_nucleo (List of Brep)      — Masa del núcleo central
  losas (List of Surface)              — Superficies horizontales por piso
  etiquetas (List of String)           — Info de usos por piso
  mensaje (String)
================================================================================
"""

import Rhino.Geometry as rg
import json
import os
import math

def unwrap(val):
    if val is None: return None
    if isinstance(val, list): return val[0] if len(val) > 0 else None
    return val

# ==============================================================================
# MAIN
# ==============================================================================

env_crv = globals().get("envelope_curve", None)
json_path_raw = globals().get("json_path", None)
floor_h_raw = globals().get("floor_height", 3.0)

json_path = str(unwrap(json_path_raw)) if json_path_raw else ""
floor_h = float(unwrap(floor_h_raw)) if floor_h_raw else 3.0

volumenes_principales = []
volumenes_nucleo = []
losas = []
etiquetas = []

if env_crv is None or not json_path or not os.path.exists(json_path):
    mensaje = "VOLUM v04 | ERROR: Falta envelope_curve o json_path inválido."
else:
    try:
        with open(json_path, "r") as f:
            data = json.load(f)
            
        programa = data.get("programa_pisos", [])
        
        # Obtener centroide y bounding box de la huella para ubicar el núcleo
        area_props = rg.AreaMassProperties.Compute(env_crv)
        centroide = area_props.Centroid if area_props else rg.Point3d(0,0,0)
        bbox = env_crv.GetBoundingBox(True)
        
        # Heurística de núcleo: 10% del área, cuadrado, en el centro
        # Dimensiones del núcleo (aprox 3x3 o 4x4 dependiendo del área)
        area_nucleo = data.get("area_por_piso", 100.0) * 0.10
        lado_nucleo = math.sqrt(area_nucleo)
        lado_nucleo = min(lado_nucleo, bbox.Max.X - bbox.Min.X, bbox.Max.Y - bbox.Min.Y)
        
        # Crear rectángulo del núcleo en el origen
        nuc_plano = rg.Plane(rg.Point3d(centroide.X - lado_nucleo/2, centroide.Y - lado_nucleo/2, 0), rg.Vector3d.ZAxis)
        nuc_rect = rg.Rectangle(nuc_plano, lado_nucleo, lado_nucleo)
        nuc_curve = nuc_rect.ToNurbsCurve()
        
        # Iterar pisos
        for p in programa:
            z = p.get("altura_z", 0.0)
            piso_num = p.get("piso", 0)
            usos = p.get("usos", [])
            
            # 1. Losa (Floor slab)
            slab = rg.Brep.CreatePlanarBreps(env_crv, 0.01)[0]
            slab.Translate(rg.Vector3d(0, 0, z))
            losas.append(slab)
            
            # 2. Volumen Principal (Envelope - Nucleo)
            # Extruir envelope
            vec_h = rg.Vector3d(0, 0, floor_h)
            env_vol = rg.Extrude.Create(env_crv, vec_h, True)
            if env_vol:
                env_vol.Translate(rg.Vector3d(0, 0, z))
                
                # Restar núcleo del volumen principal
                nuc_vol = rg.Extrude.Create(nuc_curve, vec_h, True)
                if nuc_vol:
                    nuc_vol.Translate(rg.Vector3d(0, 0, z))
                    diff = rg.Brep.CreateBooleanDifference(env_vol, nuc_vol, 0.01)
                    if diff and len(diff) > 0:
                        volumenes_principales.append(diff[0])
                    else:
                        volumenes_principales.append(env_vol)
                    
                    volumenes_nucleo.append(nuc_vol)
            
            # 3. Etiqueta
            usos_str = ", ".join(["{}: {:.0f}m2".format(u["uso"], u["area_bruta"]) for u in usos if u["uso"] != "Nucleo"])
            etiquetas.append("Piso {}: {}".format(piso_num, usos_str))

        mensaje = "VOLUM v04 | OK | {} pisos generados | Núcleo central {:.1f}x{:.1f}m".format(len(programa), lado_nucleo, lado_nucleo)

    except Exception as e:
        mensaje = "VOLUM v04 | ERROR: {}".format(str(e))
        