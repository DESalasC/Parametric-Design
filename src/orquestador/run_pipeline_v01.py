# -*- coding: utf-8 -*-
"""
================================================================================
run_pipeline_v01.py — Orquestador + Checklist interactivo (DiseñoParametrico)
Parte 1: F1 (contexto) -> F2 (demanda/financiero) -> F3 (masa) + LOOP BARRAS IO
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

NUEVO (v01.1, 2026-10-03) — Loop distribuidor↔validador (P2):
  - Paso F3_BARRAS (F3_DISTRIBUCION_v03 --presupuesto-ocupacion): genera barras_json
  - Paso NORMATIVA v09 RE-EJECUTADA con barras_json: valida ocupación ≤ presupuesto
  - Paso F1_EXPORTAR_GFA_v02.4: escribe SOLO gfa_aprobado_m2 (modo APROBADO)

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

MAPA CASO -> CHIP (coherente con F3_DISTRIBUCION_v03):
  A       -> AAA0127AZPA
  B       -> AAA0030JKOE
  B_SALUD -> AAA0030JKOE
  C       -> AAA0039KRMR

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
    try:
        if _existe(src):
            shutil.copy2(src, dst)
            return True
    except Exception as e:
        print("WARNING: Failed to copy {} to {}: {}".format(src, dst, str(e)))
    return False


def _ruta_parametros_f2_mercado(chip, dias_frescura=60):
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
        "f1_gfa": {
            "tipo": "manual",
            "estado": "hecho" if _existe(os.path.join(F2_DEMANDA, chip + "-gfa-gh.json")) else "manual",
            "artefacto": "data/fase-2-demanda/{}-gfa-gh.json".format(chip),
            "comando": None,
        },
        # --- NUEVOS PASOS LOOP BARRAS (P2) ---
        "f3_barras": {
            "tipo": "auto",
            "estado": "hecho" if _existe(os.path.join(F3_CASOS, caso, "barras.json")) else "falta",
            "artefacto": "src/fase-3-masa/casos/{}/barras.json".format(caso),
            "comando": None,  # se construye dinámicamente con presupuesto_ocupacion
        },
        "f1_normativa_aprobada": {
            "tipo": "manual",
            "estado": "manual",
            "artefacto": "NORMATIVA v09 re-ejecutada con barras_json (canvas v13.1)",
            "comando": None,
        },
        "f1_exportar_gfa_aprobado": {
            "tipo": "manual",
            "estado": "manual",
            "artefacto": "data/fase-2-demanda/{}-gfa-gh.json (modo APROBADO, solo gfa_aprobado)".format(chip),
            "comando": None,
        },
        # --- FIN NUEVOS PASOS ---
        "f2_venta": {
            "tipo": "auto",
            "estado": "hecho" if _hay_json_en(os.path.join(F2_VENTA_DIR, "resultados")) else "falta",
            "artefacto": "src/fase-2-demanda/F2_Modelo_Financiero/resultados/",
            "comando": None,
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
            "comando": [PY, os.path.join(F3_DIR, "F3_DISTRIBUCION_v02.py"), caso],
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
    }


def _comando_f2(tipo, params):
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
    print("ORQUESTADOR DiseñoParametrico — Parte 1 (F1 -> F3 + LOOP BARRAS)")
    print("CHIP: {} | CASO: {} | MODO: {}".format(chip, caso, modo))
    print("=" * 64)
    simbolos = {"hecho": "[OK]", "falta": "[  ]", "manual": "[??]"}
    orden = ["f1_contexto", "f1_contexto50", "f1_gfa",
             "f3_barras", "f1_normativa_aprobada", "f1_exportar_gfa_aprobado",
             "f2_venta", "f2_renta",
             "f3_distribucion", "f3_accesos", "f3_masa_rhino"]
    nombres = {
        "f1_contexto": "F1  Contexto normativo (fetch)",
        "f1_contexto50": "F1  Contexto 50 m (fetch)",
        "f1_gfa": "F1  Exportar GFA (manual Rhino)",
        "f3_barras": "F3  Distribuidor barras (--presupuesto-ocupacion)",
        "f1_normativa_aprobada": "F1  NORMATIVA v09 + barras_json (manual canvas)",
        "f1_exportar_gfa_aprobado": "F1  Exportar GFA APROBADO (solo gfa_aprobado)",
        "f2_venta": "F2  Modelo financiero (venta)",
        "f2_renta": "F2  Modelo Build-to-Rent (renta)",
        "f3_distribucion": "F3  Distribución espacial (v02)",
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

    if args.chip:
        chip = args.chip
    else:
        chip = _pedir("CHIP del predio [{}]: ".format(params.get("chip", "AAA0127AZPA")),
                      params.get("chip", "AAA0127AZPA"))

    if args.caso:
        caso = args.caso
    else:
        caso_previo = params.get("caso", "A")
        chip_de_caso = CASO_CHIP.get(caso_previo, "")
        default_caso = caso_previo if (not params.get("chip") or chip == chip_de_caso) else "A"
        caso = _pedir("CASO (A|B|B_SALUD|C) [{}]: ".format(default_caso), default_caso)

    if caso not in CASOS:
        print("ERROR: caso inválido '{}'. Opciones: {}".format(caso, CASOS))
        sys.exit(1)

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

    # --- Datum Z0 (ADR-024): calcular y guardar el marco de calculo del proyecto ---
    z0_modo = args.z0_modo or params.get("z0_modo", "min_lote")
    z0_valor = args.z0_valor if args.z0_valor is not None else params.get("z0_valor")
    z0_absoluto = bool(args.z0_absoluto or params.get("z0_absoluto", False))
    _cmd_z0 = [PY, os.path.join(ROOT, "scripts", "utilities", "calcular_z0_proyecto.py"),
               "--chip", chip, "--modo", z0_modo]
    if z0_valor is not None:
        _cmd_z0 += ["--valor", str(z0_valor)]
    if z0_absoluto:
        _cmd_z0 += ["--absoluto"]
    ok_z0, out_z0 = _ejecutar(_cmd_z0)
    if not ok_z0:
        print("ERROR: no se pudo calcular el datum Z0:")
        for linea in out_z0.strip().splitlines()[-6:]:
            print("    " + linea)
        sys.exit(1)
    try:
        ruta_z0 = os.path.join(POT_CACHE, chip + "-z0.json")
        if not os.path.isfile(ruta_z0):
            raise IOError("No se generó " + ruta_z0)
        with io.open(ruta_z0, "rb") as f:
            _z0_json = json.loads(f.read().decode("utf-8"))
        z0_m = float(_z0_json["z0_m"])
        z0_abs_m = float(_z0_json.get("z0_abs_m", 0.0))
        origen_z = float(_z0_json.get("origen_z_m", 0.0))
        modo_z0_usado = _z0_json.get("modo", z0_modo)
    except Exception:
        print("ERROR: salida del datum Z0 no parseable:")
        print(repr(out_z0[-500:]))
        sys.exit(1)
    print("[OK] Datum Z0 del proyecto: z0_m={:.4f} (modo={})".format(z0_m, modo_z0_usado))

    params_nuevos = {
        "_schema": "parametros_pipeline_v01",
        "chip": chip,
        "caso": caso,
        "modo": modo,
        "gfa_m2": gfa_m2,
        "costo_lote_cop": costo_lote,
        "z0_modo": modo_z0_usado,
        "z0_m": z0_m,
        "z0_abs_m": z0_abs_m,
        "origen_z_m": origen_z,
        "parametros_f2_venta": _detectar_parametros(chip, "venta"),
        "parametros_f2_renta": _detectar_parametros(chip, "renta"),
    }
    _guardar_parametros(params_nuevos)

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
        for paso_key in ["f1_contexto", "f1_contexto50"]:
            if paso_key in estado:
                estado[paso_key]["estado"] = "falta"
    _imprimir_estado(estado, chip, caso, modo)

    # 1. Pasos automáticos base (F1 fetch + F3 distribución v02 + accesos)
    pasos_auto_base = [
        ("f1_contexto", "F1 fetch contexto", lambda: _ejecutar(estado["f1_contexto"]["comando"])),
        ("f1_contexto50", "F1 fetch contexto 50m", lambda: _ejecutar(estado["f1_contexto50"]["comando"])),
        ("f3_distribucion", "F3 distribución (v02)", lambda: _ejecutar(estado["f3_distribucion"]["comando"])),
        ("f3_accesos", "F3 accesos", lambda: _ejecutar(estado["f3_accesos"]["comando"])),
    ]

    for clave, nombre, fn in pasos_auto_base:
        if estado[clave]["estado"] == "hecho":
            print("\n[OK] {} ya está hecho ({}). Se omite.".format(nombre, estado[clave]["artefacto"]))
            continue
        if not args.yes:
            resp = _pedir("\nEjecutar {}? [S/n]: ".format(nombre), "s").lower()
            if resp and resp != "s":
                continue
        print(">>> Ejecutando {} ...".format(nombre))
        ok, salida = fn()
        if ok:
            print("[OK] {} completado.".format(nombre))
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

    # 2. Loop barras IO (P2) - pasos semi-automáticos/guiados
    print("\n" + "=" * 64)
    print("LOOP BARRAS IO (P2) — F3_DISTRIBUCION_v03 + NORMATIVA v09 + EXPORT GFA APROBADO")
    print("=" * 64)

    # 2a. Obtener presupuesto_ocupacion_m2 desde NORMATIVA v09 (canvas v13.1)
    # El operador debe ejecutar NORMATIVA v09 en el canvas v13.1 y leer el Panel
    # salida: presupuesto_ocupacion_m2
    presupuesto_ocupacion = None
    if estado.get("f3_barras", {}).get("estado") == "falta":
        print("\n[MANUAL] Paso F3_BARRAS: Leer presupuesto_ocupacion_m2 del Panel NORMATIVA v09")
        print("  1. Abrir canvas F1_CONTEXTO_v13.1.gh en Rhino/Grasshopper")
        print("  2. Ejecutar NORMATIVA v09 (cablear json_path, sides_table_json, patio_curves, etc.)")
        print("  3. Leer Panel 'presupuesto_ocupacion_m2' (Number)")
        if not args.yes:
            presupuesto_str = _pedir("  Introduce presupuesto_ocupacion_m2 [662.44]: ", "662.44")
            try:
                presupuesto_ocupacion = float(presupuesto_str)
            except:
                presupuesto_ocupacion = 662.44
            print("  Presupuesto IO capturado: {:.2f} m2".format(presupuesto_ocupacion))
    else:
        presupuesto_ocupacion = 662.44

    # 2b. Ejecutar F3_DISTRIBUCION_v03 (distribuidor) con --presupuesto-ocupacion
    if estado.get("f3_barras", {}).get("estado") == "falta":
        print("\n>>> Ejecutando F3_DISTRIBUCION_v03 (distribuidor barras)...")
        cmd_barras = [
            PY, os.path.join(F3_DIR, "F3_DISTRIBUCION_v03.py"),
            "--caso", caso,
            "--presupuesto-ocupacion", str(presupuesto_ocupacion),
            "--n-barras", "2,3",
            "--entrepiso-adaptativo", "True",
            "--output-json", os.path.join(F3_CASOS, caso, "barras.json")
        ]
        ok, salida = _ejecutar(cmd_barras)
        if ok:
            print("[OK] F3_DISTRIBUCION_v03 completado -> barras.json generado")
            # Post: copiar a cache si sirve
            _copy_file(
                os.path.join(F3_CASOS, caso, "barras.json"),
                os.path.join(POT_CACHE, chip + "-barras.json")
            )
            estado["f3_barras"]["estado"] = "hecho"
        else:
            print("[ERROR] F3_DISTRIBUCION_v03 falló:")
            for linea in salida.strip().splitlines()[-8:]:
                print("    " + linea)
            if not args.yes:
                resp = _pedir("¿Continuar? [s/N]: ", "n").lower()
                if resp != "s":
                    sys.exit(1)

    # 2c. Re-ejecutar NORMATIVA v09 con barras_json (manual en canvas)
    if estado.get("f1_normativa_aprobada", {}).get("estado") == "manual":
        print("\n[MANUAL] Paso NORMATIVA APROBADA: Re-ejecutar NORMATIVA v09 con barras_json")
        print("  1. En canvas v13.1, conectar entrada 'barras_json' al Panel con contenido de barras.json")
        print("  2. Re-ejecutar NORMATIVA v09")
        print("  3. Verificar Panel: valido=True, io_real ≤ 0.70, gfa_aprobado_m2 > 0")
        if not args.yes:
            _pedir("  Presiona Enter cuando NORMATIVA reporte VALIDADO (APROBADO)...", "")
        estado["f1_normativa_aprobada"]["estado"] = "hecho"

    # 2d. Exportar GFA APROBADO (F1_EXPORTAR_GFA_v02.4)
    if estado.get("f1_exportar_gfa_aprobado", {}).get("estado") == "manual":
        print("\n[MANUAL] Paso EXPORTAR GFA APROBADO: Ejecutar F1_EXPORTAR_GFA_v02.4")
        print("  1. En canvas, conectar 'gfa_aprobado_m2' y 'ocupacion_aprobada_m2' desde NORMATIVA v09")
        print("  2. Poner flag exportar=true (orquestador POST /api/exportar-gfa)")
        print("  3. Verificar: JSON escrito con modo=APROBADO y gfa_aprobado_m2")
        if not args.yes:
            _pedir("  Presiona Enter cuando GFA APROBADO exportado...", "")
        estado["f1_exportar_gfa_aprobado"]["estado"] = "hecho"

    # 3. F2 motores (usarán gfa_aprobado del JSON exportado)
    pasos_f2 = [
        ("f2_venta", "F2 motor venta", "venta") if modo in ("venta", "mixto") else None,
        ("f2_renta", "F2 motor renta", "renta") if modo in ("renta", "mixto") else None,
    ]
    for paso in pasos_f2:
        if paso is None:
            continue
        clave, nombre, tipo = paso
        if estado[clave]["estado"] == "hecho":
            print("\n[OK] {} ya está hecho ({}). Se omite.".format(nombre, estado[clave]["artefacto"]))
            continue
        if not args.yes:
            resp = _pedir("\nEjecutar {}? [S/n]: ".format(nombre), "s").lower()
            if resp and resp != "s":
                continue
        print(">>> Ejecutando {} ...".format(nombre))
        cmd, cwd = _comando_f2(tipo, params_nuevos)
        ok, salida = _ejecutar(cmd, cwd)
        if ok:
            print("[OK] {} completado.".format(nombre))
        else:
            print("[ERROR] {} falló. Últimas líneas:".format(nombre))
            for linea in salida.strip().splitlines()[-8:]:
                print("    " + linea)
            if not args.yes:
                resp = _pedir("¿Continuar de todas formas? [s/N]: ", "n").lower()
                if resp != "s":
                    print("Detenido por el operador.")
                    sys.exit(1)

    # 4. Pasos manuales finales (GFA original, Masa Rhino)
    manuales = [
        ("f1_gfa", "F1 Exportar GFA (Rhino, modo POTENCIAL - referencia)",
         "En el canvas F1_Contexto_Base, cablea F1_EXPORTAR_GFA_v02 y ejecuta para escribir data/fase-2-demanda/{}-gfa-gh.json (modo POTENCIAL, referencia).".format(chip),
         "data/fase-2-demanda/{}-gfa-gh.json".format(chip)),
        ("f3_masa_rhino", "F3 Masa en Rhino + Morphs ArchiCAD",
         "Carga F3_VOLUM_GENERADOR_v08.py en el componente GHPython, cablea envelope_aprobado_por_piso <- NORMATIVA v09 (si APROBADO) o envelope_por_piso (potencial); cablea salidas *_mesh a AC_* (Live Connection).".format(caso),
         "Morphs en ArchiCAD (round-trip GetElements)"),
    ]
    for clave, nombre, instrucciones, artefacto in manuales:
        estado_actual = estado[clave]["estado"]
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
    print("Fin de la Parte 1 (F1 -> F3 + LOOP BARRAS IO).")
    print("Genera el checklist visual con: python run_pipeline_v01.py --checklist")
    print("=" * 64)


def _pedir(mensaje, default=""):
    try:
        valor = input(mensaje).strip()
    except (EOFError, KeyboardInterrupt):
        valor = ""
    return valor if valor else default


# ------------------------------------------------------------------ checklist HTML (same as before, updated order)

def _estado_badge(estado):
    if estado == "hecho":
        return ('<span class="badge ok">✓ Hecho</span>')
    if estado == "manual":
        return ('<span class="badge manual">✋ Manual</span>')
    return ('<span class="badge falta">✗ Falta</span>')


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


def _generar_html(estado, chip, caso, modo):
    pasos = [
        ("Fase 1 — Contexto", [
            ("f1_contexto", "1.1 Fetch contexto normativo", "auto",
             "Genera el JSON de contexto del predio (coordenadas locales, vías, vecinos).",
             "python scripts/utilities/fetch-contexto-completo_v01.py --chip {} --solo-base".format(chip),
             estado["f1_contexto"]["artefacto"]),
            ("f1_contexto50", "1.2 Fetch contexto 50 m", "auto",
             "Extrae edificios vecinos en radio 50 m (contexto50).",
             "python scripts/utilities/fetch-contexto-completo_v01.py --chip {} --solo-50".format(chip),
             estado["f1_contexto50"]["artefacto"]),
            ("f1_gfa", "1.3 Exportar GFA (manual Rhino, modo POTENCIAL)", "manual",
             "Cablea F1_EXPORTAR_GFA_v02 en el canvas y ejecuta para escribir GFA potencial (referencia).",
             "Componente F1_EXPORTAR_GFA_v02 en Grasshopper",
             estado["f1_gfa"]["artefacto"]),
        ]),
        ("Loop Barras IO (P2) — Ocupación ≤ IO", [
            ("f3_barras", "2.1 Distribuidor barras (F3_DISTRIBUCION_v03)", "auto",
             "Genera 2–3 barras crujía única que quepan en presupuesto_ocupacion_m2; emite barras.json.",
             "python src/fase-3-masa/F3_DISTRIBUCION_v03.py --caso {} --presupuesto-ocupacion <valor> --n-barras 2,3 --entrepiso-adaptativo".format(caso),
             estado["f3_barras"]["artefacto"]),
            ("f1_normativa_aprobada", "2.2 NORMATIVA v09 + barras_json (manual canvas)", "manual",
             "Re-ejecutar NORMATIVA v09 con entrada barras_json; validar valido=True, io_real ≤ 0.70, gfa_aprobado_m2 > 0.",
             "Canvas F1_CONTEXTO_v13.1: conectar barras_json → NORMATIVA v09",
             estado["f1_normativa_aprobada"]["artefacto"]),
            ("f1_exportar_gfa_aprobado", "2.3 Exportar GFA APROBADO (F1_EXPORTAR_GFA_v02.4)", "manual",
             "Cablear gfa_aprobado_m2 + ocupacion_aprobada_m2; flag exportar=true; escribe SOLO gfa_aprobado_m2.",
             "Componente F1_EXPORTAR_GFA_v02.4 + flag gfa-export-flag.json",
             estado["f1_exportar_gfa_aprobado"]["artefacto"]),
        ]),
        ("Fase 2 — Demanda / Financiero", [
            ("f2_venta", "3.1 Modelo financiero (venta)", "auto",
             "KPIs, alertas, sensibilidad y recomendación de venta.",
             "python F2_DEMANDA_MOTOR_v03.py --parametros <p> --chip {}".format(chip),
             estado["f2_venta"]["artefacto"]),
            ("f2_renta", "3.2 Modelo Build-to-Rent (renta)", "auto",
             "Construir para arrendar (CP/LP), TIR/VPN/cap rate, suelo soportable.",
             "python F2_RENTA_MOTOR_v03.py --parametros <p> --chip {}".format(chip),
             estado["f2_renta"]["artefacto"]),
        ]),
        ("Fase 3 — Masa", [
            ("f3_distribucion", "4.1 Distribución espacial (v02, layout usos)", "auto",
             "Programa-areas balanceado, matriz de adyacencias, layout y planos.",
             "python src/fase-3-masa/F3_DISTRIBUCION_v02.py {}".format(caso),
             estado["f3_distribucion"]["artefacto"]),
            ("f3_accesos", "4.2 Accesos por uso", "auto",
             "Accesos por uso (público/privado) y segregación de flujos.",
             "python src/fase-3-masa/F3_ACCESOS_INTEGRADOR_v02.py --caso {}".format(caso),
             estado["f3_accesos"]["artefacto"]),
            ("f3_masa_rhino", "4.3 Masa en Rhino + Morphs ArchiCAD (manual)", "manual",
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
<title>Orquestador DiseñoParametrico — F1→F3 + Loop Barras IO</title>
<style>
  :root { --ok:#1a7f37; --manual:#b8860b; --falta:#b42318; --bg:#f6f7f9; --card:#fff; }
  * { box-sizing: border-box; }
  body { font-family: -apple-system, "Segoe UI", Roboto, Arial, sans-serif; margin:0; background:var(--bg); color:#1f2328; line-height:1.5; }
  header { background:#1f2937; color:#fff; padding:22px 20px; }
  header h1 { margin:0 0 6px; font-size:22px; }
  header .meta { font-size:13px; opacity:.85; }
  .wrap { max-width:860px; margin:0 auto; padding:20px 16px 60px; }
  .progress { background:#fff; border:1px solid #e2e5ea; border-radius:10px; padding:16px; margin:18px 0; }
  .bar { height:12px; background:#e8ebef; border-radius:6px; overflow:hidden; margin-top:8px; }
  .bar > div { height:100%; background:var(--ok); }
  h2 { font-size:18px; margin:26px 0 10px; border-left:4px solid #1f2937; padding-left:10px; }
  .card { background:var(--card); border:1px solid #e2e5ea; border-radius:10px; padding:14px 16px; margin:10px 0; }
  .card.manual { border-left:4px solid var(--manual); }
  .card.auto { border-left:4px solid #64748b; }
  .card-head { display:flex; justify-content:space-between; align-items:center; gap:10px; flex-wrap:wrap; }
  .titulo { font-weight:600; }
  .desc { margin:6px 0; color:#3a3f46; font-size:14px; }
  .badge { font-size:12px; padding:3px 9px; border-radius:20px; color:#fff; white-space:nowrap; }
  .badge.ok { background:var(--ok); }
  .badge.manual { background:var(--manual); }
  .badge.falta { background:var(--falta); }
  code.cmd { display:block; background:#0f172a; color:#d7e0ea; padding:8px 10px; border-radius:6px; font-size:12.5px; margin:8px 0; overflow-x:auto; white-space:pre-wrap; }
  .artefacto { font-size:12.5px; color:#57606a; margin:4px 0 0; }
  .parte2 { margin-top:34px; border:1px dashed #cbd5e1; border-radius:10px; padding:18px; background:#fbfcfe; }
  .parte2 h2 { margin-top:0; }
  footer { text-align:center; color:#8a9199; font-size:12px; margin-top:30px; }
  @media (max-width:560px) { header h1 { font-size:19px; } .card-head { flex-direction:column; align-items:flex-start; } }
</style>
</head>
<body>
<header>
  <h1>Orquestador DiseñoParametrico — Parte 1 (F1 → F3 + Loop Barras IO)</h1>
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
  <footer>Generado por run_pipeline_v01.py v01.1 · DiseñoParametrico</footer>
</div>
</body>
</html>""".format(chip=chip, caso=caso, modo=modo, fecha=fecha, hechos=hechos,
             total=total, pct=pct, filas="\n".join(filas))
    return html


