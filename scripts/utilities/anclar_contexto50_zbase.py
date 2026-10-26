# -*- coding: utf-8 -*-
"""Ancla los edificios del contexto 50 m al terreno (z_base_m por edificio).

Motivo (encargo P2, 2026-09-28): los volumenes vecinos se extruian desde z=0 y en
lotes inclinados (La Candelaria) quedaban todos al nivel 0.0. Este script agrega
`z_base_m` a cada edificio muestreando el MDT urbano (servicio Catastro, REST),
reutilizando las funciones del fetch v7.

Marco: los vertices del contexto50 estan en el marco LOCAL del canvas. La
traslacion a SIRGAS (ESRI:102233) sale de metadata.traslacion_aplicada (o de
origen_sirgas + ancla_canvas_local). La cota se escribe EN EL MARCO DEL CANVAS:
z_local = z_MDT - z_ref, con z_ref = origen_sirgas.z + ancla_canvas_local.z
(asi el vertice-ancla del lote queda en z=0, igual que las curvas y la malla).

Modos de muestreo (--muestreo):
  huella     (default, decision operador 2026-10-25): centroide + 4 extremos de
             la huella (min x, max x, min y, max y). `z_base_m` = MINIMO de las
             cotas validas: el volumen apoya en el punto mas bajo de su huella y
             no flota en el borde de aguas abajo. Se guardan tambien
             `z_base_centroide_m`, `z_base_min_m` y `z_base_max_m`.
  centroide  comportamiento historico: una sola consulta por edificio.

Uso:
  python anclar_contexto50_zbase.py --chip AAA0030JKOE [--dry-run] [--limite N]
  python anclar_contexto50_zbase.py --chip AAA0030JKOE --muestreo centroide

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


def anillo(e):
    """Anillo exterior del edificio (sin el vertice de cierre)."""
    ring = None
    anillos = e.get("anillos")
    if isinstance(anillos, list) and anillos:
        ring = anillos[0]
    if ring is None:
        ring = e.get("vertices")
    pts = []
    for p in (ring or []):
        try:
            pts.append((float(p[0]), float(p[1])))
        except Exception:
            pass
    if len(pts) >= 2 and abs(pts[0][0] - pts[-1][0]) < 1e-9 and abs(pts[0][1] - pts[-1][1]) < 1e-9:
        pts.pop()
    return pts


def centroide_anillo(ring):
    pts = ring or []
    if not pts:
        return None
    n = len(pts)
    return sum(p[0] for p in pts) / n, sum(p[1] for p in pts) / n


def puntos_huella(ring, tol=0.5):
    """Centroide + extremos (min x, max x, min y, max y) deduplicados a `tol` m."""
    c = centroide_anillo(ring)
    if c is None:
        return []
    cand = [c]
    if ring:
        cand.append(min(ring, key=lambda p: p[0]))
        cand.append(max(ring, key=lambda p: p[0]))
        cand.append(min(ring, key=lambda p: p[1]))
        cand.append(max(ring, key=lambda p: p[1]))
    out = []
    for p in cand:
        if all((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2 >= tol * tol for q in out):
            out.append(p)
    return out


def consultar_puntos(puntos, fetch, crs, pausa=0.05, reintentos=2):
    """Consulta el MDT punto a punto con reintentos. Devuelve lista de z o None."""
    from pyproj import Transformer

    tr = Transformer.from_crs(crs, fetch.CRS_METRIC, always_xy=True)
    zs = []
    t0 = time.time()
    for k, (x, y) in enumerate(puntos):
        xm, ym = tr.transform(x, y)
        z = None
        for intento in range(reintentos + 1):
            z = fetch.get_elevation_from_api(xm, ym)
            if z is not None:
                break
            time.sleep(0.4 * (intento + 1))
        zs.append(z)
        if pausa:
            time.sleep(pausa)
        if (k + 1) % 50 == 0:
            print("  %d/%d puntos (%.1f s)" % (k + 1, len(puntos), time.time() - t0))
    return zs


def main():
    ap = argparse.ArgumentParser(description="Agrega z_base_m (MDT) a <CHIP>-contexto50.json")
    ap.add_argument("--chip", required=True)
    ap.add_argument("--muestreo", choices=("huella", "centroide"), default="huella",
                    help="huella = min de centroide+extremos (default); centroide = historico")
    ap.add_argument("--pausa", type=float, default=0.05, help="pausa entre consultas (s)")
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
    fetch = cargar_fetch_v7()

    n_ok = n_fail = 0
    n_puntos_total = 0
    t0 = time.time()

    if args.muestreo == "centroide":
        puntos = []
        idx = []
        for i, e in enumerate(trabajo):
            c = centroide_anillo(anillo(e))
            if c is None:
                continue
            puntos.append((c[0] + tx, c[1] + ty))
            idx.append(i)
        print("Consultando MDT (centroide) para {0} edificios...".format(len(puntos)))
        zs = consultar_puntos(puntos, fetch, crs, pausa=args.pausa)
        n_puntos_total = len(puntos)
        for k, i in enumerate(idx):
            z = zs[k] if k < len(zs) else None
            if z is None:
                n_fail += 1
                continue
            trabajo[i]["z_base_m"] = round(float(z) - z_ref, 2)
            trabajo[i]["z_base_centroide_m"] = trabajo[i]["z_base_m"]
            trabajo[i]["z_base_min_m"] = trabajo[i]["z_base_m"]
            trabajo[i]["z_base_max_m"] = trabajo[i]["z_base_m"]
            trabajo[i]["z_base_n_puntos"] = 1
            trabajo[i]["z_base_metodo"] = "centroide"
            n_ok += 1
        metodo = "MDT puntual (REST Catastro) en centroide de huella; reutiliza fetch-urban-context-v7"
    else:
        grupos = []
        planos = []
        for i, e in enumerate(trabajo):
            pts = puntos_huella(anillo(e))
            if not pts:
                continue
            grupos.append({"i": i, "pts": pts})
            for (x, y) in pts:
                planos.append((x + tx, y + ty))
        print("Consultando MDT (huella) para {0} edificios / {1} puntos...".format(len(grupos), len(planos)))
        zs = consultar_puntos(planos, fetch, crs, pausa=args.pausa)
        n_puntos_total = len(planos)
        k = 0
        for g in grupos:
            vals = zs[k:k + len(g["pts"])]
            k += len(g["pts"])
            validos = [float(z) for z in vals if z is not None]
            if not validos:
                n_fail += 1
                continue
            z_min = min(validos)
            z_max = max(validos)
            # el centroide es el primer punto del grupo
            z_c = float(vals[0]) if vals and vals[0] is not None else z_min
            e = trabajo[g["i"]]
            e["z_base_m"] = round(z_min - z_ref, 2)
            e["z_base_centroide_m"] = round(z_c - z_ref, 2)
            e["z_base_min_m"] = round(z_min - z_ref, 2)
            e["z_base_max_m"] = round(z_max - z_ref, 2)
            e["z_base_n_puntos"] = len(validos)
            e["z_base_metodo"] = "min de centroide+extremos de huella"
            n_ok += 1
        metodo = ("MDT (REST Catastro) por huella: centroide + extremos (min/max x,y); "
                  "z_base_m = minimo de las cotas validas")

    meta["z_base_fuente"] = {
        "metodo": metodo,
        "fecha": time.strftime("%Y-%m-%d %H:%M"),
        "n_ok": n_ok,
        "n_fallidos": n_fail,
        "n_puntos": n_puntos_total,
        "pausa_s": args.pausa,
        "z_ref_m": round(z_ref, 3),
        "nota": ("z_base_m en el marco del canvas (z_local = z_MDT - z_ref; z_ref = "
                 "origen_sirgas.z + ancla.z; ancla del lote = 0). Modo huella: base = "
                 "punto mas bajo de la huella (no flota en el borde de aguas abajo); "
                 "z_base_centroide_m se conserva para diagnostico."),
    }
    if args.limite:
        meta["z_base_fuente"]["limite"] = args.limite
    d["metadata"] = meta

    print("resultado: {0} ok, {1} fallidos, {2} puntos, {3:.1f} s".format(
        n_ok, n_fail, n_puntos_total, time.time() - t0))
    if args.dry_run:
        print("[dry-run] no se escribe")
        return 0 if n_fail == 0 else 1

    escribir(ruta, d)
    print("escrito:", ruta)
    act = os.path.join(ROOT, "data", "pot-cache", "contexto50-actual.json")
    if os.path.isfile(act):
        a = leer(act)
        if str((a.get("metadata") or {}).get("chip", "")).upper() == chip:
            escribir(act, d)
            print("escrito:", act)
    print("OK | z_base: {0} edificios con cota, {1} fallidos".format(n_ok, n_fail))
    return 0 if n_fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
