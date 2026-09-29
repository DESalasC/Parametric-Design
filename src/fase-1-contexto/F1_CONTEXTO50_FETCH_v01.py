# -*- coding: utf-8 -*-
"""
F1_CONTEXTO50_FETCH_v01.py  (Python 3 - utilidad de proyecto)
=====================================================================
Proyecto : DisenoParametrico / Fase 1 - Contexto
Proposito: Extraer las volumetrias construidas en un radio (def. 50 m) alrededor
           del lote y dejarlas en el MISMO marco local del canvas del proyecto.

           FUENTE PRINCIPAL (offline, igual que fetch-urban-context-v7):
             bd_uaecd.gpkg  ->  capa "Cons"  (construcciones, ESRI:102233,
             campos ConCodigo/ConNPisos/ConAltura/ConElevaci/ConNSotano/ConTSemis).
             Licencia CC BY 4.0 - UAECD / IDECA.
           FUENTE ALTERNATIVA (--fuente rest): servicio REST "construccion" de
             serviciosgis.catastrobogota.gov.co (misma entidad).

           Transformacion (identica a ETAPA 1, ver F1_ETAPA1_CONTEXTO_v02.py:219-226):
             marco A (json)  : local = ESRI − origen_sirgas
             marco B (canvas): canvas = local − ancla_SE_lote(min Y, desempate max X)
             =>  canvas = ESRI − (origen_sirgas + ancla_SE_lote)
             (traslacion pura, SIN rotacion: +X = Este, +Y = Norte)

ALTURA  : altura_m = ConNPisos * altura_piso_m.  ConAltura NO sirve (vale 0/1).
          Default 3.80 m = constante ALTURA_PISO_M del pipeline (fetch-urban-context-v7.py).
          Alternativas documentadas: 2.0 m (criterio oficial visor "Bogota 3D"), 3.0 m (OSM).

USO (usar el python del proyecto, que tiene geopandas/pyogrio):
  .venv\\Scripts\\python.exe F1_CONTEXTO50_FETCH_v01.py --chip AAA0240ZXJH --radio 50 ^
      --ctx ..\\..\\data\\pot-cache\\AAA0240ZXJH-contexto.json --out ..\\..\\data\\pot-cache
=====================================================================
"""
import argparse
import json
import math
import os
import sys

CRS_TARGET = "ESRI:102233"          # MAGNA_Ciudad_Bogota (igual que fetch-urban-context-v7)
# 2026-09-28: default PORTABLE -> env POT_GPKG_PATH > data/geobase del proyecto > ruta historica
_ROOT_PROY = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
_GPKG_PROY = os.path.join(_ROOT_PROY, "data", "geobase", "bd_uaecd.gpkg")
GPKG_DEFAULT = _GPKG_PROY if os.path.exists(_GPKG_PROY) else r"D:\Users\Dario Salas\proyectos\DesParametrico\2-Entradas\Datos_Sitio_GDB\bd_uaecd.gpkg"
ALTURA_PISO_DEF = 3.80              # ALTURA_PISO_M del pipeline (fetch-urban-context-v7.py)

# Variable de entorno para hacer portable la ruta de la geobase
GPKG_PATH = os.environ.get("POT_GPKG_PATH", GPKG_DEFAULT)
REST = ("https://serviciosgis.catastrobogota.gov.co/arcgis/rest/services/"
        "catastro/construccion/MapServer/0/query")


def leer_ctx(ctx_path):
    with open(ctx_path, "r", encoding="utf-8") as f:
        d = json.load(f)
    m = d.get("metadata", {})
    o = m.get("origen_sirgas", {})
    lote = d.get("lote_objetivo", {}).get("vertices_3d_local", []) or []
    return (float(o.get("x", 0.0)), float(o.get("y", 0.0)), float(o.get("z", 0.0)),
            o.get("crs", CRS_TARGET), m.get("chip"), m.get("azimuth_norte_grados"), lote)


def ancla_canvas(lote_local):
    """Replica EXACTA de F1_ETAPA1_CONTEXTO_v02.py:219-226 (vertice SE del lote)."""
    if not lote_local or len(lote_local) < 3:
        return 0.0, 0.0, 0.0
    a = lote_local[0]
    for v in lote_local:
        if v[1] < a[1] - 0.01 or (abs(v[1] - a[1]) < 0.01 and v[0] > a[0]):
            a = v
    return float(a[0]), float(a[1]), float(a[2])


