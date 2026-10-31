#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fetch-contexto-completo_v01.py  — Orquestador unificado de Contexto (Fase 1)
======================================================================
Proyecto: DiseñoParametrico
Propósito: Ejecuta en secuencia los dos pasos necesarios para obtener
           tanto el contexto base como el contexto 50 m (volumetrías
           de vecinos) en una sola invocación.

PASO 1: fetch-urban-context-v7.py
  → genera data/pot-cache/<CHIP>-contexto.json
  → lote, vecinos (linderos), vías oficiales, espacios públicos, POT, topografía

PASO 2: F1_CONTEXTO50_FETCH_v01.py
  → lee el JSON del Paso 1 (--ctx) para conocer marco local y ancla
  → extrae construcciones de bd_uaecd.gpkg#Cons en radio 50 m
  → genera data/pot-cache/<CHIP>-contexto50.json + .geojson

CAMBIOS v01 (2026-09-28):
  1. Creación automática de archivo canónico `contexto50-actual.json` en
     `data/pot-cache/` como copia del `<CHIP>-contexto50.json` generado.
     Esto permite que los componentes GHPython (F1_CONTEXTO50_BUILD_v01b.py,
     F1_ETAPA3_CONTEXTO50_v01.1.py) encuentren el archivo sin requerir
     que el canvas tenga el CHIP hardcodeado.

CAMBIOS v02 (2026-10-30):
  1. Nueva etapa opcional `--enviar-archicad` que, tras generar los JSON, envía
     lote, vías oficiales y espacios públicos a ArchiCAD vía Tapir
     (puerto CommandConnection 19724). Cierra el círculo JSON → ArchiCAD desde
     el orquestador sin depender del canvas GH.
     - Lote objetivo -> zona en 00-00-10_Lote_proyecto (placa a cota 0 local).
     - Vías oficiales -> wall delgado (0.10 m) en 00-20-20_Elementos_entorno_urbano.
     - Espacios públicos -> zona en 70-50-10_Zonas_verdes_publicas.
  2. Nuevo argumento `--tapir-puerto` (default 19724) para el CommandConnection.
  3. Las coordenadas se expresan en marco local (restan origen SIRGAS del metadata).

USO (desde la raíz del proyecto o vía orquestador):
  python scripts/utilities/fetch-contexto-completo.py --chip AAA0240ZXJH --gpkg <ruta_gpkg>
  python scripts/utilities/fetch-contexto-completo.py --chip AAA0240ZXJH --radio 75 --out data/pot-cache --gpkg <ruta_gpkg>
