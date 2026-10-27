# -*- coding: utf-8 -*-
"""Genera el ALZADO DEL LOTE SOBRE SU VIA FRONTAL (equivalente vertical de la planta).

Para qué sirve
--------------
Decidir el `{z=0}` local del proyecto (Ground Level) mirando el lote de frente,
desde la calle, en vez de a ciegas sobre la planta:

  * perfil del terreno a lo largo del lindero frontal y de la franja de via,
  * puntos de muestreo del MDT,
  * líneas horizontales con los candidatos a `{z=0}`:
        - color VIA   : nivel de la via en su punto alto y en su punto bajo
        - color FRENTE: nivel mas bajo y mas alto del terreno sobre la via (lindero)
        - color LOTE  : minimo global del lote (criterio vigente `min_lote`)
  * la linea seleccionada (z=0 actual del proyecto) resaltada,
  * banda de altura maxima reglamentaria (POT/PEMP) sombreada desde el z=0 elegido,
  * volumenes adyacentes (contexto50) como referencia de escala.

Salida: un HTML autocontenido con SVG (se abre sin servidor) y opcionalmente JSON.
Si se abre desde el orquestador (`servidor.py`), cada linea candidata es clicable y
fija el z=0 del proyecto (POST /api/z0).

Uso:
    python scripts/utilities/generar-alzado-via.py --chip AAA0030JKOE
    python scripts/utilities/generar-alzado-via.py --chip AAA0030JKOE --lado 25 --json
    python scripts/utilities/generar-alzado-via.py --chip AAA0030JKOE --mdt rest

Notas de datos
--------------
El MDT se interpola con la malla de ETAPA1 (118 puntos, cubre lote + ~5 m). La franja
de via se muestrea a `--ancho-via` metros fuera del lindero; si el punto cae fuera de
la malla se marca como estimado. Con `--mdt rest` se consulta el servicio de Catastro
(mas lento y requiere red) para los mismos puntos.
"""
from __future__ import print_function

import argparse
import datetime
import io
import json
import math
import os
import sys

RAIZ = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
POT_CACHE = os.path.join(RAIZ, "data", "pot-cache")
OUT_DIR = os.path.join(RAIZ, "exports", "alzado-via")

# --- colores por familia de candidato (accesibles en escala de grises por trazo) ---
COL_VIA = "#1f6feb"        # nivel de la via (alto/bajo)
COL_FRENTE = "#2da44e"     # terreno sobre la via / lindero (alto/bajo)
COL_LOTE = "#8250df"       # minimo global del lote
COL_SEL = "#b8860b"        # linea seleccionada (z=0 del proyecto)
COL_BANDA = "#f2c94c"      # banda de altura reglamentaria
# Paleta de linderos: la MISMA de la planta de seleccion de vias (index.html).
PALETA_FRENTE = {"via": "#2563eb", "via_no_frontal": "#60a5fa", "predio": "#d97706",
                 "espacio_publico": "#16a34a", "libre": "#9ca3af", "indefinido": "#9ca3af"}
ROL_A_LADO = {"lateral_izq": "izq", "lateral_der": "der", "frente": "frente", "fondo": "posterior"}