# ------------------------------------------------------------------ main

def main():
    parser = argparse.ArgumentParser(description="Orquestador + checklist DiseñoParametrico (F1->F3 + Loop Barras IO)")
    parser.add_argument("--status", action="store_true", help="Solo muestra el estado (sin ejecutar)")
    parser.add_argument("--run", action="store_true", help="Ejecuta el flujo guiado")
    parser.add_argument("--checklist", action="store_true", help="Genera checklist.html")
    parser.add_argument("--chip", default=None, help="CHIP del predio")
    parser.add_argument("--caso", default=None, help="Caso F3 (A|B|B_SALUD|C)")
    parser.add_argument("--modo", default=None, help="venta|renta|mixto")
    parser.add_argument("--gfa", type=float, default=None, help="Override de GFA (m2)")
    parser.add_argument("--costo-lote", type=float, default=None, help="Override costo de lote (COP)")
    parser.add_argument("--z0-modo", default=None, choices=("min_lote", "centro_lindero_via", "manual"), help="Datum Z0: min_lote|centro_lindero_via|manual (default min_lote)")
    parser.add_argument("--z0-valor", type=float, default=None, help="Valor Z local para modo manual (m)")
    parser.add_argument("--z0-absoluto", action="store_true", help="--z0-valor está en Z absoluto")
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