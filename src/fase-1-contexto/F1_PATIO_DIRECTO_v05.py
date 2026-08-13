#! /usr/bin/env python3
"""
================================================================================
F1_PATIO_DIRECTO_v05.py — Patios autonomos (sin LADOS_CONFIGURAR).
Proyecto: DisenoParametrico / Fase 1
GH Python Script para Grasshopper (IronPython 2.7)

PROPOSITO:
  Genera patios de aislamiento en vertices donde convergen dos lados VECINOS.
  Infiere cuales son vecinos del tratamiento (no Frontales = vecinos).
  NO depende de F1_LADOS_CONFIGURAR.

ENTRADAS:
  lot_polygon (Curve, Item) — Perimetro del lote
  json_path   (String)      — Ruta al cache JSON (para tratamiento y pisos)

SALIDAS:
  patios_curves  (Curve[]) — Lista de curvas de patio
  patio_vertices (int[])   — Indices de vertices con patio
  patio_count    (int)     — Cantidad de patios
  mensaje        (String)  — Diagnostico

VERSION: v05 — Autonomo. Infiere vecinos del tratamiento.
================================================================================
"""

import Rhino.Geometry as rg
import json
import os

RANGO_PISOS = {"1": 2, "2": 3, "3": 5, "4": 8, "5": 12}

def toi(v, d=4):
    if v is None: return d
    try:
        i = int(float(v))
        return d if i <= 0 else i
    except: return d

def verts(curve):
    if curve is None: return []
    ok, p = curve.TryGetPolyline()
    if not ok or p is None: return []
    c = p.Count
    if c >= 2 and p[0].DistanceTo(p[c-1]) < 0.001:
        return [p[i] for i in range(c-1)]
    return [p[i] for i in range(c)]

def inside(pt, vs):
    n = len(vs)
    if n < 3: return False
    cnt = 0; px, py = pt.X, pt.Y
    for i in range(n):
        v1, v2 = vs[i], vs[(i+1)%n]
        if ((v1.Y > py) != (v2.Y > py)):
            xi = v1.X + (py - v1.Y)*(v2.X - v1.X)/(v2.Y - v1.Y)
            if px < xi: cnt += 1
    return (cnt % 2) == 1


# ==============================================================================
# MAIN
# ==============================================================================

lp = globals().get("lot_polygon", None)
if isinstance(lp, list) and len(lp) == 1: lp = lp[0]
jp = str(globals().get("json_path", "")).strip("[]'\" ")

if lp is None:
    patios_curves = None; patio_vertices = []; patio_count = 0
    print("ERROR: lot_polygon None")
else:
    # --- 1. TRATAMIENTO Y PISOS ---
    tr = "Consolidacion"; re = "3"
    if jp and os.path.exists(jp):
        try:
            with open(jp,'r',encoding='utf-8') as f: jd = json.load(f)
            pd = jd.get("pot_data",{})
            tr = str(pd.get("tratamiento","Consolidacion"))
            re = str(pd.get("rango_edificabilidad","3"))
        except: pass
    
    bf = RANGO_PISOS.get(re, 5)
    tl = tr.lower()
    
    vs = verts(lp); nv = len(vs)
    
    if nv < 4:
        patios_curves = None; patio_vertices = []; patio_count = 0
        print("ERROR: < 4 vertices")
    else:
        # --- 2. INFERIR LADOS VECINOS ---
        # Frentes inferidos: lados 0 y n//2 (esquina tipica)
        # Vecinos: todos los demas
        front_set = {0}
        if nv >= 4: front_set.add(nv // 2)
        
        neighbor_set = set()
        for i in range(nv):
            if i not in front_set:
                neighbor_set.add(i)
        
        # --- 3. VERTICES VECINO-VECINO ---
        pv_list = []
        for i in range(nv):
            la = (i - 1 + nv) % nv  # lado anterior
            lb = i % nv              # lado actual
            if la in neighbor_set and lb in neighbor_set:
                pv_list.append(i)
        
        # --- 4. TAMANO PATIO ---
        try:
            la = rg.AreaMassProperties.Compute(lp).Area
        except:
            la = 315.0
        
        if la < 500 and bf <= 5:
            ps = 3.0
        else:
            ps = max(3.0, (bf * 3.0) * 0.25)
            ps = round(ps * 2) / 2
        
        # --- 5. GENERAR PATIOS ---
        patios = []
        pv_ok = []
        for vi in pv_list:
            vc = vs[vi]
            vp = vs[(vi - 1 + nv) % nv]
            vn = vs[(vi + 1) % nv]
            
            e1 = rg.Vector3d(vp.X - vc.X, vp.Y - vc.Y, 0)
            e2 = rg.Vector3d(vn.X - vc.X, vn.Y - vc.Y, 0)
            
            if e1.Length < 0.001 or e2.Length < 0.001: continue
            e1.Unitize(); e2.Unitize()
            
            # Probar 4 orientaciones
            best = -1; best_pts = None
            for sx, sy in [(-1,-1),(-1,1),(1,-1),(1,1)]:
                s1 = rg.Vector3d(sx*e1.X, sx*e1.Y, 0)
                s2 = rg.Vector3d(sy*e2.X, sy*e2.Y, 0)
                p0 = rg.Point3d(vc.X, vc.Y, 0)
                p1 = rg.Point3d(p0.X + s1.X*ps, p0.Y + s1.Y*ps, 0)
                p2 = rg.Point3d(p1.X + s2.X*ps, p1.Y + s2.Y*ps, 0)
                p3 = rg.Point3d(p0.X + s2.X*ps, p0.Y + s2.Y*ps, 0)
                ic = sum(1 for p in [p0,p1,p2,p3] if inside(p, vs))
                if ic > best: best = ic; best_pts = [p0,p1,p2,p3]
            
            if best >= 4 and best_pts:
                patios.append(rg.PolylineCurve(best_pts + [best_pts[0]]))
                pv_ok.append(vi)
        
        pcnt = len(patios)
        
        # GH outputs
        patios_curves  = patios if patios else None
        patio_vertices = pv_ok
        patio_count    = pcnt
        
        parts = [
            "=== PATIO v05 ===",
            "Trat: {} | Rango: {} | {} pisos".format(tr, re, bf),
            "Lote: {} vert | Frentes: {} | Vecinos: {}".format(nv, sorted(front_set), sorted(neighbor_set)),
            "Vert Vecino+Vecino: {} -> {} patios {:.1f}x{:.1f}m".format(pv_list, pcnt, ps, ps),
        ]
        if pcnt == 0 and len(neighbor_set) >= 2:
            parts.append("NOTA: Hay vecinos pero no comparten vertices adyacentes.")
        print("\n".join(parts))
