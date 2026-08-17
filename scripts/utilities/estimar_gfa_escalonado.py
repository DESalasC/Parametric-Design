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


def _recortar_por_linea(poly, a, b, retiro):
    """Sutherland-Hodgman contra la linea desplazada del segmento (a,b)
    hacia adentro (normal interior por orientacion del poligono)."""
    dx = b[0] - a[0]
    dy = b[1] - a[1]
    largo = math.hypot(dx, dy) or 1.0
    ccw = area_signada(poly + [poly[0]]) > 0
    if ccw:
        nx, ny = -dy / largo, dx / largo
    else:
        nx, ny = dy / largo, -dx / largo
    k = nx * (a[0] + nx * retiro) + ny * (a[1] + ny * retiro)

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
    return nuevo


def desplazar(pts, retiros):
    """Recorte de la huella por semiplanos (Sutherland-Hodgman): para cada lado
    con retiro s, se recorta el poligono contra la linea desplazada hacia el
    interior. La normal interior se deduce de la ORIENTACION del poligono
    (robusto en concavos, a diferencia del centroide)."""
    n = len(pts) - 1
    poly = list(pts[:-1])
    for i in range(n):
        sb = retiros.get(i, 0.0)
        if sb < 0.01:
            continue
        a, b = pts[i], pts[(i + 1) % n]
        poly = _recortar_por_linea(poly, a, b, sb)
        if len(poly) < 3:
            break
    if len(poly) < 3:
        return pts
    poly.append(poly[0])
    return poly


def desplazar_subsegmentos(pts, sub_segmentos):
    """v08 - Recorte por semiplanos con SUB-SEGMENTOS: lista de
    ((p1, p2), retiro) por vecino. Cada sub-segmento recorta con SU retiro
    (altura de SU vecino)."""
    poly = list(pts[:-1])
    for (a, b), sb in sub_segmentos:
        if sb < 0.01:
            continue
        poly = _recortar_por_linea(poly, a, b, sb)
        if len(poly) < 3:
            break
    if len(poly) < 3:
        return pts
    poly.append(poly[0])
    return poly


def subdividir_lado(p1, p2, alturas):
    """Subdivide (p1,p2) en partes iguales segun el numero de vecinos.
    Devuelve lista de sub-segmentos (p1j, p2j)."""
    n = len(alturas)
    if n <= 1:
        return [(p1, p2)]
    out = []
    for j in range(n):
        a = (p1[0] + (p2[0] - p1[0]) * j / n, p1[1] + (p2[1] - p1[1]) * j / n)
        b = (p1[0] + (p2[0] - p1[0]) * (j + 1) / n, p1[1] + (p2[1] - p1[1]) * (j + 1) / n)
        out.append((a, b))
    return out


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
    ap.add_argument("--vecinos-por-lado", default="",
                    help='Alturas por lateral: "<id_lado>:<alt1>,<alt2>;<id2>:..." '
                         '(p. ej. "4:6,9;7:6"; v08: cada lateral se subdivide por vecino)')
    ap.add_argument("--clasificacion", default="",
                    help="Clasificacion por segmento (F=Frontal, E=EspacioPublico, "
                         "L=Lateral, P=Posterior). Si vacia, se intenta inferir.")
    ap.add_argument("--forzar-empate", action="store_true",
                    help="Anexo 5 SECCION 1.9.c: el empate lateral aplica SOLO a "
                         "predios con lado POSTERIOR; sin 'P' en la clasificacion "
                         "no aplica (solo sismica 2%% x h). Este flag lo fuerza.")
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

    # Anexo 5, SECCION 1.9.c: el empate volumetrico lateral aplica SOLO a
    # predios con lado POSTERIOR (lote interior/fondo). Sin lado posterior
    # (dos laterales + esquina) -> solo separacion sismica NSR-10 A.6.5.
    empate_activo = args.forzar_empate or ("P" in args.clasificacion.upper())
    if not empate_activo:
        print("Empate 1.9.c: NO aplica (sin lado posterior) -> solo sismica 2%% x h")
    else:
        print("Empate 1.9.c: activo (lado posterior presente o --forzar-empate)")

    vecinos_por_lado = {}
    if args.vecinos_por_lado:
        try:
            for parte in args.vecinos_por_lado.split(";"):
                if not parte.strip():
                    continue
                lid, alts = parte.split(":")
                vecinos_por_lado[int(lid)] = [float(x) for x in alts.split(",")]
        except Exception as exc:
            print("AVISO: --vecinos-por-lado invalido (%s)" % exc)

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
    n_seg = len(pts) - 1
    for nv in range(1, args.pisos + 1):
        h_piso = nv * h
        sism = args.nsr_coef * h_piso if nv > 1 else 0.0
        sub_segs = []
        escalonado = False
        ret_lat = 0.0
        for i in range(n_seg):
            a, b = pts[i], pts[(i + 1) % n_seg]
            c = clases[i]
            if c == "Lateral" and i in vecinos_por_lado:
                alts = vecinos_por_lado[i]
                subs = subdividir_lado(a, b, alts)
                for (sa, sb2), h_v in zip(subs, alts):
                    r = 0.0
                    if empate_activo and h_piso > h_v:
                        r = max(0.2 * (h_piso - h_v), args.empate_min)
                    r = max(r, sism)
                    sub_segs.append(((sa, sb2), r))
                    ret_lat = max(ret_lat, r)
                    if r > 0:
                        escalonado = True
            elif c == "Lateral":
                r = 0.0
                if empate_activo and args.altura_vecinos > 0 and h_piso > args.altura_vecinos:
                    r = max(0.2 * (h_piso - args.altura_vecinos), args.empate_min)
                r = max(r, sism)
                sub_segs.append(((a, b), r))
                ret_lat = max(ret_lat, r)
                if r > 0:
                    escalonado = True
            elif c == "Frontal":
                r = args.antejardin
                if nv > 1 and args.voladizo_frontal > 0:
                    r = max(0.0, r - args.voladizo_frontal)
                sub_segs.append(((a, b), r))
            else:
                sub_segs.append(((a, b), 0.0))
        rec = desplazar_subsegmentos(pts, sub_segs)
        a = area_poly(rec)
        areas.append(a)
        detalle.append({"piso": nv, "altura_m": round(h_piso, 2),
                        "escalonado": escalonado, "area_m2": round(a, 2),
                        "voladizo_m": round(args.voladizo_frontal if nv > 1 else 0.0, 2),
                        "retiro_lateral_m": round(ret_lat, 2)})

    gfa = sum(areas)
    print("Lados: %s" % ", ".join(clases))
    print("Vecinos por lado: %s" % (json.dumps(vecinos_por_lado) if vecinos_por_lado else "(global)"))
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
