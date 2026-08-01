#!/usr/bin/env python3
# ==============================================================================
# setup-test-lot.py
# ------------------------------------------------------------------------------
# Crea un lote de ejemplo en data/lotes-ejemplo/ y exporta el inventario
# completo de campos del .gpkg para inspección.
#
# Uso:
#   python scripts/utilities/setup-test-lot.py
# ==============================================================================

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

import click

try:
    import pyogrio
except ImportError:
    click.echo("[ERROR] pyogrio no instalado", err=True)
    sys.exit(1)


# ---------------------------------------------------------------------------
# Configuración
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
DEFAULT_GPKG = os.environ.get(
    "POT_GPKG_PATH",
    r"D:\Users\Dario Salas\proyectos\DesParametrico\2-Entradas\Datos_Sitio_GDB\bd_uaecd.gpkg",
)


# ---------------------------------------------------------------------------
# Lote de ejemplo: Chapinero (coordenadas aproximadas MAGNA-SIRGAS Origen Bogotá)
# ---------------------------------------------------------------------------
# Coordenadas reales aproximadas de la Carrera 7 con Calle 72, Chapinero
# en MAGNA-SIRGAS Origen Bogotá (EPSG:9377)
# X ~ 1007700, Y ~ 1014400 aprox (verificar con IDECA)
LOTE_CHAPINERO = {
    "_comment": "Lote de ejemplo en Chapinero, Bogotá. Coordenadas MAGNA-SIRGAS Origen Bogotá (EPSG:9377). Reemplazar con coordenadas reales del predio.",
    "predio_id": "CHAPINERO-TEST-001",
    "direccion": "Carrera 7 # 72-30, Chapinero, Bogotá",
    "coordenadas": {
        "crs": "EPSG:9377",
        "poligono": [
            [1007650.0, 1014350.0],
            [1007720.0, 1014350.0],
            [1007720.0, 1014420.0],
            [1007650.0, 1014420.0],
            [1007650.0, 1014350.0]  # cerrar polígono
        ]
    },
    "metadata": {
        "area_m2": 4900.0,
        "frente_m": 70.0,
        "fondo_m": 70.0,
        "barrio": "Chapinero Central",
        "localidad": "Chapinero",
        "upz": "Chapinero"
    }
}

# Segundo lote de ejemplo: Centro (para probar otra UPZ)
LOTE_CENTRO = {
    "_comment": "Lote de ejemplo en Centro Histórico, Bogotá. Coordenadas MAGNA-SIRGAS Origen Bogotá.",
    "predio_id": "CENTRO-TEST-001",
    "direccion": "Calle 19 # 8-30, La Candelaria, Bogotá",
    "coordenadas": {
        "crs": "EPSG:9377",
        "poligono": [
            [1000800.0, 1006800.0],
            [1000850.0, 1006800.0],
            [1000850.0, 1006850.0],
            [1000800.0, 1006850.0],
            [1000800.0, 1006800.0]
        ]
    },
    "metadata": {
        "area_m2": 2500.0,
        "frente_m": 50.0,
        "fondo_m": 50.0,
        "barrio": "La Candelaria",
        "localidad": "La Candelaria",
        "upz": "La Candelaria"
    }
}


