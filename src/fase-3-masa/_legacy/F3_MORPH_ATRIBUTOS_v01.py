# -*- coding: utf-8 -*-
"""
================================================================================
F3_MORPH_ATRIBUTOS_v01.py - Asigna nivel (Story) y capa (Layer) a los Morphs de F3
Proyecto: DiseñoParametrico / Fase 3
GH Python Script para Grasshopper (componente "Script", IronPython 2.7)
================================================================================

PROPOSITO:
  Los Morphs que F3_VOLUM_GENERADOR_v08 envia a ArchiCAD via
  Live Connection se crean SIN nivel (Story) ni capa asignados. Este componente
  toma la geometria (morphs) con dos listas PARALELAS (piso y uso) y genera:
    - layer_names  : nombre de capa por morph (codigo GuBIMclass segun uso)
    - story_names  : nombre del nivel (Story) por morph (segun su piso/nivel)
    - manifest_json: archivo JSON piso/uso/layer/story por morph, para que un
      script Tapir (ArchiCAD API) o un post-proceso asigne en ArchiCAD los
      atributos (nivel + capa) a cada Morph ya creado.

  Mecanismo completo (3 pasos):
    Paso 1 (implementado en F3_VOLUM_GENERADOR_v08): F3 ya emite, paralela
      a `volumenes_por_uso`/`usos_etiquetas`, la lista `usos_pisos` (numero de
      piso por volumen). Cablear `usos_pisos` de F3 a la entrada `pisos` de
      este componente.
    Paso 2 (este componente): mapear uso->capa (GuBIMclass) y piso->nivel;
      emitir `layer_names`/`story_names` + el manifest en disco.
    Paso 3 (Tapir / Live Connection): cablear `layer_names` y `story_names` al
      componente Morph de la Live Connection (si expone inputs de capa/nivel),
      o consumir `morph-manifest.json` desde un script del paquete `archicad`.
      Nota verificada (F3_StorySync_v01): el paquete `archicad` (ac29) NO
      expone Create/Modify de elementos; si se confirma, la asignacion de
      nivel/capa se hace por Live Connection o manual en ArchiCAD.

NORMATIVA APLICABLE:
  Ninguna (script de atributos BIM; no calcula retiros, GFA ni normativa).

HISTORIAL:
  v01.3 (2026-08-21) - Definir __file__ para evitar error 'name '__file__' is not defined' en entornos donde no está disponible (como GHPython).
  v01.2 (2026-08-21) - Forzar acceso de lista en las salidas 0 (layer_names) y 1 (story_names) para evitar errores de conversión Text→Layer/Story.
  v01.1 (2026-08-20) - Atributos BIM por morph (id, building_material,
                     structural_function, position, renovation_status) y
                     salida layers_json (capas distintas para F1_LAYERS_XML).
  v01   (2026-08-18) - Propuesta inicial: mapeo uso->capa (GuBIMclass),
                     piso->nivel (Story) y manifest.

ENTRADAS (listas paralelas; las de tipo "Item" son unicas):
  morphs          : Geometry/Mesh (List) - Morphs a etiquetar (mismo orden de F3).
  pisos           : int (List)           - Numero de piso por morph (1..N).
  usos            : String (List)        - Uso por morph ("" para losas/nucleo).
  nombres_niveles : String (List)        - [opcional] Nombres reales de los
                                           niveles (Stories) de ArchiCAD, en
                                           orden (indice 0 = piso 1). Si falta,
                                           se usa "Nivel <piso>".
  chip            : String (Item)        - CHIP del predio (para el manifest).
  salida_path     : String (Item)        - Carpeta destino del manifest.
                                           Default: data/fase-3-masa/casos/<chip>/.
  building_material   : String (Item/List) - Material por morph (ArchiCAD).
  structural_function : int   (Item/List) - 0=Load-Bearing, 1=Non-Load-Bearing, 2=Undefined.
  position            : int   (Item/List) - 0=Exterior, 1=Interior, 2=Undefined.
  renovation_status   : int   (Item/List) - 0=Existing, 1=To Be Demolished, 2=New.

SALIDAS:
  layer_names  : String (List) - Capa por morph (paralela a morphs).
  story_names  : String (List) - Nivel por morph (paralela a morphs).
  layers_json  : String        - JSON de capas DISTINTAS (nombre/color/visible).
  manifest_json: String        - Ruta del manifest escrito ("" si falla).
  estado       : String        - Estado/resumen.

FUNCIONES INTERNAS:
  _unwrap(val)      - Aplana listas de GH de un item.
  _piso_int(val)    - Convierte a int a prueba de fallos.
  _layer_de(uso)    - Mapea uso -> capa GuBIMclass (ver LAYER_MAP).
  _story_de(piso, nombres) - Devuelve el nombre del nivel para un piso.
================================================================================
"""

