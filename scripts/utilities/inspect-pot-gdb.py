#!/usr/bin/env python3
# ==============================================================================
# inspect-pot-gdb.py
# ------------------------------------------------------------------------------
# Inspecciona la geodatabase del POT (Decreto 555/2021) y exporta un inventario
# completo de capas y campos para su integración.
#
# Uso:
#   python scripts/utilities/inspect-pot-gdb.py
#   python scripts/utilities/inspect-pot-gdb.py --layer "NombreCapa" --limit 5
# ==============================================================================

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

import click

try:
    import pyogrio
except ImportError as e:
    click.echo(f"[ERROR] pyogrio no instalado: {e}", err=True)
    sys.exit(1)


PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

# Carpeta .gdb (ESRI File Geodatabase)
DEFAULT_POT_GDB = r"D:\Users\Dario Salas\proyectos\DesParametrico\2-Entradas\Datos_Sitio_GDB\POT\POT_Decreto_555_2021_Bogota_D_C.gdb"


@click.group()
def cli() -> None:
    """Inspecciona la geodatabase del POT de Bogotá."""
    pass


@cli.command()
@click.option("--gdb", default=DEFAULT_POT_GDB, help="Ruta a la carpeta .gdb")
def list_layers(gdb: str) -> None:
    """Lista las capas de la geodatabase POT."""

    gdb_path = Path(gdb)
    if not gdb_path.exists():
        click.echo(f"[ERROR] No encontrado: {gdb_path}", err=True)
        sys.exit(1)

    if not gdb_path.is_dir():
        click.echo(f"[ERROR] Debe ser una carpeta .gdb, no un archivo: {gdb_path}", err=True)
        sys.exit(1)

    click.echo(f"[INFO] Inspeccionando: {gdb_path}")
    click.echo(f"[INFO] Tamaño carpeta: {sum(f.stat().st_size for f in gdb_path.rglob('*') if f.is_file()) / (1024*1024):.1f} MB")
    click.echo("")

    try:
        layers = pyogrio.list_layers(str(gdb_path))
        click.echo(f"Capas encontradas: {len(layers)}")
        click.echo("")
        click.echo(f"{'#':>3}  {'Nombre':50s}  {'Geometría':15s}")
        click.echo("-" * 75)
        for i, (name, geom_type) in enumerate(layers, 1):
            geom_str = str(geom_type) if geom_type else "tabla (sin geom)"
            click.echo(f"{i:>3}  {str(name):50s}  {geom_str:15s}")

        # Guardar lista en JSON para referencia
        output_path = PROJECT_ROOT / "data" / "pot_layers_inventory.json"
        output_path.parent.mkdir(parents=True, exist_ok=True)

        layers_data = [
            {"index": i, "name": str(name), "geom_type": str(geom_type) if geom_type else None}
            for i, (name, geom_type) in enumerate(layers, 1)
        ]
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(layers_data, f, ensure_ascii=False, indent=2)

        click.echo("")
        click.echo(f"[OK] Lista guardada en: {output_path}")

    except Exception as e:
        click.echo(f"[ERROR] No se pudo leer la geodatabase: {e}", err=True)
        sys.exit(2)


