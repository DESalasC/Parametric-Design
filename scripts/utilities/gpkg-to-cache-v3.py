#!/usr/bin/env python3
# ==============================================================================
# gpkg-to-cache-v3.py
# ------------------------------------------------------------------------------
# Versión 3: JOIN por atributo entre capas sin geometría.
#
# Mejoras vs v2:
#   - Predio y Calificacion son tablas SIN geometría -> JOIN por atributo
#   - Usa LotCodigo del Lote para buscar Predio relacionado
#   - Usa PreChip del Predio para buscar Calificacion
#   - Maneja correctamente el caso de coords 4D y geometrías inválidas
#   - Caché de hash MD5 para acelerar queries repetidos
#
# Uso:
#   python gpkg-to-cache-v3.py query --lot data/lotes-ejemplo/lote-real-002107015020.json
#   python gpkg-to-cache-v3.py list-layers
#   python gpkg-to-cache-v3.py show-fields --layer Lote --limit 1
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
DEFAULT_GPKG = os.environ.get(
    "POT_GPKG_PATH",
    r"D:\Users\Dario Salas\proyectos\DesParametrico\2-Entradas\Datos_Sitio_GDB\bd_uaecd.gpkg",
)
DEFAULT_WHITELIST = PROJECT_ROOT / "config" / "field-whitelist.json"
DEFAULT_OUTPUT = PROJECT_ROOT / "data" / "pot-cache"
HASH_CACHE_FILE = PROJECT_ROOT / "data" / ".gpkg_hash_cache"


# ---------------------------------------------------------------------------
# Utilidades
# ---------------------------------------------------------------------------
def file_hash_cached(path: Path) -> str:
    """Hash MD5 con caché en disco."""
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
        click.echo(f"[WARN] Whitelist no encontrada: {whitelist_path}", err=True)
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
    """Extrae campos de una fila. Búsqueda case-insensitive."""
    result = {}
    for field_name in fields:
        for k, v in row.items():
            if k.lower() == field_name.lower():
                if hasattr(v, "item"):
                    v = v.item()
                result[field_name] = v
                break
    return result


def find_lote_in_gpkg(gpkg_path: Path, lot_polygon):
    """Encuentra el lote en el .gpkg que intersecta el polígono de búsqueda."""
    bounds = lot_polygon.bounds
    click.echo(f"[INFO] Bounding box: ({bounds[0]:.2f}, {bounds[1]:.2f}, {bounds[2]:.2f}, {bounds[3]:.2f})")

    df = pyogrio.read_dataframe(str(gpkg_path), layer="Lote", bbox=bounds)
    click.echo(f"[INFO] Features cargados (filtrados por bbox): {len(df)}")

    if len(df) == 0:
        click.echo("[WARN] Sin features en bbox. Cargando todo...", err=True)
        df = pyogrio.read_dataframe(str(gpkg_path), layer="Lote")

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

    if invalid_count > 0:
        click.echo(f"[INFO] Geometrías reparadas: {invalid_count} de {checked}")

    matches.sort(key=lambda x: x[3], reverse=True)
    return matches


def find_predio_by_lot_codigo(gpkg_path: Path, lot_codigo: str) -> dict[str, Any] | None:
    """Busca en la capa Predio (sin geometría) por atributo.
    
    Predio tiene Barmanpre con formato similar a LotCodigo.
    Intenta varios campos: Barmanpre, PreCedCata, PreNupre.
    """
    if not lot_codigo:
        return None

    click.echo(f"[INFO] Buscando Predio con LotCodigo={lot_codigo}...")

    # Intentar varios campos donde podría estar el código del lote
    campos_intentar = ["Barmanpre", "PreCedCata", "PreNupre", "PreChip"]

    for campo in campos_intentar:
        try:
            df = pyogrio.read_dataframe(
                str(gpkg_path),
                layer="Predio",
                where=f"{campo} = '{lot_codigo}'",
                max_features=1,
            )
            if len(df) > 0:
                row = df.iloc[0]
                predio_dict = {k: v for k, v in row.items() if k != "geometry"}
                click.echo(f"[OK] Predio encontrado por {campo}={lot_codigo}")
                click.echo(f"     PreChip: {predio_dict.get('PreChip')}")
                click.echo(f"     PreDirecc: {predio_dict.get('PreDirecc')}")
                return predio_dict
        except Exception as e:
            click.echo(f"[WARN] Búsqueda por {campo} falló: {e}", err=True)
            continue

    # Si no encuentra por código exacto, intentar por coincidencia parcial
    # LotCodigo = "002107015020", Barmanpre podría tener partes similares
    click.echo(f"[INFO] Búsqueda exacta falló. Intentando por coincidencia parcial...")

    # Extraer partes del código: sector (3) + manzana (3) + lote (3)
    if len(lot_codigo) >= 9:
        sector_manzana = lot_codigo[:9]  # ej: "002107015"
        try:
            df = pyogrio.read_dataframe(
                str(gpkg_path),
                layer="Predio",
                where=f"Barmanpre LIKE '{sector_manzana}%'",
                max_features=10,
            )
            if len(df) > 0:
                click.echo(f"[OK] {len(df)} predios encontrados por Barmanpre LIKE '{sector_manzana}%'")
                row = df.iloc[0]  # Tomar el primero
                predio_dict = {k: v for k, v in row.items() if k != "geometry"}
                click.echo(f"     PreChip: {predio_dict.get('PreChip')}")
                click.echo(f"     PreDirecc: {predio_dict.get('PreDirecc')}")
                return predio_dict
        except Exception as e:
            click.echo(f"[WARN] Búsqueda parcial falló: {e}", err=True)

    click.echo(f"[WARN] No se encontró Predio para LotCodigo={lot_codigo}", err=True)
    return None


