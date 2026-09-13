# -*- coding: utf-8 -*-
"""
================================================================================
F1_CONTEXTO50_BUILD_v02.py — Construcción de volumetrías vecinas en Rhino
Proyecto: DisenoParametrico / Fase 1
Script de Rhino (rhinoscriptsyntax), se ejecuta en la SESIÓN ABIERTA.
================================================================================

PROPOSITO:
  Lee el mismo JSON de contexto 3D a 50 m (<CHIP>-contexto50.json) que consume
  el componente GHPython `F1_ETAPA3_CONTEXTO50_v01.py`, construye en la sesión
  de Rhino abierta:
    - la huella de cada edificio como polilínea cerrada (plano Z=0),
    - su volumen por extrusión recta en +Z hasta la altura del edificio
      (capado), y
    - los coloca en la capa `70-20-30_Volumetrias_vecinas`.
  Finalmente exporta el resultado a .3dm y .obj.

  Regla de oro (AGENTS.md): el volumen coincide en PERÍMETRO con la huella;
  la extrusión usa la MISMA polilínea cerrada que define la huella.

COMO EJECUTAR EN RHINO (8):
  1. Abrir el archivo .3dm de trabajo (la sesión abierta).
  2. Ajustar JSON_PATH (o dejarlo vacío para autodescubrir *-contexto50.json
     en SEARCH_DIRS).
  3. Pegar y ejecutar con `_EditPythonScript` (F5) o `_-RunPythonScript`.
     Los módulos ya están importados; el script corre al ejecutar el archivo.

FORMATO DEL JSON (idéntico al GHPython):
  {"chip":"...","radio_m":50,"altura_por_piso_m":2.0,
   "edificios":[{"id":"...","vertices":[[x,y],...],"pisos":N,
                 "altura_m":H,"fuente":"..."}]
  El lector acepta chip/radio_m/altura_por_piso_m en la raíz O dentro de
  `metadata` (variante anidada que entrega sub-02), y por edificio acepta
  `vertices` o `anillos` (usa el anillo exterior si hay >1; huecos no modelados).
  Los `vertices` están en COORDENADAS LOCALES DEL CANVAS (marco local del
  contexto vigente); se toman como (x, y) con z = 0.

CONSTANTES CONFIGURABLES:
  JSON_PATH      — ruta explícita al <CHIP>-contexto50.json ("" = autodescubrir).
  SEARCH_DIRS    — carpetas donde autodescubrir el JSON si JSON_PATH == "".
  OUT_DIR        — carpeta destino de .3dm/.obj (default: exports/contexto50).
  MODO_3DM       — "saveas" (según instrucción; CAMBIA el archivo activo de
                   Rhino) o "export" (NO destructivo, exporta la selección a
                   .3dm sin cambiar el documento activo). RIESGO documentado.
  EXPORTAR_3DM   — Boolean, exporta .3dm.
  EXPORTAR_OBJ   — Boolean, exporta .obj (solo los objetos creados).

TOLERANCIAS / FALLBACKS:
  - Vértices repetidos consecutivos y cierre redundante: se deduplican
    (TOL_CIERRE = 0.01 m).
  - Altura: altura_m > 0  ->  pisos * altura_por_piso_m  ->  DEFAULT_ALTURA_M
    (3.0 m, una planta; DOCUMENTADO).
  - Huellas con < 3 vértices únicos: se descartan y se cuentan.

COMPATIBILIDAD: IronPython 2.7 (sin f-strings, sin pathlib, sin type hints,
  sin walrus, sin shebang). `io.open(..., encoding=...)` para leer/escribir.
UNIDADES: metros.
NORMATIVA APLICABLE:
  - Decreto 555/2021 (POT Bogotá) para extracción de construcciones.
  - NSR-10 A.2.5 para alturas de edificios (uso de plantas estándar).
HISTORIAL DE VERSIONES:
  v01 — 2026-09-12: versión inicial.
  v02 — 2026-09-13: Incluido data/pot-cache en SEARCH_DIRS para autodescubrir
                   el JSON generado por F1_CONTEXTO50_FETCH_v01.py.
================================================================================
"""

import os
import io
import json

try:
    import rhinoscriptsyntax as rs
    _RHINO_IMPORT_ERROR = None
except Exception as _e:
    rs = None
    _RHINO_IMPORT_ERROR = _e

try:
    import scriptcontext as sc  # noqa: F401 - suministrado por Rhino
except Exception:
    sc = None


# ------------------------------------------------------------------ constantes
BASE_DIR = r"D:\Work\PROJECTS\DiseñoParametrico"
JSON_PATH = ""  # "" => autodescubrir en SEARCH_DIRS

SEARCH_DIRS = [
    os.path.join(BASE_DIR, "data", "contexto50"),
    os.path.join(BASE_DIR, "data", "fase-1-contexto"),
    os.path.join(BASE_DIR, "data", "pot-cache"),   # <<< AÑADIDO para CONTEXTO50
    os.path.join(BASE_DIR, "exports", "contexto50"),
]

