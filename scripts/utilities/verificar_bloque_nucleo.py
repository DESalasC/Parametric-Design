# -*- coding: utf-8 -*-
"""verificar_bloque_nucleo.py - QA: verifica que el BLOQUE del nucleo
(5,4 x 9,0 m, centrado en el centroide del piso 1) quepa dentro de los
envelopes de TODOS los pisos del caso (escalonados + voladizos).

Si el bloque sobresale en algun piso, la exclusion del nucleo del
F3_VOLUM_GENERADOR_v07 falla (nunca geometria intersectante) y el piso se
omite. Este script intersecta el rectangulo del bloque contra cada poligono
de piso (recorte por semiplanos, mismo algoritmo del estimador) y reporta
el area contenida por piso (48,6 m2 = cabe completo).

USO:  python scripts/utilities/verificar_bloque_nucleo.py [--altura-vecinos 6.0]
      [--voladizo-frontal 0.8] [--clasificacion EEELLLFLL] [--floor-h 3.8]
      [--antejardin 5.0] [--bloque-ancho 5.4] [--bloque-largo 9.0]
"""
import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import estimar_gfa_escalonado as e

BASE = os.path.join(os.path.dirname(__file__), "..", "..")


def centroide_poly(poly):
    """Centroide de un poligono (lista con cierre implicito)."""
    n = len(poly)
    a = 0.0
    cx = 0.0
    cy = 0.0
    for i in range(n):
        x1, y1 = poly[i]
        x2, y2 = poly[(i + 1) % n]
        cr = x1 * y2 - x2 * y1
        a += cr
        cx += (x1 + x2) * cr
        cy += (y1 + y2) * cr
    a /= 2.0
    if abs(a) < 1e-12:
        return (0.0, 0.0)
    return (cx / (6.0 * a), cy / (6.0 * a))