@cli.command()
@click.option("--gdb", default=DEFAULT_POT_GDB)
@click.option("--layer", required=True, help="Nombre de la capa")
@click.option("--limit", default=1, help="Número de features a inspeccionar")
def show_fields(gdb: str, layer: str, limit: int) -> None:
    """Muestra los campos de una capa del POT."""

    gdb_path = Path(gdb)
    if not gdb_path.exists():
        click.echo(f"[ERROR] No encontrado: {gdb_path}", err=True)
        sys.exit(1)

    click.echo(f"[INFO] Capa: {layer}")
    click.echo(f"[INFO] Cargando {limit} feature(s)...")

    try:
        df = pyogrio.read_dataframe(str(gdb_path), layer=layer, max_features=limit)
    except Exception as e:
        click.echo(f"[ERROR] No se pudo leer la capa: {e}", err=True)
        sys.exit(2)

    if len(df) == 0:
        click.echo("[WARN] Capa vacía o sin features en el límite especificado.", err=True)
        return

    fields = [c for c in df.columns if c != "geometry"]
    click.echo("")
    click.echo(f"Total campos: {len(fields)}")
    click.echo("")
    click.echo(f"{'#':>4}  {'Campo':45s}  {'Tipo':15s}  {'Ejemplo':40s}")
    click.echo("-" * 110)

    for i, field in enumerate(fields, 1):
        sample = None
        for val in df[field]:
            if val is not None:
                sample = val
                break
        sample_str = str(sample)[:40] if sample is not None else "NULL"
        dtype = str(df[field].dtype)
        click.echo(f"{i:>4}  {field:45s}  {dtype:15s}  {sample_str:40s}")

    # Mostrar info de la geometría
    if "geometry" in df.columns:
        geom_sample = df.geometry.iloc[0]
        if geom_sample is not None:
            click.echo("")
            click.echo(f"Geometría: {geom_sample.geom_type}")
            click.echo(f"Bounds: {list(geom_sample.bounds)}")
            click.echo(f"CRS: {df.crs}")


@cli.command()
@click.option("--gdb", default=DEFAULT_POT_GDB)
@click.option("--output", default=str(PROJECT_ROOT / "data" / "pot_fields_inventory.json"))
def export_all_fields(gdb: str, output: str) -> None:
    """Exporta TODOS los campos de TODAS las capas a un JSON."""

    gdb_path = Path(gdb)
    if not gdb_path.exists():
        click.echo(f"[ERROR] No encontrado: {gdb_path}", err=True)
        sys.exit(1)

    click.echo(f"[INFO] Exportando inventario completo...")

    layers = pyogrio.list_layers(str(gdb_path))
    inventory = {}

    for layer_name, geom_type in layers:
        layer_name_str = str(layer_name)
        click.echo(f"  Inspeccionando: {layer_name_str} ({geom_type})")

        try:
            df = pyogrio.read_dataframe(str(gdb_path), layer=layer_name_str, max_features=1)

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
                    "name": str(col),
                    "dtype": str(df[col].dtype),
                    "sample": str(sample)[:100] if sample is not None else None,
                })

            inventory[layer_name_str] = {
                "geom_type": str(geom_type) if geom_type else None,
                "crs": str(df.crs) if df.crs is not None else None,
                "feature_count_sample": len(df),
                "field_count": len(fields),
                "fields": fields,
            }
        except Exception as e:
            click.echo(f"    [WARN] Error: {e}", err=True)
            inventory[layer_name_str] = {"error": str(e)}

    output_path = Path(output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(inventory, f, ensure_ascii=False, indent=2, default=str)

    total_fields = sum(r.get("field_count", 0) for r in inventory.values())
    click.echo("")
    click.echo(f"[OK] Inventario exportado: {output_path}")
    click.echo(f"[OK] Capas: {len(inventory)}")
    click.echo(f"[OK] Campos totales: {total_fields}")


@cli.command()
@click.option("--gdb", default=DEFAULT_POT_GDB)
@click.option("--layer", required=True)
@click.option("--limit", default=3)
def show_features(gdb: str, layer: str, limit: int) -> None:
    """Muestra N features completos de una capa."""

    gdb_path = Path(gdb)
    if not gdb_path.exists():
        click.echo(f"[ERROR] No encontrado: {gdb_path}", err=True)
        sys.exit(1)

    try:
        df = pyogrio.read_dataframe(str(gdb_path), layer=layer, max_features=limit)
    except Exception as e:
        click.echo(f"[ERROR] No se pudo leer: {e}", err=True)
        sys.exit(2)

    click.echo(f"[INFO] {len(df)} features cargados de capa {layer}")
    click.echo("")

    for idx, row in df.iterrows():
        click.echo(f"--- Feature {idx} ---")
        for col in df.columns:
            if col == "geometry":
                geom = row[col]
                if geom is not None:
                    click.echo(f"  geometry: {geom.geom_type}, bounds={list(geom.bounds)}")
            else:
                val = row[col]
                if hasattr(val, "item"):
                    val = val.item()
                click.echo(f"  {col}: {val}")
        click.echo("")


if __name__ == "__main__":
    cli()
