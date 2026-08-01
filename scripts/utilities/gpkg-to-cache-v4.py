#!/usr/bin/env python3
# ==============================================================================
# gpkg-to-cache-v4.py
# ------------------------------------------------------------------------------
# Versión 4: integra CATASTRO (bd_uaecd.gpkg) + POT (Decreto 555/2021 .gdb)
#
# Flujo:
#   1. Carga el lote (JSON de entrada)
#   2. CATASTRO: JOIN espacial con Lote + JOIN atributo con Predio + Calificacion
#   3. POT: JOIN espacial con Area_elevacion_maxima (y otras capas POT)
#   4. Genera caché JSON consolidado con datos REALES (no valores por defecto)
#
# Uso:
#   python gpkg-to-cache-v4.py query --lot data/lotes-ejemplo/lote-real-002407033006.json
# ==============================================================================

from __future__ import annotations

import hashlib
import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

import click

try:
    import pyogrio
    from shapely.geometry import shape
    from shapely.validation import make_valid
except ImportError as e:
    click.echo(f"[ERROR] Dependencias faltantes: {e}", err=True)
    sys.exit(1)


PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
DEFAULT_CATASTRO_GPKG = os.environ.get(
    "POT_GPKG_PATH",
    r"D:\Users\Dario Salas\proyectos\DesParametrico\2-Entradas\Datos_Sitio_GDB\bd_uaecd.gpkg",
)
DEFAULT_POT_GDB = r"D:\Users\Dario Salas\proyectos\DesParametrico\2-Entradas\Datos_Sitio_GDB\POT\POT_Decreto_555_2021_Bogota_D_C.gdb"
DEFAULT_WHITELIST = PROJECT_ROOT / "config" / "field-whitelist.json"
DEFAULT_OUTPUT = PROJECT_ROOT / "data" / "pot-cache"
HASH_CACHE_FILE = PROJECT_ROOT / "data" / ".gpkg_hash_cache"

# Capas del POT que vamos a consultar (JOIN espacial con el lote)
POT_LAYERS_TO_QUERY = {
    "elevacion_maxima": {
        "layer": "Area_elevacion_maxima",
        "fields": ["ALTURA", "ELEVACION_MAXIMA", "CODIGO_UPI", "NOMBRE_UPI", "NORMATIVA", "RESTRICCION"],
        "description": "Altura máxima permitida y UPZ"
    },
    "tratamiento_urbanistico": {
        "layer": "TratamientoUrbanistico",
        "fields": ["NOMBRE", "TRATAMIENTO", "NORMATIVA", "ACTO_ADMINISTRATIVO", "NUMERO_ACTO_ADMINISTRATIVO"],
        "description": "Tratamiento: Conservación, Desarrollo, Renovación, Mejoramiento"
    },
    "area_actividad": {
        "layer": "AreaActividad",
        "fields": ["NOMBRE", "TIPO", "NORMATIVA", "ACTO_ADMINISTRATIVO"],
        "description": "Zona residencial, comercial, industrial, mixto"
    },
    "edificabilidad": {
        "layer": "Rango_edificabilidad_desarro",
        "fields": ["EDIFICABILIDAD", "RANGO", "NORMATIVA", "ACTO_ADMINISTRATIVO"],
        "description": "Índice de edificabilidad permitido"
    },
    "clasificacion_suelo": {
        "layer": "ClasificacionSuelo",
        "fields": ["CLASIFICACION", "TIPO", "NORMATIVA"],
        "description": "Suelo urbano, rural, expansión"
    },
    "unidad_planeamiento_local": {
        "layer": "Unidad_planeamiento_local",
        "fields": ["CODIGO", "NOMBRE", "UPZ", "NORMATIVA"],
        "description": "UPL - subdivisión de UPZ"
    },
    "sector_uso_residencial": {
        "layer": "Sector_uso_residencial",
        "fields": ["NOMBRE", "TIPO", "NORMATIVA"],
        "description": "Sectores residenciales específicos"
    },
    "suelo_proteccion_riesgo": {
        "layer": "SueloProteccionRiesgo",
        "fields": ["TIPO", "NIVEL_RIESGO", "NORMATIVA"],
        "description": "Suelo por riesgo (afecta edificabilidad)"
    },
}


