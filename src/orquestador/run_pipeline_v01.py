# -*- coding: utf-8 -*-
"""
================================================================================
run_pipeline_v01.py — Orquestador + Checklist interactivo (DiseñoParametrico)
Parte 1: F1 (contexto) -> F2 (demanda/financiero) -> F3 (masa)
Proyecto: DisenoParametrico / Utilidad transversal
Python 3 externo (NO IronPython). Se ejecuta desde la terminal.
================================================================================

PROPOSITO:
  Reducir el riesgo de error humano en las ejecuciones manuales. Un UNICO
  punto de entrada que:
    1. Detecta el estado real del proyecto (que ya existe / que falta).
    2. Recoge las variables una sola vez (chip, caso, modo, overrides).
    3. Ejecuta en orden los pasos AUTOMATIZABLES (CLI) validando cada salida.
    4. Guia los pasos MANUALES (Rhino/Grasshopper/ArchiCAD) con instrucciones
       y verifica el artefacto resultante.
    5. Genera un checklist HTML visual (fácil para un operador sin destreza).

MODOS:
  python run_pipeline_v01.py --status             # solo muestra el estado (sin ejecutar)
  python run_pipeline_v01.py --run [--chip X --caso A --modo mixto --yes]  # guiado/ejecuta
  python run_pipeline_v01.py --checklist          # genera checklist.html (sin ejecutar)

VARIABLES (fuente unica -> parametros_pipeline.json):
  chip            CHIP del predio (ej. AAA0127AZPA)
  caso            Caso F3 (A | B | B_SALUD | C); determina el chip si no se da
  modo            venta | renta | mixto
  gfa_m2          (opcional) override de GFA para los motores F2
  costo_lote_cop  (opcional) override de costo de lote total para F2

MAPA CASO -> CHIP (coherente con F3_DISTRIBUCION_v01):
  A       -> AAA0127AZPA
  B       -> AAA0030JKOE
  B_SALUD -> AAA0030JKOE
  C       -> AAA0039KRMR

CAMBIOS (2026-09-28):
  - Fix: import shutil (la copia de canonicos fallaba en silencio).
  - Fix: post_comando movido a la rama de exito (antes nunca se ejecutaba).
  - Estado f1_contexto/f1_contexto50 por FRESCURA (chip en el archivo), no
    por existencia: arranque en frio ya no salta el fetch.
  - Fetch unificado: usa scripts/utilities/fetch-contexto-completo_v01.py
    (--solo-base / --solo-50).
================================================================================
"""

import argparse
import datetime
import io
import json
import os
import re
import shutil
import subprocess
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))


def _candidatos_python():
    """2026-09-28: interpretes candidatos (el .venv quedo con ruedas cp312 sobre 3.11)."""
    cands = [sys.executable]
    try:
        p = subprocess.run(["py", "-0p"], capture_output=True, text=True, timeout=20)
        for ln in (p.stdout or "").splitlines():
            m = re.search(r"([A-Za-z]:\\.+?\.exe)", ln)
            if m:
                cands.append(m.group(1).strip())
    except Exception:
        pass
    cands.append(r"D:\Users\Work\AppData\Local\Programs\Python\Python312\python.exe")
    cands.append(r"C:\Program Files\Python311\python.exe")
    cands.append(os.path.join(ROOT, ".venv", "Scripts", "python.exe"))
    return cands


def _elegir_python_pipeline():
    """Primer interprete que importe numpy/pandas/geopandas/pyogrio (stack del fetch)."""
    for c in _candidatos_python():
        if not c or not os.path.exists(c) or not c.lower().endswith("python.exe"):
            continue
        try:
            p = subprocess.run([c, "-c", "import numpy, pandas, geopandas, pyogrio"],
                               capture_output=True, timeout=90)
            if p.returncode == 0:
                return c
        except Exception:
            continue
    return os.path.join(ROOT, ".venv", "Scripts", "python.exe")


PY = _elegir_python_pipeline()

CASO_CHIP = {
    "A": "AAA0127AZPA",
    "B": "AAA0030JKOE",
    "B_SALUD": "AAA0030JKOE",
    "C": "AAA0039KRMR",
}
CASOS = ["A", "B", "B_SALUD", "C"]
MODOS = ["venta", "renta", "mixto"]

POT_CACHE = os.path.join(ROOT, "data", "pot-cache")
F2_DEMANDA = os.path.join(ROOT, "data", "fase-2-demanda")
F3_CASOS = os.path.join(ROOT, "src", "fase-3-masa", "casos")
F2_VENTA_DIR = os.path.join(ROOT, "src", "fase-2-demanda", "F2_Modelo_Financiero")
F2_RENTA_DIR = os.path.join(ROOT, "src", "fase-2-demanda", "F2_Modelo_Renta")
F3_DIR = os.path.join(ROOT, "src", "fase-3-masa")

