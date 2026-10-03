"""
Fixtures compartidos para tests del proyecto DiseñoParametrico.

Uso:
    pytest tests/ -v
    pytest tests/ --cov=src --cov-report=term-missing
"""

import json
import os
import shutil
import sys
import tempfile
from pathlib import Path

# Agregar src y scripts al path
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "src"))
sys.path.insert(0, str(PROJECT_ROOT / "scripts" / "utilities"))

import pytest


# ============================================================
# AISLAMIENTO DEL ENTORNO (2026-10-02)
# ============================================================

@pytest.fixture(autouse=True, scope="session")
def _aislar_entorno_proyecto():
    """Apunta DISENO_PARAMETRICO_ROOT a un directorio temporal durante los tests.

    Motivo (incidente 2026-10-02): el test conductual ejecuta el componente
    PATIO v02, cuya funcion _exportar_diagnostico consume
    data/pot-cache/lados-export-flag.json y escribe data/pot-cache/<CHIP>-lados.json
    sobre el proyecto real. Con la raiz en un temporal vacio, el export no
    encuentra el flag y no escribe nada; el valor original se restaura al
    final de la sesion de tests.
    """
    anterior = os.environ.get("DISENO_PARAMETRICO_ROOT")
    raiz_tmp = tempfile.mkdtemp(prefix="dp_tests_root_")
    os.environ["DISENO_PARAMETRICO_ROOT"] = raiz_tmp
    try:
        yield
    finally:
        if anterior is None:
            os.environ.pop("DISENO_PARAMETRICO_ROOT", None)
        else:
            os.environ["DISENO_PARAMETRICO_ROOT"] = anterior
        shutil.rmtree(raiz_tmp, ignore_errors=True)


# ============================================================
# DATOS DE PRUEBA - LOTE AAA0127AZPA (El Prado)
# ============================================================

@pytest.fixture
def lote_aaa0127azpa_vertices():
    """Vértices del lote AAA0127AZPA (coordenadas locales)."""
    return [
        (88.0115, 79.1103),
        (87.3302, 75.0000),
        (84.1747, 75.5253),
        (75.0000, 77.0527),
        (76.3331, 85.0963),
        (78.2952, 96.9348),
        (79.1204, 101.9135),
        (91.4507, 99.8608),
        (89.6462, 88.9733),
    ]


@pytest.fixture
def lote_aaa0127azpa_clasificacion():
    """Clasificación de lados para AAA0127AZPA (adyacencia real)."""
    return [
        {"side_index": 0, "classification": "Lateral", "setback_m": 0.0},
        {"side_index": 1, "classification": "Lateral", "setback_m": 0.0},
        {"side_index": 2, "classification": "Lateral", "setback_m": 0.0},
        {"side_index": 3, "classification": "Posterior", "setback_m": 3.0},
        {"side_index": 4, "classification": "Posterior", "setback_m": 3.0},
        {"side_index": 5, "classification": "Frontal", "setback_m": 3.0},
        {"side_index": 6, "classification": "Frontal", "setback_m": 3.0},
        {"side_index": 7, "classification": "Frontal", "setback_m": 5.0},
        {"side_index": 8, "classification": "Frontal", "setback_m": 5.0},
    ]


@pytest.fixture
def pot_data_aaa0127azpa():
    """Datos POT para AAA0127AZPA (extraídos del JSON)."""
    return {
        "upz": "EL PRADO",
        "altura_maxima_m": 11.4,
        "rango_edificabilidad": "3",
        "tratamiento": "Consolidación",
    }


@pytest.fixture
def lote_aaa0127azpa_contexto_json():
    """Ruta al JSON de contexto completo, o dict si está disponible."""
    json_path = PROJECT_ROOT / "data" / "pot-cache" / "AAA0127AZPA-contexto.json"
    if json_path.exists():
        with open(json_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return None


# ============================================================
# LOTE RECTANGULAR SIMPLE (para tests geométricos)
# ============================================================

@pytest.fixture
def lote_rectangular():
    """Lote rectangular simple: 10m × 20m en el origen."""
    return [
        (0.0, 0.0),
        (20.0, 0.0),
        (20.0, 10.0),
        (0.0, 10.0),
    ]


@pytest.fixture
def lote_rectangular_clasificacion():
    """Clasificación: frente en lado largo (0-1), resto laterales."""
    return [
        {"side_index": 0, "classification": "Frontal", "setback_m": 3.0},
        {"side_index": 1, "classification": "Lateral", "setback_m": 0.0},
        {"side_index": 2, "classification": "Posterior", "setback_m": 3.0},
        {"side_index": 3, "classification": "Lateral", "setback_m": 0.0},
    ]


# ============================================================
# LOTE DE ESQUINA (para tests de patios)
# ============================================================

@pytest.fixture
def lote_esquina():
    """Lote en esquina: 15m × 12m."""
    return [
        (0.0, 0.0),
        (15.0, 0.0),
        (15.0, 12.0),
        (0.0, 12.0),
    ]


@pytest.fixture
def lote_esquina_clasificacion():
    """Dos frentes adyacentes (esquina), dos laterales."""
    return [
        {"side_index": 0, "classification": "Frontal", "setback_m": 5.0},
        {"side_index": 1, "classification": "Frontal", "setback_m": 3.0},
        {"side_index": 2, "classification": "Lateral", "setback_m": 0.0},
        {"side_index": 3, "classification": "Lateral", "setback_m": 0.0},
    ]


# ============================================================
# PARÁMETROS NORMATIVOS (Decreto 555/2021)
# ============================================================

@pytest.fixture
def rangos_edificabilidad():
    """Rangos de edificabilidad según Decreto 555/2021."""
    return {
        "1": 2,   # 1-2 pisos
        "2": 3,   # 2-3 pisos
        "3": 5,   # 3-5 pisos
        "4": 8,   # 5-8 pisos
        "5": 12,  # 8-12 pisos
    }


@pytest.fixture
def tratamientos_params():
    """Parámetros por tratamiento urbanístico."""
    return {
        "Consolidación": {"io_max": 0.70, "ic_max": 2.0, "continua_lateral": 0.0},
        "Desarrollo": {"io_max": 0.50, "ic_max": 3.0, "continua_lateral": 0.0},
        "Renovación Urbana": {"io_max": 0.60, "ic_max": 5.0, "continua_lateral": 0.0},
    }
