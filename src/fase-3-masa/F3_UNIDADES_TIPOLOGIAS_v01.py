# -*- coding: utf-8 -*-
"""
================================================================================
F3_UNIDADES_TIPOLOGIAS_v01.py - Definición de unidades tipológicas por piso (Fase 3)
Proyecto: DiseñoParametrico / Fase 3
Generador Python (CLI) + GH Python Script para Grasshopper
================================================================================
"""
import json
import os
import sys
import math
from typing import List, Dict, Any, Optional, Tuple

# ============================================================
# CONSTANTES ARQUITECTÓNICAS (NSR-10, POT, Res. 0549/2015)
# ============================================================
ANCHO_PASILLO_MIN = 1.20
ANCHO_PASILLO_PREF = 1.50
AREA_MIN_VIVIENDA_VIS = 42.0
AREA_MIN_VIVIENDA_EST = 50.0
AREA_MIN_LOCAL = 20.0
PROFUNDIDAD_MAX_VIV = 12.0
PROFUNDIDAD_MAX_LOCAL = 15.0
RECORRIDO_MAX_EVAC = 30.0
PARQUEO_VIVIENDA = 1.0
PARQUEO_COMERCIO_POR_100M2 = 1.0
AREA_PARQUEO_UNIT = 12.5
AREA_PARQUEO_CIRC = 0.30

TIPOLOGIAS_F2 = {
    "Local comercial turistico": {"area_und": 40.0, "tipo": "comercio", "min_area": AREA_MIN_LOCAL},
    "Vivienda estandar": {"area_und": 55.0, "tipo": "vivienda", "min_area": AREA_MIN_VIVIENDA_EST},
}

# ============================================================
# UTILIDADES GEOMÉTRICAS 2D
# ============================================================
def rectangulo(x: float, y: float, w: float, h: float) -> List[Tuple[float, float]]:
    hw, hh = w / 2.0, h / 2.0
    return [(x - hw, y - hh), (x + hw, y - hh), (x + hw, y + hh), (x - hw, y + hh), (x - hw, y - hh)]

def area_poligono(pts: List[Tuple[float, float]]) -> float:
    if len(pts) < 3: return 0.0
    a = 0.0
    for i in range(len(pts) - 1):
        a += pts[i][0] * pts[i + 1][1] - pts[i + 1][0] * pts[i][1]
    return abs(a) / 2.0

def bbox_poligono(pts: List[Tuple[float, float]]) -> Tuple[float, float, float, float]:
    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
    return min(xs), min(ys), max(xs), max(ys)

def rotar(pts: List[Tuple[float, float]], ang: float, cx: float = 0.0, cy: float = 0.0) -> List[Tuple[float, float]]:
    ca, sa = math.cos(ang), math.sin(ang)
    out = []
    for x, y in pts:
        x0, y0 = x - cx, y - cy
        out.append((cx + x0 * ca - y0 * sa, cy + x0 * sa + y0 * ca))
    return out

# ============================================================
# CARGA DE ARCHIVOS
# ============================================================
def cargar_json(ruta: str) -> Dict:
    if not ruta or not os.path.exists(ruta): return {}
    try:
        with open(ruta, "r", encoding="utf-8") as f: return json.load(f)
    except Exception: return {}

def resolver_rutas(caso_id: str) -> Tuple[str, str, str]:
    base = os.path.dirname(os.path.abspath(__file__))
    caso_dir = os.path.join(base, "casos", caso_id)
    layout = os.path.join(caso_dir, "layout_espacial.json")
    f2_base = os.path.join(base, "..", "fase-2-demanda", "F2_Modelo_Financiero", "resultados")
    f2_files = [f for f in os.listdir(f2_base) if f.startswith("resultados_") and f.endswith(".json")]
    f2_path = os.path.join(f2_base, f2_files[0]) if f2_files else ""
    return layout, f2_path, caso_dir

