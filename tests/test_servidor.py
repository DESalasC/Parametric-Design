# -*- coding: utf-8 -*-
"""Guardian de regresion para src/orquestador/servidor.py (formulario v2)."""

import io
import json
import os
import shutil
import sys
import threading
from http.server import HTTPServer

SRC_DIR = os.path.join(os.path.dirname(__file__), "..", "src", "orquestador")
sys.path.insert(0, SRC_DIR)

import servidor as sv  # noqa: E402


def test_lotes():
    assert "AAA0127AZPA" in sv._lotes()


def test_contexto():
    c = sv._contexto("AAA0127AZPA")
    assert c is not None and c["chip"] == "AAA0127AZPA"
    assert c["conteos"]["vias"] >= 1
    assert "desnivel_m" in c["topografia"]


def test_resultados():
    r = sv._resultados("A")
    assert r["caso"] == "A" and r["chip"] == "AAA0127AZPA"
    assert r["pisos"] == 6
    assert r["titulo"] and "El Prado" in r["titulo"]


def test_variables_sin_jerga_y_secciones():
    ids = {v["id"] for v in sv.VARIABLES}
    # variables de decision humana presentes
    for esperado in ("tipologia", "piso_adicional", "tipo_bonificacion",
                     "floor_height_user", "antejardin_decision",
                     "tratamiento", "caso", "alineacion_nucleo"):
        assert esperado in ids, "falta {}".format(esperado)
    # sin jerga interna (punto 4/5/8): sin "override", "F1", "F2", "F3", "modo"/"escenario" sueltos
    assert "uso_override" not in ids
    assert "modo" not in ids and "escenario" not in ids
    secciones = {v["seccion"] for v in sv.VARIABLES}
    assert "normativa" in secciones and "modelado" in secciones


def test_antejardin_voladizo_por_reglamentacion():
    v = {x["id"]: x for x in sv.VARIABLES}["antejardin_decision"]
    assert v["tipo"] == "select"
    assert "Según reglamentación" in v["opciones"]
    assert "Aumentar antejardín" in v["opciones"]
    assert "Disminuir voladizo" in v["opciones"]


def test_modos_y_escenarios():
    assert {m["id"] for m in sv.MODOS_FINANCIEROS} == {"venta", "renta"}
    assert {e["id"] for e in sv.ESCENARIOS_FINANCIEROS} == {"A_VIS", "B_ESTANDAR", "C_LUJO"}
    # cada uno con explicación (punto 5)
    assert all(m["descripcion"] for m in sv.MODOS_FINANCIEROS)
    assert all(e["descripcion"] for e in sv.ESCENARIOS_FINANCIEROS)


def test_usos_catalogo():
    u = sv._usos("AAA0127AZPA")
    cats = {x["categoria"] for x in u["catalogo"]}
    # Proximidad (AAPGSU): principal + restringido + prohibido (sin complementario)
    assert "principal" in cats and "restringido" in cats and "prohibido" in cats
    assert "complementario" not in cats
    principales = {x["nombre"] for x in u["catalogo"] if x["categoria"] == "principal"}
    assert any("Vivienda" in n for n in principales)
    prohibidos = {x["nombre"] for x in u["catalogo"] if x["categoria"] == "prohibido"}
    assert any("alto impacto" in n for n in prohibidos)


def test_financiero_con_fuentes():
    f = sv._financiero("AAA0127AZPA")
    assert f["disponible"] is True
    assert f["lote"]["costo_lote_total_cop"] is not None
    assert f["lote"].get("fuente")
    # 3 escenarios base + D_MIXTO (override de uso multiple, mejora menor)
    ids = {e["id"] for e in f["escenarios"]}
    assert {"A_VIS", "B_ESTANDAR", "C_LUJO"} <= ids
    assert "D_MIXTO" in ids


