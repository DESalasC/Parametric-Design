# -*- coding: utf-8 -*-
"""F1_ETAPA1_CONTEXTO_v05: bandas 3D drapeadas (salidas nuevas para el canvas v12).

Ejecuta el componente con un stub minimo de Rhino.Geometry (solo Mesh) y
verifica conteos de vertices/caras, rango de cotas (IDW del MDT) y el modo
abierto/cerrado. Corre en CPython (no requiere Rhino).
"""

import io
import json
import os
import sys
import types

BASE = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
SRC = os.path.join(BASE, "src", "fase-1-contexto", "F1_ETAPA1_CONTEXTO_v05.py")
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


def _cargar_componente():
    """Ejecuta el componente con json_path invalido (no corre el MAIN) y stubs.

    Devuelve el namespace para llamar directamente banda_drapeada() etc."""
    rg = types.ModuleType("Rhino.Geometry")
    rg.Mesh = _MeshFake
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


def test_banda_cerrada_conteos():
    ns = _cargar_componente()
    lote, pts_mdt = _datos_b()
    m = ns["banda_drapeada"](lote, 0.0, 0.0, 0.0, pts_mdt, ancho=0.5, prof=0.5, cerrada=True)
    assert m is not None
    n = len(lote) if lote[0] == lote[-1] else len(lote) + 1
    assert len(m.pts) == 4 * n
    assert len(m.faces) == 4 * n  # 4 caras por segmento, sin tapas (anillo)


def test_banda_abierta_caps():
    ns = _cargar_componente()
    lote, pts_mdt = _datos_b()
    crv = [lote[0], lote[1], lote[2]]
    m = ns["banda_drapeada"](crv, 0.0, 0.0, 0.0, pts_mdt, cerrada=False)
    assert m is not None
    assert len(m.pts) == 4 * 3
    assert len(m.faces) == 4 * 2 + 2  # segmentos + 2 tapas


def test_z_dentro_del_rango_mdt():
    ns = _cargar_componente()
    lote, pts_mdt = _datos_b()
    m = ns["banda_drapeada"](lote, 0.0, 0.0, 0.0, pts_mdt, ancho=0.5, prof=0.5)
    zs = [p[2] for p in m.pts]
    zmin = min(p[2] for p in pts_mdt) - 0.5 - 1e-6
    zmax = max(p[2] for p in pts_mdt) + 1e-6
    assert zmin <= min(zs) and max(zs) <= zmax


def test_idw_z_exacto_en_muestra():
    ns = _cargar_componente()
    lote, pts_mdt = _datos_b()
    px, py, pz = pts_mdt[0]
    assert abs(ns["_idw_z"](px, py, pts_mdt) - pz) < 1e-9


def test_categoria_multiples():
    ns = _cargar_componente()
    lote, pts_mdt = _datos_b()
    vias = [lote[:4], lote[4:8]]
    bandas = ns["bandas_por_categoria"](vias, 0.0, 0.0, 0.0, pts_mdt, cerrada=False)
    assert len(bandas) == 2
    assert all(m is not None and len(m.faces) > 0 for m in bandas)
