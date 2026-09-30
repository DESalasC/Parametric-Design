# -*- coding: utf-8 -*-
"""Script: verificar-codificacion-json.py
Proyecto: DiseñoParametrico
Fase: Transversal (utilidad de soporte)
Version: 01
Fecha: 2026-09-29
Descripcion:
    Guardián de codificación para archivos JSON del proyecto.

    Motivo: el toolchain mezcla Python 3.12, PowerShell, IronPython 2.7
    (Grasshopper) y un servidor local; hay riesgo de archivos JSON escritos
    con páginas de códigos distintas (cp1252/latin-1) o con BOM, que rompen
    lectores estrictos UTF-8 (error real observado: byte 0xF3 = 'ó' de cp1252
    al leer un contexto50 desde Grasshopper).

    Clasificación por archivo:
      OK            -- decodifica UTF-8 estricto (sin BOM) y parsea como JSON.
      WARN(bom)     -- tiene BOM UTF-8; requiere reescritura sin BOM.
      WARN(cp1252)  -- no decodifica UTF-8 estricto; sí como cp1252.
      WARN(latin-1) -- no decodifica UTF-8 ni cp1252; sí como latin-1.
      FAIL          -- no parsea como JSON ni tras la cascada de decodificación
                       (archivo corrupto o que no es JSON).

    Reparación (--aplicar): repara SOLO los archivos no-UTF-8-limpio (BOM o
    no-UTF8): decodifica con la cascada utf-8-sig -> cp1252 -> latin-1, parsea,
    redumpea como UTF-8 SIN BOM preservando el contenido (mismos caracteres),
    con backup <archivo>.bak-encoding-<YYYYMMDD-HHMM> antes de reescribir y
    escritura atómica (temp + os.replace). No transforma archivos ya OK.
    --ascii (solo junto a --aplicar) reescribe además los archivos reparados
    como ASCII-safe (ensure_ascii=True equivalente a nivel de parseo+dump).

Uso:
    python scripts/utilities/verificar-codificacion-json.py [--roots RUTA ...]
           [--aplicar] [--ascii] [--reporte RUTA]

Salida:
    Resumen por consola y reporte de texto en docs/planes/
    2026-09-29-plan-correccion-encoding-3d/anexos/scan-codificacion-<fecha>.txt
    Códigos de salida: 0 = todo OK (o todo reparado) | 1 = problemas sin
    --aplicar | 2 = algo falló al reparar.

Cambios:
    v01 (2026-09-29) — Versión inicial: escaneo recursivo de *.json,
        clasificación OK/WARN(bom)/WARN(cp1252)/WARN(latin-1)/FAIL,
        reparación con backup + escritura atómica, modo --ascii y reporte
        de texto del plan de corrección de encoding.
"""

import argparse
import codecs
import json
import os
import shutil
import sys
import tempfile
import time
from collections.abc import Sequence
from dataclasses import dataclass
from pathlib import Path

# --------------------------------------------------------------------------- #
# Constantes
# --------------------------------------------------------------------------- #

ROOT = Path(__file__).resolve().parent.parent.parent
RAIZ_DATOS_DEFAULT = ROOT / "data"
DIR_REPORTE_DEFAULT = (
    ROOT / "docs" / "planes" / "2026-09-29-plan-correccion-encoding-3d" / "anexos"
)

ESTADO_OK = "OK"
ESTADO_WARN_BOM = "WARN(bom)"
ESTADO_WARN_CP1252 = "WARN(cp1252)"
ESTADO_WARN_LATIN1 = "WARN(latin-1)"
ESTADO_FAIL = "FAIL"

ESTADOS = (ESTADO_OK, ESTADO_WARN_BOM, ESTADO_WARN_CP1252, ESTADO_WARN_LATIN1, ESTADO_FAIL)

ESTADO_POR_ORIGEN = {
    "utf-8": ESTADO_OK,
    "bom": ESTADO_WARN_BOM,
    "cp1252": ESTADO_WARN_CP1252,
    "latin-1": ESTADO_WARN_LATIN1,
}

DIRS_EXCLUIDOS = frozenset({".git", ".venv", "node_modules", "__pycache__", ".pytest_cache"})

