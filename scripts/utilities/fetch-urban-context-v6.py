"""
Script: fetch-urban-context-v6.py
Proyecto: DiseñoParametrico
Fase: 1 - Contexto y Lote
Version: 06
Descripcion:
    Extrae datos del lote, vecinos, POT y topografia desde la geobase oficial.
    NO clasifica lados (la geobase esta incompleta — ADR-008).
    La clasificacion de frentes ocurre en F1_NORMATIVA_APLICAR_v24 usando
    la regla hibrida de 15m con curvas combinadas (oficiales + manuales).
    Corregido: parseo de valores especiales de altura ("CHB", etc.) en POT GDB.
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

GPKG_PATH = r"D:\Users\Dario Salas\proyectos\DesParametrico\2-Entradas\Datos_Sitio_GDB\bd_uaecd.gpkg"
POT_GDB_PATH = r"D:\Users\Dario Salas\proyectos\DesParametrico\2-Entradas\Datos_Sitio_GDB\POT\POT_Decreto_555_2021_Bogota_D_C.gdb"

CRS_TARGET = "ESRI:102233"
CRS_METRIC = "EPSG:3116"
BUFFER_M = 75
BUFFER_VIAS_M = 500  # Radio mayor para capturar la malla vial completa
ALTURA_PISO_M = 3.80
REST_IDENTIFY_URL = "https://serviciosgis.catastrobogota.gov.co/arcgis/rest/services/topografia/modelodigitalterrenobogotaurbano/MapServer/identify"

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


def get_elevation_from_api(x_3116, y_3116):
    geometry = {"x": x_3116, "y": y_3116, "spatialReference": {"wkid": 3116}}
    params = {
        "geometry": json.dumps(geometry), "geometryType": "esriGeometryPoint",
        "sr": 3116, "tolerance": 0, "mapExtent": f"{x_3116-1},{y_3116-1},{x_3116+1},{y_3116+1}",
        "imageDisplay": "1,1,96", "returnGeometry": "false", "f": "json"
    }
    try:
        resp = requests.get(REST_IDENTIFY_URL, params=params, timeout=10)
        data = resp.json()
        if "results" in data and len(data["results"]) > 0:
            val = data["results"][0].get("value", "0")
            if isinstance(val, str):
                if ":" in val: val = val.split(":")[-1]
                return float(val.strip())
            return float(val)
    except:
        pass
    return 0.0


def extract_elevations_online(points_xy, points_crs=CRS_TARGET):
    transformer = Transformer.from_crs(points_crs, CRS_METRIC, always_xy=True)
    zs = []
    print(f"Consultando {len(points_xy)} puntos topograficos a la API...")
    for x, y in points_xy:
        x3116, y3116 = transformer.transform(x, y)
        z = get_elevation_from_api(x3116, y3116)
        zs.append(z)
    return zs


def generate_lote_topo_points(poly):
    points = list(poly.exterior.coords)[:-1]
    for i in range(len(points)):
        p1 = points[i]; p2 = points[(i+1) % len(points)]
        points.append(((p1[0]+p2[0])/2, (p1[1]+p2[1])/2))
    centroid = poly.centroid
    points.append((centroid.x, centroid.y))
    return points


def main(chip, output_dir="data/pot-cache"):
    print(f"--- Iniciando fetch de contexto para CHIP: {chip} ---")

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

    # --- TOPOGRAFIA ---
    topo_lote_xy = generate_lote_topo_points(lote_geom)
    zs_lote = extract_elevations_online(topo_lote_xy)
    lote_verts_xy = list(lote_geom.exterior.coords)
    n_verts = len(lote_verts_xy)
    lote_verts_3d = [(x, y, z) for (x, y), z in zip(lote_verts_xy, zs_lote[:n_verts])]
    mesh_points = [{"id": f"P{i}", "x": x, "y": y, "z": z}
                   for i, ((x, y), z) in enumerate(zip(topo_lote_xy, zs_lote))]

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
    vecinos_local = [{
        "chip": v["chip"],
        "vertices_3d_local": [(x - minx, y - miny, 0.0 - min_z) for x, y, z in v["vertices_3d"]]
    } for v in vecinos_data]
    mesh_local = [{
        "id": p["id"],
        "x_local": p["x"] - minx,
        "y_local": p["y"] - miny,
        "z_local": (p["z"] or 0.0) - min_z
    } for p in mesh_points]

    azimuth = calculate_azimuth(lote_geom)

    # Convertir vias a coordenadas locales
    vias_oficiales_local = []
    for via in vias_oficiales:
        coords_local = [(x - minx, y - miny, 0.0 - min_z) for x, y in via["coordenadas"]]
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
        coords_local = [(x - minx, y - miny, 0.0 - min_z) for x, y in ep["coordenadas"]]
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
            "fuente": "Catastro_REST_API",
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
    args = parser.parse_args()
    project_root = os.environ.get("DISENO_PARAMETRICO_ROOT", os.getcwd())
    out_dir = os.path.join(project_root, args.output_dir) if not os.path.isabs(args.output_dir) else args.output_dir
    main(args.chip, out_dir)
