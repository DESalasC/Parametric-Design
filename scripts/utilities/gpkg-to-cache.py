#!/usr/bin/env python3
# ==============================================================================
# gpkg-to-cache.py
# ------------------------------------------------------------------------------
# Lee el archivo bd_uaecd.gpkg de la geobase de Bogotá y genera un caché JSON
# por predio, extrayendo solo los campos relevantes (definidos en
# config/field-whitelist.json).
#
# Uso:
#   python gpkg-to-cache.py --lot data/lotes-ejemplo/lote-chapinero.json
#   python gpkg-to-cache.py --lot lote.geojson --output data/pot-cache/
#   python gpkg-to-cache.py --list-layers
#   python gpkg-to-cache.py --show-fields layer_name
#
# Requisitos:
#   pip install pyogrio shapely click rich pyproj
#
# Salida:
#   data/pot-cache/<predio-id>.json
#
# Estructura del JSON de salida:
#   {
#     "predio_id": "...",
#     "consultado_en": "2026-08-01T12:00:00",
#     "coordenadas": {...},
#     "pot": {
#       "identificacion": {...},
#       "normativa_pot": {...},
#       "alturas": {...},
#       "retiros": {...},
#       "suelo": {...},
#       "vias": {...}
#     },
#     "metadatos": {
#       "gpkg_hash": "...",
#       "campos_extraidos": 30,
#       "campos_totales": 2455
#     }
#   }
# ==============================================================================

from __future__ import annotations

import hashlib
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

import click

try:
    import pyogrio
    from shapely.geometry import shape, mapping
    from shapely.ops import transform
    from pyproj import Transformer
except ImportError as e:
    click.echo(f"[ERROR] Dependencias faltantes: {e}", err=True)
    click.echo("Instala con: pip install pyogrio shapely click rich pyproj", err=True)
    sys.exit(1)


# ---------------------------------------------------------------------------
# Configuración por defecto
# ---------------------------------------------------------------------------
DEFAULT_GPKG = r"D:\Users\Dario Salas\proyectos\DesParametrico\2-Entradas\Datos_Sitio_GDB\bd_uaecd.gpkg"
DEFAULT_WHITELIST = Path(__file__).parent.parent.parent / "config" / "field-whitelist.json"
DEFAULT_OUTPUT = Path(__file__).parent.parent.parent / "data" / "pot-cache"

# CRS
CRS_MAGNA_BOGOTA = "EPSG:9377"  # MAGNA-SIRGAS Origen Bogotá
CRS_WGS84 = "EPSG:4326"


# ---------------------------------------------------------------------------
# Utilidades
# ---------------------------------------------------------------------------
def file_hash(path: Path) -> str:
    """Calcula hash MD5 del archivo .gpkg para detectar cambios."""
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def load_whitelist(whitelist_path: Path) -> dict[str, list[str]]:
    """Carga la whitelist de campos relevantes."""
    if not whitelist_path.exists():
        click.echo(f"[WARN] Whitelist no encontrada: {whitelist_path}", err=True)
        click.echo("[WARN] Se extraerán TODOS los campos (puede ser lento).", err=True)
        return {}

    with open(whitelist_path, encoding="utf-8") as f:
        data = json.load(f)

    campos = data.get("campos", {})
    # Aplanar a una lista de campos relevantes
    flat = []
    for categoria, fields in campos.items():
        if isinstance(fields, list):
            flat.extend(fields)
    return {"_flat": flat, "_categorized": campos}


def load_lot(lot_path: Path) -> dict[str, Any]:
    """Carga el lote desde un GeoJSON o JSON interno."""
    with open(lot_path, encoding="utf-8") as f:
        data = json.load(f)

    # Si es GeoJSON Feature
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
        # Formato interno del proyecto
        coords = data["coordenadas"]["poligono"]
        geometry = {"type": "Polygon", "coordinates": [coords]}
        properties = {"predio_id": data.get("predio_id", "unknown")}
        properties.update(data.get("metadata", {}))
    else:
        raise ValueError(f"Formato de lote no reconocido: {lot_path}")

    polygon = shape(geometry)
    return {"polygon": polygon, "properties": properties, "raw": data}


def find_layer(gpkg_path: Path) -> str:
    """Encuentra la capa de predios en el .gpkg."""
    layers = pyogrio.list_layers(str(gpkg_path))
    click.echo(f"[INFO] Capas disponibles en .gpkg: {len(layers)}")
    for layer in layers:
        click.echo(f"  - {layer[0]} ({layer[1]})")

    # Buscar capa de predios por nombre común
    predio_keywords = ["predio", "predial", "catastro", "lote", "manzana"]
    for layer_name, _ in layers:
        name_lower = layer_name.lower()
        if any(kw in name_lower for kw in predio_keywords):
            click.echo(f"[INFO] Usando capa: {layer_name}")
            return layer_name

    # Si no encuentra, usar la primera
    if layers:
        layer_name = layers[0][0]
        click.echo(f"[WARN] No se encontró capa de predios por nombre. Usando: {layer_name}", err=True)
        return layer_name

    raise ValueError("No hay capas en el .gpkg")