FORMATO_TIMESTAMP_BACKUP = "%Y%m%d-%H%M"


# --------------------------------------------------------------------------- #
# Salida por consola
# --------------------------------------------------------------------------- #

def _configurar_salida() -> None:
    """Fuerza UTF-8 en stdout/stderr para evitar mojibake o crashes por code page."""
    for flujo in (sys.stdout, sys.stderr):
        try:
            flujo.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError, OSError):
            pass


def mostrar_ruta(ruta: Path) -> str:
    """Ruta corta para consola/reporte: relativa si cuelga de cwd o del proyecto."""
    for base in (Path.cwd(), ROOT):
        try:
            rel = os.path.relpath(str(ruta), str(base))
        except ValueError:  # distinto drive (p. ej. C: vs D:)
            continue
        if not rel.startswith(".."):
            return rel
    return str(ruta)


# --------------------------------------------------------------------------- #
# Decodificación / clasificación
# --------------------------------------------------------------------------- #

@dataclass
class ResultadoArchivo:
    """Resultado de clasificar la codificación de un archivo JSON."""

    ruta: Path
    estado: str
    origen: str
    detalle: str = ""


def decodificar_cascada(raw: bytes) -> tuple[str, str, list[str]]:
    """Decodifica bytes con la cascada utf-8-sig -> cp1252 -> latin-1.

    Devuelve (texto, origen, notas). Origen: 'utf-8' (limpio sin BOM), 'bom'
    (BOM UTF-8 presente), 'cp1252' o 'latin-1' (fallback de página de códigos).
    """
    notas: list[str] = []
    tiene_bom = raw.startswith(codecs.BOM_UTF8)
    cuerpo = raw[len(codecs.BOM_UTF8):] if tiene_bom else raw
    if tiene_bom:
        notas.append("BOM UTF-8 presente")
    try:
        texto = cuerpo.decode("utf-8")
        return texto, ("bom" if tiene_bom else "utf-8"), notas
    except UnicodeDecodeError as exc:
        notas.append(
            "utf-8 estricto falla en offset {0} (byte 0x{1:02X})".format(
                exc.start, cuerpo[exc.start]
            )
        )
    try:
        texto = cuerpo.decode("cp1252")
        return texto, "cp1252", notas
    except UnicodeDecodeError as exc:
        notas.append(
            "cp1252 falla en offset {0} (byte 0x{1:02X})".format(
                exc.start, cuerpo[exc.start]
            )
        )
    texto = cuerpo.decode("latin-1")
    return texto, "latin-1", notas


def clasificar_archivo(ruta: Path) -> ResultadoArchivo:
    """Clasifica un archivo JSON según su codificación y validez JSON.

    Estado: OK | WARN(bom) | WARN(cp1252) | WARN(latin-1) | FAIL.
    """
    raw = ruta.read_bytes()
    texto, origen, notas = decodificar_cascada(raw)
    try:
        json.loads(texto)
    except ValueError as exc:
        motivo = str(exc).splitlines()[0] if str(exc) else type(exc).__name__
        notas.append("JSON inválido: {0}".format(motivo))
        return ResultadoArchivo(ruta, ESTADO_FAIL, origen, "; ".join(notas))
    return ResultadoArchivo(ruta, ESTADO_POR_ORIGEN[origen], origen, "; ".join(notas))


# --------------------------------------------------------------------------- #
# Reparación
# --------------------------------------------------------------------------- #

def ruta_backup(ruta: Path, timestamp: str) -> Path:
    """Ruta libre para el backup <archivo>.bak-encoding-<YYYYMMDD-HHMM>."""
    nombre = "{0}.bak-encoding-{1}".format(ruta.name, timestamp)
    candidato = ruta.with_name(nombre)
    sufijo = 1
    while candidato.exists():
        sufijo += 1
        if sufijo > 99:
            raise RuntimeError("No hay nombre de backup libre para {0}".format(ruta))
        candidato = ruta.with_name("{0}-{1:02d}".format(nombre, sufijo))
    return candidato