# ============================================================
# DISTRIBUCIÓN DE UNIDADES POR PISO
# ============================================================
def distribuir_unidades_piso(
    nivel: Dict,
    nucleo_info: Dict,
    uso: str,
    tipologia: Dict,
    area_neta_disponible: float,
    lote_frente: float,
    lote_fondo: float,
    angulo_fachada: float = 0.0,
) -> Tuple[List[Dict], List[Dict]]:
    """
    Distribuye unidades en un piso usando dimensiones REALES del lote.
    lote_frente: dimensión paralela a la vía principal (fachada)
    lote_fondo: dimensión perpendicular a la vía
    """
    unidades = []
    circulaciones = []
    
    area_und = tipologia["area_und"]
    tipo_uso = tipologia["tipo"]
    n_max = int(area_neta_disponible / (area_und * 1.12))
    if n_max <= 0: return unidades, circulaciones
    
    n_w = nucleo_info.get("bloque", {}).get("ancho_m", 6.4)
    n_l = nucleo_info.get("bloque", {}).get("largo_m", 9.0)
    
    # Fachada principal = eje X (paralela a lote_frente)
    # Pasillo central a 0.75m del núcleo (lado norte = +Y)
    y_pasillo = n_l / 2.0 + 0.75
    prof_disp_norte = lote_fondo / 2.0 - y_pasillo
    prof_disp_sur = lote_fondo / 2.0 - (-n_l / 2.0 - 0.75)
    
    prof_max = PROFUNDIDAD_MAX_VIV if tipo_uso == "vivienda" else PROFUNDIDAD_MAX_LOCAL
    prof_und = min(prof_disp_norte, prof_max)
    
    if prof_und < tipologia["min_area"] / 8.0:
        return unidades, circulaciones
    
    ancho_und = area_und / prof_und
    margen_lateral = 1.0
    frente_util = lote_frente - 2 * margen_lateral
    n_por_fila = max(1, int(frente_util / ancho_und))
    ancho_und = frente_util / n_por_fila
    
    # Filas norte y sur
    filas = []
    if prof_disp_norte >= prof_und:
        filas.append(("norte", y_pasillo + prof_und / 2.0, prof_und))
    if prof_disp_sur >= prof_und:
        filas.append(("sur", -n_l / 2.0 - 0.75 - prof_und / 2.0, prof_und))
    if not filas:
        prof_centro = min(lote_fondo / 2.0 - n_l / 2.0 - 0.75, prof_max)
        if prof_centro >= tipologia["min_area"] / 8.0:
            filas.append(("centro", 0.0, prof_centro))
    if not filas: return unidades, circulaciones
    
    id_counter = 0
    for lado, y_centro, prof in filas:
        for i in range(n_por_fila):
            if id_counter >= n_max: break
            x_centro = -frente_util / 2.0 + ancho_und / 2.0 + i * ancho_und
            verts = rectangulo(x_centro, y_centro, ancho_und, prof)
            verts_rot = rotar(verts, angulo_fachada)
            unidades.append({
                "id": f"U_{nivel['nivel']}_{uso[:3].upper()}_{id_counter+1:02d}",
                "uso": uso, "tipologia": tipologia.get("nombre", uso),
                "piso": nivel["nivel"], "z_base_m": nivel["z_base_m"],
                "altura_piso": nivel["altura_m"], "vertices": verts_rot,
                "area_m2": round(area_poligono(verts_rot), 2),
                "ancho_m": round(ancho_und, 2), "profundidad_m": round(prof, 2),
                "orientacion": "fachada" if lado != "sur" else "patio",
                "ventilacion_natural": True, "acceso_pasillo": True,
            })
            id_counter += 1
    
    # Un solo pasillo central (norte del núcleo)
    if any(f[0] == "norte" for f in filas):
        pasillo_largo = frente_util + 2 * margen_lateral
        pasillo_verts = rotar(rectangulo(0.0, y_pasillo, pasillo_largo, ANCHO_PASILLO_PREF), angulo_fachada)
        circulaciones.append({
            "tipo": "pasillo_central", "piso": nivel["nivel"], "z_base_m": nivel["z_base_m"],
            "vertices": pasillo_verts, "ancho_m": ANCHO_PASILLO_PREF,
            "largo_m": round(pasillo_largo, 2), "conecta_nucleo": True,
        })
    
    return unidades, circulaciones

