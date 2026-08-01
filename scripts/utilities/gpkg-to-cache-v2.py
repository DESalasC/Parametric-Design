#!/usr/bin/env python3
# ==============================================================================
# gpkg-to-cache-v2.py
# ------------------------------------------------------------------------------
# Versión mejorada: consulta Lote + Predio + Calificacion en un solo caché.
#
# Mejoras vs v1:
#   - Hace JOIN automático entre capas usando PreChip / LotCodigo
#   - Genera un solo JSON consolidado con todas las categorías
#   - Maneja geometrías inválidas con make_valid + buffer(0)
#   - Cacha el hash MD5 del .gpkg para acelerar queries repetidos
#   - Trunca coords 4D a 2D automáticamente
#
# Uso:
#   python gpkg-to-cache-v2.py query --lot data/lotes-ejemplo/lote-chapinero.json
#   python gpkg-to-cache-v2.py list-layers
#   python gpkg-to-cache-v2.py show-fields --layer Lote --limit 1
#
# Salida:
#   data/pot-cache/<predio-id>.json con TODAS las categorías extraídas
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
    click.echo("Instala con: pip install pyogrio shapely click rich pyproj", err=True)
    sys.exit(1)


# ---------------------------------------------------------------------------
# Configuración
# ---------------------------------------------------------------------------
DEFAULT_GPKG = os.environ.get(
    "POT_GPKG_PATH",
    r"D:\Users\Dario Salas\proyectos\DesParametrico\2-Entradas\Datos_Sitio_GDB\bd_uaecd.gpkg",
)
DEFAULT_WHITELIST = Path(__file__).resolve().parent.parent.parent / "config" / "field-whitelist.json"
DEFAULT_OUTPUT = Path(__file__).resolve().parent.parent.parent / "data" / "pot-cache"
HASH_CACHE_FILE = Path(__file__).resolve().parent.parent.parent / "data" / ".gpkg_hash_cache"


# ---------------------------------------------------------------------------
# Utilidades
# ---------------------------------------------------------------------------
def file_hash_cached(path: Path) -> str:
    """Calcula hash MD5 del .gpkg, con caché en disco para acelerar queries repetidos."""
    if HASH_CACHE_FILE.exists():
        try:
            cache = json.loads(HASH_CACHE_FILE.read_text(encoding="utf-8"))
            cached_stat = cache.get(str(path), {})
            current_stat = path.stat()
            if (cached_stat.get("size") == current_stat.st_size
                and cached_stat.get("mtime") == current_stat.st_mtime):
                return cached_stat.get("hash", "")
        except Exception:
            pass

    # Calcular hash
    click.echo(f"[INFO] Calculando hash MD5 de {path.name} (3.1 GB, ~30s)...")
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192 * 1024), b""):  # chunks de 8MB
            h.update(chunk)
    hash_val = h.hexdigest()

    # Guardar caché
    try:
        if HASH_CACHE_FILE.exists():
            cache = json.loads(HASH_CACHE_FILE.read_text(encoding="utf-8"))
        else:
            cache = {}
        current_stat = path.stat()
        cache[str(path)] = {
            "hash": hash_val,
            "size": current_stat.st_size,
            "mtime": current_stat.st_mtime,
        }
        HASH_CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)
        HASH_CACHE_FILE.write_text(json.dumps(cache, indent=2), encoding="utf-8")
    except Exception as e:
        click.echo(f"[WARN] No se pudo cachear hash: {e}", err=True)

    return hash_val


def load_whitelist(whitelist_path: Path) -> dict[str, Any]:
    """Carga la whitelist de campos relevantes."""
    if not whitelist_path.exists():
        click.echo(f"[WARN] Whitelist no encontrada: {whitelist_path}", err=True)
        return {}

    with open(whitelist_path, encoding="utf-8") as f:
        data = json.load(f)

    campos = data.get("campos", {})
    return {"_categorized": campos}


def _truncate_coords_2d(coords: list) -> list:
    """Trunca coordenadas a 2D."""
    if not coords:
        return coords
    if isinstance(coords[0], (list, tuple)):
        return [_truncate_coords_2d(c) for c in coords]
    return list(coords[:2])


def _normalize_geometry_coords(geometry: dict) -> dict:
    """Normaliza coords GeoJSON a 2D."""
    if not isinstance(geometry, dict) or "coordinates" not in geometry:
        return geometry
    geom = dict(geometry)
    geom["coordinates"] = _truncate_coords_2d(geom["coordinates"])
    return geom


