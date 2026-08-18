"""
================================================================================
F3_VOLUM_GENERADOR_v06.py - Generacion de Masa por Pisos y Usos (fix Rhino 8)
Proyecto: DisenoParametrico / Fase 3
GH Python Script para Grasshopper (IronPython 2.7 compatible)
================================================================================

v06 (2026-08-14): fixes de compatibilidad con Rhino 8.33 detectados en la prueba
real de masa (F3_PRUEBA_MASA_A_rhino.py):
  - rg.Extrude.Create(...)  -> rg.Extrusion.Create(...).ToBrep()   (Extrude no existe)
  - rg.Rectangle(...)       -> PolylineCurve de las 4 esquinas      (Rectangle no se
    expone al namespace Python) + ToNurbsCurve() ya no aplica
Mantiene los fixes del v05 (nucleo real del JSON, altura_piso por nivel, UTF-8,
union de losas con patio) y el mismo contrato GH.

ENTRADAS (iguales a v04/v05):
  envelope_curve (Curve)   - Huella fisica con retiros y patio restado (F1)
  json_path (String)       - Ruta al programa-areas.json (F3_DISTRIBUCION)
  floor_height (Number)    - Altura de entrepiso [m] (default 3.0; se prefiere
                             la altura_z del JSON por piso)

SALIDAS (iguales a v04/v05):
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
    mensaje = "VOLUM v06 | ERROR: Falta envelope_curve o json_path invalido."
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

        # Contorno del nucleo (PolylineCurve cerrada; Rectangle no se expone en Rhino 8)
        l2 = lado_nucleo / 2.0
        cx, cy = centroide.X, centroide.Y
        nuc_pts = [rg.Point3d(cx - l2, cy - l2, 0), rg.Point3d(cx + l2, cy - l2, 0),
                   rg.Point3d(cx + l2, cy + l2, 0), rg.Point3d(cx - l2, cy + l2, 0),
                   rg.Point3d(cx - l2, cy - l2, 0)]
        nuc_curve = rg.PolylineCurve(nuc_pts)

        n_pisos = 0
        n_huecos = 0
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

            # 2. Volumen principal (envelope con hueco del nucleo, via boolean 2D
            #    de curvas -> mas estable que el boolean 3D en Rhino 8)
            hueco = rg.Curve.CreateBooleanDifference(env_crv, nuc_curve, 0.01)
            if hueco and len(hueco) > 0:
                perfil = hueco[0]
                n_huecos += 1
            else:
                perfil = env_crv
            env_ext = rg.Extrusion.Create(perfil.ToNurbsCurve(), h_piso, True)
            if env_ext:
                env_vol = env_ext.ToBrep()
                env_vol.Translate(rg.Vector3d(0, 0, z))
                nuc_ext = rg.Extrusion.Create(nuc_curve.ToNurbsCurve(), h_piso, True)
                if nuc_ext:
                    nuc_vol = nuc_ext.ToBrep()
                    nuc_vol.Translate(rg.Vector3d(0, 0, z))
                    volumenes_principales.append(env_vol)
                    volumenes_nucleo.append(nuc_vol)

            # 3. Etiqueta
            usos_str = ", ".join(["{}: {:.0f}m2".format(u["uso"], u["area_bruta"])
                                  for u in usos if u["uso"] != "Nucleo"])
            etiquetas.append("Piso {}: {}".format(piso_num, usos_str))
            n_pisos += 1

        mensaje = ("VOLUM v06 | OK | {} pisos | Nucleo {:.1f}x{:.1f}m | "
                   "balance GFA {:.0f} m2 | huecos aplicados {}/{}").format(
            n_pisos, lado_nucleo, lado_nucleo, data.get("gfa_total", 0.0),
            n_huecos, n_pisos)

    except Exception as e:
        mensaje = "VOLUM v06 | ERROR: {}".format(str(e))
