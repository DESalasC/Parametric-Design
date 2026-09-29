"""
Script: fetch-urban-context-v7.py
Proyecto: DiseñoParametrico
Fase: 1 - Contexto y Lote
Version: 07
Descripcion:
    Extrae datos del lote, vecinos, POT y topografia desde la geobase oficial.
    NO clasifica lados (la geobase esta incompleta — ADR-008).
    La clasificacion de frentes ocurre en F1_NORMATIVA_APLICAR_v24 usando
    la regla hibrida de 15m con curvas combinadas (oficiales + manuales).
    Corregido: parseo de valores especiales de altura ("CHB", etc.) en POT GDB.

CAMBIOS v7 (2026-09-28) - TOPOGRAFIA REAL (plan lote-inclinado-candelaria, P0):
    1. Parser del MDT corregido: el servicio 'identify' del modelo digital de
       terreno devuelve la cota en attributes["Stretch.Pixel Value"]; el v6 leia
       results[0]["value"] (inexistente) y devolvia 0.0 en silencio -> todos los
       chips quedaban con topografia plana (z=0).
    2. Muestreo densificado del lote: rejilla interior (default 5 m) + anillo
       exterior en calles/entorno (default 6 m, paso 8 m); primero vertices /
       puntos medios / centroide (orden v6 estable para compatibilidad).
    3. Topografia ampliada (claves NUEVAS, sin romper contrato):
         topografia.resumen      -> z_min/z_max/delta, pendiente media (ajuste de
                                    plano), direccion de bajada, n_fallidos
         topografia.perfil_lados -> cota media/min/max por arista del lote
         malla_terreno[].tipo    -> vertice|punto_medio|centroide|interior|anillo
    4. Vertice de CIERRE del lote hereda la cota del primer vertice (antes tomaba
       la del primer punto medio). Sin cotas (servicio caido) se conserva el
       comportamiento v6: z=0 plano + nota en el resumen.
"""

import argparse
import os
import json
import math
import warnings
import requests
import geopandas as gpd
import numpy as np
import pyogrio
from shapely.geometry import box, Polygon, Point, mapping
from shapely.ops import transform
from pyproj import Transformer

warnings.filterwarnings('ignore', category=UserWarning)

# Rutas por defecto (fallback); se sobreescriben con --gpkg / --pot-gdb o variables de entorno
# 2026-09-28: default PORTABLE -> data/geobase del proyecto (la ruta historica queda como ultimo recurso)
_ROOT_PROY = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
_GPKG_PROY = os.path.join(_ROOT_PROY, "data", "geobase", "bd_uaecd.gpkg")
_GDB_PROY = os.path.join(_ROOT_PROY, "data", "geobase", "POT_Decreto_555_2021_Bogota_D_C.gdb")
GPKG_PATH_DEFAULT = _GPKG_PROY if os.path.exists(_GPKG_PROY) else r"D:\Users\Dario Salas\proyectos\DesParametrico\2-Entradas\Datos_Sitio_GDB\bd_uaecd.gpkg"
POT_GDB_PATH_DEFAULT = _GDB_PROY if os.path.exists(_GDB_PROY) else r"D:\Users\Dario Salas\proyectos\DesParametrico\2-Entradas\Datos_Sitio_GDB\POT\POT_Decreto_555_2021_Bogota_D_C.gdb"

# Variables de entorno (prefijo POT_ para consistencia con CLAUDE.md)
GPKG_PATH = os.environ.get("POT_GPKG_PATH", GPKG_PATH_DEFAULT)
POT_GDB_PATH = os.environ.get("POT_GDB_PATH", POT_GDB_PATH_DEFAULT)

CRS_TARGET = "ESRI:102233"
CRS_METRIC = "EPSG:3116"
BUFFER_M = 75
BUFFER_VIAS_M = 500  # Radio mayor para capturar la malla vial completa
ALTURA_PISO_M = 3.80
REST_IDENTIFY_URL = "https://serviciosgis.catastrobogota.gov.co/arcgis/rest/services/topografia/modelodigitalterrenobogotaurbano/MapServer/identify"

# v7: muestreo topografico densificado (plan P0 lote-inclinado)
TOPO_PASO_INTERIOR_M = 5.0    # rejilla interior del lote [m]
TOPO_ANILLO_M = 6.0           # anillo exterior (calles/entorno) [m]
TOPO_ANILLO_PASO_M = 8.0      # paso de muestreo del anillo [m]
TOPO_MAX_PUNTOS = 400         # tope de seguridad del muestreo