PARAM_JSON = os.path.join(os.path.dirname(os.path.abspath(__file__)), "parametros_pipeline.json")


# ------------------------------------------------------------------ helpers

def _existe(ruta):
    return os.path.exists(ruta) if ruta else False


def _hay_json_en(directorio):
    if not os.path.isdir(directorio):
        return False
    for nombre in os.listdir(directorio):
        if nombre.endswith(".json"):
            return True
    return False


def _cargar_parametros():
    if os.path.exists(PARAM_JSON):
        try:
            with io.open(PARAM_JSON, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}


def _guardar_parametros(params):
    with io.open(PARAM_JSON, "w", encoding="utf-8") as f:
        json.dump(params, f, indent=2, ensure_ascii=False)


def _copy_file(src, dst):
    """Copy file from src to dst, creating directories as needed."""
    try:
        if _existe(src):
            shutil.copy2(src, dst)
            return True
    except Exception as e:
        print("WARNING: Failed to copy {} to {}: {}".format(src, dst, str(e)))
    return False


def _ruta_parametros_f2_mercado(chip, dias_frescura=60):
    """Parametros de mercado sincronizados desde MercadoViviendaBogota.

    Busca en data/fase-2-demanda/mercado/ el archivo
    parametros_<chip>_f2mercado_*.json mas reciente (generado por el paso
    F2_SINCRONIZAR_MERCADO_v01.py). Solo lo acepta si su
    meta.mercado.fecha_captura_origen tiene <= dias_frescura dias; en caso
    contrario devuelve None y la cadena de prioridad sigue con los parametros
    curados del proyecto (fallback retrocompatible).
    """
    import glob
    import datetime
    dir_mercado = os.path.join(ROOT, "data", "fase-2-demanda", "mercado")
    candidatos = sorted(
        glob.glob(os.path.join(dir_mercado, "parametros_{}_f2mercado_*.json".format(chip))),
        reverse=True,
    )
    for ruta in candidatos:
        try:
            with open(ruta, "r", encoding="utf-8") as f:
                datos = json.load(f)
            fecha_captura = ((datos.get("meta") or {}).get("mercado") or {}).get("fecha_captura_origen")
            if not fecha_captura:
                continue
            origen = datetime.date.fromisoformat(str(fecha_captura)[:10])
            if (datetime.date.today() - origen).days <= dias_frescura:
                return ruta
        except Exception:
            continue
    return None


def _validar_contexto_fresco(chip, tipo_contexto):
    """Valida si el archivo de contexto es fresco (contiene el chip actual).

    Args:
        chip: Chip actual a validar contra
        tipo_contexto: "contexto" o "contexto50"

    Returns:
        tuple: (es_fresco, mensaje) donde es_fresco es booleano y mensaje es string
    """
    if tipo_contexto == "contexto":
        candidatos = [os.path.join(POT_CACHE, chip + "-contexto.json"),
                      os.path.join(POT_CACHE, "CHIP-contexto.json")]
    elif tipo_contexto == "contexto50":
        candidatos = [os.path.join(POT_CACHE, "contexto50-actual.json")]
    else:
        return False, "Tipo de contexto desconocido"

    mejor_msg = "Archivo no existe"
    for ruta_archivo in candidatos:
        if not _existe(ruta_archivo):
            continue
        try:
            with io.open(ruta_archivo, "r", encoding="utf-8") as f:
                contenido = json.load(f)

            chip_archivo = ""
            if isinstance(contenido, dict):
                metadata = contenido.get("metadata", {})
                if isinstance(metadata, dict):
                    chip_archivo = str(metadata.get("chip", ""))

            if chip_archivo == chip:
                return True, "Datos actualizados para chip {} ({})".format(
                    chip, os.path.basename(ruta_archivo))
            elif chip_archivo == "":
                mejor_msg = "Archivo inicializado (esperando datos)"
            else:
                mejor_msg = "Datos obsoletos (chip: {})".format(chip_archivo)

        except Exception as e:
            mejor_msg = "Error al leer archivo: {}".format(str(e))
    return False, mejor_msg


def _detectar_parametros(chip, tipo):
    """Busca el parametros.json mas adecuado para el chip (venta o renta)."""
    if tipo == "renta":
        base = os.path.join(F2_RENTA_DIR, "parametros_{}_renta.json".format(chip))
        if os.path.exists(base):
            return base
        return os.path.join(F2_RENTA_DIR, "parametros_entrada.json")
    cand_mercado = _ruta_parametros_f2_mercado(chip)
    if cand_mercado:
        return cand_mercado
    base_mercado = os.path.join(F2_VENTA_DIR, "parametros_{}_mercado2026.json".format(chip))
    if os.path.exists(base_mercado):
        return base_mercado
    base = os.path.join(F2_VENTA_DIR, "parametros_{}.json".format(chip))
    if os.path.exists(base):
        return base
    return os.path.join(F2_VENTA_DIR, "parametros_entrada.json")