# ---------------------------------------------------------------------------
# Utilidades (mismas que v3)
# ---------------------------------------------------------------------------
def file_hash_cached(path: Path) -> str:
    if HASH_CACHE_FILE.exists():
        try:
            cache = json.loads(HASH_CACHE_FILE.read_text(encoding="utf-8"))
            cached = cache.get(str(path), {})
            current = path.stat()
            if cached.get("size") == current.st_size and cached.get("mtime") == current.st_mtime:
                return cached.get("hash", "")
        except Exception:
            pass

    click.echo(f"[INFO] Calculando hash MD5 de {path.name} (~30s)...")
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8 * 1024 * 1024), b""):
            h.update(chunk)
    hash_val = h.hexdigest()

    try:
        cache = json.loads(HASH_CACHE_FILE.read_text(encoding="utf-8")) if HASH_CACHE_FILE.exists() else {}
        current = path.stat()
        cache[str(path)] = {"hash": hash_val, "size": current.st_size, "mtime": current.st_mtime}
        HASH_CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)
        HASH_CACHE_FILE.write_text(json.dumps(cache, indent=2), encoding="utf-8")
    except Exception:
        pass

    return hash_val


def load_whitelist(whitelist_path: Path) -> dict[str, Any]:
    if not whitelist_path.exists():
        return {}
    with open(whitelist_path, encoding="utf-8") as f:
        data = json.load(f)
    return {"_categorized": data.get("campos", {})}


def _truncate_coords_2d(coords: list) -> list:
    if not coords:
        return coords
    if isinstance(coords[0], (list, tuple)):
        return [_truncate_coords_2d(c) for c in coords]
    return list(coords[:2])


def _normalize_geometry_coords(geometry: dict) -> dict:
    if not isinstance(geometry, dict) or "coordinates" not in geometry:
        return geometry
    geom = dict(geometry)
    geom["coordinates"] = _truncate_coords_2d(geom["coordinates"])
    return geom


def load_lot(lot_path: Path) -> dict[str, Any]:
    with open(lot_path, encoding="utf-8") as f:
        data = json.load(f)

    if data.get("type") == "Feature":
        geometry = data["geometry"]
        properties = data.get("properties", {})
    elif data.get("type") == "FeatureCollection":
        if not data.get("features"):
            raise ValueError("FeatureCollection vacío")
        feature = data["features"][0]
        geometry = feature["geometry"]
        properties = feature.get("properties", {})
    elif "coordenadas" in data:
        coords = data["coordenadas"]["poligono"]
        geometry = {"type": "Polygon", "coordinates": [coords]}
        properties = {"predio_id": data.get("predio_id", "unknown")}
        properties.update(data.get("metadata", {}))
    else:
        raise ValueError(f"Formato de lote no reconocido: {lot_path}")

    geometry = _normalize_geometry_coords(geometry)
    polygon = shape(geometry)
    return {"polygon": polygon, "properties": properties, "raw": data}


def repair_geometry(geom):
    if geom is None or geom.is_valid:
        return geom
    try:
        geom = make_valid(geom)
        if geom.geom_type == "MultiPolygon":
            geom = max(geom.geoms, key=lambda g: g.area)
        elif geom.geom_type == "GeometryCollection":
            polys = [g for g in geom.geoms if g.geom_type == "Polygon"]
            if polys:
                geom = max(polys, key=lambda g: g.area)
            else:
                return None
    except Exception:
        try:
            geom = geom.buffer(0)
        except Exception:
            return None
    return geom


def extract_fields(row: dict, fields: list[str]) -> dict[str, Any]:
    result = {}
    for field_name in fields:
        for k, v in row.items():
            if k.lower() == field_name.lower():
                if hasattr(v, "item"):
                    v = v.item()
                # Convertir datetime a string
                if hasattr(v, "isoformat"):
                    v = v.isoformat()
                result[field_name] = v
                break
    return result