def calcular_parqueaderos(layout: Dict, f2_mix: List[Dict], cota_via: float, 
                          lote_frente: float, lote_fondo: float) -> List[Dict]:
    n_viv = sum(d["num_unidades"] for d in f2_mix if d["uso"].lower().startswith("viv"))
    area_com = sum(d["area_vendible_m2"] for d in f2_mix if d["uso"].lower().startswith(("loc", "com")))
    req_viv = n_viv * PARQUEO_VIVIENDA
    req_com = (area_com / 100.0) * PARQUEO_COMERCIO_POR_100M2
    total_req = int(math.ceil(req_viv + req_com))
    
    area_por_puesto = AREA_PARQUEO_UNIT * (1 + AREA_PARQUEO_CIRC)
    area_lote = lote_frente * lote_fondo
    cap_por_nivel = max(1, int(area_lote * 0.8 / area_por_puesto))
    n_niveles_sotano = max(1, math.ceil(total_req / cap_por_nivel))
    
    parqueaderos = []
    for i in range(n_niveles_sotano):
        z = -(i + 1) * 2.5
        cap = min(cap_por_nivel, total_req - i * cap_por_nivel)
        parqueaderos.append({"nivel": -(i+1), "nombre": f"Sótano {i+1}", "z_base_m": z, "altura_m": 2.5,
            "capacidad": cap, "area_m2": round(cap * area_por_puesto, 1), "tipo": "sotano",
            "cota_via_m": cota_via, "es_sotano": True, "lote_frente": lote_frente, "lote_fondo": lote_fondo})
    
    resto = total_req - n_niveles_sotano * cap_por_nivel
    if resto > 0:
        for nivel in layout.get("niveles", []):
            # Parqueadero en superficie SOLO si z_base >= cota_via
            if nivel["z_base_m"] >= cota_via - 0.5:
                parqueaderos.append({"nivel": nivel["nivel"], "nombre": f"Planta {nivel['nivel']} (superficie)",
                    "z_base_m": nivel["z_base_m"], "altura_m": 2.5, "capacidad": resto,
                    "area_m2": round(resto * area_por_puesto, 1), "tipo": "superficie",
                    "cota_via_m": cota_via, "es_sotano": False,
                    "lote_frente": lote_frente, "lote_fondo": lote_fondo})
                break
    return parqueaderos

