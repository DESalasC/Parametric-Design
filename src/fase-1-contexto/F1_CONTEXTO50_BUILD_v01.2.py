# -*- coding: utf-8 -*-
"""
================================================================================
F1_CONTEXTO50_BUILD_v01.3.py — Construcción de volumetrías vecinas en Rhino / GH
Proyecto: DisenoParametrico / Fase 1
Componente GHPython (componente "Script" clásico, IronPython 2.7) para el canvas
ArchiCAD–Grasshopper (Live Connection).

PROPOSITO:
  Lee el JSON de contexto 50 m (<CHIP>-contexto50.json) y construye, por cada
  edificio vecino:
    - la HUELLA como polilínea cerrada (Curve) a la cota base del edificio
      (z_base_m del registro; Z=0 si no existe), y
    - el VOLUMEN como Brep extruido y capado en +Z hasta su altura.
  La salida `volumenes` alimenta los componentes AC_* (Morphs) del
  Grasshopper-ArchiCAD Live Connection; `bake` la deja además en la capa
  `70-20-30_Volumetrias_vecinas` de Rhino; `exportar` escribe el .3dm.

  REGLA DE ORO (AGENTS.md): el volumen coincide en PERÍMETRO con la huella;
  la extrusión usa EXACTAMENTE la misma polilínea cerrada publicada.

CORRECCION Z (2026-10-18):
  Contexto50 convertido al mismo datum del mesh de ETAPA1 leyendo el JSON
  hermano del mismo CHIP. z_origen=0 para entradas locales de F3.
  desplazamiento_z conserva el offset realmente restado a z_base_m.

CAMBIOS v01.3 (2026-10-13):
  1. Z_BASE CORRECTO (Mínimo Z válido del terreno): `compute_dz_from_stage1_context()`
     ahora usa prioridad: min_z válido malla terreno (punto más bajo lote) ->
     promedio vecinos N/S -> ancla SE -> 0.0. El `desplazamiento_z` resultante
     es Z_base (~0.03m), NO la cota SE (14.52m).
  2. Coherencia total: `desplazamiento_z` = Z_base para que terreno, vecinos
     y volúmenes compartan MISMO sistema local (SE = 0,0,0; Z local = Z_abs - Z_base).

CAMBIOS v01.2 (2026-10-08):
  1. Versionado correcto: subversión v<major>.<minor> (antes v01b).
  2. Función `altura_de()` ya retorna (altura_m, pisos, es_fallback, z_base_m)
     como 4-tupla; la cota base se lee dentro de la función (no fuera).
  3. Diagnóstico por edificio en `mensaje`: muestra z_base, altura, pisos por cada vecino.

CORRECCIONES v01c (2026-09-28, noche):
  1. Fix de la resolución defensiva del template (introducida en v01b): la
     condición ahora es case-insensitive (`"chip-contexto50.json" in
     in_json_path.lower()`) y el corte del CHIP usa f[:-14] ("-contexto.json"
     mide 14). Antes la rama nunca disparaba (patrón en minúsculas contra un
     path en MAYÚSCULAS) y [:-12] derivaba "AAA...-c" (candidato inexistente).
  2. Contraparte F1_ETAPA3_CONTEXTO50 (v01.2) sincronizada con el mismo fix y
     paridad de exclusiones; re-embebido en el canvas v11 (F1_CONTEXTO_v11).

MEJORAS v01d (2026-09-28, noche):
  1. COTA BASE POR EDIFICIO (z_base_m): si el registro trae z_base_m (lo agrega
     scripts/utilities/anclar_contexto50_zbase.py muestreando el MDT), la huella
     se eleva a esa cota y la extrusión parte de ahí; sin z_base_m el comportamiento
     es idéntico al v01c (z=0). Paridad con F1_ETAPA3_CONTEXTO50 (v01.3).
     En lotes inclinados evita que todos los volúmenes queden al nivel 0.0.

CORRECCIONES v01a (revisión 2026-09-13, alineada con F1_ETAPA3_CONTEXTO50_v01):
  1. `unwrap()` en TODAS las entradas: GH puede entregar la entrada como lista
     de 1 ítem; antes `os.path.isfile("[u'...']")` fallaba y no salía nada.
  2. SIN escalado de unidades: el proyecto trabaja en METROS (regla #11 de
     CLAUDE.md). La versión anterior multiplicaba x1000 si el doc estaba en mm
     y generaba geometría 1000x / inconsistente con el canvas.
  3. Se restaura la deduplicación de vértices (consecutivos y cierre
     redundante, TOL_CIERRE = 0.01 m) que la v01 tenía y la v01a perdió:
     los segmentos degenerados rompían el capado y omitían edificios.
  4. Extrusión vía `Extrusion.Create(crv, h, True).ToBrep()` (misma huella
     publicada), en vez de loft + CapPlanarHoles (frágil).
  5. try/except POR EDIFICIO: un registro defectuoso ya no mata todo el
     componente (antes: 0 volúmenes por un solo dato malo).
  6. Lecturas a prueba de GH: `to_float` / `parse_bool` (antes un input
     no numérico en `altura_piso` lanzaba TypeError y rojiaba el componente).
  7. `altura_por_piso_m` del JSON manda (regla ConNPisos*3.80 del fetch);
     el input `altura_piso` es override manual solo si el JSON no la trae.
  8. Diagnóstico en `mensaje` + `ghenv.Component.Message`; aviso si el doc
     de Rhino NO está en metros.
  9. Sentido del anillo forzado a ANTIHORARIO antes de extruir: los anillos
     del fetch GIS vienen horarios y extruían hacia abajo (alturas negativas
     respecto al terreno).
  10. EXCLUSIONES de contexto (2026-09-13):
     a) PREDIO DE REFERENCIA: los registros cuya huella cae dentro del lote
        objetivo NO se modelan (es el lote a disekar). El lote se lee del
        CHIP-contexto.json hermano (lote_objetivo.vertices_3d_local, marco
        ETAPA1) y se transforma al marco local del contexto50 con
        metadata.ancla_canvas_local.
     b) CONSTRUCCIONES MENORES (andenes, anexos, muretes): area <
        MIN_AREA_EDIFICIO_M2 (15 m2) o compacidad > MAX_COMPACIDAD (6.0)
        no generan volumen; se cuentan en el mensaje.

Inputs:
  json_path  (String)  — ruta al <CHIP>-contexto50.json (raíz o metadata anidada)
  altura_piso (Number) — override altura por piso [m]; default: la del JSON o 2.0
  bake       (Boolean) — bake de los volúmenes a la capa 70-20-30_Volumetrias_vecinas
  exportar   (Boolean) — exporta exports/contexto50/<CHIP>-contexto50.3dm

Outputs:
  volumenes (Brep[]) · huellas (Curve[]) · alturas (m[]) · pisos (int[])
  ids (String[]) · capa (String) · mensaje (String) · out (impreso)
  desplazamiento_z (Number) — Z_base para alinear con F3_VOLUM_GENERADOR (z_origin)

COMPATIBILIDAD: IronPython 2.7 (sin f-strings, sin pathlib, sin type hints).
UNIDADES: metros (regla #11).
================================================================================
"""

