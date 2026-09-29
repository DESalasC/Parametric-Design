# -*- coding: utf-8 -*-
"""Tests de lógica para F1_CONTEXTO50_BUILD_v01b.py (componente GHPython).

Ejecuta el script del componente con módulos Rhino/System simulados y copias
aisladas del JSON real de contexto 50 m (con/sin hermano CHIP-contexto.json),
verificando parsing, deduplicación, exclusiones, orientación, alturas y conteos.
Corre en CPython (no requiere Rhino).
"""

import io
import json
import os
import shutil
import sys
import tempfile
import types

import pytest

SRC = os.path.join(
    os.path.dirname(__file__), "..", "F1_CONTEXTO50_BUILD_v01b.py"
)
JSON_REAL = os.path.join(
    r"D:\Work\PROJECTS\DiseñoParametrico", "data", "pot-cache",
    "AAA0240ZXJH-contexto50.json",
)
JSON_BASE_REAL = os.path.join(
    r"D:\Work\PROJECTS\DiseñoParametrico", "data", "pot-cache",
    "AAA0240ZXJH-contexto.json",
)


def _fixture_dir(con_hermano=True):
    """Carpeta aislada con copias del fixture (no depender del pot-cache vivo).

    Incluye contexto50 + (opcional) hermano `CHIP-contexto.json`, el nombre que
    el componente espera para excluir las construcciones del predio objetivo.
    """
    d = tempfile.mkdtemp(prefix="dp_ctx50_fixture_")
    shutil.copy2(JSON_REAL, os.path.join(d, "AAA0240ZXJH-contexto50.json"))
    if con_hermano:
        shutil.copy2(JSON_BASE_REAL, os.path.join(d, "CHIP-contexto.json"))
    return d


# ------------------------------------------------------------------ stubs Rhino
def _instalar_stubs():
    rg = types.ModuleType("Rhino.Geometry")

    class Polyline(object):
        def __init__(self):
            self.pts = []

        def Add(self, x, y, z):
            self.pts.append((x, y, z))

    class PolylineCurve(object):
        def __init__(self, pl):
            self.pts = list(pl.pts)

        def MakeClosed(self, tol):
            return True

    class _Brep(object):
        def __init__(self, crv, h):
            self.crv = crv
            self.h = h
            self.IsValid = True

    class Extrusion(object):
        @staticmethod
        def Create(crv, h, capped):
            return types.SimpleNamespace(ToBrep=lambda: _Brep(crv, h))

    rg.Polyline = Polyline
    rg.PolylineCurve = PolylineCurve
    rg.Extrusion = Extrusion

    rhino = types.ModuleType("Rhino")
    rhino.Geometry = rg

    class UnitSystem(object):
        Meters = "m"

    rhino.UnitSystem = UnitSystem

    class _RhinoDoc(object):
        ActiveDoc = None

    rhino.RhinoDoc = _RhinoDoc

    drawing = types.ModuleType("System.Drawing")

    class _Color(object):
        @staticmethod
        def FromArgb(a, b, c):
            return (a, b, c)

    drawing.Color = _Color

    system = types.ModuleType("System")
    system.Drawing = drawing

    sys.modules["Rhino"] = rhino
    sys.modules["Rhino.Geometry"] = rg
    sys.modules["System"] = system
    sys.modules["System.Drawing"] = drawing


def _ejecutar_componente(json_path, altura_piso=None, bake=False, exportar=False,
                         src=SRC, env_root=None):
    _instalar_stubs()
    with io.open(src, "rb") as f:
        fuente = f.read().decode("utf-8")
    ns = {"json_path": json_path, "bake": bake, "exportar": exportar}
    if altura_piso is not None:
        ns["altura_piso"] = altura_piso
    # Aislamiento: sin DISENO_PARAMETRICO_ROOT no se encuentra el canónico real
    # (data/pot-cache/contexto50-actual.json) y manda el parámetro json_path.
    viejo = os.environ.get("DISENO_PARAMETRICO_ROOT")
    raiz = env_root or tempfile.mkdtemp(prefix="dp_ctx50_root_")
    os.environ["DISENO_PARAMETRICO_ROOT"] = raiz
    try:
        exec(compile(fuente, src, "exec"), ns)
    finally:
        if viejo is None:
            os.environ.pop("DISENO_PARAMETRICO_ROOT", None)
        else:
            os.environ["DISENO_PARAMETRICO_ROOT"] = viejo
    return ns


