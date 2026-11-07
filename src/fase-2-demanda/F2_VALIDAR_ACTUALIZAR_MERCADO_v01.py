#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
F2_VALIDAR_ACTUALIZAR_MERCADO_v01.py — Validación y marcado de vigencia del
mercado inmobiliario (Fase 2)
Proyecto: DiseñoParametrico — Fase 2
Python 3.12 (stdlib). Type hints.

v01.0 (2026-11-06): version inicial. Valida la fecha de los datos de mercado
de F2 y, si supera el umbral (default 14 dias), marca el archivo como vencido
y genera un reporte de acciones de actualización.

OBJETIVO:
  Recorrer los archivos de parámetros de mercado de F2 y validar si la
  información inmobiliaria (precios de venta, costos de construcción, cánones
  de arriendo) está vigente frente a la fecha actual.

ALCANCE:
  - NO consulta APIs externas ni inventa precios de mercado: no hay una fuente
    automatizada documentada en el vault para actualizar precios reales.
  - Solo lee fechas de metadatos y escribe banderas de vigencia + reporte.
  - Modo --aplicar actualiza metadatos de estado en cada archivo (sin tocar
    precios, que requieren fuente externa verificada por el operador).

ARCHIVOS INSPECCIONADOS:
  - data/fase-2-demanda/mercado/parametros_*_f2mercado_*.json
  - src/fase-2-demanda/F2_Modelo_Financiero/parametros_entrada.json
  - src/fase-2-demanda/F2_Modelo_Renta/parametros_entrada.json

FECHA DE REFERENCIA (por archivo, la mas reciente disponible):
  meta.fecha_ejecucion
  meta.mercado.fecha_captura_origen
  meta.sync.fecha_sync

SALIDA:
  data/fase-2-demanda/mercado/reporte_vigencia_mercado.json

USO:
  python F2_VALIDAR_ACTUALIZAR_MERCADO_v01.py
  python F2_VALIDAR_ACTUALIZAR_MERCADO_v01.py --umbral-dias 14
  python F2_VALIDAR_ACTUALIZAR_MERCADO_v01.py --aplicar

VARIABLES DE ENTORNO:
  DISENO_PARAMETRICO_ROOT: raiz del proyecto (default: calculada desde este
                           archivo, dos niveles arriba de src/fase-2-demanda).

ESTÁNDAR DE DOCUMENTACIÓN (CLAUDE.md del proyecto):
  Entradas:  DISENO_PARAMETRICO_ROOT (env), --umbral-dias (int), --aplicar (flag)
  Salidas:   reporte_vigencia_mercado.json (escrito), banderas meta en archivos
             vencidos (cuando --aplicar).

ULTIMOS TRES CAMBIOS:
  v01.0 (2026-11-06): creacion inicial. Validacion de vigencia de mercado F2
                      con umbral configurable y reporte JSON.