import os
import io
import json
import math
import System
import System.Drawing
import Rhino
import Rhino.Geometry as rg

# ------------------------------------------------------------------ constantes
TOL_CIERRE = 0.01                 # [m] deduplicación y cierre de anillos
DEFAULT_ALTURA_PISO_M = 2.0       # [m] si el JSON no trae altura_por_piso_m
DEFAULT_ALTURA_M = 3.0            # [m] fallback sin altura_m ni pisos (1 planta)
LAYER_VECINOS = "70-20-30_Volumetrias_vecinas"
OUT_DIR = r"D:\Work\PROJECTS\DiseñoParametrico\exports\contexto50"
MIN_AREA_EDIFICIO_M2 = 15.0       # [m2] area minima para volumen de vecino
MAX_COMPACIDAD = 6.0              # per^2/(4*pi*area): >6 = anden/muro/cinta
CTX1_HERMANO = "CHIP-contexto.json"  # lote objetivo (convencion canvas)
POT_CACHE = os.path.join(os.environ.get("DISENO_PARAMETRICO_ROOT", ""), "data", "pot-cache")


# ------------------------------------------------------------------ utilidades
def unwrap(val):
    """Extrae el primer elemento si Grasshopper envía una lista de 1 ítem."""
    if val is None:
        return None
    if isinstance(val, (list, tuple)):
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


