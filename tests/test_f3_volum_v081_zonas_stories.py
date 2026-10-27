# -*- coding: utf-8 -*-
"""F3_VOLUM v08.1: zonas BEP + cotas en mensaje + export de stories.

Ejecuta el componente REAL (CPython + stub Rhino/Grasshopper: tests/
stub_rhino_min.py) por el camino "Implantacion" (barras_implantadas_json),
sin abrir Rhino. Verifica:
  - las cotas de arranque reales en el mensaje ("cotas B1..B4"),
  - nomenclatura BEP de zonas: Number GF-Z1-COM-001 y Name descriptivo,
  - atributos JSON con number/name/nivel/zona/categoria/consecutivo,
  - plan de stories con snap + export por flag (cotas-arranque.json +
    niveles_deseados.json en casos/<chip>/; el flag vuelve a false),
  - paridad del plan con F3_StorySync_v02.plan_stories (mismo algoritmo).
"""
import io
import json
import os
import sys
import types

TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.abspath(os.path.join(TESTS_DIR, ".."))
F3 = os.path.join(BASE, "src", "fase-3-masa", "F3_VOLUM_GENERADOR_v08.py")
SS = os.path.join(BASE, "src", "interfases-archicad", "F3_StorySync_v02.py")

sys.path.insert(0, TESTS_DIR)


def _instalar_stubs():
    import stub_rhino_min as stub
    rg = sys.modules.get("Rhino.Geometry")
    if rg is None:
        rh = types.ModuleType("Rhino")
        rg = types.ModuleType("Rhino.Geometry")
        rh.Geometry = rg
        sys.modules["Rhino"] = rh
        sys.modules["Rhino.Geometry"] = rg
    for k in ("Point3d", "Vector3d", "Polyline", "PolylineCurve", "Brep",
              "AreaMassProperties", "Curve", "Line"):
        setattr(rg, k, getattr(stub, k))
    rg.Intersect = stub.Intersect
    rg.__stub_min__ = True
    gh = sys.modules.get("Grasshopper")
    if not getattr(gh, "__stub_gh__", False):
        gh = types.ModuleType("Grasshopper")
        gk = types.ModuleType("Grasshopper.Kernel")
        gd = types.ModuleType("Grasshopper.Kernel.Data")

        class GH_Path(object):
            def __init__(self, *ix):
                self.ix = tuple(int(x) for x in ix)

        class DataTree(object):
            def __init__(self):
                self.branches = {}

            @classmethod
            def __class_getitem__(cls, item):
                return cls

            def Add(self, valor, path):
                self.branches.setdefault(tuple(path.ix), []).append(valor)

        gh.DataTree = DataTree
        gh.__stub_gh__ = True
        gd.GH_Path = GH_Path
        gk.Data = gd
        gh.Kernel = gk
        sys.modules["Grasshopper"] = gh
        sys.modules["Grasshopper.Kernel"] = gk
        sys.modules["Grasshopper.Kernel.Data"] = gd


def _ejecutar(vars_gh, root=None):
    _instalar_stubs()
    src = io.open(F3, "r", encoding="utf-8").read()
    ns = {"__name__": "gh_volum_test", "__file__": F3}
    ns.update(vars_gh)
    prev = os.environ.get("DISENO_PARAMETRICO_ROOT")
    if root:
        os.environ["DISENO_PARAMETRICO_ROOT"] = root
    try:
        exec(compile(src, F3, "exec"), ns)
    finally:
        if root:
            if prev is None:
                os.environ.pop("DISENO_PARAMETRICO_ROOT", None)
            else:
                os.environ["DISENO_PARAMETRICO_ROOT"] = prev
    return ns


def _valores(tree):
    out = []
    for k in sorted(tree.branches.keys()):
        out.extend(tree.branches[k])
    return out


def _bloque(bi, cota, pisos=5, floor_h=3.05):
    x0 = 9.0 * (bi - 1)
    return {
        "id": "B%d-R1" % bi,
        "cota_arranque_m": cota,
        "pisos": pisos,
        "floor_h": floor_h,
        "huella_xy": [[x0, 0.0], [x0 + 6.0, 0.0], [x0 + 6.0, 7.0], [x0, 7.0], [x0, 0.0]],
    }


def _barras_fixture(cotas=(0.20, 3.35, 6.85, 10.15), pisos=5):
    bloques = [_bloque(i + 1, c, pisos=pisos) for i, c in enumerate(cotas)]
    return {
        "schema": "f3_barras_salida_v01",
        "chip": "AAA0030JKOE",
        "recomendada": "ALT-4B-305",
        "alternativas": [{"id": "ALT-4B-305", "bloques": bloques}],
        "mensaje": "fixture",
    }


def _layout_fixture():
    usos = ["Local comercial", "Local comercial", "Vivienda", "Vivienda", "Vivienda"]
    return {"niveles": [{"nivel": i + 1, "usos": [u]} for i, u in enumerate(usos)]}


def _vars(bloques=None, layout=None):
    return {
        "barras_implantadas_json": json.dumps(bloques or _barras_fixture()),
        "layout_usos_json": json.dumps(layout or _layout_fixture()),
    }


