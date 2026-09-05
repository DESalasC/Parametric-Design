# -*- coding: utf-8 -*-
"""
================================================================================
servidor.py — Formulario de solicitud interactivo (DiseñoParametrico)
Parte 1: F1 -> F3. Servidor local con stdlib (sin dependencias nuevas).
================================================================================

El operador NO ve comandos: abre el navegador, llena un formulario y ve los
resultados. Secciones claramente separadas: Predio, Normativa/GFA, Financiero,
Modelado.

Endpoints:
  GET  /                  -> formulario (index.html)
  GET  /api/lotes         -> CHIPs disponibles
  GET  /api/contexto?chip -> info del predio (lote, topografia/desnivel, POT)
  GET  /api/variables     -> esquema de variables de decision (por seccion)
  GET  /api/usos?chip     -> catalogo de usos (principal/complementario/prohibido)
  GET  /api/vecinos-por-lado?chip -> vecinos colindantes por lado (nomenclatura cardinal)
  GET  /api/financiero?chip -> variables financieras + fuentes (base de decision)
  GET  /api/resultados?caso -> resultados existentes (programa-areas + accesos)
  GET  /api/proyectos     -> proyectos guardados
  POST /api/proyecto      -> guarda (nombre opcional -> _provisional) o crea estructura

USO:
  .\\.venv\\Scripts\\python.exe src\\orquestador\\servidor.py [--puerto 8900]
  Abrir http://127.0.0.1:8900
================================================================================
"""

import argparse
import datetime
import io
import json
import os
import shutil
import subprocess
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
ORQ_DIR = os.path.dirname(os.path.abspath(__file__))
POT_CACHE = os.path.join(ROOT, "data", "pot-cache")
F3_CASOS = os.path.join(ROOT, "src", "fase-3-masa", "casos")
F2_VENTA_DIR = os.path.join(ROOT, "src", "fase-2-demanda", "F2_Modelo_Financiero")
F2_RENTA_DIR = os.path.join(ROOT, "src", "fase-2-demanda", "F2_Modelo_Renta")
F3_DIR = os.path.join(ROOT, "src", "fase-3-masa")
F2_VENTA_SCRIPT = os.path.join(F2_VENTA_DIR, "F2_DEMANDA_MOTOR_v03.py")
F3_DIST_SCRIPT = os.path.join(F3_DIR, "F3_DISTRIBUCION_v01.py")
F3_ACCESOS_SCRIPT = os.path.join(F3_DIR, "F3_ACCESOS_INTEGRADOR_v02.py")
F1_FETCH_SCRIPT = os.path.join(ROOT, "scripts", "utilities", "fetch-urban-context-v6.py")
PROYECTOS = os.path.join(ORQ_DIR, "proyectos")
PROVISIONAL = os.path.join(PROYECTOS, "_provisional")
NORMA_OVERRIDE_RUTA = os.path.join(ROOT, "data", "pot-bogota", "norma-override.json")
FINANCIERO_OVERRIDE_RUTA = os.path.join(ROOT, "data", "pot-bogota", "financiero-override.json")
SETBACK_OVERRIDE_RUTA = os.path.join(ROOT, "data", "pot-bogota", "setback-override.json")

# Archivos ACTIVOS (nombre literal "CHIP"): el canvas SIEMPRE lee/escribe estos,
# sin editar el panel. El orquestador los sobreescribe al seleccionar el predio.
ACTIVO_CONTEXTO = os.path.join(POT_CACHE, "CHIP-contexto.json")
ACTIVO_VECINOS = os.path.join(POT_CACHE, "CHIP-vecinos-por-lado.json")
ACTIVO_CASOS_DIR = os.path.join(F3_CASOS, "CASO")
GFA_FLAG_RUTA = os.path.join(ROOT, "data", "fase-2-demanda", "gfa-export-flag.json")
ACTIVO_PROYECTO = os.path.join(ROOT, "data", "activo", "proyecto.json")


def _norma_override_leer():
    """Lee data/pot-bogota/norma-override.json completo (dict)."""
    return _json(NORMA_OVERRIDE_RUTA)


def _norma_override_chip(chip):
    """Devuelve el override de norma para un CHIP (dict) o None."""
    data = _norma_override_leer()
    lotes = data.get("lotes") if isinstance(data.get("lotes"), dict) else {}
    ov = lotes.get(chip)
    return ov if isinstance(ov, dict) else None