def _area_shoelace(pts):
    a = 0.0
    n = len(pts)
    for i in range(n):
        x1, y1 = pts[i]
        x2, y2 = pts[(i + 1) % n]
        a += x1 * y2 - x2 * y1
    return abs(a) / 2.0


# ------------------------------------------------------------------ tests
def test_json_real_existe():
    assert os.path.isfile(JSON_REAL), "Falta el JSON real de contexto50"


def test_66_volumenes_con_exclusiones():
    """Fixture con hermano CHIP-contexto.json: 94 - 4 predio - 24 menores = 66."""
    d = _fixture_dir(con_hermano=True)
    ns = _ejecutar_componente(os.path.join(d, "AAA0240ZXJH-contexto50.json"))
    assert len(ns["volumenes"]) == 66
    assert len(ns["huellas"]) == 66
    assert len(ns["alturas"]) == 66
    assert len(ns["pisos"]) == 66
    assert len(ns["ids"]) == 66
    assert ns["capa"] == "70-20-30_Volumetrias_vecinas"
    assert "Volumenes 66/94" in ns["mensaje"]
    assert "Excluidos: 4 predio objetivo, 24 andenes/menores" in ns["mensaje"]
    # el predio de referencia (004413004056...) no debe tener volumen
    assert not [i for i in ns["ids"] if i.startswith("004413004056")]


def test_rangos_altura_coinciden_con_metadata():
    with io.open(JSON_REAL, "rb") as f:
        data = json.loads(f.read().decode("utf-8"))
    d = _fixture_dir(con_hermano=True)
    ns = _ejecutar_componente(os.path.join(d, "AAA0240ZXJH-contexto50.json"))
    assert abs(min(ns["alturas"]) - 3.8) < 1e-6
    assert abs(max(ns["alturas"]) - 19.0) < 1e-6
    assert max(ns["pisos"]) == data["metadata"]["conteo"]["pisos_max"]


def test_areas_shoelace_vs_area_m2():
    with io.open(JSON_REAL, "rb") as f:
        data = json.loads(f.read().decode("utf-8"))
    # primer registro: área declarada vs área del anillo normalizado
    ed = data["edificios"][0]
    raw = ed["anillos"][0]
    pts = [(p[0], p[1]) for p in raw]
    if abs(pts[0][0] - pts[-1][0]) < 0.01 and abs(pts[0][1] - pts[-1][1]) < 0.01:
        pts = pts[:-1]
    area = _area_shoelace(pts)
    assert abs(area - ed["area_m2"]) / ed["area_m2"] < 0.02


def test_json_path_envuelto_en_lista_se_acepta():
    d = _fixture_dir(con_hermano=True)
    ns = _ejecutar_componente([os.path.join(d, "AAA0240ZXJH-contexto50.json")])
    assert len(ns["volumenes"]) == 66


def test_sin_ctx1_hermano_mantiene_94():
    """Sin CHIP-contexto.json hermano no hay exclusion por lote (solo menores)."""
    d = _fixture_dir(con_hermano=False)
    ns = _ejecutar_componente(os.path.join(d, "AAA0240ZXJH-contexto50.json"))
    assert len(ns["volumenes"]) == 68  # 94 - 26 menores (sin lote hermano)
    assert "sin CHIP-contexto.json" in ns["mensaje"]


def test_registro_defectuoso_no_mata_el_componente():
    d = _fixture_dir(con_hermano=False)
    with io.open(JSON_REAL, "rb") as f:
        data = json.loads(f.read().decode("utf-8"))
    data["edificios"].append({"id": "ROTO", "vertices": "no-soy-una-lista"})
    tmp = os.path.join(d, "AAA0240ZXJH-contexto50.json")
    with io.open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)
    ns = _ejecutar_componente(tmp)
    assert len(ns["volumenes"]) == 68  # 94 - 26 menores; el roto no mata
    assert ns["mensaje"].count("Descartados 27") == 1


def test_sin_json_path_mensaje_alerta():
    ns = _ejecutar_componente(None)
    assert "json_path" in ns["mensaje"]
    assert ns["volumenes"] == []