# --------------------------------------------------------------------------- io
def leer_json(ruta, defecto=None):
    try:
        with io.open(ruta, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return defecto


def ruta_contexto(chip):
    return os.path.join(POT_CACHE, chip + "-contexto.json")


def ruta_contexto50(chip):
    for nombre in (chip + "-contexto50.json", "contexto50-actual.json"):
        p = os.path.join(POT_CACHE, nombre)
        if os.path.isfile(p):
            return p
    return None


def ruta_bloques(chip):
    for p in (os.path.join(RAIZ, "src", "fase-3-masa", "casos", chip, "bloques.json"),
              os.path.join(POT_CACHE, chip + "-bloques.json")):
        if os.path.isfile(p):
            return p
    return None


def ruta_z0(chip):
    return os.path.join(POT_CACHE, chip + "-z0.json")


# ------------------------------------------------------------------------ geometria
def _restar(a, b):
    return (a[0] - b[0], a[1] - b[1])


def _norma(v):
    return math.hypot(v[0], v[1])


def _unit(v):
    n = _norma(v)
    return (v[0] / n, v[1] / n) if n > 1e-9 else (0.0, 0.0)


def lado_por_longitud(ejes, idx, longitud_objetivo, tol=0.35):
    """Agrupa aristas consecutivas desde `idx` hasta cubrir la longitud del lado."""
    sel = []
    acum = 0.0
    n = len(ejes)
    for k in range(n):
        e = ejes[(idx + k) % n]
        sel.append((idx + k) % n)
        acum += e["largo"]
        if longitud_objetivo and acum >= longitud_objetivo - tol:
            break
        if not longitud_objetivo and k >= 0:
            break
    return sel


def idw(malla, x, y):
    """Cota interpolada (IDW) y aviso de si el punto cae dentro del casco de la malla."""
    num = den = 0.0
    dentro = False
    xs = [p[0] for p in malla]
    ys = [p[1] for p in malla]
    if xs and ys and min(xs) - 1e-6 <= x <= max(xs) + 1e-6 and min(ys) - 1e-6 <= y <= max(ys) + 1e-6:
        dentro = True
    for (mx, my, mz) in malla:
        d2 = (mx - x) ** 2 + (my - y) ** 2
        if d2 < 1e-9:
            return mz, True
        w = 1.0 / d2
        num += w * mz
        den += w
    return (num / den if den else None), dentro


def _rest_terreno(puntos_xy, ctx):
    """Cotas reales del MDT (REST Catastro) para [(x_local, y_local), ...].

    Devuelve (zs, ok): zs[i] = cota en el marco del canvas o None. Reutiliza el
    cliente de fetch-urban-context-v7 (misma fuente que el contexto50 / z_base).
    """
    import importlib.util

    ruta = os.path.join(RAIZ, "scripts", "utilities", "fetch-urban-context-v7.py")
    if not os.path.isfile(ruta):
        return [None] * len(puntos_xy), False
    try:
        spec = importlib.util.spec_from_file_location("fetch_urban_context_v7", ruta)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        from pyproj import Transformer
    except Exception:
        return [None] * len(puntos_xy), False

    meta = ctx.get("metadata") or {}
    tr = meta.get("traslacion_aplicada") or {}
    og = meta.get("origen_sirgas") or {}
    an = meta.get("ancla_canvas_local") or {}
    tx = float(tr.get("x", float(og.get("x", 0.0)) + float(an.get("x", 0.0))))
    ty = float(tr.get("y", float(og.get("y", 0.0)) + float(an.get("y", 0.0))))
    z_ref = float(og.get("z", 0.0)) + float(an.get("z", 0.0))

    transf = Transformer.from_crs("ESRI:102233", "EPSG:3116", always_xy=True)
    zs = []
    for (x, y) in puntos_xy:
        try:
            xm, ym = transf.transform(x + tx, y + ty)
            z = mod.get_elevation_from_api(xm, ym)
        except Exception:
            z = None
        zs.append((float(z) - z_ref) if z is not None else None)
    return zs, any(z is not None for z in zs)


# ------------------------------------------------------------------------ calculo
def construir(chip, lado_id=None, ancho_via=3.0, n_muestras=9, altura_norma=None,
              mdt="rest"):
    ctx = leer_json(ruta_contexto(chip))
    if not ctx:
        raise SystemExit("No existe %s" % ruta_contexto(chip))
    lote = [v for v in (ctx.get("lote_objetivo", {}).get("vertices_3d_local") or [])]
    if len(lote) > 1 and lote[0][:2] == lote[-1][:2]:
        lote = lote[:-1]
    if len(lote) < 3:
        raise SystemExit("Lote sin vertices suficientes")

    malla = [(p["x_local"], p["y_local"], p["z_local"])
             for p in (ctx.get("topografia", {}) or {}).get("malla_terreno", []) or []]

    ejes = []
    for i in range(len(lote)):
        a, b = lote[i], lote[(i + 1) % len(lote)]
        ejes.append({"idx": i, "a": a, "b": b,
                     "largo": math.hypot(b[0] - a[0], b[1] - a[1])})

    # --- lado frontal: el que el canvas marco como calle de acceso, si existe ---
    bloques = leer_json(ruta_bloques(chip), {}) or {}
    calle = ((bloques.get("orientacion") or {}).get("calle_acceso") or {})
    origen_lado = "parametro"
    if lado_id is None:
        if calle.get("lado_id") is not None:
            lado_id = int(calle["lado_id"])
            origen_lado = "canvas (calle de acceso)"
        else:
            # respaldo: arista del lote mas cercana a una via oficial
            lado_id = _arista_mas_cercana_a_via(lote, ejes, ctx)
            origen_lado = "arista mas cercana a via"

    longitud = calle.get("longitud_m") if (lado_id == calle.get("lado_id")) else None
    idxs = lado_por_longitud(ejes, lado_id, longitud)
    tramo = [ejes[k] for k in idxs]

    p0 = tramo[0]["a"]
    p1 = tramo[-1]["b"]
    eje_x = _unit(_restar(p1, p0))
    normal = (-eje_x[1], eje_x[0])          # izquierda del eje X
    L = _norma(_restar(p1, p0)) or 1.0

    # el vector normal debe apuntar HACIA LA CALLE (fuera del lote): se prueba con el centroide
    cx = sum(v[0] for v in lote) / len(lote)
    cy = sum(v[1] for v in lote) / len(lote)
    hacia_fuera = _restar(((p0[0] + p1[0]) / 2.0, (p0[1] + p1[1]) / 2.0), (cx, cy))
    if normal[0] * hacia_fuera[0] + normal[1] * hacia_fuera[1] < 0:
        normal = (-normal[0], -normal[1])

    def punto_en(t, off):
        """t en [0,1] sobre la cuerda del frente; off = metros hacia la calle."""
        x = p0[0] + (p1[0] - p0[0]) * t + normal[0] * off
        y = p0[1] + (p1[1] - p0[1]) * t + normal[1] * off
        return x, y

    # --- muestreo: lindero y franja de via ---
    lindero, via, muestras = [], [], []
    for k in range(n_muestras):
        t = k / float(n_muestras - 1)
        x, y = punto_en(t, 0.0)
        z, dentro = idw(malla, x, y)
        lindero.append({"t": t, "x": x, "y": y, "z": z, "estimado": not dentro})
        muestras.append({"tipo": "lindero", "x": x, "y": y, "z": z})
        xv, yv = punto_en(t, ancho_via)
        zv, dentro_v = idw(malla, xv, yv)
        if zv is None:
            zv, dentro_v = z, dentro
        via.append({"t": t, "x": xv, "y": yv, "z": zv, "estimado": not dentro_v})
        muestras.append({"tipo": "via", "x": xv, "y": yv, "z": zv})

    # --- MDT real para lindero y calle (la malla ETAPA1 no cubre la via) ---
    mdt_metodo = "IDW malla ETAPA1 (%d puntos)" % len(malla)
    if mdt == "rest":
        planos = [(p["x"], p["y"]) for p in lindero] + [(p["x"], p["y"]) for p in via]
        zs_rest, ok_rest = _rest_terreno(planos, ctx)
        if ok_rest:
            n = len(lindero)
            for k, p in enumerate(lindero):
                zr = zs_rest[k]
                if zr is not None:
                    p["z"] = zr
                    p["estimado"] = False
                p["fuente"] = "MDT REST" if zr is not None else "malla ETAPA1"
            for k, p in enumerate(via):
                zr = zs_rest[n + k]
                if zr is not None:
                    p["z"] = zr
                    p["estimado"] = False
                p["fuente"] = "MDT REST" if zr is not None else "malla ETAPA1"
            mdt_metodo = "MDT Catastro REST (puntos reales)"
        else:
            mdt_metodo = "IDW malla ETAPA1 (REST no disponible)"

    # Referencia vertical absoluta: el marco local arranca en origen_sirgas.z
    # (fetch-urban-context-v7: origen = min del MDT), asi que
    #     msnm = z_local + origen_sirgas.z
    z_ref_msnm = float(((ctx.get("metadata") or {}).get("origen_sirgas") or {}).get("z", 0.0) or 0.0)

    lados_lote = _segmentar_lados(lote, idxs, eje_x, normal)

    z_lindero = [p["z"] for p in lindero if p["z"] is not None]
    z_via = [p["z"] for p in via if p["z"] is not None]
    z_lote = [v[2] for v in lote if len(v) > 2]

    def _msnm(z):
        return round(float(z) + z_ref_msnm, 2) if z is not None else None

    candidatos = [
        {"id": "via_max", "familia": "via", "color": COL_VIA,
         "etiqueta": "Calle (franja exterior) - alta", "z": max(z_via) if z_via else None},
        {"id": "via_min", "familia": "via", "color": COL_VIA,
         "etiqueta": "Calle (franja exterior) - baja", "z": min(z_via) if z_via else None},
        {"id": "frente_max", "familia": "frente", "color": COL_FRENTE,
         "etiqueta": "Lindero del lote - cota alta", "z": max(z_lindero) if z_lindero else None},
        {"id": "frente_min", "familia": "frente", "color": COL_FRENTE,
         "etiqueta": "Lindero del lote - cota baja", "z": min(z_lindero) if z_lindero else None},
        {"id": "lote_min", "familia": "lote", "color": COL_LOTE,
         "etiqueta": "Minimo global del lote", "z": min(z_lote) if z_lote else None},
    ]

    for c in candidatos:
        c["z_msnm"] = _msnm(c["z"])

    # --- plan de niveles vigente (StorySync es canonico, ADR-024) ---
    # Solo se aceptan planes en el esquema ADR-024 (StorySync). Un plan viejo, en
    # marco canvas, quedaria 12 m por debajo del terreno y mentiria en el dibujo.
    niveles = []
    niveles_nota = "sin plan de niveles"
    for ruta_niv in (os.path.join(POT_CACHE, chip + "-niveles.json"),
                     os.path.join(RAIZ, "niveles_deseados.json"),
                     os.path.join(RAIZ, "src", "fase-3-masa", "casos", chip, "niveles_deseados.json")):
        if not os.path.isfile(ruta_niv):
            continue
        nd = leer_json(ruta_niv, {}) or {}
        if str(nd.get("chip", "")).upper() != chip:
            continue
        zgf = nd.get("zgf_m")
        sts = nd.get("stories") or []
        if zgf is None or not sts or sts[0].get("elevacion_modelo_m") is None:
            niveles_nota = ("%s esta en marco antiguo (sin zgf_m/elevacion_modelo_m): "
                            "regenerar con F3_StorySync_v02 --plan" % os.path.basename(ruta_niv))
            continue
        for st in sts:
            niveles.append({"name": st.get("name"),
                            "z_local": round(float(st["elevacion_modelo_m"]), 3),
                            "elevation_ac": st.get("elevation"),
                            "zgf_m": zgf})
        niveles_nota = "plan de niveles ADR-024 (%s)" % os.path.basename(ruta_niv)
        break

    # --- z=0 vigente ---
    z0 = leer_json(ruta_z0(chip), {}) or {}
    z0_actual = z0.get("z0_m")
    z0_modo = z0.get("modo")
    if z0_actual is None:
        z0_actual = min(z_lote) if z_lote else 0.0
        z0_modo = z0_modo or "min_lote"

    # --- altura reglamentaria ---
    pot = ctx.get("pot_data") or {}
    h_norma = float(altura_norma if altura_norma is not None else (pot.get("altura_maxima_m") or 0.0))

    # --- skyline: terreno detrás del frente (para dar profundidad a la vista) ---
    skyline = []
    for k in range(n_muestras):
        t = k / float(n_muestras - 1)
        zmax = None
        for d in (0.0, 0.25, 0.5, 0.75, 1.0):
            x, y = punto_en(t, -d * 40.0)      # hacia adentro del lote (40 m de fondo)
            z, _ = idw(malla, x, y)
            if z is not None and (zmax is None or z > zmax):
                zmax = z
        skyline.append({"t": t, "z": zmax})

    # --- volumenes adyacentes (contexto50) que caen en el ancho de la vista ---
    # OJO: el contexto50 vive en su PROPIO marco local (ancla SE = 0,0) y su Z es
    # z_local = z_MDT - z_ref. Para dibujarlo junto al lote hay que pasar a marco
    # ETAPA1:  xy + ancla_canvas_local   y   z - desplazamiento_z  (el mismo que
    # aplica F1_CONTEXTO50_BUILD).
    c50 = leer_json(ruta_contexto50(chip), {}) or {}
    meta50 = c50.get("metadata") or {}
    ancla = meta50.get("ancla_canvas_local") or {}
    ax = float(ancla.get("x", 0.0))
    ay = float(ancla.get("y", 0.0))
    desp = _desplazamiento_z(ctx, meta50)
    vecinos = []
    rings_vecinos = []
    n_predio_propio = 0
    lote_xy = [(v[0], v[1]) for v in lote]
    for e in c50.get("edificios") or []:
        zb = e.get("z_base_m")
        h = e.get("altura_m")
        if zb is None or not h:
            continue
        ring = (e.get("anillos") or [e.get("vertices")])[0] or []
        # El predio objetivo NO se dibuja nunca: si la mayoria de sus vertices cae
        # dentro del lote, es construccion del propio predio (no un vecino).
        if ring and len(ring) >= 3:
            dentro = sum(1 for p in ring if _punto_en_poligono(p[0] + ax, p[1] + ay, lote_xy))
            if dentro * 2 >= len(ring):
                n_predio_propio += 1
                continue
        px = [(p[0] + ax - p0[0]) * eje_x[0] + (p[1] + ay - p0[1]) * eje_x[1] for p in ring]
        py = [(p[0] + ax - p0[0]) * normal[0] + (p[1] + ay - p0[1]) * normal[1] for p in ring]
        if not px:
            continue
        prof = sum(py) / len(py)               # + = hacia la calle
        if prof > 25.0 or prof < -35.0:        # fuera de la banda de vista
            continue
        # rol: los inmediatamente laterales son la referencia de escala del alzado
        rol = "fondo"
        mismo_paramento = abs(prof) <= 12.0
        toca_izq = (-3.0 <= min(px) <= 0.5) or (-3.0 <= max(px) <= 0.5)
        toca_der = (L - 0.5 <= min(px) <= L + 3.0) or (L - 0.5 <= max(px) <= L + 3.0)
        if mismo_paramento and toca_izq:
            rol = "lateral_izq"
        elif mismo_paramento and toca_der:
            rol = "lateral_der"
        elif prof > 0:
            rol = "frente"
        rings_vecinos.append([(p[0] + ax, p[1] + ay) for p in ring])
        vecinos.append({"id": e.get("id"), "x0": min(px), "x1": max(px),
                        "prof": prof, "z_base": float(zb) - desp, "h": float(h),
                        "rol": rol})

    lados_lote = _frente_tipos(lote, lados_lote, rings_vecinos, ctx.get("vias_oficiales"),
                               ctx.get("espacios_publicos"))
    fuente_lados = "derivado geometricamente (sin <CHIP>-lados.json)"
    ruta_lados = os.path.join(POT_CACHE, chip + "-lados.json")
    if os.path.isfile(ruta_lados):
        fuente_lados = "canvas (LADOS, %s)" % os.path.basename(ruta_lados)

    altura_norma = {"h_m": h_norma,
                    "referencia_m": pot.get("altura_maxima_m_referencia_pzcb"),
                    "fuente": (pot.get("altura_maxima_fuente") or pot.get("fuente_norma")),
                    "altura_maxima_raw": pot.get("altura_maxima_raw"),
                    "upz": pot.get("upz")}

    return {
        "chip": chip,
        "generado": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
        "marco": "canvas (z_local = Z_abs - z_ref; ancla del lote = 0)",
        "lado": {"id": lado_id, "origen": origen_lado,
                 "etiqueta": calle.get("cardinal_label"),
                 "via_cercana": calle.get("via_cercana_nombre"),
                 "via_dist_m": calle.get("via_cercana_dist_m"),
                 "longitud_m": round(L, 2),
                 "aristas": [e["idx"] for e in tramo]},
        "frente": {"p0": [p0[0], p0[1]], "p1": [p1[0], p1[1]], "eje_x": eje_x,
                   "normal": normal, "largo_m": L},
        "lindero": lindero,
        "via": via,
        "muestras": muestras,
        "skyline": skyline,
        "candidatos": candidatos,
        "z0_actual": {"z": z0_actual, "modo": z0_modo},
        "msnm": {"z_ref_m": round(z_ref_msnm, 3),
                 "regla": "msnm = z_local + origen_sirgas.z"},
        "altura_norma": altura_norma,
        "vecinos": vecinos,
        "lados_lote": lados_lote,
        "lados_fuente": fuente_lados,
        "niveles": niveles,
        "niveles_nota": niveles_nota,
        "excluidos_predio_propio": n_predio_propio,
        "mdt": {"metodo": mdt_metodo, "puntos": len(malla)},
    }


def _segmentar_lados(lote, idxs_frente, eje_x, normal):
    """Los cuatro lados del lote vistos desde el alzado.

    Para cada arista se compara su normal con la normal exterior del frente y se
    asigna a uno de los cuatro lados; de cada lado se conserva el TRAMO CONTIGUO
    MAS LARGO (el lote es irregular: 30 vertices con aristas casi colineales).
    Los nombres usan los extremos del alzado, no los puntos cardinales, para que
    el operador no tenga que traducir.
    """
    n = len(lote)
    frente = set(idxs_frente)

    def _norm_arista(i):
        a, b = lote[i], lote[(i + 1) % n]
        v = (b[0] - a[0], b[1] - a[1])
        L = math.hypot(v[0], v[1])
        if L < 1e-9:
            return None, 0.0, a, b
        return (-v[1] / L, v[0] / L), L, a, b

    # normal exterior del frente (ya viene orientada hacia la calle)
    ref = normal
    if ref[0] * _norm_arista(sorted(frente)[0])[0][0] + \
            ref[1] * _norm_arista(sorted(frente)[0])[0][1] < 0:
        pass  # la normal del frente ya se oriento antes; se usa tal cual

    def _cat(u):
        """Categoria segun el angulo entre la normal de la arista y la del frente."""
        ang = math.degrees(math.atan2(u[0] * ref[1] - u[1] * ref[0],
                                      u[0] * ref[0] + u[1] * ref[1]))
        if -45.0 <= ang < 45.0:
            return "frente"
        if 45.0 <= ang < 135.0:
            return "izq"
        if -135.0 <= ang < -45.0:
            return "der"
        return "posterior"

    grupos = {"frente": [], "izq": [], "der": [], "posterior": []}
    for i in range(n):
        u, L, a, b = _norm_arista(i)
        if u is None:
            continue
        cat = "frente" if i in frente else _cat(u)
        grupos[cat].append(i)

    def _tramo_mas_largo(idxs):
        """Subsecuencia contigua (circular) mas larga de la lista dada."""
        if not idxs:
            return []
        s = set(idxs)
        mejor, actual = [], []
        for k in range(2 * n):
            i = k % n
            if i in s:
                actual.append(i)
                if len(actual) > len(mejor):
                    mejor = list(actual)
            else:
                actual = []
            if k >= n and not actual:
                break
        # quitar repetidos conservando orden
        vistos, out = set(), []
        for i in mejor:
            if i not in vistos:
                vistos.add(i)
                out.append(i)
        return out

    nombres = {"frente": "Frente (calle)",
               "izq": "Lateral del extremo izquierdo del alzado",
               "der": "Lateral del extremo derecho del alzado",
               "posterior": "Posterior (fondo del lote)"}

    def _lado(cat, aristas):
        zs, pts, largo = [], [], 0.0
        for j in aristas:
            a, b = lote[j], lote[(j + 1) % n]
            zs.extend([a[2], b[2]])
            largo += math.hypot(b[0] - a[0], b[1] - a[1])
            if not pts:
                pts.append([a[0], a[1]])
            pts.append([b[0], b[1]])
        if not zs:
            return None
        return {"nombre": nombres[cat], "categoria": cat, "es_frente": cat == "frente",
                "z_min": round(min(zs), 3), "z_max": round(max(zs), 3),
                "desnivel_m": round(max(zs) - min(zs), 3),
                "largo_m": round(largo, 2), "puntos": pts, "aristas": aristas}

    lados = [_lado("frente", sorted(frente))]
    for cat in ("izq", "der", "posterior"):
        tr = _tramo_mas_largo(grupos[cat])
        if tr:
            lados.append(_lado(cat, tr))
    return [l for l in lados if l]


def _punto_en_poligono(x, y, ring):
    """Ray casting clasico sobre [(x, y), ...]."""
    dentro = False
    n = len(ring)
    j = n - 1
    for i in range(n):
        xi, yi = ring[i]
        xj, yj = ring[j]
        if ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / ((yj - yi) or 1e-12) + xi):
            dentro = not dentro
        j = i
    return dentro