def test_mensaje_cotas_y_zonas_bep(tmp_path):
    ns = _ejecutar(_vars(), root=str(tmp_path))
    msg = ns["mensaje"]
    assert "cotas B1..B4: 0.20 / 3.35 / 6.85 / 10.15 m" in msg
    assert "stories: 8 niveles (GF-L07, snap ajuste max 0.80 m)" in msg
    assert "| niveles:" not in msg  # sin flag no exporta

    nums = _valores(ns["zonas_pisos"])
    names = _valores(ns["zonas_nombres"])
    assert len(nums) == 20 and len(names) == 20
    assert nums[0] == "GF-Z1-COM-001"
    assert nums[2] == "L02-Z1-VIV-001"
    assert nums[12] == "L02-Z3-VIV-001"
    assert nums[-1] == "L04-Z4-VIV-001"
    assert names[0] == "Local comercial \u00b7 Bloque 1 \u00b7 Piso 1"
    assert names[-1] == "Vivienda \u00b7 Bloque 4 \u00b7 Piso 5"

    atr = json.loads(_valores(ns["zonas_atributos"])[12])
    assert atr["number"] == "L02-Z3-VIV-001"
    assert atr["nivel"] == "L02" and atr["zona"] == "Z3"
    assert atr["categoria"] == "VIV" and atr["consecutivo"] == 1
    assert abs(atr["z_base_m"] - (6.85 + 2 * 3.05)) < 1e-9
    assert atr["bloque"] == "B3-R1" and atr["piso"] == 3

    casos = os.path.join(str(tmp_path), "src", "fase-3-masa", "casos", "AAA0030JKOE")
    assert not os.path.exists(os.path.join(casos, "niveles_deseados.json"))


def test_export_flag_escribe_stories_y_apaga_flag(tmp_path):
    root = str(tmp_path)
    flag_dir = os.path.join(root, "data", "fase-3-masa")
    os.makedirs(flag_dir)
    flag = os.path.join(flag_dir, "stories-export-flag.json")
    with io.open(flag, "w", encoding="utf-8") as f:
        f.write(u'{"exportar": true, "chip": "AAA0030JKOE"}')

    ns = _ejecutar(_vars(), root=root)
    assert "| niveles: casos/AAA0030JKOE/niveles_deseados.json" in ns["mensaje"]

    casos = os.path.join(root, "src", "fase-3-masa", "casos", "AAA0030JKOE")
    niv = json.loads(io.open(os.path.join(casos, "niveles_deseados.json"),
                             encoding="utf-8").read())
    assert niv["schema"] == "f3_niveles_deseados_v01"
    assert niv["chip"] == "AAA0030JKOE"
    assert [s["name"] for s in niv["stories"]] == \
        ["GF", "L01", "L02", "L03", "L04", "L05", "L06", "L07"]
    elev = [s["elevation"] for s in niv["stories"]]
    # ADR-024: `elevation` va en marco ArchiCAD (GF = 0); la cota de calculo va en zgf_m
    esperado = [0.0, 3.05, 6.1, 9.15, 12.2, 15.25, 18.3, 21.35]
    assert all(abs(a - b) < 1e-6 for a, b in zip(elev, esperado))
    assert abs(niv["zgf_m"] - 0.2) < 1e-9
    assert niv["base_z_m"] == 0.0
    assert all(abs(s["elevacion_modelo_m"] - (s["elevation"] + 0.2)) < 1e-6
               for s in niv["stories"])
    assert abs(niv["bloques"][1]["ajuste_m"] - (-0.10)) < 1e-9
    assert abs(niv["bloques"][3]["ajuste_m"] - (-0.80)) < 1e-9
    assert niv["bloques"][1]["offset_niveles"] == 1
    assert niv["bloques"][3]["offset_niveles"] == 3

    cot = json.loads(io.open(os.path.join(casos, "cotas-arranque.json"),
                             encoding="utf-8").read())
    assert cot["schema"] == "f3_cotas_arranque_v01"
    assert len(cot["bloques"]) == 4
    assert abs(cot["bloques"][0]["cota_arranque_m"] - 0.20) < 1e-9

    flag_data = json.loads(io.open(flag, "r", encoding="utf-8").read())
    assert flag_data["exportar"] is False


def test_helpers_bep_y_fallback(tmp_path):
    layout = {"niveles": [{"usos": []}] * 5}
    ns = _ejecutar(_vars(layout=layout), root=str(tmp_path))
    assert ns["_nivel_bep"](1) == "GF"
    assert ns["_nivel_bep"](2) == "L01"
    assert ns["_nivel_bep"](5) == "L04"
    assert ns["_categoria_bep"](["Vivienda"]) == "VIV"
    assert ns["_categoria_bep"](["Consultorios"]) == "CON"
    assert ns["_categoria_bep"](["Local comercial", "Consultorios"]) == "COM"
    assert ns["_categoria_bep"](["Sin uso catalogado"]) == "ZZ"
    nums = _valores(ns["zonas_pisos"])
    assert nums[0] == "GF-Z1-ZZ-001"
    names = _valores(ns["zonas_nombres"])
    assert names[0] == "Uso por definir \u00b7 Bloque 1 \u00b7 Piso 1"


def test_paridad_plan_con_storysync_v02(tmp_path):
    import importlib.util
    spec = importlib.util.spec_from_file_location("f3_storysync_v02", SS)
    ss = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ss)

    bloques = [
        {"id": b["id"], "cota_arranque_m": b["cota_arranque_m"], "pisos": b["pisos"]}
        for b in _barras_fixture()["alternativas"][0]["bloques"]
    ]
    plan_ss = ss.plan_stories(bloques, 3.05)
    ns = _ejecutar(_vars(), root=str(tmp_path))
    plan_cv = ns["_plan_stories"](bloques, 3.05)

    assert plan_cv["stories"] == plan_ss["stories"]
    assert plan_cv["bloques"] == plan_ss["bloques"]
    assert plan_cv["floor_h_m"] == plan_ss["floor_h_m"]
    assert plan_cv["base_z_m"] == plan_ss["base_z_m"]