def rectangulo_bloque(cx, cy, ancho, largo):
    """Rectangulo del bloque en sentido HORARIO (el lote del caso A es CW;
    _recortar_por_linea infiere la normal de la orientacion del poligono)."""
    a2, l2 = ancho / 2.0, largo / 2.0
    return [(cx - a2, cy - l2), (cx - a2, cy + l2),
            (cx + a2, cy + l2), (cx + a2, cy - l2)]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--chip", default="AAA0127AZPA")
    ap.add_argument("--altura-vecinos", type=float, default=6.0)
    ap.add_argument("--voladizo-frontal", type=float, default=0.8)
    ap.add_argument("--clasificacion", default="EEELLLFLL")
    ap.add_argument("--floor-h", type=float, default=3.8)
    ap.add_argument("--antejardin", type=float, default=5.0)
    ap.add_argument("--empate-min", type=float, default=3.0)
    ap.add_argument("--nsr-coef", type=float, default=0.02)
    ap.add_argument("--pisos", type=int, default=6)
    ap.add_argument("--bloque-ancho", type=float, default=5.4)
    ap.add_argument("--bloque-largo", type=float, default=9.0)
    ap.add_argument("--vecinos-por-lado", default="")
    ap.add_argument("--forzar-empate", action="store_true",
                    help="Fuerza el empate 1.9.c (por defecto solo aplica con lado Posterior)")
    args = ap.parse_args()

    ruta = os.path.join(BASE, "data", "pot-cache", args.chip + "-contexto.json")
    with open(ruta, "r", encoding="utf-8") as f:
        ctx = json.load(f)
    pts = [tuple(v[:2]) for v in ctx["lote_objetivo"]["vertices_3d_local"]]
    mapa = {"F": "Frontal", "E": "EspacioPublico", "L": "Lateral", "P": "Posterior"}
    clases = [mapa[c] for c in args.clasificacion.upper()]
    # Anexo 5, SECCION 1.9.c: empate solo con lado POSTERIOR; sin el -> solo sismica
    empate_activo = args.forzar_empate or ("P" in args.clasificacion.upper())
    if not empate_activo:
        print("Empate 1.9.c: NO aplica (sin lado posterior) -> solo sismica 2% x h")

    vecinos_por_lado = {}
    if args.vecinos_por_lado:
        for parte in args.vecinos_por_lado.split(";"):
            lid, alts = parte.split(":")
            vecinos_por_lado[int(lid)] = [float(x) for x in alts.split(",")]

    n_seg = len(pts) - 1
    h = args.floor_h
    pisos_poly = []
    for nv in range(1, args.pisos + 1):
        h_piso = nv * h
        sism = args.nsr_coef * h_piso if nv > 1 else 0.0
        sub_segs = []
        for i in range(n_seg):
            a, b = pts[i], pts[(i + 1) % n_seg]
            c = clases[i]
            if c == "Lateral" and i in vecinos_por_lado:
                alts = vecinos_por_lado[i]
                subs = e.subdividir_lado(a, b, alts)
                for (sa, sb2), h_v in zip(subs, alts):
                    r = max(0.2 * (h_piso - h_v), args.empate_min) \
                        if (empate_activo and h_piso > h_v) else 0.0
                    sub_segs.append(((sa, sb2), max(r, sism)))
            elif c == "Lateral":
                r = max(0.2 * (h_piso - args.altura_vecinos), args.empate_min) \
                    if (empate_activo and args.altura_vecinos > 0 and h_piso > args.altura_vecinos) else 0.0
                sub_segs.append(((a, b), max(r, sism)))
            elif c == "Frontal":
                r = args.antejardin
                if nv > 1 and args.voladizo_frontal > 0:
                    r = max(0.0, r - args.voladizo_frontal)
                sub_segs.append(((a, b), r))
            else:
                sub_segs.append(((a, b), 0.0))
        rec = e.desplazar_subsegmentos(pts, sub_segs)
        pisos_poly.append(rec[:-1])

    c1 = centroide_poly(pisos_poly[0])
    area_bloque = args.bloque_ancho * args.bloque_largo

    print("Centroide piso 1: (%.2f, %.2f)" % c1)
    print("Bloque nucleo: %.2f x %.2f = %.2f m2 (centrado por piso)" % (
        args.bloque_ancho, args.bloque_largo, area_bloque))
    print("-" * 72)
    ok_total = True
    for nv in range(args.pisos):
        h_piso = (nv + 1) * h
        sism = args.nsr_coef * h_piso if nv > 0 else 0.0
        sub_segs = []
        for i in range(n_seg):
            a, b = pts[i], pts[(i + 1) % n_seg]
            c = clases[i]
            if c == "Lateral" and i in vecinos_por_lado:
                alts = vecinos_por_lado[i]
                subs = e.subdividir_lado(a, b, alts)
                for (sa, sb2), h_v in zip(subs, alts):
                    r = max(0.2 * (h_piso - h_v), args.empate_min) \
                        if (empate_activo and h_piso > h_v) else 0.0
                    sub_segs.append(((sa, sb2), max(r, sism)))
            elif c == "Lateral":
                r = max(0.2 * (h_piso - args.altura_vecinos), args.empate_min) \
                    if (empate_activo and args.altura_vecinos > 0 and h_piso > args.altura_vecinos) else 0.0
                sub_segs.append(((a, b), max(r, sism)))
            elif c == "Frontal":
                r = args.antejardin
                if nv > 0 and args.voladizo_frontal > 0:
                    r = max(0.0, r - args.voladizo_frontal)
                sub_segs.append(((a, b), r))
            else:
                sub_segs.append(((a, b), 0.0))
        # El F3 centra el bloque en el CENTROIDE DE CADA PISO (la envolvente
        # escalonada se retira en sur/este y desplaza el centroide).
        ci = centroide_poly(pisos_poly[nv])
        bloque = rectangulo_bloque(ci[0], ci[1], args.bloque_ancho, args.bloque_largo)
        inter = list(bloque)
        for (a, b), r in sub_segs:
            inter = e._recortar_por_linea(inter, a, b, r)
            if len(inter) < 3:
                break
        a_int = e.area_poly(inter) if len(inter) >= 3 else 0.0
        # Misma regla del F3: tolerancia 2% del AREA DEL PISO
        area_piso = e.area_poly(pisos_poly[nv] + [pisos_poly[nv][0]])
        cabe = abs(a_int - area_bloque) <= 0.02 * area_piso
        ok_total = ok_total and cabe
        print("P%s h=%5.1f  area_piso=%7.2f  bloque contenido: %6.2f m2  %s" % (
            nv + 1, h_piso, area_piso, a_int, "CABE" if cabe else "SOBRESALE"))
    print("-" * 72)
    print("RESULTADO: %s" % ("bloque cabe en los %d pisos (centrado por piso)" % args.pisos
                             if ok_total
                             else "bloque SOBRESALE en >=1 piso -> piso omitido"))
    return 0 if ok_total else 1


if __name__ == "__main__":
    raise SystemExit(main())
