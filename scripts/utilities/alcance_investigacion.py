# -*- coding: utf-8 -*-
"""
================================================================================
alcance_investigacion.py — Areas de influencia multi-nivel (Fase 2)
Proyecto: DisenoParametrico / Fase 2
Python 3.8+ (pyproj + shapely opcionales: si no estan, N3 queda PENDIENTE)
================================================================================

OBJETIVO:
  Definir y materializar las areas de influencia del estudio de demanda para un
  lote dado:

    N1-CERCANO             : radio 2.000 m  (vecindario directo)
    N2-INTERMEDIO          : radio 5.000 m  (area de mercado actual)
    N3-LEJANO-ACCESIBILIDAD: sin radio fijo; accesibilidad al transporte:
                             estaciones TransMilenio / paraderos SITP a < 500 m
                             del lote, e isocrona de 20 minutos en transporte
                             publico (preferencias sobre rutas principales de
                             transporte publico y privado).

USO:
  python alcance_investigacion.py --chip AAA0039KRMR [--config <json>]
                                  [--capas-dir data/transporte]

CAPAS (data/transporte/, descargadas con descargar_capas_transporte.py):
  - estaciones_tm.geojson   (153 estaciones troncales TransMilenio, WGS84)
  - paraderos_sitp.geojson  (paraderos zonales SITP, WGS84)
  - trazados_tm.geojson     (20 corredores troncales, WGS84)

ISOCRONA 20 MIN (metodo documentado, primer orden SIN GTFS completo):
  - Velocidad comercial media SITP/TM ~20 km/h -> 20 min ~ 6.667 m de red.
  - Corredores TM: distancia a lo largo del trazado del corredor (shapely
    project/interpolate) desde la estacion de acceso del lote.
  - Red zonal SITP: distancia euclidiana x factor de sinuosidad 1,3 (equivalente
    a ~5.128 m euclidianos) desde el paradero de acceso.
  - Se reportan conteos de cobertura (paraderos/estaciones alcanzables) y el
    metodo queda documentado en el JSON; la isocrona exacta con horarios (GTFS
    completo + routing) queda como mejora futura.

SALIDAS (exports/alcance/<CHIP>-alcance.json):
  - Anillos N1/N2 (circulo SIRGAS) y N3 materializado con las metricas reales.
================================================================================
"""

import argparse
import io
import json
import math
import os

DEFAULT_CONFIG = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "..",
    "data", "fase-2-demanda", "alcance-investigacion.json")
POT_CACHE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "..", "data", "pot-cache")
OUT_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "..",
    "exports", "alcance")
DEFAULT_CAPAS = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "..", "data", "transporte")

# Isocrona: 20 min x 20 km/h = 6.666,7 m de red; factor de sinuosidad red zonal
VEL_COMERCIAL_KMH = 20.0
MIN_ISOCRONA = 20.0
D_RED_MAX_M = VEL_COMERCIAL_KMH * 1000.0 * MIN_ISOCRONA / 60.0  # 6.666,7 m
FACTOR_SINUOSIDAD = 1.3
D_EUC_MAX_PARADEROS_M = D_RED_MAX_M / FACTOR_SINUOSIDAD  # ~5.128 m

try:
    import pyproj
    from shapely.geometry import LineString, Point
    _TRANS = pyproj.Transformer.from_crs("EPSG:4326", "ESRI:102233", always_xy=True)
    _CAPAS_OK = True
except Exception:  # pragma: no cover
    _CAPAS_OK = False


def _cargar(path):
    with io.open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def circulo(origen_x, origen_y, radio_m, pasos=48):
    """Poligono del anillo (SIRGAS, metros) para GIS/Grasshopper."""
    pts = []
    for i in range(pasos):
        a = 2.0 * math.pi * i / pasos
        pts.append([round(origen_x + radio_m * math.cos(a), 2),
                    round(origen_y + radio_m * math.sin(a), 2)])
    pts.append(pts[0])
    return pts