def test_altura_piso_override_cuando_json_no_trae():
    with io.open(JSON_REAL, "rb") as f:
        data = json.loads(f.read().decode("utf-8"))
    del data["metadata"]["altura_por_piso_m"]
    # registro CON pisos=2 -> 2 * override; sin pisos -> fallback documentado 3.0 m
    data["edificios"] = [
        {"id": "X", "vertices": [[0, 0], [10, 0], [10, 10], [0, 10]], "pisos": 2},
        {"id": "Y", "vertices": [[0, 0], [5, 0], [5, 5], [0, 5]]},
    ]
    tmp = os.path.join(tempfile.mkdtemp(prefix="dp_ctx50_ovr_"),
                       "AAA0240ZXJH-contexto50.json")
    with io.open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)
    ns = _ejecutar_componente(tmp, altura_piso=3.5)
    assert abs(ns["alturas"][0] - 7.0) < 1e-6
    assert ns["pisos"][0] == 2
    assert abs(ns["alturas"][1] - 3.0) < 1e-6  # fallback DOCUMENTADO (1 planta)
    assert ns["pisos"][1] == 1


def test_anillo_horario_se_invierte_a_antihorario():
    """Anillos horarios del fetch GIS deben salir CCW (extrusion +Z)."""
    with io.open(JSON_REAL, "rb") as f:
        data = json.loads(f.read().decode("utf-8"))
    ed = data["edificios"][0]
    pts = [list(p) for p in ed["anillos"][0]]
    if pts[0] == pts[-1]:
        pts = pts[:-1]
    s = 0.0
    n = len(pts)
    for i in range(n):
        x1, y1 = pts[i]
        x2, y2 = pts[(i + 1) % n]
        s += x1 * y2 - x2 * y1
    assert s < 0, "el anillo real deberia ser horario (precondicion del test)"

    data["edificios"] = [ed]
    tmp = os.path.join(tempfile.mkdtemp(prefix="dp_ctx50_orient_"),
                       "AAA0240ZXJH-contexto50.json")
    with io.open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)
    ns = _ejecutar_componente(tmp)
    p3 = ns["huellas"][0].pts  # stub: [(x, y, z), ...] con cierre duplicado
    u = p3[:-1]
    s2 = 0.0
    n2 = len(u)
    for i in range(n2):
        x1, y1 = u[i][0], u[i][1]
        x2, y2 = u[(i + 1) % n2][0], u[(i + 1) % n2][1]
        s2 += x1 * y2 - x2 * y1
    assert s2 > 0, "la huella debe quedar antihoraria (normal +Z)"


def test_ironpython_27_compatible():
    """Sin f-strings ni walrus (IronPython 2.7)."""
    with io.open(SRC, "rb") as f:
        fuente = f.read().decode("utf-8")
    assert "f'" not in fuente and 'f"' not in fuente
    assert ":=" not in fuente


def test_defensiva_template_resuelve_chip():
    """Path template CHIP-contexto50.json -> resuelve <CHIP>-contexto50.json hermano."""
    d = _fixture_dir(con_hermano=True)
    shutil.copy2(JSON_BASE_REAL, os.path.join(d, "AAA0240ZXJH-contexto.json"))
    ns = _ejecutar_componente(os.path.join(d, "CHIP-contexto50.json"))
    assert len(ns["volumenes"]) == 66
    assert "Volumenes 66/94" in ns["mensaje"]


def test_z_base_v01d_mueve_y_conserva_perimetro():
    """v01d: si el registro trae z_base_m, la huella/volumen parten de esa cota
    sin cambiar el perimetro (XY identicos); sin z_base_m quedan en Z=0."""
    d = _fixture_dir(con_hermano=False)
    with io.open(JSON_REAL, "rb") as f:
        data = json.loads(f.read().decode("utf-8"))
    data["edificios"] = data["edificios"][:12]
    tmp = os.path.join(d, "AAA0240ZXJH-contexto50.json")
    with io.open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)
    ns0 = _ejecutar_componente(tmp)
    for ed in data["edificios"]:
        ed["z_base_m"] = 12.5
    with io.open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)
    ns1 = _ejecutar_componente(tmp)
    assert len(ns1["volumenes"]) == len(ns0["volumenes"]) > 0
    h0 = ns0["huellas"][0].pts
    h1 = ns1["huellas"][0].pts
    assert [(p[0], p[1]) for p in h0] == [(p[0], p[1]) for p in h1]
    assert all(abs(p[2] - 0.0) < 1e-9 for p in h0)
    assert all(abs(p[2] - 12.5) < 1e-9 for p in h1)
    assert "z_base 12.5-12.5m" in ns1["mensaje"]
