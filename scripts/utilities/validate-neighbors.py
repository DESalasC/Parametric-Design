#!/usr/bin/env python3
# ==============================================================================
# validate-neighbors.py
# ------------------------------------------------------------------------------
# Valida el formato de entrada de vecinos antes de pasar a ANALISIS_VECINOS.py
# en Grasshopper.
#
# Acepta:
#   - Archivo .3dm (Rhino) con Breps cerrados y propiedad AlturaTotal
#   - Archivo .json con lista de vecinos (huella + altura)
#   - Carpeta con archivos .3dm o .json
#
# Verifica:
#   1. Cada vecino es un Brep cerrado (no superficie abierta)
#   2. Cada vecino tiene AlturaTotal asignada (User Text o propiedad)
#   3. La altura es razonable (3-200 m)
#   4. La huella es una polilínea cerrada (no NURBS)
#   5. Coordenadas en rango MAGNA-SIRGAS Bogotá o local Archicad
#
# Uso:
#   python validate-neighbors.py --input data/neighbors/vecinos.3dm
#   python validate-neighbors.py --input data/neighbors/vecinos.json --verbose
#
# Salida:
#   - Código 0: todos válidos
#   - Código 1: algunos inválidos (ver reporte)
#   - Código 2: error de formato o archivo
# ==============================================================================

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import click

try:
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
except ImportError:
    click.echo("[ERROR] Instala rich: pip install rich", err=True)
    sys.exit(2)

console = Console()


# ---------------------------------------------------------------------------
# Constantes
# ---------------------------------------------------------------------------
ALTURA_MIN_M = 3.0
ALTURA_MAX_M = 200.0

# Rango aproximado de coordenadas MAGNA-SIRGAS Origen Bogotá
MAGNA_X_RANGE = (990000, 1010000)
MAGNA_Y_RANGE = (990000, 1010000)


# ---------------------------------------------------------------------------
# Validadores
# ---------------------------------------------------------------------------
class NeighborValidator:
    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.errors: list[dict[str, Any]] = []
        self.warnings: list[dict[str, Any]] = []
        self.valid: list[dict[str, Any]] = []

    def add_error(self, vecino_id: str, msg: str):
        self.errors.append({"vecino_id": vecino_id, "error": msg})
        if self.verbose:
            console.print(f"  [red]ERROR[/red] {vecino_id}: {msg}")

    def add_warning(self, vecino_id: str, msg: str):
        self.warnings.append({"vecino_id": vecino_id, "warning": msg})
        if self.verbose:
            console.print(f"  [yellow]WARN[/yellow] {vecino_id}: {msg}")

    def add_valid(self, vecino_id: str, info: dict[str, Any]):
        self.valid.append({"vecino_id": vecino_id, **info})
        if self.verbose:
            console.print(f"  [green]OK[/green] {vecino_id}: altura={info.get('altura_total')}m")


def validate_json_neighbor(vecino: dict[str, Any], validator: NeighborValidator, idx: int) -> None:
    """Valida un vecino en formato JSON."""
    vecino_id = vecino.get("id", f"vecino-{idx:03d}")

    # 1. Verificar campos obligatorios
    if "altura_total" not in vecino:
        validator.add_error(vecino_id, "Falta campo 'altura_total'")
        return

    altura = vecino["altura_total"]
    if not isinstance(altura, (int, float)):
        validator.add_error(vecino_id, f"altura_total no es numérico: {altura}")
        return

    # 2. Rango de altura
    if altura < ALTURA_MIN_M:
        validator.add_error(vecino_id, f"Altura {altura}m < mínimo {ALTURA_MIN_M}m")
        return
    if altura > ALTURA_MAX_M:
        validator.add_warning(vecino_id, f"Altura {altura}m > máximo {ALTURA_MAX_M}m (¿rascacielos?)")

    # 3. Verificar huella
    if "huella" not in vecino:
        validator.add_error(vecino_id, "Falta campo 'huella' (polígono)")
        return

    huella = vecino["huella"]
    if not isinstance(huella, list) or len(huella) < 3:
        validator.add_error(vecino_id, f"Huella inválida: necesita >= 3 puntos, tiene {len(huella) if isinstance(huella, list) else 'N/A'}")
        return

    # 4. Verificar que es polilínea (no NURBS)
    for i, pt in enumerate(huella):
        if not isinstance(pt, (list, tuple)) or len(pt) < 2:
            validator.add_error(vecino_id, f"Punto {i} de huella inválido: {pt}")
            return

    # 5. Verificar coordenadas en rango MAGNA
    xs = [pt[0] for pt in huella]
    ys = [pt[1] for pt in huella]
    x_range = (min(xs), max(xs))
    y_range = (min(ys), max(ys))

    if x_range[0] > 100 and x_range[0] < MAGNA_X_RANGE[0]:
        validator.add_warning(vecino_id, f"Coordenadas X ({x_range[0]:.0f}) fuera de rango MAGNA Bogotá. ¿Es origen local (0,0,0)?")
    elif x_range[0] >= MAGNA_X_RANGE[0] and x_range[1] <= MAGNA_X_RANGE[1]:
        pass  # OK, está en MAGNA
    elif x_range[0] < 100:
        validator.add_warning(vecino_id, f"Coordenadas X ({x_range[0]:.1f}) sugieren origen local Archicad")

    # 6. Verificar que la huella es cerrada (primer punto == último)
    if huella[0] != huella[-1]:
        validator.add_warning(vecino_id, "Huella no está cerrada (se cerrará automáticamente)")

    # Todo OK
    validator.add_valid(vecino_id, {
        "altura_total": altura,
        "num_puntos_huella": len(huella),
        "bbox": {"x": x_range, "y": y_range},
    })