def test_guardar_provisional_y_crear_estructura():
    ruta, destino = sv._guardar_proyecto("", {"chip": "AAA0127AZPA"})
    assert "_provisional" in destino
    nombre = "TEST_Eliminar"
    try:
        ok, carpeta = sv._crear_estructura(nombre)
        assert ok
        assert os.path.isdir(os.path.join(carpeta, "Archicad"))
        assert os.path.isdir(os.path.join(carpeta, "Normativa"))
    finally:
        shutil.rmtree(os.path.join(sv.PROYECTOS, nombre), ignore_errors=True)


def test_guardar_proyecto_escribe_espejo_activo():
    contenido = {"chip": "AAA0127AZPA", "origen": "test_espejo"}
    ruta, destino = sv._guardar_proyecto("", contenido)
    try:
        assert os.path.isfile(sv.ACTIVO_PROYECTO)
        with io.open(sv.ACTIVO_PROYECTO, "r", encoding="utf-8") as f:
            espejo = json.load(f)
        assert espejo.get("origen") == "test_espejo"
    finally:
        if os.path.isfile(sv.ACTIVO_PROYECTO):
            os.remove(sv.ACTIVO_PROYECTO)


def test_http_smoke():
    srv = HTTPServer(("127.0.0.1", 0), sv.Handler)
    t = threading.Thread(target=srv.serve_forever, daemon=True)
    t.start()
    puerto = srv.server_address[1]
    try:
        import urllib.request as u
        base = "http://127.0.0.1:{}".format(puerto)

        r = u.urlopen(base + "/api/lotes", timeout=5)
        assert json.loads(r.read().decode("utf-8"))["ok"] is True

        r = u.urlopen(base + "/api/contexto?chip=AAA0127AZPA", timeout=5)
        assert json.loads(r.read().decode("utf-8"))["contexto"]["chip"] == "AAA0127AZPA"

        r = u.urlopen(base + "/api/usos?chip=AAA0127AZPA", timeout=5)
        assert json.loads(r.read().decode("utf-8"))["ok"] is True

        r = u.urlopen(base + "/api/financiero?chip=AAA0127AZPA", timeout=5)
        assert json.loads(r.read().decode("utf-8"))["financiero"]["disponible"] is True

        r = u.urlopen(base + "/api/resultados?caso=A", timeout=5)
        assert json.loads(r.read().decode("utf-8"))["resultados"]["caso"] == "A"

        import urllib.request as u2
        body = json.dumps({"nombre": "", "chip": "AAA0127AZPA",
                           "variables": {"tipologia": "Aislada"},
                           "usos": ["Vivienda"], "modos": ["venta"],
                           "escenarios": ["C_LUJO"]}).encode("utf-8")
        req = u2.Request(base + "/api/proyecto", data=body, method="POST",
                         headers={"Content-Type": "application/json"})
        resp = json.loads(u2.urlopen(req, timeout=5).read().decode("utf-8"))
        assert resp["ok"] is True and "_provisional" in resp["destino"]
    finally:
        srv.shutdown()
        srv.server_close()


def test_usos_area_actividad_fuente():
    u = sv._usos("AAA0127AZPA")
    cats = {x["categoria"] for x in u["catalogo"]}
    assert cats == {"principal", "restringido", "prohibido"}
    assert u["fuente"] == "area_actividad"
    assert u["categoria_area_actividad"] == "Proximidad"
    assert u["sector_clave"] == "EL PRADO"
    assert u["pendiente_usos_sector"] is False  # resuelto por area de actividad
    assert all("fuente" in x for x in u["catalogo"])


def test_usos_area_actividad_geobase():
    """areas-actividad.json (capa AreaActividad POT 555) integrado al endpoint."""
    assert sv._area_actividad("AAA0127AZPA")["codigo"] == "AAPGSU"
    assert sv._area_actividad("AAA0030JKOE")["codigo"] == "PEMP"
    assert sv._area_actividad("AAA0039KRMR")["codigo"] == "AAERVIS"
    assert sv._area_actividad("ZZZ00000000") is None
    u = sv._usos("AAA0127AZPA")
    assert u["area_actividad"]["codigo"] == "AAPGSU"
    assert u["area_actividad"]["nombre"]
    assert u["pendiente_cuadro_uso"] is True
    assert u["categoria_area_actividad"] == "Proximidad"