def escribir_atomico(destino: Path, contenido: bytes) -> None:
    """Escritura atómica: temporal en el mismo directorio + os.replace."""
    fd, tmp = tempfile.mkstemp(
        prefix=destino.name + ".tmp-", suffix=".tmp", dir=str(destino.parent)
    )
    try:
        with os.fdopen(fd, "wb") as fh:
            fh.write(contenido)
            fh.flush()
            os.fsync(fh.fileno())
        os.replace(tmp, str(destino))
    except BaseException:
        try:
            if os.path.exists(tmp):
                os.unlink(tmp)
        except OSError:
            pass
        raise


def reparar_archivo(ruta: Path, timestamp: str, modo_ascii: bool) -> Path:
    """Repara un archivo no-UTF-8-limpio: reescribe como UTF-8 SIN BOM.

    Decodifica con la cascada, parsea y redumpea (ensure_ascii según modo_ascii)
    preservando el contenido. Crea backup antes de reescribir y usa escritura
    atómica. Devuelve la ruta del backup. Lanza excepción si no se puede.
    """
    raw = ruta.read_bytes()
    texto, _origen, _notas = decodificar_cascada(raw)
    datos = json.loads(texto)
    salida = json.dumps(datos, ensure_ascii=modo_ascii, indent=2)
    if json.loads(salida) != datos:
        raise ValueError("Round-trip JSON inconsistente para {0}".format(ruta))
    backup = ruta_backup(ruta, timestamp)
    shutil.copy2(str(ruta), str(backup))
    escribir_atomico(ruta, salida.encode("utf-8"))
    return backup


# --------------------------------------------------------------------------- #
# Escaneo
# --------------------------------------------------------------------------- #

def listar_archivos_json(raices: Sequence[Path]) -> tuple[list[Path], list[Path]]:
    """Lista archivos *.json bajo las raíces (recursivo, sin dirs excluidos).

    Devuelve (archivos, raices_faltantes); los archivos vienen únicos y ordenados.
    """
    vistos: set[str] = set()
    archivos: list[Path] = []
    faltantes: list[Path] = []
    for raiz in raices:
        candidatos: list[Path] = []
        if raiz.is_file():
            if raiz.suffix.lower() == ".json":
                candidatos.append(raiz)
        elif raiz.is_dir():
            for dirpath, dirnames, filenames in os.walk(str(raiz)):
                dirnames[:] = sorted(d for d in dirnames if d not in DIRS_EXCLUIDOS)
                for nombre in filenames:
                    if nombre.lower().endswith(".json"):
                        candidatos.append(Path(dirpath) / nombre)
        else:
            faltantes.append(raiz)
            continue
        for ruta in candidatos:
            clave = os.path.normcase(str(ruta.resolve()))
            if clave not in vistos:
                vistos.add(clave)
                archivos.append(ruta)
    archivos.sort(key=lambda p: os.path.normcase(str(p)))
    return archivos, faltantes


def escanear(archivos: Sequence[Path]) -> list[ResultadoArchivo]:
    """Clasifica cada archivo; los errores de lectura cuentan como FAIL."""
    resultados: list[ResultadoArchivo] = []
    for ruta in archivos:
        try:
            resultados.append(clasificar_archivo(ruta))
        except OSError as exc:
            resultados.append(
                ResultadoArchivo(
                    ruta, ESTADO_FAIL, "?", "lectura fallida: {0}".format(exc)
                )
            )
    return resultados


# --------------------------------------------------------------------------- #
# Reporte
# --------------------------------------------------------------------------- #

def contar_estados(resultados: Sequence[ResultadoArchivo]) -> dict[str, int]:
    """Cuenta resultados por estado (siempre con todas las claves de ESTADOS)."""
    cuenta: dict[str, int] = {estado: 0 for estado in ESTADOS}
    for res in resultados:
        if res.estado in cuenta:
            cuenta[res.estado] += 1
    return cuenta


