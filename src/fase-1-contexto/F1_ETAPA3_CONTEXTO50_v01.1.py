# -*- coding: utf-8 -*-
"""
================================================================================
F1_ETAPA3_CONTEXTO50_v01.1.py — Etapa 3 (opcional): Volumetrías del contexto 50 m
Proyecto: DisenoParametrico / Fase 1
GH Python Script para Grasshopper (componente "Script" clásico, IronPython 2.7)
================================================================================

PROPOSITO:
  Tercera etapa OPCIONAL del pipeline F1. Toma el JSON de contexto 3D
  (<CHIP>-contexto50.json) que trae la huella (footprint) de cada edificio
  vecino dentro de un radio de 50 m del predio objetivo, YA EXPRESADA EN
  COORDENADAS LOCALES DEL CANVAS (mismo marco que `vertices_3d_local` del
  contexto vigente) y devuelve:
    - las huellas como polilíneas cerradas (Curve) en el plano Z=0, y
    - los volúmenes como Brep extruidos en +Z hasta la altura de cada edificio.
  Esta es la contraparte "automática + verificable" de la construcción MANUAL
  de Morphs de vecinos que hoy se hace en ArchiCAD (capa
  `70-20-30_Volumetrias_vecinas`). NO reemplaza esa capa: alimenta geometría
  para revisión en Grasshopper / Rhino.

REGLA DE ORO (AGENTS.md):
  El volumen debe coincidir en perímetro con la huella; por eso la extrusión
  usa EXACTAMENTE la misma polilínea cerrada que se publica como huella.

CAMBIOS v01.1 (2026-09-28):
  1. Agregada resolución defensiva del template "CHIP-contexto50.json": si el
     input json_path contiene el template, busca en el directorio un archivo
     *-contexto.json real (excluyendo CHIP-contexto.json) y deriva el nombre
     del contexto50 correspondiente. Permite que el canvas use el template
     sin modificar mientras el orquestador no cree el canónico.
  2. Agregada constante POT_CACHE y función _existe() para soporte de la
     resolución defensiva.
  3. Compatibilidad con orquestador: prioridad a `contexto50-actual.json` (creado
     por fetch-contexto-completo.py) > parámetro json_path > resolución defensiva.
  4. Actualizada referencia al builder: `F1_CONTEXTO50_BUILD_v01b.py`.

ENTRADA (la única imprescindible):
  json_path (String) — Ruta al <CHIP>-contexto50.json. Forma mínima del JSON
  (el lector acepta chip/radio_m/altura_por_piso_m en la raíz O dentro de
  `metadata`, porque sub-02 entrega la variante anidada):
      {
        "chip": "...", "radio_m": 50, "altura_por_piso_m": 2.0,
        "edificios": [
          {"id": "...", "vertices": [[x, y], ...], "pisos": N,
           "altura_m": H, "fuente": "..."}
        ]
      }
  Variante anidada real (sub-02): "metadata":{"chip":..,"radio_m":..,
  "altura_por_piso_m":..}, y cada edificio con "anillos" (lista de anillos)
  además de "vertices". Se usa `vertices` si está; si no, `anillos[0]`.
  Los vértices son [[x, y], ...] (acepta [x, y, z]; se toma z=0 porque el JSON
  ya está en marco local). La polilínea se cierra con tolerancia TOL_CIERRE.
  Limitación documentada: si un edificio trae >1 anillo (patio interior), solo
  se modela la huella exterior; se cuentan en `edificios_con_anillos_extra`.

ENTRADAS OPCIONALES (leídas con globals().get(), con default seguro):
  escribir_stats (Boolean) — Si True, escribe un sidecar
                             <CHIP>-contexto50-stats.json junto al JSON.
                             Default: False.
  stats_path (String)      — Carpeta destino del sidecar. Default: la carpeta
                             del json_path.

SALIDAS:
  huellas_curvas (Curve[]) — Huellas cerradas en Z=0, una por edificio válido.
  volumenes      (Brep[])  — Extrusiones cerradas (capadas) en +Z, una por
                             edificio válido, misma huella.
  layer_name     (String)  — "70-20-30_Volumetrias_vecinas".
  stats_json     (String)  — Métricas: nº de edificios, rango/altura media,
                             área total de huellas, volumen total, fallbacks.
  mensaje        (String)  — Diagnóstico legible.
  ok             (Boolean) — True si se procesó al menos un edificio y no hubo
                             error fatal.

LOGICA / COSAS QUE MANEJA:
  - Vértices repetidos: se deduplican los consecutivos (y el cierre redundante)
    con tolerancia TOL_CIERRE = 0.01 m.
  - Anillos cerrados: si el primer vértice coincide con el último se descarta
    el duplicado y la polilínea se cierra una sola vez.
  - altura_m nula/<=0: se usa `pisos * altura_por_piso_m`; si tampoco hay
    pisos, se usa DEFAULT_ALTURA_M = 3.0 m (una planta, DOCUMENTADO).
  - Huellas con < 3 vértices únicos: se descartan y se registran en el stats.
  - Multi-anillo (patio): solo se modela el anillo exterior (huecos no modelados).
  - Tolerancia/cierre: se fuerza el cierre de la polilínea (MakeClosed) con
    TOL_CIERRE; la extrusión usa la MISMA curva publicada como huella.

UNIDADES: metros (Rhino configurado en metros — regla #11 del proyecto).
COMPATIBILIDAD: IronPython 2.7 (sin f-strings, sin pathlib, sin type hints,
                sin walrus, sin shebang). `import Rhino.Geometry as rg`.

RELACION CON EL RESTO DEL PIPELINE:
  - El builder de Rhino `F1_CONTEXTO50_BUILD_v01b.py` replica esta lógica en la
    sesión abierta y exporta .3dm/.obj.
  - La capa `70-20-30_Volumetrias_vecinas` es la destino de los Morphs de
    vecinos (ver CLAUDE.md, "ArchiCAD Layers").
================================================================================
"""

