"""
================================================================================
F3_VOLUM_GENERADOR_v05.py - Generacion de Masa por Pisos y Usos (fix v04)
Proyecto: DisenoParametrico / Fase 3
GH Python Script para Grasshopper (IronPython 2.7 compatible)
================================================================================

DIAGNOSTICO v04 (2026-08-14):
  - Heredaba el JSON de F3_PROGRAMA_AREAS_v01 cuyo balance era incorrecto
    (con GFA 1.053 m2 generaba solo 382,6 m2 construidos: deficit 670 m2).
  - Nucleo heuristico 10% del area por piso (sin criterio NSR-10).
  - Z fijas de 3,0 m (ignoraba primer piso 3,6 m).
  - open() sin encoding (riesgo con tildes en Windows/IronPython).
  - CreatePlanarBreps tomaba solo el primer brep (huella con patio -> perdia losas).

FIXES v05:
  1. Consume programa-areas.json emitido por F3_DISTRIBUCION_v01 (balanceado:
     suma de areas = GFA real; nucleo por componentes NSR-10; altura_z real).
  2. Nucleo: usa dimension real del JSON (nucleo.lado_m) si existe; si no,
     fallback al 10% heuristico del v04.
  3. Losas: CreatePlanarBreps puede devolver varios breps (patio) -> union booleana.
  4. Lectura UTF-8 (io.open) y manejo de errores por piso.

ENTRADAS (iguales a v04):
  envelope_curve (Curve)   - Huella fisica con retiros y patio restado (F1)
  json_path (String)       - Ruta al programa-areas.json (F3_DISTRIBUCION)
  floor_height (Number)    - Altura de entrepiso [m] (default 3.0; se prefiere
                             la altura_z del JSON por piso)

SALIDAS (iguales a v04):
  volumenes_principales (List of Brep) - Masa por piso (area util, sin nucleo)
  volumenes_nucleo (List of Brep)      - Masa del nucleo central
  losas (List of Surface)              - Superficies horizontales por piso
  etiquetas (List of String)           - Info de usos por piso
  mensaje (String)
================================================================================
"""

import Rhino.Geometry as rg
import json
import os
import math
import io

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
mensaje = ""

if env_crv is None or not json_path or not os.path.exists(json_path):
    mensaje = "VOLUM v05 | ERROR: Falta envelope_curve o json_path invalido."
else:
    try:
        with io.open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        programa = data.get("programa_pisos", [])

        # Centroide y bounding box de la huella
        area_props = rg.AreaMassProperties.Compute(env_crv)
        centroide = area_props.Centroid if area_props else rg.Point3d(0, 0, 0)
        bbox = env_crv.GetBoundingBox(True)

        # Nucleo: dimension real del JSON (F3_DISTRIBUCION, por componentes NSR-10)
        # o fallback al 10% heuristico (v04)
        nucleo_info = data.get("nucleo", {})
        lado_nucleo = nucleo_info.get("lado_m", None)
        if not lado_nucleo:
            area_nucleo = data.get("area_por_piso", 100.0) * 0.10
            lado_nucleo = math.sqrt(area_nucleo)
        lado_nucleo = min(float(lado_nucleo), bbox.Max.X - bbox.Min.X,
                          bbox.Max.Y - bbox.Min.Y)

        nuc_plano = rg.Plane(rg.Point3d(centroide.X - lado_nucleo / 2,
                                        centroide.Y - lado_nucleo / 2, 0),
                             rg.Vector3d.ZAxis)
        nuc_rect = rg.Rectangle(nuc_plano, lado_nucleo, lado_nucleo)
        nuc_curve = nuc_rect.ToNurbsCurve()

        n_pisos = 0
        for p in programa:
            z = p.get("altura_z", 0.0)
            piso_num = p.get("piso", 0)
            usos = p.get("usos", [])
            h_piso = float(p.get("altura_piso", floor_h))
            if not h_piso or h_piso <= 0:
                h_piso = floor_h

            # 1. Losa: puede haber varios breps (huella con patio) -> unir
            slabs = rg.Brep.CreatePlanarBreps(env_crv, 0.01)
            if not slabs or len(slabs) == 0:
                continue
            slab = slabs[0]
            if len(slabs) > 1:
                union = rg.Brep.CreateBooleanUnion(slabs, 0.01)
                if union and len(union) > 0:
                    slab = union[0]
            slab.Translate(rg.Vector3d(0, 0, z))
            losas.append(slab)

            # 2. Volumen principal (envelope - nucleo)
            vec_h = rg.Vector3d(0, 0, h_piso)
            env_vol = rg.Extrude.Create(env_crv, vec_h, True)
            if env_vol:
                env_vol.Translate(rg.Vector3d(0, 0, z))
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
            usos_str = ", ".join(["{}: {:.0f}m2".format(u["uso"], u["area_bruta"])
                                  for u in usos if u["uso"] != "Nucleo"])
            etiquetas.append("Piso {}: {}".format(piso_num, usos_str))
            n_pisos += 1

        mensaje = ("VOLUM v05 | OK | {} pisos | Nucleo {:.1f}x{:.1f}m | "
                   "balance GFA {:.0f} m2").format(
            n_pisos, lado_nucleo, lado_nucleo, data.get("gfa_total", 0.0))

    except Exception as e:
        mensaje = "VOLUM v05 | ERROR: {}".format(str(e))
