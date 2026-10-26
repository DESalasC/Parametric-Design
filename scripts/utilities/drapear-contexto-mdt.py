# -*- coding: utf-8 -*-
"""Drapea vías y espacios públicos del contexto ETAPA1 sobre el MDT.

Regla (operador 2026-10-25):
  - VIAS: el terreno se muestrea a lo largo de cada tramo RECTO y se ajusta una
    recta z(s) por mínimos cuadrados. La vía queda con pendiente constante en el
    tramo (media en tramos largos), no vertex a vertex. Un tramo nuevo empieza
    cuando cambia el rumbo en planta más de `--ang` grados.
  - ESPACIOS PUBLICOS: muestreo DIRECTO de cada vértice del perímetro (sin ajuste).
  - Solo se drapea lo que cae dentro del buffer del lote (`--buffer`, default 75 m);
    el resto queda como referencia 2D (z=0).

Marco: `coordenadas_local` está en el marco local de ETAPA1 con z relativa a
`metadata.origen_sirgas.z`. La cota escrita es z_local = z_MDT - origen_z.

Uso:
  python drapear-contexto-mdt.py --chip AAA0030JKOE
  python drapear-contexto-mdt.py --chip AAA0030JKOE --dry-run
  python drapear-contexto-mdt.py --chip AAA0030JKOE --buffer 75 --ang 8

Escribe (con backup .bak-drape-<ts>):
  data/pot-cache/<CHIP>-contexto.json
"""
from __future__ import print_function

import argparse
import importlib.util
import io
import json
import math
import os
import shutil
import sys
import time

from shapely.geometry import LineString, Point, Polygon

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
        shutil.copy2(path, path + ".bak-drape-" + time.strftime("%Y%m%d-%H%M"))
    with io.open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def dist(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])


def rumbo(a, b):
    return math.atan2(b[1] - a[1], b[0] - a[0])


def tramos_rectos(pts, ang_deg=8.0, min_len=20.0):
    """Divide una polilínea en tramos por cambio de rumbo; fusiona cortos."""
    if len(pts) < 2:
        return []
    cortes = [0]
    for i in range(1, len(pts) - 1):
        h1 = rumbo(pts[i - 1], pts[i])
        h2 = rumbo(pts[i], pts[i + 1])
        if abs((h2 - h1 + math.pi) % (2 * math.pi) - math.pi) > math.radians(ang_deg):
            cortes.append(i)
    cortes.append(len(pts) - 1)
    out = []
    for k in range(len(cortes) - 1):
        a, b = cortes[k], cortes[k + 1]
        L = sum(dist(pts[i], pts[i + 1]) for i in range(a, b))
        if out and L < min_len:
            out[-1] = (out[-1][0], b)
        else:
            out.append((a, b))
    return [(a, b, sum(dist(pts[i], pts[i + 1]) for i in range(a, b))) for a, b in out]


def muestras_tramo(pts, a, b, max_muestras=9, paso=20.0):
    """Puntos (x,y,s) equiespaciados sobre el tramo a..b."""
    L = sum(dist(pts[i], pts[i + 1]) for i in range(a, b))
    if L <= 1e-6:
        return [(pts[a][0], pts[a][1], 0.0)]
    k = max(2, min(max_muestras, int(math.ceil(L / paso)) + 1))
    out = []
    for m in range(k):
        s_obj = L * m / float(k - 1)
        s = 0.0
        for i in range(a, b):
            d = dist(pts[i], pts[i + 1])
            if s + d >= s_obj - 1e-9:
                t = 0.0 if d <= 1e-12 else (s_obj - s) / d
                out.append((pts[i][0] + t * (pts[i + 1][0] - pts[i][0]),
                            pts[i][1] + t * (pts[i + 1][1] - pts[i][1]), s_obj))
                break
            s += d
        else:
            out.append((pts[b][0], pts[b][1], L))
    return out


def ajuste_recta(sv, zv):
    """z = a + b*s por mínimos cuadrados. Devuelve (a,b) o (mean,0)."""
    n = len(sv)
    if n < 2:
        return (zv[0] if zv else 0.0), 0.0
    ms = sum(sv) / n
    mz = sum(zv) / n
    num = sum((s - ms) * (z - mz) for s, z in zip(sv, zv))
    den = sum((s - ms) ** 2 for s in sv)
    if abs(den) < 1e-12:
        return mz, 0.0
    b = num / den
    return mz - b * ms, b


def consultar(puntos, fetch, crs, pausa=0.05, reintentos=2):
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