def _existe(path):
    """Verifica si un path existe (wrapper para os.path.exists)."""
    return os.path.exists(path) if path else False


def leer_json(path):
    """Lectura tolerante: utf-8 primero, latin-1 como respaldo."""
    with io.open(path, "rb") as f:
        raw = f.read()
    try:
        return json.loads(raw.decode("utf-8"))
    except Exception:
        return json.loads(raw.decode("latin-1"))


def meta_get(data, key, default=None):
    """Lee una clave en raíz y, si no está, dentro de `metadata`."""
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
    if isinstance(v, dict):
        try:
            return (float(v["x"]), float(v["y"]))
        except Exception:
            return None
    try:
        return (float(v[0]), float(v[1]))
    except (TypeError, ValueError, IndexError):
        return None


def normalizar_vertices(raw):
    """Deduplica consecutivos + cierre redundante. Devuelve [(x, y), ...]."""
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


def extraer_anillos(ed):
    """Anillos del edificio como listas de (x, y). El primero es la huella.

    Acepta la forma real del fetch (sub-02): `anillos` (lista de anillos) y
    `vertices`; también variantes GeoJSON (`geometry.coordinates`).
    """
    out = []
    rings_raw = None
    if isinstance(ed, dict):
        for k in ("anillos", "rings"):
            if k in ed and isinstance(ed[k], list) and ed[k]:
                rings_raw = ed[k]
                break
        if rings_raw:
            for r in rings_raw:
                pts = normalizar_vertices(r)
                if len(pts) >= 3:
                    out.append(pts)
        if not out:
            for k in ("vertices", "polygon", "coords", "coordenadas", "points", "puntos"):
                if k in ed and isinstance(ed[k], list) and ed[k]:
                    pts = normalizar_vertices(ed[k])
                    if len(pts) >= 3:
                        out.append(pts)
                    break
        if not out and isinstance(ed.get("geometry"), dict):
            geom = ed["geometry"]
            coords = geom.get("coordinates", None)
            gtype = str(geom.get("type", ""))
            if gtype == "Polygon" and coords:
                for r in coords:
                    pts = normalizar_vertices(r)
                    if len(pts) >= 3:
                        out.append(pts)
                        break  # solo anillo exterior
            elif gtype == "MultiPolygon" and coords:
                for poly in coords:
                    if poly:
                        pts = normalizar_vertices(poly[0])
                        if len(pts) >= 3:
                            out.append(pts)
                            break  # primer polígono, anillo exterior
    return out


def altura_de(ed, altura_por_piso):
    """Devuelve (altura_m, pisos, es_fallback, z_base_m).

    Prioridad:
      1. altura_m > 0 (del JSON, catastral) + z_base_m opcional
      2. pisos * altura_por_piso (si no hay altura_m) + z_base_m opcional
      3. DEFAULT_ALTURA_M (fallback)
    `z_base_m` = None cuando el registro no trae cota MDT: el llamador decide el
    fallback (no se inventa 0.0, que tras el desplazamiento Z de ETAPA1 elevaba
    todos los morphs 14,5 m sobre el terreno - fallo 2026-10-26).
    """
    altura = to_float(ed.get("altura_m"), None)
    z_base = to_float(ed.get("z_base_m"), None)  # cota base del edificio (MDT muestreado)
    pisos_raw = to_float(ed.get("pisos"), None)

    if altura is not None and altura > 0:
        p = int(round(pisos_raw)) if (pisos_raw is not None and pisos_raw > 0) \
            else max(1, int(round(altura / altura_por_piso)))
        return altura, p, False, z_base
    if pisos_raw is not None and pisos_raw > 0 and altura_por_piso > 0:
        p = int(round(pisos_raw))
        return p * altura_por_piso, p, True, z_base
    # fallback total
    return DEFAULT_ALTURA_M, 1, True, z_base