def _frente_tipos(lote, lados, vecinos, vias, eps, tol_m=12.0):
    """Tipo de frente de cada lado con la paleta de la planta de seleccion de vias.

    Prioridad: primero se intenta el cuadro de lados del canvas (<CHIP>-lados.json,
    exportado con el flag de LADOS); si no esta, se deriva geometricamente:
      - 'predio'          si hay edificacion vecina a menos de tol_m del lado
      - 'via'             si hay via oficial a menos de tol_m
      - 'espacio_publico' si hay EP a menos de tol_m
      - 'libre'           en otro caso
    """
    def _dist_punto_seg(p, a, b):
        ax, ay = a
        bx, by = b
        vx, vy = bx - ax, by - ay
        L2 = vx * vx + vy * vy
        if L2 <= 1e-12:
            return math.hypot(p[0] - ax, p[1] - ay)
        tt = max(0.0, min(1.0, ((p[0] - ax) * vx + (p[1] - ay) * vy) / L2))
        return math.hypot(p[0] - (ax + tt * vx), p[1] - (ay + tt * vy))

    def _min_dist(puntos_lado, poligonos):
        mejor = 1e9
        for ring in poligonos:
            for k in range(len(ring)):
                a, b = ring[k], ring[(k + 1) % len(ring)]
                for p in puntos_lado:
                    d = _dist_punto_seg(p, a, b)
                    if d < mejor:
                        mejor = d
        return mejor

    vias_rings = [[(p[0], p[1]) for p in (v.get("coordenadas_local") or [])]
                  for v in (vias or [])]
    eps_rings = [[(p[0], p[1]) for p in (e.get("coordenadas_local") or [])]
                 for e in (eps or [])]
    vec_rings = []
    for ring in vecinos or []:
        if ring and len(ring) >= 3:
            vec_rings.append([(p[0], p[1]) for p in ring])

    for l in lados:
        pts = l["puntos"]
        muestras = pts[:: max(1, len(pts) // 6)]
        if l.get("es_frente"):
            l["frente_tipo"] = "via"
            continue
        if vec_rings and _min_dist(muestras, vec_rings) <= tol_m:
            l["frente_tipo"] = "predio"
        elif vias_rings and _min_dist(muestras, vias_rings) <= tol_m:
            l["frente_tipo"] = "via"
        elif eps_rings and _min_dist(muestras, eps_rings) <= tol_m:
            l["frente_tipo"] = "espacio_publico"
        else:
            l["frente_tipo"] = "libre"
    return lados


def _desplazamiento_z(ctx, meta50):
    """desplazamiento_z de F1_CONTEXTO50_BUILD: origen_etapa1 + Z_base - z_ref."""
    m1 = ctx.get("metadata") or {}
    origen = float((m1.get("origen_sirgas") or {}).get("z", 0.0) or 0.0)
    ancla = float((m1.get("ancla_canvas_local") or {}).get("z", 0.0) or 0.0)
    ref = float((meta50.get("z_base_fuente") or {}).get("z_ref_m", origen + ancla))
    zs = [float(p.get("z_local", 0.0)) for p in
          ((ctx.get("topografia") or {}).get("malla_terreno") or [])]
    zs = [z for z in zs if abs(z) > 0.001]
    base = min(zs) if zs else 0.0
    return origen + base - ref


def _arista_mas_cercana_a_via(lote, ejes, ctx):
    """Respaldo: arista del lote mas cercana a una via oficial."""
    vias = ctx.get("vias_oficiales") or []
    mejor, mejor_d = 0, 1e9
    for e in ejes:
        mx = (e["a"][0] + e["b"][0]) / 2.0
        my = (e["a"][1] + e["b"][1]) / 2.0
        for v in vias:
            pts = v.get("coordenadas_local") or []
            for p in pts:
                d = math.hypot(p[0] - mx, p[1] - my)
                if d < mejor_d:
                    mejor_d, mejor = d, e["idx"]
    return mejor


# ------------------------------------------------------------------------ dibujo
def _esc(t):
    return (str(t).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def svg_alzado(datos, ancho=1280, alto=700):
    """SVG del alzado: lote de frente, vecinos laterales a escala, lados marcados."""
    lindero = datos["lindero"]
    via = datos["via"]
    sky = datos["skyline"]
    L = datos["frente"]["largo_m"] or 1.0

    z0 = datos["z0_actual"]["z"] or 0.0
    h_norma = datos["altura_norma"]["h_m"] or 0.0
    laterales = [v for v in datos["vecinos"] if v.get("rol", "").startswith("lateral")]
    tipo_lado = {l["categoria"]: l.get("frente_tipo", "libre")
                 for l in datos.get("lados_lote", [])}

    def _color_vecino(v):
        cat = ROL_A_LADO.get(v.get("rol", "fondo"), "posterior")
        return PALETA_FRENTE.get(tipo_lado.get(cat, "libre"), "#9ca3af")

    # --- ventana vertical: decision + banda + vecinos laterales completos ---
    base = [p["z"] for p in lindero + via if p["z"] is not None]
    base += [c["z"] for c in datos["candidatos"] if c["z"] is not None]
    base.append(z0)
    zmin = min(base) - 0.9
    zmax = max(base + [z0 + h_norma] + [v["z_base"] + v["h"] for v in laterales] + [z0 + 4]) + 1.2

    m = {"izq": 78, "der": 336, "arr": 58, "aba": 62}
    w = ancho - m["izq"] - m["der"]
    h = alto - m["arr"] - m["aba"]

    def X(x_m):
        return m["izq"] + (x_m / L) * w

    def Y(z):
        return m["arr"] + h - ((z - zmin) / (zmax - zmin)) * h

    partes = []
    A = partes.append
    A('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="100%%" '
      'style="max-width:%dpx;font-family:Segoe UI,Arial,sans-serif">' % (ancho, alto, ancho))
    A('<rect x="0" y="0" width="%d" height="%d" fill="#ffffff"/>' % (ancho, alto))
    A('<rect x="%d" y="%d" width="%d" height="%d" fill="#f7f9fc"/>' % (m["izq"], m["arr"], w, h))

    # --- silueta del terreno detras ---
    pts_sky = [(X(s["t"] * L), Y(max(zmin, s["z"]))) for s in sky if s["z"] is not None]
    if pts_sky:
        d = ("M %.1f,%.1f L " % (pts_sky[0][0], Y(zmin))
             + " L ".join("%.1f,%.1f" % p for p in pts_sky)
             + " L %.1f,%.1f Z" % (pts_sky[-1][0], Y(zmin)))
        A('<path d="%s" fill="#efeade" fill-opacity="0.55" stroke="#d6cfbf" '
          'stroke-width="1" stroke-dasharray="3 3"/>' % d)

    # --- banda POT/PEMP al fondo ---
    if h_norma:
        y0, y1 = Y(min(z0, z0 + h_norma)), Y(max(z0, z0 + h_norma))
        A('<rect x="%d" y="%.1f" width="%d" height="%.1f" fill="%s" fill-opacity="0.07"/>'
          % (m["izq"], y1, w, y0 - y1, COL_BANDA))
        A('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="1.2" '
          'stroke-dasharray="7 4"/>' % (m["izq"], y1, m["izq"] + w, y1, COL_BANDA))
        A('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="#15803d" stroke-width="2"/>'
          % (m["izq"], y1, m["izq"] + w, y1))
        A('<text x="%d" y="%.1f" font-size="11.5" font-weight="600" fill="#15803d">'
          'altura maxima vigente %.2f m desde z=0</text>'
          % (m["izq"] + 8, y1 - 5, h_norma))
        _ref = datos["altura_norma"].get("referencia_m")
        if _ref and abs(float(_ref) - h_norma) > 0.01:
            yr = Y(z0 + float(_ref))
            A('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="#b42318" stroke-width="1.4" '
              'stroke-dasharray="10 5"/>' % (m["izq"], yr, m["izq"] + w, yr))
            A('<text x="%d" y="%.1f" font-size="10.5" fill="#b42318">'
              'PZCB (referencia) %.2f m</text>' % (m["izq"] + 8, yr - 5, float(_ref)))

    # --- vecinos: fondo tenue; LATERALES a escala y con su cara ---
    for v in sorted(datos["vecinos"], key=lambda v: (v.get("rol") != "lateral_izq",
                                                     v.get("rol") != "lateral_der", v["prof"])):
        x0, x1 = X(max(-40.0, v["x0"])), X(min(L + 40.0, v["x1"]))
        if x1 - x0 < 1.2:
            continue
        zb, zt = v["z_base"], v["z_base"] + v["h"]
        if zt <= zmin or zb >= zmax:
            continue
        y0, y1 = Y(max(zb, zmin)), Y(min(zt, zmax))
        lat = v.get("rol", "").startswith("lateral")
        col = _color_vecino(v)
        if lat:
            A('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s" '
              'fill-opacity="0.42" stroke="%s" stroke-width="1.4"/>'
              % (x0, y1, x1 - x0, y0 - y1, col, col))
            # altura de la cara del vecino, para comparar a escala
            A('<text x="%.1f" y="%.1f" font-size="10.5" fill="#1f2328" text-anchor="middle">'
              '%.1f m</text>' % ((x0 + x1) / 2.0, y1 - 5, v["h"]))
            A('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" '
              'stroke-width="0.9" stroke-dasharray="3 3"/>'
              % (x0, y0, x1, y0, col))
        else:
            A('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s" '
              'fill-opacity="0.16" stroke="%s" stroke-width="0.7"/>'
              % (x0, y1, x1 - x0, y0 - y1, col, col))

    # --- franja de calle y lindero ---
    pts_via = [(X(p["t"] * L), Y(p["z"])) for p in via if p["z"] is not None]
    if pts_via:
        A('<path d="M %.1f,%.1f L ' % (pts_via[0][0], Y(zmin))
          + " L ".join("%.1f,%.1f" % p for p in pts_via)
          + " L %.1f,%.1f Z" % (pts_via[-1][0], Y(zmin))
          + '" fill="#dfe3e8" stroke="none"/>')
        A('<polyline points="%s" fill="none" stroke="%s" stroke-width="2.6"/>'
          % (" ".join("%.1f,%.1f" % p for p in pts_via), COL_VIA))
    pts_l = [(X(p["t"] * L), Y(p["z"])) for p in lindero if p["z"] is not None]
    if pts_l:
        A('<polyline points="%s" fill="none" stroke="#1f2328" stroke-width="2.8"/>'
          % " ".join("%.1f,%.1f" % p for p in pts_l))

    # --- puntos de muestreo ---
    for p in datos["muestras"]:
        if p["z"] is None:
            continue
        t = _t_de(p, datos)
        if not (-0.02 <= t <= 1.02):
            continue
        col = COL_VIA if p["tipo"] == "via" else "#1f2328"
        A('<circle cx="%.1f" cy="%.1f" r="2.7" fill="#fff" stroke="%s" stroke-width="1.5"/>'
          % (X(t * L), Y(p["z"]), col))

    # --- niveles del plan vigente (ADR-024) ---
    for n in datos.get("niveles", []):
        z = n.get("z_local")
        if z is None or not (zmin <= z <= zmax):
            continue
        y = Y(z)
        A('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="#0f766e" stroke-width="0.9" '
          'stroke-dasharray="1 5" opacity="0.75"/>' % (m["izq"], y, m["izq"] + w, y))
        _col = "#b42318" if (n["z_local"] - z0) > h_norma + 1e-6 else "#0f766e"
        A('<text x="%d" y="%.1f" font-size="9.5" fill="%s">%s</text>'
          % (m["izq"] + 4, y - 3, _col, _esc(n.get("name") or "")))

    # --- escalera vertical de niveles (a la derecha del alzado) ---
    _niv = [n for n in datos.get("niveles", []) if n.get("z_local") is not None
            and zmin <= n["z_local"] <= zmax]
    if _niv:
        xl = m["izq"] + w - 26
        for k, n in enumerate(_niv):
            y = Y(n["z_local"])
            A('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#0f766e" stroke-width="1.2"/>'
              % (xl, y, xl + 12, y))
            _col2 = "#b42318" if (n["z_local"] - z0) > h_norma + 1e-6 else "#0f766e"
            A('<text x="%.1f" y="%.1f" font-size="9.5" fill="%s">%s</text>'
              % (xl + 14, y + 3, _col2, _esc(n.get("name") or "")))
            if k:
                z_prev = _niv[k - 1]["z_local"]
                A('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#0f766e" '
                  'stroke-width="0.8" stroke-dasharray="2 2"/>' % (xl + 6, Y(z_prev), xl + 6, y))
                A('<text x="%.1f" y="%.1f" font-size="8.5" fill="#0f766e" text-anchor="end">'
                  '%.2f</text>' % (xl - 2, (Y(z_prev) + y) / 2.0 + 3, n["z_local"] - z_prev))
        A('<text x="%.1f" y="%.1f" font-size="9" fill="#0f766e" transform="rotate(-90 %.1f %.1f)">'
          'niveles (entrepiso)</text>' % (xl - 12, m["arr"] + h / 2, xl - 12, m["arr"] + h / 2))

    # --- lados del lote: esquinas del frente y fondo ---
    frente = next((l for l in datos.get("lados_lote", []) if l["es_frente"]), None)
    if frente:
        z_ini = lindero[0]["z"] if lindero[0]["z"] is not None else z0
        z_fin = lindero[-1]["z"] if lindero[-1]["z"] is not None else z0
        for xx, zz, etq in ((0.0, z_ini, "esquina izq"), (L, z_fin, "esquina der")):
            A('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#8b949e" '
              'stroke-width="0.9" stroke-dasharray="2 3"/>' % (X(xx), Y(zz), X(xx), Y(zmax)))
            A('<text x="%.1f" y="%.1f" font-size="10" fill="#57606a" text-anchor="middle">'
              '%s %+.2f m</text>' % (X(xx), Y(zz) + 13, etq, zz))
    post = next((l for l in datos.get("lados_lote", []) if l["categoria"] == "posterior"), None)
    if post:
        yp = Y(post["z_max"])
        A('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="#8250df" stroke-width="1.4" '
          'stroke-dasharray="2 4" opacity="0.9"/>' % (m["izq"], yp, m["izq"] + w, yp))
        A('<text x="%d" y="%.1f" font-size="10.5" fill="#6b3fb5">fondo del lote  '
          '%.2f-%.2f m</text>' % (m["izq"] + 8, yp - 5, post["z_min"], post["z_max"]))

    # --- candidatos ---
    ocupado = []
    for c in sorted([c for c in datos["candidatos"] if c["z"] is not None], key=lambda c: -c["z"]):
        y = Y(c["z"])
        A('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="1.5" '
          'stroke-dasharray="6 4" opacity="0.9"/>' % (m["izq"], y, m["izq"] + w, y, c["color"]))
        yt = y + 4
        while any(abs(yt - o) < 15 for o in ocupado):
            yt += 15
        ocupado.append(yt)
        A('<text x="%d" y="%.1f" font-size="11.5" fill="%s">%s  %+.2f m  |  %.2f msnm</text>'
          % (m["izq"] + w + 10, yt, c["color"], _esc(c["etiqueta"]), c["z"],
             c.get("z_msnm") if c.get("z_msnm") is not None else c["z"]))

    # --- seleccionado ---
    ys = Y(z0)
    A('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="3.4"/>'
      % (m["izq"], ys, m["izq"] + w, ys, COL_SEL))
    yt = ys - 8
    while any(abs(yt - o) < 15 for o in ocupado):
        yt -= 15
    A('<text x="%d" y="%.1f" font-size="12.5" font-weight="700" fill="%s">'
      'z=0 SELECCIONADO  %+.2f m  |  %.2f msnm  [%s]</text>'
      % (m["izq"] + w + 10, yt, COL_SEL, z0, z0 + datos["msnm"]["z_ref_m"],
         _esc(datos["z0_actual"]["modo"])))

    # --- rejilla Y ---
    span = zmax - zmin
    for cand in (0.5, 1.0, 2.0, 2.5, 5.0, 10.0, 20.0):
        if span / cand <= 10:
            paso = cand
            break
    else:
        paso = 25.0
    z = math.ceil(zmin / paso) * paso
    while z <= zmax:
        y = Y(z)
        A('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="#e3e7ee" stroke-width="0.8"/>'
          % (m["izq"], y, m["izq"] + w, y))
        A('<text x="%d" y="%.1f" font-size="10.5" fill="#6b7480" text-anchor="end">%.1f</text>'
          % (m["izq"] - 8, y + 3.5, z))
        z += paso
    A('<text x="18" y="%d" font-size="11" fill="#3a3f46" transform="rotate(-90 18 %d)">'
      'cota z local [m]</text>' % (m["arr"] + h // 2, m["arr"] + h // 2))
    A('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#3a3f46" stroke-width="1.2"/>'
      % (m["izq"], m["arr"] + h, m["izq"] + w, m["arr"] + h))
    A('<text x="%d" y="%d" font-size="11" fill="#3a3f46" text-anchor="middle">'
      'frente del lote - %.1f m (escala 1:1 en X y Z)</text>'
      % (m["izq"] + w // 2, m["arr"] + h + 22, L))

    # --- escala grafica (regla) ---
    _lado_m = 10.0 if (zmax - zmin) > 8 else 5.0
    x_esc0 = m["izq"] + 16
    x_esc1 = X(_lado_m)
    y_esc = m["arr"] + h - 14
    A('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#3a3f46" stroke-width="1.6"/>'
      % (x_esc0, y_esc, x_esc1, y_esc))
    for _xx in (x_esc0, x_esc1):
        A('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#3a3f46" stroke-width="1.6"/>'
          % (_xx, y_esc - 4, _xx, y_esc + 4))
    A('<text x="%.1f" y="%.1f" font-size="10" fill="#3a3f46">%.0f m</text>'
      % ((x_esc0 + x_esc1) / 2.0 - 8, y_esc - 8, _lado_m))

    # --- cota vertical acotada del vecino lateral mas alto (referencia de escala) ---
    if laterales:
        _alto = max(laterales, key=lambda v: v["z_base"] + v["h"])
        xd = X(min(L + 6.0, max(0.0, _alto["x1"]))) + 6
        y0d, y1d = Y(_alto["z_base"]), Y(_alto["z_base"] + _alto["h"])
        A('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#b42318" stroke-width="1"/>'
          % (xd, y0d, xd, y1d))
        for _yy in (y0d, y1d):
            A('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#b42318" stroke-width="1"/>'
              % (xd - 4, _yy, xd + 4, _yy))
        A('<text x="%.1f" y="%.1f" font-size="9.5" fill="#b42318" transform="rotate(-90 %.1f %.1f)">'
          'vecino %.2f m</text>' % (xd - 4, (y0d + y1d) / 2.0, xd - 4, (y0d + y1d) / 2.0, _alto["h"]))

    # --- rotulos F / L / P en los extremos ---
    A('<text x="%.1f" y="%.1f" font-size="11" font-weight="700" fill="#b8860b" '
      'text-anchor="middle">F</text>' % (X(L / 2.0), m["arr"] + h + 40))
    A('<text x="%.1f" y="%.1f" font-size="10.5" font-weight="700" fill="#d97706" '
      'text-anchor="end">L</text>' % (X(0.0) - 6, m["arr"] + h - 6))
    A('<text x="%.1f" y="%.1f" font-size="10.5" font-weight="700" fill="#d97706">L</text>'
      % (X(L) + 4, m["arr"] + h - 6))

    # --- leyenda ---
    lx = m["izq"]
    ly = m["arr"] - 20
    for col, etq in ((COL_VIA, "calle"), (COL_FRENTE, "lindero"),
                     (COL_LOTE, "minimo del lote"), (COL_SEL, "z=0 seleccionado")):
        A('<rect x="%d" y="%d" width="16" height="4" rx="2" fill="%s"/>' % (lx, ly, col))
        A('<text x="%d" y="%d" font-size="11" fill="#3a3f46">%s</text>' % (lx + 22, ly + 5, etq))
        lx += 82

    # --- planta en miniatura con los lados ---
    A(_planta_lados(datos, m["izq"] + 6, m["arr"] + 6, 190, 150))

    # --- titulo ---
    A('<text x="%d" y="26" font-size="16" font-weight="600" fill="#1f2328">'
      'Alzado sobre la via frontal - %s</text>' % (m["izq"], _esc(datos["chip"])))
    A('<text x="%d" y="44" font-size="11.5" fill="#57606a">lado %s (%s) - %s - %s</text>'
      % (m["izq"], _esc(datos["lado"]["id"]),
         _esc(datos["lado"]["etiqueta"] or "sin etiqueta"),
         _esc(datos["lado"]["origen"]), _esc(datos["mdt"]["metodo"])))
    A("</svg>")
    return "\n".join(partes)


def _planta_lados(datos, x0, y0, w, h):
    """Planta en miniatura: lote con sus cuatro lados rotulados."""
    lote = []
    for l in datos.get("lados_lote", []):
        for p in l["puntos"]:
            lote.append(p)
    if not lote:
        return ""
    xs = [p[0] for p in lote]
    ys = [p[1] for p in lote]
    ancho = max(xs) - min(xs) or 1.0
    alto = max(ys) - min(ys) or 1.0
    esc = min((w - 16) / ancho, (h - 16) / alto)

    def P(p):
        return (x0 + 8 + (p[0] - min(xs)) * esc,
                y0 + h - 8 - (p[1] - min(ys)) * esc)

    colores = {l["categoria"]: PALETA_FRENTE.get(l.get("frente_tipo", "libre"), "#9ca3af")
               for l in datos.get("lados_lote", [])}
    out = ['<g opacity="0.96">',
           '<rect x="%d" y="%d" width="%d" height="%d" fill="#ffffff" fill-opacity="0.85" '
           'stroke="#d0d7de" stroke-width="0.8" rx="6"/>' % (x0, y0, w, h),
           '<text x="%d" y="%d" font-size="9.5" fill="#57606a">planta - lados del lote</text>'
           % (x0 + 8, y0 + 13)]
    for l in datos.get("lados_lote", []):
        pts = l["puntos"]
        if len(pts) < 2:
            continue
        d = " ".join("%.1f,%.1f" % P(p) for p in pts)
        out.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="2.4" '
                   'stroke-linecap="round"/>' % (d, colores.get(l["categoria"], "#8b949e")))
        # rotulo en el punto medio del lado
        m = pts[len(pts) // 2]
        px, py = P(m)
        letra = {"frente": "F", "posterior": "P", "izq": "L", "der": "L"}[l["categoria"]]
        out.append('<circle cx="%.1f" cy="%.1f" r="7" fill="#fff" stroke="%s" stroke-width="1"/>'
                   % (px, py, colores.get(l["categoria"], "#8b949e")))
        out.append('<text x="%.1f" y="%.1f" font-size="9" font-weight="600" text-anchor="middle" '
                   'fill="%s">%s</text>' % (px, py + 3, colores.get(l["categoria"], "#8b949e"), letra))
    out.append("</g>")
    return "\n".join(out)


def svg_detalle(datos, ancho=1280, alto=260):
    """Detalle del datum: la zona de decision (calle/lindero/candidatos) en zoom.

    El alzado principal esta a escala real (incluye los vecinos laterales), asi que
    las lineas candidatas quedan muy juntas; este panel las separa para poder leerlas.
    """
    z0 = datos["z0_actual"]["z"] or 0.0
    L = datos["frente"]["largo_m"] or 1.0
    lindero = datos["lindero"]
    via = datos["via"]
    zs = [p["z"] for p in lindero + via if p["z"] is not None]
    zs += [c["z"] for c in datos["candidatos"] if c["z"] is not None]
    zs.append(z0)
    h_norma = datos["altura_norma"]["h_m"] or 0.0
    if h_norma:
        zs.append(z0 + min(h_norma, 3.0))
    zmin = min(zs) - 0.30
    zmax = max(zs) + 0.30

    m = {"izq": 78, "der": 336, "arr": 30, "aba": 34}
    w = ancho - m["izq"] - m["der"]
    h = alto - m["arr"] - m["aba"]

    def X(x_m):
        return m["izq"] + (x_m / L) * w

    def Y(z):
        return m["arr"] + h - ((z - zmin) / (zmax - zmin)) * h

    A = []
    A.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="100%%" '
             'style="max-width:%dpx;font-family:Segoe UI,Arial,sans-serif">' % (ancho, alto, ancho))
    A.append('<rect x="0" y="0" width="%d" height="%d" fill="#ffffff"/>' % (ancho, alto))
    A.append('<rect x="%d" y="%d" width="%d" height="%d" fill="#f7f9fc"/>' % (m["izq"], m["arr"], w, h))

    for p in datos["muestras"]:
        if p["z"] is None:
            continue
        t = _t_de(p, datos)
        if not (-0.02 <= t <= 1.02):
            continue
        col = COL_VIA if p["tipo"] == "via" else "#1f2328"
        A.append('<circle cx="%.1f" cy="%.1f" r="2.4" fill="#fff" stroke="%s" stroke-width="1.3"/>'
                 % (X(t * L), Y(p["z"]), col))

    pts_v = [(X(p["t"] * L), Y(p["z"])) for p in via if p["z"] is not None]
    if pts_v:
        A.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="2.4"/>'
                 % (" ".join("%.1f,%.1f" % p for p in pts_v), COL_VIA))
    pts_l = [(X(p["t"] * L), Y(p["z"])) for p in lindero if p["z"] is not None]
    if pts_l:
        A.append('<polyline points="%s" fill="none" stroke="#1f2328" stroke-width="2.6"/>'
                 % " ".join("%.1f,%.1f" % p for p in pts_l))

    ocupado = []
    for c in sorted([c for c in datos["candidatos"] if c["z"] is not None], key=lambda c: -c["z"]):
        y = Y(c["z"])
        A.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="1.4" '
                 'stroke-dasharray="6 4"/>' % (m["izq"], y, m["izq"] + w, y, c["color"]))
        yt = y + 4
        while any(abs(yt - o) < 14 for o in ocupado):
            yt += 14
        ocupado.append(yt)
        A.append('<text x="%d" y="%.1f" font-size="11.5" fill="%s">%s  %+.2f m  |  %.2f msnm</text>'
                 % (m["izq"] + w + 10, yt, c["color"], _esc(c["etiqueta"]), c["z"],
                    c.get("z_msnm") if c.get("z_msnm") is not None else c["z"]))

    ys = Y(z0)
    A.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="3"/>'
             % (m["izq"], ys, m["izq"] + w, ys, COL_SEL))
    yt = ys - 7
    while any(abs(yt - o) < 14 for o in ocupado):
        yt -= 14
    A.append('<text x="%d" y="%.1f" font-size="12" font-weight="700" fill="%s">'
             'z=0 SELECCIONADO  %+.2f m  |  %.2f msnm</text>'
             % (m["izq"] + w + 10, yt, COL_SEL, z0, z0 + datos["msnm"]["z_ref_m"]))

    paso = 0.25 if (zmax - zmin) < 3 else 0.5
    z = math.ceil(zmin / paso) * paso
    while z <= zmax:
        y = Y(z)
        A.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="#e3e7ee" stroke-width="0.8"/>'
                 % (m["izq"], y, m["izq"] + w, y))
        A.append('<text x="%d" y="%.1f" font-size="10" fill="#6b7480" text-anchor="end">%.2f</text>'
                 % (m["izq"] - 8, y + 3.5, z))
        z += paso
    A.append('<text x="%d" y="18" font-size="11.5" font-weight="600" fill="#3a3f46">'
             'Detalle del datum (zoom %s)</text>' % (m["izq"], "x4" if paso == 0.25 else "x2"))
    A.append("</svg>")
    return "\n".join(A)


def svg_comparativa(datos, ancho=1280, alto=300):
    """Comparativa del datum: la misma seccion con z=0 en min_lote vs en la calle.

    Sirve para ver el efecto de elegir uno u otro sobre la banda de altura permitida.
    """
    z0 = datos["z0_actual"]["z"] or 0.0
    h = datos["altura_norma"]["h_m"] or 0.0
    ref = datos["altura_norma"].get("referencia_m")
    cands = {c["id"]: c for c in datos["candidatos"]}
    escenarios = [
        ("min_lote", "z=0 en el minimo del lote (criterio vigente)", cands.get("lote_min"), COL_SEL),
        ("via_min", "z=0 en el punto bajo de la calle", cands.get("via_min"), COL_VIA),
    ]
    escenarios = [e for e in escenarios if e[2] and e[2]["z"] is not None]
    if len(escenarios) < 2:
        return ""

    zs = [e[2]["z"] for e in escenarios] + [e[2]["z"] + h for e in escenarios]
    if ref:
        zs.append(escenarios[0][2]["z"] + float(ref))
    zmin, zmax = min(zs) - 1.0, max(zs) + 1.0

    m = {"izq": 78, "der": 40, "arr": 40, "aba": 46}
    hh = alto - m["arr"] - m["aba"]
    wcol = (ancho - m["izq"] - m["der"]) / 2.0 - 30

    def Y(z):
        return m["arr"] + hh - ((z - zmin) / (zmax - zmin)) * hh

    A = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="100%%" '
         'style="max-width:%dpx;font-family:Segoe UI,Arial,sans-serif">' % (ancho, alto, ancho),
         '<rect x="0" y="0" width="%d" height="%d" fill="#ffffff"/>' % (ancho, alto)]
    A.append('<text x="%d" y="20" font-size="12" font-weight="600" fill="#3a3f46">'
             'Que cambia si el z=0 se toma en la calle en vez del minimo del lote</text>' % m["izq"])

    for k, (cid, etq, c, col) in enumerate(escenarios):
        x0 = m["izq"] + k * (wcol + 60)
        z = c["z"]
        y0, ytop = Y(z), Y(z + h)
        A.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s" fill-opacity="0.10"/>'
                 % (x0, ytop, wcol, y0 - ytop, col))
        A.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="3"/>'
                 % (x0, y0, x0 + wcol, y0, col))
        A.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="2"/>'
                 % (x0, ytop, x0 + wcol, ytop, col))
        A.append('<text x="%.1f" y="%.1f" font-size="11.5" font-weight="600" fill="%s">%s</text>'
                 % (x0, Y(zmax) - 6, col, _esc(etq)))
        A.append('<text x="%.1f" y="%.1f" font-size="11" fill="#3a3f46">z=0: %+.2f m  |  %.2f msnm</text>'
                 % (x0, y0 + 16, z, c.get("z_msnm") or 0.0))
        A.append('<text x="%.1f" y="%.1f" font-size="11" fill="#3a3f46">techo permitido: %+.2f m  |  %.2f msnm</text>'
                 % (x0, ytop - 6, z + h, (c.get("z_msnm") or 0.0) + h))
        if ref and abs(float(ref) - h) > 0.01:
            yr = Y(z + float(ref))
            A.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#b42318" '
                     'stroke-width="1.2" stroke-dasharray="8 4"/>' % (x0, yr, x0 + wcol, yr))
            A.append('<text x="%.1f" y="%.1f" font-size="10" fill="#b42318">PZCB %.2f m</text>'
                     % (x0 + 4, yr - 4, float(ref)))

    # delta entre escenarios
    z_a, z_b = escenarios[0][2]["z"], escenarios[1][2]["z"]
    xb = m["izq"] + wcol + 30
    ya, yb = Y(z_a), Y(z_b)
    A.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#6b7280" stroke-width="1" '
             'stroke-dasharray="3 3"/>' % (m["izq"] + wcol, ya, xb, ya))
    A.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#6b7280" stroke-width="1" '
             'stroke-dasharray="3 3"/>' % (m["izq"] + wcol, yb, xb, yb))
    A.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#6b7280" stroke-width="1.4"/>'
             % (xb, ya, xb, yb))
    A.append('<text x="%.1f" y="%.1f" font-size="10.5" fill="#6b7280">delta %.2f m</text>'
             % (xb + 4, (ya + yb) / 2.0 + 3, abs(z_b - z_a)))
    A.append("</svg>")
    return "\n".join(A)