OUT_DIR = os.path.join(BASE_DIR, "exports", "contexto50")

MODO_3DM = "saveas"      # "saveas" (instrucción; cambia el doc activo) | "export"
EXPORTAR_3DM = True
EXPORTAR_OBJ = True

LAYER_VECINOS = "70-20-30_Volumetrias_vecinas"
LAYER_COLOR = (170, 170, 170)     # RGB gris (Morphs de vecinos)

TOL_CIERRE = 0.01                 # [m]
DEFAULT_ALTURA_PISO_M = 2.0       # [m]
DEFAULT_ALTURA_M = 3.0            # [m] fallback (1 planta)


# ------------------------------------------------------------------ utilidades
def leer_json(path):
    """Lectura tolerante: utf-8 primero, latin-1 como respaldo."""
    with io.open(path, "rb") as f:
        raw = f.read()
    try:
        return json.loads(raw.decode("utf-8"))
    except Exception:
        return json.loads(raw.decode("latin-1"))


def to_float(val, default):
    if val is None:
        return default
    try:
        return float(val)
    except (TypeError, ValueError):
        return default


def meta_get(data, key, default=None):
    """Lee una clave en raíz y, si no está, dentro de `metadata`. Ver GHPython."""
    if not isinstance(data, dict):
        return default
    v = data.get(key, None)
    if v is not None:
        return v
    meta = data.get("metadata", None)
    if isinstance(meta, dict):
        v = meta.get(key, None)
        if v is not None:
            return v
    return default


def anillos_de(ed):
    """Anillos del edificio como listas de (x, y); el primero es la huella."""
    out = []
    rings_raw = ed.get("anillos", None)
    if rings_raw:
        for r in rings_raw:
            pts = normalizar_vertices(r)
            if len(pts) >= 3:
                out.append(pts)
    if not out:
        pts = normalizar_vertices(ed.get("vertices", []))
        if len(pts) >= 3:
            out.append(pts)
    return out


def normalizar_vertices(raw):
    """Deduplica consecutivos + cierre redundante. Devuelve [(x, y), ...]."""
    pts = []
    for v in (raw or []):
        try:
            p = (float(v[0]), float(v[1]))
        except (TypeError, ValueError, IndexError):
            continue
        if pts:
            ult = pts[-1]
            if abs(p[0] - ult[0]) <= TOL_CIERRE and abs(p[1] - ult[1]) <= TOL_CIERRE:
                continue
        pts.append(p)
    if len(pts) >= 2:
        a, b = pts[0], pts[-1]
        if abs(a[0] - b[0]) <= TOL_CIERRE and abs(a[1] - b[1]) <= TOL_CIERRE:
            pts.pop()
    return pts


def altura_de(ed, altura_por_piso):
    """Devuelve (altura_m, es_fallback). Ver encabezado."""
    altura = to_float(ed.get("altura_m"), None)
    if altura is not None and altura > 0:
        return altura, False
    pisos = to_float(ed.get("pisos"), None)
    if pisos is not None and pisos > 0 and altura_por_piso > 0:
        return pisos * altura_por_piso, True
    return DEFAULT_ALTURA_M, True


def descobrir_json():
    """Autodescubre el primer *-contexto50.json en SEARCH_DIRS."""
    for d in SEARCH_DIRS:
        if not os.path.isdir(d):
            continue
        try:
            nombres = sorted(os.listdir(d))
        except Exception:
            continue
        for n in nombres:
            if n.lower().endswith("contexto50.json"):
                return os.path.join(d, n)
    return ""


def asegurar_layer(nombre):
    """Crea el layer si no existe; tolerante a fallos."""
    try:
        if not rs.IsLayer(nombre):
            rs.AddLayer(nombre, LAYER_COLOR)
        return True
    except Exception:
        try:
            rs.AddLayer(nombre)
            return True
        except Exception:
            return False


def capar_si_hace_falta(obj_id):
    """Cierra el sólido extruido si quedó abierto (planar holes)."""
    try:
        if rs.IsPolysurface(obj_id):
            if not rs.IsPolysurfaceClosed(obj_id):
                rs.CapPlanarHoles(obj_id)
    except Exception:
        pass


# ==============================================================================
# MAIN
# ==============================================================================

