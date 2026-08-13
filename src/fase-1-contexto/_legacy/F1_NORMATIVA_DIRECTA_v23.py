#! /usr/bin/env python3
"""
================================================================================
F1_NORMATIVA_DIRECTA_v23.py — Motor normativo AUTONOMO.
Proyecto: DisenoParametrico / Fase 1
GH Python Script para Grasshopper (IronPython 2.7)

PROPOSITO:
  Calcula huella, IO, IC, pisos y altura SIN depender de F1_LADOS_CONFIGURAR.
  Los retiros los infiere del tratamiento (Consolidacion=Continua: frentes 3m,
  laterales 0m). Acepta patio_curve opcional.

ENTRADAS:
  lot_polygon (Curve, Item) — Perimetro del lote
  json_path   (String)      — Ruta al cache JSON
  floor_height_user (Number, Item) — Altura entrepiso [2.5-3.8]m
  patio_curve (Curve[])     — Patio(s) de F1_PATIO_VECINO (opcional, List)

SALIDAS:
  envelope_curve, ocupacion_real, io_maximo, ic_real, ic_maximo,
  altura_total, pisos_aplicados, mensaje

VERSION: v23.0 — Autonomo. Sin dependencia de LADOS_CONFIGURAR.
================================================================================
"""

import Rhino.Geometry as rg
import json
import os
import math

ALTURA_MIN = 2.5
ALTURA_MAX = 3.8
TOL = 0.01
RANGO_PISOS = {"1": 2, "2": 3, "3": 5, "4": 8, "5": 12}

def unwrap(v):
    if v is None: return None
    if isinstance(v, list): return v[0] if v else None
    return v

def tof(v, d=0.0, m=None):
    if v is None: return d
    try:
        f = float(v)
        if m is not None and f < m: return d
        return f
    except: return d

def toi(v, d=1):
    if v is None: return d
    try:
        i = int(float(v))
        return d if i <= 0 else i
    except: return d

def segs(curve):
    if curve is None: return []
    ok, p = curve.TryGetPolyline()
    if not ok or p is None: return []
    c = p.Count
    closed = c >= 2 and p[0].DistanceTo(p[c-1]) < 0.001
    n = c - 1 if closed else c
    return [rg.Line(p[i], p[(i+1)%c]) for i in range(n)]

def sub_patios(fp, patios):
    if fp is None or patios is None: return fp
    if not isinstance(patios, list): patios = [patios]
    patios = [p for p in patios if p is not None]
    if not patios: return fp
    r = fp
    for pt in patios:
        try:
            fb = rg.Brep.CreatePlanarBreps([r], TOL)
            pb = rg.Brep.CreatePlanarBreps([pt], TOL)
            if fb and pb and fb and pb:
                bd = rg.Brep.CreateBooleanDifference([fb[0]], [pb[0]], TOL)
                if bd:
                    e = [x for x in bd[0].Edges if x]
                    if e:
                        j = rg.Curve.JoinCurves(e)
                        if j: r = j[0]
        except: continue
    return r


# ==============================================================================
# MAIN
# ==============================================================================

lp  = unwrap(globals().get("lot_polygon", None))
jp  = str(globals().get("json_path", "")).strip("[]'\" ")
fh  = tof(unwrap(globals().get("floor_height_user", None)), ALTURA_MIN, ALTURA_MIN)
if fh > ALTURA_MAX: fh = ALTURA_MAX
pc  = globals().get("patio_curve", None)

if lp is None:
    envelope_curve = None; ocupacion_real = 0.0; io_maximo = 0.70
    ic_real = 0.0; ic_maximo = 2.0; altura_total = 0.0; pisos_aplicados = 0
    mensaje = "ERROR: lot_polygon es None"
    print(mensaje)