def _a_local(coords):
    """Reproyecta (lon, lat) -> (x, y) Bogota local (ESRI:102233, igual que el contexto F1)."""
    if not _CAPAS_OK:
        return None
    x, y = _TRANS.transform(coords[0], coords[1])
    return [round(float(x), 2), round(float(y), 2)]


def _puntos_geojson(path):
    """Devuelve lista de dicts {nombre, xy_local} desde un GeoJSON de puntos."""
    try:
        d = _cargar(path)
    except Exception:
        return None
    pts = []
    for f in d.get("features", []):
        g = f.get("geometry") or {}
        if g.get("type") != "Point":
            continue
        xy = _a_local(g["coordinates"])
        if xy is None:
            return None
        props = f.get("properties", {}) or {}
        nombre = (props.get("nombre_estacion") or props.get("NTRNOMBRE")
                  or props.get("NTRCODIGO") or str(props.get("OBJECTID", "")))
        pts.append({"nombre": str(nombre), "xy": xy})
    return pts


def _lineas_geojson(path):
    """Lista de polilineas locales (shapely LineString) + nombre."""
    try:
        d = _cargar(path)
    except Exception:
        return None
    lineas = []
    for f in d.get("features", []):
        g = f.get("geometry") or {}
        if g.get("type") == "MultiLineString":
            for part in g["coordinates"]:
                lineas.append((f.get("properties", {}).get("nombre_trazado_troncal", "?"), part))
        elif g.get("type") == "LineString":
            lineas.append((f.get("properties", {}).get("nombre_trazado_troncal", "?"), g["coordinates"]))
    out = []
    for nombre, part in lineas:
        loc = []
        ok = True
        for c in part:
            xy = _a_local(c)
            if xy is None:
                ok = False
                break
            loc.append(xy)
        if ok and len(loc) >= 2:
            out.append({"nombre": str(nombre), "linea": LineString(loc)})
    return out


def materializar_n3(ox, oy, capas_dir):
    """Metricas N3 con capas reales. Devuelve dict o None si no hay capas."""
    if not _CAPAS_OK:
        return None
    estaciones = _puntos_geojson(os.path.join(capas_dir, "estaciones_tm.geojson"))
    paraderos = _puntos_geojson(os.path.join(capas_dir, "paraderos_sitp.geojson"))
    trazados = _lineas_geojson(os.path.join(capas_dir, "trazados_tm.geojson"))
    if not estaciones or not paraderos or not trazados:
        return None

    pto = Point(ox, oy)

    # --- Distancias minimas y conteos < 500 m -------------------------------
    def _min_dist(puntos, limite=None):
        mejor = None
        n_dentro = 0
        for p in puntos:
            d = pto.distance(Point(p["xy"]))
            if limite is not None and d <= limite:
                n_dentro += 1
            if mejor is None or d < mejor[1]:
                mejor = (p["nombre"], round(float(d), 1))
        return mejor, n_dentro

    (nom_tm, d_tm), tm_500 = _min_dist(estaciones, 500.0)
    (nom_par, d_par), par_500 = _min_dist(paraderos, 500.0)

    # --- Isocrona 20 min (primer orden) -------------------------------------
    # 1) Corredores TM: estacion de acceso -> estaciones del mismo corredor a
    #    distancia de red <= D_RED_MAX_M a lo largo del trazado.
    est_tm_20 = 0
    corredor_acceso = None
    est_acceso = next((e for e in estaciones if e["nombre"] == nom_tm), None)
    if est_acceso is not None:
        pe = Point(est_acceso["xy"])
        mejor_trazado = None
        mejor_d = None
        for t in trazados:
            d = pe.distance(t["linea"])
            if mejor_d is None or d < mejor_d:
                mejor_d = d
                mejor_trazado = t
        if mejor_trazado is not None and mejor_d <= 100.0:
            corredor_acceso = mejor_trazado["nombre"]
            s_acc = mejor_trazado["linea"].project(pe)
            for e in estaciones:
                p_i = Point(e["xy"])
                if p_i.distance(mejor_trazado["linea"]) <= 50.0:
                    s_i = mejor_trazado["linea"].project(p_i)
                    if abs(s_i - s_acc) <= D_RED_MAX_M:
                        est_tm_20 += 1

    # 2) Red zonal: paraderos a distancia euclidiana <= D_EUC_MAX_PARADEROS_M
    #    desde el paradero de acceso (factor de sinuosidad 1,3).
    par_20 = 0
    if d_par is not None:
        p_acc = Point(next(p for p in paraderos if p["nombre"] == nom_par)["xy"])
        for p in paraderos:
            if p_acc.distance(Point(p["xy"])) <= D_EUC_MAX_PARADEROS_M:
                par_20 += 1

    return {
        "estacion_tm_mas_cercana": {"nombre": nom_tm, "distancia_m": d_tm},
        "paradero_sitp_mas_cercano": {"codigo": nom_par, "distancia_m": d_par},
        "estaciones_tm_500m": tm_500,
        "paraderos_sitp_500m": par_500,
        "isocrona_20min_aprox": {
            "metodo": ("Primer orden, SIN GTFS completo: velocidad comercial 20 km/h -> "
                       "%d m de red en 20 min; corredores TM por arclength del trazado; "
                       "red zonal con factor de sinuosidad 1,3 (%.0f m euclidianos)."
                       % (D_RED_MAX_M, D_EUC_MAX_PARADEROS_M)),
            "distancia_red_max_m": round(D_RED_MAX_M, 1),
            "corredor_tm_acceso": corredor_acceso,
            "estaciones_tm_alcanzables_20min": est_tm_20,
            "paraderos_sitp_alcanzables_20min": par_20,
            "gtfs_completo": "PENDIENTE (requiere GTFS con horarios y routing)",
        },
        "red_principal_privado": {
            "malla_vial_disponible": True,
            "criterio": "Malla vial arterial e intermedia del POT (contexto F1)",
        },
        "capas_utilizadas": ["estaciones_tm.geojson", "paraderos_sitp.geojson",
                             "trazados_tm.geojson"],
    }