def lineas_detalle(
    problemas: Sequence[ResultadoArchivo],
    faltantes: Sequence[Path],
    reparados: dict[str, Path],
    fallidos: dict[str, str],
) -> list[str]:
    """Una línea por archivo con problema o advertencia (y por raíz faltante)."""
    lineas: list[str] = []
    for raiz in faltantes:
        lineas.append("  [ERROR] raíz no encontrada: {0}".format(mostrar_ruta(raiz)))
    for res in problemas:
        clave = str(res.ruta)
        sufijo = ""
        if clave in reparados:
            sufijo = " [REPARADO; backup: {0}]".format(mostrar_ruta(reparados[clave]))
        if clave in fallidos:
            sufijo = " [FALLÓ REPARACIÓN: {0}]".format(fallidos[clave])
        linea = "  [{0}] {1}".format(res.estado, mostrar_ruta(res.ruta))
        if res.detalle:
            linea += " - " + res.detalle
        lineas.append(linea + sufijo)
    return lineas


def construir_reporte(
    argv_efectivo: Sequence[str],
    raices: Sequence[Path],
    resultados: Sequence[ResultadoArchivo],
    problemas: Sequence[ResultadoArchivo],
    faltantes: Sequence[Path],
    reparados: dict[str, Path],
    fallidos: dict[str, str],
    modo_aplicar: bool,
    modo_ascii: bool,
) -> list[str]:
    """Construye las líneas del reporte de texto (fecha, comando, resumen, detalle)."""
    cuenta = contar_estados(resultados)
    comando = "verificar-codificacion-json.py"
    if argv_efectivo:
        comando += " " + " ".join(argv_efectivo)
    lineas: list[str] = []
    lineas.append("Reporte de verificación de codificación JSON")
    lineas.append("Proyecto: DiseñoParametrico | Plan: 2026-09-29-plan-correccion-encoding-3d")
    lineas.append("=" * 72)
    lineas.append("Fecha/hora: {0}".format(time.strftime("%Y-%m-%d %H:%M:%S")))
    lineas.append("Comando: {0}".format(comando))
    lineas.append("Raíces: {0}".format(", ".join(mostrar_ruta(r) for r in raices)))
    lineas.append(
        "Modo: {0}".format(
            "verificación + reparación (--aplicar)" if modo_aplicar else "solo verificación"
        )
    )
    if modo_aplicar:
        lineas.append("ASCII-safe: {0}".format("sí (--ascii)" if modo_ascii else "no"))
    lineas.append("")
    lineas.append(
        "Resumen: {0} archivos | OK: {1} | WARN(bom): {2} | WARN(cp1252): {3} | "
        "WARN(latin-1): {4} | FAIL: {5}".format(
            len(resultados),
            cuenta[ESTADO_OK],
            cuenta[ESTADO_WARN_BOM],
            cuenta[ESTADO_WARN_CP1252],
            cuenta[ESTADO_WARN_LATIN1],
            cuenta[ESTADO_FAIL],
        )
    )
    lineas.append("Problemas: {0}".format(len(problemas) + len(faltantes)))
    if modo_aplicar:
        lineas.append("Reparados: {0} | Fallidos: {1}".format(len(reparados), len(fallidos)))
    detalle = lineas_detalle(problemas, faltantes, reparados, fallidos)
    if detalle:
        lineas.append("")
        lineas.append("Detalle (una línea por archivo con problema o advertencia):")
        lineas.extend(detalle)
    else:
        lineas.append("")
        lineas.append("Sin problemas ni advertencias.")
    return lineas


