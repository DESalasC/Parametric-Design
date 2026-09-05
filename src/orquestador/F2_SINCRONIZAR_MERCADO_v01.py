#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
F2_SINCRONIZAR_MERCADO_v01.py - Paso de integracion MercadoViviendaBogota -> DisenoParametrico.

Valida y copia (SOLO LECTURA del origen) el archivo de parametros de mercado
generado por el integrador F4 de MercadoViviendaBogota:

    D:\\Work\\PROJECTS\\MercadoViviendaBogota\\data\\normalized\\fase2_export\\parametros_f2\\parametros_<CHIP>_f2mercado_<YYYY-MM>.json

hacia la zona de aterrizaje de DisenoParametrico:

    data\\fase-2-demanda\\mercado\\parametros_<CHIP>_f2mercado_<YYYY-MM>.json

Los orquestadores (servidor.py y run_pipeline_v01.py) prefieren ese archivo
si esta fresco (<= 60 dias desde la captura de origen); si no, caen a los
parametros curados del proyecto (fallback retrocompatible).

Uso:
    python F2_SINCRONIZAR_MERCADO_v01.py                                  # chip de parametros_pipeline.json
    python F2_SINCRONIZAR_MERCADO_v01.py --chip AAA0127AZPA
    python F2_SINCRONIZAR_MERCADO_v01.py --chip AAA0127AZPA --listar
    python F2_SINCRONIZAR_MERCADO_v01.py --chip AAA0127AZPA --forzar      # copia aunque este vencido

Reglas:
- NUNCA escribe dentro de MercadoViviendaBogota (su historico es append-only).
- Valida claves minimas antes de copiar (meta.mercado + escenarios con precios).
- Exit codes: 0 OK | 2 vencido (no copiado sin --forzar) | 3 sin export | 4 export invalido.