def nivel_indicadores(niveles, nid):
    for n in niveles.values():
        if n.get("id") == nid:
            return n
    return None


def construir_alcance(chip, config_path, capas_dir):
    config = _cargar(config_path)
    ctx_path = os.path.join(POT_CACHE, chip + "-contexto.json")
    if not os.path.exists(ctx_path):
        raise SystemExit("Contexto no encontrado: %s" % ctx_path)
    ctx = _cargar(ctx_path)

    origen = ctx["metadata"]["origen_sirgas"]
    ox, oy = float(origen["x"]), float(origen["y"])

    niveles = config["niveles"]
    cercano = nivel_indicadores(niveles, "N1-CERCANO")
    intermedio = nivel_indicadores(niveles, "N2-INTERMEDIO")
    lejano = nivel_indicadores(niveles, "N3-LEJANO-ACCESIBILIDAD")

    vias = ctx.get("vias_oficiales", []) or []
    n_vias = len(vias)
    n_por_fuente = {}
    for v in vias:
        f = v.get("fuente", "?")
        n_por_fuente[f] = n_por_fuente.get(f, 0) + 1

    # N3: materializar con capas reales o reportar PENDIENTE
    acc = materializar_n3(ox, oy, capas_dir)
    if acc is None:
        acc = {
            "distancia_estacion_tm_m": "PENDIENTE (capa estaciones TransMilenio)",
            "distancia_paradero_sitp_m": "PENDIENTE (capa paraderos SITP)",
            "isocrona_20min_tp": "PENDIENTE (GTFS TransMilenio/SITP)",
            "red_principal_privado": {
                "malla_vial_disponible": True,
                "vias_en_contexto_f1": n_vias,
                "vias_por_fuente": n_por_fuente,
                "criterio": "Malla vial arterial e intermedia del POT",
            },
        }

    doc = {
        "chip": chip,
        "origen_sirgas": {"crs": origen["crs"], "x": ox, "y": oy},
        "area_lote_m2": ctx["lote_objetivo"]["area_m2"],
        "niveles": [
            {
                "id": cercano["id"],
                "etiqueta": cercano["etiqueta"],
                "radio_m": cercano["radio_m"],
                "circulo_sirgas": circulo(ox, oy, cercano["radio_m"]),
                "enfoque": cercano["enfoque"],
                "indicadores": cercano["indicadores"],
            },
            {
                "id": intermedio["id"],
                "etiqueta": intermedio["etiqueta"],
                "radio_m": intermedio["radio_m"],
                "circulo_sirgas": circulo(ox, oy, intermedio["radio_m"]),
                "enfoque": intermedio["enfoque"],
                "indicadores": intermedio["indicadores"],
            },
            {
                "id": lejano["id"],
                "etiqueta": lejano["etiqueta"],
                "radio_m": None,
                "criterios": lejano["criterios"],
                "estado_datos": config["estado_datos"],
                "accesibilidad": acc,
                "enfoque": lejano["enfoque"],
                "indicadores": lejano["indicadores"],
            },
        ],
        "consultas_investigacion": {
            "N1-CERCANO": [
                "Precios y canones de oferta activa a <=2 km (portales: Ciencuadras, FincaRaiz, Properati).",
                "Vacancia y absorcion del sector inmediato.",
                "Equipamientos y usos del primer anillo.",
            ],
            "N2-INTERMEDIO": [
                "Comparables de la UPZ y UPZ vecinas dentro de 5 km.",
                "Oferta nueva en construccion (licencias) en el anillo intermedio.",
                "Tendencia poblacional y capacidad de compra de la zona.",
            ],
            "N3-LEJANO-ACCESIBILIDAD": [
                "Distancia al corredor/estacion TransMilenio mas cercano (<500 m).",
                "Cobertura de paraderos SITP a <500 m.",
                "Isocrona de 20 min en transporte publico (primer orden; GTFS completo pendiente).",
                "Acceso a la malla vial arterial (transporte privado).",
            ],
        },
        "nota": "Los radios se miden desde el origen SIRGAS del lote. N3 usa accesibilidad en lugar de radio fijo; capas en data/transporte/ (descargar_capas_transporte.py).",
    }

    os.makedirs(OUT_DIR, exist_ok=True)
    salida = os.path.join(OUT_DIR, chip + "-alcance.json")
    with io.open(salida, "w", encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False, indent=2)
    return salida, doc