import json
import os
from datetime import date

# Define __file__ if not already defined (for compatibility with environments that don't set it)
try:
    __file__
except NameError:
    import ghpythonlib.component as comp
    __file__ = comp.OnPingDocument().FileName if comp.OnPingDocument() else "unknown"

# ---- Forzar acceso de lista en las salidas 0 (layer_names) y 1 (story_names) ----
try:
    import Grasshopper as gh
    ghenv.Component.Params.Output[0].Access = gh.Kernel.GH_ParamAccess.list   # layer_names
    ghenv.Component.Params.Output[1].Access = gh.Kernel.GH_ParamAccess.list   # story_names
except Exception:
    # Si falla el acceso a Grasshopper, continuar sin forzar el modo de acceso
    # (dependerá de la configuración manual del componente)
    pass

# ---- Tabla de capas: codigos GuBIMclass del proyecto ----------------------
# Formato NN-NN-NN[-NN]_Descripcion (fuente: data/GuBIMclass_Layers_v3.xml,
# generado desde Layers.csv por generate-archicad-layers-xml-v3.py). La masa
# conceptual de F3 se asigna al elemento BIM que representara en F5:
LAYER_MAP = {
    "Vivienda": "30-10-10_Fachadas",               # envolvente vertical
    "Comercio": "30-10-10_Fachadas",
    "Oficinas": "30-10-10_Fachadas",
    "Salud": "30-10-10_Fachadas",
    "Educacion": "30-10-10_Fachadas",
    "Servicios": "20-20-10-30_Muros estructurales",  # nucleo/servicios
    "Nucleo": "20-20-10-40_Escaleras de estructura",  # circulacion vertical
    "Circulacion": "20-20-10-40_Escaleras de estructura",
    "Servicios_Nucleo": "20-20-10-30_Muros estructurales",
    "Losa": "20-20-20-10_Forjados",               # entrepisos
}
# Capa de referencia ya existente en F1_Layers_Proyecto_v01.xml
LAYER_DEFAULT = "00-10-20_Elementos_referencia"
NIVEL_PREFIX = "Nivel "   # fallback cuando no llegan nombres_niveles

# Determine output directory: prefer environment variable, fallback to cwd with warning
try:
    proj_root = os.environ.get('DISENO_PARAMETRICO_ROOT')
    if proj_root:
        DEFAULT_OUT_DIR = os.path.join(proj_root, 'data', 'fase-3-masa', 'casos')
    else:
        # Fallback: use current working directory (hoping it's the project root)
        DEFAULT_OUT_DIR = os.path.join(os.getcwd(), 'data', 'fase-3-masa', 'casos')
        # Try to warn the user
        try:
            import Grasshopper as gh
            ghenv.Component.AddRuntimeMessage(
                gh.Kernel.GH_RuntimeMessageLevel.Warning,
                "Environment variable DISENO_PARAMETRICO_ROOT not set. Using current working directory for output path."
            )
        except Exception:
            pass
except Exception:
    # Last resort: hardcoded path (should not happen in production)
    DEFAULT_OUT_DIR = r"D:\Work\PROJECTS\DiseñoParametrico\data\fase-3-masa\casos"


def _unwrap(val):
    """Aplana listas de GH de un item; None -> lista vacia."""
    if val is None:
        return []
    if isinstance(val, list):
        return val
    return [val]


def _piso_int(val):
    """Convierte a int a prueba de fallos; fallo -> 0."""
    try:
        if val is None or val == "":
            return 0
        return int(round(float(val)))
    except Exception:
        return 0


def _layer_de(uso):
    """Mapea el uso (o categoria especial) a su capa GuBIMclass."""
    key = str(uso or "").strip()
    if key in ("Nucleo", "Circulacion", "Circulacion vertical", "Punto fijo"):
        return LAYER_MAP["Circulacion"]
    if key in ("Servicios", "Servicios tecnicos", "Cuarto tecnico", "Basuras",
               "Ductos"):
        return LAYER_MAP["Servicios_Nucleo"]
    if key in ("Losa", "Losa entrepiso", "Placa"):
        return LAYER_MAP["Losa"]
    if key in LAYER_MAP:
        return LAYER_MAP[key]
    if key == "":
        # sin uso = losa/placa del piso
        return LAYER_MAP["Losa"]
    return LAYER_DEFAULT


