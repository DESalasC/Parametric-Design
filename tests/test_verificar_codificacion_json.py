# -*- coding: utf-8 -*-
"""
Tests de scripts/utilities/verificar-codificacion-json.py

El nombre del script tiene guiones, por lo que se carga vía
importlib.util.spec_from_file_location.

Cubre:
- Clasificación: OK, WARN(bom), WARN(cp1252), WARN(latin-1), FAIL.
- --aplicar: reescritura como UTF-8 sin BOM, backup creado, contenido
  lógicamente idéntico (parseado) y sin --aplicar no se toca ningún archivo.
- --ascii: solo transforma los archivos que se están reparando.
"""

import codecs
import importlib.util
import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
UTIL_PATH = PROJECT_ROOT / "scripts" / "utilities" / "verificar-codificacion-json.py"


def _cargar_modulo():
    """Carga la utilidad (nombre con guiones) como módulo importable."""
    spec = importlib.util.spec_from_file_location("verificar_codificacion_json", str(UTIL_PATH))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


mod = _cargar_modulo()


def _contenido():
    """Contenido JSON de prueba con caracteres no ASCII (tildes)."""
    return {
        "chip": "AAA0240ZXJH",
        "ciudad": "Bogotá D.C.",
        "nota": "café con ñandú — ó",
        "valores": [1, 2.5, None, True],
    }


def _bytes_utf8(contenido):
    return json.dumps(contenido, ensure_ascii=False, indent=2).encode("utf-8")


def _bytes_cp1252(contenido):
    return json.dumps(contenido, ensure_ascii=False, indent=2).encode("cp1252")


class TestClasificacion:
    """Clasificación de un archivo según su codificación y validez JSON."""

    def test_utf8_valido_ok(self, tmp_path):
        ruta = tmp_path / "ok.json"
        ruta.write_bytes(_bytes_utf8(_contenido()))
        res = mod.clasificar_archivo(ruta)
        assert res.estado == "OK"
        assert res.origen == "utf-8"

    def test_utf8_con_bom_warn(self, tmp_path):
        ruta = tmp_path / "bom.json"
        ruta.write_bytes(codecs.BOM_UTF8 + _bytes_utf8(_contenido()))
        res = mod.clasificar_archivo(ruta)
        assert res.estado == "WARN(bom)"
        assert res.origen == "bom"

    def test_cp1252_warn(self, tmp_path):
        ruta = tmp_path / "cp1252.json"
        raw = _bytes_cp1252(_contenido())
        assert b"\xf3" in raw  # 'ó' en cp1252 (caso real observado)
        ruta.write_bytes(raw)
        res = mod.clasificar_archivo(ruta)
        assert res.estado == "WARN(cp1252)"
        assert res.origen == "cp1252"

    def test_latin1_warn(self, tmp_path):
        # 0x90 no es válido ni en utf-8 ni en cp1252, pero sí en latin-1.
        ruta = tmp_path / "latin1.json"
        ruta.write_bytes(b'{"nota": "dato\x90x"}')
        res = mod.clasificar_archivo(ruta)
        assert res.estado == "WARN(latin-1)"
        assert res.origen == "latin-1"

    def test_bytes_basura_fail(self, tmp_path):
        ruta = tmp_path / "basura.json"
        ruta.write_bytes(b"\xff\xfe\x93 basura que no es JSON \xf3\x00\x01")
        res = mod.clasificar_archivo(ruta)
        assert res.estado == "FAIL"


class TestAplicar:
    """Reparación y modo de solo verificación."""

    def test_aplicar_repara_cp1252(self, tmp_path):
        contenido = _contenido()
        ruta = tmp_path / "lote.json"
        original = _bytes_cp1252(contenido)
        ruta.write_bytes(original)
        reporte = tmp_path / "reporte.txt"

        codigo = mod.main(["--aplicar", "--roots", str(tmp_path), "--reporte", str(reporte)])
        assert codigo == 0

        raw = ruta.read_bytes()
        assert not raw.startswith(codecs.BOM_UTF8)
        texto = raw.decode("utf-8")  # estricto: no debe lanzar
        assert json.loads(texto) == contenido

        backups = sorted(tmp_path.glob("lote.json.bak-encoding-*"))
        assert len(backups) == 1
        assert backups[0].read_bytes() == original

        assert reporte.exists()
        assert "WARN(cp1252)" in reporte.read_text(encoding="utf-8")

    def test_sin_aplicar_no_modifica(self, tmp_path):
        ruta = tmp_path / "solo-lectura.json"
        original = _bytes_cp1252(_contenido())
        ruta.write_bytes(original)
        reporte = tmp_path / "reporte.txt"

        codigo = mod.main(["--roots", str(tmp_path), "--reporte", str(reporte)])
        assert codigo == 1

        assert ruta.read_bytes() == original
        assert not list(tmp_path.glob("*.bak-encoding-*"))

    def test_ascii_solo_en_reparados(self, tmp_path):
        ok = tmp_path / "ok.json"
        ok_bytes = _bytes_utf8(_contenido())
        ok.write_bytes(ok_bytes)  # utf-8 limpio con 'ó': NO debe tocarse
        malo = tmp_path / "malo.json"
        malo.write_bytes(_bytes_cp1252(_contenido()))
        reporte = tmp_path / "reporte.txt"

        codigo = mod.main(
            ["--aplicar", "--ascii", "--roots", str(tmp_path), "--reporte", str(reporte)]
        )
        assert codigo == 0

        assert ok.read_bytes() == ok_bytes  # intacto
        reparado = malo.read_bytes()
        reparado.decode("ascii")  # ASCII-safe: no debe lanzar
        assert json.loads(reparado.decode("ascii")) == _contenido()