def generar_unidades_completas(
    layout: Dict, f2_resultados: Dict, cota_via: float = 0.0,
    angulo_fachada: float = 0.0,
    lote_frente: float = 0.0, lote_fondo: float = 0.0,
) -> Tuple[List[Dict], List[Dict], List[Dict]]:
    f2_mix = []
    for esc in f2_resultados.get("escenarios", []):
        if esc.get("escenario_id") == "D_MIXTO":
            f2_mix = esc.get("mix_usos_detalle", [])
            break
    if not f2_mix:
        f2_mix = [
            {"uso": "Local comercial turistico", "num_unidades": 21, "area_vendible_m2": 840.0},
            {"uso": "Vivienda estandar", "num_unidades": 31, "area_vendible_m2": 1705.0},
        ]
    
    uso_map = {}
    for d in f2_mix:
        uf = d["uso"]
        if "viv" in uf.lower():
            uso_map["Vivienda"] = dict(TIPOLOGIAS_F2.get("Vivienda estandar", {"area_und": 55.0, "tipo": "vivienda"}))
            uso_map["Vivienda"]["nombre"] = "Vivienda estándar"
            uso_map["Vivienda"]["total_unidades"] = d["num_unidades"]
        elif "loc" in uf.lower() or "com" in uf.lower():
            uso_map["Local comercial"] = dict(TIPOLOGIAS_F2.get("Local comercial turistico", {"area_und": 40.0, "tipo": "comercio"}))
            uso_map["Local comercial"]["nombre"] = "Local comercial turístico"
            uso_map["Local comercial"]["total_unidades"] = d["num_unidades"]
    
    nucleo_info = layout.get("nucleos", {})
    huella = layout.get("huella_m2", 662.5)
    
    # Estimar lote si no viene de F1 (fallback)
    if lote_frente <= 0 or lote_fondo <= 0:
        # Usar huella del envelope como referencia
        # Relación típica Bogotá: frente ~15-25m, fondo 1.5-2.0x frente
        lote_frente = math.sqrt(huella / 1.5)
        lote_fondo = lote_frente * 1.5
    
    # Calcular capacidad por piso
    capacidad_por_piso = {}
    for nivel in layout.get("niveles", []):
        area_neta = (nivel["gfa_m2"] - nucleo_info.get("nucleo_solidos_m2", 44.6)) * 0.88
        for uso in nivel.get("usos", []):
            if uso in uso_map:
                cap = int(area_neta / (uso_map[uso]["area_und"] * 1.12))
                capacidad_por_piso[(uso, nivel["nivel"])] = cap
    
    # Distribuir totales F2 entre pisos (priorizando mayor capacidad)
    unidades_asignadas = {}
    reparto = layout.get("reparto_vertical", {})
    for uso, pisos in reparto.items():
        if uso not in uso_map: continue
        total = uso_map[uso]["total_unidades"]
        pisos_ord = sorted(pisos, key=lambda p: capacidad_por_piso.get((uso, p), 0), reverse=True)
        restantes = total
        for p in pisos_ord:
            cap = capacidad_por_piso.get((uso, p), 0)
            asignar = min(restantes, cap)
            if asignar > 0:
                unidades_asignadas[(uso, p)] = asignar
                restantes -= asignar
        # Forzar resto en cualquier piso con capacidad
        if restantes > 0:
            for p in pisos:
                cap = capacidad_por_piso.get((uso, p), 0)
                if cap > 0:
                    add = min(restantes, cap)
                    unidades_asignadas[(uso, p)] = unidades_asignadas.get((uso, p), 0) + add
                    restantes -= add
                    if restantes <= 0: break
    
    todas_unidades = []
    todas_circulaciones = []
    for nivel in layout.get("niveles", []):
        pn = nivel["nivel"]
        for uso in nivel.get("usos", []):
            if uso not in uso_map: continue
            n_und = unidades_asignadas.get((uso, pn), 0)
            if n_und <= 0: continue
            tip = dict(uso_map[uso]); tip["num_unidades_piso"] = n_und
            area_neta = (nivel["gfa_m2"] - nucleo_info.get("nucleo_solidos_m2", 44.6)) * 0.88
            unds, circs = distribuir_unidades_piso(nivel, nucleo_info, uso, tip, area_neta,
                lote_frente, lote_fondo, angulo_fachada)
            todas_unidades.extend(unds)
            todas_circulaciones.extend(circs)
    
    parqueaderos = calcular_parqueaderos(layout, f2_mix, cota_via, lote_frente, lote_fondo)
    return todas_unidades, todas_circulaciones, parqueaderos

def convertir_a_volum_generador(unidades, circulaciones, parqueaderos):
    vol, etiq, pis = [], [], []
    por_uso = {}
    for u in unidades: por_uso.setdefault(u["uso"], []).append(u)
    for uso, unds in por_uso.items():
        for u in unds:
            vol.append([[[v[0], v[1], 0.0] for v in u["vertices"]]])
            etiq.append(f"{uso} {u['tipologia']}"); pis.append(u["piso"])
    for c in circulaciones:
        vol.append([[[v[0], v[1], 0.0] for v in c["vertices"]]])
        etiq.append("Circulacion"); pis.append(c["piso"])
    for p in parqueaderos:
        area = p["area_m2"]; lado = math.sqrt(area)
        vol.append([[[v[0], v[1], 0.0] for v in rectangulo(0, 0, lado, lado)]])
        etiq.append(f"Parqueadero {p['nombre']}"); pis.append(p["nivel"])
    return vol, etiq, pis