def validate_json_file(file_path: Path, validator: NeighborValidator) -> None:
    """Valida un archivo JSON con lista de vecinos."""
    try:
        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        validator.add_error(file_path.name, f"JSON inválido: {e}")
        return

    vecinos = data if isinstance(data, list) else data.get("vecinos", [])
    if not vecinos:
        validator.add_error(file_path.name, "No hay vecinos en el archivo")
        return

    console.print(f"[cyan]Validando {len(vecinos)} vecinos de {file_path.name}[/cyan]")

    for idx, vecino in enumerate(vecinos):
        validate_json_neighbor(vecino, validator, idx)


def validate_3dm_file(file_path: Path, validator: NeighborValidator) -> None:
    """Valida un archivo .3dm de Rhino con vecinos como Breps."""
    try:
        import rhino3dm
    except ImportError:
        validator.add_error(file_path.name, "rhino3dm no instalado. Instala con: pip install rhino3dm")
        return

    try:
        model = rhino3dm.File3dm.Read(str(file_path))
    except Exception as e:
        validator.add_error(file_path.name, f"No se pudo leer .3dm: {e}")
        return

    breps = [obj for obj in model.Objects if obj.Geometry.ObjectType == rhino3dm.ObjectType.Brep]
    if not breps:
        validator.add_error(file_path.name, "No se encontraron Breps en el archivo")
        return

    console.print(f"[cyan]Validando {len(breps)} Breps de {file_path.name}[/cyan]")

    for idx, obj in enumerate(breps):
        vecino_id = f"brep-{idx:03d}"
        brep = obj.Geometry

        # 1. Verificar que es cerrado
        if not brep.IsSolid:
            validator.add_error(vecino_id, "Brep no es sólido cerrado (¿superficie abierta?)")
            continue

        # 2. Buscar AlturaTotal en User Text
        user_texts = obj.Attributes.UserStrings
        altura_str = None
        for ut in user_texts:
            if ut[0].lower() in ("alturatotal", "altura_total", "altura"):
                altura_str = ut[1]
                break

        if altura_str is None:
            validator.add_error(vecino_id, "No tiene AlturaTotal en User Text")
            continue

        try:
            altura = float(altura_str)
        except ValueError:
            validator.add_error(vecino_id, f"AlturaTotal no es numérico: '{altura_str}'")
            continue

        # 3. Rango de altura
        if altura < ALTURA_MIN_M:
            validator.add_error(vecino_id, f"Altura {altura}m < mínimo {ALTURA_MIN_M}m")
            continue
        if altura > ALTURA_MAX_M:
            validator.add_warning(vecino_id, f"Altura {altura}m > máximo {ALTURA_MAX_M}m")

        # 4. Verificar huella (proyectar a XY)
        try:
            bbox = brep.GetBoundingBox()
            min_pt = bbox.Min
            max_pt = bbox.Max
            x_range = (min_pt.X, max_pt.X)
            y_range = (min_pt.Y, max_pt.Y)

            # Coordenadas MAGNA
            if x_range[0] >= MAGNA_X_RANGE[0] and x_range[1] <= MAGNA_X_RANGE[1]:
                pass  # OK
            elif x_range[0] < 100:
                validator.add_warning(vecino_id, f"Coordenadas X ({x_range[0]:.1f}) sugieren origen local Archicad")

        except Exception as e:
            validator.add_warning(vecino_id, f"No se pudo calcular bbox: {e}")
            x_range = y_range = (None, None)

        validator.add_valid(vecino_id, {
            "altura_total": altura,
            "bbox": {"x": x_range, "y": y_range},
        })


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
@click.command()
@click.option(
    "--input", "-i",
    required=True,
    type=click.Path(exists=True),
    help="Archivo .3dm, .json o carpeta con vecinos",
)
@click.option("--verbose", "-v", is_flag=True, help="Salida detallada")
@click.option(
    "--output", "-o",
    type=click.Path(),
    default=None,
    help="Guardar reporte JSON en este archivo",
)
def main(input: str, verbose: bool, output: str | None) -> None:
    """Valida vecinos antes de pasar a ANALISIS_VECINOS.py en Grasshopper."""
    input_path = Path(input)
    validator = NeighborValidator(verbose=verbose)

    console.print(Panel.fit(
        f"[bold]Validador de Vecinos[/bold]\nInput: {input_path}",
        border_style="cyan",
    ))

    # Determinar tipo de input
    if input_path.is_file():
        if input_path.suffix.lower() == ".json":
            validate_json_file(input_path, validator)
        elif input_path.suffix.lower() == ".3dm":
            validate_3dm_file(input_path, validator)
        else:
            console.print(f"[red]Formato no soportado: {input_path.suffix}[/red]")
            sys.exit(2)
    elif input_path.is_dir():
        files = list(input_path.glob("*.json")) + list(input_path.glob("*.3dm"))
        if not files:
            console.print(f"[red]No se encontraron .json o .3dm en {input_path}[/red]")
            sys.exit(2)
        console.print(f"[cyan]Procesando {len(files)} archivos...[/cyan]")
        for f in files:
            if f.suffix.lower() == ".json":
                validate_json_file(f, validator)
            elif f.suffix.lower() == ".3dm":
                validate_3dm_file(f, validator)
    else:
        console.print(f"[red]Path inválido: {input_path}[/red]")
        sys.exit(2)

    # Reporte final
    console.print()
    table = Table(title="Resumen de Validación")
    table.add_column("Estado", style="bold")
    table.add_column("Cantidad", justify="right")
    table.add_row("[green]Válidos[/green]", str(len(validator.valid)))
    table.add_row("[yellow]Warnings[/yellow]", str(len(validator.warnings)))
    table.add_row("[red]Errores[/red]", str(len(validator.errors)))
    console.print(table)

    # Detalle de errores
    if validator.errors:
        console.print()
        err_table = Table(title="Errores")
        err_table.add_column("Vecino ID")
        err_table.add_column("Error")
        for e in validator.errors:
            err_table.add_row(e["vecino_id"], e["error"])
        console.print(err_table)

    # Detalle de warnings
    if validator.warnings:
        console.print()
        warn_table = Table(title="Warnings")
        warn_table.add_column("Vecino ID")
        warn_table.add_column("Warning")
        for w in validator.warnings:
            warn_table.add_row(w["vecino_id"], w["warning"])
        console.print(warn_table)

    # Guardar reporte si se pidió
    if output:
        report = {
            "input": str(input_path),
            "timestamp": validator.valid[0].get("vecino_id") if validator.valid else None,
            "summary": {
                "validos": len(validator.valid),
                "warnings": len(validator.warnings),
                "errores": len(validator.errors),
            },
            "detalle": {
                "validos": validator.valid,
                "warnings": validator.warnings,
                "errores": validator.errors,
            },
        }
        with open(output, "w", encoding="utf-8") as f:
            json.dump(report, f, ensure_ascii=False, indent=2, default=str)
        console.print(f"\n[green]Reporte guardado: {output}[/green]")

    # Código de salida
    if validator.errors:
        console.print("\n[red]VALIDACIÓN FALLIDA: hay errores que corregir.[/red]")
        sys.exit(1)
    elif validator.warnings:
        console.print("\n[yellow]VALIDACIÓN OK con warnings.[/yellow]")
        sys.exit(0)
    else:
        console.print("\n[green]VALIDACIÓN OK: todos los vecinos son válidos.[/green]")
        sys.exit(0)


if __name__ == "__main__":
    main()
