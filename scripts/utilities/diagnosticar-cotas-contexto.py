# -*- coding: utf-8 -*-
"""Diagnostico de cotas del contexto F1 (ETAPA1 + contexto50).

Uso:
    python scripts/utilities/diagnosticar-cotas-contexto.py --chip AAA0030JKOE
    python scripts/utilities/diagnosticar-cotas-contexto.py --chip AAA0030JKOE --md informe.md

Verifica:
  1. Coherencia del datum: z_ref = origen_sirgas.z + ancla_canvas_local.z.
  2. Z_base de ETAPA1 (minimo Z valido de la malla de terreno).
  3. desplazamiento_z que aplica F1_CONTEXTO50_BUILD a z_base_m.
  4. Geometrias planas (z=0) en vias, espacios publicos y vecinos de ETAPA1.
  5. Residuo de la cota de cada vecino (MDT centroide) contra la malla IDW de ETAPA1,
     solo para los vecinos cuyo centroide cae dentro del bbox de la malla.

No modifica datos. Sale con codigo 1 si alguna verificacion critica falla.
"""
from __future__ import print_function

import argparse
import io
import json
import os

TOL_DATUM = 0.01
TOL_Z = 0.001


def leer_json(ruta):
    with io.open(ruta, encoding="utf-8") as f:
        return json.load(f)


def z_validas(puntos):
    return [p["z_local"] for p in puntos if abs(p["z_local"]) > TOL_Z]


def rango(valores):
    return (min(valores), max(valores)) if valores else (0.0, 0.0)


def contar_planas(registros, clave):
    """(#registros, #vertices, #vertices con z==0)."""
    n_reg = 0
    n_pts = 0
    n_cero = 0
    for reg in registros or []:
        coords = reg.get(clave) or []
        if not coords:
            continue
        n_reg += 1
        for c in coords:
            if len(c) >= 3:
                n_pts += 1
                if abs(c[2]) <= TOL_Z:
                    n_cero += 1
    return n_reg, n_pts, n_cero