def _area_compacidad(pts):
    """(area m2, compacidad per^2/(4*pi*area)) de un anillo (x, y)."""
    a = 0.0
    per = 0.0
    n = len(pts)
    for i in range(n):
        x1, y1 = pts[i][0], pts[i][1]
        x2, y2 = pts[(i + 1) % n][0], pts[(i + 1) % n][1]
        a += x1 * y2 - x2 * y1
        per += math.hypot(x2 - x1, y2 - y1)
    area = abs(a) / 2.0
    comp = (per * per) / (4.0 * math.pi * area) if area > 0 else 999.0
    return area, comp


def _punto_en_poligono(x, y, poly):
    """Ray casting; poly = [(x, y), ...] sin punto de cierre repetido."""
    dentro = False
    n = len(poly)
    j = n - 1
    for i in range(n):
        xi, yi = poly[i][0], poly[i][1]
        xj, yj = poly[j][0], poly[j][1]
        if ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / ((yj - yi) or 1e-12) + xi):
            dentro = not dentro
        j = i
    return dentro


def cargar_lote_objetivo(json_path, data_c50):
    """Lote del predio objetivo en el marco LOCAL del contexto50.

    Lee el CHIP-contexto.json hermano (convencion canvas del instructivo),
    toma lote_objetivo.vertices_3d_local (marco ETAPA1) y lo transforma al
    marco local del contexto50 restando metadata.ancla_canvas_local.
    Devuelve ([(x, y), ...] o None, nota_diagnostico).
    """
    try:
        carpeta = os.path.dirname(json_path or "")
        ruta_ctx1 = os.path.join(carpeta, CTX1_HERMANO)
        if not os.path.isfile(ruta_ctx1):
            return None, "sin {0} en {1}".format(CTX1_HERMANO, carpeta)
        c1 = leer_json(ruta_ctx1)
        lo = c1.get("lote_objetivo") if isinstance(c1, dict) else None
        pts = []
        if isinstance(lo, dict):
            for v in (lo.get("vertices_3d_local") or lo.get("vertices") or []):
                p = _pt_xy(v)
                if p is not None:
                    pts.append(p)
        if len(pts) < 3:
            return None, "sin lote_objetivo valido en " + CTX1_HERMANO
        if len(pts) >= 2 and abs(pts[0][0] - pts[-1][0]) <= TOL_CIERRE \
                and abs(pts[0][1] - pts[-1][1]) <= TOL_CIERRE:
            pts.pop()
        meta = data_c50.get("metadata") if isinstance(data_c50, dict) else None
        ancla = meta.get("ancla_canvas_local") if isinstance(meta, dict) else None
        ax = to_float(ancla.get("x"), None) if isinstance(ancla, dict) else None
        ay = to_float(ancla.get("y"), None) if isinstance(ancla, dict) else None
        if ax is None or ay is None:
            return pts, "sin ancla en metadata; lote asumido en mismo marco"
        return [(p[0] - ax, p[1] - ay) for p in pts], ""
    except Exception as e:
        return None, "lote no cargado: {0}".format(str(e))