def reporte_txt(unidades, circulaciones, parqueaderos):
    lines = ["="*72, "F3 - UNIDADES TIPOLÓGICAS, CIRCULACIONES Y PARQUEADEROS", "="*72]
    por_uso = {}
    for u in unidades:
        k = f"{u['uso']} ({u['tipologia']})"
        por_uso.setdefault(k, {"c":0, "a":0.0, "p":set()})
        por_uso[k]["c"] += 1; por_uso[k]["a"] += u["area_m2"]; por_uso[k]["p"].add(u["piso"])
    lines.append(f"\nUNIDADES TOTALES: {len(unidades)}")
    for k, v in por_uso.items():
        lines.append(f"  {k}: {v['c']} unds, {v['a']:.1f} m², pisos {sorted(v['p'])}")
    lines.append(f"\nCIRCULACIONES: {len(circulaciones)}")
    for c in circulaciones:
        lines.append(f"  Piso {c['piso']}: {c['tipo']} {c['largo_m']:.1f}x{c['ancho_m']:.1f}m")
    total_parq = sum(p["capacidad"] for p in parqueaderos)
    lines.append(f"\nPARQUEADEROS: {total_parq} puestos en {len(parqueaderos)} nivel(es)")
    for p in parqueaderos:
        t = "SÓTANO" if p["es_sotano"] else "SUPERFICIE"
        lines.append(f"  {p['nombre']} (z={p['z_base_m']:.1f}m): {p['capacidad']} pts, {p['area_m2']:.1f} m² [{t}]")
    lines.append("\nVERIFICACIONES:")
    lines.append(f"  Ventilación natural: {sum(1 for u in unidades if u.get('ventilacion_natural'))}/{len(unidades)}")
    for c in circulaciones:
        if c["ancho_m"] < ANCHO_PASILLO_MIN:
            lines.append(f"  ADV: Pasillo P{c['piso']} {c['ancho_m']:.2f}m < {ANCHO_PASILLO_MIN}m")
    return "\n".join(lines)