def extract_fields(
    row: dict[str, Any],
    whitelist: dict[str, list[str]],
) -> dict[str, dict[str, Any]]:
    """Extrae campos de la fila según la whitelist categorizada."""
    result: dict[str, dict[str, Any]] = {}
    categorias = whitelist.get("_categorized", {})

    for categoria, fields in categorias.items():
        result[categoria] = {}
        for field_name in fields:
            # Búsqueda case-insensitive
            for k, v in row.items():
                if k.lower() == field_name.lower():
                    result[categoria][field_name] = v
                    break

    return result


# ---------------------------------------------------------------------------
# Comandos CLI
# ---------------------------------------------------------------------------
@click.group()
def cli() -> None:
    """Utilidad para consultar el .gpkg de POT de Bogotá."""
    pass


@cli.command()
@click.option("--gpkg", default=DEFAULT_GPKG, help="Ruta al archivo .gpkg")
def list_layers(gpkg: str) -> None:
    """Lista las capas disponibles en el .gpkg."""
    gpkg_path = Path(gpkg)
    if not gpkg_path.exists():
        click.echo(f"[ERROR] No encontrado: {gpkg_path}", err=True)
        sys.exit(1)

    layers = pyogrio.list_layers(str(gpkg_path))
    click.echo(f"Capas en {gpkg_path.name}: {len(layers)}")
    for i, (name, geom_type) in enumerate(layers, 1):
        click.echo(f"  {i:3d}. {name} ({geom_type})")


@cli.command()
@click.option("--gpkg", default=DEFAULT_GPKG, help="Ruta al archivo .gpkg")
@click.option("--layer", required=True, help="Nombre de la capa")
@click.option("--limit", default=10, help="Número de features a inspeccionar")
def show_fields(gpkg: str, layer: str, limit: int) -> None:
    """Muestra los campos de una capa (útil para ajustar la whitelist)."""
    gpkg_path = Path(gpkg)
    if not gpkg_path.exists():
        click.echo(f"[ERROR] No encontrado: {gpkg_path}", err=True)
        sys.exit(1)

    click.echo(f"Leyendo metadatos de capa: {layer}")
    df = pyogrio.read_dataframe(str(gpkg_path), layer=layer, max_features=limit)

    fields = list(df.columns)
    click.echo(f"\nTotal de campos: {len(fields)}")
    click.echo("\nCampos:")
    for i, field in enumerate(fields, 1):
        # Mostrar tipo de dato del primer valor no nulo
        sample = None
        for val in df[field]:
            if val is not None:
                sample = val
                break
        sample_str = str(sample)[:50] if sample is not None else "NULL"
        click.echo(f"  {i:4d}. {field:50s} | ejemplo: {sample_str}")

    # Sugerir exportar a CSV
    click.echo(f"\nPara exportar todos los campos a CSV:")
    click.echo(f"  python -c \"import pyogrio; df = pyogrio.read_dataframe('{gpkg}', layer='{layer}', max_features=1); df.head(0).to_csv('fields_report.csv', index=False)\"")