def dentro(buf, p):
    return buf.contains(Point(p[0], p[1])) or buf.distance(Point(p[0], p[1])) < 1e-6


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--chip", required=True)
    ap.add_argument("--buffer", type=float, default=75.0)
    ap.add_argument("--ang", type=float, default=8.0)
    ap.add_argument("--min-tramo", type=float, default=20.0)
    ap.add_argument("--pausa", type=float, default=0.05)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    chip = args.chip.strip().upper()

    ruta = os.path.join(ROOT, "data", "pot-cache", chip + "-contexto.json")
    if not os.path.isfile(ruta):
        print("[ERROR] No existe", ruta)
        return 2
    d = leer(ruta)
    meta = d.get("metadata") or {}
    origen_z = float((meta.get("origen_sirgas") or {}).get("z") or 0.0)
    crs = str(meta.get("origen_sirgas", {}).get("crs") or "ESRI:102233")
    lote = (d.get("lote_objetivo") or {}).get("vertices_3d_local") or []
    if len(lote) < 3:
        print("[ERROR] Sin lote_objetivo")
        return 2
    poly = Polygon([(v[0], v[1]) for v in lote])
    buf = poly.buffer(args.buffer)

    # ---- plan de muestras ----
    plan = []          # (x, y) en marco local
    vias_plan = []     # dict por tramo
    n_tramos = 0
    for iv, via in enumerate(d.get("vias_oficiales") or []):
        coords = via.get("coordenadas_local") or []
        pts = [(p[0], p[1]) for p in coords]
        if len(pts) < 2:
            continue
        inside = [i for i, p in enumerate(pts) if dentro(buf, p)]
        if not inside:
            continue
        # runs consecutivos
        runs = []
        start = prev = inside[0]
        for i in inside[1:]:
            if i == prev + 1:
                prev = i
            else:
                runs.append((start, prev))
                start = prev = i
        runs.append((start, prev))
        for (ra, rb) in runs:
            if rb <= ra:
                continue
            sub = pts[ra:rb + 1]
            for (a, b, L) in tramos_rectos(sub, args.ang, args.min_tramo):
                if L < 2.0:
                    continue
                ms = muestras_tramo(sub, a, b)
                vias_plan.append({"via": iv, "ra": ra, "rb": rb, "a": a, "b": b,
                                  "sub": sub, "muestras": ms, "L": L})
                for (x, y, s) in ms:
                    plan.append((x, y))
                n_tramos += 1

    ep_plan = []       # dict por vértice único
    vistos = {}
    n_ep_pts = 0
    for ie, ep in enumerate(d.get("espacios_publicos") or []):
        coords = ep.get("coordenadas_local") or []
        if len(coords) < 3:
            continue
        for ip, p in enumerate(coords):
            if not dentro(buf, p):
                continue
            key = (round(p[0], 2), round(p[1], 2))
            if key in vistos:
                ep_plan.append({"ie": ie, "ip": ip, "key": key})
                continue
            vistos[key] = len(plan)
            plan.append((p[0], p[1]))
            ep_plan.append({"ie": ie, "ip": ip, "key": key})
            n_ep_pts += 1

    print("Plan: %d tramos de via, %d muestras de via, %d vertices de EP, %d consultas"
          % (n_tramos, len(vias_plan), n_ep_pts, len(plan)))
    if not plan:
        print("Nada que drapear.")
        return 0

    fetch = cargar_fetch_v7()
    t_mdt = time.time()
    zs = consultar(plan, fetch, crs, pausa=args.pausa)
    n_fail = sum(1 for z in zs if z is None)
    print("MDT: %d ok, %d fallidos (%.1f s)" % (len(zs) - n_fail, n_fail, time.time() - t_mdt))

    # ---- asignar vias ----
    k = 0
    pred = {}   # (via, idx_global) -> [z_local]
    for t in vias_plan:
        vals = zs[k:k + len(t["muestras"])]
        k += len(t["muestras"])
        pares = [(m[2], z) for m, z in zip(t["muestras"], vals) if z is not None]
        if not pares:
            continue
        sv = [p[0] for p in pares]
        zv = [float(p[1]) for p in pares]
        a, b = ajuste_recta(sv, zv)
        # índice acumulado de s para los vértices del subtramo
        s = 0.0
        for j in range(t["a"], t["b"] + 1):
            if j > t["a"]:
                s += dist(t["sub"][j - 1], t["sub"][j])
            gi = t["ra"] + j
            pred.setdefault((t["via"], gi), []).append((a + b * s) - origen_z)
    for (iv, gi), vals in pred.items():
        via = d["vias_oficiales"][iv]
        via["coordenadas_local"][gi][2] = round(sum(vals) / len(vals), 3)

    # ---- asignar EP ----
    for e in ep_plan:
        gi = vistos[e["key"]]
        z = zs[gi] if gi < len(zs) else None
        if z is None:
            continue
        d["espacios_publicos"][e["ie"]]["coordenadas_local"][e["ip"]][2] = round(float(z) - origen_z, 3)

    meta["drape_mdt"] = {
        "fecha": time.strftime("%Y-%m-%d %H:%M"),
        "buffer_m": args.buffer,
        "origen_z": round(origen_z, 3),
        "vias": {"tramos": n_tramos,
                 "metodo": "ajuste lineal z(s) por tramo recto (media en tramos largos)",
                 "angulo_corte_deg": args.ang, "tramo_min_m": args.min_tramo},
        "espacios_publicos": {"vertices": n_ep_pts,
                              "metodo": "muestreo directo de vertices del perimetro"},
        "n_fallidos": n_fail,
        "nota": ("Solo se drapea dentro del buffer del lote; el resto queda 2D. "
                 "z_local = z_MDT - origen_sirgas.z (marco ETAPA1)."),
    }
    d["metadata"] = meta

    if args.dry_run:
        print("[dry-run] no se escribe")
        return 0 if n_fail == 0 else 1
    escribir(ruta, d)
    print("escrito:", ruta)
    return 0 if n_fail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
