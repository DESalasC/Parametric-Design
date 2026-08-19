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
PROYECTOS = os.path.join(ORQ_DIR, "proyectos")
PROVISIONAL = os.path.join(PROYECTOS, "_provisional")

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
    {"id": "empate_posterior_pisos", "label": "Nº de pisos del edificio vecino posterior", "tipo": "int",
     "default": 0, "seccion": "normativa",
     "ayuda": "Número de pisos del edificio vecino posterior (proyecto existente). Independiente de empate_posterior_m; pueden darse ambos."},
    {"id": "empate_posterior_m", "label": "Altura (m) del edificio vecino posterior", "tipo": "number",
     "default": None, "seccion": "normativa",
     "ayuda": "Altura total en metros del edificio vecino posterior (proyecto existente). Independiente de empate_posterior_pisos; pueden darse ambos."},
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


def _aporte_a_pago_parcial(aporte, pago_parcial_pct=None):
    """Traduce aporte_lote -> pago_parcial_pct del motor F2 (venta_completa=100,
    aporte_completo=0, participacion=% indicado, default 30)."""
    if aporte == "venta_completa":
        return 100.0
    if aporte == "aporte_completo":
        return 0.0
    try:
        p = float(pago_parcial_pct) if pago_parcial_pct not in (None, "") else 30.0
    except (TypeError, ValueError):
        p = 30.0
    return round(min(100.0, max(0.0, p)), 1)


def _ruta_parametros_f2_venta(chip):
    for cand in (os.path.join(F2_VENTA_DIR, "parametros_{}_mercado2026.json".format(chip)),
                 os.path.join(F2_VENTA_DIR, "parametros_{}.json".format(chip))):
        if os.path.exists(cand):
            return cand
    return os.path.join(F2_VENTA_DIR, "parametros_entrada.json")


def _calcular_f2(chip, aporte_lote, pago_parcial_pct, gfa_m2=None, costo_lote_cop=None):
    """Ejecuta F2 (venta) con el pago_parcial derivado del aporte del lote."""
    pago = _aporte_a_pago_parcial(aporte_lote, pago_parcial_pct)
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
    return {
        "ok": ok,
        "aporte_lote": aporte_lote,
        "pago_parcial_pct": pago,
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
        for k in ("area_m2", "area", "area_m"):
            if lote.get(k) is not None:
                return lote[k]
        return None

    return {
        "chip": chip,
        "lote": {
            "area_m2": _area_lote(),
            "perimetro_m": lote.get("perimetro_m") or lote.get("perimetro"),
            "n_vertices": len(lote.get("vertices", []) or lote.get("poligono", []) or []),
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
        },
    }


def _vecinos_por_lado(chip):
    """Vecinos colindantes por lado (nomenclatura cardinal) desde el JSON pre-generado."""
    data = _json(os.path.join(POT_CACHE, chip + "-vecinos-por-lado.json"))
    return data if data else None


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


def _catalogo_usos(base_cats, sector):
    """Arma el catalogo de usos: sector si trae listas, si no base. Cada item
    lleva 'fuente' para trazabilidad (base vs sector)."""
    if sector and (sector.get("principal") or sector.get("complementario") or sector.get("prohibido")):
        cats = {c: sector.get(c, []) for c in ("principal", "complementario", "prohibido")}
        fuente = "sector"
    else:
        cats = {c: base_cats.get(c, []) for c in ("principal", "complementario", "prohibido")}
        fuente = "base"
    catalogo = []
    for categoria in ("principal", "complementario", "prohibido"):
        for nombre in cats.get(categoria, []):
            catalogo.append({
                "nombre": nombre,
                "categoria": categoria,
                "descripcion": USOS_DESC.get(nombre, ""),
                "fuente": fuente,
            })
    return catalogo, fuente


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
        "prohibido": [u["nombre"] for u in USOS_CATALOGO if u["categoria"] == "prohibido"],
    }
    sectores = data.get("sectores") or {}
    key = _normalizar_upz(upz)
    sector = sectores.get(key) if key else None
    catalogo, fuente = _catalogo_usos(base_cats, sector)
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
        "pendiente_cuadro_uso": area_actividad is not None,
        "sector_uso_geobase": sector_uso_geobase,
        "nota": data.get("nota") or ("Catálogo base NSR-10 A.2.5 + POT 555. Los usos permitidos/prohibidos "
                "definitivos dependen de la reglamentación del sector/UPZ y deben validarse."),
    }


def _financiero(chip):
    """Variables financieras + fuentes (base de decisión del operador)."""
    ruta = None
    for cand in (os.path.join(F2_VENTA_DIR, "parametros_{}_mercado2026.json".format(chip)),
                 os.path.join(F2_VENTA_DIR, "parametros_{}.json".format(chip))):
        if os.path.exists(cand):
            ruta = cand
            break
    if not ruta:
        return {"chip": chip, "disponible": False, "nota": "sin parametros F2 para este chip"}
    d = _json(ruta)
    lote = d.get("lote", {})
    fin = d.get("financiero", {})
    esc = d.get("escenarios", {})
    escenarios = []
    for eid, ev in esc.items():
        escenarios.append({
            "id": eid,
            "nombre": ev.get("nombre", eid),
            "nivel_acabados": ev.get("nivel_acabados"),
            "precio_venta_m2": ev.get("precio_venta_m2"),
            "costo_construccion_m2": ev.get("costo_construccion_m2"),
            "fuente_precio": ev.get("fuente_precio"),
        })
    return {
        "chip": chip,
        "disponible": True,
        "ruta_parametros": ruta,
        "lote": {
            "area_m2": lote.get("area_m2"),
            "precio_suelo_m2": lote.get("precio_suelo_m2"),
            "impuestos_escritura_pct": lote.get("impuestos_escritura_pct"),
            "costo_lote_total_cop": lote.get("costo_lote_total_cop"),
            "fuente": lote.get("fuente"),
            "fuente_url": lote.get("fuente_url"),
        },
        "financiero": {
            "costos_blandos_pct": fin.get("costos_blandos_pct"),
            "marketing_ventas_pct": fin.get("marketing_ventas_pct"),
            "nota_costos_blandos": fin.get("nota_costos_blandos"),
            "nota_marketing": fin.get("nota_marketing"),
        },
        "escenarios": escenarios,
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
        if parsed.path == "/api/financiero":
            chip = (q.get("chip") or [""])[0]
            self._send(200, {"ok": True, "financiero": _financiero(chip)})
            return
        if parsed.path == "/api/resultados":
            caso = (q.get("caso") or ["A"])[0]
            self._send(200, {"ok": True, "resultados": _resultados(caso)})
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
            self._send(200, {"ok": True, "ruta": ruta, "destino": destino, "estructura_creada": creado})
            return

        if parsed.path == "/api/calcular-f2":
            chip = (data.get("chip") or "").strip()
            if not chip:
                self._json_error("chip requerido")
                return
            res = _calcular_f2(chip, data.get("aporte_lote", "participacion"),
                               data.get("pago_parcial_pct"), data.get("gfa_m2"),
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
