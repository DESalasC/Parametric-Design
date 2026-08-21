"""
================================================================================
F1_ETAPA2_LADOS_v01.py — Etapa 2: Clasificar lados por colindancia real
Proyecto: DisenoParametrico / Fase 1
GH Python Script para Grasshopper (IronPython 2.7 compatible)
================================================================================

PROPOSITO:
  Etapa 2 del pipeline v26. Recibe la geometria YA CLASIFICADA desde
  ArchiCAD (via Tapir GetElements por capa) y clasifica los 4 lados del
  lote por COLINDANCIA REAL:

    - Lado toca capa Vias        → Frontal
    - Lado toca capa ZonasVerdes → EspacioPublico
    - Lado toca predio vecino    → Lateral
    - Opuesto al Frontal (si 1)  → Posterior

  Como la clasificacion fue manual en ArchiCAD, ya no hay ambiguedad
  de datos GIS incompletos. ADR-008 se aplica sobre datos veraces.

ENTRADAS:
  lot_vertices (Point3d[])     — 4 vertices desde Discontinuity
  vias_curves (Curve[])        — Poligonos de vias (capa 00-20-20)
  ep_curves (Curve[])          — Zonas verdes/parques (capa 70-50-10)
  vecinos_curves (Curve[])     — Predios vecinos privados

SALIDAS:
  sides_table_json (String)    — Clasificacion de los 4 lados
  lot_simplificado (Curve)     — Poligono de 4 vertices
  es_esquina (bool)            — True si 2+ lados Frontal
  mensaje (String)             — Diagnostico
================================================================================
"""

import Rhino.Geometry as rg
import json
import math

TOL_COLINDANCIA_M = 0.5


def safe_list(val):
    if val is None: return []
    if isinstance(val, list): return val
    return [val]


def centroide(vertices):
    sx = sum(v.X for v in vertices)
    sy = sum(v.Y for v in vertices)
    n = len(vertices)
    return rg.Point3d(sx / n, sy / n, 0)


def curva_toca_segmento(p1, p2, curva, tol=TOL_COLINDANCIA_M):
    """Verifica si una curva toca el segmento del lote (muestreo denso)."""
    if curva is None:
        return False
    long_seg = p1.DistanceTo(p2)
    muestras = max(5, int(long_seg / 0.2) + 1)
    for i in range(muestras):
        t = float(i) / max(1, muestras - 1)
        pt = rg.Point3d(
            p1.X + t * (p2.X - p1.X),
            p1.Y + t * (p2.Y - p1.Y), 0)
        success, param = curva.ClosestPoint(pt)
        if success:
            closest = curva.PointAt(param)
            if pt.DistanceTo(closest) < tol:
                return True
    return False


def lado_colindante(p1, p2, curvas):
    """Retorna True si el lado toca alguna curva del grupo."""
    for crv in curvas:
        if crv is not None and curva_toca_segmento(p1, p2, crv):
            return True
    return False


# ==============================================================================
# MAIN
# ==============================================================================

lot_vertices_raw = globals().get("lot_vertices", None)
vias_raw = globals().get("vias_curves", None)
ep_raw = globals().get("ep_curves", None)
vecinos_raw = globals().get("vecinos_curves", None)

lot_vertices = safe_list(lot_vertices_raw)
vias_list = safe_list(vias_raw)
ep_list = safe_list(ep_raw)
vecinos_list = safe_list(vecinos_raw)

sides_table_json = ""
lot_simplificado = None
es_esquina = False

if len(lot_vertices) < 3:
    mensaje = "LADOS v01 | ERROR: Se necesitan >= 3 vertices ({} recibidos)".format(
        len(lot_vertices))
else:
    try:
        n = len(lot_vertices)
        ctr = centroide(lot_vertices)

        # Reconstruir poligono simplificado
        poly = rg.Polyline()
        for v in lot_vertices:
            poly.Add(v.X, v.Y, v.Z)
        if not poly.IsClosed and n >= 3:
            poly.Add(lot_vertices[0].X, lot_vertices[0].Y, lot_vertices[0].Z)
        lot_simplificado = rg.PolylineCurve(poly)

        # Clasificar por colindancia real (prioridad: Via > EP > Vecino)
        lados = []
        for i in range(n):
            j = (i + 1) % n
            p1 = lot_vertices[i]
            p2 = lot_vertices[j]

            toca_via = lado_colindante(p1, p2, vias_list)
            toca_ep = lado_colindante(p1, p2, ep_list)
            toca_vecino = lado_colindante(p1, p2, vecinos_list)

            if toca_via:
                cat = "Frontal"
            elif toca_ep:
                cat = "EspacioPublico"
            else:
                cat = "Lateral" if toca_vecino else "Posterior"

            lados.append({
                "id": i,
                "clasificacion": cat,
                "toca_via": toca_via,
                "toca_ep": toca_ep,
                "toca_vecino": toca_vecino
            })

        # Post-procesar: si 1 solo Frontal, el opuesto es Posterior
        categorias = [l["clasificacion"] for l in lados]
        n_frontales = categorias.count("Frontal")
        es_esquina = n_frontales >= 2

        if n_frontales == 1 and n == 4:
            idx = categorias.index("Frontal")
            op = (idx + 2) % 4
            if lados[op]["clasificacion"] != "Frontal":
                lados[op]["clasificacion"] = "Posterior"

        sides_data = {
            "lados": lados, "total_lados": len(lados),
            "es_esquina": es_esquina,
            "regla": "Colindancia real ArchiCAD (v26)"
        }
        sides_table_json = json.dumps(sides_data)

        cats_final = [l["clasificacion"] for l in lados]
        mensaje = "LADOS v01 | {} lados | {} | Vias:{} EP:{} Vecinos:{} Esq:{}".format(
            n, ", ".join(cats_final),
            len(vias_list), len(ep_list), len(vecinos_list), es_esquina)

    except Exception as e:
        mensaje = "LADOS v01 | ERROR: {}".format(str(e))
