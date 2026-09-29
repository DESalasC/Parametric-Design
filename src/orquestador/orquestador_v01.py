# -*- coding: utf-8 -*-
"""
================================================================================
orquestador_v01.py — PUNTO DE ENTRADA ÚNICO (DiseñoParametrico · Parte 1: F1->F3)
================================================================================

Un solo archivo para el operador. Hace dos cosas, integradas:

  1. FRONT-END: sirve la interfaz web en http://127.0.0.1:8900
     (reutiliza `servidor.py`: formulario + endpoints /api/*).
  2. PIPELINE: ejecuta TODO el pipeline (F1 contexto + contexto50, F2 venta/renta,
     F3 masa) LLAMANDO al front-end por HTTP — sin abrir/ejecutar dos archivos.

El pipeline corre "allí" (en el servidor/front-end): este archivo actúa como
lanzador y cliente; el servidor es quien ejecuta los pasos y responde.

MODOS DE USO:
  python src\\orquestador\\orquestador_v01.py                    # sirve el front-end (bloqueante)
  python src\\orquestador\\orquestador_v01.py --abrir            # sirve + abre el navegador
  python src\\orquestador\\orquestador_v01.py --run [--chip X --caso A --modo mixto --yes]
        # asegura el front-end (lo arranca si falta) y ejecuta el pipeline COMPLETO vía HTTP
  python src\\orquestador\\orquestador_v01.py --status [--chip X --caso A --modo mixto]
        # estado de pasos + verificación lados/patio (F1.5)
  python src\\orquestador\\orquestador_v01.py --checklist         # genera checklist.html
  python src\\orquestador\\orquestador_v01.py --stop              # detiene el front-end (puerto 8900)

NOTA (puerto 19723): la validación EN CANVAS (Live Connection Grasshopper-ArchiCAD)
requiere que la sesión de AutoClaw esté cerrada: AutoClaw ocupa 127.0.0.1:19723 y
la Live Connection solo conecta por ese puerto. Los pasos de canvas se guían y
verifican por artefacto; no se automatizan desde aquí.

CAMBIOS (2026-09-28):
  - Nace como archivo único: compone `servidor` (front-end/endpoints) y
    `run_pipeline_v01` (lógica de pasos/estado). El operador ya no ejecuta
    dos archivos diferentes.
  - `--run` ejecuta el pipeline completo A TRAVÉS del front-end (HTTP).

USO (Init-DP): el lanzador de escritorio vive en D:\\Work\\Scripts\\Init-DP.ps1.
================================================================================
"""

import argparse
import io
import json
import os
import subprocess
import sys
import time
import urllib.request as _ureq

# ------------------------------------------------------------------ rutas
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
PUERTO_DEFAULT = 8900

sys.path.insert(0, HERE)

import run_pipeline_v01 as rp  # noqa: E402  (lógica de pasos/estado/checklist)


# ------------------------------------------------------------------ utilidades HTTP

def _http_json(method, url, payload=None, timeout=20):
    data = None
    headers = {}
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
        headers["Content-Type"] = "application/json"
    req = _ureq.Request(url, data=data, headers=headers, method=method)
    with _ureq.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def _base(puerto):
    return "http://127.0.0.1:{}".format(puerto)


def _servidor_arriba(puerto, timeout=1.5):
    try:
        r = _http_json("GET", _base(puerto) + "/api/lotes", timeout=timeout)
        return bool(r.get("ok"))
    except Exception:
        return False


def _asegurar_servidor(puerto):
    """Devuelve la URL base; arranca servidor.py como proceso separado si falta."""
    base = _base(puerto)
    if _servidor_arriba(puerto):
        print("[i] Front-end ya activo en {}".format(base))
        return base

    logs = os.path.join(HERE, "logs")
    if not os.path.isdir(logs):
        os.makedirs(logs)
    log = io.open(os.path.join(logs, "servidor_{}.log".format(puerto)), "a")
    cmd = [sys.executable, os.path.join(HERE, "servidor.py"), "--puerto", str(puerto)]
    flags = 0
    if os.name == "nt":
        flags = 0x00000008 | 0x00000200  # DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP
    subprocess.Popen(cmd, cwd=ROOT, stdout=log, stderr=log, creationflags=flags)
    for _ in range(40):
        time.sleep(0.5)
        if _servidor_arriba(puerto):
            print("[ok] Front-end arrancado en {}".format(base))
            return base
    raise RuntimeError("El front-end no respondió en {} (revise logs/)".format(base))