def escribir_reporte(destino: Path, lineas: Sequence[str]) -> None:
    """Escribe el reporte en UTF-8 (crea directorios intermedios si faltan)."""
    destino.parent.mkdir(parents=True, exist_ok=True)
    texto = "\n".join(lineas) + "\n"
    with open(destino, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(texto)


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #

def parsear_args(argv: Sequence[str] | None) -> argparse.Namespace:
    """Define y parsea los argumentos de línea de comandos."""
    parser = argparse.ArgumentParser(
        prog="verificar-codificacion-json.py",
        description="Verifica (y opcionalmente repara) la codificación de archivos JSON.",
    )
    parser.add_argument(
        "--roots",
        nargs="+",
        metavar="RUTA",
        default=None,
        help="Raíces a escanear recursivamente, en busca de *.json (default: data/ del proyecto).",
    )
    parser.add_argument(
        "--aplicar",
        action="store_true",
        help="Repara los archivos no-UTF-8-limpio (BOM o no-UTF8) con backup y escritura atómica.",
    )
    parser.add_argument(
        "--ascii",
        action="store_true",
        help="Con --aplicar: reescribe además los reparados como ASCII-safe (ensure_ascii=True).",
    )
    parser.add_argument(
        "--reporte",
        metavar="RUTA",
        default=None,
        help=(
            "Ruta del reporte de texto (default: docs/planes/"
            "2026-09-29-plan-correccion-encoding-3d/anexos/scan-codificacion-<fecha>.txt)."
        ),
    )
    args = parser.parse_args(argv)
    if args.ascii and not args.aplicar:
        parser.error("--ascii requiere --aplicar")
    return args


def main(argv: Sequence[str] | None = None) -> int:
    """Punto de entrada. Devuelve código de salida 0 (OK) / 1 (problemas) / 2 (fallo)."""
    args = parsear_args(argv)
    _configurar_salida()
    argv_efectivo = list(argv) if argv is not None else sys.argv[1:]

    if args.roots:
        raices = [
            r if r.is_absolute() else (Path.cwd() / r)
            for r in (Path(texto).expanduser() for texto in args.roots)
        ]
    else:
        raices = [RAIZ_DATOS_DEFAULT]

    archivos, faltantes = listar_archivos_json(raices)
    resultados = escanear(archivos)
    problemas = [res for res in resultados if res.estado != ESTADO_OK]
    cuenta = contar_estados(resultados)

    reparados: dict[str, Path] = {}
    fallidos: dict[str, str] = {}
    if args.aplicar and problemas:
        timestamp = time.strftime(FORMATO_TIMESTAMP_BACKUP)
        for res in problemas:
            try:
                backup = reparar_archivo(res.ruta, timestamp, args.ascii)
                reparados[str(res.ruta)] = backup
            except Exception as exc:  # noqa: BLE001 — el guardián reporta, no crashea
                fallidos[str(res.ruta)] = "{0}: {1}".format(type(exc).__name__, exc)

    print("=" * 72)
    print("Verificación de codificación JSON{0}".format(" [--aplicar]" if args.aplicar else ""))
    print("=" * 72)
    print("Raíces: {0}".format(", ".join(mostrar_ruta(r) for r in raices)))
    print("Archivos *.json: {0}".format(len(resultados)))
    print(
        "OK: {0} | WARN(bom): {1} | WARN(cp1252): {2} | WARN(latin-1): {3} | FAIL: {4}".format(
            cuenta[ESTADO_OK],
            cuenta[ESTADO_WARN_BOM],
            cuenta[ESTADO_WARN_CP1252],
            cuenta[ESTADO_WARN_LATIN1],
            cuenta[ESTADO_FAIL],
        )
    )
    print("Problemas: {0}".format(len(problemas) + len(faltantes)))
    detalle = lineas_detalle(problemas, faltantes, reparados, fallidos)
    if detalle:
        print("Detalle:")
        for linea in detalle:
            print(linea)
    if args.aplicar:
        print("Reparados: {0} | Fallidos: {1}".format(len(reparados), len(fallidos)))

    if args.reporte:
        ruta_reporte = Path(args.reporte)
    else:
        ruta_reporte = DIR_REPORTE_DEFAULT / (
            "scan-codificacion-{0}.txt".format(time.strftime("%Y-%m-%d"))
        )
    lineas_reporte = construir_reporte(
        argv_efectivo,
        raices,
        resultados,
        problemas,
        faltantes,
        reparados,
        fallidos,
        args.aplicar,
        args.ascii,
    )
    try:
        escribir_reporte(ruta_reporte, lineas_reporte)
        print("Reporte: {0}".format(mostrar_ruta(ruta_reporte)))
    except OSError as exc:
        print("ADVERTENCIA: no se pudo escribir el reporte ({0}): {1}".format(
            mostrar_ruta(ruta_reporte), exc))

    if args.aplicar:
        if fallidos or faltantes:
            print("Resultado: hubo fallos de reparación (exit 2).")
            return 2
        print("Resultado: sin problemas pendientes (exit 0).")
        return 0
    if problemas or faltantes:
        print(
            "Resultado: problemas detectados (exit 1); ningún archivo fue modificado. "
            "Usa --aplicar para reparar."
        )
        return 1
    print("Resultado: OK — codificación limpia (exit 0).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
