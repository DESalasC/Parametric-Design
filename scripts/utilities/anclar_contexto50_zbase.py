# -*- coding: utf-8 -*-
"""Ancla los edificios del contexto 50 m al terreno (z_base_m por edificio).

Motivo (encargo P2, 2026-09-28): los volumenes vecinos se extruian desde z=0 y en
lotes inclinados (La Candelaria) quedaban todos al nivel 0.0. Este script agrega
`z_base_m` a cada edificio muestreando el MDT urbano (servicio Catastro, REST),
reutilizando las funciones del fetch v7.

Marco: los vertices del contexto50 estan en el marco LOCAL del canvas. La
traslacion a SIRGAS (ESRI:102233) sale de metadata.traslacion_aplicada (o de
origen_sirgas + ancla_canvas_local). La muestra es puntual en el centroide de la
huella (tolerancia documentada +-0.5 m).

La cota se escribe EN EL MARCO DEL CANVAS: z_local = z_MDT - z_ref, con
z_ref = origen_sirgas.z + ancla_canvas_local.z (asi el vertice-ancla del lote
queda en z=0, igual que las curvas y la malla del canvas).

Uso:
  python anclar_contexto50_zbase.py --chip AAA0030JKOE [--dry-run] [--limite N]

Escribe (con backup .bak-zbase-<ts>):
  data/pot-cache/<CHIP>-contexto50.json
  data/pot-cache/contexto50-actual.json   (si el chip coincide)
"""
import argparse
import importlib.util
import io
import json
import os
import shutil
import sys
import time

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
FETCH_V7 = os.path.join(ROOT, "scripts", "utilities", "fetch-urban-context-v7.py")


def cargar_fetch_v7():
    spec = importlib.util.spec_from_file_location("fetch_urban_context_v7", FETCH_V7)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def leer(path):
    with io.open(path, "rb") as f:
        return json.loads(f.read().decode("utf-8"))


def escribir(path, data):
    if os.path.exists(path):
        shutil.copy2(path, path + ".bak-zbase-" + time.strftime("%Y%m%d-%H%M"))
    with io.open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def traslacion(meta):
    """Traslacion local->SIRGAS (ESRI:102233) desde metadata."""
    t = meta.get("traslacion_aplicada") or {}
    if t.get("x") is not None and t.get("y") is not None:
        return float(t["x"]), float(t["y"])
    og = meta.get("origen_sirgas") or {}
    an = meta.get("ancla_canvas_local") or {}
    return (float(og.get("x", 0.0)) + float(an.get("x", 0.0)),
            float(og.get("y", 0.0)) + float(an.get("y", 0.0)))


def z_ref_datum(meta):
    """Origen vertical del canvas: z_local = z_SIRGAS - z_ref (ancla del lote = 0)."""
    og = meta.get("origen_sirgas") or {}
    an = meta.get("ancla_canvas_local") or {}
    try:
        return float(og.get("z", 0.0)) + float(an.get("z", 0.0))
    except Exception:
        return 0.0


def centroide_anillo(ring):
    pts = []
    for p in (ring or []):
        try:
            pts.append((float(p[0]), float(p[1])))
        except Exception:
            pass
    if len(pts) >= 2 and abs(pts[0][0] - pts[-1][0]) < 1e-9 and abs(pts[0][1] - pts[-1][1]) < 1e-9:
        pts.pop()
    if not pts:
        return None
    n = len(pts)
    return sum(p[0] for p in pts) / n, sum(p[1] for p in pts) / n


def main():
    ap = argparse.ArgumentParser(description="Agrega z_base_m (MDT) a <CHIP>-contexto50.json")
    ap.add_argument("--chip", required=True)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--limite", type=int, default=0, help="Solo los primeros N edificios (pruebas)")
    args = ap.parse_args()
    chip = args.chip.strip().upper()

    ruta = os.path.join(ROOT, "data", "pot-cache", chip + "-contexto50.json")
    if not os.path.isfile(ruta):
        print("[ERROR] No existe", ruta)
        return 2
    d = leer(ruta)
    meta = d.get("metadata") or {}
    tx, ty = traslacion(meta)
    z_ref = z_ref_datum(meta)
    crs = str(meta.get("crs_fuente") or "ESRI:102233")
    edificios = d.get("edificios") or []
    if not edificios:
        print("[ERROR] Sin 'edificios' en el JSON")
        return 2

    trabajo = edificios[:args.limite] if args.limite else edificios
    puntos = []
    idx_con_punto = []
    for i, e in enumerate(trabajo):
        if not isinstance(e, dict):
            continue
        ring = None
        anillos = e.get("anillos")
        if isinstance(anillos, list) and anillos:
            ring = anillos[0]
        if ring is None:
            ring = e.get("vertices")
        c = centroide_anillo(ring)
        if c is None:
            continue
        puntos.append((c[0] + tx, c[1] + ty))
        idx_con_punto.append(i)

    if not puntos:
        print("[ERROR] Sin centroides utilizables")
        return 2

    fetch = cargar_fetch_v7()
    print("Consultando MDT para {0} edificios...".format(len(puntos)))
    zs = fetch.extract_elevations_online(puntos, points_crs=crs)

    n_ok = n_fail = 0
    for k, i in enumerate(idx_con_punto):
        z = zs[k] if k < len(zs) else None
        if z is None:
            n_fail += 1
            continue
        trabajo[i]["z_base_m"] = round(float(z) - z_ref, 2)
        n_ok += 1

    meta["z_base_fuente"] = {
        "metodo": "MDT puntual (REST Catastro) en centroide de huella; reutiliza fetch-urban-context-v7",
        "fecha": time.strftime("%Y-%m-%d %H:%M"),
        "n_ok": n_ok,
        "n_fallidos": n_fail,
        "z_ref_m": round(z_ref, 3),
        "nota": ("z_base_m en el marco del canvas (z_local = z_MDT - z_ref; z_ref = "
                 "origen_sirgas.z + ancla.z; ancla del lote = 0). Muestra puntual; "
                 "tolerancia +-0.5 m. Sin z_base_m los volumenes se extruyen desde z=0."),
    }
    if args.limite:
        meta["z_base_fuente"]["limite"] = args.limite
    d["metadata"] = meta

    if args.dry_run:
        print("[dry-run] n_ok={0} n_fallidos={1} (no se escribe)".format(n_ok, n_fail))
        return 0

    escribir(ruta, d)
    print("escrito:", ruta)
    act = os.path.join(ROOT, "data", "pot-cache", "contexto50-actual.json")
    if os.path.isfile(act):
        a = leer(act)
        if str((a.get("metadata") or {}).get("chip", "")).upper() == chip:
            escribir(act, d)
            print("escrito:", act)
    print("OK | z_base: {0} edificios con cota, {1} fallidos".format(n_ok, n_fail))
    return 0


if __name__ == "__main__":
    sys.exit(main())