else:
    # --- 1. DATOS POT ---
    hp = 11.4; tr = "Consolidacion"; icx = 2.0; iox = 0.70; re = "3"
    if jp and os.path.exists(jp):
        try:
            with open(jp,'r',encoding='utf-8') as f: jd = json.load(f)
            pd = jd.get("pot_data",{})
            hp = tof(pd.get("altura_maxima_m"), 11.4, 0.5)
            tr = str(pd.get("tratamiento","Consolidacion"))
            re = str(pd.get("rango_edificabilidad","3"))
        except: pass
    tl = tr.lower()
    if "desarrollo" in tl:   iox,icx = 0.50,3.0
    elif "renovacion" in tl: iox,icx = 0.60,5.0
    elif "conservacion" in tl: iox,icx = 0.50,2.0
    fn = RANGO_PISOS.get(re, 5)
    
    # --- 2. GEOMETRIA ---
    try:
        amp = rg.AreaMassProperties.Compute(lp)
        al = amp.Area; ct = amp.Centroid
    except:
        al, ct = 315.0, rg.Point3d(0,0,0)
    
    ss = segs(lp); n = len(ss)
    if n < 3:
        envelope_curve = lp; ocupacion_real = 1.0; io_maximo = iox
        ic_real = 0.0; ic_maximo = icx; altura_total = 0.0; pisos_aplicados = 0
        mensaje = "ERROR: < 3 lados"
        print(mensaje)
    else:
        # --- 3. RETIROS (inferidos del tratamiento) ---
        if "desarrollo" in tl or "renovacion" in tl:
            rf, rl = 5.0, 3.0
        else:
            rf, rl = 3.0, 0.0  # Consolidacion/Continua
        
        fi = [0]
        if n >= 4: fi.append(n // 2)
        
        sm = {}
        for i in range(n):
            sm[i] = rf if i in fi else rl
        
        # --- 4. OFFSET ---
        # Intentar offset uniforme con el retiro maximo, luego strips para laterales
        ms = max(sm.values())
        
        def try_offset(curve, dist):
            for direction in [-1, 1]:
                for factor in [1.0, 0.7, 0.5, 0.3]:
                    d = dist * factor * direction
                    try:
                        oc = curve.Offset(rg.Plane.WorldXY, d, TOL, rg.CurveOffsetCornerStyle.Sharp)
                        if oc:
                            oa = rg.AreaMassProperties.Compute(oc[0]).Area
                            if oa < al * 0.99:
                                return oc
                    except: continue
            return None
        
        oc = try_offset(lp, ms)
        
        if oc:
            fp = oc[0]
            # Strips para lados con retiro < max
            oss = segs(fp)
            if len(oss) == n:
                strips = []
                for i in range(n):
                    if sm[i] < ms - 0.01:
                        oseg = ss[i]; fseg = oss[i]
                        pts = [rg.Point3d(oseg.From.X, oseg.From.Y, 0),
                               rg.Point3d(oseg.To.X, oseg.To.Y, 0),
                               rg.Point3d(fseg.To.X, fseg.To.Y, 0),
                               rg.Point3d(fseg.From.X, fseg.From.Y, 0),
                               rg.Point3d(oseg.From.X, oseg.From.Y, 0)]
                        strips.append(rg.PolylineCurve(pts))
                if strips:
                    try:
                        allc = [fp] + strips
                        breps = []
                        for c in allc:
                            b = rg.Brep.CreatePlanarBreps([c], TOL)
                            if b: breps.append(b[0])
                        if len(breps) >= 2:
                            mu = rg.Brep.CreateBooleanUnion(breps, TOL)
                            if mu:
                                e = [x for x in mu[0].Edges if x]
                                if e:
                                    j = rg.Curve.JoinCurves(e)
                                    if j: fp = j[0]
                    except: pass
        else:
            fp = lp  # fallback: lote original
        
        # --- 5. PATIOS ---
        pcnt = 0
        if pc is not None and fp is not None:
            if isinstance(pc, list):
                pcnt = len([p for p in pc if p is not None])
            else:
                pcnt = 1
            fp = sub_patios(fp, pc)
        
        # --- 6. AREAS ---
        try: ae = rg.AreaMassProperties.Compute(fp).Area
        except: ae = al
        if ae <= 0: ae = 1.0
        if ae > al * 1.5: ae = al; fp = lp
        
        io = ae / al if al > 0 else 0
        
        # --- 7. PISOS ---
        ah = fn * fh
        if ah > hp > 0:
            pa = max(1, int(hp / fh))
            at = pa * fh
        else:
            pa = fn; at = ah
        
        ic = (ae * pa) / al if al > 0 else 0
        
        # --- 8. MENSAJE ---
        ec = fp
        parts = [
            "=== NORMATIVA v23 ===",
            "Trat: {} | Rango: {} | Pisos norma: {}".format(tr, re, fn),
            "Lote: {} lados | Area: {:.1f}m2 | Huella: {:.1f}m2".format(n, al, ae),
            "IO: {:.2f}/Max {:.2f} | IC: {:.2f}/Max {:.2f}".format(io, iox, ic, icx),
            "Pisos: {} x {:.2f}m = {:.2f}m (max POT: {:.1f}m)".format(pa, fh, at, hp),
        ]
        sbs = []
        for i in sorted(sm.keys()):
            v = sm[i]; m = "F" if i in fi else ("L" if v > 0 else "-")
            sbs.append("{}{}:{:.1f}".format(m, i, v))
        parts.append("Retiros: [{}]".format(", ".join(sbs)))
        parts.append("Patios: {}".format(pcnt))
        if io > iox: parts.append("ALERTA: IO excede")
        if ic > icx: parts.append("ALERTA: IC excede")
        msg = "\n".join(parts)
        print(msg)
        
        # GH outputs
        envelope_curve  = ec
        ocupacion_real  = io
        io_maximo       = iox
        ic_real         = ic
        ic_maximo       = icx
        altura_total    = at
        pisos_aplicados = pa
        mensaje         = msg