# ---------------------------------------------------------------------------
# CATASTRO (de v3)
# ---------------------------------------------------------------------------
def find_lote_in_gpkg(gpkg_path: Path, lot_polygon):
    bounds = lot_polygon.bounds
    click.echo(f"[INFO] Bounding box: ({bounds[0]:.2f}, {bounds[1]:.2f}, {bounds[2]:.2f}, {bounds[3]:.2f})")

    df = pyogrio.read_dataframe(str(gpkg_path), layer="Lote", bbox=bounds)
    click.echo(f"[INFO] Features cargados (filtrados por bbox): {len(df)}")

    if len(df) == 0:
        df = pyogrio.read_dataframe(str(gpkg_path), layer="Lote")

    if not lot_polygon.is_valid:
        lot_polygon = lot_polygon.buffer(0)

    matches = []
    invalid_count = 0

    for idx, row in df.iterrows():
        geom = row.geometry
        if geom is None:
            continue
        if not geom.is_valid:
            invalid_count += 1
            geom = repair_geometry(geom)
            if geom is None:
                continue
        try:
            if not geom.intersects(lot_polygon):
                continue
        except Exception:
            continue
        try:
            overlap_area = geom.intersection(lot_polygon).area
        except Exception:
            overlap_area = 0.0
        matches.append((idx, row, geom, overlap_area))

    if invalid_count > 0:
        click.echo(f"[INFO] Geometrías reparadas: {invalid_count}")

    matches.sort(key=lambda x: x[3], reverse=True)
    return matches


def find_predio_by_lot_codigo(gpkg_path: Path, lot_codigo: str) -> dict[str, Any] | None:
    if not lot_codigo:
        return None

    click.echo(f"[INFO] Buscando Predio con LotCodigo={lot_codigo}...")

    for campo in ["Barmanpre", "PreCedCata", "PreNupre", "PreChip"]:
        try:
            df = pyogrio.read_dataframe(
                str(gpkg_path), layer="Predio",
                where=f"{campo} = '{lot_codigo}'", max_features=1,
            )
            if len(df) > 0:
                row = df.iloc[0]
                predio_dict = {k: v for k, v in row.items() if k != "geometry"}
                click.echo(f"[OK] Predio encontrado por {campo}")
                return predio_dict
        except Exception:
            continue

    # Búsqueda parcial
    if len(lot_codigo) >= 9:
        sector_manzana = lot_codigo[:9]
        try:
            df = pyogrio.read_dataframe(
                str(gpkg_path), layer="Predio",
                where=f"Barmanpre LIKE '{sector_manzana}%'", max_features=10,
            )
            if len(df) > 0:
                row = df.iloc[0]
                return {k: v for k, v in row.items() if k != "geometry"}
        except Exception:
            pass

    return None


def find_calificacion_by_pre_chip(gpkg_path: Path, pre_chip: str) -> dict[str, Any] | None:
    if not pre_chip:
        return None

    click.echo(f"[INFO] Buscando Calificacion con PreChip={pre_chip}...")

    try:
        df = pyogrio.read_dataframe(
            str(gpkg_path), layer="Calificacion",
            where=f"PreChip = '{pre_chip}'", max_features=5,
        )
    except Exception as e:
        click.echo(f"[WARN] Error: {e}", err=True)
        return None

    if len(df) == 0:
        return None

    row = df.iloc[0]
    return {k: v for k, v in row.items() if k != "geometry"}


# ---------------------------------------------------------------------------
# POT (NUEVO)
# ---------------------------------------------------------------------------
def query_pot_layer(gdb_path: Path, layer_name: str, fields: list[str], lot_polygon) -> dict[str, Any]:
    """Hace JOIN espacial entre el lote y una capa del POT."""
    click.echo(f"[INFO] Consultando POT capa: {layer_name}")

    try:
        # Filtrar por bbox del lote
        bounds = lot_polygon.bounds
        df = pyogrio.read_dataframe(str(gdb_path), layer=layer_name, bbox=bounds)
        click.echo(f"  Features en bbox: {len(df)}")

        if len(df) == 0:
            # Sin filtro
            df = pyogrio.read_dataframe(str(gdb_path), layer=layer_name)
            click.echo(f"  Features totales: {len(df)}")

        if len(df) == 0:
            return {"_status": "vacia", "_error": "Capa sin features"}

        # Asegurar que el lote es válido
        if not lot_polygon.is_valid:
            lot_polygon_fixed = lot_polygon.buffer(0)
        else:
            lot_polygon_fixed = lot_polygon

        # Buscar el feature que contiene o intersecta el lote
        best_match = None
        best_overlap = 0

        for idx, row in df.iterrows():
            geom = row.geometry
            if geom is None:
                continue
            if not geom.is_valid:
                geom = repair_geometry(geom)
                if geom is None:
                    continue

            try:
                if not geom.intersects(lot_polygon_fixed):
                    continue
                overlap = geom.intersection(lot_polygon_fixed).area
                if overlap > best_overlap:
                    best_overlap = overlap
                    best_match = (idx, row)
            except Exception:
                continue

        if best_match is None:
            return {"_status": "no_interseca", "_error": "El lote no intersecta ningún feature de esta capa"}

        idx, row = best_match
        row_dict = {k: v for k, v in row.items() if k != "geometry"}
        extracted = extract_fields(row_dict, fields)

        click.echo(f"  [OK] Feature idx={idx}, overlap={best_overlap:.2f} m²")
        for k, v in extracted.items():
            click.echo(f"       {k}: {v}")

        return {
            "_status": "OK",
            "_feature_idx": str(idx),
            "_overlap_area_m2": best_overlap,
            **extracted,
        }

    except Exception as e:
        click.echo(f"  [ERROR] {e}", err=True)
        return {"_status": "error", "_error": str(e)}


