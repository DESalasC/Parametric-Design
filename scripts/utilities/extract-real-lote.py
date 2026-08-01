#!/usr/bin/env python3
# ==============================================================================
# extract-real-lote.py
# ------------------------------------------------------------------------------
# Extrae un lote REAL del .gpkg con sus coordenadas correctas (puntos, no bbox)
# y genera un archivo lote-real-XXX.json listo para usar con gpkg-to-cache.py.
#
# Soluciona el problema donde el usuario copió bounding boxes como si fueran
# puntos del polígono.
#
# Uso:
#   python scripts/utilities/extract-real-lote.py
#   python scripts/utilities/extract-real-lote.py --index 100
#   python scripts/utilities/extract-real-lote.py --lot-codigo 002107015020
# ==============================================================================

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

import click

try:
    import pyogrio
    from shapely.geometry import mapping
    from shapely.validation import make_valid
except ImportError as e:
    click.echo(f"[ERROR] Dependencias faltantes: {e}", err=True)
    sys.exit(1)


PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
DEFAULT_GPKG = os.environ.get(
    "POT_GPKG_PATH",
    r"D:\Users\Dario Salas\proyectos\DesParametrico\2-Entradas\Datos_Sitio_GDB\bd_uaecd.gpkg",
)


def repair_geom(geom):
    """Repara geometría inválida."""
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


@click.command()
@click.option("--gpkg", default=DEFAULT_GPKG, help="Ruta al .gpkg")
@click.option("--index", default=0, type=int, help="Índice del lote a extraer (0=primero)")
@click.option("--lot-codigo", default=None, help="Buscar por LotCodigo específico")
@click.option("--output-dir", default=str(PROJECT_ROOT / "data" / "lotes-ejemplo"))
def main(gpkg: str, index: int, lot_codigo: str | None, output_dir: str) -> None:
    """Extrae un lote real del .gpkg con coords correctas."""

    gpkg_path = Path(gpkg)
    if not gpkg_path.exists():
        click.echo(f"[ERROR] .gpkg no encontrado: {gpkg_path}", err=True)
        sys.exit(1)

    click.echo(f"[INFO] .gpkg: {gpkg_path.name} ({gpkg_path.stat().st_size / (1024*1024):.1f} MB)")

    # 1. Buscar lote
    click.echo("")
    click.echo("[1] Buscando lote...")

    if lot_codigo:
        click.echo(f"    Filtrando por LotCodigo={lot_codigo}...")
        df = pyogrio.read_dataframe(
            str(gpkg_path),
            layer="Lote",
            where=f"LotCodigo = '{lot_codigo}'",
        )
    else:
        click.echo(f"    Cargando lote en índice {index}...")
        # Skip hasta el índice deseado
        df = pyogrio.read_dataframe(
            str(gpkg_path),
            layer="Lote",
            skip_features=index,
            max_features=1,
        )

    if len(df) == 0:
        click.echo(f"[ERROR] No se encontró lote", err=True)
        sys.exit(2)

    row = df.iloc[0]
    geom = row.geometry

    click.echo(f"    [OK] Lote encontrado:")
    click.echo(f"    - LotCodigo: {row.LotCodigo}")
    click.echo(f"    - LotCodMzn: {row.LotCodMzn}")
    click.echo(f"    - LotTipo: {row.LotTipo} ({row.d_LotTipo})")
    click.echo(f"    - SHAPE_Area: {row.SHAPE_Area:.2f} m²")
    click.echo(f"    - Geometría tipo: {geom.geom_type}")
    click.echo(f"    - Geometría válida: {geom.is_valid}")

    # 2. Reparar geometría si es inválida
    if not geom.is_valid:
        click.echo("    [WARN] Geometría inválida. Reparando...", err=True)
        geom = repair_geom(geom)
        if geom is None:
            click.echo("    [ERROR] No se pudo reparar la geometría", err=True)
            sys.exit(2)
        click.echo(f"    [OK] Geometría reparada. Nueva área: {geom.area:.2f} m²")

    # 3. Extraer coordenadas REALES del polígono (no bounding box)
    click.echo("")
    click.echo("[2] Extrayendo coordenadas reales...")

    geom_map = mapping(geom)
    # Truncar a 2D si es 3D
    coords_2d = []
    for ring in geom_map["coordinates"]:
        ring_2d = []
        for point in ring:
            if isinstance(point, (list, tuple)):
                ring_2d.append([float(point[0]), float(point[1])])  # Solo X, Y
            else:
                ring_2d.append([float(point)])
        coords_2d.append(ring_2d)

    click.echo(f"    [OK] Puntos en el polígono: {len(coords_2d[0])}")
    click.echo(f"    [OK] Primer punto: {coords_2d[0][0]}")
    click.echo(f"    [OK] Último punto: {coords_2d[0][-1]} (debe ser igual al primero para cerrar)")
    click.echo(f"    [OK] Bounds: {list(geom.bounds)}")
    click.echo(f"    [OK] Área: {geom.area:.2f} m²")

    # 4. Generar archivo lote-real-XXX.json
    output_dir_path = Path(output_dir)
    output_dir_path.mkdir(parents=True, exist_ok=True)

    predio_id = f"REAL-{row.LotCodigo}"
    output_file = output_dir_path / f"lote-real-{row.LotCodigo}.json"

    lote_json = {
        "_comment": f"Lote real extraído del bd_uaecd.gpkg el 2026-08-01. Coordenadas en ESRI:102233 (MAGNA Ciudad Bogotá).",
        "predio_id": predio_id,
        "direccion": f"Lote catastral {row.LotCodigo}",
        "coordenadas": {
            "crs": "ESRI:102233",
            "poligono": coords_2d[0]  # Solo el anillo exterior
        },
        "metadata": {
            "area_m2": float(row.SHAPE_Area),
            "perimetro_m": float(row.SHAPE_Leng),
            "lot_codigo": str(row.LotCodigo),
            "lot_cod_mzn": str(row.LotCodMzn),
            "lot_tipo": int(row.LotTipo) if row.LotTipo is not None else None,
            "d_lot_tipo": str(row.d_LotTipo),
            "d_lot_dispe": str(row.d_LotDispe),
            "d_lot_distr": str(row.d_LotDistr),
            "d_lot_clind": str(row.d_LotCLind),
            "d_lot_mtopo": str(row.d_LotMTopo),
            "d_lot_mejor": str(row.d_LotMejor),
            "fuente": "bd_uaecd.gpkg capa Lote",
            "feature_idx_original": index
        }
    }

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(lote_json, f, ensure_ascii=False, indent=2)

    click.echo("")
    click.echo(f"[OK] Archivo generado: {output_file}")

    # 5. Listo para usar
    click.echo("")
    click.echo("=" * 60)
    click.echo("  LOTE REAL LISTO PARA USAR")
    click.echo("=" * 60)
    click.echo("")
    click.echo("Para generar el caché POT:")
    click.echo(f"  python scripts/utilities/gpkg-to-cache-v3.py query --lot {output_file}")
    click.echo("")
    click.echo("Para ver el archivo:")
    click.echo(f"  code {output_file}")
    click.echo("")
    click.echo("Para extraer OTRO lote (cambiar índice):")
    click.echo(f"  python scripts/utilities/extract-real-lote.py --index 100")
    click.echo("")
    click.echo("Para buscar por LotCodigo específico:")
    click.echo(f"  python scripts/utilities/extract-real-lote.py --lot-codigo 002107015020")
    click.echo("")


if __name__ == "__main__":
    main()
