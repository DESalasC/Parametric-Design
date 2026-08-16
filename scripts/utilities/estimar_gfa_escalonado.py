# -*- coding: utf-8 -*-
"""estimar_gfa_escalonado.py — Estimacion del GFA escalonado (NORMATIVA_v07) en CPython.

Replica en geometria plana pura (sin Rhino) la logica del
F1_ETAPA2_NORMATIVA_v07 para el caso AAA0127AZPA:
  1. Clasifica los lados del lote como el LADOS_v06: vertices coincidentes con
     vecinos (< 0,10 m) -> Lateral; contacto con espacio publico ->
     EspacioPublico; resto -> Frontal (via manual del operador, ausente en el
     cache POT).
  2. Retiros base: Frontal = antejardin (5,0 m), EP = 0, Lateral = 0
     (tipologia Continua; sin lado Posterior en este lote).
  3. Escalonamiento (v07): en pisos con h > altura_vecinos, retiro lateral =
     max(1/5 x (h - h_vecino), empate_min) — mayor entre POT (SECCION 1.9.c)
     y separacion sismica NSR-10 A.6.5 (coef x h).
  4. Recorta el poligono por piso (desplazamiento de lados + intersecciones,
     mismo algoritmo de build_footprint_retiros) y calcula el area (shoelace).

NOTA: estimacion SIN el patio de 3x3 (el PATIO_v02 lo genera en el canvas) —
el area base queda ~3,7% por encima de la ocupacion real de F1 (243,5 m2).

USO:  python scripts/utilities/estimar_gfa_escalonado.py [--altura-vecinos 6.0]
      [--empate-min 3.0] [--nsr-coef 0.02] [--floor-h 3.8] [--antejardin 5.0]
"""
import argparse
import json
import math
import os

BASE = os.path.join(os.path.dirname(__file__), "..", "..")
TOL_VERTICES = 0.10      # LADOS_v06: coincidencia de vertices con vecinos
TOL_CONTACTO = 0.5       # contacto con EP


def area_poly(pts):
    s = 0.0
    n = len(pts)
    for i in range(n):
        x1, y1 = pts[i]
        x2, y2 = pts[(i + 1) % n]
        s += x1 * y2 - x2 * y1
    return abs(s) / 2.0


def dist_pt_seg(p, a, b):
    x, y = p
    ax, ay = a
    bx, by = b
    dx, dy = bx - ax, by - ay
    if dx == 0 and dy == 0:
        return math.hypot(x - ax, y - ay)
    t = max(0.0, min(1.0, ((x - ax) * dx + (y - ay) * dy) / (dx * dx + dy * dy)))
    return math.hypot(x - (ax + t * dx), y - (ay + t * dy))


def punto_en_poly(p, poly):
    x, y = p
    dentro = False
    n = len(poly)
    j = n - 1
    for i in range(n):
        xi, yi = poly[i]
        xj, yj = poly[j]
        if ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / (yj - yi + 1e-12) + xi):
            dentro = not dentro
        j = i
    return dentro


def tocar_ep(seg_mid, eps):
    for ep in eps:
        if punto_en_poly(seg_mid, ep):
            return True
        for a, b in zip(ep, ep[1:] + ep[:1]):
            if dist_pt_seg(seg_mid, a, b) < TOL_CONTACTO:
                return True
    return False


def vertice_coincide_vecino(p, vecinos):
    for v in vecinos:
        for q in v:
            if math.hypot(p[0] - q[0], p[1] - q[1]) < TOL_VERTICES:
                return True
    return False


def clasificar_lados(pts, vecinos, eps):
    """LADOS_v06 simplificado: Lateral por vertices coincidentes, EP por
    contacto, resto Frontal (via manual). Devuelve lista de clases."""
    n = len(pts) - 1
    clases = []
    for i in range(n):
        a = pts[i]
        b = pts[(i + 1) % n]
        if vertice_coincide_vecino(a, vecinos) and vertice_coincide_vecino(b, vecinos):
            clases.append("Lateral")
            continue
        mid = ((a[0] + b[0]) / 2.0, (a[1] + b[1]) / 2.0)
        if tocar_ep(mid, eps):
            clases.append("EspacioPublico")
        else:
            clases.append("Frontal")
    return clases


def area_signada(pts):
    """Area con signo (positiva = sentido antihorario)."""
    s = 0.0
    n = len(pts) - 1
    for i in range(n):
        x1, y1 = pts[i]
        x2, y2 = pts[(i + 1) % n]
        s += x1 * y2 - x2 * y1
    return s / 2.0