def compute_dz_from_stage1_context(in_json_path, data):
    """Offset entre contexto50 (Z_abs-z_ref) y mesh de ETAPA1 (Z_abs-Z_base).
    Se reproduce la seleccion de Z_base de F1_ETAPA1_CONTEXTO_v02.
    No se fuerza el terreno inclinado ni el vertice SE a Z=0.
    """
    meta = data.get("metadata", {}) or {}
    origen = meta.get("origen_sirgas", {}) or {}
    ancla_z = to_float((meta.get("ancla_canvas_local", {}) or {}).get("z"), 0.0)
    origen_z = to_float(origen.get("z"), 0.0)
    ref = to_float((meta.get("z_base_fuente", {}) or {}).get("z_ref_m"),
                   origen_z + ancla_z)
    chip_actual = meta.get("chip", "")
    stage_path = os.path.join(os.path.dirname(in_json_path), chip_actual + "-contexto.json")
    # Sin contexto hermano no se asume otro origen (antes lanzaba IOError y el
    # componente devolvia 0 volumenes con ERROR en el mensaje).
    stage = leer_json(stage_path) if os.path.isfile(stage_path) else {}
    stage_meta = stage.get("metadata", {}) or {}
    stage_origen_z = to_float((stage_meta.get("origen_sirgas", {}) or {}).get("z"), 0.0)
    pts = (stage.get("topografia", {}) or {}).get("malla_terreno", []) or []
    valid_z = [to_float(p.get("z_local"), 0.0) for p in pts]
    valid_z = [z for z in valid_z if abs(z) > 0.001]
    min_z = min(valid_z) if valid_z else 0.0
    verts = (stage.get("lote_objetivo", {}) or {}).get("vertices_3d_local", []) or []
    anchor = None
    if len(verts) >= 3:
        anchor = verts[0]
        for v in verts:
            if v[1] < anchor[1] - 0.01 or (abs(v[1] - anchor[1]) < 0.01 and v[0] > anchor[0]):
                anchor = v
    norte, sur = [], []
    lot_y = anchor[1] if anchor is not None else 0.0
    for vecino in stage.get("vecinos", []) or []:
        vv = vecino.get("vertices_3d_local", []) or []
        if len(vv) < 3:
            continue
        vy = sum(v[1] for v in vv) / len(vv)
        vz = sum(v[2] for v in vv) / len(vv)
        if abs(vz) > 0.001:
            if vy > lot_y:
                norte.append((vy-lot_y, vz))
            elif vy < lot_y:
                sur.append((lot_y-vy, vz))
    if min_z > 0.0:
        base = min_z
    elif norte and sur:
        base = sorted(norte)[0][1] / 2.0 + sorted(sur)[0][1] / 2.0
    elif anchor is not None:
        base = anchor[2]
    else:
        base = 0.0
    # z_ajustado = z_base_m - offset = Z_abs - (origen_stage_z + base).
    return stage_origen_z + base - ref



def _es_horario(pts):
    """True si el anillo (x, y) esta en sentido horario (area con signo < 0)."""
    s = 0.0
    n = len(pts)
    for i in range(n):
        x1, y1 = pts[i]
        x2, y2 = pts[(i + 1) % n]
        s += x1 * y2 - x2 * y1
    return s < 0.0


def construir_huella(pts, z_base=0.0):
    """PolylineCurve cerrada a la cota z_base desde [(x, y), ...]; None si no se puede.

    v01d: z_base = cota base del edificio (z_base_m del JSON; 0.0 si falta).
    Fuerza sentido ANTIHORARIO: Extrusion.Create extruye segun la normal del
    plano de la curva; un anillo horario (como el que entrega el fetch GIS)
    tiene normal -Z y el volumen crece DEBAJO del terreno.
    """
    if not pts or len(pts) < 3:
        return None
    if _es_horario(pts):
        pts = list(reversed(pts))
    pl = rg.Polyline()
    for p in pts:
        pl.Add(p[0], p[1], z_base)
    pl.Add(pts[0][0], pts[0][1], z_base)  # cierre explícito (regla de oro)
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
    """Extrusión capada en +Z; devuelve Brep o None. Misma huella -> mismo perímetro."""
    if crv is None or altura is None or altura <= 0:
        return None
    try:
        ext = rg.Extrusion.Create(crv, altura, True)
    except Exception:
        ext = None
    if ext is None:
        return None
    try:
        brp = ext.ToBrep()
        if brp is not None and brp.IsValid:
            return brp
        return brp
    except Exception:
        return None


