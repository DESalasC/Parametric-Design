"""
================================================================================
F1_ETAPA2_PATIO_v02.py — Patio desde el Vertice N
Proyecto: DisenoParametrico / Fase 1
GH Python Script para Grasshopper (IronPython 2.7 compatible)
================================================================================

ALGORITMO (actualizado 2026-09-28 con decisiones del operador):
  El patio se origina en el VERTICE N (el vertice del lote simplificado
  mas alejado de las vias del frente, segun F1_ETAPA2_LADOS_v06).

  v02.3 — Decisiones del operador (2026-09-28):
    (a) GARANTIAS del patio: area minima = 9 m2 y "3 metros lineales" de
        distancia entre CADA lado del predio y el borde del patio que le es
        opuesto (claridad/profundidad desde cada lado que comparte el vertice N).
        La forma no es critica: se usa un paralelogramo anclado al vertice N,
        alineado a las direcciones de los dos lados. Para esquinas no
        perpendiculares (angulo theta entre los lados) el lado se escala:
            L = max(lado_base, 3.0 / sin(theta))
        de modo que claridad = L*sin(theta) >= 3.0 m  y
        area = L^2 * sin(theta) >= 9.0 m2 (pues L >= 3/sin >= 3).
    (b) SIMPLIFICACION de lados colineales (misma regla que LADOS v06.5):
        vertices con giro < 2.5 grados se fusionan; giro >= 2.5 grados se
        mantiene, independiente del numero final de lados.
    (c) Los puntos mejorados de Vertice N se DEDUPLICAN (>= 0.30 m entre
        candidatos) y solo se usan si coinciden con un vertice del lote
        (<= 0.15 m). Se genera como maximo UN (1) patio.

SUBVERSIONES INTERNAS (v02.x: iteraciones sin cambio de version general):
  v02.0 (2026-08-12) - Algoritmo original: patio cuadrado desde el
         Vertice N sobre los dos lados laterales que lo comparten.
  v02.1 (2026-08-23) - El patio de esquina se ancla en el Vertice N
         cuando los DOS lados que lo comparten son colindantes (Lateral
         o Posterior); antes solo "Lateral" dejaba el patio sin generar.
  v02.2 (2026-08-25) - Consume vertice_n_points de F1_ETAPA2_LADOS_v06.3
         (puntos mejorados del Vertice N por intersecciones reales con
         vias) y genera un patio por cada punto disponible.
  v02.3 (2026-09-28) - Garantias de area (>= 9 m2) y claridad (>= 3 m
         lineales) por lado via escala L = max(base, 3/sin(theta));
         simplificacion de lados colineales (< 2.5 grados) compartida con
         LADOS v06.5; dedup de puntos mejorados; maximo 1 patio; mensajes
         con metricas (area, claridad) y motivos de descarte.
  v02.4 (2026-09-28) - EXPORT del diagnostico lados/patio: si existe el flag
         data/pot-cache/lados-export-flag.json con {exportar: true} (lo pone
         el servidor/orquestador via POST /api/exportar-lados), escribe
         data/pot-cache/<CHIP>-lados.json para verificacion automatica (F1.5)
         y devuelve el flag a false (mismo patron que F1_EXPORTAR_GFA_v02).
  v02.5 (2026-09-29) - LECTOR CANONICO de codificacion en la lectura del flag
         (cascada utf-8-sig -> cp1252 -> latin-1 con avisos) y escritura
         ASCII-safe (ensure_ascii=True) en los JSON exportados.
Regla de versionado: la version general (v02 -> v03) SOLO cambia con
cambios mayores (contrato de entradas/salidas o algoritmo central); las
iteraciones internas se registran como subversiones v02.x en este
encabezado. Historial reconstruido desde git el 2026-09-01.

ENTRADAS:
  lot_vertices (Point3d[])     — vertices desde Discontinuity
  sides_table_json (String)    — Clasificacion desde F1_ETAPA2_LADOS_v06
  altura_max_pot (Number)      — Altura maxima [m]

SALIDAS:
  patios_curves   (Curve[])   — Rectangulo(s) de patio desde vertice N
  patio_count     (int)       — Numero de patios (0 o 1)
  mensaje         (String)    — Diagnostico
================================================================================
"""

import Rhino.Geometry as rg
import json
import math
import os
from datetime import datetime