import Rhino.Geometry as rg
import json
import io
import os


# ------------------------------------------------------------------ constantes
TOL_CIERRE = 0.01                 # [m] deduplicación y cierre de anillos
DEFAULT_ALTURA_PISO_M = 2.0       # [m] altura de piso si el JSON no la trae
DEFAULT_ALTURA_M = 3.0            # [m] fallback sin altura_m ni pisos (1 planta)
LAYER_VECINOS = "70-20-30_Volumetrias_vecinas"
FUENTE_STATS = "F1_ETAPA3_CONTEXTO50_v01.1"
POT_CACHE = os.path.join(os.environ.get("DISENO_PARAMETRICO_ROOT", ""), "data", "pot-cache")


def _existe(path):
    """Verifica si un path existe (wrapper para os.path.exists)."""
    return os.path.exists(path) if path else False


# ------------------------------------------------------------------ utilidades
def unwrap(val):
    """Extrae el primer elemento si Grasshopper envía una lista de 1 item."""
    if val is None:
        return None
    if isinstance(val, list):
        return val[0] if len(val) > 0 else None
    return val


def parse_bool(val):
    """Lee Toggles/Boolean de GH a prueba de fallos."""
    val = unwrap(val)
    if val is None:
        return False
    if isinstance(val, bool):
        return val
    s = str(val).strip().lower()
    return s in ("true", "1", "verdadero", "yes", "si")


def to_float(val, default):
    """Convierte a float; devuelve default si no es numérico."""
    val = unwrap(val)
    if val is None:
        return default
    try:
        return float(val)
    except (TypeError, ValueError):
        return default


def leer_json(path):
    """Lectura tolerante: utf-8 primero, latin-1 como respaldo."""
    with io.open(path, "rb") as f:
        raw = f.read()
    try:
        return json.loads(raw.decode("utf-8"))
    except Exception:
        return json.loads(raw.decode("latin-1"))


def meta_get(data, key, default=None):
    """Lee una clave en el nivel raíz y, si no está, dentro de `metadata`.

    El JSON de sub-02 anida chip/radio_m/altura_por_piso_m en `metadata`;
    la forma mínima del encargo los pone en la raíz. Se aceptan ambas.
    """
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


def _pt_xy(v):
    """Normaliza un vértice [x, y] o [x, y, z] a (x, y); None si inválido."""
    if v is None:
        return None
    try:
        return (float(v[0]), float(v[1]))
    except (TypeError, ValueError, IndexError):
        return None


def normalizar_vertices(raw):
    """Deduplica consecutivos + cierre redundante. Devuelve lista de (x, y)."""
    pts = []
    for v in (raw or []):
        p = _pt_xy(v)
        if p is None:
            continue
        if pts:
            ult = pts[-1]
            if abs(p[0] - ult[0]) <= TOL_CIERRE and abs(p[1] - ult[1]) <= TOL_CIERRE:
                continue  # vértice repetido consecutivo
        pts.append(p)
    # quitar cierre redundante (primer == último)
    if len(pts) >= 2:
        a, b = pts[0], pts[-1]
        if abs(a[0] - b[0]) <= TOL_CIERRE and abs(a[1] - b[1]) <= TOL_CIERRE:
            pts.pop()
    return pts