# ==============================================================================
# ENTRADAS (a prueba de GH: unwrap + tipos seguros)
# ==============================================================================
_raw_path = unwrap(globals().get("json_path", None))
json_path_param = str(_raw_path).strip("[]'\" ") if _raw_path is not None else ""

# Check for canonical file first (for orchestrator-managed workflow)
canonical_path = os.path.join(POT_CACHE, "contexto50-actual.json")
in_json_path = canonical_path if _existe(canonical_path) else json_path_param

# Fallback logic: if canonical doesn't exist or is empty, use parameter
if not in_json_path or not _existe(in_json_path):
    in_json_path = json_path_param

# DEFENSIVA: si el path contiene el template "CHIP", intentar resolver el CHIP real
# desde el archivo hermano CHIP-contexto.json en el mismo directorio
if in_json_path and "chip-contexto50.json" in in_json_path.lower():
    try:
        # Buscar archivo hermano CHIP-contexto.json en el mismo directorio
        dir_base = os.path.dirname(in_json_path) or POT_CACHE
        for f in os.listdir(dir_base):
            if f.upper().endswith("-CONTEXTO.JSON") and not f.upper().startswith("CHIP-"):
                chip_real = f[:-14]  # quitar "-contexto.json" (14 chars)
                candidato = os.path.join(dir_base, chip_real + "-contexto50.json")
                if _existe(candidato):
                    in_json_path = candidato
                    break
    except Exception:
        pass  # si falla, seguir con el path original (dará error claro después)
in_bake = parse_bool(globals().get("bake", False))
in_exportar = parse_bool(globals().get("exportar", False))
in_altura_override = to_float(globals().get("altura_piso", None), None)

# ==============================================================================
# SALIDAS (inicialización — evita NameError si algo falla)
# ==============================================================================
volumenes = []
huellas = []
alturas = []
pisos = []
ids = []
capa = LAYER_VECINOS
mensaje = ""
desplazamiento_z = 0.0

if not in_json_path:
    mensaje = "CONTEXTO50_BUILD | ALERTA: input 'json_path' no conectado."
elif not os.path.isfile(in_json_path):
    mensaje = "CONTEXTO50_BUILD | ERROR: archivo no encontrado: {0}".format(in_json_path)
