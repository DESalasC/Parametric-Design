#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
F2_DISPARAR_RECAPTURA_MERCADO_v01.py — Validador y disparador de recaptura de
mercado inmobiliario para la Fase 2 (DisenoParametrico).
Proyecto: DisenoParametrico — Fase 2
Python 3.12 (stdlib). Type hints.

v01.0 (2026-11-06): version inicial.

OBJETIVO:
  Ejecutarse al arrancar el Orquestador web (servidor.py) y, opcionalmente, bajo
  demanda. Valida la vigencia de la informacion inmobiliaria de F2 (precios de
  venta, costos de construccion, canon de arriendo) y, si esta vencida (>
  umbral, default 14 dias), dispara la recaptura automatica desde las fuentes
  documentadas sin intervention humana cuando es posible.

ALCANCE Y NIVELES DE AUTOMATIZACION:

  NIVEL 1 (automatico, sin intervention humana):
    - Validar vigencia contra meta.fecha_ejecucion / meta.mercado.fecha_captura_origen
      / meta.sync.fecha_sync de cada archivo de mercado de F2.
    - Sincronizar (copiar) el export ya procesado de MercadoViviendaBogota hacia
      DisenoParametrico mediante F2_SINCRONIZAR_MERCADO_v01.py.
    - Regenerar los exports de MVB desde capturas crudas existentes con
      F4_INTEGRADOR_v01.py --mes <YYYY-MM> (lectura de data/raw ya capturada;
      no requiere navegador).

  NIVEL 2 (requiere fuente externa / posible intervention humana):
    - Si MVB no tiene capturas crudas para el mes vigente, la recaptura desde
      portales (Ciencuadras, Fincaraiz, La Haus, etc.) requiere navegador Edge
      y, en portales SPA (Ciencuadras), clic humano para paginacion profunda.
      En ese caso el script genera un pendiente_mercado.json y devuelve codigo
      de salida 2 para que el operador ejecute la captura manual en MVB.

ARCHIVOS INSPECCIONADOS (DisenoParametrico):
  - data/fase-2-demanda/mercado/parametros_*_f2mercado_*.json
  - src/fase-2-demanda/F2_Modelo_Financiero/parametros_entrada.json
  - src/fase-2-demanda/F2_Modelo_Renta/parametros_entrada.json
  - src/orquestador/parametros_pipeline.json (chip por defecto)

ENTORNO (MercadoViviendaBogota, proyecto externo):
  - D:\Work\PROJECTS\MercadoViviendaBogota\scripts\F4_INTEGRADOR_v01.py
  - D:\Work\PROJECTS\MercadoViviendaBogota\scripts\append_run.py
  - D:\Work\PROJECTS\MercadoViviendaBogota\data\raw\<fecha>\  (capturas crudas)

SALIDAS:
  - data/fase-2-demanda/mercado/reporte_recaptura_mercado.json  (ejecucion)
  - data/fase-2-demanda/mercado/pendiente_mercado.json          (solo si NIVEL 2)
  - Banderas meta.estado_vigencia en archivos vencidos (cuando --aplicar).

VARIABLES DE ENTORNO:
  DISENO_PARAMETRICO_ROOT: raiz de DP (default: calculada desde este archivo).
  MERCADO_VIVIENDA_BOGOTA_ROOT: raiz de MVB (default: D:\Work\PROJECTS\MercadoViviendaBogota).

USO:
  python F2_DISPARAR_RECAPTURA_MERCADO_v01.py
  python F2_DISPARAR_RECAPTURA_MERCADO_v01.py --umbral-dias 14 --aplicar
  python F2_DISPARAR_RECAPTURA_MERCADO_v01.py --chip AAA0030JKOE --mes 2026-11
  python F2_DISPARAR_RECAPTURA_MERCADO_v01.py --solo-validar

CODIGOS DE SALIDA:
  0 = todo vigente o sincronizado correctamente (NIVEL 1 OK).
  1 = error de ejecucion.
  2 = vencido y sin export fresco en MVB: requiere recaptura manual en portales
      (NIVEL 2). Se genera pendiente_mercado.json.