def _detener_servidor(puerto):
    """Detiene el proceso python que escucha en el puerto (solo si es python)."""
    try:
        out = subprocess.run(["netstat", "-ano"], capture_output=True, text=True).stdout
    except Exception as ex:
        print("No se pudo consultar netstat:", ex)
        return False
    pids = set()
    for ln in out.splitlines():
        if ":{} ".format(puerto) in ln and "LISTENING" in ln.upper():
            pids.add(ln.split()[-1])
    if not pids:
        print("[i] Nada escuchando en el puerto {}.".format(puerto))
        return False
    detenido = False
    for pid in pids:
        try:
            q = subprocess.run(["tasklist", "/FI", "PID eq {}".format(pid), "/FO", "CSV", "/NH"],
                               capture_output=True, text=True).stdout
            nombre = q.split(",")[0].strip('"') if q else ""
            if "python" in nombre.lower():
                subprocess.run(["taskkill", "/PID", pid, "/F"], capture_output=True, text=True)
                print("[ok] Detenido PID {} ({})".format(pid, nombre))
                detenido = True
            else:
                print("[aviso] PID {} es '{}'; no se detiene por seguridad.".format(pid, nombre))
        except Exception as ex:
            print("[aviso] no se pudo detener PID {}: {}".format(pid, ex))
    return detenido


# ------------------------------------------------------------------ modos

def modo_servir(args):
    base = _base(args.puerto)
    print("=" * 68)
    print("ORQUESTADOR DiseñoParametrico — punto de entrada único (F1 -> F3)")
    print("Front-end: {}".format(base))
    print("Pipeline completo disponible en el navegador (botón 'Ejecutar pipeline completo').")
    print("Ctrl+C para detener (o use --stop desde otra consola).")
    print("=" * 68)
    if args.abrir and os.name == "nt":
        time.sleep(0.8)
        try:
            os.startfile(base)  # abre el navegador predeterminado
        except Exception:
            pass
    # servir en primer plano (reutiliza servidor.py)
    python = sys.executable
    return subprocess.call([python, os.path.join(HERE, "servidor.py"), "--puerto", str(args.puerto)], cwd=ROOT)


def modo_run(args):
    """Ejecuta el pipeline completo A TRAVÉS del front-end (HTTP)."""
    chip = args.chip
    if not chip:
        params = rp._cargar_parametros()
        chip = params.get("chip", "AAA0127AZPA")
    caso = args.caso or None
    modo = args.modo or "mixto"
    escenario = args.escenario or "D_MIXTO"

    base = _asegurar_servidor(args.puerto)
    print(">> Activando CHIP {}{} en el front-end...".format(chip, " y caso {}".format(caso) if caso else ""))
    _http_json("POST", base + "/api/activar-chip", {"chip": chip})
    if caso:
        _http_json("POST", base + "/api/activar-caso", {"caso": caso})

    print(">> Ejecutando pipeline completo (F1 -> F2 -> F3) vía {} ...".format(base))
    r = _http_json("POST", base + "/api/pipeline",
                   {"chip": chip, "caso": caso, "modo": modo, "escenario": escenario,
                    "modalidad_dueno_lote": {"tipo": "participacion", "pago_parcial_pct": 30}},
                   timeout=1800)
    p = r.get("pipeline") or {}
    print()
    for s in p.get("pasos", []):
        print("  [{}] {:32s} {}".format("OK" if s.get("ok") else "--", s.get("paso", ""), str(s.get("salida", ""))[:110]))
    lp = p.get("lados_patio") or {}
    if lp:
        print()
        print("  F1.5 lados/patio: {} — {}".format("OK" if lp.get("ok") else "pendiente", lp.get("detalle", "")))
    print()
    print("Pipeline {} para {}.".format("COMPLETADO" if p.get("completado") else "con pendientes", chip))
    return 0 if p.get("completado") else 2