def find_calificacion_by_pre_chip(gpkg_path: Path, pre_chip: str) -> dict[str, Any] | None:
    """Busca en la capa Calificacion (sin geometría) por PreChip."""
    if not pre_chip:
        return None

    click.echo(f"[INFO] Buscando Calificacion con PreChip={pre_chip}...")

    try:
        df = pyogrio.read_dataframe(
            str(gpkg_path),
            layer="Calificacion",
            where=f"PreChip = '{pre_chip}'",
            max_features=5,
        )
    except Exception as e:
        click.echo(f"[WARN] Error consultando Calificacion: {e}", err=True)
        return None

    if len(df) == 0:
        click.echo(f"[WARN] Sin calificaciones para PreChip={pre_chip}", err=True)
        return None

    click.echo(f"[OK] {len(df)} calificaciones encontradas")

    # Si hay múltiples, tomar la primera (o la de mayor PreAreaUso)
    row = df.iloc[0]
    calif_dict = {k: v for k, v in row.items() if k != "geometry"}

    click.echo(f"     PreUso: {calif_dict.get('PreUso')}")
    click.echo(f"     PreUCalif: {calif_dict.get('PreUCalif')}")
    click.echo(f"     PrePiso: {calif_dict.get('PrePiso')}")

    return calif_dict


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
@click.group()
def cli() -> None:
    """Utilidad para consultar el .gpkg de Catastro de Bogotá."""
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
        click.echo(f"  {i:3d}. {name} ({geom_type or 'sin geometría'})")


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
    """Consulta catastro y genera caché JSON consolidado con JOIN por atributo."""

    gpkg_path = Path(gpkg)
    if not gpkg_path.exists():
        click.echo(f"[ERROR] .gpkg no encontrado: {gpkg_path}", err=True)
        sys.exit(1)

    lot_path = Path(lot)
    output_path = Path(output)
    output_path.mkdir(parents=True, exist_ok=True)

    # 1. Whitelist
    wl = load_whitelist(Path(whitelist))
    total_wl = sum(len(v) for v in wl.get("_categorized", {}).values())
    click.echo(f"[INFO] Whitelist cargada: {total_wl} campos")

    # 2. Lote
    lot_data = load_lot(lot_path)
    predio_id = lot_data["properties"].get("predio_id", lot_path.stem)
    click.echo(f"[INFO] Lote cargado: {predio_id}")
    click.echo(f"[INFO] Área del lote de entrada: {lot_data['polygon'].area:.2f} m²")

    # 3. Hash
    gpkg_md5 = file_hash_cached(gpkg_path)
    click.echo(f"[INFO] Hash MD5: {gpkg_md5}")

    # 4. Buscar en Lote (con geometría)
    click.echo("")
    click.echo("[1/3] Consultando capa Lote (JOIN espacial)...")
    lot_matches = find_lote_in_gpkg(gpkg_path, lot_data["polygon"])

    if not lot_matches:
        click.echo("[ERROR] No se encontró lote que intersecte.", err=True)
        sys.exit(2)

    best_lot = lot_matches[0]
    idx, lot_row, lot_geom, overlap = best_lot
    click.echo(f"[OK] Lote encontrado: idx={idx}, overlap={overlap:.2f} m²")

    lot_dict = {k: v for k, v in lot_row.items() if k != "geometry"}
    lot_codigo = lot_dict.get("LotCodigo")
    click.echo(f"[OK] LotCodigo: {lot_codigo}")

    # Extraer campos de Lote
    lot_fields = wl.get("_categorized", {}).get("lote_geometria", [])
    lot_data_extracted = extract_fields(lot_dict, lot_fields)

    # 5. Buscar en Predio (sin geometría, JOIN por atributo)
    click.echo("")
    click.echo("[2/3] Consultando capa Predio (JOIN por atributo)...")
    predio_dict = find_predio_by_lot_codigo(gpkg_path, lot_codigo)

    predio_identificacion = {}
    predio_ubicacion = {}
    predio_areas = {}
    predio_uso_actual = {}
    pre_chip = None

    if predio_dict:
        pre_chip = predio_dict.get("PreChip")

        predio_identificacion = extract_fields(
            predio_dict,
            wl.get("_categorized", {}).get("predio_identificacion", [])
        )
        predio_ubicacion = extract_fields(
            predio_dict,
            wl.get("_categorized", {}).get("predio_ubicacion", [])
        )
        predio_areas = extract_fields(
            predio_dict,
            wl.get("_categorized", {}).get("predio_areas", [])
        )
        predio_uso_actual = extract_fields(
            predio_dict,
            wl.get("_categorized", {}).get("predio_uso_actual", [])
        )

        click.echo(f"[OK] Campos extraídos de Predio: "
                   f"{len(predio_identificacion) + len(predio_ubicacion) + len(predio_areas) + len(predio_uso_actual)}")
    else:
        click.echo("[WARN] No se pudo recuperar información de Predio.", err=True)

    # 6. Buscar en Calificacion (sin geometría, JOIN por PreChip)
    click.echo("")
    click.echo("[3/3] Consultando capa Calificacion (JOIN por PreChip)...")
    calif_dict = find_calificacion_by_pre_chip(gpkg_path, pre_chip) if pre_chip else None

    calif_uso = {}
    vecinos_altura = {}
    altura_estimada_m = None
    altura_formula = None

    if calif_dict:
        calif_uso = extract_fields(
            calif_dict,
            wl.get("_categorized", {}).get("calificacion_uso", [])
        )
        vecinos_altura = extract_fields(
            calif_dict,
            wl.get("_categorized", {}).get("vecinos_altura_estimada", [])
        )

        # Calcular altura estimada
        pre_piso = calif_dict.get("PrePiso")
        if pre_piso is not None:
            try:
                altura_estimada_m = float(pre_piso) * 3.0
                altura_formula = "PrePiso × 3.0"
                click.echo(f"[OK] Altura estimada: {altura_estimada_m} m (PrePiso={pre_piso} × 3.0)")
            except (ValueError, TypeError):
                pass

        click.echo(f"[OK] Campos extraídos de Calificacion: {len(calif_uso) + len(vecinos_altura)}")
    else:
        click.echo("[WARN] No se pudo recuperar información de Calificacion.", err=True)

    # 7. Construir JSON consolidado
    total_extraidos = (
        len(lot_data_extracted)
        + len(predio_identificacion)
        + len(predio_ubicacion)
        + len(predio_areas)
        + len(predio_uso_actual)
        + len(calif_uso)
        + len(vecinos_altura)
    )

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
            "lot_codigo": lot_codigo,
            "pre_chip": pre_chip,
            "campos_extraidos": total_extraidos,
            "campos_totales_whitelist": total_wl,
            "joins_realizados": {
                "lote_espacial": True,
                "predio_atributo": predio_dict is not None,
                "calificacion_atributo": calif_dict is not None,
            }
        },
    }

    # 8. Guardar
    output_file = output_path / f"{predio_id}.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2, default=str)

    click.echo("")
    click.echo("=" * 60)
    click.echo(f"[OK] Caché generado: {output_file}")
    click.echo(f"[OK] Campos extraídos: {total_extraidos} de {total_wl} en whitelist")
    click.echo(f"[OK] JOIN Lote: OK (idx={idx})")
    click.echo(f"[OK] JOIN Predio: {'OK' if predio_dict else 'FALLÓ'}")
    click.echo(f"[OK] JOIN Calificacion: {'OK' if calif_dict else 'FALLÓ'}")
    click.echo("=" * 60)


if __name__ == "__main__":
    cli()