def detectar_estado(chip, caso):
    """Devuelve un dict con el estado de cada paso: 'hecho' | 'falta' | 'manual'."""
    return {
        "f1_contexto": {
            "tipo": "auto",
            "estado": "hecho" if _validar_contexto_fresco(chip, "contexto")[0] else "falta",
            "artefacto": "data/pot-cache/CHIP-contexto.json (activo) | {}-contexto.json".format(chip),
            "comando": [PY, os.path.join(ROOT, "scripts", "utilities", "fetch-contexto-completo_v01.py"), "--chip", chip, "--solo-base"],
            "post_comando": lambda: (
                _copy_file(
                    os.path.join(POT_CACHE, chip + "-contexto.json"),
                    os.path.join(POT_CACHE, "CHIP-contexto.json")
                ),
                _copy_file(
                    os.path.join(POT_CACHE, chip + "-contexto.json"),
                    os.path.join(POT_CACHE, "contexto-actual.json")
                ),
            ) if _existe(os.path.join(POT_CACHE, chip + "-contexto.json")) else None,
        },
        "f1_gfa": {
            "tipo": "manual",
            "estado": "hecho" if _existe(os.path.join(F2_DEMANDA, chip + "-gfa-gh.json")) else "manual",
            "artefacto": "data/fase-2-demanda/{}-gfa-gh.json".format(chip),
            "comando": None,
        },
        "f2_venta": {
            "tipo": "auto",
            "estado": "hecho" if _hay_json_en(os.path.join(F2_VENTA_DIR, "resultados")) else "falta",
            "artefacto": "src/fase-2-demanda/F2_Modelo_Financiero/resultados/",
            "comando": None,  # se construye en _ejecutar con los overrides
        },
        "f2_renta": {
            "tipo": "auto",
            "estado": "hecho" if _hay_json_en(os.path.join(F2_RENTA_DIR, "resultados")) else "falta",
            "artefacto": "src/fase-2-demanda/F2_Modelo_Renta/resultados/",
            "comando": None,
        },
        "f3_distribucion": {
            "tipo": "auto",
            "estado": "hecho" if _existe(os.path.join(F3_CASOS, caso, "programa-areas.json")) else "falta",
            "artefacto": "src/fase-3-masa/casos/{}/programa-areas.json".format(caso),
            "comando": [PY, os.path.join(F3_DIR, "F3_DISTRIBUCION_v01.py"), caso],
        },
        "f3_accesos": {
            "tipo": "auto",
            "estado": "hecho" if _existe(os.path.join(F3_CASOS, caso, "accesos.json")) else "falta",
            "artefacto": "src/fase-3-masa/casos/{}/accesos.json".format(caso),
            "comando": [PY, os.path.join(F3_DIR, "F3_ACCESOS_INTEGRADOR_v02.py"), "--caso", caso],
        },
        "f3_masa_rhino": {
            "tipo": "manual",
            "estado": "manual",
            "artefacto": "Morphs nativos en ArchiCAD (sesión abierta de Rhino)",
            "comando": None,
        },
        "f1_contexto50": {
            "tipo": "auto",
            "estado": "hecho" if _validar_contexto_fresco(chip, "contexto50")[0] else "falta",
            "artefacto": "data/pot-cache/contexto50-actual.json",
            "comando": [PY, os.path.join(ROOT, "scripts", "utilities", "fetch-contexto-completo_v01.py"),
                      "--chip", chip, "--solo-50"],
            "post_comando": lambda: _copy_file(
                os.path.join(POT_CACHE, chip + "-contexto50.json"),
                os.path.join(POT_CACHE, "contexto50-actual.json")
            ) if _existe(os.path.join(POT_CACHE, chip + "-contexto50.json")) else None,
            "depends_on": ["f1_contexto"],
        },
    }


def _comando_f2(tipo, params):
    """Construye el comando del motor F2 (venta o renta) con los overrides."""
    if tipo == "renta":
        script = os.path.join(F2_RENTA_DIR, "F2_RENTA_MOTOR_v03.py")
        cwd = F2_RENTA_DIR
        parametros = _detectar_parametros(params["chip"], "renta")
    else:
        script = os.path.join(F2_VENTA_DIR, "F2_DEMANDA_MOTOR_v03.py")
        cwd = F2_VENTA_DIR
        parametros = _detectar_parametros(params["chip"], "venta")
    cmd = [PY, script, "--parametros", parametros, "--chip", params["chip"]]
    if params.get("gfa_m2"):
        cmd += ["--gfa", str(params["gfa_m2"])]
    if params.get("costo_lote_cop"):
        cmd += ["--costo-lote", str(params["costo_lote_cop"])]
    return cmd, cwd


