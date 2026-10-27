# -*- coding: utf-8 -*-
import io
import json
import math
from shapely.geometry import Polygon, LineString, MultiLineString

c1 = json.load(io.open("data/pot-cache/AAA0030JKOE-contexto.json", encoding="utf-8"))
lot = Polygon([(v[0], v[1]) for v in c1["lote_objetivo"]["vertices_3d_local"][:-1]])
buf = lot.buffer(75.0)
print("buffer area", buf.area)


def dist(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])


def dp(pts, tol=1.0):
    if len(pts) < 3:
        return pts
    a, b = pts[0], pts[-1]
    imax, dmax = 0, -1.0
    for i in range(1, len(pts) - 1):
        p = pts[i]
        dx, dy = b[0] - a[0], b[1] - a[1]
        L2 = dx * dx + dy * dy
        d = dist(p, a) if L2 < 1e-12 else math.hypot(
            p[0] - (a[0] + max(0, min(1, ((p[0] - a[0]) * dx + (p[1] - a[1]) * dy) / L2)) * dx),
            p[1] - (a[1] + max(0, min(1, ((p[0] - a[0]) * dx + (p[1] - a[1]) * dy) / L2)) * dy))
        if d > dmax:
            imax, dmax = i, d
    if dmax > tol:
        return dp(pts[:imax + 1], tol)[:-1] + dp(pts[imax:], tol)
    return [a, b]


def heading(a, b):
    return math.atan2(b[1] - a[1], b[0] - a[0])


def split(pts, ang=8.0, min_len=20.0):
    raw = [0]
    for i in range(1, len(pts) - 1):
        h1 = heading(pts[i - 1], pts[i]); h2 = heading(pts[i], pts[i + 1])
        if abs((h2 - h1 + math.pi) % (2 * math.pi) - math.pi) > math.radians(ang):
            raw.append(i)
    raw.append(len(pts) - 1)
    out = []
    for k in range(len(raw) - 1):
        a, b = raw[k], raw[k + 1]
        L = sum(dist(pts[i], pts[i + 1]) for i in range(a, b))
        if out and L < min_len:
            out[-1] = (out[-1][0], b)
        else:
            out.append((a, b))
    return [(a, b, sum(dist(pts[i], pts[i + 1]) for i in range(a, b))) for a, b in out]


n_v = n_t = n_k = 0
for v in c1.get("vias_oficiales") or []:
    pts = [(p[0], p[1]) for p in (v.get("coordenadas_local") or [])]
    if len(pts) < 2:
        continue
    ls = LineString(pts).intersection(buf)
    geoms = [ls] if ls.geom_type == "LineString" else list(getattr(ls, "geoms", []))
    for g in geoms:
        if g.is_empty or g.geom_type != "LineString":
            continue
        p2 = dp(list(g.coords), 1.0)
        tr = split(p2)
        n_v += 1
        n_t += len(tr)
        for (a, b, L) in tr:
            n_k += max(2, min(9, int(math.ceil(L / 20.0)) + 1))
print("vias recortadas a 75m: segmentos", n_v, "tramos", n_t, "muestras", n_k)

n_ep = n_vp = 0
for ep in c1.get("espacios_publicos") or []:
    pts = [(p[0], p[1]) for p in (ep.get("coordenadas_local") or [])]
    if len(pts) < 3:
        continue
    poly = Polygon(pts)
    g = poly.intersection(buf)
    if g.is_empty:
        continue
    n_ep += 1
    for ring in ([g.exterior] if hasattr(g, "exterior") else []):
        n_vp += len(list(ring.coords)) - 1
    if hasattr(g, "geoms"):
        for sub in g.geoms:
            if hasattr(sub, "exterior"):
                n_vp += len(list(sub.exterior.coords)) - 1
print("EP recortados:", n_ep, "vertices:", n_vp)
print("TOTAL estimado:", n_k + n_vp)
