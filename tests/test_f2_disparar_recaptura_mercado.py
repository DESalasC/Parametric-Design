# -*- coding: utf-8 -*-
"""
Tests de F2_DISPARAR_RECAPTURA_MERCADO_v01 — Validador y disparador de
recaptura de mercado (Fase 2).

Ejecutar:  pytest tests/test_f2_disparar_recaptura_mercado.py -v
"""
import datetime
import io
import json
import os
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
F2_DIR = PROJECT_ROOT / "src" / "fase-2-demanda"
sys.path.insert(0, str(F2_DIR))

import pytest

import F2_DISPARAR_RECAPTURA_MERCADO_v01 as disparador


def _escribir_json(ruta: Path, datos: dict) -> None:
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_text(json.dumps(datos, ensure_ascii=False, indent=2), encoding="utf-8")


def _hace_dias(dias: int) -> str:
    return (datetime.date.today() - datetime.timedelta(days=dias)).isoformat()


def _setup_raices(tmp_path: Path, archivos_dp: dict[str, dict]) -> tuple[Path, Path]:
    """Crea raiz DP y raiz MVB temporales con los archivos de DP indicados.
    Devuelve (root_dp, root_mvb)."""
    root_dp = tmp_path / "dp"
    root_mvb = tmp_path / "mvb"
    for rel, datos in archivos_dp.items():
        _escribir_json(root_dp / rel, datos)
    # Estructura minima de MVB (sin capturas crudas)
    (root_mvb / "scripts").mkdir(parents=True, exist_ok=True)
    return root_dp, root_mvb