def main():
    ap = argparse.ArgumentParser(description="Areas de influencia multi-nivel")
    ap.add_argument("--chip", required=True, help="CHIP del lote")
    ap.add_argument("--config", default=DEFAULT_CONFIG)
    ap.add_argument("--capas-dir", default=DEFAULT_CAPAS)
    args = ap.parse_args()

    salida, doc = construir_alcance(args.chip, args.config, args.capas_dir)
    print("OK alcance de investigacion: %s" % salida)
    print("  N1-CERCANO    : radio 2.000 m")
    print("  N2-INTERMEDIO : radio 5.000 m")
    acc = doc["niveles"][2]["accesibilidad"]
    if "isocrona_20min_aprox" in acc:
        iso = acc["isocrona_20min_aprox"]
        print("  N3-ACCESIBILIDAD MATERIALIZADO:")
        print("    TM mas cercana: %s a %.0f m | %d estaciones < 500 m"
              % (acc["estacion_tm_mas_cercana"]["nombre"],
                 acc["estacion_tm_mas_cercana"]["distancia_m"],
                 acc["estaciones_tm_500m"]))
        print("    Paradero SITP mas cercano: %s a %.0f m | %d paraderos < 500 m"
              % (acc["paradero_sitp_mas_cercano"]["codigo"],
                 acc["paradero_sitp_mas_cercano"]["distancia_m"],
                 acc["paraderos_sitp_500m"]))
        print("    Isocrona 20 min (aprox): %d paraderos | %d estaciones TM | corredor %s"
              % (iso["paraderos_sitp_alcanzables_20min"],
                 iso["estaciones_tm_alcanzables_20min"],
                 iso["corredor_tm_acceso"]))
    else:
        print("  N3-ACCESIBILIDAD: PENDIENTE (capas no disponibles)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
