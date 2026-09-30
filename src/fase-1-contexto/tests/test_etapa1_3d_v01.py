# -*- coding: utf-8 -*-
"""Tests offline de F1_ETAPA1_CONTEXTO_3D_v01 (ramas 3D para el canvas v12).

Ejecuta el componente con stubs minimos de Rhino.Geometry (Mesh, Polyline,
PolylineCurve, Point3d) y verifica: curvas drapeadas cerradas, bandas
(existentes) y utilidades. Corre en CPython (no requiere Rhino).
"""

import io
import json
import os
import sys
import types

BASE = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
SRC = os.path.join(BASE, "src", "fase-1-contexto", "F1_ETAPA1_CONTEXTO_3D_v01.py")
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


def _cargar_componente():
    rg = types.ModuleType("Rhino.Geometry")
    rg.Mesh = _MeshFake
    rg.Polyline = _PolylineFake
    rg.PolylineCurve = _PolylineCurveFake
    rg.Point3d = lambda x, y, z: (float(x), float(y), float(z))
    rhino = types.ModuleType("Rhino")
    rhino.Geometry = rg
    system = types.ModuleType("System")
    system.IO = types.ModuleType("System.IO")
    system.Text = types.ModuleType("System.Text")
    sys.modules["Rhino"] = rhino
    sys.modules["Rhino.Geometry"] = rg
    sys.modules["System"] = system
    sys.modules["System.IO"] = system.IO
    sys.modules["System.Text"] = system.Text
    with io.open(SRC, "rb") as f:
        fuente = f.read().decode("utf-8")
    ns = {"json_path": None}
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
    assert os.path.isfile(JSON_B)


def test_curva_drapeada_cierra_y_cotiza():
    ns = _cargar_componente()
    lote, pts_mdt = _datos_b()
    c = ns["curva_drapeada"](lote, 0.0, 0.0, 0.0, pts_mdt, cerrada=True)
    assert c is not None
    n = len(lote) if lote[0] == lote[-1] else len(lote) + 1
    assert len(c.pts) == n
    assert abs(c.pts[0][0] - c.pts[-1][0]) < 1e-9
    zs = [p[2] for p in c.pts]
    zmin = min(p[2] for p in pts_mdt) - 1e-6
    zmax = max(p[2] for p in pts_mdt) + 1e-6
    assert zmin <= min(zs) and max(zs) <= zmax


def test_banda_drapeada_conteos():
    ns = _cargar_componente()
    lote, pts_mdt = _datos_b()
    m = ns["banda_drapeada"](lote, 0.0, 0.0, 0.0, pts_mdt, cerrada=True)
    assert m is not None
    n = len(lote) if lote[0] == lote[-1] else len(lote) + 1
    assert len(m.pts) == 4 * n
    assert len(m.faces) == 4 * n


def test_rectangulo_horizontal():
    ns = _cargar_componente()
    rc = ns["_rectangulo_horizontal"](0.0, 0.0, 10.0, 5.0, 0.0)
    assert rc is not None
    assert len(rc.pts) == 5
    assert rc.pts[0] == rc.pts[-1]
    assert all(abs(p[2]) < 1e-12 for p in rc.pts)


def test_parse_bool_defaults():
    ns = _cargar_componente()
    assert ns["parse_bool"](None, True) is True
    assert ns["parse_bool"]("false", True) is False
    assert ns["parse_bool"]("True", False) is True


def test_bandas_por_categoria():
    ns = _cargar_componente()
    lote, pts_mdt = _datos_b()
    bandas = ns["bandas_por_categoria"]([lote[:4], lote[4:8]], 0.0, 0.0, 0.0, pts_mdt, cerrada=False)
    assert len(bandas) == 2
    assert all(m is not None and len(m.faces) > 0 for m in bandas)