def _imprimir_estado_local(chip, caso, modo):
    estado = rp.detectar_estado(chip, caso)
    simbolos = {"hecho": "[OK]", "falta": "[  ]", "manual": "[??]"}
    orden = ["f1_contexto", "f1_contexto50", "f1_gfa", "f2_venta", "f2_renta",
             "f3_distribucion", "f3_accesos", "f3_masa_rhino"]
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
    print("=" * 72)
    print("ORQUESTADOR (estado) — CHIP: {} | CASO: {} | MODO: {}".format(chip, caso, modo))
    print("=" * 72)
    for clave in orden:
        p = estado.get(clave, {})
        print("{} {}  {}".format(simbolos.get(p.get("estado"), "[??]"), nombres.get(clave, clave), p.get("artefacto", "")))
    lp = rp.estado_lados_patio(chip)
    print("-" * 72)
    print("{} F1.5 Lados/patio (diagnóstico canvas)  {}  [{}]".format(
        "[OK]" if lp.get("ok") else "[??]", lp.get("artefacto", ""), lp.get("detalle", "")))
    for c in lp.get("checks", []):
        if not c.get("ok"):
            print("        > REVISAR {}: {}".format(c.get("nombre"), c.get("detalle", "")))
    print("-" * 72)


def modo_status(args):
    chip = args.chip
    caso = args.caso or "A"
    modo = args.modo or "mixto"
    if not chip:
        params = rp._cargar_parametros()
        chip = params.get("chip", "AAA0127AZPA")
    # si hay front-end arriba, el estado se pide por HTTP (misma fuente que la UI)
    if _servidor_arriba(args.puerto):
        try:
            r = _http_json("GET", _base(args.puerto) + "/api/estado?chip={}&caso={}&modo={}".format(chip, caso, modo))
            print("=" * 72)
            print("ORQUESTADOR (estado vía front-end) — CHIP: {} | CASO: {} | MODO: {}".format(chip, caso, modo))
            print("=" * 72)
            for p in r.get("pasos", []):
                print("[{}] {:26s} {}".format(p.get("estado"), p.get("clave"), p.get("artefacto", "")))
            lp = r.get("lados_patio") or {}
            print("-" * 72)
            print("F1.5 lados/patio: {} — {}".format("OK" if lp.get("ok") else "pendiente", lp.get("detalle", "")))
            return 0
        except Exception as ex:
            print("[i] Front-end no respondió ({}); estado local.".format(ex))
    _imprimir_estado_local(chip, caso, modo)
    return 0


def modo_checklist(args):
    params = rp._cargar_parametros()
    chip = args.chip or params.get("chip", "AAA0127AZPA")
    caso = args.caso or params.get("caso", "A")
    modo = args.modo or params.get("modo", "mixto")
    estado = rp.detectar_estado(chip, caso)
    html = rp._generar_html(estado, chip, caso, modo)
    salida = os.path.join(HERE, "checklist.html")
    with io.open(salida, "w", encoding="utf-8") as f:
        f.write(html)
    print("Checklist generado: {}".format(salida))
    return 0


def main():
    parser = argparse.ArgumentParser(
        description="Orquestador DiseñoParametrico — punto de entrada único (front-end 8900 + pipeline F1->F3)")
    parser.add_argument("--puerto", type=int, default=PUERTO_DEFAULT, help="Puerto del front-end (default 8900)")
    parser.add_argument("--abrir", action="store_true", help="Abrir el navegador al servir")
    parser.add_argument("--run", action="store_true", help="Ejecutar el pipeline completo vía front-end")
    parser.add_argument("--status", action="store_true", help="Mostrar estado (pasos + lados/patio)")
    parser.add_argument("--checklist", action="store_true", help="Generar checklist.html")
    parser.add_argument("--stop", action="store_true", help="Detener el front-end del puerto")
    parser.add_argument("--chip", default=None, help="CHIP del predio")
    parser.add_argument("--caso", default=None, help="Caso F3 (A|B|B_SALUD|C)")
    parser.add_argument("--modo", default=None, help="venta|renta|mixto")
    parser.add_argument("--escenario", default=None, help="Escenario F3 (default D_MIXTO)")
    parser.add_argument("--yes", action="store_true", help="Sin confirmaciones (compat CLI)")
    args = parser.parse_args()

    if args.stop:
        ok = _detener_servidor(args.puerto)
        return 0 if ok else 1
    if args.run:
        return modo_run(args)
    if args.status:
        return modo_status(args)
    if args.checklist:
        return modo_checklist(args)
    return modo_servir(args)


if __name__ == "__main__":
    sys.exit(main())