def _story_de(piso, nombres):
    """Devuelve el nombre del nivel (Story) para un numero de piso, usando los
    nombres reales de ArchiCAD si estan disponibles."""
    n = _piso_int(piso)
    if nombres and 1 <= n <= len(nombres):
        nombre = str(nombres[n - 1] or "").strip()
        if nombre:
            return nombre
    return NIVEL_PREFIX + str(n) if n >= 1 else NIVEL_PREFIX + "0"


# ------------------------------------------------------------------ helpers 2
def _enum_int(val, default):
    """Entero de enumeracion (0/1/2) a prueba de fallos; invalido -> default."""
    try:
        if val is None or val == "":
            return default
        return int(round(float(val)))
    except Exception:
        return default


def _valor_lista(vals, i, default):
    """Valor por indice: lista paralela a morphs o Item broadcast."""
    if vals is None:
        return default
    if isinstance(vals, list):
        return vals[i] if i < len(vals) else default
    return vals


# ------------------------------------------------------------------ entradas
morphs = globals().get("morphs", None)
pisos = globals().get("pisos", None)
usos = globals().get("usos", None)
nombres_niveles = globals().get("nombres_niveles", None)
chip = globals().get("chip", None)
salida_path = globals().get("salida_path", None)
building_material = globals().get("building_material", None)
structural_function = globals().get("structural_function", None)
position = globals().get("position", None)
renovation_status = globals().get("renovation_status", None)

_morphs = _unwrap(morphs)
_pisos = _unwrap(pisos)
_usos = _unwrap(usos)
_niveles = _unwrap(nombres_niveles)

n = len(_morphs)
layer_names = []
story_names = []
registros = []
for i in range(n):
    piso = _pisos[i] if i < len(_pisos) else 0
    uso = _usos[i] if i < len(_usos) else ""
    layer = _layer_de(uso)
    story = _story_de(piso, _niveles)
    mat = str(_valor_lista(building_material, i, "") or "").strip()
    sf = _enum_int(_valor_lista(structural_function, i, 2), 2)
    pos = _enum_int(_valor_lista(position, i, 2), 2)
    rn = _enum_int(_valor_lista(renovation_status, i, 2), 2)
    layer_names.append(layer)
    story_names.append(story)
    registros.append({
        "id": i + 1,
        "index": i,
        "piso": _piso_int(piso),
        "uso": str(uso or "").strip(),
        "layer": layer,
        "story": story,
        "building_material": mat,
        "structural_function": sf,
        "position": pos,
        "renovation_status": rn,
    })

# Capas DISTINTAS usadas por los morphs (para F1_LAYERS_XML_v02): se exportan
# como [{"nombre","color","visible"}] e importables en ArchiCAD ANTES de
# generar los morphs.
_vistos = []
for r in registros:
    if r["layer"] not in _vistos:
        _vistos.append(r["layer"])
layers_unicos = []
for k, nombre in enumerate(_vistos):
    layers_unicos.append({"nombre": nombre, "color": 20 + k, "visible": True})
layers_json = json.dumps(layers_unicos, ensure_ascii=False)

manifest_json = ""
estado = "OK: {0} morphs etiquetados".format(n)

if n > 0:
    try:
        chip_str = str(chip or "").strip() or "chip"
        carpeta = str(salida_path or "").strip()
        if carpeta == "":
            carpeta = os.path.join(DEFAULT_OUT_DIR, chip_str)
        if not os.path.isdir(carpeta):
            os.makedirs(carpeta)
        ruta = os.path.join(carpeta, "morph-manifest.json")
        payload = {
            "chip": chip_str,
            "generado": date.today().isoformat(),
            "total_morphs": n,
            "_enums": {
                "structural_function": {"0": "Load-Bearing", "1": "Non-Load-Bearing", "2": "Undefined"},
                "position": {"0": "Exterior", "1": "Interior", "2": "Undefined"},
                "renovation_status": {"0": "Existing", "1": "To Be Demolished", "2": "New"},
            },
            "layers": layers_unicos,
            "morphs": registros,
        }
        with open(ruta, "w") as f:
            f.write(json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=True))
        manifest_json = ruta
        estado = "OK: {0} morphs | manifest: {1}".format(n, ruta)
    except Exception as e:
        estado = "ERROR escribiendo manifest: " + str(e)

try:
    ghenv.Component.Message = estado  # noqa: F821 - inyectado por Grasshopper
except Exception:  # noqa: BLE001
    pass