def _ejecutar(cmd, cwd=ROOT):
    """Ejecuta un comando y devuelve (ok, salida). Nunca lanza excepción."""
    try:
        proc = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True,
                              encoding="utf-8", errors="replace")
        salida = (proc.stdout or "") + (proc.stderr or "")
        return proc.returncode == 0, salida
    except Exception as ex:
        return False, "ERROR de ejecución: {}".format(str(ex))


def _pedir(mensaje, default=""):
    try:
        valor = input(mensaje).strip()
    except (EOFError, KeyboardInterrupt):
        valor = ""
    return valor if valor else default


def estado_lados_patio(chip):
    """F1.5 (2026-09-28) - Verifica el diagnostico <CHIP>-lados.json del canvas v11.

    El canvas lo genera cuando el servidor/orquestador pone el flag
    data/pot-cache/lados-export-flag.json (componente PATIO v02.4).
    Devuelve dict con comprobaciones minimas: chip correcto, lados >= 3,
    patio >= 1, area >= 9 m2 y claridad >= 3 m (decision operador 2026-09-28).
    """
    ruta = os.path.join(POT_CACHE, chip + "-lados.json")
    res = {"existe": False, "ok": False,
           "artefacto": "data/pot-cache/{}-lados.json".format(chip),
           "detalle": "sin diagnostico (use 'Exportar diagnostico lados+patio' en el canvas)",
           "checks": []}
    if not os.path.exists(ruta):
        return res
    res["existe"] = True
    try:
        with io.open(ruta, "r", encoding="utf-8") as f:
            d = json.load(f)
    except Exception as e:
        res["detalle"] = "diagnostico ilegible: {}".format(str(e))
        return res
    checks = res["checks"]

    def _chk(nombre, ok, detalle):
        checks.append({"nombre": nombre, "ok": bool(ok), "detalle": detalle})

    _chk("chip", str(d.get("chip")) == chip, "chip={}".format(d.get("chip")))
    sides = d.get("sides") or {}
    n_lados = sides.get("total_lados")
    _chk("lados>=3", isinstance(n_lados, int) and n_lados >= 3, "total_lados={}".format(n_lados))
    patio = d.get("patio") or {}
    count = patio.get("count")
    _chk("patio>=1", isinstance(count, int) and count >= 1, "count={}".format(count))
    patios = patio.get("patios") or []
    for i, p in enumerate(patios):
        area = p.get("area_m2")
        clar = p.get("claridad_m")
        _chk("patio{}_area>=9".format(i),
             area is not None and float(area) >= 9.0 - 1e-6, "area={}".format(area))
        _chk("patio{}_claridad>=3".format(i),
             clar is not None and float(clar) >= 3.0 - 1e-6, "claridad={}".format(clar))
    msg = str(patio.get("mensaje") or "") + " " + str(sides.get("mensaje") or "")
    _chk("sin_ERROR", "ERROR" not in msg, "")
    res["ok"] = all(c["ok"] for c in checks)
    res["detalle"] = "lados={} · patio={} · {}".format(
        n_lados, count, "OK" if res["ok"] else "REVISAR")
    return res


# ------------------------------------------------------------------ status

def _imprimir_estado(estado, chip, caso, modo):
    print("=" * 64)
    print("ORQUESTADOR DiseñoParametrico — Parte 1 (F1 -> F3)")
    print("CHIP: {} | CASO: {} | MODO: {}".format(chip, caso, modo))
    print("=" * 64)
    simbolos = {"hecho": "[OK]", "falta": "[  ]", "manual": "[??]"}
    orden = ["f1_contexto", "f1_contexto50", "f1_gfa", "f2_venta", "f2_renta", "f3_distribucion", "f3_accesos", "f3_masa_rhino"]
    nombres = {
        "f1_contexto": "F1  Contexto normativo (fetch)",
        "f1_contexto50": "F1  Contexto 50 m (fetch)",
        "f1_gfa": "F1  Exportar GFA (manual Rhino)",
        "f2_venta": "F2  Modelo financiero (venta)",
        "f2_renta": "F2  Modelo Build-to-Rent (renta)",
        "f3_distribucion": "F3  Distribución espacial",
        "f3_accesos": "F3  Accesos por uso",
        "f3_masa_rhino": "F3  Masa en Rhino + Morphs ArchiCAD (manual)",
    }
    for clave in orden:
        paso = estado[clave]
        print("{} {}  {}".format(simbolos[paso["estado"]], nombres[clave], paso["artefacto"]))
    print("-" * 64)


