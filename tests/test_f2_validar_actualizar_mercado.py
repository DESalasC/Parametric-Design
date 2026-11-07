# -*- coding: utf-8 -*-
"""
Tests de F2_VALIDAR_ACTUALIZAR_MERCADO_v01 — Validación de vigencia del
mercado inmobiliario (Fase 2).

Ejecutar:  pytest tests/test_f2_validar_actualizar_mercado.py -v
"""
import json
import os
import sys
from datetime import date, timedelta
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
F2_DIR = PROJECT_ROOT / "src" / "fase-2-demanda"
sys.path.insert(0, str(F2_DIR))

import pytest

import F2_VALIDAR_ACTUALIZAR_MERCADO_v01 as validador


def _escribir_json(ruta: Path, datos: dict) -> None:
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_text(json.dumps(datos, ensure_ascii=False, indent=2), encoding="utf-8")


def _hace_dias(dias: int) -> str:
    return (date.today() - timedelta(days=dias)).isoformat()


# ---------------------------------------------------------------
# Validación de un archivo individual
# ---------------------------------------------------------------

def test_archivo_vencido_sobre_umbral(tmp_path: Path):
    """Fecha de 30 dias atrás con umbral 14 -> vencido."""
    ruta = tmp_path / "parametros_CHIPX_f2mercado_2026-09.json"
    _escribir_json(ruta, {"meta": {"fecha_ejecucion": _hace_dias(30)}})
    res = validador.validar_archivo(ruta, umbral_dias=14, fecha_hoy=date.today())
    assert res["valido"] is True
    assert res["vencido"] is True
    assert res["dias_transcurridos"] == 30


def test_archivo_fresco_dentro_umbral(tmp_path: Path):
    """Fecha de 5 días atrás con umbral 14 -> fresco."""
    ruta = tmp_path / "parametros_CHIPY_f2mercado_2026-09.json"
    _escribir_json(ruta, {"meta": {"fecha_ejecucion": _hace_dias(5)}})
    res = validador.validar_archivo(ruta, umbral_dias=14, fecha_hoy=date.today())
    assert res["vencido"] is False


def test_umbral_personalizado(tmp_path: Path):
    """Umbral 60, fecha de 30 días atrás -> fresco."""
    ruta = tmp_path / "parametros_CHIPZ_f2mercado_2026-09.json"
    _escribir_json(ruta, {"meta": {"fecha_ejecucion": _hace_dias(30)}})
    res = validador.validar_archivo(ruta, umbral_dias=60, fecha_hoy=date.today())
    assert res["vencido"] is False


def test_sin_fecha_es_invalido(tmp_path: Path):
    ruta = tmp_path / "parametros_SINFECHA.json"
    _escribir_json(ruta, {"meta": {}})
    res = validador.validar_archivo(ruta, umbral_dias=14, fecha_hoy=date.today())
    assert res["valido"] is False
    assert res["vencido"] is False
    assert res["error"] is not None


def test_extrae_fecha_mas_reciente(tmp_path: Path):
    """Si hay varias fechas, toma la más reciente."""
    ruta = tmp_path / "parametros_MULTI.json"
    _escribir_json(ruta, {
        "meta": {
            "fecha_ejecucion": _hace_dias(10),
            "fecha_sync": _hace_dias(2),
        },
        "mercado": {
            "fecha_captura_origen": _hace_dias(20),
        },
    })
    res = validador.validar_archivo(ruta, umbral_dias=14, fecha_hoy=date.today())
    assert res["fecha_datos"] == _hace_dias(2)
    assert res["vencido"] is False


# ---------------------------------------------------------------
# Generación de reporte
# ---------------------------------------------------------------

def _setup_raiz_temporal(tmp_path: Path, archivos: dict[str, dict]) -> Path:
    """Crea la estructura data/fase-2-demanda/mercado bajo una raíz temporal
    y escribe los archivos indicados. Devuelve la raíz."""
    root = tmp_path / "root"
    dir_mercado = root / "data" / "fase-2-demanda" / "mercado"
    dir_mercado.mkdir(parents=True)
    for nombre, datos in archivos.items():
        _escribir_json(dir_mercado / nombre, datos)
    return root


def test_generar_reporte_contabiliza_vencidos(tmp_path: Path):
    """El reporte conta vencidos y frescos correctamente."""
    hoy = date.today()
    root = _setup_raiz_temporal(tmp_path, {
        "parametros_VENC_f2mercado_2026-09.json": {"meta": {"fecha_ejecucion": _hace_dias(30)}},
        "parametros_FRE_f2mercado_2026-09.json": {"meta": {"fecha_ejecucion": _hace_dias(3)}},
    })

    anterior = os.environ.get("DISENO_PARAMETRICO_ROOT")
    os.environ["DISENO_PARAMETRICO_ROOT"] = str(root)
    try:
        reporte = validador.generar_reporte(root, umbral_dias=14, fecha_hoy=hoy, aplicar=False)
    finally:
        if anterior is None:
            os.environ.pop("DISENO_PARAMETRICO_ROOT", None)
        else:
            os.environ["DISENO_PARAMETRICO_ROOT"] = anterior

    assert reporte["total_archivos"] == 2
    assert reporte["vencidos"] == 1
    assert reporte["frescos"] == 1
    assert reporte["umbral_dias"] == 14
    assert (root / "data" / "fase-2-demanda" / "mercado" / "reporte_vigencia_mercado.json").exists()


def test_aplicar_escribe_bandera_vencido(tmp_path: Path):
    """--aplicar escribe estado_vigencia VENCIDO en archivos vencidos."""
    root = _setup_raiz_temporal(tmp_path, {
        "parametros_APLICA_f2mercado_2026-09.json": {
            "meta": {"fecha_ejecucion": _hace_dias(40), "chip": "APLICA"}
        },
    })

    anterior = os.environ.get("DISENO_PARAMETRICO_ROOT")
    os.environ["DISENO_PARAMETRICO_ROOT"] = str(root)
    try:
        reporte = validador.generar_reporte(root, umbral_dias=14, fecha_hoy=date.today(), aplicar=True)
    finally:
        if anterior is None:
            os.environ.pop("DISENO_PARAMETRICO_ROOT", None)
        else:
            os.environ["DISENO_PARAMETRICO_ROOT"] = anterior

    ruta = root / "data" / "fase-2-demanda" / "mercado" / "parametros_APLICA_f2mercado_2026-09.json"
    datos = json.loads(ruta.read_text(encoding="utf-8"))
    assert datos["meta"]["estado_vigencia"] == "VENCIDO"
    assert datos["meta"]["requiere_actualizacion_mercado"] is True
    assert reporte["vencidos"] == 1