def _poner_env(root_dp: Path, root_mvb: Path, monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setenv("DISENO_PARAMETRICO_ROOT", str(root_dp))
    monkeypatch.setenv("MERCADO_VIVIENDA_BOGOTA_ROOT", str(root_mvb))


# ---------------------------------------------------------------
# Validacion de archivo individual
# ---------------------------------------------------------------

def test_validar_archivo_vencido(tmp_path: Path):
    ruta = tmp_path / "parametros_X_f2mercado_2026-09.json"
    _escribir_json(ruta, {"meta": {"fecha_ejecucion": _hace_dias(30)}})
    res = disparador.validar_archivo(ruta, umbral_dias=14, hoy=datetime.date.today())
    assert res["valido"] is True
    assert res["vencido"] is True
    assert res["dias_transcurridos"] == 30


def test_validar_archivo_fresco(tmp_path: Path):
    ruta = tmp_path / "parametros_Y_f2mercado_2026-09.json"
    _escribir_json(ruta, {"meta": {"fecha_ejecucion": _hace_dias(3)}})
    res = disparador.validar_archivo(ruta, umbral_dias=14, hoy=datetime.date.today())
    assert res["vencido"] is False


def test_validar_archivo_sin_fecha(tmp_path: Path):
    ruta = tmp_path / "parametros_SF.json"
    _escribir_json(ruta, {"meta": {}})
    res = disparador.validar_archivo(ruta, umbral_dias=14, hoy=datetime.date.today())
    assert res["valido"] is False
    assert res["vencido"] is False
    assert res["error"] is not None


# ---------------------------------------------------------------
# Validacion de todos los archivos de DP
# ---------------------------------------------------------------

def test_validar_todos_conta_vencidos(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    root_dp = tmp_path / "dp"
    dir_mercado = root_dp / "data" / "fase-2-demanda" / "mercado"
    dir_mercado.mkdir(parents=True)
    _escribir_json(dir_mercado / "parametros_VEN_f2mercado_2026-09.json", {"meta": {"fecha_ejecucion": _hace_dias(30)}})
    _escribir_json(dir_mercado / "parametros_FRE_f2mercado_2026-09.json", {"meta": {"fecha_ejecucion": _hace_dias(3)}})
    fin_dir = root_dp / "src" / "fase-2-demanda" / "F2_Modelo_Financiero"
    fin_dir.mkdir(parents=True)
    _escribir_json(fin_dir / "parametros_entrada.json", {"meta": {"fecha_ejecucion": _hace_dias(86)}})

    monkeypatch.setenv("DISENO_PARAMETRICO_ROOT", str(root_dp))
    hoy = datetime.date.today()
    resultados = disparador.validar_todos(root_dp, umbral_dias=14, hoy=hoy)
    vencidos = [r for r in resultados if r["vencido"]]
    frescos = [r for r in resultados if r["valido"] and not r["vencido"]]
    assert len(resultados) == 3
    assert len(vencidos) == 2  # VEN (30d) + entrada financiero (86d)
    assert len(frescos) == 1   # FRE (3d)


# ---------------------------------------------------------------
# Pendiente Nivel 2
# ---------------------------------------------------------------

def test_generar_pendiente_nivel2_escribe_json(tmp_path: Path):
    root_dp = tmp_path / "dp"
    hoy = datetime.date.today()
    vencidos = [
        {"ruta": "x/parametros_A.json", "fecha_datos": "2026-08-01", "dias_transcurridos": 90, "vencido": True},
    ]
    ruta = disparador.generar_pendiente_nivel2(root_dp, "CHIPX", vencidos, hoy)
    assert ruta.exists()
    datos = json.loads(ruta.read_text(encoding="utf-8"))
    assert datos["estado"] == "RECAPTURA_PENDIENTE_NIVEL2"
    assert datos["chip"] == "CHIPX"
    assert len(datos["archivos_vencidos"]) == 1


# ---------------------------------------------------------------
# Disparar completo (solo_validar)
# ---------------------------------------------------------------

def test_disparar_solo_validar_con_vencidos(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    root_dp, root_mvb = _setup_raices(tmp_path, {
        "data/fase-2-demanda/mercado/parametros_VEN_f2mercado_2026-09.json": {
            "meta": {"fecha_ejecucion": _hace_dias(30)}
        },
    })
    _poner_env(root_dp, root_mvb, monkeypatch)

    reporte = disparador.disparar(
        root=root_dp, mvb_root=root_mvb, umbral_dias=14, aplicar=False,
        chip="CHIPX", mes="2026-09", solo_validar=True, hoy=datetime.date.today(),
    )
    assert reporte["total_archivos"] == 1
    assert reporte["vencidos"] == 1
    assert reporte["frescos"] == 0
    assert reporte["nivel_alcanzado"] == 0
    assert reporte["codigo_salida"] == 2  # vencido y solo_validar -> 2


def test_disparar_solo_validar_sin_vencidos(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    root_dp, root_mvb = _setup_raices(tmp_path, {
        "data/fase-2-demanda/mercado/parametros_FRE_f2mercado_2026-09.json": {
            "meta": {"fecha_ejecucion": _hace_dias(3)}
        },
    })
    _poner_env(root_dp, root_mvb, monkeypatch)

    reporte = disparador.disparar(
        root=root_dp, mvb_root=root_mvb, umbral_dias=14, aplicar=False,
        chip="CHIPX", mes="2026-09", solo_validar=True, hoy=datetime.date.today(),
    )
    assert reporte["vencidos"] == 0
    assert reporte["codigo_salida"] == 0


# ---------------------------------------------------------------
# Disparar completo con stubs de scripts (subprocess real)
# ---------------------------------------------------------------

def _crear_stub(ruta: Path, contenido_salida: str = "OK") -> None:
    """Crea un script Python stub que imprime y sale con codigo 0."""
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_text(
        'import sys\nprint("{0}")\nsys.exit(0)\n'.format(contenido_salida),
        encoding="utf-8",
    )


def test_disparar_completo_nivel2_pendiente(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    """Archivos vencidos + stubs de scripts (que salen ok pero no modifican
    los archivos) => NIVEL 2, pendiente generado, codigo 2."""
    hoy = datetime.date.today()
    root_dp, root_mvb = _setup_raices(tmp_path, {
        "data/fase-2-demanda/mercado/parametros_VEN_f2mercado_2026-09.json": {
            "meta": {"fecha_ejecucion": _hace_dias(30)}
        },
        "src/fase-2-demanda/F2_Modelo_Financiero/parametros_entrada.json": {
            "meta": {"fecha_ejecucion": _hace_dias(86)}
        },
        "src/fase-2-demanda/F2_Modelo_Renta/parametros_entrada.json": {
            "meta": {"fecha_ejecucion": _hace_dias(85)}
        },
        "src/orquestador/parametros_pipeline.json": {"chip": "AAA0030JKOE"},
    })
    # Stubs de los scripts de sincronizacion y regeneracion (subprocess los invoca)
    _crear_stub(root_dp / "src" / "orquestador" / "F2_SINCRONIZAR_MERCADO_v01.py")
    _crear_stub(root_mvb / "scripts" / "F4_INTEGRADOR_v01.py")

    _poner_env(root_dp, root_mvb, monkeypatch)

    reporte = disparador.disparar(
        root=root_dp, mvb_root=root_mvb, umbral_dias=14, aplicar=False,
        chip="AAA0030JKOE", mes=hoy.strftime("%Y-%m"), solo_validar=False, hoy=hoy,
    )
    assert reporte["vencidos"] == 3
    assert reporte["nivel_alcanzado"] == 2
    assert reporte["codigo_salida"] == 2
    assert reporte.get("pendiente_nivel2") is not None
    acciones = [a["accion"] for a in reporte["acciones"]]
    assert "sincronizar_mvb" in acciones
    assert "regenerar_exports_mvb" in acciones
    assert "pendiente_nivel2" in acciones


def test_disparar_completo_sin_vencidos_codigo_cero(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    """Todos los archivos frescos => NIVEL 1, codigo 0, sin acciones de recaptura."""
    hoy = datetime.date.today()
    root_dp, root_mvb = _setup_raices(tmp_path, {
        "data/fase-2-demanda/mercado/parametros_FRE_f2mercado_2026-09.json": {
            "meta": {"fecha_ejecucion": _hace_dias(3)}
        },
    })
    _poner_env(root_dp, root_mvb, monkeypatch)

    reporte = disparador.disparar(
        root=root_dp, mvb_root=root_mvb, umbral_dias=14, aplicar=False,
        chip="CHIPX", mes=hoy.strftime("%Y-%m"), solo_validar=False, hoy=hoy,
    )
    assert reporte["vencidos"] == 0
    assert reporte["nivel_alcanzado"] == 1
    assert reporte["codigo_salida"] == 0
    assert len(reporte["acciones"]) == 1
    assert reporte["acciones"][0]["accion"] == "validar_vigencia"