def main():
    if rs is None:
        print("F1_CONTEXTO50_BUILD v02 | ERROR: rhinoscriptsyntax no disponible "
              "(¿{0}?). Ejecutar dentro de Rhino.".format(_RHINO_IMPORT_ERROR))
        return

    # 1) resolver JSON
    ruta_json = JSON_PATH if JSON_PATH else descubrir_json()
    if not ruta_json or not os.path.exists(ruta_json):
        print("F1_CONTEXTO50_BUILD v02 | ERROR: no se encontro el JSON de "
              "contexto50 (JSON_PATH='{0}').".format(JSON_PATH))
        return

    try:
        data = leer_json(ruta_json)
    except Exception as e:
        print("F1_CONTEXTO50_BUILD v02 | ERROR leyendo JSON: {0}".format(str(e)))
        return

    chip = str(meta_get(data, "chip", "") or "")
    radio_m = to_float(meta_get(data, "radio_m"), 0.0)
    altura_por_piso = to_float(meta_get(data, "altura_por_piso_m"), DEFAULT_ALTURA_PISO_M)
    if altura_por_piso <= 0:
        altura_por_piso = DEFAULT_ALTURA_PISO_M
    edificios = data.get("edificios", []) or []

    # 2) layer destino
    layer_ok = asegurar_layer(LAYER_VECINOS)

    # 3) construir
    rs.EnableRedraw(False)
    creados = []
    n_ok = 0
    n_skip = 0
    n_fallback = 0
    alturas = []
    errores = []

    try:
        for ed in edificios:
            ed_id = str(ed.get("id", "") or "")
            anillos = anillos_de(ed)
            if len(anillos) < 1:
                n_skip += 1
                continue
            pts = anillos[0]  # huella exterior (huecos no modelados)

            altura, es_fallback = altura_de(ed, altura_por_piso)
            if es_fallback:
                n_fallback += 1

            try:
                # polilínea cerrada (el último punto coincide con el primero)
                puntos = [[p[0], p[1], 0.0] for p in pts]
                puntos.append([pts[0][0], pts[0][1], 0.0])
                crv_id = rs.AddPolyline(puntos)
                if not crv_id:
                    n_skip += 1
                    errores.append(ed_id or "(sin id)")
                    continue

                # extrusión recta en +Z y capado
                ext_id = rs.ExtrudeCurveStraight(
                    crv_id, [0.0, 0.0, 0.0], [0.0, 0.0, altura])
                if ext_id:
                    capar_si_hace_falta(ext_id)
                    try:
                        rs.DeleteObject(crv_id)  # dejar solo el sólido
                    except Exception:
                        pass
                    if layer_ok:
                        rs.ObjectLayer(ext_id, LAYER_VECINOS)
                    creados.append(ext_id)
                else:
                    # sin extrusión: al menos conservar la huella
                    if layer_ok:
                        rs.ObjectLayer(crv_id, LAYER_VECINOS)
                    creados.append(crv_id)

                alturas.append(altura)
                n_ok += 1
            except Exception as e_ed:
                n_skip += 1
                errores.append("{0}: {1}".format(ed_id or "(sin id)", str(e_ed)))
    finally:
        rs.EnableRedraw(True)

    # 4) exportar
    ruta_3dm = ""
    ruta_obj = ""
    if not os.path.isdir(OUT_DIR):
        try:
            os.makedirs(OUT_DIR)
        except Exception:
            pass
    base = chip if chip else "contexto50"

    if EXPORTAR_3DM and creados:
        ruta_3dm = os.path.join(OUT_DIR, base + "-contexto50.3dm")
        try:
            if MODO_3DM == "saveas":
                rs.Command('_-SaveAs "{0}" _Enter'.format(ruta_3dm), False)
            else:
                rs.SelectObjects(creados)
                rs.Command('_-Export "{0}" _Enter'.format(ruta_3dm), False)
                rs.UnselectAllObjects()
        except Exception as e_3dm:
            print("WARN export .3dm: {0}".format(str(e_3dm)))
            ruta_3dm = ""

    if EXPORTAR_OBJ and creados:
        ruta_obj = os.path.join(OUT_DIR, base + "-contexto50.obj")
        try:
            rs.SelectObjects(creados)
            rs.Command('_-Export "{0}" _Enter'.format(ruta_obj), False)
            rs.UnselectAllObjects()
        except Exception as e_obj:
            print("WARN export .obj: {0}".format(str(e_obj)))
            ruta_obj = ""

    # 5) resumen
    if alturas:
        a_min, a_max = min(alturas), max(alturas)
    else:
        a_min, a_max = 0.0, 0.0

    print("F1_CONTEXTO50_BUILD v02 | CHIP {0} | R {1:.0f}m | Objetos {2} | "
          "Descartados {3} | Fallbacks {4} | Alturas {5:.1f}-{6:.1f}m".format(
              chip or "?", radio_m, n_ok, n_skip, n_fallback, a_min, a_max))
    if errores:
        print("Errores por edificio: {0}".format("; ".join(errores[:20])))
    print("Layer: {0} ({1})".format(LAYER_VECINOS,
                                    "ok" if layer_ok else "NO CREADO"))
    if ruta_3dm:
        print("3dm: {0}".format(ruta_3dm))
    if ruta_obj:
        print("obj: {0}".format(ruta_obj))
    print("JSON: {0}".format(ruta_json))


main()