@click.command()
@click.option("--gpkg", default=DEFAULT_GPKG, help="Ruta al .gpkg")
@click.option("--export-fields", is_flag=True, default=True, help="Exportar inventario de campos a JSON")
def main(gpkg: str, export_fields: bool) -> None:
    """Crea lotes de ejemplo y exporta inventario de campos del .gpkg."""

    click.echo("")
    click.echo("=" * 60)
    click.echo("  setup-test-lot.py")
    click.echo("=" * 60)
    click.echo("")

    # 1. Verificar .gpkg
    gpkg_path = Path(gpkg)
    if not gpkg_path.exists():
        click.echo(f"[ERROR] .gpkg no encontrado: {gpkg_path}", err=True)
        click.echo(f"        Variable POT_GPKG_PATH = {os.environ.get('POT_GPKG_PATH', 'NO DEFINIDA')}", err=True)
        sys.exit(1)

    click.echo(f"[OK] .gpkg encontrado: {gpkg_path}")
    click.echo(f"     Tamaño: {gpkg_path.stat().st_size / (1024*1024):.1f} MB")

    # 2. Crear lotes de ejemplo
    lotes_dir = PROJECT_ROOT / "data" / "lotes-ejemplo"
    lotes_dir.mkdir(parents=True, exist_ok=True)

    click.echo("")
    click.echo("[1] Creando lotes de ejemplo...")

    lotes = [
        ("lote-chapinero.json", LOTE_CHAPINERO),
        ("lote-centro.json", LOTE_CENTRO),
    ]

    for filename, content in lotes:
        path = lotes_dir / filename
        with open(path, "w", encoding="utf-8") as f:
            json.dump(content, f, ensure_ascii=False, indent=2)
        click.echo(f"  [OK] {path}")

    # 3. Exportar inventario de campos
    if export_fields:
        click.echo("")
        click.echo("[2] Exportando inventario de campos del .gpkg...")

        try:
            layers = pyogrio.list_layers(str(gpkg_path))
            click.echo(f"  Capas encontradas: {len(layers)}")

            inventory = {}
            for layer_name, geom_type in layers:
                layer_name_str = str(layer_name)
                click.echo(f"  Inspeccionando: {layer_name_str} ({geom_type})")

                try:
                    df = pyogrio.read_dataframe(
                        str(gpkg_path),
                        layer=layer_name_str,
                        max_features=1,
                    )

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
                        "geom_type": str(geom_type),
                        "field_count": len(fields),
                        "fields": fields,
                    }
                    click.echo(f"    -> {len(fields)} campos")

                except Exception as e:
                    click.echo(f"    [WARN] Error leyendo {layer_name_str}: {e}", err=True)
                    inventory[layer_name_str] = {"error": str(e)}

            # Guardar
            output_path = PROJECT_ROOT / "data" / "gdb_fields_inventory.json"
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(inventory, f, ensure_ascii=False, indent=2, default=str)

            total_fields = sum(r.get("field_count", 0) for r in inventory.values())
            click.echo(f"  [OK] Inventario exportado: {output_path}")
            click.echo(f"  [OK] Total campos: {total_fields}")

        except Exception as e:
            click.echo(f"  [ERROR] Falló exportación: {e}", err=True)

    # 4. Generar whitelist preliminar basada en campos d_Lot*
    click.echo("")
    click.echo("[3] Generando whitelist preliminar (campos d_Lot*)...")

    try:
        # Leer capa Lote
        df = pyogrio.read_dataframe(str(gpkg_path), layer="Lote", max_features=1)

        lot_fields = [col for col in df.columns if col.startswith("d_Lot")]
        click.echo(f"  Campos d_Lot* encontrados: {len(lot_fields)}")

        # Otros campos comunes que pueden ser útiles
        other_interesting = []
        keywords = ["area", "uso", "altura", "retiro", "tratam", "suelo", "via", "upz", "barrio", "localidad"]
        for col in df.columns:
            if col == "geometry":
                continue
            col_lower = col.lower()
            if any(kw in col_lower for kw in keywords):
                if col not in lot_fields:
                    other_interesting.append(col)

        click.echo(f"  Otros campos relevantes: {len(other_interesting)}")

        # Whitelist preliminar
        whitelist = {
            "_comment": "Whitelist preliminar AUTO-GENERADA por setup-test-lot.py. REVISAR Y AJUSTAR manualmente.",
            "_fecha_generacion": "2026-08-01",
            "_total_campos_capa_lote": len([c for c in df.columns if c != "geometry"]),
            "campos": {
                "identificacion_lote": lot_fields[:20] if len(lot_fields) > 20 else lot_fields,
                "normativa_pot": [c for c in other_interesting if any(kw in c.lower() for kw in ["uso", "tratam", "suelo"])],
                "alturas": [c for c in other_interesting if "altura" in c.lower()],
                "retiros": [c for c in other_interesting if "retiro" in c.lower()],
                "vias": [c for c in other_interesting if "via" in c.lower()],
                "ubicacion": [c for c in other_interesting if any(kw in c.lower() for kw in ["upz", "barrio", "localidad"])],
                "areas": [c for c in other_interesting if "area" in c.lower()],
            },
            "_nota": "Esta whitelist es preliminar. Editar manualmente basándose en data/gdb_fields_inventory.json"
        }

        whitelist_path = PROJECT_ROOT / "config" / "field-whitelist.json"
        whitelist_path.parent.mkdir(parents=True, exist_ok=True)
        with open(whitelist_path, "w", encoding="utf-8") as f:
            json.dump(whitelist, f, ensure_ascii=False, indent=2, default=str)

        click.echo(f"  [OK] Whitelist: {whitelist_path}")

    except Exception as e:
        click.echo(f"  [ERROR] Falló whitelist: {e}", err=True)

    # 5. Probar query con lote Chapinero
    click.echo("")
    click.echo("[4] Probando query con lote Chapinero...")

    try:
        lote_path = lotes_dir / "lote-chapinero.json"

        # Importar y ejecutar el comando query de gpkg-to-cache
        sys.path.insert(0, str(PROJECT_ROOT / "scripts" / "utilities"))
        from importlib import import_module
        gpkg_module = import_module("gpkg-to-cache".replace("-", "_"))

        # Llamar directamente al comando query
        from click.testing import CliRunner
        runner = CliRunner()
        result = runner.invoke(gpkg_module.cli, [
            "query",
            "--lot", str(lote_path),
            "--layer", "Lote",
        ])

        if result.exit_code == 0:
            click.echo(result.output)
            click.echo("  [OK] Query exitoso")
        else:
            click.echo(f"  [WARN] Query falló (puede ser normal si coordenadas no intersectan):", err=True)
            click.echo(result.output, err=True)
            if result.exception:
                import traceback
                click.echo("".join(traceback.format_exception(type(result.exception), result.exception, result.exception.__traceback__)), err=True)

    except Exception as e:
        click.echo(f"  [ERROR] No se pudo probar query: {e}", err=True)
        import traceback
        click.echo(traceback.format_exc(), err=True)

    # 6. Resumen
    click.echo("")
    click.echo("=" * 60)
    click.echo("  RESUMEN")
    click.echo("=" * 60)
    click.echo("")
    click.echo("Archivos generados:")
    click.echo(f"  - data/lotes-ejemplo/lote-chapinero.json")
    click.echo(f"  - data/lotes-ejemplo/lote-centro.json")
    click.echo(f"  - data/gdb_fields_inventory.json  (revisar con VS Code)")
    click.echo(f"  - config/field-whitelist.json     (editar manualmente)")
    click.echo("")
    click.echo("Próximos pasos:")
    click.echo("  1. Abrir data/gdb_fields_inventory.json y revisar campos disponibles")
    click.echo("  2. Ajustar config/field-whitelist.json con los campos relevantes")
    click.echo("  3. Probar: python scripts/utilities/gpkg-to-cache.py query --lot data/lotes-ejemplo/lote-chapinero.json")
    click.echo("")
    click.echo("Si las coordenadas del lote Chapinero no intersectan, ajustar en:")
    click.echo("  data/lotes-ejemplo/lote-chapinero.json -> coordenadas.poligono")
    click.echo("")


if __name__ == "__main__":
    main()
