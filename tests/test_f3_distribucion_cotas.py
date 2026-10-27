# -*- coding: utf-8 -*-
"""Cota de arranque de los bloques (ZONAS) contra el terreno.

Regla (v03.10, 2026-10-26): el bloque apoya en el punto MAS BAJO de su huella
(centroide + vertices + puntos medios), no en la cota del centroide. Antes, en
ladera, el volumen flotaba en su borde de aguas abajo.
"""
import json
import os
import sys
import types

sys.path.insert(0, os.path.dirname(__file__))
from test_f3_distribucion_v03_gh import _base_fixture, _ejecutar_como_gh  # noqa: E402


class _Pt(object):
    def __init__(self, x, y, z):
        self.X, self.Y, self.Z = x, y, z


class _Vec(object):
    def __init__(self, x, y, z):
        self.X, self.Y, self.Z = x, y, z


class _Ray(object):
    def __init__(self, origen, direccion):
        self.origin, self.direction = origen, direccion

    def PointAt(self, t):
        return _Pt(self.origin.X + t * self.direction.X,
                   self.origin.Y + t * self.direction.Y,
                   self.origin.Z + t * self.direction.Z)


class _BBox(object):
    def __init__(self, z_max):
        self.Max = _Pt(0.0, 0.0, z_max)


class _Mesh(object):
    """Malla falsa: superficie z = f(x, y) con caja -100..+100."""

    def __init__(self, f):
        self.f = f

    def GetBoundingBox(self, exact):
        return _BBox(100.0)


def _instalar_rhino(f):
    rg = types.ModuleType("Rhino.Geometry")
    rg.Point3d = _Pt
    rg.Vector3d = _Vec
    rg.Ray3d = _Ray
    rg.Mesh = _Mesh

    class _Intersection(object):
        @staticmethod
        def MeshRay(mesh, ray):
            # rayo vertical descendente: t = z_origen - f(x, y)
            return ray.origin.Z - mesh.f(ray.origin.X, ray.origin.Y)

    class _Intersect(object):
        Intersection = _Intersection

    rg.Intersect = _Intersect
    rhino = types.ModuleType("Rhino")
    rhino.Geometry = rg
    sys.modules["Rhino"] = rhino
    sys.modules["Rhino.Geometry"] = rg
    sys.modules.pop("rhinoscriptsyntax", None)


def _bloques(ns):
    data = json.loads(ns["barras_json"])
    alt = next(a for a in data["alternativas"] if a["id"] == data["recomendada"])
    return alt["bloques"]


def _correr(f):
    _instalar_rhino(f)
    return _ejecutar_como_gh({
        "chip": "AAA0030JKOE",
        "base_normativa_json": _base_fixture(),
        "topo_mesh": _Mesh(f),
    })


def test_cota_arranque_es_el_minimo_de_la_huella():
    """Ladera z = 0.1*y (3,8 m en 38 m de fondo): la cota es la del borde bajo."""
    bloques = _bloques(_correr(lambda x, y: 0.1 * y))
    assert len(bloques) >= 2
    for b in bloques:
        ys = [p[1] for p in b["huella_xy"]]
        esperado = round(0.1 * min(ys), 3)
        assert abs(b["cota_arranque_m"] - esperado) < 0.002, (b["id"], b["cota_arranque_m"], esperado)
        # el centroide siempre queda por encima del minimo en una ladera
        assert b["cota_arranque_centroide_m"] > b["cota_arranque_m"]
        assert b["cota_arranque_max_m"] >= b["cota_arranque_centroide_m"]
        assert b["cota_arranque_n_puntos"] >= 5
        assert "minimo del terreno bajo la huella" in b["criterio_arranque"]

    # los bloques NO comparten cota: cada uno arranca donde esta su borde bajo
    cotas = [b["cota_arranque_m"] for b in bloques]
    assert len(set(cotas)) == len(cotas)


def test_aviso_de_bajada_respecto_al_centroide():
    ns = _correr(lambda x, y: 0.1 * y)
    avisos = json.loads(ns["barras_json"])["alternativas"][0]["avisos"]
    assert any("bajada media" in a for a in avisos), avisos


def test_cota_fija_del_operador_manda():
    """Con `cota_arranque_m` como entrada se respeta la cota fija (sin muestreo)."""
    _instalar_rhino(lambda x, y: 0.1 * y)
    ns = _ejecutar_como_gh({
        "chip": "AAA0030JKOE",
        "base_normativa_json": _base_fixture(),
        "topo_mesh": _Mesh(lambda x, y: 0.1 * y),
        "cota_arranque_m": 7.25,
    })
    for b in _bloques(ns):
        assert abs(b["cota_arranque_m"] - 7.25) < 1e-6
        assert b["criterio_arranque"] == "cota fija del operador"


def test_sin_malla_mantiene_comportamiento_previo():
    """Sin topografia el canal de respaldo sigue dando z0 = 0 con aviso."""
    _instalar_rhino(lambda x, y: 0.0)
    ns = _ejecutar_como_gh({"chip": "AAA0030JKOE", "base_normativa_json": _base_fixture()})
    for b in _bloques(ns):
        assert b["cota_arranque_m"] == 0.0
    avisos = json.loads(ns["barras_json"])["alternativas"][0]["avisos"]
    assert any("sin topografia utilizable" in a for a in avisos)