# ------------------------------------------------------------------ run

def _modo_run(args):
    params = _cargar_parametros()

    # 1. variables (con defaults desde el parametros existente o detección)
    if args.chip:
        chip = args.chip
    else:
        chip = _pedir("CHIP del predio [{}]: ".format(params.get("chip", "AAA0127AZPA")),
                      params.get("chip", "AAA0127AZPA"))

    if args.caso:
        caso = args.caso
    else:
        # si el chip dado no corresponde al caso previo, intentar inferir
        caso_previo = params.get("caso", "A")
        chip_de_caso = CASO_CHIP.get(caso_previo, "")
        default_caso = caso_previo if (not params.get("chip") or chip == chip_de_caso) else "A"
        caso = _pedir("CASO (A|B|B_SALUD|C) [{}]: ".format(default_caso), default_caso)

    if caso not in CASOS:
        print("ERROR: caso inválido '{}'. Opciones: {}".format(caso, CASOS))
        sys.exit(1)

    # coherencia chip <-> caso
    chip_esperado = CASO_CHIP[caso]
    if not args.chip and chip != chip_esperado:
        print("AVISO: el caso {} corresponde al chip {}; se usa {}.".format(caso, chip_esperado, chip_esperado))
        chip = chip_esperado

    if args.modo:
        modo = args.modo
    else:
        modo = _pedir("MODO (venta|renta|mixto) [{}]: ".format(params.get("modo", "mixto")),
                      params.get("modo", "mixto"))
    if modo not in MODOS:
        print("ERROR: modo inválido '{}'. Opciones: {}".format(modo, MODOS))
        sys.exit(1)

    gfa_m2 = args.gfa if args.gfa is not None else params.get("gfa_m2")
    costo_lote = args.costo_lote if args.costo_lote is not None else params.get("costo_lote_cop")

    params_nuevos = {
        "_schema": "parametros_pipeline_v01",
        "chip": chip,
        "caso": caso,
        "modo": modo,
        "gfa_m2": gfa_m2,
        "costo_lote_cop": costo_lote,
        "parametros_f2_venta": _detectar_parametros(chip, "venta"),
        "parametros_f2_renta": _detectar_parametros(chip, "renta"),
    }
    _guardar_parametros(params_nuevos)

    # Initialize blank canonical context files if they don't exist
    contexto_blank = json.dumps({
        "metadata": {"chip": "", "origen_sirgas": {"x": 0, "y": 0, "z": 0}},
        "lote_objetivo": {"vertices_3d_local": []},
        "vias_oficiales": [],
        "espacios_publicos": [],
        "vecinos": []
    }, indent=2)

    contexto50_blank = json.dumps({
        "metadata": {"chip": "", "radio_m": 0, "altura_por_piso_m": 0},
        "edificios": []
    }, indent=2)

    contexto_path = os.path.join(POT_CACHE, "contexto-actual.json")
    contexto50_path = os.path.join(POT_CACHE, "contexto50-actual.json")

    if not _existe(contexto_path):
        with io.open(contexto_path, "w", encoding="utf-8") as f:
            f.write(contexto_blank)

    if not _existe(contexto50_path):
        with io.open(contexto50_path, "w", encoding="utf-8") as f:
            f.write(contexto50_blank)

    estado = detectar_estado(chip, caso)
    if args.refresh:
        # Force refresh of context steps by marking them as 'falta'
        for paso_key in ["f1_contexto", "f1_contexto50"]:
            if paso_key in estado:
                estado[paso_key]["estado"] = "falta"
    _imprimir_estado(estado, chip, caso, modo)

    # 2. pasos automáticos
    pasos_auto = [
        ("f1_contexto", "F1 fetch contexto", lambda: _ejecutar(estado["f1_contexto"]["comando"])),
        ("f1_contexto50", "F1 fetch contexto 50m", lambda: _ejecutar(estado["f1_contexto50"]["comando"])),
        ("f2_venta", "F2 motor venta", None) if modo in ("venta", "mixto") else None,
        ("f2_renta", "F2 motor renta", None) if modo in ("renta", "mixto") else None,
        ("f3_distribucion", "F3 distribución", lambda: _ejecutar(estado["f3_distribucion"]["comando"])),
        ("f3_accesos", "F3 accesos", lambda: _ejecutar(estado["f3_accesos"]["comando"])),
    ]

    for paso in pasos_auto:
        if paso is None:
            continue
        clave, nombre, fn = paso
        if estado[clave]["estado"] == "hecho":
            print("\n[OK] {} ya está hecho ({}). Se omite.".format(nombre, estado[clave]["artefacto"]))
            continue
        if not args.yes:
            resp = _pedir("\nEjecutar {}? [S/n]: ".format(nombre), "s").lower()
            if resp and resp != "s":
                continue
        print(">>> Ejecutando {} ...".format(nombre))
        if clave in ("f2_venta", "f2_renta"):
            cmd, cwd = _comando_f2("renta" if clave == "f2_renta" else "venta", params_nuevos)
            ok, salida = _ejecutar(cmd, cwd)
        else:
            ok, salida = fn()
        if ok:
            print("[OK] {} completado.".format(nombre))
            # Post-comando (fix 2026-09-28: el bloque estaba dentro de la rama
            # de fallo y nunca se ejecutaba; p.ej. copia <CHIP>-contexto.json
            # -> contexto-actual.json).
            if "post_comando" in estado[clave] and estado[clave]["post_comando"]:
                try:
                    estado[clave]["post_comando"]()
                except Exception as e:
                    print("WARNING: Post-comando failed for {}: {}".format(clave, str(e)))
        else:
            print("[ERROR] {} falló. Últimas líneas:".format(nombre))
            lineas = salida.strip().splitlines()
            for linea in lineas[-8:]:
                print("    " + linea)
            if not args.yes:
                resp = _pedir("¿Continuar de todas formas? [s/N]: ", "n").lower()
                if resp != "s":
                    print("Detenido por el operador.")
                    sys.exit(1)

    # 3. pasos manuales (guiados)
    manuales = [
        ("f1_gfa", "F1 Exportar GFA (Rhino)",
         "En el canvas F1_Contexto_Base (sesión abierta de Rhino), cablea "
         "F1_EXPORTAR_GFA_v02 y ejecuta para escribir data/fase-2-demanda/{}-gfa-gh.json.".format(chip),
         "data/fase-2-demanda/{}-gfa-gh.json".format(chip)),
        ("f3_masa_rhino", "F3 Masa en Rhino + Morphs ArchiCAD",
         "Carga F3_VOLUM_GENERADOR_v08.py en el componente GHPython, cablea "
         "envelope_por_piso <- NORMATIVA_v08 y json_path <- casos/{}/programa-areas.json; "
         "cablea las salidas *_mesh a los AC_* de Live Connection (Morphs).".format(caso),
         "Morphs en ArchiCAD (round-trip GetElements)"),
    ]
    for clave, nombre, instrucciones, artefacto in manuales:
        estado_actual = detectar_estado(chip, caso)[clave]["estado"]
        if estado_actual == "hecho":
            print("\n[OK] {} ya está hecho ({}).".format(nombre, artefacto))
            continue
        print("\n" + "=" * 64)
        print("[MANUAL] {}".format(nombre))
        print("=" * 64)
        print(instrucciones)
        print("Salida esperada: {}".format(artefacto))
        if not args.yes:
            _pedir("Presiona Enter cuando esté listo (o escribe 'saltar')...", "")
        nuevo = detectar_estado(chip, caso)[clave]["estado"]
        if nuevo == "hecho":
            print("[OK] Verificado: {} presente.".format(artefacto))
        else:
            print("[AVISO] Aún no se detecta el artefacto. Verifica antes de continuar.")

    print("\n" + "=" * 64)
    print("Fin de la Parte 1 (F1 -> F3).")
    print("Genera el checklist visual con: python run_pipeline_v01.py --checklist")
    print("La Parte 2 (F4 ambiental + F5 BIM) se desarrollará aparte.")
    print("=" * 64)