def altura_de(props, ap):
    for k in ("ConNPisos", "CONNPISOS", "ConElevaci", "CONELEVACI"):
        v = props.get(k)
        if v not in (None, "", 0, "0", "None"):
            try:
                n = float(v)
                if n >= 1:
                    return round(n * ap, 2), int(n), "%s*%.2f" % (k, ap)
            except (ValueError, TypeError):
                pass
    return round(2 * ap, 2), 2, "default(2 niveles)"


def _esri_a_canvas(coords, ox, oy, dx, dy):
    """coords = [(X_esri, Y_esri), ...] -> [[x, y], ...] en marco canvas."""
    return [[round(X - (ox + dx), 3), round(Y - (oy + dy), 3)] for (X, Y) in coords]


def fuente_gpkg(gpkg, lote_esri, radio, ap):
    import geopandas as gpd
    from shapely.geometry import Polygon
    base = Polygon(lote_esri).buffer(radio)          # buffer en CRS proyectado = metros exactos
    gdf = gpd.read_file(gpkg, layer="Cons", mask=base)
    gdf = gdf[gdf.geometry.intersects(base)].copy()
    out = []
    for _, row in gdf.iterrows():
        geom = row.geometry
        if geom is None or geom.is_empty:
            continue
        partes = list(geom.geoms) if geom.geom_type == "MultiPolygon" else [geom]
        for k, parte in enumerate(partes):
            if parte.geom_type != "Polygon" or len(parte.exterior.coords) < 4:
                continue
            props = row.to_dict()
            h, pisos, crit = altura_de(props, ap)
            sid = str(props.get("ConCodigo") or props.get("CONCODIGO") or "CON")
            out.append({
                "id": sid if len(partes) == 1 else "%s_p%d" % (sid, k + 1),
                "esri_ring": [(float(x), float(y)) for x, y in parte.exterior.coords],
                "pisos": pisos,
                "altura_m": h,
                "criterio_altura": crit,
                "area_m2": round(parte.area, 2),
                "lote": str(props.get("ConCodLote") or ""),
                "sotanos": props.get("ConNSotano") or props.get("CONNSOTANO") or 0,
                "fuente": "bd_uaecd.gpkg#Cons (UAECD, CC BY 4.0)",
            })
    return out, gdf.crs.to_string() if gdf.crs is not None else CRS_TARGET


def fuente_rest(lon, lat, radio, ap):
    import urllib.parse
    import urllib.request
    params = {"geometry": "%f,%f" % (lon, lat), "geometryType": "esriGeometryPoint",
              "inSR": 4326, "distance": radio, "units": "esriSRUnit_Meter",
              "spatialRel": "esriSpatialRelIntersects",
              "outFields": "CONCODIGO,CONNPISOS,CONALTURA,CONELEVACI,CONNSOTANO,CONCOD_LOTE,LOTECODIGO",
              "returnGeometry": "true", "outSR": 4326, "f": "geojson"}
    req = urllib.request.Request(REST + "?" + urllib.parse.urlencode(params),
                                 headers={"User-Agent": "DisenoParametrico-F1/1.0"})
    with urllib.request.urlopen(req, timeout=90) as r:
        return json.loads(r.read().decode("utf-8"))


