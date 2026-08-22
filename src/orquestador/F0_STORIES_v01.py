# -*- coding: utf-8 -*-
# ============================================================================
# F0_STORIES_v01.py - lista de Stories (nombres + elevaciones) para Tapir SetStories
# ============================================================================
# Proposito: derivar la lista de niveles (Story) del edificio desde
#   programa-areas.json (el mismo archivo que lee F3_VOLUM_GENERADOR) y
#   exponerla como listas para cablear al componente Tapir "SetStories"
#   (StoryNames + StoryElevations + ShowOnSections + Execute).
#
#   Las elevaciones se toman del campo `altura_z` de cada piso, de modo que
#   coinciden EXACTAMENTE con la Z donde F3 genera los morphs/placas. Asi no
#   hay desfase entre Story y geometria.
#
# Normativa aplicable: ninguna (script de orquestacion del canvas; no calcula
#   retiros, GFA ni normativa).
#
# Historial de versiones:
#   v01.2 (2026-08-21) - Definir __file__ para evitar error 'name '__file__' is not defined' en entornos donde no está disponible (como GHPython).
#   v01.1 (2026-08-20) - Forzar acceso de lista en las salidas 0 (story_names) y 1 (story_elevations) para evitar errores de conversión Text→List.
#   v01   (2026-08-19) - carga inicial.
#
# Entradas:
#   json_path        : str (Item)   - ruta a programa-areas.json (misma que F3).
#   num_pisos        : int (Item)   - fallback: numero de pisos si no hay json.
#   floor_height     : float (Item) - fallback: altura de entrepiso [m].
#   nombre_base      : str (Item)   - prefijo de nombre; default "Nivel".
#   nivel_terreno    : str (Item)   - opcional: nombre de un nivel de terreno
#                                     previo (ej. "Terreno"); "" = sin extra.
#   show_on_sections : bool (Item)  - passthrough a SetStories; default True.
#
# Salidas:
#   story_names       : list[str]   - nombres (orden ascendente).
#   story_elevations  : list[float] - elevacion [m] por story (misma longitud).
#   show_on_sections  : bool        - passthrough para SetStories.
#   ok                : bool        - True si se genero la lista.
#   log               : str         - resumen / error.
#
# Funciones internas:
#   _f(v) - float a prueba de fallos.
#   _i(v) - int a prueba de fallos.
# ============================================================================

import io
import json
import os

# Define __file__ if not already defined (for compatibility with environments that don't set it)
try:
    __file__
except NameError:
    import ghpythonlib.component as comp
    __file__ = comp.OnPingDocument().FileName if comp.OnPingDocument() else "unknown"

# ---- Forzar acceso de lista en las salidas 0 (story_names) y 1 (story_elevations) ----
try:
    import Grasshopper as gh
    ghenv.Component.Params.Output[0].Access = gh.Kernel.GH_ParamAccess.list   # story_names
    ghenv.Component.Params.Output[1].Access = gh.Kernel.GH_ParamAccess.list   # story_elevations
except Exception:
    # Si falla el acceso a Grasshopper, continuar sin forzar el modo de acceso
    # (dependerá de la configuración manual del componente)
    pass


def _f(v):
    try:
        return float(v)
    except Exception:
        return 0.0


def _i(v):
    try:
        return int(round(float(v)))
    except Exception:
        return 0


json_path = globals().get("json_path") or ""
num_pisos = _i(globals().get("num_pisos"))
floor_height = _f(globals().get("floor_height"))
nombre_base = str(globals().get("nombre_base") or "Nivel").strip() or "Nivel"
nivel_terreno = str(globals().get("nivel_terreno") or "").strip()

_ss = globals().get("show_on_sections", None)
if _ss is None:
    show_on_sections = True
elif isinstance(_ss, bool):
    show_on_sections = _ss
else:
    show_on_sections = str(_ss).strip().lower() in ("true", "1", "si", "yes")

story_names = []
story_elevations = []
ok = False
log = ""

if json_path and os.path.exists(json_path):
    try:
        with io.open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        pisos = data.get("programa_pisos") or []
        if isinstance(pisos, list):
            pisos = sorted(pisos, key=lambda p: _i(p.get("piso", 0)) if isinstance(p, dict) else 0)
            for p in pisos:
                if not isinstance(p, dict):
                    continue
                n = _i(p.get("piso", 0))
                z = _f(p.get("altura_z", 0.0))
                story_names.append("{} {}".format(nombre_base, n))
                story_elevations.append(z)
        if story_names:
            ok = True
            log = "OK: {} stories desde {}".format(len(story_names), json_path)
        else:
            log = "ERROR: programa_pisos vacio en {}".format(json_path)
    except Exception as e:
        log = "ERROR leyendo {}: {}".format(json_path, e)
else:
    if num_pisos > 0:
        h = floor_height if floor_height > 0.0 else 3.0
        for n in range(1, num_pisos + 1):
            story_names.append("{} {}".format(nombre_base, n))
            story_elevations.append((n - 1) * h)
        ok = True
        log = "OK: {} stories (fallback {} pisos x h={:.2f}m)".format(len(story_names), num_pisos, h)
    else:
        log = "ERROR: json_path invalido y num_pisos <= 0. Cablear json_path o num_pisos."

# Nivel de terreno opcional (para lot/vias/vecinos a cota 0). OJO: si el
# "Nivel 1" del programa tambien esta a cota 0, habra colision de elevaciones.
if nivel_terreno:
    story_names.insert(0, nivel_terreno)
    story_elevations.insert(0, 0.0)
    log += " | nivel_terreno '{}' agregado a cota 0".format(nivel_terreno)

try:
    ghenv.Component.Message = log  # noqa: F821
except Exception:
    pass