def _t_de(punto, datos):
    """t (0..1) de un punto de muestreo sobre la cuerda del frente."""
    p0 = datos["frente"]["p0"]
    e = datos["frente"]["eje_x"]
    L = datos["frente"]["largo_m"] or 1.0
    return ((punto["x"] - p0[0]) * e[0] + (punto["y"] - p0[1]) * e[1]) / L


# ------------------------------------------------------------------------ html
def html_alzado(datos, svg, servidor=False, svg_detalle_=None, svg_cmp_=None):
    z0 = datos["z0_actual"]["z"]
    filas = []
    for c in datos["candidatos"]:
        if c["z"] is None:
            continue
        filas.append(
            '<tr><td><span class="sw" style="background:%s"></span>%s</td>'
            '<td class="num">%+.2f</td><td class="num">%s</td><td class="num">%+.2f</td>'
            '<td><button data-z="%.3f" class="usar">fijar z=0</button></td></tr>'
            % (c["color"], _esc(c["etiqueta"]), c["z"],
               ("%.2f" % c["z_msnm"]) if c.get("z_msnm") is not None else "-",
               c["z"] - z0, c["z"]))
    filas_lados = []
    for l in datos.get("lados_lote", []):
        filas_lados.append(
            '<tr><td>%s</td><td class="num">%.1f</td><td class="num">%+.2f</td>'
            '<td class="num">%+.2f</td><td class="num">%.2f</td></tr>'
            % (_esc(l["nombre"]), l["largo_m"], l["z_min"], l["z_max"], l["desnivel_m"]))

    h_norma = datos["altura_norma"]["h_m"] or 0.0
    aviso = ""
    estimados = sum(1 for p in datos["lindero"] + datos["via"] if p.get("estimado"))
    if estimados:
        aviso = ('<p class="aviso">%d de %d puntos de muestreo caen fuera de la malla '
                 'ETAPA1: su cota es extrapolada.</p>'
                 % (estimados, len(datos["lindero"]) + len(datos["via"])))

    js = """
<script>
document.querySelectorAll('button.usar').forEach(function(b){
  b.addEventListener('click', function(){
    var z = parseFloat(b.dataset.z);
    fetch('/api/z0', {method:'POST', headers:{'Content-Type':'application/json'},
      body: JSON.stringify({chip: CHIP, z0_m: z, modo: 'manual', origen: 'alzado'})})
      .then(function(r){ return r.json(); })
      .then(function(j){
         document.getElementById('estado').textContent =
            j.ok ? ('z=0 fijado en ' + j.z0_m.toFixed(3) + ' m. Recarga para verlo.') :
                   ('No se pudo fijar: ' + (j.error || 'error'));
      })
      .catch(function(e){ document.getElementById('estado').textContent = String(e); });
  });
});
</script>""" if servidor else """
<script>
document.querySelectorAll('button.usar').forEach(function(b){
  b.addEventListener('click', function(){
    document.getElementById('estado').textContent =
      'Abre esta pagina desde el orquestador (servidor.py) para fijar el z=0, o ejecuta: ' +
      'python src\\\\orquestador\\\\run_pipeline_v01.py --z0-modo manual --z0-valor ' + b.dataset.z;
  });
});
</script>"""

    return _html_plantilla(datos, svg, filas, h_norma, aviso, js, filas_lados, svg_detalle_, svg_cmp_)