def desplazar(pts, retiros):
    """Recorte de la huella por semiplanos (Sutherland-Hodgman): para cada lado
    con retiro s, se recorta el poligono contra la linea desplazada hacia el
    interior. La normal interior se deduce de la ORIENTACION del poligono
    (robusto en concavos, a diferencia del centroide)."""
    n = len(pts) - 1
    ccw = area_signada(pts) > 0
    poly = list(pts[:-1])
    for i in range(n):
        sb = retiros.get(i, 0.0)
        if sb < 0.01:
            continue
        a, b = pts[i], pts[(i + 1) % n]
        dx, dy = b[0] - a[0], b[1] - a[1]
        largo = math.hypot(dx, dy) or 1.0
        # normal interior: izquierda de la direccion si CCW, derecha si CW
        if ccw:
            nx, ny = -dy / largo, dx / largo
        else:
            nx, ny = dy / largo, -dx / largo
        # linea desplazada hacia adentro: (px, py) tal que nx*x + ny*y = k
        k = nx * (a[0] + nx * sb) + ny * (a[1] + ny * sb)

        def dentro(p):
            return nx * p[0] + ny * p[1] >= k - 1e-9

        def cruce(p, q):
            dp = nx * p[0] + ny * p[1] - k
            dq = nx * q[0] + ny * q[1] - k
            t = dp / (dp - dq)
            return (p[0] + t * (q[0] - p[0]), p[1] + t * (q[1] - p[1]))

        nuevo = []
        m = len(poly)
        for j in range(m):
            p = poly[j]
            q = poly[(j + 1) % m]
            dp, dq = dentro(p), dentro(q)
            if dp:
                nuevo.append(p)
            if dp != dq:
                nuevo.append(cruce(p, q))
        poly = nuevo
        if len(poly) < 3:
            break
    if len(poly) < 3:
        return pts
    poly.append(poly[0])
    return poly


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--chip", default="AAA0127AZPA")
    ap.add_argument("--altura-vecinos", type=float, default=6.0)
    ap.add_argument("--empate-min", type=float, default=3.0)
    ap.add_argument("--nsr-coef", type=float, default=0.02)
    ap.add_argument("--floor-h", type=float, default=3.8)
    ap.add_argument("--antejardin", type=float, default=5.0)
    ap.add_argument("--pisos", type=int, default=6)
    ap.add_argument("--voladizo-frontal", type=float, default=0.0,
                    help="Voladizo frontal en pisos != 1 (SECCION 1.13.b); "
                         "p. ej. 0.8 para via de 12,9 m con antejardin")
    ap.add_argument("--clasificacion", default="",
                    help="Clasificacion por segmento (F=Frontal, E=EspacioPublico, "
                         "L=Lateral, P=Posterior). Si vacia, se intenta inferir.")
    args = ap.parse_args()

    ruta = os.path.join(BASE, "data", "pot-cache", args.chip + "-contexto.json")
    with open(ruta, "r", encoding="utf-8") as f:
        ctx = json.load(f)
    pts = [tuple(v[:2]) for v in ctx["lote_objetivo"]["vertices_3d_local"]]
    vecinos = []
    for vec in ctx.get("vecinos", []):
        v = vec.get("vertices_3d_local") or vec.get("coordenadas_local") or []
        if v:
            vecinos.append([tuple(p[:2]) for p in v])
    eps = []
    for ep in ctx.get("espacios_publicos", []):
        e = ep.get("vertices_3d_local") or ep.get("coordenadas_local") or []
        if e:
            eps.append([tuple(p[:2]) for p in e])
    if not vecinos and isinstance(ctx.get("vecinos"), list) and ctx["vecinos"] and isinstance(ctx["vecinos"][0], list):
        vecinos = [[tuple(v[:2]) for v in vec] for vec in ctx["vecinos"]]

    if args.clasificacion:
        mapa = {"F": "Frontal", "E": "EspacioPublico", "L": "Lateral",
                "P": "Posterior"}
        letras = list(args.clasificacion.upper())
        if len(letras) != len(pts) - 1:
            print("ERROR: clasificacion debe tener %d letras (tiene %d)" % (
                len(pts) - 1, len(letras)))
            return 1
        clases = [mapa.get(c, "Lateral") for c in letras]
    else:
        clases = clasificar_lados(pts, vecinos, eps)
    retiros_base = {}
    for i, c in enumerate(clases):
        if c == "Frontal":
            retiros_base[i] = args.antejardin
        elif c == "EspacioPublico":
            retiros_base[i] = 0.0
        else:
            retiros_base[i] = 0.0

    areas = []
    detalle = []
    h = args.floor_h
    for nv in range(1, args.pisos + 1):
        h_piso = nv * h
        retiros_nv = dict(retiros_base)
        escalonado = False
        if h_piso > args.altura_vecinos:
            r_empate = max(0.2 * (h_piso - args.altura_vecinos), args.empate_min)
            r_sismica = args.nsr_coef * h_piso
            r_lat = max(r_empate, r_sismica)
            for i, c in enumerate(clases):
                if c == "Lateral":
                    retiros_nv[i] = max(retiros_nv.get(i, 0.0), r_lat)
            escalonado = True
        # Voladizo (SECCION 1.13): pisos != 1, solo lados Frontal
        if nv > 1 and args.voladizo_frontal > 0:
            for i, c in enumerate(clases):
                if c == "Frontal":
                    retiros_nv[i] = max(0.0, retiros_nv.get(i, 0.0) - args.voladizo_frontal)
        rec = desplazar(pts, retiros_nv)
        a = area_poly(rec)
        areas.append(a)
        detalle.append({"piso": nv, "altura_m": round(h_piso, 2),
                        "escalonado": escalonado, "area_m2": round(a, 2),
                        "voladizo_m": round(args.voladizo_frontal if nv > 1 else 0.0, 2),
                        "retiro_lateral_m": round(max([retiros_nv.get(i, 0.0)
                                                      for i, c in enumerate(clases) if c == "Lateral"] or [0.0]), 2)})

    gfa = sum(areas)
    print("Lados: %s" % ", ".join(clases))
    print("GFA base (sin escalonar): %.1f m2" % (areas[0] * args.pisos))
    print("GFA ESCALONADO%s: %.1f m2  (-%.1f%% vs base)" % (
        " + voladizo %.2f m" % args.voladizo_frontal if args.voladizo_frontal > 0 else "",
        gfa, 100 * (1 - gfa / (areas[0] * args.pisos))))
    for d in detalle:
        print("  P%s h=%5.1f  area=%7.1f m2  retiro_lat=%4.2f m  voladizo=%4.2f m  %s" % (
            d["piso"], d["altura_m"], d["area_m2"], d["retiro_lateral_m"],
            d["voladizo_m"], "ESCALONADO" if d["escalonado"] else ""))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