def main():
    ap_ = argparse.ArgumentParser()
    ap_.add_argument("--chip", required=True)
    ap_.add_argument("--radio", type=float, default=50.0)
    ap_.add_argument("--altura-piso", type=float, default=ALTURA_PISO_DEF)
    ap_.add_argument("--ctx", default=None)
    ap_.add_argument("--out", default=".")
    ap_.add_argument("--gpkg", default=GPKG_PATH)
    ap_.add_argument("--fuente", choices=["gpkg", "rest"], default="gpkg")
    ap_.add_argument("--marco", choices=["canvas", "json"], default="canvas")
    args = ap_.parse_args()

    ctx = args.ctx or os.path.join("data", "pot-cache", "%s-contexto.json" % args.chip)
    if not os.path.exists(ctx):
        print("ERROR: no existe el contexto %s" % ctx); sys.exit(2)

    ox, oy, oz, crs, chip_ctx, azim, lote_local = leer_ctx(ctx)
    dx, dy, dz = ancla_canvas(lote_local)
    ax, ay = (ox + dx, oy + dy) if args.marco == "canvas" else (ox, oy)
    print("Contexto   : %s" % ctx)
    print("CRS        : %s | origen_sirgas=(%.3f, %.3f)" % (crs, ox, oy))
    print("Ancla SE   : (%.3f, %.3f) | marco salida=%s | traslacion=(%.3f, %.3f)"
          % (dx, dy, args.marco, ax, ay))

    lote_esri = [(ox + v[0], oy + v[1]) for v in lote_local]

    if args.fuente == "gpkg":
        if not os.path.exists(args.gpkg):
            print("ERROR: no existe la Geobase %s" % args.gpkg); sys.exit(2)
        print("Fuente     : Geobase %s (capa Cons)" % os.path.basename(args.gpkg))
        crudos, crs_fte = fuente_gpkg(args.gpkg, lote_esri, args.radio, args.altura_piso)
    else:
        from pyproj import Transformer
        back = Transformer.from_crs(crs, "EPSG:4326", always_xy=True)
        lon, lat = back.transform(ox + sum(v[0] for v in lote_local) / len(lote_local),
                                  oy + sum(v[1] for v in lote_local) / len(lote_local))
        print("Fuente     : REST UAECD (centro %.6f, %.6f)" % (lat, lon))
        gj = fuente_rest(lon, lat, args.radio, args.altura_piso)
        from pyproj import Transformer as T2
        fwd = T2.from_crs("EPSG:4326", crs, always_xy=True)
        crudos = []
        for i, ft in enumerate(gj.get("features", [])):
            g = ft.get("geometry", {})
            polys = [g["coordinates"]] if g.get("type") == "Polygon" else (g.get("coordinates") or [])
            for k, poly in enumerate(polys):
                ring = [(fwd.transform(p[0], p[1])[0], fwd.transform(p[0], p[1])[1]) for p in poly[0]]
                h, pisos, crit = altura_de(ft.get("properties", {}), args.altura_piso)
                crudos.append({"id": "REST%03d_%d" % (i, k), "esri_ring": ring, "pisos": pisos,
                               "altura_m": h, "criterio_altura": crit, "area_m2": None,
                               "lote": "", "sotanos": 0, "fuente": "REST UAECD Construccion"})
        crs_fte = "EPSG:4326 -> %s" % crs

    print("Construcciones en radio %.0f m del lote: %d" % (args.radio, len(crudos)))

    edificios, feats = [], []
    for e in crudos:
        ring = _esri_a_canvas(e["esri_ring"], ox, oy, dx, dy)
        if len(ring) >= 4:
            edificios.append({"id": e["id"], "vertices": ring, "anillos": [ring],
                              "pisos": e["pisos"], "altura_m": e["altura_m"],
                              "criterio_altura": e["criterio_altura"],
                              "area_m2": e.get("area_m2"),
                              "fuente": e["fuente"]})
            feats.append({"type": "Feature",
                          "properties": {"id": e["id"], "pisos": e["pisos"],
                                         "altura_m": e["altura_m"]},
                          "geometry": {"type": "Polygon", "coordinates": ring}})

    alturas = [x["altura_m"] for x in edificios]
    out = {"metadata": {
        "chip": args.chip, "esquema": "contexto50/v1", "marco": args.marco,
        "radio_m": args.radio, "buffer_desde": "lote (poligono)",
        "crs_fuente": crs_fte, "crs_canvas": crs,
        "origen_sirgas": {"crs": crs, "x": ox, "y": oy, "z": oz},
        "ancla_canvas_local": {"x": dx, "y": dy, "z": dz,
                               "regla": "vertice SE del lote (min Y, desempate max X)"},
        "traslacion_aplicada": {"x": ax, "y": ay},
        "azimuth_norte_grados": azim,
        "altura_por_piso_m": args.altura_piso,
        "regla_altura": "altura = ConNPisos * %.2f m (ConAltura NO sirve: vale 0/1)" % args.altura_piso,
        "fuente": ("Geobase bd_uaecd.gpkg#Cons" if args.fuente == "gpkg" else "REST UAECD Construccion"),
        "licencia": "CC BY 4.0",
        "atribucion": "UAECD - Gerencia de Informacion Catastral / IDECA",
        "conteo": {"edificaciones": len(edificios),
                   "pisos_max": max([e["pisos"] for e in edificios]) if edificios else 0,
                   "altura_max_m": max(alturas) if alturas else 0},
    }, "edificios": edificios}

    os.makedirs(args.out, exist_ok=True)
    p_json = os.path.join(args.out, "%s-contexto50.json" % args.chip)
    with open(p_json, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    p_gj = os.path.join(args.out, "%s-contexto50.geojson" % args.chip)
    with open(p_gj, "w", encoding="utf-8") as f:
        json.dump({"type": "FeatureCollection", "metadata": out["metadata"], "features": feats},
                  f, ensure_ascii=False, indent=1)

    print("Edificios: %d | pisos max %d | alturas %.1f-%.1f m"
          % (len(edificios), out["metadata"]["conteo"]["pisos_max"],
             min(alturas), max(alturas)))
    print("OK -> %s" % p_json)


if __name__ == "__main__":
    main()