def construir_huella(pts):
    """Devuelve una PolylineCurve cerrada en Z=0 desde puntos (x, y) o None."""
    if not pts or len(pts) < 3:
        return None
    pl = rg.Polyline()
    for p in pts:
        pl.Add(p[0], p[1], 0.0)
    pl.Add(pts[0][0], pts[0][1], 0.0)  # cierre explícito
    try:
        crv = rg.PolylineCurve(pl)
    except Exception:
        return None
    if crv is None:
        return None
    try:
        crv.MakeClosed(TOL_CIERRE)
    except Exception:
        pass
    return crv


def extruir(crv, altura):
    """Extrusión capada en +Z; devuelve Brep o None."""
    if crv is None or altura <= 0:
        return None
    try:
        ext = rg.Extrusion.Create(crv, altura, True)
    except Exception:
        return None
    if ext is None:
        return None
    try:
        brp = ext.ToBrep()
    except Exception:
        return None
    return brp


def area_curva(crv):
    """Área de la huella cerrada (m2); 0.0 si no se puede calcular."""
    try:
        amp = rg.AreaMassProperties.Compute(crv)
        if amp is not None:
            return float(amp.Area)
    except Exception:
        pass
    return 0.0


def volumen_brep(brp):
    """Volumen del Brep (m3); 0.0 si no se puede calcular."""
    try:
        vmp = rg.VolumeMassProperties.Compute(brp)
        if vmp is not None:
            return float(vmp.Volume)
    except Exception:
        pass
    return 0.0


def anillos_de(ed):
    """Anillos del edificio como listas de (x, y). El primero es la huella.

    Acepta `anillos` (lista de anillos, forma de sub-02) con `vertices` como
    respaldo; hoy el dato real trae 1 anillo y vertices == anillos[0].
    """
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


def altura_de(ed, altura_por_piso):
    """Altura del edificio + flag de fallback.

    Prioridad: altura_m > 0  ->  pisos * altura_por_piso_m  ->  DEFAULT_ALTURA_M.
    Devuelve (altura_m, es_fallback).
    """
    altura = to_float(ed.get("altura_m"), None)
    if altura is not None and altura > 0:
        return altura, False
    pisos = to_float(ed.get("pisos"), None)
    if pisos is not None and pisos > 0 and altura_por_piso > 0:
        return pisos * altura_por_piso, True
    return DEFAULT_ALTURA_M, True


# ==============================================================================
# MAIN
# ==============================================================================

# --- salidas con default (evita NameError si algo falla) ---
huellas_curvas = []
volumenes = []
layer_name = LAYER_VECINOS
stats_json = "{}"
mensaje = ""
ok = False

# Get json_path parameter with fallback to canonical file
raw_path = globals().get("json_path", None)
json_path_param = str(unwrap(raw_path)).strip("[]'\" ") if raw_path is not None else ""

# Check for canonical file first (for orchestrator-managed workflow)
canonical_path = os.path.join(POT_CACHE, "contexto50-actual.json")
json_path = canonical_path if _existe(canonical_path) else json_path_param

# Fallback logic: if canonical doesn't exist or is empty, use parameter
if not json_path or not _existe(json_path):
    json_path = json_path_param

# DEFENSIVA: si el path contiene el template "CHIP", intentar resolver el CHIP real
# desde el archivo hermano CHIP-contexto.json en el mismo directorio
if json_path and "CHIP-contexto50.json" in json_path.upper():
    try:
        # Buscar archivo hermano CHIP-contexto.json en el mismo directorio
        dir_base = os.path.dirname(json_path) or POT_CACHE
        for f in os.listdir(dir_base):
            if f.upper().endswith("-CONTEXTO.JSON") and not f.upper().startswith("CHIP-"):
                chip_real = f[:-12]  # quitar "-contexto.json"
                candidato = os.path.join(dir_base, chip_real + "-contexto50.json")
                if _existe(candidato):
                    json_path = candidato
                    break
    except Exception:
        pass  # si falla, seguir con el path original (dará error claro después)

escribir_stats = parse_bool(globals().get("escribir_stats", False))
stats_path = unwrap(globals().get("stats_path", None))

if not json_path or not _existe(json_path):
    mensaje = "ETAPA3 v01 | ERROR: no se encontro el JSON de contexto50: {0}".format(json_path)