"""

from __future__ import annotations

import argparse
import datetime
import io
import json
import os
from pathlib import Path
from typing import Any

# ----------------------------------------------------------------------------
# Rutas y constantes
# ----------------------------------------------------------------------------

DEFAULT_UMBRAL_DIAS = 14

_ARCHIVOS_MERCADO_FIJOS = (
    "src/fase-2-demanda/F2_Modelo_Financiero/parametros_entrada.json",
    "src/fase-2-demanda/F2_Modelo_Renta/parametros_entrada.json",
)

REPORTE_NOMBRE = "reporte_vigencia_mercado.json"

_FECHAS_META = (
    "fecha_ejecucion",
    "fecha_captura",
    "fecha_captura_origen",
    "fecha_sync",
)


def _raiz_proyecto() -> Path:
    """Raíz del proyecto: DISENO_PARAMETRICO_ROOT o cálculo desde este archivo."""
    env_root = os.environ.get("DISENO_PARAMETRICO_ROOT")
    if env_root:
        return Path(env_root)
    return Path(__file__).resolve().parents[3]  # src/fase-2-demanda -> raiz


def _candidatos_mercado(root: Path) -> list[Path]:
    """Lista los archivos de parámetros de mercado de F2 a inspeccionar."""
    candidatos: list[Path] = []

    dir_mercado = root / "data" / "fase-2-demanda" / "mercado"
    if dir_mercado.is_dir():
        candidatos.extend(sorted(dir_mercado.glob("parametros_*_f2mercado_*.json")))

    for rel in _ARCHIVOS_MERCADO_FIJOS:
        p = root / rel
        if p.is_file():
            candidatos.append(p)

    # Deduplicar manteniendo orden
    vistos: set[Path] = set()
    unicos: list[Path] = []
    for c in candidatos:
        if c not in vistos:
            vistos.add(c)
            unicos.append(c)
    return unicos


def _leer_json(ruta: Path) -> dict[str, Any] | None:
    try:
        with io.open(ruta, "r", encoding="utf-8") as fh:
            return json.load(fh)
    except Exception:
        return None


def _extraer_fecha_datos(datos: dict[str, Any]) -> str | None:
    """Devuelve la fecha mas reciente disponible en los metadatos (YYYY-MM-DD)."""
    fechas: list[str] = []
    meta = datos.get("meta") or {}
    for clave in _FECHAS_META:
        valor = meta.get(clave)
        if isinstance(valor, str) and len(valor) >= 10:
            fechas.append(valor[:10])
    mercado = meta.get("mercado") or {}
    for clave in ("fecha_captura", "fecha_captura_origen", "fecha_sync"):
        valor = mercado.get(clave)
        if isinstance(valor, str) and len(valor) >= 10:
            fechas.append(valor[:10])
    if not fechas:
        return None
    fechas_validas = []
    for f in fechas:
        try:
            datetime.date.fromisoformat(f)
            fechas_validas.append(f)
        except ValueError:
            continue
    if not fechas_validas:
        return None
    return max(fechas_validas)


def _chip_de_ruta(ruta: Path) -> str | None:
    """Intenta extraer el CHIP del nombre de archivo.

    Solo reconoce el patron parametros_<CHIP>_f2mercado_<YYYY-MM>.json.
    Para archivos como parametros_entrada.json devuelve None (no es un archivo
    de mercado por chip, es el archivo de parametros por defecto de F2).
    """
    nombre = ruta.name
    if not nombre.startswith("parametros_") or "_f2mercado_" not in nombre:
        return None
    # parametros_AAA0127AZPA_f2mercado_2026-09.json -> AAA0127AZPA
    resto = nombre.replace("parametros_", "", 1)
    chip = resto.split("_f2mercado_", 1)[0]
    return chip or None


def validar_archivo(ruta: Path, umbral_dias: int, fecha_hoy: datetime.date) -> dict[str, Any]:
    """Valida la vigencia de un archivo de mercado. Devuelve un dict de resultado."""
    resultado: dict[str, Any] = {
        "ruta": str(ruta),
        "chip": _chip_de_ruta(ruta),
        "existe": True,
        "valido": False,
        "fecha_datos": None,
        "dias_transcurridos": None,
        "vencido": False,
        "error": None,
    }

    datos = _leer_json(ruta)
    if datos is None:
        resultado["error"] = "JSON ilegible o vacio"
        return resultado

    fecha_str = _extraer_fecha_datos(datos)
    resultado["fecha_datos"] = fecha_str
    if fecha_str is None:
        resultado["error"] = "sin fecha de referencia en metadatos"
        return resultado

    try:
        fecha_datos = datetime.date.fromisoformat(fecha_str)
    except ValueError:
        resultado["error"] = f"fecha ilegible: {fecha_str}"
        return resultado

    dias = (fecha_hoy - fecha_datos).days
    resultado["dias_transcurridos"] = dias
    resultado["vencido"] = dias > umbral_dias
    resultado["valido"] = True
    return resultado


def generar_reporte(
    root: Path,
    umbral_dias: int,
    fecha_hoy: datetime.date,
    aplicar: bool = False,
) -> dict[str, Any]:
    """Recorre los archivos de mercado y genera el reporte de vigencia."""
    archivos = _candidatos_mercado(root)
    resultados: list[dict[str, Any]] = []

    for ruta in archivos:
        res = validar_archivo(ruta, umbral_dias, fecha_hoy)
        resultados.append(res)

        if aplicar and res["valido"] and res["vencido"]:
            datos = _leer_json(ruta)
            if datos is not None:
                meta = datos.setdefault("meta", {})
                meta["estado_vigencia"] = "VENCIDO"
                meta["requiere_actualizacion_mercado"] = True
                meta["umbral_dias_validacion"] = umbral_dias
                meta["fecha_validacion"] = fecha_hoy.isoformat()
                meta["dias_transcurridos_validacion"] = res["dias_transcurridos"]
                try:
                    with io.open(ruta, "w", encoding="utf-8") as fh:
                        json.dump(datos, fh, ensure_ascii=False, indent=2)
                except Exception as ex:  # pragma: no cover - escritura
                    res["error"] = (res["error"] or "") + f"; no se pudo escribir: {ex}"

    vencidos = [r for r in resultados if r["vencido"]]
    frescos = [r for r in resultados if r["valido"] and not r["vencido"]]
    invalidos = [r for r in resultados if not r["valido"]]

    reporte: dict[str, Any] = {
        "fecha_validacion": fecha_hoy.isoformat(),
        "umbral_dias": umbral_dias,
        "total_archivos": len(resultados),
        "vencidos": len(vencidos),
        "frescos": len(frescos),
        "invalidos": len(invalidos),
        "archivos": resultados,
    }

    dir_mercado = root / "data" / "fase-2-demanda" / "mercado"
    dir_mercado.mkdir(parents=True, exist_ok=True)
    ruta_reporte = dir_mercado / REPORTE_NOMBRE
    with io.open(ruta_reporte, "w", encoding="utf-8") as fh:
        json.dump(reporte, fh, ensure_ascii=False, indent=2)

    reporte["ruta_reporte"] = str(ruta_reporte)
    return reporte


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Valida la vigencia de la información inmobiliaria de F2 y marca vencidos."
    )
    parser.add_argument(
        "--umbral-dias",
        type=int,
        default=DEFAULT_UMBRAL_DIAS,
        help=f"Umbral de vigencia en dias (default {DEFAULT_UMBRAL_DIAS}).",
    )
    parser.add_argument(
        "--aplicar",
        action="store_true",
        help="Escribe banderas de vencimiento en los archivos de mercado vencidos.",
    )
    args = parser.parse_args()

    root = _raiz_proyecto()
    fecha_hoy = datetime.date.today()

    reporte = generar_reporte(root, args.umbral_dias, fecha_hoy, aplicar=args.aplicar)

    print(
        "F2_VALIDAR_ACTUALIZAR_MERCADO_v01 — {vencidos} de {total} archivos vencidos "
        "(umbral {umbral} dias)".format(
            vencidos=reporte["vencidos"],
            total=reporte["total_archivos"],
            umbral=args.umbral_dias,
        )
    )
    for r in reporte["archivos"]:
        estado = "VENCIDO" if r["vencido"] else ("fresco" if r["valido"] else "INVALIDO")
        print(
            "  [{estado}] {chip} | fecha={fecha} | dias={dias} | {ruta}".format(
                estado=estado,
                chip=r["chip"] or "?",
                fecha=r["fecha_datos"] or "-",
                dias=r["dias_transcurridos"] if r["dias_transcurridos"] is not None else "-",
                ruta=r["ruta"],
            )
        )
    print("  Reporte: {0}".format(reporte["ruta_reporte"]))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