@cli.command()
@click.option(
    "--lot",
    required=True,
    type=click.Path(exists=True),
    help="Ruta al archivo del lote (GeoJSON o JSON interno)",
)
@click.option("--gpkg", default=DEFAULT_GPKG, help="Ruta al archivo .gpkg")
@click.option(
    "--whitelist",
    default=str(DEFAULT_WHITELIST),
    help="Ruta al archivo field-whitelist.json",
)
@click.option(
    "--output",
    default=str(DEFAULT_OUTPUT),
    help="Carpeta de salida para el caché JSON",
)
@click.option("--layer", default=None, help="Capa del .gpkg (auto-detectar si no se especifica)")
def query(lot: str, gpkg: str, whitelist: str, output: str, layer: str | None) -> None:
    """Consulta el POT para un lote específico y genera el caché JSON."""
    gpkg_path = Path(gpkg)
    if not gpkg_path.exists():
        click.echo(f"[ERROR] .gpkg no encontrado: {gpkg_path}", err=True)
        sys.exit(1)

    lot_path = Path(lot)
    output_path = Path(output)
    output_path.mkdir(parents=True, exist_ok=True)

    # 1. Cargar whitelist
    wl = load_whitelist(Path(whitelist))
    click.echo(f"[INFO] Whitelist cargada: {len(wl.get('_flat', []))} campos")

    # 2. Cargar lote
    lot_data = load_lot(lot_path)
    predio_id = lot_data["properties"].get("predio_id", lot_path.stem)
    click.echo(f"[INFO] Lote cargado: {predio_id}")
    click.echo(f"[INFO] Área aproximada: {lot_data['polygon'].area:.2f} m² (en CRS del lote)")

    # 3. Hash del .gpkg
    click.echo(f"[INFO] Calculando hash del .gpkg (puede tardar)...")
    gpkg_md5 = file_hash(gpkg_path)
    click.echo(f"[INFO] Hash MD5: {gpkg_md5}")

    # 4. Detectar capa
    if layer is None:
        layer_name = find_layer(gpkg_path)
    else:
        layer_name = layer

    # 5. Leer el .gpkg filtrando por bounding box del lote (más rápido)
    bounds = lot_data["polygon"].bounds  # (minx, miny, maxx, maxy)
    click.echo(f"[INFO] Bounding box: {bounds}")
    click.echo(f"[INFO] Leyendo capa {layer_name} (esto puede tardar)...")

    df = pyogrio.read_dataframe(
        str(gpkg_path),
        layer=layer_name,
        bbox=bounds,
    )

    if len(df) == 0:
        click.echo("[WARN] No se encontraron predios en el bbox. Probando sin filtro...", err=True)
        df = pyogrio.read_dataframe(str(gpkg_path), layer=layer_name)

    click.echo(f"[INFO] Features cargados: {len(df)}")

    # 6. Encontrar el predio que contiene o intersecta el lote
    from shapely.geometry import Polygon

    matched = None
    for idx, row in df.iterrows():
        geom = row.geometry
        if geom is None:
            continue
        # Intersección
        if geom.intersects(lot_data["polygon"]):
            matched = (idx, row)
            overlap_area = geom.intersection(lot_data["polygon"]).area
            click.echo(
                f"[INFO] Predio encontrado: idx={idx}, "
                f"overlap={overlap_area:.2f} m²"
            )
            break

    if matched is None:
        click.echo("[ERROR] No se encontró predio que intersecte el lote.", err=True)
        click.echo("[ERROR] Verifica el CRS del lote (debe ser MAGNA-SIRGAS Origen Bogotá).", err=True)
        sys.exit(2)

    idx, row = matched

    # 7. Extraer campos según whitelist
    row_dict = {k: v for k, v in row.items() if k != "geometry"}
    pot_data = extract_fields(row_dict, wl)

    # 8. Construir JSON de salida
    output_data = {
        "predio_id": predio_id,
        "consultado_en": datetime.now().isoformat(),
        "coordenadas": {
            "crs": CRS_MAGNA_BOGOTA,
            "poligono": lot_data["raw"].get("coordenadas", {}).get("poligono", []),
        },
        "pot": pot_data,
        "metadatos": {
            "gpkg_path": str(gpkg_path),
            "gpkg_hash_md5": gpkg_md5,
            "layer": layer_name,
            "feature_id": str(idx),
            "campos_extraidos": sum(len(v) for v in pot_data.values()),
            "campos_totales_en_predio": len(row_dict),
        },
    }

    # 9. Guardar
    output_file = output_path / f"{predio_id}.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2, default=str)

    click.echo(f"\n[OK] Caché generado: {output_file}")
    click.echo(f"[OK] Campos extraídos: {output_data['metadatos']['campos_extraidos']}")
    click.echo(f"[OK] Campos totales en predio: {output_data['metadatos']['campos_totales_en_predio']}")


@cli.command()
@click.option("--gpkg", default=DEFAULT_GPKG, help="Ruta al archivo .gpkg")
@click.option(
    "--output",
    default="gdb_layer_fields_report.json",
    help="Archivo de salida",
)
def export_fields(gpkg: str, output: str) -> None:
    """Exporta todos los campos de todas las capas a un JSON (para inspección)."""
    gpkg_path = Path(gpkg)
    if not gpkg_path.exists():
        click.echo(f"[ERROR] No encontrado: {gpkg_path}", err=True)
        sys.exit(1)

    layers = pyogrio.list_layers(str(gpkg_path))
    result = {}

    for layer_name, geom_type in layers:
        click.echo(f"[INFO] Inspeccionando: {layer_name}")
        try:
            df = pyogrio.read_dataframe(str(gpkg_path), layer=layer_name, max_features=1)
            fields = []
            for col in df.columns:
                if col == "geometry":
                    continue
                sample = None
                for val in df[col]:
                    if val is not None:
                        sample = val
                        break
                fields.append({
                    "name": col,
                    "dtype": str(df[col].dtype),
                    "sample": str(sample)[:100] if sample is not None else None,
                })
            result[layer_name] = {
                "geom_type": geom_type,
                "field_count": len(fields),
                "fields": fields,
            }
        except Exception as e:
            click.echo(f"[WARN] Error leyendo {layer_name}: {e}", err=True)
            result[layer_name] = {"error": str(e)}

    with open(output, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2, default=str)

    total_fields = sum(r.get("field_count", 0) for r in result.values())
    click.echo(f"\n[OK] Exportado: {output}")
    click.echo(f"[OK] Capas: {len(result)}")
    click.echo(f"[OK] Campos totales: {total_fields}")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    cli()