def query_all_pot_layers(gdb_path: Path, lot_polygon) -> dict[str, Any]:
    """Consulta todas las capas POT configuradas."""
    click.echo("")
    click.echo("[POT] Consultando capas del Decreto 555/2021...")

    if not gdb_path.exists():
        click.echo(f"[ERROR] POT .gdb no encontrado: {gdb_path}", err=True)
        return {"_status": "gdb_no_encontrado"}

    result = {}
    for key, config in POT_LAYERS_TO_QUERY.items():
        click.echo("")
        result[key] = query_pot_layer(
            gdb_path,
            config["layer"],
            config["fields"],
            lot_polygon,
        )

    return result


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
@click.group()
def cli() -> None:
    """Consulta CATASTRO + POT y genera caché JSON consolidado."""
    pass


@cli.command()
@click.option("--lot", required=True, type=click.Path(exists=True))
@click.option("--catastro-gpkg", default=DEFAULT_CATASTRO_GPKG)
@click.option("--pot-gdb", default=DEFAULT_POT_GDB)
@click.option("--whitelist", default=str(DEFAULT_WHITELIST))
@click.option("--output", default=str(DEFAULT_OUTPUT))
def query(lot: str, catastro_gpkg: str, pot_gdb: str, whitelist: str, output: str) -> None:
    """Consulta catastro + POT y genera caché JSON con datos REALES."""

    catastro_path = Path(catastro_gpkg)
    pot_path = Path(pot_gdb)
    output_path = Path(output)
    output_path.mkdir(parents=True, exist_ok=True)

    # 1. Whitelist
    wl = load_whitelist(Path(whitelist))
    total_wl = sum(len(v) for v in wl.get("_categorized", {}).values())
    click.echo(f"[INFO] Whitelist cargada: {total_wl} campos")

    # 2. Lote
    lot_data = load_lot(Path(lot))
    predio_id = lot_data["properties"].get("predio_id", Path(lot).stem)
    click.echo(f"[INFO] Lote cargado: {predio_id}")
    click.echo(f"[INFO] Área: {lot_data['polygon'].area:.2f} m²")

    # 3. Hash catastro
    catastro_md5 = file_hash_cached(catastro_path)
    click.echo(f"[INFO] Hash catastro: {catastro_md5}")

    # ============================================
    # CATASTRO
    # ============================================
    click.echo("")
    click.echo("=" * 60)
    click.echo("[CATASTRO] Consultando bd_uaecd.gpkg")
    click.echo("=" * 60)

    # 4. Lote
    click.echo("")
    click.echo("[1/3] Capa Lote (JOIN espacial)...")
    lot_matches = find_lote_in_gpkg(catastro_path, lot_data["polygon"])

    if not lot_matches:
        click.echo("[ERROR] No se encontró lote.", err=True)
        sys.exit(2)

    idx, lot_row, lot_geom, overlap = lot_matches[0]
    lot_dict = {k: v for k, v in lot_row.items() if k != "geometry"}
    lot_codigo = lot_dict.get("LotCodigo")
    click.echo(f"[OK] LotCodigo: {lot_codigo}, overlap={overlap:.2f} m²")

    lot_fields = wl.get("_categorized", {}).get("lote_geometria", [])
    lot_data_extracted = extract_fields(lot_dict, lot_fields)

    # 5. Predio
    click.echo("")
    click.echo("[2/3] Capa Predio (JOIN por atributo)...")
    predio_dict = find_predio_by_lot_codigo(catastro_path, lot_codigo)

    predio_identificacion = {}
    predio_ubicacion = {}
    predio_areas = {}
    predio_uso_actual = {}
    pre_chip = None

    if predio_dict:
        pre_chip = predio_dict.get("PreChip")
        predio_identificacion = extract_fields(predio_dict, wl.get("_categorized", {}).get("predio_identificacion", []))
        predio_ubicacion = extract_fields(predio_dict, wl.get("_categorized", {}).get("predio_ubicacion", []))
        predio_areas = extract_fields(predio_dict, wl.get("_categorized", {}).get("predio_areas", []))
        predio_uso_actual = extract_fields(predio_dict, wl.get("_categorized", {}).get("predio_uso_actual", []))

    # 6. Calificacion
    click.echo("")
    click.echo("[3/3] Capa Calificacion (JOIN por PreChip)...")
    calif_dict = find_calificacion_by_pre_chip(catastro_path, pre_chip) if pre_chip else None

    calif_uso = {}
    vecinos_altura = {}
    altura_estimada_m = None
    altura_formula = None

    if calif_dict:
        calif_uso = extract_fields(calif_dict, wl.get("_categorized", {}).get("calificacion_uso", []))
        vecinos_altura = extract_fields(calif_dict, wl.get("_categorized", {}).get("vecinos_altura_estimada", []))

        pre_piso = calif_dict.get("PrePiso")
        if pre_piso is not None:
            try:
                altura_estimada_m = float(pre_piso) * 3.0
                altura_formula = "PrePiso × 3.0"
            except (ValueError, TypeError):
                pass

    # ============================================
    # POT
    # ============================================
    pot_data = query_all_pot_layers(pot_path, lot_geom)

    # Extraer campos clave del POT (si se encontraron)
    pot_elev = pot_data.get("elevacion_maxima", {})
    pot_trat = pot_data.get("tratamiento_urbanistico", {})
    pot_act = pot_data.get("area_actividad", {})
    pot_edif = pot_data.get("edificabilidad", {})
    pot_suelo = pot_data.get("clasificacion_suelo", {})
    pot_upl = pot_data.get("unidad_planeamiento_local", {})
    pot_resid = pot_data.get("sector_uso_residencial", {})
    pot_riesgo = pot_data.get("suelo_proteccion_riesgo", {})

    pot_altura_maxima = pot_elev.get("ALTURA") if pot_elev.get("_status") == "OK" else None
    pot_elevacion_maxima = pot_elev.get("ELEVACION_MAXIMA") if pot_elev.get("_status") == "OK" else None
    pot_upz = None
    if pot_elev.get("_status") == "OK":
        pot_upz = {
            "codigo": pot_elev.get("CODIGO_UPI"),
            "nombre": pot_elev.get("NOMBRE_UPI"),
        }
    pot_normativa = pot_elev.get("NORMATIVA") if pot_elev.get("_status") == "OK" else None

    # Resumen del POT (campos principales)
    pot_resumen = {
        "_status": "OK" if pot_altura_maxima is not None else "PENDIENTE",
        "_fuente": "Decreto 555 del 29 de diciembre de 2021",
        "altura_maxima_m": pot_altura_maxima,
        "elevacion_maxima_amsl_m": pot_elevacion_maxima,
        "upz": pot_upz,
        "tratamiento_urbanistico": {
            "nombre": pot_trat.get("NOMBRE"),
            "tratamiento": pot_trat.get("TRATAMIENTO"),
            "normativa": pot_trat.get("NORMATIVA"),
        } if pot_trat.get("_status") == "OK" else None,
        "area_actividad": {
            "nombre": pot_act.get("NOMBRE"),
            "tipo": pot_act.get("TIPO"),
            "normativa": pot_act.get("NORMATIVA"),
        } if pot_act.get("_status") == "OK" else None,
        "edificabilidad": {
            "valor": pot_edif.get("EDIFICABILIDAD"),
            "rango": pot_edif.get("RANGO"),
            "normativa": pot_edif.get("NORMATIVA"),
        } if pot_edif.get("_status") == "OK" else None,
        "clasificacion_suelo": {
            "clasificacion": pot_suelo.get("CLASIFICACION"),
            "tipo": pot_suelo.get("TIPO"),
        } if pot_suelo.get("_status") == "OK" else None,
        "unidad_planeamiento_local": {
            "codigo": pot_upl.get("CODIGO"),
            "nombre": pot_upl.get("NOMBRE"),
            "upz": pot_upl.get("UPZ"),
        } if pot_upl.get("_status") == "OK" else None,
        "sector_uso_residencial": {
            "nombre": pot_resid.get("NOMBRE"),
            "tipo": pot_resid.get("TIPO"),
        } if pot_resid.get("_status") == "OK" else None,
        "suelo_proteccion_riesgo": {
            "tipo": pot_riesgo.get("TIPO"),
            "nivel_riesgo": pot_riesgo.get("NIVEL_RIESGO"),
        } if pot_riesgo.get("_status") == "OK" else None,
        "normativa_legal": pot_normativa,
    }

    # ============================================
    # JSON FINAL
    # ============================================
    total_catastro = (
        len(lot_data_extracted) + len(predio_identificacion) + len(predio_ubicacion)
        + len(predio_areas) + len(predio_uso_actual) + len(calif_uso) + len(vecinos_altura)
    )

    # Contar capas POT exitosas
    pot_capas_ok = sum(1 for v in pot_data.values() if v.get("_status") == "OK")
    pot_capas_totales = len(pot_data)

    output_data = {
        "predio_id": predio_id,
        "consultado_en": datetime.now().isoformat(),
        "crs": {
            "catastro": "MAGNA Ciudad Bogota (ESRI:102233)",
            "pot": "PCS_CarMAGBOG (custom Bogotá)",
            "nota": "CRS similares, mismo false_easting/northing. Intersección espacial funciona."
        },
        "coordenadas": {
            "crs": "ESRI:102233",
            "poligono": lot_data["raw"].get("coordenadas", {}).get("poligono", []),
            "bbox": list(lot_geom.bounds),
        },
        "catastro": {
            "lote_geometria": lot_data_extracted,
            "predio_identificacion": predio_identificacion,
            "predio_ubicacion": predio_ubicacion,
            "predio_areas": predio_areas,
            "predio_uso_actual": predio_uso_actual,
            "calificacion_uso": calif_uso,
            "vecinos_altura_estimada": vecinos_altura,
            "_altura_estimada_m": altura_estimada_m,
            "_altura_formula": altura_formula,
        },
        "pot": pot_resumen,
        "pot_detalle_completo": pot_data,
        "metadatos": {
            "catastro_gpkg": str(catastro_path),
            "catastro_hash_md5": catastro_md5,
            "pot_gdb": str(pot_path),
            "lot_codigo": lot_codigo,
            "pre_chip": pre_chip,
            "campos_catastro_extraidos": total_catastro,
            "pot_capas_consultadas": pot_capas_totales,
            "pot_capas_encontradas": pot_capas_ok,
            "pot_altura_encontrada": pot_altura_maxima is not None,
            "joins_realizados": {
                "lote_espacial": True,
                "predio_atributo": predio_dict is not None,
                "calificacion_atributo": calif_dict is not None,
                "pot_elevacion_espacial": pot_altura_maxima is not None,
            }
        },
    }

    # Guardar
    output_file = output_path / f"{predio_id}.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2, default=str)

    click.echo("")
    click.echo("=" * 60)
    click.echo(f"[OK] Caché generado: {output_file}")
    click.echo(f"[OK] Campos catastro: {total_catastro}")
    click.echo(f"[OK] POT capas encontradas: {pot_capas_ok}/{pot_capas_totales}")
    click.echo(f"[OK] POT altura máxima: {pot_altura_maxima} m" + (" (REAL)" if pot_altura_maxima else " (no encontrada)"))
    click.echo(f"[OK] POT UPZ: {pot_upz['nombre'] if pot_upz else 'N/A'}")
    if pot_trat.get("_status") == "OK":
        click.echo(f"[OK] POT tratamiento: {pot_trat.get('TRATAMIENTO') or pot_trat.get('NOMBRE')}")
    if pot_edif.get("_status") == "OK":
        click.echo(f"[OK] POT edificabilidad: {pot_edif.get('EDIFICABILIDAD')}")
    click.echo("=" * 60)


if __name__ == "__main__":
    cli()