"""

from __future__ import annotations

import argparse
import datetime
import io
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any

# ----------------------------------------------------------------------------
# Rutas y constantes
# ----------------------------------------------------------------------------

DEFAULT_UMBRAL_DIAS = 14
DEFAULT_MVB_ROOT = r"D:\Work\PROJECTS\MercadoViviendaBogota"

REPORTE_NOMBRE = "reporte_recaptura_mercado.json"
PENDIENTE_NOMBRE = "pendiente_mercado.json"

_F2_ARCHIVOS = (
    "data/fase-2-demanda/mercado/parametros_*_f2mercado_*.json",
    "src/fase-2-demanda/F2_Modelo_Financiero/parametros_entrada.json",
    "src/fase-2-demanda/F2_Modelo_Renta/parametros_entrada.json",
)

_PIPELINE_REL = "src/orquestador/parametros_pipeline.json"


def _raiz_dp() -> Path:
    env_root = os.environ.get("DISENO_PARAMETRICO_ROOT")
    if env_root:
        return Path(env_root)
    return Path(__file__).resolve().parents[3]  # src/fase-2-demanda -> raiz


def _raiz_mvb() -> Path:
    env_root = os.environ.get("MERCADO_VIVIENDA_BOGOTA_ROOT")
    if env_root:
        return Path(env_root)
    return Path(DEFAULT_MVB_ROOT)


def _python_exe() -> str:
    """Intenta el .venv de DP, luego sys.executable."""
    venv = _raiz_dp() / ".venv" / "Scripts" / "python.exe"
    if venv.exists():
        return str(venv)
    return sys.executable


def _leer_json(ruta: Path) -> dict[str, Any] | None:
    try:
        with io.open(ruta, "r", encoding="utf-8") as fh:
            return json.load(fh)
    except Exception:
        return None


def _chip_por_defecto(root: Path) -> str | None:
    p = root / _PIPELINE_REL
    d = _leer_json(p)
    if d and d.get("chip"):
        return str(d["chip"])
    return None


def _fecha_mas_reciente(datos: dict[str, Any]) -> str | None:
    """Fecha mas reciente disponible en metadatos (YYYY-MM-DD)."""
    fechas: list[str] = []
    meta = datos.get("meta") or {}
    for clave in ("fecha_ejecucion", "fecha_captura", "fecha_captura_origen", "fecha_sync"):
        v = meta.get(clave)
        if isinstance(v, str) and len(v) >= 10:
            fechas.append(v[:10])
    mercado = meta.get("mercado") or {}
    for clave in ("fecha_captura", "fecha_captura_origen", "fecha_sync"):
        v = mercado.get(clave)
        if isinstance(v, str) and len(v) >= 10:
            fechas.append(v[:10])
    validas: list[str] = []
    for f in fechas:
        try:
            datetime.date.fromisoformat(f)
            validas.append(f)
        except ValueError:
            continue
    return max(validas) if validas else None


def _dias_transcurridos(fecha_str: str, hoy: datetime.date) -> int | None:
    try:
        return (hoy - datetime.date.fromisoformat(fecha_str[:10])).days
    except ValueError:
        return None


# ----------------------------------------------------------------------------
# Validacion de vigencia (reutiliza logica de F2_VALIDAR_ACTUALIZAR_MERCADO_v01
# sin importarla para mantener acoplamiento bajo)
# ----------------------------------------------------------------------------

def validar_archivo(ruta: Path, umbral_dias: int, hoy: datetime.date) -> dict[str, Any]:
    res: dict[str, Any] = {
        "ruta": str(ruta),
        "existe": True,
        "valido": False,
        "fecha_datos": None,
        "dias_transcurridos": None,
        "vencido": False,
        "error": None,
    }
    datos = _leer_json(ruta)
    if datos is None:
        res["error"] = "JSON ilegible o vacio"
        return res
    fecha = _fecha_mas_reciente(datos)
    res["fecha_datos"] = fecha
    if fecha is None:
        res["error"] = "sin fecha de referencia en metadatos"
        return res
    dias = _dias_transcurridos(fecha, hoy)
    res["dias_transcurridos"] = dias
    res["vencido"] = bool(dias is not None and dias > umbral_dias)
    res["valido"] = True
    return res


def validar_todos(root: Path, umbral_dias: int, hoy: datetime.date) -> list[dict[str, Any]]:
    """Valida todos los archivos de mercado de F2 bajo la raiz del proyecto.

    Recorre los patrones de _F2_ARCHIVOS usando root.glob() directamente,
    que es la forma simple y correcta de expandir patrones con comodines.
    """
    resultados: list[dict[str, Any]] = []
    for patron in _F2_ARCHIVOS:
        for p in sorted(root.glob(patron)):
            if p.is_file():
                resultados.append(validar_archivo(p, umbral_dias, hoy))
    # deduplicar por ruta
    vistos: set[str] = set()
    unicos: list[dict[str, Any]] = []
    for r in resultados:
        if r["ruta"] not in vistos:
            vistos.add(r["ruta"])
            unicos.append(r)
    return unicos


# ----------------------------------------------------------------------------
# Acciones de recaptura (niveles 1 y 2)
# ----------------------------------------------------------------------------

def _ejecutar(cmd: list[str], cwd: str | None = None, timeout: int = 600) -> dict[str, Any]:
    """Ejecuta un comando y devuelve {ok, codigo, salida}."""
    try:
        proc = subprocess.run(
            cmd, cwd=cwd, capture_output=True, text=True,
            encoding="utf-8", errors="replace", timeout=timeout,
        )
        salida = ((proc.stdout or "") + (proc.stderr or "")).strip()
        return {"ok": proc.returncode == 0, "codigo": proc.returncode, "salida": salida[-2000:]}
    except Exception as ex:
        return {"ok": False, "codigo": -1, "salida": "ERROR: " + str(ex)}


def sincronizar_desde_mvb(root: Path, mvb_root: Path, chip: str) -> dict[str, Any]:
    """NIVEL 1: copia el export de MVB hacia DP usando F2_SINCRONIZAR_MERCADO_v01.py."""
    script = root / "src" / "orquestador" / "F2_SINCRONIZAR_MERCADO_v01.py"
    if not script.exists():
        return {"ok": False, "accion": "sincronizar_mvb", "detalle": "script no encontrado: " + str(script)}
    py = _python_exe()
    res = _ejecutar([py, str(script), "--chip", chip, "--forzar"], cwd=str(root))
    return {"ok": res["ok"], "accion": "sincronizar_mvb", "chip": chip, "detalle": res["salida"], "codigo": res["codigo"]}


def regenerar_exports_mvb(mvb_root: Path, mes: str) -> dict[str, Any]:
    """NIVEL 1: regenera exports de MVB desde capturas crudas existentes (sin navegador)."""
    script = mvb_root / "scripts" / "F4_INTEGRADOR_v01.py"
    if not script.exists():
        return {"ok": False, "accion": "regenerar_exports_mvb", "detalle": "script no encontrado: " + str(script)}
    py = _python_exe()
    res = _ejecutar([py, str(script), "--mes", mes], cwd=str(mvb_root))
    return {"ok": res["ok"], "accion": "regenerar_exports_mvb", "mes": mes, "detalle": res["salida"], "codigo": res["codigo"]}


def generar_pendiente_nivel2(root: Path, chip: str, vencidos: list[dict[str, Any]], hoy: datetime.date) -> Path:
    """NIVEL 2: escribe pendiente_mercado.json para recaptura manual en portales."""
    dir_mercado = root / "data" / "fase-2-demanda" / "mercado"
    dir_mercado.mkdir(parents=True, exist_ok=True)
    ruta = dir_mercado / PENDIENTE_NOMBRE
    pendiente = {
        "fecha": hoy.isoformat(),
        "chip": chip,
        "estado": "RECAPTURA_PENDIENTE_NIVEL2",
        "motivo": "sin export fresco en MercadoViviendaBogota; requiere recaptura desde portales",
        "archivos_vencidos": vencidos,
        "fuentes_documentadas": [
            "metrocuadrado", "fincaraiz", "properati", "ciencuadras", "lahaus",
            "galeria_inmobiliaria_sdh", "coordenada_inmobiliaria", "dane_ipvn", "lonja_bogota", "curadurias_urbanas",
        ],
        "nota": "La recaptura desde portales vive en MercadoViviendaBogota (D:\\Work\\PROJECTS\\MercadoViviendaBogota). "
                "Fincaraiz y La Haus capturan via GET directo (JSON embebido); Ciencuadras es SPA Angular y su "
                "paginacion profunda requiere navegador Edge + clic humano (documentado en acta 2026-08-25).",
    }
    with io.open(ruta, "w", encoding="utf-8") as fh:
        json.dump(pendiente, fh, ensure_ascii=False, indent=2)
    return ruta


# ----------------------------------------------------------------------------
# Orquestador principal
# ----------------------------------------------------------------------------

def disparar(
    root: Path,
    mvb_root: Path,
    umbral_dias: int,
    aplicar: bool,
    chip: str | None,
    mes: str | None,
    solo_validar: bool,
    hoy: datetime.date,
) -> dict[str, Any]:
    """Ejecuta el ciclo validador + disparador. Devuelve el reporte completo."""
    if chip is None:
        chip = _chip_por_defecto(root) or "AAA0030JKOE"

    archivos = validar_todos(root, umbral_dias, hoy)
    vencidos = [a for a in archivos if a["vencido"]]
    frescos = [a for a in archivos if a["valido"] and not a["vencido"]]
    invalidos = [a for a in archivos if not a["valido"]]

    reporte: dict[str, Any] = {
        "fecha": hoy.isoformat(),
        "chip": chip,
        "umbral_dias": umbral_dias,
        "total_archivos": len(archivos),
        "vencidos": len(vencidos),
        "frescos": len(frescos),
        "invalidos": len(invalidos),
        "archivos": archivos,
        "acciones": [],
        "nivel_alcanzado": 0,
        "codigo_salida": 0,
    }

    if solo_validar:
        reporte["nivel_alcanzado"] = 0
        reporte["codigo_salida"] = 0 if not vencidos else 2
        return reporte

    if not vencidos:
        reporte["acciones"].append({
            "accion": "validar_vigencia",
            "detalle": "Todos los archivos de mercado estan dentro del umbral de {0} dias.".format(umbral_dias),
        })
        reporte["nivel_alcanzado"] = 1
        return reporte

    # Hay vencidos: NIVEL 1 - intentar sincronizar desde MVB
    act = sincronizar_desde_mvb(root, mvb_root, chip)
    reporte["acciones"].append(act)

    if act["ok"]:
        # Revalidar despues de sincronizar
        archivos_post = validar_todos(root, umbral_dias, hoy)
        vencidos_post = [a for a in archivos_post if a["vencido"]]
        reporte["archivos_post_sincronizacion"] = archivos_post
        reporte["vencidos_despues"] = len(vencidos_post)
        if not vencidos_post:
            reporte["nivel_alcanzado"] = 1
            reporte["codigo_salida"] = 0
            reporte["acciones"].append({
                "accion": "sincronizacion_ok",
                "detalle": "Export de MVB sincronizado; vigencia restaurada para el chip {0}.".format(chip),
            })
            return reporte
        # Sincronizado pero todavia vencido: intentar regenerar exports de MVB desde capturas crudas
        if mes is None:
            mes = hoy.strftime("%Y-%m")
        regen = regenerar_exports_mvb(mvb_root, mes)
        reporte["acciones"].append(regen)
        if regen["ok"]:
            act2 = sincronizar_desde_mvb(root, mvb_root, chip)
            reporte["acciones"].append(act2)
            archivos_post2 = validar_todos(root, umbral_dias, hoy)
            vencidos_post2 = [a for a in archivos_post2 if a["vencido"]]
            reporte["archivos_post_regeneracion"] = archivos_post2
            reporte["vencidos_despues_regeneracion"] = len(vencidos_post2)
            if not vencidos_post2:
                reporte["nivel_alcanzado"] = 1
                reporte["codigo_salida"] = 0
                reporte["acciones"].append({
                    "accion": "regeneracion_ok",
                    "detalle": "Exports de MVB regenerados desde capturas crudas y sincronizados.",
                })
                return reporte

    # Si llegamos aqui, NIVEL 1 no alcanzo: NIVEL 2 (pendiente para captura manual en portales)
    if mes is None:
        mes = hoy.strftime("%Y-%m")
    ruta_pendiente = generar_pendiente_nivel2(root, chip, vencidos, hoy)
    reporte["pendiente_nivel2"] = str(ruta_pendiente)
    reporte["nivel_alcanzado"] = 2
    reporte["codigo_salida"] = 2
    reporte["acciones"].append({
        "accion": "pendiente_nivel2",
        "detalle": "Recaptura pendiente en MercadoViviendaBogota desde portales (nivel 2). Ver {0}.".format(ruta_pendiente),
    })

    # Aplicar banderas de vencimiento en los archivos de DP
    if aplicar:
        dir_mercado = root / "data" / "fase-2-demanda" / "mercado"
        dir_mercado.mkdir(parents=True, exist_ok=True)
        for a in vencidos:
            p = Path(a["ruta"])
            datos = _leer_json(p)
            if datos is not None:
                meta = datos.setdefault("meta", {})
                meta["estado_vigencia"] = "VENCIDO"
                meta["requiere_actualizacion_mercado"] = True
                meta["umbral_dias_validacion"] = umbral_dias
                meta["fecha_validacion"] = hoy.isoformat()
                meta["dias_transcurridos_validacion"] = a["dias_transcurridos"]
                try:
                    with io.open(p, "w", encoding="utf-8") as fh:
                        json.dump(datos, fh, ensure_ascii=False, indent=2)
                except Exception:
                    pass

    # Escribir reporte
    dir_mercado = root / "data" / "fase-2-demanda" / "mercado"
    dir_mercado.mkdir(parents=True, exist_ok=True)
    ruta_reporte = dir_mercado / REPORTE_NOMBRE
    with io.open(ruta_reporte, "w", encoding="utf-8") as fh:
        json.dump(reporte, fh, ensure_ascii=False, indent=2)
    reporte["ruta_reporte"] = str(ruta_reporte)
    return reporte


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Valida vigencia del mercado F2 y dispara recaptura automatica si está vencido."
    )
    parser.add_argument("--chip", default=None, help="CHIP del lote (default: el de parametros_pipeline.json).")
    parser.add_argument("--mes", default=None, help="Mes para regenerar exports en MVB (YYYY-MM). Default: mes actual.")
    parser.add_argument("--umbral-dias", type=int, default=DEFAULT_UMBRAL_DIAS, help=f"Umbral de vigencia en dias (default {DEFAULT_UMBRAL_DIAS}).")
    parser.add_argument("--aplicar", action="store_true", help="Escribe banderas de vencimiento en archivos de DP vencidos.")
    parser.add_argument("--solo-validar", action="store_true", help="Solo valida y reporta, no dispara recaptura.")
    args = parser.parse_args()

    root = _raiz_dp()
    mvb_root = _raiz_mvb()
    hoy = datetime.date.today()

    reporte = disparar(
        root=root,
        mvb_root=mvb_root,
        umbral_dias=args.umbral_dias,
        aplicar=args.aplicar,
        chip=args.chip,
        mes=args.mes,
        solo_validar=args.solo_validar,
        hoy=hoy,
    )

    print("F2_DISPARAR_RECAPTURA_MERCADO_v01 — chip {chip} | vencidos {vencidos}/{total} | nivel {nivel} | salida {codigo}".format(
        chip=reporte["chip"],
        vencidos=reporte["vencidos"],
        total=reporte["total_archivos"],
        nivel=reporte["nivel_alcanzado"],
        codigo=reporte["codigo_salida"],
    ))
    for a in reporte["acciones"]:
        print("  [{accion}] {detalle}".format(accion=a["accion"], detalle=a["detalle"][:200]))
    if reporte.get("ruta_reporte"):
        print("  Reporte: {0}".format(reporte["ruta_reporte"]))
    if reporte.get("pendiente_nivel2"):
        print("  Pendiente N2: {0}".format(reporte["pendiente_nivel2"]))

    return reporte["codigo_salida"]


if __name__ == "__main__":
    raise SystemExit(main())