def load_lot(lot_path: Path) -> dict[str, Any]:
    """Carga el lote desde GeoJSON o JSON interno."""
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
    """Repara una geometría inválida usando make_valid + buffer(0)."""
    if geom is None:
        return None
    if geom.is_valid:
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
    """Extrae campos de una fila según lista de fields. Búsqueda case-insensitive."""
    result = {}
    for field_name in fields:
        for k, v in row.items():
            if k.lower() == field_name.lower():
                # Convertir tipos no serializables
                if hasattr(v, "item"):
                    v = v.item()
                result[field_name] = v
                break
    return result


def find_intersecting_features(gpkg_path: Path, layer: str, lot_polygon, max_features: int = 10):
    """Encuentra features de la capa que intersectan el lote."""
    bounds = lot_polygon.bounds
    click.echo(f"[INFO] Bounding box: {bounds}")

    df = pyogrio.read_dataframe(str(gpkg_path), layer=layer, bbox=bounds)
    click.echo(f"[INFO] Features cargados (filtrados por bbox): {len(df)}")

    if len(df) == 0:
        click.echo(f"[WARN] Sin features en bbox. Cargando todo (puede tardar)...", err=True)
        df = pyogrio.read_dataframe(str(gpkg_path), layer=layer)

    # Asegurar que el lote es válido
    if not lot_polygon.is_valid:
        click.echo("[WARN] Lote inválido. Reparando con buffer(0)...", err=True)
        lot_polygon = lot_polygon.buffer(0)

    matches = []
    invalid_count = 0
    checked = 0

    for idx, row in df.iterrows():
        geom = row.geometry
        if geom is None:
            continue
        checked += 1

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

        if len(matches) >= max_features:
            break

    if invalid_count > 0:
        click.echo(f"[INFO] Geometrías reparadas: {invalid_count} de {checked}")

    # Ordenar por overlap descendente
    matches.sort(key=lambda x: x[3], reverse=True)
    return matches


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
@click.group()
def cli() -> None:
    """Utilidad para consultar el .gpkg de POT/Catastro de Bogotá."""
    pass


@cli.command()
@click.option("--gpkg", default=DEFAULT_GPKG)
def list_layers(gpkg: str) -> None:
    """Lista las capas del .gpkg."""
    gpkg_path = Path(gpkg)
    if not gpkg_path.exists():
        click.echo(f"[ERROR] No encontrado: {gpkg_path}", err=True)
        sys.exit(1)
    layers = pyogrio.list_layers(str(gpkg_path))
    click.echo(f"Capas en {gpkg_path.name}: {len(layers)}")
    for i, (name, geom_type) in enumerate(layers, 1):
        click.echo(f"  {i:3d}. {name} ({geom_type})")


@cli.command()
@click.option("--gpkg", default=DEFAULT_GPKG)
@click.option("--layer", required=True)
@click.option("--limit", default=1)
def show_fields(gpkg: str, layer: str, limit: int) -> None:
    """Muestra los campos de una capa."""
    gpkg_path = Path(gpkg)
    if not gpkg_path.exists():
        click.echo(f"[ERROR] No encontrado: {gpkg_path}", err=True)
        sys.exit(1)

    click.echo(f"Leyendo capa: {layer}")
    df = pyogrio.read_dataframe(str(gpkg_path), layer=layer, max_features=limit)
    fields = [c for c in df.columns if c != "geometry"]
    click.echo(f"\nTotal campos: {len(fields)}")
    for i, field in enumerate(fields, 1):
        sample = None
        for val in df[field]:
            if val is not None:
                sample = val
                break
        sample_str = str(sample)[:60] if sample is not None else "NULL"
        click.echo(f"  {i:4d}. {field:40s} | {sample_str}")