"""

import argparse
import json
import os
import sys
import subprocess


def run_step(cmd, cwd, label):
    """Ejecuta un subcomando y propaga el código de salida."""
    print(f"\n{'='*60}")
    print(f">>> {label}")
    print(f"   Comando: {' '.join(cmd)}")
    print(f"{'='*60}")
    result = subprocess.run(cmd, cwd=cwd)
    if result.returncode != 0:
        print(f"\n[FALLO] {label} (codigo {result.returncode})")
    else:
        print(f"\n[OK] {label}")
    return result.returncode


def _gpkg_candidato():
    """2026-09-28: ruta portable de la geobase del proyecto (data/geobase)."""
    cand = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
                        "data", "geobase", "bd_uaecd.gpkg")
    return cand if os.path.exists(cand) else ""


def main():
    parser = argparse.ArgumentParser(
        description="Orquestador unificado: contexto base + contexto 50m"
    )
    parser.add_argument("--chip", required=True, help="CHIP del predio objetivo")
    parser.add_argument(
        "--radio", type=float, default=50.0, help="Radio en metros para contexto50 (default: 50)"
    )
    parser.add_argument(
        "--altura-piso", type=float, default=3.80, help="Altura por piso en metros (default: 3.80)"
    )
    parser.add_argument(
        "--out", default="data/pot-cache", help="Carpeta de salida (default: data/pot-cache)"
    )
    parser.add_argument(
        "--fuente", choices=["gpkg", "rest"], default="gpkg", help="Fuente para contexto50 (default: gpkg)"
    )
    parser.add_argument(
        "--marco", choices=["canvas", "json"], default="canvas", help="Marco de salida contexto50 (default: canvas)"
    )
    parser.add_argument(
        "--gpkg", default=os.environ.get("POT_GPKG_PATH") or _gpkg_candidato(), help="Ruta a bd_uaecd.gpkg (default: $POT_GPKG_PATH o data/geobase)"
    )
    parser.add_argument(
        "--solo-base", action="store_true", help="Solo ejecutar Paso 1 (contexto base)"
    )
    parser.add_argument(
        "--solo-50", action="store_true", help="Solo ejecutar Paso 2 (requiere CHIP-contexto.json previo)"
    )
    parser.add_argument(
        "--enviar-archicad", action="store_true", help="Tras generar JSON, enviar lote/vias/espacios_publicos a ArchiCAD via Tapir (puerto 19724)"
    )
    parser.add_argument(
        "--tapir-puerto", type=int, default=19723, help="Puerto Tapir CommandConnection de ArchiCAD (default: 19723; verificado que la API responde en 19723 en este equipo 2026-10-30). Si Rhino.Compute está activo, cambiar a qwen2.5:7b."
    )
    args = parser.parse_args()

    project_root = os.environ.get("DISENO_PARAMETRICO_ROOT", os.getcwd())
    out_dir_abs = os.path.join(project_root, args.out) if not os.path.isabs(args.out) else args.out

    # Rutas a los scripts
    script_base = os.path.join(project_root, "scripts", "utilities", "fetch-urban-context-v7.py")
    script_50 = os.path.join(project_root, "src", "fase-1-contexto", "F1_CONTEXTO50_FETCH_v01.py")

    # Verificar que existen
    for s, name in [(script_base, "fetch-urban-context-v7.py"), (script_50, "F1_CONTEXTO50_FETCH_v01.py")]:
        if not os.path.exists(s):
            print(f"ERROR: No se encuentra {name} en {s}")
            return 1

    # Validar GPKG si se usa fuente gpkg
    if not args.solo_50 and args.fuente == "gpkg":
        gpkg_path = args.gpkg
        if not gpkg_path:
            print("ERROR: Se requiere --gpkg o variable de entorno POT_GPKG_PATH para fuente gpkg")
            return 1
        if not os.path.exists(gpkg_path):
            print(f"ERROR: No existe la geobase: {gpkg_path}")
            return 1

    # Archivo de contexto base que generará el Paso 1
    ctx_base = os.path.join(out_dir_abs, f"{args.chip}-contexto.json")

    # ── PASO 1: Contexto base ──────────────────────────────────────────────
    if not args.solo_50:
        cmd1 = [
            sys.executable, script_base,
            "--chip", args.chip,
            "--output-dir", out_dir_abs,
        ]
        if args.gpkg:
            cmd1.extend(["--gpkg", args.gpkg])
        rc = run_step(cmd1, project_root, "PASO 1: fetch-urban-context-v7 (contexto base)")
        if rc != 0:
            return rc

    # ── PASO 2: Contexto 50m ───────────────────────────────────────────────
    if not args.solo_base:
        if not os.path.exists(ctx_base):
            print(f"\n[ERROR] No existe el contexto base requerido: {ctx_base}")
            print("   Ejecuta primero sin --solo-50 o genera el contexto base por separado.")
            return 1

        cmd2 = [
            sys.executable, script_50,
            "--chip", args.chip,
            "--radio", str(args.radio),
            "--altura-piso", str(args.altura_piso),
            "--ctx", ctx_base,
            "--out", out_dir_abs,
            "--fuente", args.fuente,
            "--marco", args.marco,
        ]
        if args.gpkg:
            cmd2.extend(["--gpkg", args.gpkg])
        rc = run_step(cmd2, project_root, "PASO 2: F1_CONTEXTO50_FETCH_v01 (contexto 50m)")
        if rc != 0:
            return rc

    # ── Crear archivo canónico para el canvas (contexto50-actual.json) ─────────
    ctx50_real = os.path.join(out_dir_abs, f"{args.chip}-contexto50.json")
    ctx50_canonical = os.path.join(out_dir_abs, "contexto50-actual.json")
    if os.path.exists(ctx50_real):
        try:
            import shutil
            shutil.copy2(ctx50_real, ctx50_canonical)
            print(f"   Canonico: {ctx50_canonical}")
        except Exception as e:
            print(f"   AVISO: No se pudo crear canonico: {e}")

    # ── Etapa opcional: enviar lote/vias/espacios_publicos a ArchiCAD vía Tapir ──
    # Determinar puerto Tapir: usar detectar-puerto-archicad.py y fallback a
    # --tapir-puerto si la detección falla.
    if args.enviar_archicad:
        # Ejecutar script de detección de puerto
        detect_script = os.path.join(project_root, "scripts", "utilities", "detectar-puerto-archicad.py")
        rc_detect = subprocess.run(
            [sys.executable, detect_script, "--json"],
            capture_output=True, text=True, cwd=project_root
        )
        detect_result = {}
        if rc_detect.returncode == 0:
            try:
                detect_result = json.loads(rc_detect.stdout)
            except Exception:
                detect_result = {}
        # Usar puerto detectado si ArchiCAD respondió, si no, fallback al argumento
        if detect_result.get("puerto") and detect_result.get("resultados"):
            # Verificar que al menos un puerto tenga estado "tapir"
            puerto_tapir = None
            for r in detect_result["resultados"]:
                if r.get("estado") == "tapir":
                    puerto_tapir = r["puerto"]
                    break
            if puerto_tapir is None and detect_result.get("puerto"):
                # Fallback: usar el puerto detectado aunque no sea tapir estricto
                puerto_tapir = detect_result["puerto"]
        else:
            puerto_tapir = args.tapir_puerto

        ctx_file = os.path.join(out_dir_abs, f"{args.chip}-contexto.json")
        rc_tapir = _enviar_a_archicad(ctx_file, args.chip, puerto=puerto_tapir)
        if rc_tapir != 0:
            return rc_tapir

    print(f"\n{'='*60}")
    print(f"CONTEXTO COMPLETO GENERADO para CHIP {args.chip}")
    print(f"   {ctx_base}")
    print(f"   {ctx50_real}")
    print(f"   {os.path.join(out_dir_abs, f'{args.chip}-contexto50.geojson')}")
    print(f"   Canonico para canvas: {ctx50_canonical}")
    print(f"{'='*60}")
    return 0


# ============================================================================
# Envío a ArchiCAD vía Tapir (JSON/Python API, puerto 19724)
# ============================================================================
def _conectar_tapir(puerto=19723):
    """Abre CommandConnection a ArchiCAD. Devuelve conn o None."""
    try:
        from archicad import ACConnection
        conn = ACConnection.connect(port=puerto)
        return conn
    except Exception as e:
        print("   AVISO: No se pudo conectar a ArchiCAD Tapir puerto {}: {}".format(puerto, e))
        return None


def _elementos_desde_json(ctx_path, chip):
    """Lee <CHIP>-contexto.json y devuelve lista de elementos para mapear a ArchiCAD.

    Elementos:
      - lote_objetivo      -> zona en 00-00-10_Lote_proyecto (altura 0, referencia de terreno)
      - vias_oficiales     -> linea (wall delgado) en 00-20-20_Elementos_entorno_urbano
      - espacios_publicos  -> zona en 70-50-10_Zonas_verdes_publicas
    """
    if not os.path.exists(ctx_path):
        print("   ERROR: No existe el JSON de contexto: {}".format(ctx_path))
        return None
    try:
        with open(ctx_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print("   ERROR: No se pudo leer el JSON de contexto: {}".format(e))
        return None

    meta = data.get("metadata", {})
    origen = meta.get("origen_sirgas", {})
    dx = float(origen.get("x", 0.0))
    dy = float(origen.get("y", 0.0))

    elementos = []

    # Lote objetivo como zona de referencia (placa a cota 0 local).
    lote = data.get("lote_objetivo", {})
    lote_verts = lote.get("vertices_3d_local", [])
    if lote_verts and len(lote_verts) >= 3:
        # Aceptar coordenadas 2D [x,y] o 3D [x,y,z]
        poligono = []
        for v in lote_verts:
            if len(v) >= 3:
                poligono.append([round(v[0] - dx, 3), round(v[1] - dy, 3)])
            elif len(v) == 2:
                poligono.append([round(v[0] - dx, 3), round(v[1] - dy, 3)])
            else:
                poligono.append([round(v[0], 3), round(v[1], 3)])
        elementos.append({
            "tipo": "zone",
            "vertices": poligono,
            "altura_m": 0.0,
            "capa": "00-00-10_Lote_proyecto",
            "nombre": "Lote " + chip,
        })

    # Vías oficiales como líneas (walls delgados de -0.15 m de elevación en planta, por debajo del nivel L01).
    for via in data.get("vias_oficiales", []):
        coords = via.get("coordenadas_local", [])
        if len(coords) >= 2:
            pts = []
            for c in coords:
                if len(c) >= 3:
                    pts.append([round(c[0] - dx, 3), round(c[1] - dy, 3)])
                elif len(c) == 2:
                    pts.append([round(c[0] - dx, 3), round(c[1] - dy, 3)])
                else:
                    pts.append([round(c[0], 3), round(c[1], 3)])
            elementos.append({
                "tipo": "wall",
                "vertices": pts,
                "altura_m": -0.15,
                "capa": "00-20-20_Elementos_entorno_urbano",
                "nombre": via.get("nombre") or via.get("codigo") or "Via",
            })

    # Espacios públicos como zonas.
    for ep in data.get("espacios_publicos", []):
        coords = ep.get("coordenadas_local", [])
        if len(coords) >= 3:
            poligono = []
            for c in coords:
                if len(c) >= 3:
                    poligono.append([round(c[0] - dx, 3), round(c[1] - dy, 3)])
                elif len(c) == 2:
                    poligono.append([round(c[0] - dx, 3), round(c[1] - dy, 3)])
                else:
                    poligono.append([round(c[0], 3), round(c[1], 3)])
            elementos.append({
                "tipo": "zone",
                "vertices": poligono,
                "altura_m": 0.0,
                "capa": "70-50-10_Zonas_verdes_publicas",
                "nombre": ep.get("nombre") or "Espacio publico",
            })

    return elementos


def _enviar_a_archicad(ctx_path, chip, puerto=19724):
    """Envía lote/vias/espacios_publicos del JSON de contexto a ArchiCAD vía Tapir.

    Retorna 0 si se envió todo, 1 si falló la conexión o el envío.
    """
    print("\n" + "=" * 60)
    print(">>> ETAPA OPCIONAL: Enviar contexto a ArchiCAD (Tapir puerto {})".format(puerto))
    print("=" * 60)

    conn = _conectar_tapir(puerto)
    if conn is None:
        print("   [FALLO] No se pudo conectar a ArchiCAD. Asegúrese de que ArchiCAD esté abierto y escuche en el puerto {}.".format(puerto))
        return 1

    elementos = _elementos_desde_json(ctx_path, chip)
    if elementos is None:
        return 1
    if not elementos:
        print("   AVISO: No hay elementos para enviar (lote, vías o espacios públicos vacíos).")
        return 0

    commands = conn.commands
    enviados = 0
    errores = 0
    for el in elementos:
        try:
            verts = el["vertices"]
            if el["tipo"] == "zone":
                res = commands.CreateZone(polygon=verts, layer=el["capa"])
            elif el["tipo"] == "wall":
                res = commands.CreateWall(polygon=verts, height=float(el["altura_m"]), layer=el["capa"])
            elif el["tipo"] == "slab":
                res = commands.CreateSlab(polygon=verts, thickness=float(el["altura_m"]), layer=el["capa"])
            else:
                print("   AVISO: tipo no soportado {} para {}".format(el["tipo"], el.get("nombre")))
                errores += 1
                continue
            print("   OK: {} -> {} (id={})".format(el["tipo"], el["capa"], res))
            enviados += 1
        except Exception as e:
            print("   ERROR: {} -> {}: {}".format(el["tipo"], el.get("nombre"), e))
            errores += 1

    print("   Enviados: {} | Errores: {}".format(enviados, errores))
    if errores and enviados == 0:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())