Requisito: Python 3.8+ (stdlib). Corre igual en la .venv 3.12 de DisenoParametrico
o en el python del sistema 3.13.
"""
import argparse
import datetime
import glob
import io
import json
import os
import shutil
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
MVB_ROOT = r"D:\Work\PROJECTS\MercadoViviendaBogota"
DIR_ORIGEN = os.path.join(MVB_ROOT, "data", "normalized", "fase2_export", "parametros_f2")
DIR_ATERRIZAJE = os.path.join(ROOT, "data", "fase-2-demanda", "mercado")
PARAM_PIPELINE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "parametros_pipeline.json")
ESCENARIOS_MINIMOS = ("A_VIS", "B_ESTANDAR", "C_LUJO")
DIAS_FRESCURA = 60


def _chip_por_defecto():
    try:
        with io.open(PARAM_PIPELINE, "r", encoding="utf-8") as fh:
            datos = json.load(fh)
        chip = datos.get("chip")
        if chip:
            return str(chip)
    except Exception:
        pass
    return None


def listar_exports(chip):
    patron = os.path.join(DIR_ORIGEN, "parametros_{}_f2mercado_*.json".format(chip))
    return sorted(glob.glob(patron), reverse=True)


def validar(ruta):
    """Devuelve (datos, error). Valida parse + claves minimas del export."""
    try:
        with io.open(ruta, "r", encoding="utf-8") as fh:
            datos = json.load(fh)
    except Exception as ex:
        return None, "JSON ilegible: {0}".format(ex)
    mercado = (datos.get("meta") or {}).get("mercado") or {}
    if not mercado.get("sector"):
        return None, "falta meta.mercado.sector"
    if not mercado.get("fecha_captura_origen"):
        return None, "falta meta.mercado.fecha_captura_origen"
    escenarios = datos.get("escenarios") or {}
    for esc in ESCENARIOS_MINIMOS:
        bloque = escenarios.get(esc)
        if not isinstance(bloque, dict) or not isinstance(bloque.get("precio_venta_m2"), (int, float)):
            return None, "escenario {0} sin precio_venta_m2 numerico".format(esc)
    return datos, None


def dias_desde_captura(datos):
    fecha = str(((datos.get("meta") or {}).get("mercado") or {}).get("fecha_captura_origen", ""))[:10]
    origen = datetime.date.fromisoformat(fecha)
    return (datetime.date.today() - origen).days


def sincronizar(chip, mes=None, forzar=False):
    candidatos = listar_exports(chip)
    if mes:
        candidatos = [c for c in candidatos if mes in os.path.basename(c)]
    if not candidatos:
        return 3, "Sin export de mercado para el chip {0} en:\n  {1}".format(chip, DIR_ORIGEN)

    ruta_origen = candidatos[0]
    datos, error = validar(ruta_origen)
    if datos is None:
        return 4, "Export invalido ({0}):\n  {1}".format(error, ruta_origen)

    try:
        dias = dias_desde_captura(datos)
    except Exception:
        return 4, "fecha_captura_origen ilegible en {0}".format(ruta_origen)

    vencido = dias > DIAS_FRESCURA
    if vencido and not forzar:
        return 2, ("Export VENCIDO ({0} dias > {1}): captura del {2}. Ejecuta una recaptura en "
                   "MercadoViviendaBogota o usa --forzar para copiarlo marcado como vencido.\n  {3}"
                   .format(dias, DIAS_FRESCURA,
                           (datos["meta"]["mercado"]["fecha_captura_origen"]), ruta_origen))

    if not os.path.isdir(DIR_ATERRIZAJE):
        os.makedirs(DIR_ATERRIZAJE)
    destino = os.path.join(DIR_ATERRIZAJE, os.path.basename(ruta_origen))
    shutil.copy2(ruta_origen, destino)

    # Anota la sincronizacion SOLO en la copia (el origen nunca se toca)
    with io.open(destino, "r", encoding="utf-8") as fh:
        copia = json.load(fh)
    copia.setdefault("meta", {})["sync"] = {
        "fecha_sync": datetime.datetime.now().isoformat(timespec="seconds"),
        "origen": ruta_origen,
        "dias_desde_captura": dias,
        "vencido": vencido,
        "validado": True,
        "sincronizador": "F2_SINCRONIZAR_MERCADO_v01",
    }
    with io.open(destino, "w", encoding="utf-8") as fh:
        json.dump(copia, fh, ensure_ascii=False, indent=2)

    mercado = copia["meta"]["mercado"]
    resumen = [
        "OK: parametros de mercado sincronizados para {0}".format(chip),
        "  origen : {0}".format(ruta_origen),
        "  copia  : {0}".format(destino),
        "  sector : {0} | captura de origen: {1} ({2} dias{3})".format(
            mercado.get("sector"), mercado.get("fecha_captura_origen"), dias,
            ", VENCIDO" if vencido else ""),
        "  precios : {0}".format("; ".join(
            "{0} precio ${1:,.0f}/m2 (n={2})".format(esc,
                (copia["escenarios"][esc]["precio_venta_m2"]),
                (mercado.get("cobertura_franjas") or {}).get(esc, {}).get("n_fichas", "?"))
            for esc in ESCENARIOS_MINIMOS if esc in copia.get("escenarios", {}))),
    ]
    return 0, "\n".join(resumen)


def main():
    parser = argparse.ArgumentParser(description="Sincroniza el export de mercado de MercadoViviendaBogota hacia DisenoParametrico (solo lectura del origen).")
    parser.add_argument("--chip", default=_chip_por_defecto(), help="CHIP del lote (por defecto, el de parametros_pipeline.json).")
    parser.add_argument("--mes", default=None, help="Filtra por mes del export (YYYY-MM). Por defecto usa el mas reciente.")
    parser.add_argument("--listar", action="store_true", help="Solo lista los exports disponibles para el chip.")
    parser.add_argument("--forzar", action="store_true", help="Copia aunque la captura este vencida (la copia queda marcada como vencida).")
    args = parser.parse_args()

    if not args.chip:
        parser.error("No hay chip por defecto en parametros_pipeline.json; pasa --chip.")

    if args.listar:
        disponibles = listar_exports(args.chip)
        if not disponibles:
            print("Sin exports para {0} en {1}".format(args.chip, DIR_ORIGEN))
            return 3
        print("Exports disponibles para {0}:".format(args.chip))
        for ruta in disponibles:
            print("  " + os.path.basename(ruta))
        return 0

    codigo, mensaje = sincronizar(args.chip, mes=args.mes, forzar=args.forzar)
    print(mensaje)
    return codigo


if __name__ == "__main__":
    sys.exit(main())