def _norma_override_guardar(chip, override):
    """Guarda (merge) el override de norma para un CHIP. Devuelve (ok, ruta)."""
    data = _norma_override_leer()
    data.setdefault("_schema", "norma_override_v01")
    if not isinstance(data.get("lotes"), dict):
        data["lotes"] = {}
    nuevo = {}
    prev = data["lotes"].get(chip)
    if isinstance(prev, dict):
        nuevo.update(prev)
    if isinstance(override, dict):
        for k, v in override.items():
            if v is None or v == "":
                nuevo.pop(k, None)
            else:
                nuevo[k] = v
    nuevo["ultima_edicion"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    data["lotes"][chip] = nuevo
    try:
        os.makedirs(os.path.dirname(NORMA_OVERRIDE_RUTA), exist_ok=True)
        with io.open(NORMA_OVERRIDE_RUTA, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return True, NORMA_OVERRIDE_RUTA
    except Exception as e:
        return False, str(e)


def _area_shoelace_local(vertices):
    """Area (m2) desde vertices_3d_local [x,y,z] (formula del zapato).
    Devuelve None si no hay vertices suficientes."""
    pts = []
    for p in (vertices or []):
        if isinstance(p, (list, tuple)) and len(p) >= 2:
            pts.append([float(p[0]), float(p[1])])
    if len(pts) < 3:
        return None
    if pts[0] == pts[-1]:
        pts = pts[:-1]
    if len(pts) < 3:
        return None
    s = 0.0
    m = len(pts)
    for i in range(m):
        x1, y1 = pts[i][0], pts[i][1]
        x2, y2 = pts[(i + 1) % m][0], pts[(i + 1) % m][1]
        s += x1 * y2 - x2 * y1
    return round(abs(s) / 2.0, 2)


def _perimetro_local(vertices):
    """Perimetro (m) desde vertices_3d_local [x,y,z]. Devuelve None si no hay vertices."""
    pts = []
    for p in (vertices or []):
        if isinstance(p, (list, tuple)) and len(p) >= 2:
            pts.append([float(p[0]), float(p[1])])
    if len(pts) < 2:
        return None
    m = len(pts)
    total = 0.0
    for i in range(m):
        x1, y1 = pts[i][0], pts[i][1]
        x2, y2 = pts[(i + 1) % m][0], pts[(i + 1) % m][1]
        total += ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return round(total, 2)


def _financiero_override_leer():
    return _json(FINANCIERO_OVERRIDE_RUTA)


def _financiero_override_chip(chip):
    data = _financiero_override_leer()
    lotes = data.get("lotes") if isinstance(data.get("lotes"), dict) else {}
    ov = lotes.get(chip)
    return ov if isinstance(ov, dict) else None


def _financiero_override_guardar(chip, override):
    """Guarda (merge) el override financiero de un CHIP y proyecta un
    parametros_<CHIP>_mercado2026.json para que F2 lo use. Devuelve (ok, detalle)."""
    data = _financiero_override_leer()
    data.setdefault("_schema", "financiero_override_v01")
    if not isinstance(data.get("lotes"), dict):
        data["lotes"] = {}
    nuevo = {}
    prev = data["lotes"].get(chip)
    if isinstance(prev, dict):
        nuevo.update(prev)
    if isinstance(override, dict):
        for k, v in override.items():
            if v is None or v == "":
                nuevo.pop(k, None)
            else:
                nuevo[k] = v
    nuevo["ultima_edicion"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    data["lotes"][chip] = nuevo
    try:
        os.makedirs(os.path.dirname(FINANCIERO_OVERRIDE_RUTA), exist_ok=True)
        with io.open(FINANCIERO_OVERRIDE_RUTA, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    except Exception as e:
        return False, str(e)

    # Proyectar a un parametros_<CHIP>_mercado2026.json (entrada real de F2)
    try:
        base_ruta = os.path.join(F2_VENTA_DIR, "parametros_entrada.json")
        base = _json(base_ruta)
        if base:
            chip_ctx = _contexto(chip)
            area_real = None
            if chip_ctx:
                area_real = chip_ctx["lote"]["area_m2"]
            area_final = nuevo.get("area_m2")
            if area_final is None or area_final == "":
                area_final = area_real if area_real is not None else base.get("lote", {}).get("area_m2")
            base.setdefault("lote", {})["area_m2"] = area_final
            for k in ("precio_suelo_m2", "impuestos_escritura_pct", "costo_lote_total_cop", "fuente"):
                if nuevo.get(k) not in (None, ""):
                    base["lote"][k] = nuevo[k]
            for k in ("costos_blandos_pct", "marketing_ventas_pct"):
                if nuevo.get(k) not in (None, ""):
                    base.setdefault("financiero", {})[k] = nuevo[k]
            esc_ov = nuevo.get("escenarios")
            if isinstance(esc_ov, dict):
                base.setdefault("escenarios", {})
                for eid, ev in esc_ov.items():
                    if not isinstance(ev, dict):
                        continue
                    base["escenarios"].setdefault(eid, {})
                    for k in ("precio_venta_m2", "costo_construccion_m2"):
                        if ev.get(k) not in (None, ""):
                            base["escenarios"][eid][k] = ev[k]
            base.setdefault("meta", {})["chip"] = chip
            out_ruta = os.path.join(F2_VENTA_DIR, "parametros_{}_mercado2026.json".format(chip))
            with io.open(out_ruta, "w", encoding="utf-8") as f:
                json.dump(base, f, indent=2, ensure_ascii=False)
            return True, FINANCIERO_OVERRIDE_RUTA
    except Exception as e:
        return False, str(e)
    return True, FINANCIERO_OVERRIDE_RUTA


def _setback_override_leer():
    """Lee data/pot-bogota/setback-override.json completo (dict)."""
    return _json(SETBACK_OVERRIDE_RUTA)


def _setback_override_chip(chip):
    """Devuelve el override de setback para un CHIP (lista) o None."""
    data = _setback_override_leer()
    lotes = data.get("lotes") if isinstance(data.get("lotes"), dict) else {}
    ov = lotes.get(chip)
    return ov if isinstance(ov, list) else None


def _setback_override_guardar(chip, override):
    """Guarda (merge) el override de setback por lado para un CHIP.
    El override es un dict con formato: {"AAA0240ZXJH": [{"side_id": 0, "has_setback": true}, ...]}.
    Devuelve (ok, ruta)."""
    data = _setback_override_leer()
    data.setdefault("_schema", "setback_override_v01")
    if not isinstance(data.get("lotes"), dict):
        data["lotes"] = {}
    nuevo = {}
    prev = data["lotes"].get(chip)
    if isinstance(prev, dict):
        # Convertir lista de overrides existentes a dict por side_id para facilitar merge
        prev_dict = {item.get("side_id"): item for item in prev if isinstance(item, dict) and "side_id" in item}
    else:
        prev_dict = {}

    if isinstance(override, dict) and chip in override:
        override_list = override[chip]
        if isinstance(override_list, list):
            for item in override_list:
                if isinstance(item, dict) and "side_id" in item and "has_setback" in item:
                    side_id = int(item["side_id"])
                    has_setback = bool(item["has_setback"])
                    nuevo[side_id] = {"side_id": side_id, "has_setback": has_setback}
                # Ignore items malformados
            # Merge con prev: los nuevos valores sobrescriben los antiguos
            for side_id, item in prev_dict.items():
                if side_id not in nuevo:
                    nuevo[side_id] = item
            # Convertir de nuevo a lista
            final_list = [nuevo[sid] for sid in sorted(nuevo.keys())]
            data["lotes"][chip] = final_list
        else:
            # Si no es una lista válida, mantener lo existente
            if isinstance(prev, list):
                data["lotes"][chip] = prev
            else:
                data["lotes"][chip] = []
    else:
        # No se proporcionó override para este chip, mantener lo existente
        if isinstance(prev, list):
            data["lotes"][chip] = prev
        else:
            data["lotes"][chip] = []

    # Actualizar timestamp
    if isinstance(data["lotes"].get(chip), list) and len(data["lotes"][chip]) > 0:
        # Añadir timestamp al primer elemento si no existe
        if not isinstance(data["lotes"][chip][0], dict) or "ultima_edicion" not in data["lotes"][chip][0]:
            if data["lotes"][chip]:
                data["lotes"][chip][0]["ultima_edicion"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    elif isinstance(data["lotes"].get(chip), list):
        # Lista vacía, crear elemento con timestamp
        data["lotes"][chip] = [{"ultima_edicion": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}]

    try:
        os.makedirs(os.path.dirname(SETBACK_OVERRIDE_RUTA), exist_ok=True)
        with io.open(SETBACK_OVERRIDE_RUTA, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return True, SETBACK_OVERRIDE_RUTA
    except Exception as e:
        return False, str(e)


def _vecinos_override_ruta(chip):
    return os.path.join(POT_CACHE, chip + "-vecinos-por-lado-override.json")


def _vecinos_por_lado_data(chip):
    """Vecinos por lado CON overrides del operador (si existen), si no el auto."""
    auto = _json(os.path.join(POT_CACHE, chip + "-vecinos-por-lado.json"))
    ov = _json(_vecinos_override_ruta(chip))
    if ov and ov.get("lados"):
        return ov
    return auto or None


def _activar_chip(chip):
    """Sobreescribe los archivos ACTIVOS (CHIP-*.json) con los datos del CHIP
    seleccionado para que el canvas no requiera edición. Devuelve dict con lo activado."""
    activados = {}
    ctx = os.path.join(POT_CACHE, chip + "-contexto.json")
    if os.path.exists(ctx):
        try:
            shutil.copy2(ctx, ACTIVO_CONTEXTO)
            activados["contexto"] = ACTIVO_CONTEXTO
        except Exception:
            pass
    vpl = _vecinos_por_lado_data(chip)
    if vpl:
        try:
            with io.open(ACTIVO_VECINOS, "w", encoding="utf-8") as f:
                json.dump(vpl, f, indent=2, ensure_ascii=False)
            activados["vecinos_por_lado"] = ACTIVO_VECINOS
        except Exception:
            pass
    # Espejo ACTIVO del proyecto (data/activo/proyecto.json): al cambiar de
    # chip se actualiza el campo 'chip' para que F0_LOAD_PROYECTO lea el
    # chip vigente. Fix 2026-09-01 (revision adversarial O2).
    try:
        datos = {}
        if os.path.isfile(ACTIVO_PROYECTO):
            with io.open(ACTIVO_PROYECTO, "r", encoding="utf-8") as f:
                datos = json.load(f)
        if not isinstance(datos, dict):
            datos = {}
        datos["chip"] = chip
        carpeta_activo = os.path.dirname(ACTIVO_PROYECTO)
        if not os.path.isdir(carpeta_activo):
            os.makedirs(carpeta_activo)
        with io.open(ACTIVO_PROYECTO, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=2, ensure_ascii=False)
        activados["proyecto"] = ACTIVO_PROYECTO
    except Exception:
        pass
    return activados


def _activar_caso(caso):
    """Sobreescribe los archivos ACTIVOS de F3 (casos/CASO/) con el caso seleccionado
    para que F3_VOLUM_GENERADOR_v08 lea un path fijo. Devuelve dict con lo activado."""
    activados = {}
    if not caso:
        return activados
    src = os.path.join(F3_CASOS, caso)
    if not os.path.isdir(src):
        return activados
    try:
        os.makedirs(ACTIVO_CASOS_DIR, exist_ok=True)
    except Exception:
        return activados
    for nombre in ("programa-areas.json", "accesos.json", "layout_espacial.json"):
        origen = os.path.join(src, nombre)
        if os.path.exists(origen):
            try:
                shutil.copy2(origen, os.path.join(ACTIVO_CASOS_DIR, nombre))
                activados[nombre] = os.path.join(ACTIVO_CASOS_DIR, nombre)
            except Exception:
                pass
    # Espejo ACTIVO del proyecto: al cambiar de caso se actualiza el campo
    # 'caso' para que F0_LOAD_PROYECTO lea el caso vigente. Fix 2026-09-01 (O2).
    try:
        datos = {}
        if os.path.isfile(ACTIVO_PROYECTO):
            with io.open(ACTIVO_PROYECTO, "r", encoding="utf-8") as f:
                datos = json.load(f)
        if not isinstance(datos, dict):
            datos = {}
        datos["caso"] = caso
        carpeta_activo = os.path.dirname(ACTIVO_PROYECTO)
        if not os.path.isdir(carpeta_activo):
            os.makedirs(carpeta_activo)
        with io.open(ACTIVO_PROYECTO, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=2, ensure_ascii=False)
        activados["proyecto"] = ACTIVO_PROYECTO
    except Exception:
        pass
    return activados


def _gfa_flag_poner(valor):
    """Pone el flag de exportación GFA (True dispara la exportación en el canvas,
    que al terminar lo devuelve a False)."""
    try:
        os.makedirs(os.path.dirname(GFA_FLAG_RUTA), exist_ok=True)
        with io.open(GFA_FLAG_RUTA, "w", encoding="utf-8") as f:
            json.dump({"exportar": bool(valor)}, f, ensure_ascii=False)
        return GFA_FLAG_RUTA
    except Exception:
        return None


CASO_CHIP = {"A": "AAA0127AZPA", "B": "AAA0030JKOE", "B_SALUD": "AAA0030JKOE", "C": "AAA0039KRMR"}
CASO_TITULO = {
    "A": "A — El Prado (Suba): local + vivienda",
    "B": "B — La Candelaria: local turístico + vivienda",
    "B_SALUD": "B_SALUD — La Candelaria: consultorios + vivienda",
    "C": "C — Muzú (Puente Aranda): local + vivienda VIS",
}

# Catálogo base de usos (NSR-10 A.2.5 + POT 555). La clasificación principal/
# complementario/prohibido depende del sector; aquí es un punto de partida
# que debe validarse con la reglamentación de la UPZ.
USOS_CATALOGO = [
    {"nombre": "Vivienda", "categoria": "principal", "descripcion": "Residencial (VIS, VIP, no VIS)."},
    {"nombre": "Comercio", "categoria": "principal", "descripcion": "Locales y retail de escala zonal/vecinal."},
    {"nombre": "Oficinas", "categoria": "complementario", "descripcion": "Uso empresarial/oficinas."},
    {"nombre": "Salud", "categoria": "complementario", "descripcion": "Consultorios y centros de salud."},
    {"nombre": "Servicios", "categoria": "complementario", "descripcion": "Servicios personales, técnicos y alimentarios."},
    {"nombre": "Educación", "categoria": "complementario", "descripcion": "Educación formal y no formal."},
    {"nombre": "Institucional", "categoria": "prohibido", "descripcion": "Institucional de escala metropolitana."},
    {"nombre": "Industrial", "categoria": "prohibido", "descripcion": "Industrial (no en sectores residenciales)."},
]

USOS_DESC = {u["nombre"]: u["descripcion"] for u in USOS_CATALOGO}
USOS_SECTOR_RUTA = os.path.join(ROOT, "data", "pot-bogota", "usos-por-sector.json")
AREAS_ACTIVIDAD_RUTA = os.path.join(ROOT, "data", "pot-bogota", "areas-actividad.json")
SECTORES_USO_RUTA = os.path.join(ROOT, "data", "pot-bogota", "sectores-uso-lotes.json")

# Variables de decisión por sección (sin jerga interna). Las de tipo "check" se
# renderizan como casillas múltiples; las de tipo select/number/bool como control.
VARIABLES = [
    # ---- Sección 1: Normativa y GFA
    {"id": "tipologia", "label": "Tipología de implantación", "tipo": "select",
     "opciones": ["Continua", "Aislada"], "default": "Continua", "seccion": "normativa",
     "ayuda": "Continua = sin aislamiento lateral; Aislada = aislamiento 3 m."},
    {"id": "piso_adicional", "label": "Habilitar piso adicional (servicios o VIS)", "tipo": "bool",
     "default": False, "seccion": "normativa",
     "ayuda": "Permite un piso extra por servicios o por uso VIS."},
    {"id": "tipo_bonificacion", "label": "Tipo de bonificación", "tipo": "select",
     "opciones": ["Ninguno", "Servicios", "VIS"], "default": "Ninguno", "seccion": "normativa",
     "ayuda": "Bonificación que habilita el piso adicional."},
    {"id": "floor_height_user", "label": "Altura de placa (m)", "tipo": "number",
     "default": 3.0, "seccion": "normativa", "ayuda": "Altura libre de entrepiso (primer piso suele 3.6)."},
    {"id": "antejardin_decision", "label": "Antejardín / voladizo", "tipo": "select",
     "opciones": ["Según reglamentación", "Aumentar antejardín", "Disminuir voladizo"],
     "default": "Según reglamentación", "seccion": "normativa",
     "ayuda": "Ambos los fija la reglamentación; aquí solo se indica si se ajusta al alza el antejardín o a la baja el voladizo."},
    {"id": "antejardin_m", "label": "Antejardín (m)", "tipo": "number",
     "default": 0.0, "seccion": "normativa",
     "ayuda": "Retiro frontal en metros (override de 'Aumentar antejardín'). 0 = deriva de reglamentación."},
    {"id": "voladizo_frontal_m", "label": "Voladizo frontal (m)", "tipo": "number",
     "default": 0.0, "seccion": "normativa",
     "ayuda": "Voladizo frontal en metros (override de 'Disminuir voladizo'). 0 = deriva del perfil vial."},
    {"id": "tratamiento", "label": "Tratamiento urbanístico", "tipo": "select",
     "opciones": ["Consolidación", "Renovación urbana", "Desarrollo", "Mejoramiento integral"],
     "default": "Consolidación", "seccion": "normativa",
     "ayuda": "Tratamiento POT del predio (condiciona ocupación y edificabilidad)."},
    # ---- Sección 3: Modelado
    {"id": "caso", "label": "Escenario de modelado", "tipo": "select",
     "opciones": ["A", "B", "B_SALUD", "C"], "default": "A", "seccion": "modelado",
     "ayuda": "Escenario de distribución de masa. Se modela únicamente sobre el CHIP seleccionado en la sección 1 (Predio)."},
    {"id": "alineacion_nucleo", "label": "Posición del núcleo de servicios", "tipo": "select",
     "opciones": [{"v": 0, "label": "Centro"}, {"v": 1, "label": "Contra medianera"}, {"v": 2, "label": "Lado opuesto"}],
     "default": 1, "seccion": "modelado",
     "ayuda": "El 'switch' de posición del núcleo (escaleras + ascensor + servicios)."},
    # ---- Sección 3: Financiero (aporte del lote)
    {"id": "aporte_lote", "label": "Aporte del lote (vinculación al negocio)", "tipo": "select",
     "opciones": [
         {"v": "venta_completa", "label": "Venta completa del lote"},
         {"v": "participacion", "label": "Participación por porcentajes"},
         {"v": "aporte_completo", "label": "Aporte completo (especie)"},
     ],
     "default": "participacion", "seccion": "aporte",
     "ayuda": "Cómo se vincula el lote al negocio (aplica al modo Venta): venta total (pago 100% efectivo), participación porcentual (parte efectivo + parte en especie) o aporte completo en especie. Alimenta pago_parcial_pct / fraccion_aporte del motor F2."},
    {"id": "pago_parcial_pct", "label": "Pago parcial en efectivo (%)", "tipo": "number",
     "default": 30.0, "seccion": "aporte",
     "ayuda": "Solo aplica en 'Participación por porcentajes': % del costo del lote pagado en efectivo al dueño (el resto en especie). Venta completa = 100%, aporte completo = 0%."},
]

MODOS_FINANCIEROS = [
    {"id": "venta", "label": "Venta", "descripcion": "El proyecto se vende (unidades VIS/estándar/lujo)."},
    {"id": "renta", "label": "Renta (Build-to-Rent)", "descripcion": "Se construye para arrendar (corto/largo plazo)."},
]

ESCENARIOS_FINANCIEROS = [
    {"id": "A_VIS", "label": "VIS / VIP", "descripcion": "Vivienda de interés social (acabado básico, precio tope VIS)."},
    {"id": "B_ESTANDAR", "label": "Estándar", "descripcion": "Segmento medio (acabado estándar)."},
    {"id": "C_LUJO", "label": "Lujo", "descripcion": "Segmento alto (acabado premium)."},
]

# Nombres canónicos de los archivos de intercambio (única fuente de verdad para el
# cableado del canvas). REGLA DEL CANVAS: los componentes GH leen/escriben SIEMPRE el
# archivo ACTIVO (nombre literal "CHIP"/"CASO"); el orquestador lo sobreescribe al
# seleccionar el predio y conserva el archivo por-CHIP como historial.
ARCHIVOS_INTERCAMBIO = [
    {"id": "contexto", "canvas": True,
     "activo": "data/pot-cache/CHIP-contexto.json",
     "archivo": "data/pot-cache/<CHIP>-contexto.json",
     "produce": "fetch-urban-context-v6.py (escribe <CHIP>-contexto.json) → orquestador copia al activo",
     "consume": "F1_ETAPA1_CONTEXTO_v02 (lee el activo)"},
    {"id": "vecinos_por_lado", "canvas": True,
     "activo": "data/pot-cache/CHIP-vecinos-por-lado.json",
     "archivo": "data/pot-cache/<CHIP>-vecinos-por-lado.json",
     "produce": "vecinos_por_lado.py (escribe <CHIP>-vecinos-por-lado.json) → orquestador copia al activo (con confirmaciones)",
     "consume": "F1_ETAPA2_NORMATIVA_v08 (lee el activo: vecinos_por_lado_json)"},
    {"id": "gfa_gh", "canvas": True,
     "activo": "data/fase-2-demanda/CHIP-gfa-gh.json",
     "archivo": "data/fase-2-demanda/<CHIP>-gfa-gh.json",
     "produce": "F1_EXPORTAR_GFA_v02 (disparado por gfa-export-flag.json; escribe activo + archivo)",
     "consume": "F2_DEMANDA_MOTOR_v03 / F2_RENTA_MOTOR_v03 (leen el archivo por CHIP)"},
    {"id": "gfa_flag", "canvas": False,
     "activo": None,
     "archivo": "data/fase-2-demanda/gfa-export-flag.json",
     "produce": "orquestador (POST /api/exportar-gfa)",
     "consume": "F1_EXPORTAR_GFA_v02 (dispara la exportación y la devuelve a false)"},
    {"id": "programa_areas", "canvas": True,
     "activo": "src/fase-3-masa/casos/CASO/programa-areas.json",
     "archivo": "src/fase-3-masa/casos/<CASO>/programa-areas.json",
     "produce": "F3_DISTRIBUCION_v01.py (escribe <CASO>) → orquestador copia al activo",
     "consume": "F3_VOLUM_GENERADOR_v08 (lee el activo: json_path)"},
    {"id": "accesos", "canvas": True,
     "activo": "src/fase-3-masa/casos/CASO/accesos.json",
     "archivo": "src/fase-3-masa/casos/<CASO>/accesos.json",
     "produce": "F3_ACCESOS_INTEGRADOR_v02.py (escribe <CASO>) → orquestador copia al activo",
     "consume": "orquestador (resultados)"},
    {"id": "vecinos_override", "canvas": False,
     "activo": None,
     "archivo": "data/pot-cache/<CHIP>-vecinos-por-lado-override.json",
     "produce": "orquestador (POST /api/vecinos-por-lado)",
     "consume": "orquestador (GET) — confirmaciones del operador"},
    {"id": "norma_override", "canvas": False,
     "activo": None,
     "archivo": "data/pot-bogota/norma-override.json",
     "produce": "orquestador (POST /api/norma-override)",
     "consume": "fetch-urban-context-v6.py (fusiona en pot_data, gana sobre la geobase)"},
    {"id": "financiero_override", "canvas": False,
     "activo": None,
     "archivo": "data/pot-bogota/financiero-override.json",
     "produce": "orquestador (POST /api/financiero)",
     "consume": "orquestador + generación de parametros_<CHIP>_mercado2026.json"},
    {"id": "setback_override", "canvas": False,
     "activo": None,
     "archivo": "data/pot-bogota/<CHIP>-setback-override.json",
     "produce": "orquestador (POST /api/setback-override)",
     "consume": "F1_ETAPA2_LADOS_v06 (lee lado_via_setback_override_json)"},
    {"id": "parametros_f2_venta", "canvas": False,
     "activo": None,
     "archivo": "src/fase-2-demanda/F2_Modelo_Financiero/parametros_<CHIP>_mercado2026.json",
     "produce": "orquestador (POST /api/financiero) o manual",
     "consume": "F2_DEMANDA_MOTOR_v03.py (--parametros)"},
    {"id": "resultados_f2", "canvas": False,
     "activo": None,
     "archivo": "src/fase-2-demanda/F2_Modelo_Financiero/resultados/resultados_<CHIP>.json",
     "produce": "F2_DEMANDA_MOTOR_v03.py",
     "consume": "orquestador + F3"},
]


def _modalidad_dueno_lote(aporte_lote=None, pago_parcial_pct=None):
    """Fuente fija: bloque canonico modalidad_dueno_lote {tipo, pago_parcial_pct}.
    Unico productor: el orquestador. tipo: venta_completa | participacion |
    aporte_completo. pago_parcial_pct: % del costo del lote en efectivo (0..100).
    venta_completa -> 100, aporte_completo -> 0, participacion -> % indicado."""
    tipo = aporte_lote if aporte_lote in ("venta_completa", "participacion",
                                            "aporte_completo") else "participacion"
    if tipo == "venta_completa":
        pago = 100.0
    elif tipo == "aporte_completo":
        pago = 0.0
    else:
        try:
            pago = float(pago_parcial_pct) if pago_parcial_pct not in (None, "") else 30.0
        except (TypeError, ValueError):
            pago = 30.0
    return {"tipo": tipo, "pago_parcial_pct": round(min(100.0, max(0.0, pago)), 1)}


def _persistir_modalidad_f2_entrada(chip, modalidad):
    """Proyecta modalidad_dueno_lote en data/activo/f2_entrada.json (entrada F2)."""
    ruta = os.path.join(ROOT, "data", "activo", "f2_entrada.json")
    d = _json(ruta)
    d.setdefault("operador", {})["modalidad_dueno_lote"] = {
        "tipo": modalidad.get("tipo", "participacion"),
        "pago_parcial_pct": modalidad.get("pago_parcial_pct", 30.0),
    }
    d["chip"] = chip
    try:
        with io.open(ruta, "w", encoding="utf-8") as f:
            json.dump(d, f, indent=2, ensure_ascii=False)
        return True
    except Exception:
        return False


def _modalidad_desde_data(data):
    """Construye modalidad_dueno_lote desde el payload (bloque nuevo o campos legacy)."""
    m = data.get("modalidad_dueno_lote")
    if isinstance(m, dict):
        return _modalidad_dueno_lote(m.get("tipo"), m.get("pago_parcial_pct"))
    return _modalidad_dueno_lote(data.get("aporte_lote"), data.get("pago_parcial_pct"))


def _ruta_parametros_f2_mercado(chip, dias_frescura=60):
    """Parametros de mercado sincronizados desde MercadoViviendaBogota.

    Busca en data/fase-2-demanda/mercado/ el archivo
    parametros_<chip>_f2mercado_*.json mas reciente (generado por el paso
    F2_SINCRONIZAR_MERCADO_v01.py). Solo lo acepta si su
    meta.mercado.fecha_captura_origen tiene <= dias_frescura dias; en caso
    contrario devuelve None y la cadena de prioridad sigue con los parametros
    curados del proyecto (fallback retrocompatible).
    """
    import glob
    import datetime
    dir_mercado = os.path.join(ROOT, "data", "fase-2-demanda", "mercado")
    candidatos = sorted(
        glob.glob(os.path.join(dir_mercado, "parametros_{}_f2mercado_*.json".format(chip))),
        reverse=True,
    )
    for ruta in candidatos:
        try:
            with open(ruta, "r", encoding="utf-8") as f:
                datos = json.load(f)
            fecha_captura = ((datos.get("meta") or {}).get("mercado") or {}).get("fecha_captura_origen")
            if not fecha_captura:
                continue
            origen = datetime.date.fromisoformat(str(fecha_captura)[:10])
            if (datetime.date.today() - origen).days <= dias_frescura:
                return ruta
        except Exception:
            continue
    return None


def _ruta_parametros_f2_venta(chip):
    cand_mercado = _ruta_parametros_f2_mercado(chip)
    if cand_mercado:
        return cand_mercado
    for cand in (os.path.join(F2_VENTA_DIR, "parametros_{}_mercado2026.json".format(chip)),
                 os.path.join(F2_VENTA_DIR, "parametros_{}_venta.json".format(chip)),
                 os.path.join(F2_VENTA_DIR, "parametros_{}.json".format(chip))):
        if os.path.exists(cand):
            return cand
    return os.path.join(F2_VENTA_DIR, "parametros_entrada.json")


def _calcular_f2(chip, modalidad, gfa_m2=None, costo_lote_cop=None):
    """Ejecuta F2 (venta) con la modalidad del dueno del lote (fuente fija)."""
    pago = modalidad.get("pago_parcial_pct", 30.0)
    _persistir_modalidad_f2_entrada(chip, modalidad)
    parametros = _ruta_parametros_f2_venta(chip)
    cmd = [sys.executable, F2_VENTA_SCRIPT, "--parametros", parametros, "--chip", chip,
           "--pago-parcial", str(pago)]
    if gfa_m2:
        cmd += ["--gfa", str(gfa_m2)]
    if costo_lote_cop:
        cmd += ["--costo-lote", str(costo_lote_cop)]
    try:
        proc = subprocess.run(cmd, cwd=F2_VENTA_DIR, capture_output=True, text=True,
                              encoding="utf-8", errors="replace", timeout=180)
        ok = proc.returncode == 0
        salida = ((proc.stdout or "") + (proc.stderr or "")).strip()
    except Exception as ex:
        ok, salida = False, "ERROR: " + str(ex)
    resumen = None
    ruta_res = os.path.join(F2_VENTA_DIR, "resultados", "resultados_completos.json")
    if ok and os.path.exists(ruta_res):
        d = _json(ruta_res)
        resumen = {
            "chip": (d.get("meta") or {}).get("chip", chip),
            "gfa_max_m2": d.get("gfa_max_m2"),
            "recomendado": (d.get("recomendacion") or {}).get("recomendado"),
            "veredicto": (d.get("recomendacion") or {}).get("veredicto_textual"),
        }
        # canonico resultados_<CHIP>.json para que F3 lo localice
        try:
            shutil.copy2(ruta_res, os.path.join(F2_VENTA_DIR, "resultados",
                                                "resultados_" + chip + ".json"))
        except Exception:
            pass
    return {
        "ok": ok,
        "modalidad_dueno_lote": modalidad,
        "fraccion_aporte_pct": round(100.0 - pago, 1),
        "resumen": resumen,
        "salida": salida[-1500:],
    }


def _generar_f3(chip, escenario="D_MIXTO"):
    """Ejecuta F3 (distribución + accesos) para un CHIP y devuelve el resumen."""
    cmd = [sys.executable, F3_DIST_SCRIPT, "--chip", chip, "--escenario", escenario]
    try:
        proc = subprocess.run(cmd, cwd=F3_DIR, capture_output=True, text=True,
                              encoding="utf-8", errors="replace", timeout=180)
        ok = proc.returncode == 0
        salida = ((proc.stdout or "") + (proc.stderr or "")).strip()
    except Exception as ex:
        ok, salida = False, "ERROR: " + str(ex)
    if ok:
        try:
            subprocess.run([sys.executable, F3_ACCESOS_SCRIPT, "--caso", chip],
                           cwd=F3_DIR, capture_output=True, text=True,
                           encoding="utf-8", errors="replace", timeout=120)
        except Exception:
            pass
    res = _resultados(chip)
    res["chip"] = chip
    return {"ok": ok, "chip": chip, "salida": salida[-1500:], "resultados": res}


def _pipeline(chip, modalidad, escenario="D_MIXTO"):
    """Flujo completo F1 (contexto, si falta) -> F2 (venta con aporte) -> F3 (masa)."""
    pasos = []
    ctx = os.path.join(POT_CACHE, chip + "-contexto.json")
    if os.path.exists(ctx):
        pasos.append({"paso": "f1_contexto", "ok": True, "salida": "contexto ya existente"})
    else:
        try:
            proc = subprocess.run([sys.executable, F1_FETCH_SCRIPT, "--chip", chip],
                                  cwd=ROOT, capture_output=True, text=True,
                                  encoding="utf-8", errors="replace", timeout=300)
            ok1 = proc.returncode == 0 and os.path.exists(ctx)
            sal1 = ((proc.stdout or "") + (proc.stderr or "")).strip()
        except Exception as ex:
            ok1, sal1 = False, "ERROR: " + str(ex)
        pasos.append({"paso": "f1_contexto", "ok": ok1, "salida": sal1[-800:]})

    f2 = _calcular_f2(chip, modalidad)
    pasos.append({"paso": "f2_venta", "ok": f2["ok"], "salida": f2["salida"][-800:]})

    f3 = None
    if f2["ok"]:
        f3 = _generar_f3(chip, escenario)
        pasos.append({"paso": "f3_distribucion", "ok": f3["ok"], "salida": f3["salida"][-800:]})
    else:
        pasos.append({"paso": "f3_distribucion", "ok": False, "salida": "omitido: F2 falló"})

    return {
        "chip": chip,
        "completado": all(p["ok"] for p in pasos),
        "pasos": pasos,
        "f2": {"modalidad_dueno_lote": f2["modalidad_dueno_lote"],
               "fraccion_aporte_pct": f2["fraccion_aporte_pct"],
               "resumen": f2["resumen"]},
        "f3": ({"resultados": f3["resultados"]} if f3 and f3["ok"] else None),
    }


def _json(ruta):
    if not os.path.exists(ruta):
        return {}
    try:
        with io.open(ruta, "r", encoding="utf-8") as f:
            d = json.load(f)
        return d if isinstance(d, dict) else {}
    except Exception:
        return {}


def _lotes():
    chips = []
    if os.path.isdir(POT_CACHE):
        for nombre in sorted(os.listdir(POT_CACHE)):
            if nombre.endswith("-contexto.json"):
                chips.append(nombre[:-len("-contexto.json")])
    return chips


def _contexto(chip):
    raw = _json(os.path.join(POT_CACHE, chip + "-contexto.json"))
    if not raw:
        return None
    lote = raw.get("lote_objetivo", {})
    topo = raw.get("topografia", {})
    pot = raw.get("pot_data", {})
    desnivel = None
    if isinstance(topo, dict):
        try:
            cmin = float(topo.get("cota_min") or topo.get("min") or 0)
            cmax = float(topo.get("cota_max") or topo.get("max") or 0)
            desnivel = round(cmax - cmin, 2)
        except Exception:
            desnivel = None

    def _area_lote():
        real = _area_shoelace_local(lote.get("vertices_3d_local") or lote.get("vertices") or lote.get("poligono"))
        if real is not None:
            return real
        for k in ("area_m2", "area", "area_m"):
            if lote.get(k) is not None:
                return lote[k]
        return None

    _v3d = lote.get("vertices_3d_local") or lote.get("vertices") or lote.get("poligono") or []

    return {
        "chip": chip,
        "lote": {
            "area_m2": _area_lote(),
            "perimetro_m": _perimetro_local(_v3d) or lote.get("perimetro_m") or lote.get("perimetro"),
            "n_vertices": len(_v3d),
        },
        "topografia": {
            "estado": topo.get("estado", "ESTIMADA") if isinstance(topo, dict) else None,
            "desnivel_m": desnivel,
        },
        "conteos": {
            "vias": len(raw.get("vias_oficiales", [])),
            "vecinos": len(raw.get("vecinos", [])),
            "espacios_publicos": len(raw.get("espacios_publicos", [])),
        },
        "pot": {
            "upz": pot.get("upz"),
            "tratamiento": pot.get("tratamiento"),
            "sector_normativo": pot.get("sector_normativo"),
            "rango_edificabilidad": pot.get("rango_edificabilidad"),
            "altura_maxima_m": pot.get("altura_maxima_m"),
            "io_maximo": pot.get("io_maximo"),
            "ic_maximo": pot.get("ic_maximo"),
            "tipologia": pot.get("tipologia"),
            "antejardin_m": pot.get("antejardin_m"),
        },
    }


def _vecinos_por_lado(chip):
    """Vecinos colindantes por lado (nomenclatura cardinal) CON overrides del operador."""
    data = _vecinos_por_lado_data(chip)
    return data if data else None


# ---------------- Plano SVG (lados + contexto 25 m) ----------------


def _clip_segment_lb(p1, p2, rect):
    """Liang-Barsky: devuelve el segmento visible [x1,y1,x2,y2] o None."""
    x0, y0 = p1[0], p1[1]
    x1, y1 = p2[0], p2[1]
    xmin, ymin, xmax, ymax = rect
    dx = x1 - x0
    dy = y1 - y0
    p = [-dx, dx, -dy, dy]
    q = [x0 - xmin, xmax - x0, y0 - ymin, ymax - y0]
    u1, u2 = 0.0, 1.0
    for pi, qi in zip(p, q):
        if pi == 0:
            if qi < 0:
                return None
        else:
            r = qi / pi
            if pi < 0:
                if r > u2:
                    return None
                if r > u1:
                    u1 = r
            else:
                if r < u1:
                    return None
                if r < u2:
                    u2 = r
    return [x0 + u1 * dx, y0 + u1 * dy, x0 + u2 * dx, y0 + u2 * dy]


def _clip_polyline(pts, rect):
    """Recorta una polilinea a rect; lista de segmentos visibles [[x1,y1,x2,y2], ...]."""
    out = []
    for i in range(len(pts) - 1):
        seg = _clip_segment_lb(pts[i], pts[i + 1], rect)
        if seg:
            out.append(seg)
    return out


def _clip_polygon(pts, rect):
    """Sutherland-Hodgman: recorta un poligono a rect; lista de [x, y]."""
    xmin, ymin, xmax, ymax = rect

    def eje(poly, axis, bound, mayor):
        out = []
        n = len(poly)
        for i in range(n):
            cur = poly[i]
            prev = poly[i - 1]
            cur_in = cur[axis] >= bound if mayor else cur[axis] <= bound
            prev_in = prev[axis] >= bound if mayor else prev[axis] <= bound
            if cur_in:
                if not prev_in:
                    t = (bound - prev[axis]) / (cur[axis] - prev[axis])
                    out.append([prev[0] + t * (cur[0] - prev[0]),
                                prev[1] + t * (cur[1] - prev[1])])
                out.append(list(cur))
            elif prev_in:
                t = (bound - prev[axis]) / (cur[axis] - prev[axis])
                out.append([prev[0] + t * (cur[0] - prev[0]),
                            prev[1] + t * (cur[1] - prev[1])])
        return out

    poly = [list(p) for p in pts]
    poly = eje(poly, 0, xmin, True)
    poly = eje(poly, 0, xmax, False)
    poly = eje(poly, 1, ymin, True)
    poly = eje(poly, 1, ymax, False)
    return poly


def _area_m2(pts):
    """Area (m2) de un poligono por formula del zapato (shoelace)."""
    if not pts or len(pts) < 3:
        return 0.0
    s = 0.0
    m = len(pts)
    for i in range(m):
        x1, y1 = pts[i][0], pts[i][1]
        x2, y2 = pts[(i + 1) % m][0], pts[(i + 1) % m][1]
        s += x1 * y2 - x2 * y1
    return round(abs(s) / 2.0, 1)


def _plano(chip):
    """Geometria del plano SVG: lote + lados reconstruidos + contexto recortado a 25 m."""
    ctx = _json(os.path.join(POT_CACHE, chip + "-contexto.json"))
    vl = _vecinos_por_lado_data(chip) or {}
    if not ctx:
        return None
    lote = [[float(p[0]), float(p[1])]
            for p in ctx.get("lote_objetivo", {}).get("vertices_3d_local", [])]
    if len(lote) < 3:
        return None
    if lote[0] == lote[-1]:
        lote = lote[:-1]
    n = len(lote)

    lados = []
    for k, lado in enumerate((vl or {}).get("lados", [])):
        segs = lado.get("segmentos", [])
        pts = []
        for s in segs:
            pts.append(lote[int(s) % n])
        if segs:
            pts.append(lote[(int(segs[-1]) + 1) % n])
        lados.append({
            "lado_id": lado.get("lado_id", k),
            "cardinal": lado.get("cardinal"),
            "cardinal_label": lado.get("cardinal_label", lado.get("cardinal")),
            "frente": lado.get("frente"),
            "frente_override": lado.get("frente_override"),
            "azimut_grados": lado.get("azimut_grados"),
            "longitud_m": lado.get("longitud_m"),
            "n_vecinos": lado.get("n_vecinos"),
            "vecinos_chips": [v.get("chip") for v in lado.get("vecinos", [])],
            "polyline": [[round(p[0], 2), round(p[1], 2)] for p in pts],
        })

    xs = [p[0] for p in lote]
    ys = [p[1] for p in lote]
    xmin, xmax = min(xs) - 25.0, max(xs) + 25.0
    ymin, ymax = min(ys) - 25.0, max(ys) + 25.0
    rect = (xmin, ymin, xmax, ymax)

    vias = []
    for v in ctx.get("vias_oficiales", []):
        pts = [[float(p[0]), float(p[1])] for p in v.get("coordenadas_local", [])]
        if len(pts) >= 2:
            segs = _clip_polyline(pts, rect)
            if segs:
                vias.append({"nombre": v.get("nombre"),
                             "segmentos": [[round(x, 2) for x in s] for s in segs]})

    eps = []
    for e in ctx.get("espacios_publicos", []):
        pts = [[float(p[0]), float(p[1])] for p in e.get("coordenadas_local", [])]
        if len(pts) >= 3:
            poly = _clip_polygon(pts, rect)
            if len(poly) >= 3:
                eps.append({"nombre": e.get("nombre"),
                            "polyline": [[round(p[0], 2), round(p[1], 2)] for p in poly]})

    vecinos = []
    areas = {}
    for v in ctx.get("vecinos", []):
        pts = [[float(p[0]), float(p[1])] for p in v.get("vertices_3d_local", [])]
        if len(pts) >= 3:
            poly = _clip_polygon(pts, rect)
            if len(poly) >= 3:
                _chip = v.get("chip", "")
                areas[_chip] = round(_area_m2(pts), 1)
                vecinos.append({"chip": _chip,
                                "area_m2": areas[_chip],
                                "polyline": [[round(p[0], 2), round(p[1], 2)] for p in poly]})

    nombres = {}
    for lado_v in (vl or {}).get("lados", []):
        for v in lado_v.get("vecinos", []):
            _c = v.get("chip")
            if _c:
                nombres.setdefault(_c, v.get("nombre") or _c)

    colindantes = {}
    for lado in lados:
        for cv in lado["vecinos_chips"]:
            if cv:
                _e = colindantes.setdefault(cv, {"chip": cv, "n_lados": 0, "lado_id": lado["lado_id"]})
                _e["n_lados"] += 1

    return {
        "chip": chip,
        "azimuth_norte_grados": (ctx.get("metadata") or {}).get("azimuth_norte_grados"),
        "viewport": [round(xmin, 2), round(ymin, 2), round(xmax, 2), round(ymax, 2)],
        "lote": [[round(p[0], 2), round(p[1], 2)] for p in lote],
        "lados": lados,
        "vias": vias,
        "vecinos": vecinos,
        "espacios_publicos": eps,
        "colindantes": [{"chip": _e["chip"], "n_lados": _e["n_lados"],
                         "lado_id": _e["lado_id"],
                         "nombre": nombres.get(_e["chip"], _e["chip"]),
                         "area_m2": areas.get(_e["chip"])}
                        for _c, _e in sorted(colindantes.items())],
    }


def _usos_por_sector():
    """Carga data/pot-bogota/usos-por-sector.json (base + overrides por UPZ/sector)."""
    return _json(USOS_SECTOR_RUTA)


def _area_actividad(chip):
    """Area de actividad del lote desde data/pot-bogota/areas-actividad.json
    (capa AreaActividad de la geobase POT 555). Devuelve dict o None."""
    data = _json(AREAS_ACTIVIDAD_RUTA)
    lote = (data.get("lotes") or {}).get(chip)
    if not lote:
        return None
    return {
        "codigo": lote.get("area_actividad"),
        "nombre": lote.get("nombre"),
        "fuente": data.get("fuente"),
    }


def _sector_uso_geobase(chip):
    """Clasificacion de uso por sector desde data/pot-bogota/sectores-uso-lotes.json
    (cruce espacial contra las capas del Decreto 555). Devuelve dict o None."""
    data = _json(SECTORES_USO_RUTA)
    return (data.get("lotes") or {}).get(chip)


def _normalizar_upz(upz):
    if not upz:
        return None
    return " ".join(str(upz).strip().split()).upper()


def _categoria_aa(codigo):
    """Mapea el codigo de area de actividad (AreaActividad) a la categoria del
    cuadro de usos (Proximidad / Estructurante / Grandes_Servicios_Metropolitanos)."""
    data = _usos_por_sector()
    taxo = data.get("aa_taxonomia") or {}
    return taxo.get(codigo)


def _catalogo_usos(cats, fuente):
    """Arma el catalogo de usos (principal/complementario/restringido/prohibido)
    con trazabilidad por item. `cats` trae esas 4 claves."""
    catalogo = []
    for categoria in ("principal", "complementario", "restringido", "prohibido"):
        for nombre in (cats or {}).get(categoria, []):
            catalogo.append({
                "nombre": nombre,
                "categoria": categoria,
                "descripcion": USOS_DESC.get(nombre, ""),
                "fuente": fuente,
            })
    return catalogo


def _usos(chip):
    ctx = _contexto(chip)
    upz = ctx["pot"]["upz"] if ctx else None
    tratamiento = ctx["pot"]["tratamiento"] if ctx else None
    area_actividad = _area_actividad(chip)
    sector_uso_geobase = _sector_uso_geobase(chip)
    data = _usos_por_sector()
    base_cats = data.get("base") or {
        "principal": [u["nombre"] for u in USOS_CATALOGO if u["categoria"] == "principal"],
        "complementario": [u["nombre"] for u in USOS_CATALOGO if u["categoria"] == "complementario"],
        "restringido": [],
        "prohibido": [u["nombre"] for u in USOS_CATALOGO if u["categoria"] == "prohibido"],
    }
    sectores = data.get("sectores") or {}
    areas_actividad = data.get("areas_actividad") or {}
    key = _normalizar_upz(upz)
    sector = sectores.get(key) if key else None

    # 1) Resolucion normativa por AREA DE ACTIVIDAD (Art. 233-243 + Anexo 5)
    categoria_aa = None
    cats = None
    fuente = "base"
    if area_actividad:
        categoria_aa = _categoria_aa(area_actividad.get("codigo"))
        if categoria_aa and categoria_aa in areas_actividad:
            cats = areas_actividad[categoria_aa]
            fuente = "area_actividad"
    # 2) Fallback: sector UPZ (legacy)
    if cats is None:
        if sector and (sector.get("principal") or sector.get("complementario")
                       or sector.get("restringido") or sector.get("prohibido")):
            cats = sector
            fuente = "sector"
        else:
            cats = base_cats
            fuente = "base"

    catalogo = _catalogo_usos(cats, fuente)
    return {
        "chip": chip,
        "upz": upz,
        "tratamiento": tratamiento,
        "catalogo": catalogo,
        "fuente": fuente,
        "sector_clave": key,
        "sector_estado": (sector or {}).get("estado"),
        "pendiente_usos_sector": bool(sector and sector.get("estado") == "pendiente-usos"),
        "area_actividad": area_actividad,
        "categoria_area_actividad": categoria_aa,
        "pendiente_cuadro_uso": area_actividad is not None,
        "sector_uso_geobase": sector_uso_geobase,
        "nota": data.get("nota") or ("Cuadro de usos segun area de actividad (Decreto 555/2021 "
                "Art. 233-243 + Anexo 5). P=principal, C=complementario, R=restringido; "
                "lo no listado esta prohibido en esa area de actividad."),
    }


def _financiero(chip):
    """Variables financieras + fuentes (base de decisión del operador).
    El área del lote se toma del contexto real F1 (no del valor de referencia
    del archivo de parámetros); los overrides del operador (financiero-override.json)
    ganan sobre los valores de referencia de mercado."""
    ruta = None
    for cand in (os.path.join(F2_VENTA_DIR, "parametros_{}_mercado2026.json".format(chip)),
                 os.path.join(F2_VENTA_DIR, "parametros_{}_venta.json".format(chip)),
                 os.path.join(F2_VENTA_DIR, "parametros_{}.json".format(chip))):
        if os.path.exists(cand):
            ruta = cand
            break
    usar_default = False
    if not ruta:
        ruta = os.path.join(F2_VENTA_DIR, "parametros_entrada.json")
        usar_default = True
        if not os.path.exists(ruta):
            return {"chip": chip, "disponible": False, "nota": "sin parametros F2 para este chip"}
    d = _json(ruta)
    ov = _financiero_override_chip(chip) or {}

    ctx = _contexto(chip)
    area_real = (ctx or {}).get("lote", {}).get("area_m2") if ctx else None
    area_final = ov.get("area_m2") if ov.get("area_m2") not in (None, "") else (
        area_real if area_real is not None else d.get("lote", {}).get("area_m2"))

    lote = d.get("lote", {})
    fin = d.get("financiero", {})
    esc = d.get("escenarios", {})

    def _mix(ov_key, base_val):
        v = ov.get(ov_key)
        return base_val if v is None or v == "" else v

    area_fuente = "parametros"
    if ov.get("area_m2") not in (None, ""):
        area_fuente = "override"
    elif area_real is not None:
        area_fuente = "contexto"

    lote_out = {
        "area_m2": area_final,
        "area_m2_fuente": area_fuente,
        "precio_suelo_m2": _mix("precio_suelo_m2", lote.get("precio_suelo_m2")),
        "impuestos_escritura_pct": _mix("impuestos_escritura_pct", lote.get("impuestos_escritura_pct")),
        "costo_lote_total_cop": _mix("costo_lote_total_cop", lote.get("costo_lote_total_cop")),
        "fuente": ov.get("fuente") or lote.get("fuente"),
        "fuente_url": ov.get("fuente_url") or lote.get("fuente_url"),
    }
    financiero_out = {
        "costos_blandos_pct": _mix("costos_blandos_pct", fin.get("costos_blandos_pct")),
        "marketing_ventas_pct": _mix("marketing_ventas_pct", fin.get("marketing_ventas_pct")),
        "nota_costos_blandos": fin.get("nota_costos_blandos"),
        "nota_marketing": fin.get("nota_marketing"),
    }
    escenarios = []
    esc_ov = ov.get("escenarios") if isinstance(ov.get("escenarios"), dict) else {}
    for eid, ev in esc.items():
        eo = esc_ov.get(eid) if isinstance(esc_ov.get(eid), dict) else {}
        escenarios.append({
            "id": eid,
            "nombre": ev.get("nombre", eid),
            "nivel_acabados": ev.get("nivel_acabados"),
            "precio_venta_m2": eo.get("precio_venta_m2") if eo.get("precio_venta_m2") not in (None, "") else ev.get("precio_venta_m2"),
            "costo_construccion_m2": eo.get("costo_construccion_m2") if eo.get("costo_construccion_m2") not in (None, "") else ev.get("costo_construccion_m2"),
            "fuente_precio": ev.get("fuente_precio"),
        })
    nota = None
    if usar_default:
        nota = ("Este CHIP no tiene archivo de parámetros propio; se muestran los valores de "
                "referencia de mercado (parametros_entrada.json). Edítelos y pulse 'Guardar financiero' "
                "para crear parametros_{}_mercado2026.json.".format(chip))
    return {
        "chip": chip,
        "disponible": True,
        "ruta_parametros": ruta,
        "tiene_override": bool(ov),
        "lote": lote_out,
        "financiero": financiero_out,
        "escenarios": escenarios,
        "nota": nota,
    }


def _resultados(caso):
    base = os.path.join(F3_CASOS, caso)
    pa = _json(os.path.join(base, "programa-areas.json"))
    ac = _json(os.path.join(base, "accesos.json"))
    lay = _json(os.path.join(base, "layout_espacial.json"))
    usos = sorted({u.get("uso") for p in pa.get("programa_pisos", [])
                   for u in p.get("usos", []) if u.get("uso") != "Nucleo"})
    return {
        "caso": caso,
        "titulo": CASO_TITULO.get(caso),
        "chip": CASO_CHIP.get(caso) or caso,
        "gfa_total": pa.get("gfa_total"),
        "pisos": pa.get("pisos"),
        "area_por_piso": pa.get("area_por_piso"),
        "usos": usos,
        "nucleo": {
            "hueco_m2_piso": pa.get("nucleo", {}).get("hueco_m2_piso"),
            "circulacion_m2": pa.get("nucleo", {}).get("circulacion_m2"),
            "servicios_m2": pa.get("nucleo", {}).get("servicios_m2"),
        },
        "accesos": ac.get("resumen", {}),
        "reparto_vertical": lay.get("reparto_vertical", {}),
        "poblacion": lay.get("poblacion_estimada", {}),
    }


def _proyectos():
    if not os.path.isdir(PROYECTOS):
        return []
    return sorted([n for n in os.listdir(PROYECTOS)
                   if os.path.isdir(os.path.join(PROYECTOS, n)) and not n.startswith("_")])


def _guardar_proyecto(nombre, data):
    destino = PROVISIONAL if not nombre else os.path.join(PROYECTOS, nombre)
    if not os.path.isdir(destino):
        os.makedirs(destino)
    ruta = os.path.join(destino, "proyecto.json")
    with io.open(ruta, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    # Espejo ACTIVO: data/activo/proyecto.json es la ruta estable que
    # consume F0_LOAD_PROYECTO (input ruta_json). Se reescribe en cada
    # guardado; cierra el pendiente #4 del cierre 2026-08-23.
    try:
        carpeta_activo = os.path.dirname(ACTIVO_PROYECTO)
        if not os.path.isdir(carpeta_activo):
            os.makedirs(carpeta_activo)
        shutil.copy2(ruta, ACTIVO_PROYECTO)
    except OSError as exc:
        print("[aviso] no se pudo escribir el espejo activo: %s" % exc)
    return ruta, destino


def _crear_estructura(nombre):
    """Crea la estructura del proyecto y copia el material provisional."""
    if not nombre:
        return False, "nombre vacío"
    carpeta = os.path.join(PROYECTOS, nombre)
    if not os.path.isdir(carpeta):
        os.makedirs(carpeta)
    for sub in ("Normativa", "Financiero", "Modelado", "Archicad"):
        d = os.path.join(carpeta, sub)
        if not os.path.isdir(d):
            os.makedirs(d)
    # copiar material provisional (si existe) al proyecto nombrado
    if os.path.isdir(PROVISIONAL):
        for nombre_archivo in os.listdir(PROVISIONAL):
            origen = os.path.join(PROVISIONAL, nombre_archivo)
            destino = os.path.join(carpeta, nombre_archivo)
            if os.path.isfile(origen) and not os.path.exists(destino):
                shutil.copy2(origen, destino)
    return True, carpeta


class Handler(BaseHTTPRequestHandler):
    def _send(self, code, body, ctype="application/json; charset=utf-8"):
        if isinstance(body, (dict, list)):
            body = json.dumps(body, ensure_ascii=False)
        data = body.encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def _json_error(self, msg, code=400):
        self._send(code, {"ok": False, "error": msg})

    def do_GET(self):
        parsed = urlparse(self.path)
        q = parse_qs(parsed.query)
        if parsed.path in ("/", "/index.html"):
            ruta = os.path.join(ORQ_DIR, "index.html")
            if os.path.exists(ruta):
                with io.open(ruta, "r", encoding="utf-8") as f:
                    self._send(200, f.read(), "text/html; charset=utf-8")
            else:
                self._json_error("index.html no encontrado", 404)
            return
        if parsed.path == "/api/lotes":
            self._send(200, {"ok": True, "lotes": _lotes()})
            return
        if parsed.path == "/api/variables":
            self._send(200, {"ok": True, "variables": VARIABLES,
                             "caso_chip": CASO_CHIP, "caso_titulo": CASO_TITULO,
                             "modos": MODOS_FINANCIEROS, "escenarios": ESCENARIOS_FINANCIEROS})
            return
        if parsed.path == "/api/proyectos":
            self._send(200, {"ok": True, "proyectos": _proyectos()})
            return
        if parsed.path == "/api/contexto":
            chip = (q.get("chip") or [""])[0]
            info = _contexto(chip)
            if info is None:
                self._json_error("sin contexto para el chip '{}'".format(chip), 404)
            else:
                self._send(200, {"ok": True, "contexto": info})
            return
        if parsed.path == "/api/usos":
            chip = (q.get("chip") or [""])[0]
            self._send(200, {"ok": True, "usos": _usos(chip)})
            return
        if parsed.path == "/api/vecinos-por-lado":
            chip = (q.get("chip") or [""])[0]
            info = _vecinos_por_lado(chip)
            if info is None:
                self._json_error("sin vecinos-por-lado para el chip '{}'".format(chip), 404)
            else:
                self._send(200, {"ok": True, "vecinos_por_lado": info})
            return

        if parsed.path == "/api/plano":
            chip = (q.get("chip") or [""])[0]
            info = _plano(chip)
            if info is None:
                self._json_error("sin plano para el chip '{}'".format(chip), 404)
            else:
                self._send(200, {"ok": True, "plano": info})
            return
        if parsed.path == "/api/financiero":
            chip = (q.get("chip") or [""])[0]
            self._send(200, {"ok": True, "financiero": _financiero(chip)})
            return
        if parsed.path == "/api/resultados":
            caso = (q.get("caso") or ["A"])[0]
            self._send(200, {"ok": True, "resultados": _resultados(caso)})
            return
        if parsed.path == "/api/norma-override":
            chip = (q.get("chip") or [""])[0]
            ov = _norma_override_chip(chip) if chip else None
            ctx = _contexto(chip) if chip else None
            self._send(200, {"ok": True, "chip": chip,
                             "contexto_pot": (ctx or {}).get("pot", {}),
                             "override": ov or {}})
            return
        if parsed.path == "/api/archivos":
            self._send(200, {"ok": True, "archivos": ARCHIVOS_INTERCAMBIO})
            return
        if parsed.path == "/api/setback-override":
            chip = (q.get("chip") or [""])[0]
            ov = _setback_override_chip(chip) if chip else None
            ctx = _contexto(chip) if chip else None
            # Provide the override in the format expected by the frontend
            override_data = {}
            if ov and isinstance(ov, list):
                override_data[chip] = ov
            self._send(200, {"ok": True, "chip": chip,
                             "contexto": (ctx or {}).get("pot", {}),
                             "override": override_data})
            return
        self._json_error("ruta no encontrada", 404)

    def do_POST(self):
        parsed = urlparse(self.path)
        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length).decode("utf-8", errors="replace")
        try:
            data = json.loads(body) if body else {}
        except Exception:
            self._json_error("JSON inválido")
            return

        if parsed.path == "/api/proyecto":
            nombre = data.get("nombre", "").strip()
            crear = bool(data.get("crear_estructura", False))
            if crear and not nombre:
                self._json_error("Para crear la estructura escriba un nombre de proyecto.")
                return
            ruta, destino = _guardar_proyecto(nombre, data)
            creado = None
            if crear:
                ok, carpeta = _crear_estructura(nombre)
                if ok:
                    creado = carpeta
            self._send(200, {"ok": True, "ruta": ruta, "destino": destino, "estructura_creada": creado, "ruta_activa": ACTIVO_PROYECTO})
            return

        if parsed.path == "/api/calcular-f2":
            chip = (data.get("chip") or "").strip()
            if not chip:
                self._json_error("chip requerido")
                return
            res = _calcular_f2(chip, _modalidad_desde_data(data), data.get("gfa_m2"),
                               data.get("costo_lote_cop"))
            self._send(200, {"ok": True, "f2": res})
            return

        if parsed.path == "/api/generar-f3":
            chip = (data.get("chip") or "").strip()
            if not chip:
                self._json_error("chip requerido")
                return
            res = _generar_f3(chip, data.get("escenario", "D_MIXTO"))
            self._send(200, {"ok": True, "f3": res})
            return

        if parsed.path == "/api/pipeline":
            chip = (data.get("chip") or "").strip()
            if not chip:
                self._json_error("chip requerido")
                return
            res = _pipeline(chip, _modalidad_desde_data(data),
                            data.get("escenario", "D_MIXTO"))
            self._send(200, {"ok": True, "pipeline": res})
            return

        if parsed.path == "/api/norma-override":
            chip = (data.get("chip") or "").strip()
            if not chip:
                self._json_error("chip requerido")
                return
            ok, ruta = _norma_override_guardar(chip, data.get("override") or {})
            self._send(200, {"ok": ok, "ruta": ruta,
                             "override": _norma_override_chip(chip)})
            return

        if parsed.path == "/api/financiero":
            chip = (data.get("chip") or "").strip()
            if not chip:
                self._json_error("chip requerido")
                return
            ok, detalle = _financiero_override_guardar(chip, data.get("override") or {})
            self._send(200, {"ok": ok, "ruta": detalle,
                             "financiero": _financiero(chip) if ok else None})
            return

        if parsed.path == "/api/setback-override":
            chip = (data.get("chip") or "").strip()
            if not chip:
                self._json_error("chip requerido")
                return
            ok, ruta = _setback_override_guardar(chip, data.get("override") or {})
            self._send(200, {"ok": ok, "ruta": ruta,
                             "setback_override": _setback_override_chip(chip)})
            return

        if parsed.path == "/api/vecinos-por-lado":
            chip = (data.get("chip") or "").strip()
            if not chip:
                self._json_error("chip requerido")
                return
            vpl = data.get("vecinos_por_lado")
            if not isinstance(vpl, dict):
                self._json_error("vecinos_por_lado requerido")
                return
            vpl["chip"] = chip
            vpl["_schema"] = "vecinos_por_lado_override_v01"
            vpl["_saved_at"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            ruta = _vecinos_override_ruta(chip)
            try:
                with io.open(ruta, "w", encoding="utf-8") as f:
                    json.dump(vpl, f, indent=2, ensure_ascii=False)
                # refrescar el ACTIVO que lee el canvas
                with io.open(ACTIVO_VECINOS, "w", encoding="utf-8") as f:
                    json.dump(vpl, f, indent=2, ensure_ascii=False)
                self._send(200, {"ok": True, "ruta": ruta, "activo": ACTIVO_VECINOS})
            except Exception as e:
                self._json_error(str(e), 500)
            return

        if parsed.path == "/api/activar-chip":
            chip = (data.get("chip") or "").strip()
            if not chip:
                self._json_error("chip requerido")
                return
            activados = _activar_chip(chip)
            self._send(200, {"ok": True, "chip": chip, "activados": activados})
            return

        if parsed.path == "/api/activar-caso":
            caso = (data.get("caso") or "").strip()
            if not caso:
                self._json_error("caso requerido")
                return
            activados = _activar_caso(caso)
            self._send(200, {"ok": True, "caso": caso, "activados": activados})
            return

        if parsed.path == "/api/exportar-gfa":
            ruta = _gfa_flag_poner(True)
            if ruta is None:
                self._json_error("no se pudo escribir el flag de exportación", 500)
                return
            self._send(200, {"ok": True, "flag": ruta,
                             "mensaje": "Flag exportar=true escrito. El canvas exportará y lo devolverá a false."})
            return

        self._json_error("ruta no encontrada", 404)

    def log_message(self, fmt, *args):
        sys.stderr.write("[servidor] " + (fmt % args) + "\n")


def main():
    parser = argparse.ArgumentParser(description="Formulario interactivo DiseñoParametrico")
    parser.add_argument("--puerto", type=int, default=8900)
    args = parser.parse_args()
    if not os.path.isdir(PROYECTOS):
        os.makedirs(PROYECTOS)
    if not os.path.isdir(PROVISIONAL):
        os.makedirs(PROVISIONAL)
    server = HTTPServer(("127.0.0.1", args.puerto), Handler)
    print("=" * 64)
    print("Formulario DiseñoParametrico (Parte 1: F1 -> F3)")
    print("Abre en el navegador: http://127.0.0.1:{}".format(args.puerto))
    print("Ctrl+C para detener.")
    print("=" * 64)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nDetenido.")
        server.server_close()


if __name__ == "__main__":
    main()