def idw(malla, x, y):
    num = 0.0
    den = 0.0
    for mx, my, mz in malla:
        d2 = (mx - x) ** 2 + (my - y) ** 2
        if d2 < 1e-9:
            return mz
        w = 1.0 / d2
        num += w * mz
        den += w
    return num / den if den else 0.0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--chip", required=True)
    ap.add_argument("--data", default=os.path.join("data", "pot-cache"))
    ap.add_argument("--md", default="")
    args = ap.parse_args()

    ruta_c1 = os.path.join(args.data, args.chip + "-contexto.json")
    ruta_c50 = os.path.join(args.data, args.chip + "-contexto50.json")
    c1 = leer_json(ruta_c1)
    c50 = leer_json(ruta_c50)

    lineas = []
    fallos = []

    def out(txt=""):
        lineas.append(txt)
        print(txt)

    meta = c50.get("metadata", {})
    origen_z = float((meta.get("origen_sirgas") or {}).get("z") or 0.0)
    ancla = meta.get("ancla_canvas_local") or {}
    ancla_z = float(ancla.get("z") or 0.0)
    z_ref = float((meta.get("z_base_fuente") or {}).get("z_ref_m") or (origen_z + ancla_z))
    delta = (origen_z + ancla_z) - z_ref

    out("# Diagnostico de cotas - %s" % args.chip)
    out("")
    out("## 1. Datum")
    out("origen_sirgas.z      = %.3f m" % origen_z)
    out("ancla_canvas_local.z = %.3f m" % ancla_z)
    out("z_ref_m              = %.3f m" % z_ref)
    out("origen_z + ancla_z   = %.3f m (delta %.4f m)" % (origen_z + ancla_z, delta))
    if abs(delta) > TOL_DATUM:
        fallos.append("datum incoherente: z_ref != origen_z + ancla_z (delta %.3f m)" % delta)
        out("ESTADO: FALLA - el datum del contexto50 no cierra.")
    else:
        out("ESTADO: OK - el datum cierra (< %.2f m)." % TOL_DATUM)

    topo = c1.get("topografia") or {}
    malla_pts = topo.get("malla_terreno") or []
    zs = z_validas(malla_pts)
    n_cero_malla = sum(1 for p in malla_pts if abs(p["z_local"]) <= TOL_Z)
    base = min(zs) if zs else 0.0

    out("")
    out("## 2. Z_base de ETAPA1")
    out("puntos de malla      = %d (%d con z=0.000)" % (len(malla_pts), n_cero_malla))
    out("Z_base (min valido)  = %.3f m" % base)
    out("Z max malla          = %.3f m" % (max(zs) if zs else 0.0))
    if n_cero_malla and base > 0.05:
        out("AVISO: hay puntos en 0.000 excluidos por el filtro |z|>0.001;")
        out("       si son cotas reales, Z_base queda %.2f m por encima del punto mas bajo." % base)

    desp = (origen_z + base) - z_ref
    lote = (c1.get("lote_objetivo") or {}).get("vertices_3d_local") or []
    lz = [v[2] - base for v in lote]
    out("")
    out("## 3. Desplazamiento aplicado por CONTEXTO50_BUILD")
    out("desplazamiento_z     = origen_z + Z_base - z_ref = %.3f m" % desp)
    out("lote en Z local      = %.3f .. %.3f m (desnivel %.2f m)" % (min(lz), max(lz), max(lz) - min(lz)))
    out("comprobacion         = z_base_m - desplazamiento_z = z_local - Z_base")

    out("")
    out("## 4. Geometrias planas en ETAPA1 (z=0)")
    for clave, etiqueta in (("coordenadas_local", "vias_oficiales"), ("coordenadas_local", "espacios_publicos"),
                            ("vertices_3d_local", "vecinos")):
        regs = c1.get(etiqueta) or []
        n_reg, n_pts, n_cero = contar_planas(regs, clave)
        pct = (100.0 * n_cero / n_pts) if n_pts else 0.0
        out("%-18s registros=%3d vertices=%5d con z=0: %5d (%.1f%%)" % (etiqueta, n_reg, n_pts, n_cero, pct))
        if n_pts and pct > 99.0:
            fallos.append("%s sin cota: %.0f%% de vertices en z=0" % (etiqueta, pct))

    out("")
    out("## 5. Vecinos del contexto50 vs malla ETAPA1")
    eds = c50.get("edificios") or []
    metodo = str((meta.get("z_base_fuente") or {}).get("metodo") or "")
    modo_min = ("minimo" in metodo.lower()) or ("min de" in metodo.lower())
    zb = [float(e["z_base_m"]) for e in eds if e.get("z_base_m") is not None]
    zb_local = [z - desp for z in zb]
    n_con = len(zb)
    out("metodo z_base        = %s" % (metodo or "(sin metadata)"))
    out("edificios con cota   = %d/%d" % (n_con, len(eds)))
    if zb_local:
        out("z_base_m (canvas)    = %.3f .. %.3f m" % (min(zb), max(zb)))
        out("z_base ajustado      = %.3f .. %.3f m" % (min(zb_local), max(zb_local)))
    if eds and n_con < len(eds):
        fallos.append("%d/%d edificios sin z_base_m: sus morphs quedan en el datum (0.0) "
                      "en vez de apoyar en su terreno; ejecutar anclar_contexto50_zbase.py"
                      % (len(eds) - n_con, len(eds)))
    if len(zb_local) > 1:
        dispersion = max(zb_local) - min(zb_local)
        out("dispersion de bases  = %.3f m (max-min)" % dispersion)
        if dispersion < 0.05:
            fallos.append("todas las bases a la misma altura (dispersion %.3f m): "
                          "los morphs flotan o se solapan" % dispersion)
    if metodo and not modo_min:
        out("AVISO: metodo de muestreo = %s (la regla vigente es el MINIMO de la huella)" % metodo)
    ajustes = [float(e["z_base_centroide_m"]) - float(e["z_base_m"])
               for e in eds if e.get("z_base_centroide_m") is not None and e.get("z_base_m") is not None]
    if ajustes:
        out("ajuste por huella   = centroide - min: promedio %.2f m | max %.2f m"
            % (sum(ajustes) / len(ajustes), max(abs(a) for a in ajustes)))

    ax = float(ancla.get("x") or 0.0)
    ay = float(ancla.get("y") or 0.0)
    minx = min(p["x_local"] for p in malla_pts) if malla_pts else 0.0
    maxx = max(p["x_local"] for p in malla_pts) if malla_pts else 0.0
    miny = min(p["y_local"] for p in malla_pts) if malla_pts else 0.0
    maxy = max(p["y_local"] for p in malla_pts) if malla_pts else 0.0
    malla = [(p["x_local"], p["y_local"], p["z_local"]) for p in malla_pts]

    residuos = []
    for e in eds:
        if e.get("z_base_m") is None:
            continue
        vv = e.get("vertices") or []
        if vv and vv[0] == vv[-1]:
            vv = vv[:-1]
        if len(vv) < 3:
            continue
        pts = [(p[0] + ax, p[1] + ay) for p in vv]
        cx = sum(p[0] for p in pts) / len(pts)
        cy = sum(p[1] for p in pts) / len(pts)
        # Solo huellas COMPLETAS dentro de la malla: fuera de ella el IDW extrapola.
        dentro = all(minx <= x <= maxx and miny <= y <= maxy for x, y in pts)
        if dentro:
            if modo_min:
                z_terreno = min(idw(malla, x, y) for x, y in pts) - base
            else:
                z_terreno = idw(malla, cx, cy) - base
            residuos.append(float(e["z_base_m"]) - desp - z_terreno)

    if residuos:
        prom = sum(residuos) / len(residuos)
        out("huellas completas en malla = %d" % len(residuos))
        out("contraste con malla ETAPA1 (informativo: la malla es una interpolacion de 118 puntos):")
        out("  residuo z_vecino-terreno (%s): promedio %.2f m | min %.2f | max %.2f | |max| %.2f"
            % ("min huella" if modo_min else "centroide", prom, min(residuos), max(residuos),
               max(abs(r) for r in residuos)))
        out("  no es un criterio de falla: el MDT puntual y la malla IDW son dos superficies distintas.")
    else:
        out("sin vecinos dentro del bbox de la malla (no comparable)")

    out("")
    out("## Veredicto")
    if fallos:
        for f in fallos:
            out("- FALLA: %s" % f)
    else:
        out("- Sin fallas criticas de datum ni de cotas planas.")
    out("- Las geometrias planas (vias/EP/vecinos ETAPA1) no pueden drapearse sin muestrear el MDT")
    out("  en sus vertices: la malla de ETAPA1 solo cubre el lote + ~5 m.")

    if args.md:
        with io.open(args.md, "w", encoding="utf-8") as f:
            f.write(u"\n".join(lineas) + u"\n")
        print("\n[OK] informe escrito en %s" % args.md)

    return 1 if fallos else 0


if __name__ == "__main__":
    raise SystemExit(main())