PATIO_MINIMO_M = 3.0
ALTURA_ENTREPISO = 3.0
# v02.3: garantias (decision operador 2026-09-28)
CLARIDAD_MINIMA_M = 3.0
AREA_MINIMA_M2 = 9.0
# v02.3: simplificacion colineal (misma regla que LADOS v06.5)
UMBRAL_COLINEAL_GRADOS = 2.5
# v02.3: dedup de puntos mejorados y coincidencia con vertice del lote
CLUSTER_PUNTOS_M = 0.30
COINCIDENCIA_VERTICE_M = 0.15
# v02.3: clamp de sin(theta) para esquinas degeneradas (~5 grados)
SIN_MINIMO = 0.087


def _decodificar_cascada(raw, ruta="<bytes>"):
    """LECTOR CANONICO (v02.5): utf-8-sig estricto -> cp1252 -> latin-1."""
    try:
        return raw.decode("utf-8-sig")
    except Exception:
        pass
    try:
        texto = raw.decode("cp1252")
        print("[AVISO ENCODING] leido como cp1252 (no utf-8): %s" % ruta)
        return texto
    except Exception:
        pass
    texto = raw.decode("latin-1")
    print("[AVISO ENCODING] leido como latin-1 (ultimo recurso): %s" % ruta)
    return texto


def unwrap(val):
    if val is None: return None
    if isinstance(val, list): return val[0] if len(val) > 0 else None
    return val


def safe_list(val):
    if val is None: return []
    if isinstance(val, list): return val
    return [val]


def _giro_grados(p_prev, p, p_next):
    """v02.3 - Angulo de giro (0-180) en p entre vector entrante y saliente.

    0 = colineal recto; 180 = retorno.
    """
    ax = p.X - p_prev.X
    ay = p.Y - p_prev.Y
    bx = p_next.X - p.X
    by = p_next.Y - p.Y
    la = math.sqrt(ax * ax + ay * ay)
    lb = math.sqrt(bx * bx + by * by)
    if la < 1e-12 or lb < 1e-12:
        return 0.0
    cosang = (ax * bx + ay * by) / (la * lb)
    if cosang > 1.0: cosang = 1.0
    if cosang < -1.0: cosang = -1.0
    return math.degrees(math.acos(cosang))


def simplificar_colineales(vertices, umbral_grados=UMBRAL_COLINEAL_GRADOS):
    """v02.3 - Fusiona vertices colineales o con giro < umbral (2.5 grados).

    Misma regla que LADOS v06.5 (decision operador 2026-09-28): se simplifican
    los vertices con variacion de angulo INFERIOR a 2.5 grados; los de 2.5
    grados o mas se mantienen, independiente del numero final de lados.
    Elimina iterativamente el vertice de MENOR giro bajo el umbral y recalcula
    (asi los angulos que superan el umbral tras fusionar se conservan).
    Nunca baja de 3 vertices.
    """
    pts = []
    for v in vertices:
        if not pts or pts[-1].DistanceTo(v) > 1e-9:
            pts.append(v)
    if len(pts) > 1 and pts[0].DistanceTo(pts[-1]) < 1e-9:
        pts.pop()
    while len(pts) > 3:
        n = len(pts)
        mejor_i = -1
        mejor_giro = None
        for i in range(n):
            g = _giro_grados(pts[(i - 1) % n], pts[i], pts[(i + 1) % n])
            if g < umbral_grados and (mejor_giro is None or g < mejor_giro):
                mejor_giro = g
                mejor_i = i
        if mejor_i < 0:
            break
        pts.pop(mejor_i)
    return pts


def deduplicar_puntos(puntos, tol_m=CLUSTER_PUNTOS_M):
    """v02.3 - Conserva el primer punto de cada cluster (>= tol_m)."""
    kept = []
    for p in puntos:
        duplicado = False
        for q in kept:
            if p.DistanceTo(q) < tol_m:
                duplicado = True
                break
        if not duplicado:
            kept.append(p)
    return kept


def _raiz_proyecto():
    """v02.4 - Raiz del proyecto desde la variable de entorno del canvas."""
    raiz = os.environ.get("DISENO_PARAMETRICO_ROOT", "")
    if raiz and os.path.isdir(raiz):
        return raiz
    return ""


def _escribir_json_utf8(ruta, data):
    """Escritura canonica v02.5: UTF-8 sin BOM + ASCII-safe (ensure_ascii)
    para robustez entre herramientas; nombre historico conservado."""
    with open(ruta, "wb") as f:
        f.write(json.dumps(data, indent=2, ensure_ascii=True).encode("utf-8"))