else:
    try:
        data = leer_json(in_json_path)

        chip = str(meta_get(data, "chip", "") or "contexto")
        radio_m = to_float(meta_get(data, "radio_m"), 0.0)
        # El JSON manda (regla ConNPisos*3.80); el input es override si falta.
        altura_por_piso = to_float(meta_get(data, "altura_por_piso_m"), None)
        if altura_por_piso is None or altura_por_piso <= 0:
            altura_por_piso = in_altura_override if (in_altura_override and in_altura_override > 0) \
                else DEFAULT_ALTURA_PISO_M

        # Registros en la clave conocida (tolerante a variantes)
        edificios = []
        if isinstance(data, list):
            edificios = data
        elif isinstance(data, dict):
            for clave in ("edificios", "vecinos", "predios_vecinos", "volumetrias", "features"):
                v = data.get(clave, None)
                if isinstance(v, list) and len(v) > 0:
                    edificios = v
                    break

        n_total = len(edificios)
        n_skip = 0
        n_fallback = 0
        n_predio = 0
        n_menores = 0
        n_sin_cota = 0
        descartados = []
        zbs = []

        lote_local, nota_lote = cargar_lote_objetivo(in_json_path, data)
        
        # Calcular el desplazamiento Z desde el contexto de etapa 1 (mismo que F1_ETAPA1_CONTEXTO_v02.py)
        desplazamiento_z = compute_dz_from_stage1_context(in_json_path, data)

        for idx, ed in enumerate(edificios):
            ed_id = ""
            try:
                if not isinstance(ed, dict):
                    n_skip += 1
                    continue
                ed_id = str(ed.get("id", "") or ed.get("chip", "") or ed.get("codigo", "")
                            or "vecino_{:03d}".format(idx + 1))
                anillos = extraer_anillos(ed)
                if not anillos:
                    descartados.append(ed_id or "(sin id)")
                    n_skip += 1
                    continue
                pts = anillos[0]  # huella exterior (huecos no modelados)

                # --- exclusion a): construcciones del predio de referencia ---
                if lote_local is not None:
                    cx = sum(pp[0] for pp in pts) / len(pts)
                    cy = sum(pp[1] for pp in pts) / len(pts)
                    if _punto_en_poligono(cx, cy, lote_local):
                        n_predio += 1
                        n_skip += 1
                        continue

                # --- exclusion b): construcciones menores (andenes/anexos/muretes)
                area_m2, comp = _area_compacidad(pts)
                if area_m2 < MIN_AREA_EDIFICIO_M2 or comp > MAX_COMPACIDAD:
                    n_menores += 1
                    n_skip += 1
                    continue

                altura, p, es_fallback, z_base = altura_de(ed, altura_por_piso)
                if es_fallback:
                    n_fallback += 1

                # Apply the stage1 context Z displacement to align with F1_ETAPA1_CONTEXTO_v02.py
                # Sin cota MDT no se aplica el desplazamiento: el volumen queda en el
                # datum de ETAPA1 (0.0) y se avisa, en vez de flotar +desplazamiento.
                if z_base is None:
                    n_sin_cota += 1
                    z_base_ajustado = 0.0
                else:
                    z_base_ajustado = z_base - desplazamiento_z

                crv = construir_huella(pts, z_base_ajustado)
                if crv is None:
                    descartados.append(ed_id or "(sin id)")
                    n_skip += 1
                    continue

                brp = extruir(crv, altura)
                if brp is None:
                    descartados.append(ed_id or "(sin id)")
                    n_skip += 1
                    continue

                volumenes.append(brp)
                huellas.append(crv)          # misma curva de la extrusión
                alturas.append(altura)        # metros (regla #11)
                pisos.append(p)
                zbs.append(z_base_ajustado)  # Store adjusted z_base for reporting
                ids.append(ed_id)
            except Exception as e_ed:
                n_skip += 1
                descartados.append("{0}: {1}".format(ed_id or "(sin id)", str(e_ed)))

        # --- aviso de unidades (sin escalar: el canvas trabaja en metros) ---
        aviso_unidades = ""
        try:
            doc = Rhino.RhinoDoc.ActiveDoc
            if doc is not None and doc.ModelUnitSystem != Rhino.UnitSystem.Meters:
                aviso_unidades = " | AVISO: doc Rhino no esta en metros ({0})".format(
                    str(doc.ModelUnitSystem))
        except Exception:
            pass

        # --- Bake a la capa de vecinos (Morphs manuales / revisión) ---
        nota_bake = ""
        if in_bake and len(volumenes) > 0:
            doc = Rhino.RhinoDoc.ActiveDoc
            if doc is None:
                nota_bake = " | bake: sin doc activo"
            else:
                try:
                    layer_idx = doc.Layers.FindByFullPath(LAYER_VECINOS, -1)
                    if layer_idx < 0:
                        nl = Rhino.DocObjects.Layer()
                        nl.Name = LAYER_VECINOS
                        nl.Color = System.Drawing.Color.FromArgb(170, 170, 170)
                        layer_idx = doc.Layers.Add(nl)
                    attr = Rhino.DocObjects.ObjectAttributes()
                    attr.LayerIndex = layer_idx
                    for b in volumenes:
                        doc.Objects.AddBrep(b, attr)
                    doc.Views.Redraw()
                    nota_bake = " | bake: {0} -> {1}".format(len(volumenes), LAYER_VECINOS)
                except Exception as e_bake:
                    nota_bake = " | bake ERROR: {0}".format(str(e_bake))

        # --- Exportación .3dm ---
        nota_export = ""
        if in_exportar and len(volumenes) > 0:
            try:
                if not os.path.isdir(OUT_DIR):
                    os.makedirs(OUT_DIR)
                path_3dm = os.path.join(OUT_DIR, chip + "-contexto50.3dm")
                f3dm = Rhino.FileIO.File3dm()
                for b in volumenes:
                    f3dm.Objects.AddBrep(b)
                f3dm.Write(path_3dm, 8)
                nota_export = " | 3dm: {0}".format(path_3dm)
            except Exception as e_ex:
                nota_export = " | export ERROR: {0}".format(str(e_ex))

        if alturas:
            a_min, a_max = min(alturas), max(alturas)
        else:
            a_min, a_max = 0.0, 0.0

        # Diagnóstico detallado por edificio (primeros 10)
        detalle_edificios = []
        for i in range(min(len(ids), 10)):
            zb = zbs[i] if i < len(zbs) else 0.0
            h = alturas[i] if i < len(alturas) else 0.0
            p = pisos[i] if i < len(pisos) else 0
            detalle_edificios.append("{0}: z={1:.1f} h={2:.1f} p={3}".format(ids[i], zb, h, p))
        if len(ids) > 10:
            detalle_edificios.append("... (+{0} mas)".format(len(ids) - 10))

        mensaje = (
            "CONTEXTO50_BUILD v01.2 | CHIP {0} | R {1:.0f}m | Volumenes {2}/{3} | "
            "Descartados {4} | Alturas {5:.1f}-{6:.1f}m | Fallbacks {7}"
        ).format(chip, radio_m, len(volumenes), n_total, n_skip, a_min, a_max, n_fallback)
        if zbs:
            mensaje += " | z_base (ajustado) {0:.1f}-{1:.1f}m ({2} con cota de {3})".format(
                min(zbs), max(zbs), len(zbs) - n_sin_cota, len(zbs))
            if len(zbs) > 1 and (max(zbs) - min(zbs)) < 0.05:
                mensaje += " | AVISO: todos los volumenes a la MISMA altura (revisar z_base_m del JSON)"
        if n_sin_cota:
            mensaje += " | ALERTA: {0} sin cota MDT -> en datum ETAPA1 (0.0)".format(n_sin_cota)
        if detalle_edificios:
            mensaje += " | Detalle: " + "; ".join(detalle_edificios)
        mensaje += " | Excluidos: {0} predio objetivo, {1} andenes/menores".format(
            n_predio, n_menores)
        if nota_lote:
            mensaje += " | lote: " + nota_lote
        if descartados:
            mensaje += " | {0}".format("; ".join(descartados[:5]))
        mensaje += " | Desplazamiento Z aplicado: {0:.3f}m (desde contexto etapa 1)".format(desplazamiento_z)
        mensaje += aviso_unidades + nota_bake + nota_export

    except Exception as e_main:
        mensaje = "CONTEXTO50_BUILD v01.2 | ERROR al procesar el JSON: {0}".format(str(e_main))

# ==============================================================================
# SALIDAS EXPUESTAS para cableado a F3_VOLUM_GENERADOR_v08
# ==============================================================================
# `desplazamiento_z` = Z_base del terreno (para conectar a z_origin de F3_VOLUM_GENERADOR)
# `z_origen`      = alias de desplazamiento_z (mismo valor, nombre alternativo)
# `z_base_promedio` = promedio de z_base_ajustado de todos los edificios vecinos
try:
    z_origen = 0.0  # F3 recibe geometria/programa ya en marco local; no restar otra vez.
    desplazamiento_z_out = desplazamiento_z
    if zbs:
        z_base_promedio = sum(zbs) / len(zbs)
    else:
        z_base_promedio = 0.0
except Exception:
    z_origen = 0.0
    desplazamiento_z_out = 0.0
    z_base_promedio = 0.0

print(mensaje)
try:
    ghenv.Component.Message = mensaje  # noqa: F821 - inyectado por Grasshopper
except Exception:
    pass
