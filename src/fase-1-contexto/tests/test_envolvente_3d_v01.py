# -*- coding: utf-8 -*-
"""Tests offline de F1_ETAPA2_ENVOLVENTE_3D_v01 (curva + banda + volumen).

Ejecuta el componente con stubs minimos de Rhino.Geometry (Mesh, Polyline,
PolylineCurve, Curve.DivideByCount) y verifica conteos y rangos de cota.
Corre en CPython (no requiere Rhino).
"""

import io
import json
import os
import sys
import types

BASE = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
SRC = os.path.join(BASE, "src", "fase-1-contexto", "F1_ETAPA2_ENVOLVENTE_3D_v01.py")
JSON_B = os.path.join(BASE, "data", "pot-cache", "AAA0030JKOE-contexto.json")


class _MeshFake(object):
    class _V(object):
        def __init__(self, m):
            self.m = m

        def Add(self, x, y, z):
            self.m.pts.append((float(x), float(y), float(z)))
            return len(self.m.pts) - 1

    class _F(object):
        def __init__(self, m):
            self.m = m

        def AddFace(self, a, b, c, d=None):
            self.m.faces.append(tuple(x for x in (a, b, c, d) if x is not None))
            return len(self.m.faces) - 1

    class _N(object):
        def ComputeNormals(self):
            pass

    def __init__(self):
        self.pts = []
        self.faces = []
        self.Vertices = _MeshFake._V(self)
        self.Faces = _MeshFake._F(self)
        self.Normals = _MeshFake._N()

    def Compact(self):
        pass


class _PolylineFake(object):
    def __init__(self):
        self.pts = []

    def Add(self, *args):
        if len(args) == 1 and isinstance(args[0], (tuple, list)):
            x, y = args[0][0], args[0][1]
            z = args[0][2] if len(args[0]) > 2 else 0.0
        else:
            x, y = args[0], args[1]
            z = args[2] if len(args) > 2 else 0.0
        self.pts.append((float(x), float(y), float(z if z is not None else 0.0)))

    def __getitem__(self, i):
        return self.pts[i]

    @property
    def IsClosed(self):
        if len(self.pts) < 2:
            return False
        return abs(self.pts[0][0] - self.pts[-1][0]) < 1e-9 and abs(self.pts[0][1] - self.pts[-1][1]) < 1e-9


class _PolylineCurveFake(object):
    def __init__(self, poly):
        self.Polyline = poly
        self.pts = poly.pts


class _Pt(object):
    def __init__(self, x, y, z=0.0):
        self.X = float(x)
        self.Y = float(y)
        self.Z = float(z)


class _CrvFake(object):
    """Curva minimima: PointAt(t) interpola linealmente sobre una lista de puntos."""

    def __init__(self, pts):
        self.pts = [_Pt(*p) for p in pts]

    def PointAt(self, t):
        i = int(round(float(t) * (len(self.pts) - 1)))
        i = max(0, min(i, len(self.pts) - 1))
        return self.pts[i]


class _CurveStatic(object):
    @staticmethod
    def DivideByCount(crv, n, includeEnds):
        return [i / float(n) for i in range(n + 1)]


def _cargar_componente():
    rg = types.ModuleType("Rhino.Geometry")
    rg.Mesh = _MeshFake
    rg.Polyline = _PolylineFake
    rg.PolylineCurve = _PolylineCurveFake
    rg.Point3d = lambda x, y, z: (float(x), float(y), float(z))
    rg.Curve = _CurveStatic
    with io.open(SRC, "rb") as f:
        fuente = f.read().decode("utf-8")
    ns = {"__name__": "envolvente3d_test"}
    sys.modules["Rhino.Geometry"] = rg
    rh = types.ModuleType("Rhino")
    rh.Geometry = rg
    sys.modules["Rhino"] = rh
    exec(compile(fuente, SRC, "exec"), ns)
    return ns


def _datos_b():
    with io.open(JSON_B, "rb") as f:
        data = json.loads(f.read().decode("utf-8"))
    lote = [tuple(v) for v in data["lote_objetivo"]["vertices_3d_local"]]
    mesh = data["topografia"]["malla_terreno"]
    pts_mdt = [(p["x_local"], p["y_local"], p["z_local"]) for p in mesh]
    return lote, pts_mdt


def test_componente_existe():
    assert os.path.isfile(SRC)


def test_prisma_conteos():
    ns = _cargar_componente()
    cuadro = [(0.0, 0.0), (10.0, 0.0), (10.0, 10.0), (0.0, 10.0)]
    m = ns["prisma_desde_poligono"](cuadro, 0.0, 3.0)
    assert m is not None
    assert len(m.pts) == 8            # 4 abajo + 4 arriba
    assert len(m.faces) == 4 + 4      # paredes + 2 tapas (4 triangulos en total con n=4)


def test_banda_envolvente_no_none():
    ns = _cargar_componente()
    lote, pts_mdt = _datos_b()
    lote_xy = [(v[0], v[1]) for v in lote]
    m = ns["banda_drapeada"](lote_xy, pts_mdt)
    assert m is not None
    assert len(m.pts) >= 4 * 4


def test_muestreo_curva():
    ns = _cargar_componente()
    crv = _CrvFake([(0, 0, 0), (10, 0, 0), (10, 10, 0), (0, 10, 0)])
    pts = ns["_puntos_de_curva"](crv, n=64)
    assert len(pts) == 65
    xy = ns["_pts_a_tuplas"](pts)
    assert len(xy) == 65
    assert xy[0] == (0.0, 0.0)


def test_curva_drapeada_cierra():
    ns = _cargar_componente()
    lote, pts_mdt = _datos_b()
    lote_xy = [(v[0], v[1]) for v in lote]
    c = ns["curva_drapeada"](lote_xy, pts_mdt)
    assert c is not None
    n = len(lote_xy) if lote_xy[0] == lote_xy[-1] else len(lote_xy) + 1
    assert len(c.pts) == n


def test_prisma_alto_cero_none():
    ns = _cargar_componente()
    cuadro = [(0.0, 0.0), (5.0, 0.0), (5.0, 5.0)]
    assert ns["prisma_desde_poligono"](cuadro, 0.0, 0.0) is None