def test_usos_sector_geobase():
    """sectores-uso-lotes.json (cruce espacial Decreto 555) integrado al endpoint."""
    u = sv._usos("AAA0127AZPA")
    s = u["sector_uso_geobase"]
    assert s is not None
    upl = s["unidad_planeamiento_local"]
    assert upl["CODIGO_UPL"] == "UPL27"
    assert upl["NOMBRE"] == "Niza"


def test_catalogo_usos_cuatro_categorias():
    cats = {"principal": ["Vivienda", "Comercio"], "complementario": ["Salud"],
            "restringido": ["Industria BIA"], "prohibido": ["Industria AIA"]}
    catalogo = sv._catalogo_usos(cats, "area_actividad")
    assert {x["categoria"] for x in catalogo} == {"principal", "complementario", "restringido", "prohibido"}
    principales = {x["nombre"] for x in catalogo if x["categoria"] == "principal"}
    assert principales == {"Vivienda", "Comercio"}
    assert all(x["fuente"] == "area_actividad" for x in catalogo)


def test_usos_area_actividad_estructurante_y_pemp():
    # AAERVIS -> Estructurante (todo complementario, sin principal)
    u = sv._usos("AAA0039KRMR")
    assert u["categoria_area_actividad"] == "Estructurante"
    assert u["fuente"] == "area_actividad"
    cats = {x["categoria"] for x in u["catalogo"]}
    assert "complementario" in cats and "principal" not in cats
    # PEMP (BIC) -> sin categoria en el cuadro AA -> fallback base
    p = sv._usos("AAA0030JKOE")
    assert p["categoria_area_actividad"] is None
    assert p["fuente"] == "base"
    assert p["area_actividad"]["codigo"] == "PEMP"


def test_aporte_lote_variable():
    """Aporte del lote (vinculacion al negocio) expuesto como variable de decision."""
    v = {x["id"]: x for x in sv.VARIABLES}["aporte_lote"]
    assert v["tipo"] == "select"
    assert v["seccion"] == "aporte"
    assert {o["v"] for o in v["opciones"]} == {"venta_completa", "participacion", "aporte_completo"}
    # pago_parcial_pct acompaña como variable numerica (solo aplica en participacion)
    p = {x["id"]: x for x in sv.VARIABLES}["pago_parcial_pct"]
    assert p["tipo"] == "number" and p["seccion"] == "aporte"


def test_modalidad_dueno_lote():
    """Fuente fija: modalidad_dueno_lote -> {tipo, pago_parcial_pct}."""
    assert sv._modalidad_dueno_lote("venta_completa") == {"tipo": "venta_completa", "pago_parcial_pct": 100.0}
    assert sv._modalidad_dueno_lote("aporte_completo") == {"tipo": "aporte_completo", "pago_parcial_pct": 0.0}
    assert sv._modalidad_dueno_lote("participacion", None) == {"tipo": "participacion", "pago_parcial_pct": 30.0}
    assert sv._modalidad_dueno_lote("participacion", 50) == {"tipo": "participacion", "pago_parcial_pct": 50.0}
    assert sv._modalidad_dueno_lote("participacion", 150) == {"tipo": "participacion", "pago_parcial_pct": 100.0}
    assert sv._modalidad_dueno_lote("participacion", -5) == {"tipo": "participacion", "pago_parcial_pct": 0.0}


def test_modalidad_desde_data():
    """Backward-compat: acepta bloque nuevo modalidad_dueno_lote o campos legacy."""
    assert sv._modalidad_desde_data({"modalidad_dueno_lote": {"tipo": "aporte_completo", "pago_parcial_pct": 0}}) == \
        {"tipo": "aporte_completo", "pago_parcial_pct": 0.0}
    assert sv._modalidad_desde_data({"aporte_lote": "venta_completa"}) == \
        {"tipo": "venta_completa", "pago_parcial_pct": 100.0}
    assert sv._modalidad_desde_data({}) == {"tipo": "participacion", "pago_parcial_pct": 30.0}