def _html_plantilla(datos, svg, filas, h_norma, aviso, js, filas_lados=(), svg_det=None, svg_cmp=None):
    return """<!DOCTYPE html>
<html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Alzado sobre la via frontal - %(chip)s</title>
<style>
 body{font-family:'Segoe UI',Arial,sans-serif;margin:0;background:#f6f7f9;color:#1f2328}
 .wrap{max-width:1300px;margin:0 auto;padding:18px}
 .card{background:#fff;border:1px solid #e2e5ea;border-radius:12px;padding:14px 16px;margin:12px 0}
 h1{font-size:19px;margin:0 0 4px}
 .sub{color:#57606a;font-size:13px;margin:0}
 table{border-collapse:collapse;width:100%%;font-size:13px}
 th,td{padding:7px 8px;border-bottom:1px solid #eceff3;text-align:left}
 th{font-size:12px;text-transform:uppercase;letter-spacing:.03em;color:#57606a}
 td.num{text-align:right;font-variant-numeric:tabular-nums}
 .sw{display:inline-block;width:18px;height:4px;border-radius:2px;margin-right:8px;vertical-align:middle}
 .usar{font-size:12px;padding:4px 10px;border-radius:6px;border:1px solid #d0d7de;background:#fff;cursor:pointer}
 .usar:hover{background:#f3f4f6}
 .aviso{background:#fff8e1;border:1px solid #f0d98c;padding:8px 10px;border-radius:8px;font-size:12.5px}
 .chip{display:inline-block;background:#eef2f7;border-radius:999px;padding:2px 10px;font-size:12px;margin-left:8px}
</style></head><body><div class="wrap">
<h1>Alzado sobre la via frontal <span class="chip">%(chip)s</span></h1>
<p class="sub">Lado %(lado_id)s (%(lado_etq)s) - longitud de frente %(largo).1f m - %(marco)s
  &middot; <b>msnm = z local + %(zref).3f m</b></p>
<div class="card">%(svg)s</div>
<div class="card">%(svg_det)s</div>
<div class="card">%(svg_cmp)s</div>
<div class="card">
 <table>
  <thead><tr><th>Candidato a z=0</th><th class="num">cota local [m]</th>
   <th class="num">cota msnm [m]</th><th class="num">vs z=0 actual</th><th></th></tr></thead>
  <tbody>%(filas)s</tbody>
 </table>
 <h3 style="font-size:14px;margin:18px 0 6px">Lados del lote</h3>
 <table>
  <thead><tr><th>Lado</th><th class="num">longitud [m]</th><th class="num">cota min</th>
   <th class="num">cota max</th><th class="num">desnivel [m]</th></tr></thead>
  <tbody>%(lados)s</tbody>
 </table>
 <p class="sub">Linderos: <b>%(lados_fuente)s</b>. Para el datum manda el lado
   <b>Frente</b>; los colores son los mismos de la planta de seleccion de vias
   (azul = via, naranja = predio/vecino, verde = espacio publico, gris = libre).</p>
 <p class="sub">Niveles: %(niveles_nota)s. Vecinos del propio predio excluidos: %(n_propio)d.</p>
 <p class="sub" style="margin-top:10px">Altura maxima reglamentaria: <b>%(h).2f m</b> desde el z=0 elegido
   (%(fuente)s). Banda sombreada en el grafico.</p>
 %(aviso)s
 <p id="estado" class="sub"></p>
</div>
<p class="sub">Generado %(fecha)s por scripts/utilities/generar-alzado-via.py</p>
</div>%(js)s</body></html>
""" % {
        "chip": _esc(datos["chip"]),
        "lado_id": datos["lado"]["id"],
        "lado_etq": _esc(datos["lado"]["etiqueta"] or "-"),
        "largo": datos["frente"]["largo_m"] or 0.0,
        "marco": _esc(datos["marco"]),
        "zref": datos["msnm"]["z_ref_m"],
        "svg": svg,
        "filas": "\n".join(filas),
        "h": h_norma,
        "fuente": _esc(datos["altura_norma"].get("fuente") or "POT"),
        "aviso": aviso,
        "fecha": _esc(datos["generado"]),
        "js": js,
        "lados": "\n".join(filas_lados),
        "lados_fuente": _esc(datos.get("lados_fuente") or "-"),
        "niveles_nota": _esc(datos.get("niveles_nota") or "-"),
        "n_propio": datos.get("excluidos_predio_propio", 0),
        "svg_det": svg_det or "",
        "svg_cmp": svg_cmp or "",
    }