# Valores especiales de altura en el POT GDB (codigos alfanumericos)
ALTURA_CODIGOS_ESPECIALES = {
    "CHB": {"altura_max": 7.0, "rango": "1", "tratamiento_override": "Conservacion"},
    "CH":  {"altura_max": 7.0, "rango": "1", "tratamiento_override": "Conservacion"},
    "PAT": {"altura_max": 7.0, "rango": "1", "tratamiento_override": "Patrimonio"},
}


# --- OVERRIDE DE NORMA (orquestador) ---
# Completa los datos normativos que la geobase POT no trae (rango, altura, IO, IC,
# antejardin, tipologia). Lo edita el orquestador (data/pot-bogota/norma-override.json)
# y GANA sobre la geobase (el operador lo confirma).
NORMA_OVERRIDE_PATH = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "..", "data", "pot-bogota", "norma-override.json")


def _cargar_norma_override(chip):
    try:
        with open(NORMA_OVERRIDE_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception:
        return None
    if not isinstance(data, dict):
        return None
    lotes = data.get("lotes") if isinstance(data.get("lotes"), dict) else {}
    ov = lotes.get(chip)
    return ov if isinstance(ov, dict) else None


def _aplicar_norma_override(pot_data, chip):
    """Fusiona el override de norma (orquestador) en pot_data. El override GANA
    sobre la geobase. Devuelve True si se aplico al menos un campo."""
    ov = _cargar_norma_override(chip)
    if not ov:
        return False
    mapeo = {
        "upz": "upz",
        "tratamiento": "tratamiento",
        "tipologia": "tipologia",
        "rango_edificabilidad": "rango_edificabilidad",
        "io_maximo": "io_maximo",
        "ic_maximo": "ic_maximo",
        "semisotano_permitido": "semisotano_permitido",
        "voladizo_permitido": "voladizo_permitido",
        "subdivision_min_m2": "subdivision_min_m2",
        "frente_min_m": "frente_min_m",
        "fuente": "fuente_norma",
    }
    aplicado = []
    for k_src, k_dst in mapeo.items():
        v = ov.get(k_src)
        if v is None or v == "":
            continue
        pot_data[k_dst] = v
        aplicado.append(k_dst)
    aj = ov.get("antejardin_min_m")
    if aj is not None and aj != "":
        try:
            pot_data["antejardin_m"] = float(aj)
            aplicado.append("antejardin_m")
        except (ValueError, TypeError):
            pass
    pisos = ov.get("altura_maxima_pisos")
    if pisos is not None and pisos != "":
        try:
            pot_data["altura_maxima_pisos"] = int(pisos)
            if pot_data.get("altura_maxima_m") in (None, ""):
                pot_data["altura_maxima_m"] = round(float(pisos) * ALTURA_PISO_M, 2)
            aplicado.append("altura_maxima_pisos")
        except (ValueError, TypeError):
            pass
    if aplicado:
        print("  NORMA OVERRIDE aplicado (%s): %s" % (chip, ", ".join(aplicado)))
    return bool(aplicado)


def truncate_coords_2d(geom):
    if geom.is_empty: return geom
    if geom.has_z: return transform(lambda x, y, z=None: (x, y), geom)
    return geom


def make_geom_valid(geom):
    if not geom.is_valid: geom = geom.buffer(0)
    return truncate_coords_2d(geom)


def calculate_azimuth(poly):
    if not isinstance(poly, Polygon) or poly.is_empty: return 0.0
    coords = list(poly.exterior.coords)
    if len(coords) < 2: return 0.0
    x1, y1 = coords[0]; x2, y2 = coords[1]
    dx = x2 - x1; dy = y2 - y1
    if dx == 0 and dy == 0: return 0.0
    angulo_rad = math.atan2(dx, dy)
    angulo_deg = math.degrees(angulo_rad)
    return angulo_deg if angulo_deg >= 0 else angulo_deg + 360


def parse_elevation_value(resp_json):
    """v7: extrae la cota [m] de una respuesta 'identify' del MDT urbano.

    El servicio responde: {"results":[{"attributes":{"Stretch.Pixel Value":"2645.7"}}]}
    (el v6 leia results[0]["value"], inexistente -> devolvia 0.0 silencioso).
    Acepta tambien el formato viejo con "value" y textos tipo "Elevacion: 123".
    Devuelve float, o None si no hay valor numerico.
    """
    try:
        results = resp_json.get("results") or []
        if not results:
            return None
        res0 = results[0]
        val = None
        attrs = res0.get("attributes")
        if isinstance(attrs, dict):
            if "Stretch.Pixel Value" in attrs:
                val = attrs.get("Stretch.Pixel Value")
            else:
                for cand in attrs.values():
                    if cand is None or str(cand).strip() == "":
                        continue
                    try:
                        val = float(str(cand))
                        break
                    except (ValueError, TypeError):
                        continue
        if val is None:
            val = res0.get("value")
        if val is None:
            return None
        if isinstance(val, str):
            if ":" in val:
                val = val.split(":")[-1]
            val = val.strip()
        return float(val)
    except (ValueError, TypeError, AttributeError, IndexError):
        return None


def get_elevation_from_api(x_3116, y_3116):
    geometry = {"x": x_3116, "y": y_3116, "spatialReference": {"wkid": 3116}}
    params = {
        "geometry": json.dumps(geometry), "geometryType": "esriGeometryPoint",
        "sr": 3116, "tolerance": 2, "mapExtent": f"{x_3116-2},{y_3116-2},{x_3116+2},{y_3116+2}",
        "imageDisplay": "400,400,96", "returnGeometry": "false", "f": "json"
    }
    try:
        resp = requests.get(REST_IDENTIFY_URL, params=params, timeout=15)
        return parse_elevation_value(resp.json())
    except Exception:
        return None


def extract_elevations_online(points_xy, points_crs=CRS_TARGET):
    transformer = Transformer.from_crs(points_crs, CRS_METRIC, always_xy=True)
    zs = []
    n_fallidos = 0
    print(f"Consultando {len(points_xy)} puntos topograficos a la API...")
    for x, y in points_xy:
        x3116, y3116 = transformer.transform(x, y)
        z = get_elevation_from_api(x3116, y3116)
        if z is None:
            n_fallidos += 1
        zs.append(z)
    if n_fallidos:
        print("  ADVERTENCIA: %d/%d puntos sin cota (servicio/red)" % (n_fallidos, len(points_xy)))
    return zs


def generate_lote_topo_points(poly, paso_interior=TOPO_PASO_INTERIOR_M,
                              anillo_m=TOPO_ANILLO_M, anillo_paso=TOPO_ANILLO_PASO_M):
    """v7: puntos de muestreo topografico del lote.

    Orden (compatibilidad v6): (1) vertices, (2) puntos medios de arista,
    (3) centroide; v7 agrega (4) rejilla interior y (5) anillo exterior
    (calles/entorno). Devuelve lista de (x, y, tipo).
    """
    pts = []
    seen = []

    def _add(x, y, tipo, min_dist=1.0):
        if len(pts) >= TOPO_MAX_PUNTOS:
            return
        for (sx, sy) in seen:
            if (sx - x) ** 2 + (sy - y) ** 2 < min_dist * min_dist:
                return
        seen.append((x, y))
        pts.append((x, y, tipo))

    vertices = list(poly.exterior.coords)[:-1]
    n = len(vertices)
    for (vx, vy) in vertices:
        _add(vx, vy, "vertice", min_dist=1e-6)
    for i in range(n):
        p1 = vertices[i]; p2 = vertices[(i + 1) % n]
        _add((p1[0] + p2[0]) / 2.0, (p1[1] + p2[1]) / 2.0, "punto_medio", min_dist=1e-6)
    c = poly.centroid
    _add(c.x, c.y, "centroide", min_dist=1e-6)

    # (4) rejilla interior
    minx, miny, maxx, maxy = poly.bounds
    x = minx + paso_interior / 2.0
    while x < maxx:
        y = miny + paso_interior / 2.0
        while y < maxy:
            if poly.contains(Point(x, y)):
                _add(x, y, "interior")
            y += paso_interior
        x += paso_interior

    # (5) anillo exterior (calles / entorno)
    try:
        ring = poly.buffer(anillo_m)
        per = ring.exterior.length
        if per > 0:
            n_ring = max(8, int(per / max(1.0, anillo_paso)))
            for k in range(n_ring):
                pt = ring.exterior.interpolate(k * per / n_ring)
                _add(pt.x, pt.y, "anillo")
    except Exception as e:
        print("  ADVERTENCIA: anillo topografico no generado (%s)" % e)
    return pts


def calcular_resumen_topo(pts):
    """v7: resumen estadistico del muestreo (cotas absolutas).

    Ajusta un plano z = a*x + b*y + c por minimos cuadrados para estimar la
    pendiente media y la direccion de bajada (+y ~ norte de la proyeccion).
    """
    valid = [(p["x"], p["y"], p["z"]) for p in pts if p.get("z") is not None]
    resumen = {"n_puntos": len(pts), "n_validos": len(valid), "n_fallidos": len(pts) - len(valid)}
    if not valid:
        resumen.update({"z_min_m": None, "z_max_m": None, "delta_m": None,
                        "pendiente_media_pct": None, "pendiente_media_grados": None,
                        "direccion_bajada_grados": None,
                        "nota": "sin cotas (servicio/red); la topografia queda plana z=0"})
        return resumen
    zs = [z for (_x, _y, z) in valid]
    resumen.update({"z_min_m": round(min(zs), 2), "z_max_m": round(max(zs), 2),
                    "delta_m": round(max(zs) - min(zs), 2)})
    if len(valid) >= 3:
        try:
            A = np.array([[x, y, 1.0] for (x, y, _z) in valid])
            Z = np.array(zs)
            coef, _res, _rk, _sv = np.linalg.lstsq(A, Z, rcond=None)
            a = float(coef[0]); b = float(coef[1])
            grad = math.sqrt(a * a + b * b)
            resumen["pendiente_media_pct"] = round(grad * 100.0, 2)
            resumen["pendiente_media_grados"] = round(math.degrees(math.atan(grad)), 2)
            resumen["direccion_bajada_grados"] = round((math.degrees(math.atan2(-a, -b))) % 360.0, 1)
            resumen["pendiente_origen"] = "ajuste_plano_lstsq"
        except Exception:
            pass
    resumen["nota"] = ("cotas MDT Catastro (ESTIMADA). Validar con levantamiento. "
                       "La direccion usa +y como norte de la proyeccion.")
    return resumen


def main(chip, output_dir="data/pot-cache", gpkg_path=None, pot_gdb_path=None,
         topo_paso=None, topo_anillo=None, topo_anillo_paso=None):
    print(f"--- Iniciando fetch de contexto para CHIP: {chip} ---")

    # Permitir override de rutas via argumentos
    global GPKG_PATH, POT_GDB_PATH
    if gpkg_path:
        GPKG_PATH = gpkg_path
    if pot_gdb_path:
        POT_GDB_PATH = pot_gdb_path

    if not os.path.exists(GPKG_PATH):
        raise FileNotFoundError(f"No se encontro la geobase en: {GPKG_PATH}")

    target_lot_codigo = chip
    if any(c.isalpha() for c in chip):
        try:
            predio_info = pyogrio.read_info(GPKG_PATH, layer='Predio')
            predio_fields = predio_info['fields']
            chip_predio_field = next((f for f in ['PreChip', 'CHIP'] if f in predio_fields), None)
            if chip_predio_field:
                predio_gdf = gpd.read_file(GPKG_PATH, layer='Predio',
                                           where=f"{chip_predio_field} = '{chip}'", engine="pyogrio")
                if not predio_gdf.empty:
                    fk_field = next((f for f in ['LotCodigo', 'Barmanpre'] if f in predio_gdf.columns), None)
                    if fk_field: target_lot_codigo = str(predio_gdf.iloc[0][fk_field])
        except Exception as e:
            print(f"Advertencia: No se pudo hacer JOIN con Predio ({e}).")

    layer_info = pyogrio.read_info(GPKG_PATH, layer='Lote')
    available_fields = layer_info['fields']
    chip_field = 'LotCodigo' if 'LotCodigo' in available_fields else 'Barmanpre'
    lote_gdf = gpd.read_file(GPKG_PATH, layer='Lote',
                             where=f"{chip_field} = '{target_lot_codigo}'", engine="pyogrio")

    if lote_gdf.empty:
        raise ValueError(f"No se encontro el lote con {chip_field}: {target_lot_codigo}")

    lote_geom = make_geom_valid(lote_gdf.geometry.iloc[0])
    print(f"Lote encontrado. Area: {lote_geom.area:.2f} m2")

    bbox = box(*lote_geom.bounds)
    buffer_poly = bbox.buffer(BUFFER_M)
    buffer_vias = bbox.buffer(BUFFER_VIAS_M)

    vecinos_gdf = gpd.read_file(GPKG_PATH, layer='Lote', mask=buffer_poly, engine="pyogrio")
    if chip_field in vecinos_gdf.columns:
        vecinos_gdf = vecinos_gdf[vecinos_gdf[chip_field] != target_lot_codigo]

    # --- EXTRACCION DE DATOS POT ---
    pot_data = {"upz": "N/A", "altura_maxima_m": None, "altura_maxima_raw": None,
                "rango_edificabilidad": None, "tratamiento": "N/A",
                "sector_normativo": None}

    if os.path.exists(POT_GDB_PATH):
        print("Consultando Geodatabase del POT (.gdb)...")
        try:
            # 1. UPZ
            alt_gdf = gpd.read_file(POT_GDB_PATH, layer='Area_elevacion_maxima',
                                    mask=lote_geom, engine="pyogrio")
            if not alt_gdf.empty:
                pot_data["upz"] = str(alt_gdf.iloc[0].get('NOMBRE_UPI', 'N/A'))

            # 2. Tratamiento y Altura
            trat_gdf = gpd.read_file(POT_GDB_PATH, layer='TratamientoUrbanistico',
                                     mask=lote_geom, engine="pyogrio")
            if not trat_gdf.empty:
                pot_data["tratamiento"] = str(trat_gdf.iloc[0].get('NOMBRE_TRATAMIENTO', 'N/A'))
                alt_pisos = trat_gdf.iloc[0].get('ALTURA_MAXIMA')
                if alt_pisos is not None:
                    try:
                        pot_data["altura_maxima_m"] = float(alt_pisos) * ALTURA_PISO_M
                    except (ValueError, TypeError):
                        # Valor no numerico (ej: "CHB" para Centro Historico)
                        codigo = str(alt_pisos).strip().upper()
                        pot_data["altura_maxima_raw"] = codigo
                        if codigo in ALTURA_CODIGOS_ESPECIALES:
                            especial = ALTURA_CODIGOS_ESPECIALES[codigo]
                            pot_data["altura_maxima_m"] = especial["altura_max"]
                            pot_data["rango_edificabilidad"] = especial["rango"]
                            pot_data["tratamiento"] = especial.get("tratamiento_override", pot_data["tratamiento"])
                            print(f"  POT: codigo especial '{codigo}' -> altura={especial['altura_max']}m, rango={especial['rango']}, tratamiento={pot_data['tratamiento']}")
                        else:
                            print(f"  ADVERTENCIA: Codigo de altura no reconocido: '{codigo}'")

            # 3. Rango de edificabilidad (si no se establecio por codigo especial)
            if pot_data["rango_edificabilidad"] is None:
                edif_gdf = gpd.read_file(POT_GDB_PATH, layer='Rango_edificabilidad_desarro',
                                         mask=lote_geom, engine="pyogrio")
                if not edif_gdf.empty:
                    pot_data["rango_edificabilidad"] = str(edif_gdf.iloc[0].get('RANGO', 'N/A'))

            print(f"Datos POT extraidos: {pot_data}")
        except Exception as e:
            print(f"Advertencia: No se pudo leer el POT .gdb ({e}).")
    else:
        print(f"Advertencia: No se encontro el POT .gdb en {POT_GDB_PATH}")

    # --- OVERRIDE DE NORMA (orquestador): completa lo que la geobase no trae ---
    _aplicar_norma_override(pot_data, chip)

    def es_via_no_frontal(row):
        """Determina si una vía es de tipo 'via_no_frontal' (no genera setback pero cuenta para esquina).
        Basado en campos típicos del POT GDB."""
        # Verificar campos comunes que podrían indicar vía peatonal o de alcance limitado
        tipo_via = str(row.get('TIPO_VIA', '')).strip().upper()
        perfil_tipo = str(row.get('PERFIL_TIPO', '')).strip().upper()
        clasificacion = str(row.get('CLASIFICACION_VIAL', row.get('CLASIFICACION', ''))).strip().upper()

        # Indicadores comunes de vía_no_frontal (peatonal, de servicio, etc.)
        no_frontal_indicators = [
            'PEATONAL', 'PEDESTRIAN', 'WALKWAY', 'SIDEWALK',
            'SERVICIO', 'SERVICE', 'ACCESO', 'ACCESS',
            'CICLOVIA', 'BIKE PATH', 'CICLORUTA'
        ]

        # Verificar si algún indicador está presente en los campos
        for indicator in no_frontal_indicators:
            if (indicator in tipo_via or
                indicator in perfil_tipo or
                indicator in clasificacion):
                return True

        # Verificar valores específicos conocidos
        if tipo_via in ['PEATONAL', 'PEDESTRIAN', 'WALKWAY']:
            return True

        return False

    # --- EXTRACCION DE VIAS (3 capas del POT GDB) ---
    vias_oficiales = []
    espacios_publicos = []

    def extract_via_layer(layer_name, geom_type_check=True):
        """Extrae geometrias de una capa vial del POT GDB y las separa en vias_oficiales y espacios_publicos.
        Las vias_no_frontal van a espacios_publicos (no generan setback pero cuenta para esquina)."""
        nonlocal vias_oficiales, espacios_publicos
        try:
            gdf = gpd.read_file(POT_GDB_PATH, layer=layer_name, mask=buffer_vias, engine="pyogrio")
            if gdf is None or gdf.empty:
                return 0
            count = 0
            for idx, row in gdf.iterrows():
                geom = row.geometry
                if geom is None or geom.is_empty:
                    continue
                coords_list = []
                if geom.geom_type == 'MultiLineString':
                    for line in geom.geoms:
                        coords_list.append(list(line.coords))
                elif geom.geom_type == 'LineString':
                    coords_list.append(list(geom.coords))
                elif geom.geom_type == 'MultiPolygon':
                    for poly in geom.geoms:
                        coords_list.append(list(poly.exterior.coords))
                elif geom.geom_type == 'Polygon':
                    coords_list.append(list(geom.exterior.coords))

                # Determinar si es via_no_frontal
                if es_via_no_frontal(row):
                    # Agregar a espacios_publicos (no genera setback pero cuenta para esquina)
                    for coords in coords_list:
                        espacios_publicos.append({
                            "fuente": layer_name,
                            "nombre": str(row.get('NOMBRE', '')),
                            "tipo": "via_no_frontal",
                            "coordenadas": coords
                        })
                        count += 1
                else:
                    # Agregar a vias_oficiales (genera setback)
                    for coords in coords_list:
                        vias_oficiales.append({
                            "fuente": layer_name,
                            "codigo": str(row.get('CODIGO_ID', '')),
                            "nombre": str(row.get('NOMBRE', '')),
                            "clasificacion_vial": str(row.get('CLASIFICACION_VIAL', row.get('CLASIFICACION', ''))),
                            "tipo_via": str(row.get('TIPO_VIA', row.get('PERFIL_TIPO', ''))),
                            "ancho": row.get('ANCHO'),
                            "coordenadas": coords
                        })
                        count += 1
            return count
        except Exception as e:
            print(f"  {layer_name}: error ({e})")
            return 0

    if os.path.exists(POT_GDB_PATH):
        print("Extrayendo capas viales del POT GDB...")
        n1 = extract_via_layer('Eje_vial')
        n2 = extract_via_layer('MallaVialIntermedia')
        n3 = extract_via_layer('RedInfraestructuraVialArterial')
        print(f"  Vias extraidas: Eje_vial={n1}, MallaIntermedia={n2}, VialArterial={n3} = {len(vias_oficiales)} total")

        # --- Espacios publicos (parques, plazas, zonas verdes) ---
        for capa_ep in ['Parque', 'Plaza', 'Espacio_publico_centro_poblado']:
            try:
                ep_gdf = gpd.read_file(POT_GDB_PATH, layer=capa_ep, mask=buffer_vias, engine="pyogrio")
                if ep_gdf is not None and not ep_gdf.empty:
                    for idx, row in ep_gdf.iterrows():
                        geom = row.geometry
                        if geom is None or geom.is_empty:
                            continue
                        if geom.geom_type in ('Polygon', 'MultiPolygon'):
                            coords = list(geom.exterior.coords) if geom.geom_type == 'Polygon' else list(geom.geoms[0].exterior.coords)
                            espacios_publicos.append({
                                "fuente": capa_ep,
                                "nombre": str(row.get('NOMBRE', '')),
                                "tipo": capa_ep,
                                "coordenadas": coords
                            })
            except Exception as e:
                pass
        print(f"  Espacios publicos extraidos: {len(espacios_publicos)}")

    # --- TOPOGRAFIA (v7: parser MDT corregido + muestreo densificado) ---
    topo_pts_tipos = generate_lote_topo_points(
        lote_geom,
        paso_interior=topo_paso or TOPO_PASO_INTERIOR_M,
        anillo_m=topo_anillo or TOPO_ANILLO_M,
        anillo_paso=topo_anillo_paso or TOPO_ANILLO_PASO_M)
    topo_xy = [(x, y) for (x, y, _t) in topo_pts_tipos]
    zs_topo = extract_elevations_online(topo_xy)
    lote_verts_xy = list(lote_geom.exterior.coords)
    n_edges = max(0, len(lote_verts_xy) - 1)

    lote_verts_3d = []
    for i, (x, y) in enumerate(lote_verts_xy):
        if i < n_edges and i < len(zs_topo) and zs_topo[i] is not None:
            z = zs_topo[i]
        elif i >= n_edges and lote_verts_3d:
            z = lote_verts_3d[0][2]  # v7: cierre = cota del primer vertice
        else:
            z = 0.0
        lote_verts_3d.append((x, y, z))

    mesh_points = [{"id": f"P{i}", "x": x, "y": y, "z": z, "tipo": t}
                   for i, ((x, y, t), z) in enumerate(zip(topo_pts_tipos, zs_topo))]

    resumen_topo = calcular_resumen_topo(
        [{"x": x, "y": y, "z": z} for ((x, y, _t), z) in zip(topo_pts_tipos, zs_topo)])

    # v7: perfil de cotas por arista del lote (insumo para lados/cotas de frente)
    perfil_lados = []
    for i in range(n_edges):
        j = (i + 1) % n_edges
        zs_e = []
        for idx in (i, n_edges + i, j):
            if 0 <= idx < len(zs_topo) and zs_topo[idx] is not None:
                zs_e.append(zs_topo[idx])
        if zs_e:
            perfil_lados.append({
                "id": i,
                "z_media_m": round(sum(zs_e) / len(zs_e), 2),
                "z_min_m": round(min(zs_e), 2),
                "z_max_m": round(max(zs_e), 2),
                "n": len(zs_e),
            })
        else:
            perfil_lados.append({"id": i, "z_media_m": None, "z_min_m": None, "z_max_m": None, "n": 0})

    all_zs = [z for _, _, z in lote_verts_3d] + [p["z"] for p in mesh_points if p["z"] is not None]
    min_z = min(all_zs) if all_zs else 0.0

    # --- VECINOS ---
    vecinos_data = []
    for idx, row in vecinos_gdf.iterrows():
        v_geom = make_geom_valid(row.geometry)
        v_xy = list(v_geom.exterior.coords)
        vecinos_data.append({
            "chip": str(row.get(chip_field, 'N/A')),
            "vertices_3d": [(x, y, 0.0) for x, y in v_xy]
        })

    # --- COORDENADAS LOCALES ---
    minx, miny, maxx, maxy = buffer_poly.bounds
    lote_local = [(x - minx, y - miny, z - min_z) for x, y, z in lote_verts_3d]
    # v7: vecinos sin cota -> datum local z=0.0 (antes: 0.0 - min_z, que con
    # cotas reales habria desplazado la geometria hacia abajo por -min_z)
    vecinos_local = [{
        "chip": v["chip"],
        "vertices_3d_local": [(x - minx, y - miny, 0.0) for x, y, z in v["vertices_3d"]]
    } for v in vecinos_data]
    # v7: se descartan puntos sin cota (antes caian a 0.0 -> z local absurdo con
    # cotas reales); el conteo de fallidos queda en topografia.resumen
    mesh_local = [{
        "id": p["id"],
        "x_local": p["x"] - minx,
        "y_local": p["y"] - miny,
        "z_local": p["z"] - min_z,
        "tipo": p.get("tipo", "vertice")
    } for p in mesh_points if p["z"] is not None]

    azimuth = calculate_azimuth(lote_geom)

    # Convertir vias a coordenadas locales
    vias_oficiales_local = []
    for via in vias_oficiales:
        # v7: z de referencia = datum local (0.0)
        coords_local = [(x - minx, y - miny, 0.0) for x, y in via["coordenadas"]]
        vias_oficiales_local.append({
            "fuente": via.get("fuente", ""),
            "codigo": via["codigo"],
            "nombre": via["nombre"],
            "clasificacion_vial": via["clasificacion_vial"],
            "tipo_via": via["tipo_via"],
            "ancho": via.get("ancho"),
            "coordenadas_local": coords_local
        })

    # Convertir espacios publicos a coordenadas locales
    espacios_publicos_local = []
    for ep in espacios_publicos:
        # v7: z de referencia = datum local (0.0)
        coords_local = [(x - minx, y - miny, 0.0) for x, y in ep["coordenadas"]]
        espacios_publicos_local.append({
            "fuente": ep["fuente"],
            "nombre": ep["nombre"],
            "tipo": ep["tipo"],
            "coordenadas_local": coords_local
        })

    # ═══════════════════════════════════════════════════════════════
    # CLASIFICACION DE LADOS: NO se hace aqui.
    # La geobase oficial esta incompleta (calles no digitalizadas
    # en Eje_vial). La clasificacion real ocurre en el script
    # F1_NORMATIVA_APLICAR_v24 usando la regla hibrida de 15m
    # (ADR-008) con curvas de via combinadas:
    #   - oficiales: extraidas del Eje_vial del POT (incompletas)
    #   - manuales: dibujadas en ArchiCAD (completan lo faltante)
    # ═══════════════════════════════════════════════════════════════
    print("NOTA: La clasificacion de frentes NO se hace en este script.")
    print("      Se delega a F1_NORMATIVA_APLICAR_v24 (regla hibrida 15m, ADR-008).")

    output_data = {
        "metadata": {
            "chip": chip,
            "origen_sirgas": {"crs": CRS_TARGET, "x": minx, "y": miny, "z": min_z},
            "azimuth_norte_grados": azimuth,
            "buffer_metros": BUFFER_M
        },
        "pot_data": pot_data,
        "topografia": {
            "estado": "ESTIMADA",
            "fuente": "Catastro_REST_API_MDT",
            "version": "v2",
            "muestreo": {
                "paso_interior_m": topo_paso or TOPO_PASO_INTERIOR_M,
                "anillo_m": topo_anillo or TOPO_ANILLO_M,
                "anillo_paso_m": topo_anillo_paso or TOPO_ANILLO_PASO_M,
            },
            "resumen": resumen_topo,
            "perfil_lados": perfil_lados,
            "malla_terreno": mesh_local
        },
        "lote_objetivo": {
            "vertices_3d_local": lote_local,
            "area_m2": round(lote_geom.area, 2)
        },
        "vecinos": vecinos_local,
        "vias_oficiales": vias_oficiales_local,
        "espacios_publicos": espacios_publicos_local
    }

    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f"{chip}-contexto.json")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)
    print(f"EXITO: Contexto guardado en {output_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--chip", required=True)
    parser.add_argument("--output-dir", default="data/pot-cache")
    parser.add_argument("--gpkg", default=None, help="Ruta a bd_uaecd.gpkg (override)")
    parser.add_argument("--pot-gdb", default=None, help="Ruta a POT.gdb (override)")
    # v7: parametros del muestreo topografico
    parser.add_argument("--topo-paso", type=float, default=None,
                        help="Paso de la rejilla interior [m] (default %s)" % TOPO_PASO_INTERIOR_M)
    parser.add_argument("--topo-anillo", type=float, default=None,
                        help="Offset del anillo exterior [m] (default %s)" % TOPO_ANILLO_M)
    parser.add_argument("--topo-anillo-paso", type=float, default=None,
                        help="Paso del anillo exterior [m] (default %s)" % TOPO_ANILLO_PASO_M)
    args = parser.parse_args()
    project_root = os.environ.get("DISENO_PARAMETRICO_ROOT", os.getcwd())
    out_dir = os.path.join(project_root, args.output_dir) if not os.path.isabs(args.output_dir) else args.output_dir
    main(args.chip, out_dir, gpkg_path=args.gpkg, pot_gdb_path=args.pot_gdb,
         topo_paso=args.topo_paso, topo_anillo=args.topo_anillo,
         topo_anillo_paso=args.topo_anillo_paso)