# ------------------------------------------------------------------ checklist HTML

def _estado_badge(estado):
    if estado == "hecho":
        return ('<span class="badge ok">✓ Hecho</span>')
    if estado == "manual":
        return ('<span class="badge manual">✋ Manual</span>')
    return ('<span class="badge falta">✗ Falta</span>')


def _generar_html(estado, chip, caso, modo):
    pasos = [
        ("Fase 1 — Contexto", [
            ("f1_contexto", "1.1 Fetch contexto normativo", "auto",
             "Genera el JSON de contexto del predio (coordenadas locales, vías, vecinos).",
             "python scripts/utilities/fetch-urban-context-v7.py --chip {}".format(chip),
             estado["f1_contexto"]["artefacto"]),
            ("f1_gfa", "1.2 Exportar GFA (manual Rhino)", "manual",
             "Cablea F1_EXPORTAR_GFA_v02 en el canvas y ejecuta para escribir el GFA que consumirán los motores F2.",
             "Componente F1_EXPORTAR_GFA_v02 en Grasshopper",
             estado["f1_gfa"]["artefacto"]),
        ]),
        ("Fase 2 — Demanda / Financiero", [
            ("f2_venta", "2.1 Modelo financiero (venta)", "auto",
             "KPIs, alertas, sensibilidad y recomendación de venta.",
             "python F2_DEMANDA_MOTOR_v03.py --parametros <p> --chip {}".format(chip),
             estado["f2_venta"]["artefacto"]),
            ("f2_renta", "2.2 Modelo Build-to-Rent (renta)", "auto",
             "Construir para arrendar (CP/LP), TIR/VPN/cap rate, suelo soportable.",
             "python F2_RENTA_MOTOR_v03.py --parametros <p> --chip {}".format(chip),
             estado["f2_renta"]["artefacto"]),
        ]),
        ("Fase 3 — Masa", [
            ("f3_distribucion", "3.1 Distribución espacial", "auto",
             "Programa-areas balanceado, matriz de adyacencias, layout y planos.",
             "python src/fase-3-masa/F3_DISTRIBUCION_v01.py {}".format(caso),
             estado["f3_distribucion"]["artefacto"]),
            ("f3_accesos", "3.2 Accesos por uso", "auto",
             "Accesos por uso (público/privado) y segregación de flujos.",
             "python src/fase-3-masa/F3_ACCESOS_INTEGRADOR_v02.py --caso {}".format(caso),
             estado["f3_accesos"]["artefacto"]),
            ("f3_masa_rhino", "3.3 Masa en Rhino + Morphs (manual)", "manual",
             "F3_VOLUM_GENERADOR_v08 + salidas a Morphs nativos de ArchiCAD (Live Connection).",
             "Componente F3_VOLUM_GENERADOR_v08 en Grasshopper",
             estado["f3_masa_rhino"]["artefacto"]),
        ]),
    ]

    total = 0
    hechos = 0
    for _, pasos_fase in pasos:
        for _ in pasos_fase:
            total += 1
    for _, pasos_fase in pasos:
        for clave, _, _, _, _, _ in pasos_fase:
            if estado[clave]["estado"] == "hecho":
                hechos += 1

    filas = []
    for titulo_fase, pasos_fase in pasos:
        filas.append('<h2>{}</h2>'.format(titulo_fase))
        for clave, titulo, tipo, descripcion, comando, artefacto in pasos_fase:
            badge = _estado_badge(estado[clave]["estado"])
            cmd_html = ('<code class="cmd">{}</code>'.format(comando)) if comando else (
                '<code class="cmd">(manual — ver instrucciones)</code>')
            filas.append('''
            <div class="card {tipo}">
              <div class="card-head"><span class="titulo">{titulo}</span>{badge}</div>
              <p class="desc">{descripcion}</p>
              {cmd}
              <p class="artefacto">Salida: <b>{artefacto}</b></p>
            </div>'''.format(tipo=tipo, titulo=titulo, badge=badge,
                             descripcion=descripcion, cmd=cmd_html, artefacto=artefacto))

    pct = int(round(100.0 * hechos / total)) if total else 0
    fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    html = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Orquestador DiseñoParametrico — F1→F3</title>