# ------------------------------------------------------------------------ main
def _pedir_export_lados(chip):
    """Deja el flag de LADOS encendido para que el canvas exporte <CHIP>-lados.json.

    Fuente unica: el alzado usa el cuadro de lados del canvas (LADOS) cuando existe;
    si no existe, se pide y mientras tanto se deriva geometricamente.
    """
    flag = os.path.join(POT_CACHE, "lados-export-flag.json")
    dato = {"exportar": True, "chip": chip,
            "ts": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "motivo": "alzado sobre la via frontal requiere los lados del canvas"}
    try:
        with io.open(flag, "w", encoding="utf-8") as f:
            json.dump(dato, f, indent=2, ensure_ascii=False)
        return True
    except Exception:
        return False


def main():
    ap = argparse.ArgumentParser(description="Alzado del lote sobre su via frontal")
    ap.add_argument("--chip", required=True)
    ap.add_argument("--lado", type=int, default=None, help="indice de arista del lado frontal")
    ap.add_argument("--ancho-via", type=float, default=3.0, help="franja de via [m]")
    ap.add_argument("--altura-norma", type=float, default=None, help="altura POT/PEMP [m]")
    ap.add_argument("--salida", default=None)
    ap.add_argument("--json", action="store_true", help="imprime el payload JSON")
    ap.add_argument("--mdt", choices=("rest", "malla"), default="rest",
                    help="rest = MDT Catastro real (red); malla = IDW de la malla ETAPA1")
    args = ap.parse_args()

    chip = args.chip.strip().upper()
    datos = construir(chip, lado_id=args.lado, ancho_via=args.ancho_via,
                      altura_norma=args.altura_norma, mdt=args.mdt)
    if not os.path.isfile(os.path.join(POT_CACHE, chip + "-lados.json")):
        _pedir_export_lados(chip)

    svg = svg_alzado(datos)
    svg_det = svg_detalle(datos)
    svg_cmp = svg_comparativa(datos)
    html = html_alzado(datos, svg, servidor=False, svg_detalle_=svg_det, svg_cmp_=svg_cmp)

    if not os.path.isdir(OUT_DIR):
        os.makedirs(OUT_DIR)
    salida = args.salida or os.path.join(OUT_DIR, chip + "-alzado-via.html")
    with io.open(salida, "w", encoding="utf-8") as f:
        f.write(html)
    with io.open(os.path.join(OUT_DIR, chip + "-alzado-via.json"), "w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=1)

    if args.json:
        print(json.dumps(datos, ensure_ascii=False))
    else:
        print("Alzado: %s" % salida)
        for c in datos["candidatos"]:
            if c["z"] is not None:
                print("  %-34s %+7.2f m" % (c["etiqueta"], c["z"]))
        print("  z=0 actual (%s): %+.2f m | altura norma %.2f m"
              % (datos["z0_actual"]["modo"], datos["z0_actual"]["z"], datos["altura_norma"]["h_m"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