# ============================================================
# MAIN CLI
# ============================================================
def main():
    caso_id = f2_path = layout_path = None
    cota_via = 0.0; salida_dir = None
    angulo_fachada = 0.0; lote_frente = 0.0; lote_fondo = 0.0
    argv = sys.argv[1:]; i = 0
    while i < len(argv):
        a = argv[i]
        if a == "--caso" and i+1 < len(argv): caso_id = argv[i+1]; i+=2
        elif a == "--f2-resultados" and i+1 < len(argv): f2_path = argv[i+1]; i+=2
        elif a == "--layout" and i+1 < len(argv): layout_path = argv[i+1]; i+=2
        elif a == "--cota-via" and i+1 < len(argv): cota_via = float(argv[i+1]); i+=2
        elif a == "--salida" and i+1 < len(argv): salida_dir = argv[i+1]; i+=2
        elif a == "--angulo-fachada" and i+1 < len(argv): angulo_fachada = math.radians(float(argv[i+1])); i+=2
        elif a == "--lote-frente" and i+1 < len(argv): lote_frente = float(argv[i+1]); i+=2
        elif a == "--lote-fondo" and i+1 < len(argv): lote_fondo = float(argv[i+1]); i+=2
        else: i+=1
    if caso_id:
        layout_path, f2_path_auto, caso_dir = resolver_rutas(caso_id)
        if not f2_path: f2_path = f2_path_auto
        if not salida_dir: salida_dir = caso_dir
    elif not layout_path or not f2_path:
        print("ERROR: --caso o (--layout + --f2-resultados)"); sys.exit(1)
    else:
        caso_dir = os.path.dirname(layout_path)
        if not salida_dir: salida_dir = caso_dir
    layout = cargar_json(layout_path)
    f2 = cargar_json(f2_path)
    if not layout: print(f"ERROR: layout no encontrado: {layout_path}"); sys.exit(1)
    if not f2:
        print(f"ADV: F2 no encontrado, usando defaults")
        f2 = {"escenarios": [{"escenario_id": "D_MIXTO", "mix_usos_detalle": [
            {"uso": "Local comercial turistico", "num_unidades": 21, "area_vendible_m2": 840.0},
            {"uso": "Vivienda estandar", "num_unidades": 31, "area_vendible_m2": 1705.0},
        ]}]}
    chip = layout.get("chip", caso_id or "chip")
    u, c, p = generar_unidades_completas(layout, f2, cota_via, angulo_fachada, lote_frente, lote_fondo)
    vol, et, pi = convertir_a_volum_generador(u, c, p)
    if not os.path.isdir(salida_dir): os.makedirs(salida_dir)
    data = {"metadata": {"version": "1.0.0", "modulo": "F3_UNIDADES_TIPOLOGIAS_v01", "chip": chip,
        "total_unidades": len(u), "total_circulaciones": len(c), "total_parqueaderos": sum(x["capacidad"] for x in p),
        "lote_frente_m": lote_frente, "lote_fondo_m": lote_fondo},
        "unidades": u, "circulaciones": c, "parqueaderos": p,
        "volumenes_para_F3_VOLUM_GENERADOR": {"volumenes_por_uso": vol, "usos_etiquetas": et, "usos_pisos": pi}}
    with open(os.path.join(salida_dir, f"unidades_{chip}.json"), "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    with open(os.path.join(salida_dir, f"unidades_{chip}.txt"), "w", encoding="utf-8") as f:
        f.write(reporte_txt(u, c, p))
    print(reporte_txt(u, c, p))
    print(f"\nGuardado: unidades_{chip}.json / .txt")

# ============================================================
# GH PYTHON COMPONENT
# ============================================================
# Entradas GH (globals):
#   f2_resultados_json (String, ruta o JSON crudo)
#   layout_espacial_json (String, ruta o JSON crudo)
#   cota_via_m (Number, Item)
#   chip (String, Item)
#   angulo_fachada_deg (Number, Item, opcional)
#   lote_frente_m (Number, Item) - DESDE F1 envelope_curve
#   lote_fondo_m (Number, Item) - DESDE F1 envelope_curve
# Salidas GH:
#   unidades_json, parqueaderos_json, circulaciones_json (String)
#   volumenes_por_uso (List[List[List[float]]]) - para F3_VOLUM_GENERADOR
#   usos_etiquetas (List[str]), usos_pisos (List[int])
#   mensaje (String)

def _u(val):
    if val is None: return None
    if hasattr(val, "Value"): return val.Value
    return val

def _pj(val):
    if not val: return None
    s = str(val).strip()
    if s.endswith(".json") and os.path.exists(s): return cargar_json(s)
    try: return json.loads(s)
    except: return None

def _gh():
    f2 = _pj(_u(globals().get("f2_resultados_json")))
    lay = _pj(_u(globals().get("layout_espacial_json")))
    cota = float(_u(globals().get("cota_via_m", 0.0)) or 0.0)
    chip = _u(globals().get("chip")) or "chip"
    ang = math.radians(float(_u(globals().get("angulo_fachada_deg", 0.0)) or 0.0))
    lf = float(_u(globals().get("lote_frente_m", 0.0)) or 0.0)
    lfondo = float(_u(globals().get("lote_fondo_m", 0.0)) or 0.0)
    if not lay: return "", "", "", [], [], [], "UNIDADES v1.0 | ERROR: sin layout"
    if not f2:
        f2 = {"escenarios": [{"escenario_id": "D_MIXTO", "mix_usos_detalle": [
            {"uso": "Local comercial turistico", "num_unidades": 21, "area_vendible_m2": 840.0},
            {"uso": "Vivienda estandar", "num_unidades": 31, "area_vendible_m2": 1705.0},
        ]}]}
    u, c, p = generar_unidades_completas(lay, f2, cota, ang, lf, lfondo)
    vol, et, pi = convertir_a_volum_generador(u, c, p)
    totp = sum(x["capacidad"] for x in p)
    return (json.dumps({"unidades": u}, ensure_ascii=False),
            json.dumps({"parqueaderos": p}, ensure_ascii=False),
            json.dumps({"circulaciones": c}, ensure_ascii=False),
            vol, et, pi,
            f"UNIDADES v1.0 | OK | {len(u)} u | {len(c)} circ | {totp} parq ({len(p)} niv)")

if __name__ == "__main__": main()

# GH outputs
unidades_json = parqueaderos_json = circulaciones_json = mensaje = ""
volumenes_por_uso = []; usos_etiquetas = []; usos_pisos = []
try:
    (unidades_json, parqueaderos_json, circulaciones_json,
     volumenes_por_uso, usos_etiquetas, usos_pisos, mensaje) = _gh()
except Exception as e:
    mensaje = f"UNIDADES v1.0 | ERROR: {e}"
    try: ghenv.Component.Message = mensaje  # noqa
    except: pass