else:
    try:
        data = leer_json(json_path)

        chip = str(meta_get(data, "chip", "") or "")
        radio_m = to_float(meta_get(data, "radio_m"), 0.0)
        altura_por_piso = to_float(meta_get(data, "altura_por_piso_m"), DEFAULT_ALTURA_PISO_M)
        if altura_por_piso <= 0:
            altura_por_piso = DEFAULT_ALTURA_PISO_M
        edificios = data.get("edificios", []) or []

        alturas = []
        areas = []
        volumen_total = 0.0
        n_fallback = 0
        n_anillos_extra = 0
        descartados = []
        detalle = []

        for ed in edificios:
            ed_id = str(ed.get("id", "") or "")
            anillos = anillos_de(ed)
            n_anillos = len(anillos)
            if n_anillos > 1:
                n_anillos_extra += 1

            if n_anillos < 1:
                descartados.append(ed_id or "(sin id)")
                continue
            pts = anillos[0]  # huella exterior (los huecos no se modelan)

            crv = construir_huella(pts)
            if crv is None:
                descartados.append(ed_id or "(sin id)")
                continue

            altura, es_fallback = altura_de(ed, altura_por_piso)
            if es_fallback:
                n_fallback += 1

            brp = extruir(crv, altura)

            area_m2 = area_curva(crv)
            vol_m3 = volumen_brep(brp) if brp is not None else 0.0

            huellas_curvas.append(crv)
            if brp is not None:
                volumenes.append(brp)

            alturas.append(altura)
            areas.append(area_m2)
            volumen_total += vol_m3

            detalle.append({
                "id": ed_id,
                "altura_m": round(altura, 3),
                "pisos": to_float(ed.get("pisos"), None),
                "area_m2": round(area_m2, 3),
                "volumen_m3": round(vol_m3, 3),
                "n_anillos": n_anillos,
                "fuente": str(ed.get("fuente", "") or ""),
                "cerrado": True,
                "fallback_altura": es_fallback,
            })

        n_total = len(edificios)
        n_ok = len(huellas_curvas)
        area_total = sum(areas)

        if alturas:
            altura_min = min(alturas)
            altura_max = max(alturas)
            altura_prom = sum(alturas) / float(len(alturas))
        else:
            altura_min = 0.0
            altura_max = 0.0
            altura_prom = 0.0

        stats = {
            "chip": chip,
            "fuente_stats": FUENTE_STATS,
            "radio_m": round(radio_m, 3),
            "altura_por_piso_m": round(altura_por_piso, 3),
            "edificios_total": n_total,
            "edificios_ok": n_ok,
            "edificios_descartados": len(descartados),
            "ids_descartados": descartados,
            "altura_min_m": round(altura_min, 3),
            "altura_max_m": round(altura_max, 3),
            "altura_promedio_m": round(altura_prom, 3),
            "altura_fallbacks": n_fallback,
            "edificios_con_anillos_extra": n_anillos_extra,
            "area_huellas_m2": round(area_total, 3),
            "volumen_total_m3": round(volumen_total, 3),
            "layer_destino": LAYER_VECINOS,
            "edificios": detalle,
        }
        stats_json = json.dumps(stats, ensure_ascii=False, indent=2)

        ok = n_ok > 0
        mensaje = (
            "ETAPA3 v01 | CHIP {0} | R {1:.0f}m | Edificios {2}/{3} | "
            "Alturas {4:.1f}-{5:.1f}m | Area huellas {6:.1f}m2 | "
            "Vol {7:.1f}m3 | Fallbacks altura {8}"
        ).format(chip or "?", radio_m, n_ok, n_total,
                 altura_min, altura_max, area_total, volumen_total, n_fallback)

        # --- sidecar opcional (io.open utf-8, regla del proyecto) ---
        if escribir_stats and chip:
            try:
                carpeta = stats_path
                if carpeta is None or str(carpeta).strip() == "":
                    carpeta = os.path.dirname(json_path)
                carpeta = str(carpeta).strip()
                if not os.path.isdir(carpeta):
                    os.makedirs(carpeta)
                ruta_stats = os.path.join(carpeta, chip + "-contexto50-stats.json")
                with io.open(ruta_stats, "w", encoding="utf-8") as f:
                    f.write(stats_json)
                mensaje += " | stats: " + ruta_stats
            except Exception as e_stats:
                mensaje += " | WARN stats no escrito: " + str(e_stats)

    except Exception as e:
        ok = False
        mensaje = "ETAPA3 v01 | ERROR al procesar el JSON: {0}".format(str(e))

try:
    ghenv.Component.Message = mensaje  # noqa: F821 - inyectado por Grasshopper
except Exception:
    pass