<style>
  :root {{ --ok:#1a7f37; --manual:#b8860b; --falta:#b42318; --bg:#f6f7f9; --card:#fff; }}
  * {{ box-sizing: border-box; }}
  body {{ font-family: -apple-system, "Segoe UI", Roboto, Arial, sans-serif; margin:0; background:var(--bg); color:#1f2328; line-height:1.5; }}
  header {{ background:#1f2937; color:#fff; padding:22px 20px; }}
  header h1 {{ margin:0 0 6px; font-size:22px; }}
  header .meta {{ font-size:13px; opacity:.85; }}
  .wrap {{ max-width:860px; margin:0 auto; padding:20px 16px 60px; }}
  .progress {{ background:#fff; border:1px solid #e2e5ea; border-radius:10px; padding:16px; margin:18px 0; }}
  .bar {{ height:12px; background:#e8ebef; border-radius:6px; overflow:hidden; margin-top:8px; }}
  .bar > div {{ height:100%; background:var(--ok); }}
  h2 {{ font-size:18px; margin:26px 0 10px; border-left:4px solid #1f2937; padding-left:10px; }}
  .card {{ background:var(--card); border:1px solid #e2e5ea; border-radius:10px; padding:14px 16px; margin:10px 0; }}
  .card.manual {{ border-left:4px solid var(--manual); }}
  .card.auto {{ border-left:4px solid #64748b; }}
  .card-head {{ display:flex; justify-content:space-between; align-items:center; gap:10px; flex-wrap:wrap; }}
  .titulo {{ font-weight:600; }}
  .desc {{ margin:6px 0; color:#3a3f46; font-size:14px; }}
  .badge {{ font-size:12px; padding:3px 9px; border-radius:20px; color:#fff; white-space:nowrap; }}
  .badge.ok {{ background:var(--ok); }}
  .badge.manual {{ background:var(--manual); }}
  .badge.falta {{ background:var(--falta); }}
  code.cmd {{ display:block; background:#0f172a; color:#d7e0ea; padding:8px 10px; border-radius:6px; font-size:12.5px; margin:8px 0; overflow-x:auto; white-space:pre-wrap; }}
  .artefacto {{ font-size:12.5px; color:#57606a; margin:4px 0 0; }}
  .parte2 {{ margin-top:34px; border:1px dashed #cbd5e1; border-radius:10px; padding:18px; background:#fbfcfe; }}
  .parte2 h2 {{ margin-top:0; }}
  footer {{ text-align:center; color:#8a9199; font-size:12px; margin-top:30px; }}
  @media (max-width:560px) {{ header h1 {{ font-size:19px; }} .card-head {{ flex-direction:column; align-items:flex-start; }} }}
</style>
</head>
<body>
<header>
  <h1>Orquestador DiseñoParametrico — Parte 1 (F1 → F3)</h1>
  <div class="meta">CHIP: {chip} &nbsp;|&nbsp; CASO: {caso} &nbsp;|&nbsp; MODO: {modo} &nbsp;|&nbsp; Generado: {fecha}</div>
</header>
<div class="wrap">
  <div class="progress">
    <b>Progreso: {hechos} de {total} pasos listos ({pct}%)</b>
    <div class="bar"><div style="width:{pct}%"></div></div>
  </div>
  {filas}
  <div class="parte2">
    <h2>Parte 2 — F4 ambiental + F5 BIM (próximamente)</h2>
    <p>Se desarrollará como un módulo aparte bajo los mismos estándares de esta parte.
       Incluirá: <b>F4</b> (Ladybug + EPW Bogotá sobre la masa F3) y <b>F5</b> (inyección BIM
       nativa a ArchiCAD vía protocolo Tapir / puerto 19723).</p>
    <p><b>Round-trip del operador:</b> los cambios que el operador haga en ArchiCAD a la
       distribución de componentes (escaleras, servicios, núcleo) vuelven a Grasshopper vía
       <b>Live Connection GetElements</b>; esa geometría final — no la generada por F3 — es la
       que debe alimentar Ladybug (F4).</p>
  </div>
  <footer>Generado por run_pipeline_v01.py · DiseñoParametrico</footer>
</div>
</body>
</html>""".format(chip=chip, caso=caso, modo=modo, fecha=fecha, hechos=hechos,
             total=total, pct=pct, filas="\n".join(filas))
    return html


def _modo_checklist(args):
    params = _cargar_parametros()
    chip = args.chip or params.get("chip", "AAA0127AZPA")
    caso = args.caso or params.get("caso", "A")
    modo = args.modo or params.get("modo", "mixto")
    estado = detectar_estado(chip, caso)
    html = _generar_html(estado, chip, caso, modo)
    salida = os.path.join(os.path.dirname(os.path.abspath(__file__)), "checklist.html")
    with io.open(salida, "w", encoding="utf-8") as f:
        f.write(html)
    print("Checklist generado: {}".format(salida))


# ------------------------------------------------------------------ main

def main():
    parser = argparse.ArgumentParser(description="Orquestador + checklist DiseñoParametrico (F1->F3)")
    parser.add_argument("--status", action="store_true", help="Solo muestra el estado (sin ejecutar)")
    parser.add_argument("--run", action="store_true", help="Ejecuta el flujo guiado")
    parser.add_argument("--checklist", action="store_true", help="Genera checklist.html")
    parser.add_argument("--chip", default=None, help="CHIP del predio")
    parser.add_argument("--caso", default=None, help="Caso F3 (A|B|B_SALUD|C)")
    parser.add_argument("--modo", default=None, help="venta|renta|mixto")
    parser.add_argument("--gfa", type=float, default=None, help="Override de GFA (m2)")
    parser.add_argument("--costo-lote", type=float, default=None, help="Override costo de lote (COP)")
    parser.add_argument("--yes", action="store_true", help="No pedir confirmaciones")
    parser.add_argument("--refresh", action="store_true", help="Forzar actualización de contexto ignorando el estado actual")
    args = parser.parse_args()

    if args.status:
        params = _cargar_parametros()
        chip = args.chip or params.get("chip", "AAA0127AZPA")
        caso = args.caso or params.get("caso", "A")
        modo = args.modo or params.get("modo", "mixto")
        _imprimir_estado(detectar_estado(chip, caso), chip, caso, modo)
    elif args.checklist:
        _modo_checklist(args)
    elif args.run:
        _modo_run(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