@cli.command()
@click.option("--lot", required=True, type=click.Path(exists=True))
@click.option("--gpkg", default=DEFAULT_GPKG)
@click.option("--whitelist", default=str(DEFAULT_WHITELIST))
@click.option("--output", default=str(DEFAULT_OUTPUT))
def query(lot: str, gpkg: str, whitelist: str, output: str) -> None:
    """Consulta catastro para un lote y genera caché JSON consolidado."""

    gpkg_path = Path(gpkg)
    if not gpkg_path.exists():
        click.echo(f"[ERROR] .gpkg no encontrado: {gpkg_path}", err=True)
        sys.exit(1)

    lot_path = Path(lot)
    output_path = Path(output)
    output_path.mkdir(parents=True, exist_ok=True)

    # 1. Cargar whitelist
    wl = load_whitelist(Path(whitelist))
    click.echo(f"[INFO] Whitelist cargada: {sum(len(v) for v in wl.get('_categorized', {}).values())} campos")

    # 2. Cargar lote
    lot_data = load_lot(lot_path)
    predio_id = lot_data["properties"].get("predio_id", lot_path.stem)
    click.echo(f"[INFO] Lote cargado: {predio_id}")
    click.echo(f"[INFO] Área: {lot_data['polygon'].area:.2f} m²")

    # 3. Hash
    gpkg_md5 = file_hash_cached(gpkg_path)
    click.echo(f"[INFO] Hash MD5: {gpkg_md5}")

    # 4. Buscar en capa Lote
    click.echo("")
    click.echo("[1/3] Consultando capa Lote...")
    lot_matches = find_intersecting_features(gpkg_path, "Lote", lot_data["polygon"], max_features=5)

    if not lot_matches:
        click.echo("[ERROR] No se encontró lote que intersecte.", err=True)
        sys.exit(2)

    best_lot = lot_matches[0]
    idx, lot_row, lot_geom, overlap = best_lot
    click.echo(f"[OK] Lote encontrado: idx={idx}, overlap={overlap:.2f} m²")

    # Extraer campos de Lote
    lot_dict = {k: v for k, v in lot_row.items() if k != "geometry"}
    lot_fields = wl.get("_categorized", {}).get("lote_geometria", [])
    lot_data_extracted = extract_fields(lot_dict, lot_fields)

    # Buscar PreChip equivalente en el lote (LotCodigo suele ser el código del lote)
    lot_codigo = lot_dict.get("LotCodigo")
    click.echo(f"[INFO] LotCodigo: {lot_codigo}")

    # 5. Buscar en capa Predio (usando PreCSector + PreCManz + PreCLote que se relacionan con LotCodigo)
    click.echo("")
    click.echo("[2/3] Consultando capa Predio...")

    # El LotCodigo tiene formato como "002407033006" — parte del código catastral
    # Intentamos buscar Predio por Barmanpre o por intersección geométrica
    predio_data_extracted = {}
    try:
        # Intento 1: filtrar por Barmanpre si coincide con parte de LotCodigo
        # LotCodigo = "002407033006", Barmanpre = "006217003012" (formato diferente)
        # Mejor: filtrar por bbox del lote y buscar intersección

        predio_matches = find_intersecting_features(gpkg_path, "Predio", lot_geom, max_features=10)

        if predio_matches:
            # Tomar el que tenga mayor overlap
            best_predio = predio_matches[0]
            p_idx, p_row, p_geom, p_overlap = best_predio
            click.echo(f"[OK] Predio encontrado: idx={p_idx}, overlap={p_overlap:.2f} m²")

            predio_dict = {k: v for k, v in p_row.items() if k != "geometry"}
            predio_fields = (
                wl.get("_categorized", {}).get("predio_identificacion", [])
                + wl.get("_categorized", {}).get("predio_ubicacion", [])
                + wl.get("_categorized", {}).get("predio_areas", [])
                + wl.get("_categorized", {}).get("predio_uso_actual", [])
            )
            predio_data_extracted = extract_fields(predio_dict, predio_fields)
            click.echo(f"[OK] Campos extraídos de Predio: {len(predio_data_extracted)}")
        else:
            click.echo("[WARN] No se encontró Predio que intersecte.", err=True)
    except Exception as e:
        click.echo(f"[WARN] Error consultando Predio: {e}", err=True)

    # 6. Buscar en capa Calificacion (usando PreChip del predio encontrado)
    click.echo("")
    click.echo("[3/3] Consultando capa Calificacion...")

    calif_data_extracted = {}
    pre_chip = predio_data_extracted.get("PreChip")

    if pre_chip:
        try:
            # Filtrar Calificacion por PreChip
            df_calif = pyogrio.read_dataframe(
                str(gpkg_path),
                layer="Calificacion",
                where=f"PreChip = '{pre_chip}'",
            )
            click.echo(f"[INFO] Calificaciones para PreChip={pre_chip}: {len(df_calif)}")

            if len(df_calif) > 0:
                # Si hay múltiples (varias construcciones), tomar la primera
                calif_row = df_calif.iloc[0]
                calif_dict = {k: v for k, v in calif_row.items() if k != "geometry"}

                calif_fields = (
                    wl.get("_categorized", {}).get("calificacion_uso", [])
                    + wl.get("_categorized", {}).get("vecinos_altura_estimada", [])
                )
                calif_data_extracted = extract_fields(calif_dict, calif_fields)
                click.echo(f"[OK] Campos extraídos de Calificacion: {len(calif_data_extracted)}")

                # Calcular altura estimada
                pre_piso = calif_data_extracted.get("PrePiso")
                if pre_piso is not None:
                    try:
                        altura_estimada = float(pre_piso) * 3.0
                        calif_data_extracted["_altura_estimada_m"] = altura_estimada
                        calif_data_extracted["_altura_formula"] = "PrePiso × 3.0"
                        click.echo(f"[OK] Altura estimada: {altura_estimada} m (PrePiso={pre_piso} × 3.0)")
                    except (ValueError, TypeError):
                        pass
            else:
                click.echo(f"[WARN] Sin calificaciones para PreChip={pre_chip}", err=True)
        except Exception as e:
            click.echo(f"[WARN] Error consultando Calificacion: {e}", err=True)
    else:
        click.echo("[WARN] Sin PreChip, no se puede consultar Calificacion.", err=True)

    # 7. Construir JSON consolidado
    output_data = {
        "predio_id": predio_id,
        "consultado_en": datetime.now().isoformat(),
        "crs": {
            "nombre": "MAGNA Ciudad Bogota",
            "codigo": "ESRI:102233",
            "rango_coords": "X~93000-103000, Y~98000-118000"
        },
        "coordenadas": {
            "crs": "ESRI:102233",
            "poligono": lot_data["raw"].get("coordenadas", {}).get("poligono", []),
            "bbox": list(lot_data["polygon"].bounds),
        },
        "catastro": {
            "lote_geometria": lot_data_extracted,
            "predio_identificacion": {k: v for k, v in predio_data_extracted.items()
                                       if k in wl.get("_categorized", {}).get("predio_identificacion", [])},
            "predio_ubicacion": {k: v for k, v in predio_data_extracted.items()
                                  if k in wl.get("_categorized", {}).get("predio_ubicacion", [])},
            "predio_areas": {k: v for k, v in predio_data_extracted.items()
                              if k in wl.get("_categorized", {}).get("predio_areas", [])},
            "predio_uso_actual": {k: v for k, v in predio_data_extracted.items()
                                   if k in wl.get("_categorized", {}).get("predio_uso_actual", [])},
            "calificacion_uso": {k: v for k, v in calif_data_extracted.items()
                                  if k in wl.get("_categorized", {}).get("calificacion_uso", [])},
            "vecinos_altura_estimada": {k: v for k, v in calif_data_extracted.items()
                                         if k in wl.get("_categorized", {}).get("vecinos_altura_estimada", [])},
            "_altura_estimada_m": calif_data_extracted.get("_altura_estimada_m"),
            "_altura_formula": calif_data_extracted.get("_altura_formula"),
        },
        "pot": {
            "_status": "PENDIENTE",
            "_comentario": "El bd_uaecd.gpkg NO contiene POT. Requiere fuente separada (ver ADR-002).",
            "valores_por_defecto": {
                "retiro_frontal_m": 3.0,
                "retiro_posterior_m": 3.0,
                "retiro_lateral_m": 3.0,
                "altura_maxima_m": 12.0,
                "edificabilidad": None,
                "ocupacion_maxima": None,
            }
        },
        "metadatos": {
            "gpkg_path": str(gpkg_path),
            "gpkg_hash_md5": gpkg_md5,
            "layer_lote_idx": str(idx),
            "overlap_area_m2": overlap,
            "campos_extraidos": (
                len(lot_data_extracted)
                + len(predio_data_extracted)
                + len(calif_data_extracted)
            ),
            "campos_totales_whitelist": sum(len(v) for v in wl.get("_categorized", {}).values()),
        },
    }

    # 8. Guardar
    output_file = output_path / f"{predio_id}.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2, default=str)

    click.echo("")
    click.echo("=" * 60)
    click.echo(f"[OK] Caché generado: {output_file}")
    click.echo(f"[OK] Campos extraídos: {output_data['metadatos']['campos_extraidos']}")
    click.echo(f"[OK] Whitelist total: {output_data['metadatos']['campos_totales_whitelist']}")
    click.echo("=" * 60)


if __name__ == "__main__":
    cli()
