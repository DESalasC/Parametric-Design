# -*- coding: utf-8 -*-
"""Tests offline del LECTOR CANONICO de JSON (F1_ETAPA1_CONTEXTO_v04.3).

Ejecuta el componente con stubs de Rhino/System y verifica la cascada de
codificacion: utf-8 estricto -> cp1252 -> latin-1, con avisos ruidosos y
error explicito (hex de cabecera) cuando todo falla. Incluye el caso real
observado 2026-09-29: byte 0xF3 ('o' acentuada en cp1252) que reventaba un
decode estricto de UTF-8 en IronPython.
"""

import io
import json
import os
import sys
import types
import contextlib

BASE = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
SRC = os.path.join(BASE, "src", "fase-1-contexto", "F1_ETAPA1_CONTEXTO_v04.3.py")


class _Utf8EncodingCtor(object):
    def __init__(self, *a):
        pass

    def GetString(self, b):
        return b.decode("utf-8")  # estricto: falla ante bytes cp1252


class _Enc(object):
    def __init__(self, name):
        self.name = name

    def GetString(self, b):
        return b.decode(self.name)


def _build_system():
    m = types.ModuleType("System")
    io_m = types.ModuleType("System.IO")
    tx = types.ModuleType("System.Text")
    io_m.File = types.SimpleNamespace(
        ReadAllBytes=lambda p: open(p, "rb").read(),
        Exists=lambda p: os.path.exists(p))
    tx.UTF8Encoding = _Utf8EncodingCtor

    def _get_enc(cp):
        cp = int(cp)
        if cp == 1252:
            return _Enc("cp1252")
        if cp == 28591:
            return _Enc("latin-1")
        return _Enc("latin-1")

    tx.Encoding = types.SimpleNamespace(GetEncoding=_get_enc)
    m.IO = io_m
    m.Text = tx
    return m


def _cargar():
    rg = types.ModuleType("Rhino.Geometry")
    rg.Mesh = object  # no se usa en estos tests
    rh = types.ModuleType("Rhino")
    rh.Geometry = rg
    sys.modules["Rhino"] = rh
    sys.modules["Rhino.Geometry"] = rg
    m = _build_system()
    sys.modules["System"] = m
    sys.modules["System.IO"] = m.IO
    sys.modules["System.Text"] = m.Text
    with io.open(SRC, "rb") as f:
        fuente = f.read().decode("utf-8")
    ns = {"json_path": None}
    exec(compile(fuente, SRC, "exec"), ns)
    return ns


def _escribir(tmp_path, nombre, texto, encoding):
    p = os.path.join(str(tmp_path), nombre)
    with open(p, "wb") as f:
        f.write(texto.encode(encoding))
    return p


def test_componente_existe():
    assert os.path.isfile(SRC)


def test_utf8_normal_sin_aviso(tmp_path):
    ns = _cargar()
    p = _escribir(tmp_path, "ok.json", u'{"tratamiento": "Consolidación", "n": 1}', "utf-8")
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        data = ns["leer_json_seguro"](p)
    assert data["tratamiento"] == u"Consolidación"
    assert data["n"] == 1
    assert "AVISO ENCODING" not in buf.getvalue()


def test_cp1252_se_lee_con_aviso(tmp_path):
    ns = _cargar()
    p = _escribir(tmp_path, "cp1252.json", u'{"tratamiento": "Consolidación"}', "cp1252")
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        data = ns["leer_json_seguro"](p)
    assert data["tratamiento"] == u"Consolidación"
    salida = buf.getvalue()
    assert "[AVISO ENCODING]" in salida
    assert "cp1252" in salida


def test_bom_utf8_sin_aviso(tmp_path):
    ns = _cargar()
    p = _escribir(tmp_path, "bom.json", u'{"tratamiento": "Consolidación"}', "utf-8-sig")
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        data = ns["leer_json_seguro"](p)
    assert data["tratamiento"] == u"Consolidación"
    assert "AVISO ENCODING" not in buf.getvalue()


def test_basura_error_con_hex(tmp_path):
    ns = _cargar()
    p = os.path.join(str(tmp_path), "basura.bin")
    with open(p, "wb") as f:
        f.write(b"\x81\x8d\x00\xff")
    try:
        ns["leer_json_seguro"](p)
        assert False, "debia lanzar excepcion"
    except Exception as e:
        msg = str(e)
        assert "Primeros bytes" in msg
        assert "81" in msg and "8D" in msg


def test_archivo_inexistente(tmp_path):
    ns = _cargar()
    try:
        ns["leer_json_seguro"](os.path.join(str(tmp_path), "no_existe.json"))
        assert False, "debia lanzar excepcion"
    except Exception as e:
        assert "no existe" in str(e)