def _exportar_diagnostico(sides_data, patios_export, mensaje_final):
    """v02.4 - Exporta el diagnostico lados/patio si el flag lo solicita.

    Flag: data/pot-cache/lados-export-flag.json {"exportar": true, "chip": ...}
    Salida: data/pot-cache/<CHIP>-lados.json (schema lados_patio_diagnostico_v01).
    Devuelve la ruta escrita, o None si no fue solicitado.
    """
    raiz = _raiz_proyecto()
    if not raiz:
        return None
    flag_ruta = os.path.join(raiz, "data", "pot-cache", "lados-export-flag.json")
    if not os.path.exists(flag_ruta):
        return None
    try:
        with open(flag_ruta, "rb") as f:
            _raw = f.read()
        flag = json.loads(_decodificar_cascada(_raw, flag_ruta))
    except Exception:
        return None
    if not isinstance(flag, dict) or not flag.get("exportar"):
        return None
    chip = str(flag.get("chip") or "").strip()
    if not chip:
        return None
    lados = []
    for l in (sides_data.get("lados") or []):
        lados.append({
            "id": l.get("id"),
            "clasificacion": l.get("clasificacion"),
            "motivo": l.get("motivo"),
            "cardinal": l.get("cardinal"),
            "toca_via": l.get("toca_via"),
            "toca_ep": l.get("toca_ep"),
            "toca_vecino": l.get("toca_vecino"),
        })
    data = {
        "schema": "lados_patio_diagnostico_v01",
        "chip": chip,
        "generado_por": "F1_ETAPA2_PATIO_v02.5",
        "generado_en": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "solicitud": flag,
        "sides": {
            "total_lados": sides_data.get("total_lados"),
            "n_vertices_originales": sides_data.get("n_vertices_originales"),
            "vertice_a": sides_data.get("vertice_a"),
            "vertice_n": sides_data.get("vertice_n"),
            "es_esquina": sides_data.get("es_esquina"),
            "ancho_via_m": sides_data.get("ancho_via_m"),
            "lados": lados,
        },
        "patio": {
            "count": len(patios_export),
            "patios": patios_export,
            "mensaje": mensaje_final,
        },
    }
    out_ruta = os.path.join(raiz, "data", "pot-cache", chip + "-lados.json")
    _escribir_json_utf8(out_ruta, data)
    # devolver el flag a false (patron GFA)
    _escribir_json_utf8(flag_ruta, {"exportar": False, "chip": chip,
                                    "ts": datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
    return out_ruta


def point_in_lot(pt, vertices):
    """Ray casting + deteccion de punto sobre el borde (tol 0.1m)."""
    n = len(vertices)
    if n < 3: return False
    px, py = pt.X, pt.Y
    # 1) Ray casting estandar
    count = 0
    for i in range(n):
        v1 = vertices[i]
        v2 = vertices[(i + 1) % n]
        if ((v1.Y > py) != (v2.Y > py)):
            if (v2.Y - v1.Y) != 0:
                x_int = v1.X + (py - v1.Y) * (v2.X - v1.X) / (v2.Y - v1.Y)
                if px < x_int:
                    count += 1
    if (count % 2) == 1:
        return True
    # 2) Punto sobre el borde (distancia al segmento < 0.1m)
    for i in range(n):
        v1 = vertices[i]
        v2 = vertices[(i + 1) % n]
        dx = v2.X - v1.X
        dy = v2.Y - v1.Y
        l2 = dx * dx + dy * dy
        if l2 < 1e-12:
            continue
        t = ((px - v1.X) * dx + (py - v1.Y) * dy) / l2
        t = max(0.0, min(1.0, t))
        cx = v1.X + t * dx
        cy = v1.Y + t * dy
        dist = math.sqrt((px - cx) ** 2 + (py - cy) ** 2)
        if dist < 0.1:
            return True
    return False


def _dir_interior(corner_pt, p1, p2):
    """Direccion unitaria desde corner_pt hacia el otro extremo del borde."""
    otro = p2 if corner_pt.DistanceTo(p1) < 0.05 else p1
    d = rg.Vector3d(otro.X - corner_pt.X, otro.Y - corner_pt.Y, 0)
    if d.Length > 1e-9:
        d.Unitize()
    return d


def build_patio_desde_vertice(corner_pt, borde_a_p1, borde_a_p2,
                              borde_b_p1, borde_b_p2, lado_base, lot_vertices):
    """
    v02.3 - Paralelogramo de patio anclado en corner_pt (vertice N), con lados
    ALINEADOS a las direcciones de los dos bordes del lote que comparten el
    vertice (las direcciones apuntan hacia el INTERIOR del lote).

    Garantias (decisiones operador 2026-09-28):
      - claridad respecto a cada lado = L * sin(theta) >= 3.0 m
      - area = L^2 * sin(theta) >= 9.0 m2
    => L = max(lado_base, CLARIDAD_MINIMA_M / sin(theta)).

    Retorna (curva, (L, sin_theta)) o None si no valida (no cabe / no es
    interior al lote).
    """
    da = _dir_interior(corner_pt, borde_a_p1, borde_a_p2)
    db = _dir_interior(corner_pt, borde_b_p1, borde_b_p2)

    sin_t = abs(da.X * db.Y - da.Y * db.X)
    if sin_t < SIN_MINIMO:
        sin_t = SIN_MINIMO

    size = max(lado_base, CLARIDAD_MINIMA_M / sin_t)
    size_area = math.sqrt(AREA_MINIMA_M2 / sin_t)
    if size < size_area:
        size = size_area

    len_a = borde_a_p1.DistanceTo(borde_a_p2)
    len_b = borde_b_p1.DistanceTo(borde_b_p2)
    if size > 0.98 * min(len_a, len_b):
        return None

    p0 = rg.Point3d(corner_pt)
    p1 = rg.Point3d(p0.X + da.X * size, p0.Y + da.Y * size, p0.Z)
    p3 = rg.Point3d(p0.X + db.X * size, p0.Y + db.Y * size, p0.Z)
    p2 = rg.Point3d(p1.X + db.X * size, p1.Y + db.Y * size, p0.Z)

    # Validacion de interioridad: p1/p3 caen sobre los bordes del lote (dentro
    # de la tolerancia de borde de point_in_lot) y p2 debe quedar adentro.
    if not (point_in_lot(p1, lot_vertices)
            and point_in_lot(p2, lot_vertices)
            and point_in_lot(p3, lot_vertices)):
        return None

    poly = rg.Polyline()
    poly.Add(p0); poly.Add(p1); poly.Add(p2); poly.Add(p3); poly.Add(p0)
    return (rg.PolylineCurve(poly), (size, sin_t), [p0, p1, p2, p3])


# ==============================================================================
# MAIN
# ==============================================================================

lot_vertices_raw = globals().get("lot_vertices", None)
sides_raw = globals().get("sides_table_json", None)
altura_raw = globals().get("altura_max_pot", None)

lot_vertices = safe_list(lot_vertices_raw)
n_vertices_brutos = len(lot_vertices)
# v02.3: simplificacion de lados colineales (giro < 2.5 grados), identica a
# la que aplica LADOS v06.5 sobre el mismo input -> los indices del JSON de
# lados coinciden con esta lista simplificada.
lot_vertices = simplificar_colineales(lot_vertices, UMBRAL_COLINEAL_GRADOS)

sides_data = None
if sides_raw is not None:
    try:
        if isinstance(sides_raw, list) and sides_raw:
            s = str(sides_raw[0])
        else:
            s = str(sides_raw)
        sides_data = json.loads(s)
    except:
        sides_data = None

try:
    altura_max = float(unwrap(altura_raw)) if altura_raw else 11.4
except:
    altura_max = 11.4

patios_curves = []
patio_count = 0

if sides_data is None or len(lot_vertices) < 3:
    mensaje = "PATIO v02.4 | ERROR: vertices={} sides={}".format(
        len(lot_vertices), "OK" if sides_data else "FALTA")
else:
    try:
        lados = sides_data.get("lados", [])
        vertice_n = sides_data.get("vertice_n", None)
        n = len(lot_vertices)

        if vertice_n is None:
            mensaje = "PATIO v02.4 | ERROR: sides_table_json sin vertice_n (usar F1_ETAPA2_LADOS_v06)"
        else:
            # Tamano base del patio segun altura (reglamentacion POT)
            pisos = max(1, int(math.ceil(altura_max / ALTURA_ENTREPISO)))
            patio_lado_base = max(PATIO_MINIMO_M, pisos * 0.25)

            resultados = []
            descartes = []

            def _intentar(vi, idx, etiqueta):
                if len(lados) >= n and n > 0:
                    lado1 = lados[idx]
                    lado2 = lados[(idx + n - 1) % n]
                else:
                    lado1 = {}
                    lado2 = {}
                cat1 = lado1.get("clasificacion", "Desconocido")
                cat2 = lado2.get("clasificacion", "Desconocido")
                if not (cat1 in ("Lateral", "Posterior") and cat2 in ("Lateral", "Posterior")):
                    descartes.append("{}: V{} sin lados colindantes ({},{})".format(
                        etiqueta, idx, cat1, cat2))
                    return None
                va1 = vi
                va2 = lot_vertices[(idx + 1) % n]
                vb1 = lot_vertices[(idx + n - 1) % n]
                vb2 = vi
                res = build_patio_desde_vertice(
                    vi, va1, va2, vb1, vb2, patio_lado_base, lot_vertices)
                if res is None:
                    descartes.append("{}: patio en V{} no valida (no cabe / no interior)".format(
                        etiqueta, idx))
                    return None
                return res

            # 1) Puntos mejorados de Vertice N (v02.2) con dedup y filtro de
            #    coincidencia con vertices del lote (v02.3).
            vertice_n_points_data = sides_data.get("vertice_n_points")
            candidatos = []
            if vertice_n_points_data:
                for coords in vertice_n_points_data:
                    try:
                        candidatos.append(rg.Point3d(
                            coords[0], coords[1],
                            coords[2] if len(coords) > 2 else 0))
                    except Exception:
                        pass
                candidatos = deduplicar_puntos(candidatos, CLUSTER_PUNTOS_M)

            for vi in candidatos:
                min_dist = float('inf')
                idx = 0
                for i, v in enumerate(lot_vertices):
                    dist = v.DistanceTo(vi)
                    if dist < min_dist:
                        min_dist = dist
                        idx = i
                if min_dist > COINCIDENCIA_VERTICE_M:
                    descartes.append("mejorado ({:.2f},{:.2f}) a {:.2f} m de un vertice".format(
                        vi.X, vi.Y, min_dist))
                    continue
                res = _intentar(vi, idx, "mejorado")
                if res:
                    resultados.append((res[0], res[1], res[2], idx))
                    break  # v02.3: maximo 1 patio

            # 2) Fallback tradicional (indice vertice_n) si no hubo resultado.
            if not resultados:
                vi = lot_vertices[vertice_n]
                res = _intentar(vi, vertice_n, "fallback")
                if res:
                    resultados.append((res[0], res[1], res[2], vertice_n))

            cats = [l.get("clasificacion", "?") for l in lados]

            if resultados:
                crv, info, pts_patio, idx_usado = resultados[0]
                size = info[0]
                sin_t = info[1]
                area = size * size * sin_t
                claridad = size * sin_t
                patios_curves = [crv]
                patio_count = 1
                patios_export = [{
                    "puntos": [[p.X, p.Y] for p in pts_patio],
                    "lado_m": round(size, 4),
                    "area_m2": round(area, 4),
                    "claridad_m": round(claridad, 4),
                }]
                modo = "puntos_mejorados" if candidatos else "fallback_V_N"
                mensaje = ("PATIO v02.4 | V_N=V{} | Verts {}->{} | Lados: {} | "
                           "Patio {:.2f}x{:.2f} m (area {:.2f} m2; claridad {:.2f} m) | "
                           "Generados: 1 | Modo: {}").format(
                    idx_usado, n_vertices_brutos, n, ", ".join(cats),
                    size, size, area, claridad, modo)
                if descartes:
                    mensaje += " | Descartes: " + "; ".join(descartes[:3])
            else:
                patios_export = []
                mensaje = ("PATIO v02.4 | V_N=V{} | Verts {}->{} | Lados: {} | "
                           "Generados: 0 | Motivo: {}").format(
                    vertice_n, n_vertices_brutos, n, ", ".join(cats),
                    "; ".join(descartes) if descartes else "sin candidatos de esquina")

            # v02.4: export del diagnostico si el servidor/orquestador lo solicito
            try:
                ruta_diag = _exportar_diagnostico(sides_data, patios_export, mensaje)
                if ruta_diag:
                    mensaje += " | Lados export OK: {}".format(ruta_diag)
            except Exception as _e_exp:
                mensaje += " | Lados export aviso: {}".format(str(_e_exp))

    except Exception as e:
        mensaje = "PATIO v02.4 | ERROR: {}".format(str(e))
