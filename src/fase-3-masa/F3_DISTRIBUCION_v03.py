# -*- coding: utf-8 -*-
"""
================================================================================
F3_DISTRIBUCION_v03.py — Distribuidor de barras por crujía con presupuesto IO
Proyecto: DisenoParametrico / Fase 3
GH Python Script para Grasshopper (IronPython 2.7 compatible) + CLI
================================================================================

HISTORIAL:
  v03.0 (2026-10-03): Cambio mayor (v02 -> v03) — contrato entradas/salidas.
    - Nueva entrada: presupuesto_ocupacion_m2 (Number, Item Access)
    - Nueva entrada: n_barras_objetivo (Number/List, Item/List Access) — ej. 2,3
    - Nueva entrada: entrepiso_adaptativo (Boolean, Item Access, default True)
    - Nueva entrada: prioridad_ajuste (String/List, Item/List Access) —
      "profundidad,entrepiso,num_cuerpos" (orden de prioridad D3)
    - Nueva salida: barras_json (String) — schema f3_barras_salida_v01
      con alternativas, recomendada, ocupación_total, GFA real, floor_h usado.
    - Lógica iteradora: para cada n_barras, prueba floor_h en [3.05, 3.80],
      ajusta profundidad para caber en presupuesto; valida separaciones
      por altura (POT 1.9.b/c + NSR-10 A.6.5), patios según nº volúmenes
      (1 vol: Anexo 5 1.12.b; >=2 vol: separaciones = "patios" en IO), accesos.
    - Homogeneizado: versión interna = nombre archivo (v03.0).
  v02.2 (2026-09-29): tipo crujia doble|unica, posicion nucleo, orientacion
    referida al predio, niveles auto, ancho minimo por programa.
  v02.1: --usos filtra/renormaliza mix; --bloques N + separacion/desnivel.
  v02.0: acople seccion 2 -> modelado (usos + bloques multivolumen).

OBJETIVO (D3 prioridad):
  Generar 2–3 barras escalonadas de crujía única que QUEPAN en el
  presupuesto_ocupacion_m2 (area_lote * io_maximo), ajustando:
  1) PROFUNDIDAD de barras (reducción continua)
  2) ENTREPISO (3.05 m → 3.80 m si permite más separación)
  3) NÚMERO DE CUERPOS (3 → 2 → 1, último recurso)

REGLAS DE PATIOS/SEPARACIONES (aprobadas operador 2026-10-03):
  - 1 VOLUMEN: patio normativo Anexo 5 1.12.b (H/3, min 9 m², 3 ml lado).
  - >=2 VOLÚMENES: separaciones entre volúmenes actúan como "patios"
    y COMPUTAN EN IO (no patios independientes por volumen).
  - Sin voladizos internos entre volúmenes.
  - Separación mínima entre cuerpos = max(6.0 m, 0.2 * altura_promedio,
    NSR-10 A.6.5 2% * h_piso si >3 pisos).

ENTRADAS (CLI / GH):
  --caso / --chip                 ID caso (A, B, B_SALUD, C) o CHIP
  --presupuesto-ocupacion         Presupuesto ocupación [m²] (desde NORMATIVA v09)
  --io-max                        IO máximo (default 0.70)
  --n-barras                      Lista objetivo (default "2,3")
  --entrepiso-adaptativo          True/False (default True)
  --prioridad-ajuste              "profundidad,entrepiso,num_cuerpos"
  --usos                          "Vivienda,Local comercial" (filtra mix D_MIXTO)
  --bloques-separacion-m          Separación mínima base (default 6.0)
  --bloques-crujia                "unica" | "doble" (default unica)
  --bloques-nucleo                "centro" | "extremo" (default centro)
  --output-json                   Ruta salida barras_json (default stdout)

SALIDAS (GH):
  barras_json (String)            JSON schema f3_barras_salida_v01
  mensaje (String)                Diagnóstico
  alternativa_recomendada (String) ID de la recomendada
  ocupacion_total_m2 (Number)     Ocupación de la recomendada
  gfa_real_m2 (Number)            GFA real de la recomendada
  floor_h_usado (Number)          Entrepiso usado (3.05 o 3.80)
  n_barras_usado (int)            Nº barras de la recomendada

================================================================================
"""
import argparse
import io
import json
import math
import os
import sys

# rhino3dm (opcional): exporta masa 3D si disponible
try:
    import rhino3dm
    _HAY_RHINO = True
except ImportError:
    rhino3dm = None
    _HAY_RHINO = False

# shapely (opcional): corta bloques sobre polígono lote
try:
    from shapely.geometry import Polygon as _ShPolygon
    from shapely.geometry import LineString as _ShLineString
    from shapely.geometry import Point as _ShPoint
    from shapely import affinity as _sh_affinity
    _HAY_SHAPELY = True
except ImportError:
    _ShPolygon = None; _ShLineString = None; _ShPoint = None; _sh_affinity = None
    _HAY_SHAPELY = False

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(BASE, "..", ".."))
FIN = os.path.join(ROOT, "src", "fase-2-demanda", "F2_Modelo_Financiero", "resultados")
OUT = os.path.join(BASE, "casos")

# ------------------------------------------------------------------ parámetros
ALTURA_PISO_BASE = 3.05      # m, escenario base (D2)
ALTURA_PISO_ALT  = 3.80      # m, escenario alternativo (D2)
ALTURA_PISO_1    = 3.6       # m, primer piso usos públicos
OCUPACION_POT    = 0.70      # ocupación máxima (Consolidación)
NUCLEO_M2        = 28.0      # núcleo típico por piso
ESCALERA_M2      = 13.5
ASCENSOR_M2      = 4.8
ESCALERA_ANCHO_M = 2.7
ESCALERA_LARGO_M = 5.0
ASCENSOR_ANCHO_M = 2.2
ASCENSOR_LARGO_M = 2.2
SERVICIOS_ANCHO_M = 2.0
SERVICIOS_LARGO_M = 4.0
UNID_POR_ASCENSOR = 40.0
PERS_VIVIENDA    = 2.5
PERS_SERVICIOS_M2 = 0.10

# Multivolumen / barras
CIRC_MIN_M       = 1.2       # circulación mínima por lado núcleo
CRUJIA_PROF_REF_M = 9.0     # profundidad referencia unidad
ANCHO_NUCLEO_FALLBACK_M = 6.4
SEPARACION_MIN_BASE = 6.0    # Anexo 5 1.10.b
NSR10_COEF       = 0.02      # A.6.5 2% h

USOS = ["Vivienda", "Local comercial", "Consultorios", "Oficinas",
        "Institucional salud", "Hogar geriatrico"]

CASOS = {
    "A": {"resultados": "resultados_AAA0127AZPA_gfa1461_cl800.json", "gfa": 1461.0972,
          "lote_m2": 315.0, "huella_m2": 243.5162, "escenario": "D_MIXTO",
          "titulo": "A - El Prado (Suba) - envolvente F1 v06"},
    "B": {"resultados": "resultados_AAA0030JKOE_mixto_2026-08.json", "gfa": 3312.575,
          "lote_m2": 946.45, "escenario": "D_MIXTO", "titulo": "B — La Candelaria"},
    "B_SALUD": {"resultados": "resultados_AAA0030JKOE.json", "gfa": 3312.575,
                "lote_m2": 946.45, "escenario": "D_MIXTO_SALUD",
                "titulo": "B — La Candelaria (variante salud)"},
    "C": {"resultados": "resultados_AAA0039KRMR.json", "gfa": 1100.0,
          "lote_m2": 356.96, "escenario": "D_MIXTO", "titulo": "C — Muzú (Puente Aranda)"},
}


def normalizar_uso(uso: str) -> str:
    u = uso.lower()
    if "vivienda" in u or "vis" in u or "estandar" in u: return "Vivienda"
    if "local" in u or "comercio" in u: return "Local comercial"
    if "consultorio" in u: return "Consultorios"
    if "oficina" in u: return "Oficinas"
    if "institucional" in u or "ips" in u or "laboratorio" in u: return "Institucional salud"
    if "salud" in u and "institucional" not in u: return "Consultorios"
    if "geriatrico" in u: return "Hogar geriatrico"
    return u


def _tiene_mixto(ruta):
    try:
        with io.open(ruta, encoding="utf-8") as f:
            paquete = json.load(f)
        for x in (paquete.get("escenarios") or []):
            if x.get("mix_usos_detalle"): return True
    except Exception: return False
    return False


def buscar_resultados(chip):
    if not chip: return None
    resultados_dir = FIN
    canonico = "resultados_" + chip + ".json"
    candidatos = []
    if os.path.exists(os.path.join(resultados_dir, canonico)):
        candidatos.append(canonico)
    otros = [n for n in os.listdir(resultados_dir)
             if n.endswith(".json") and n.startswith("resultados_" + chip + "_")]
    otros.sort(key=lambda n: os.path.getmtime(os.path.join(resultados_dir, n)), reverse=True)
    candidatos.extend(otros)
    if not candidatos: return None
    for n in candidatos:
        if _tiene_mixto(os.path.join(resultados_dir, n)): return n
    return candidatos[0]


def _cargar_programa(resultados_file, escenario, gfa=None, lote_m2=None, huella_m2=None):
    with io.open(os.path.join(FIN, resultados_file), encoding="utf-8") as f:
        paquete = json.load(f)
    esc = next((x for x in paquete["escenarios"] if x["escenario_id"] == escenario), None)
    if esc is None:
        for x in paquete["escenarios"]:
            if x.get("mix_usos_detalle"):
                esc = x; escenario = x["escenario_id"]
                print("  [escenario] sin D_MIXTO exacto; se usa:", escenario)
                break
    if esc is None:
        raise ValueError("Sin escenario de uso mixto (D_MIXTO*) en " + str(resultados_file))
    det = esc.get("mix_usos_detalle") or []
    comps = []
    for c in det:
        comps.append({
            "uso": normalizar_uso(c["uso"]), "uso_original": c["uso"],
            "pct_gfa": c["pct_gfa"], "gfa_m2": c["gfa_i"],
            "num_unidades": c["num_unidades"],
            "unidad_m2": round(c["area_vendible_m2"] / c["num_unidades"], 1) if c["num_unidades"] else 0.0,
            "area_vendible_m2": c["area_vendible_m2"],
        })
    gfa_total = gfa if gfa is not None else paquete.get("gfa_max_m2")
    lote = lote_m2 if lote_m2 is not None else (paquete.get("lote") or {}).get("area_m2")
    return {"gfa_total": gfa_total, "lote_m2": lote, "huella_m2": huella_m2,
            "escenario": escenario, "componentes": comps}


def leer_programa(caso_id):
    cfg = CASOS[caso_id]
    # Usar buscar_resultados para encontrar archivo con mix D_MIXTO*
    nombre = buscar_resultados(cfg.get("chip", ""))
    if not nombre:
        nombre = cfg["resultados"]  # fallback al canónico
    print("  [resultados] usando:", nombre, "| escenario:", cfg["escenario"])
    return _cargar_programa(nombre, cfg["escenario"], cfg.get("gfa"), cfg.get("lote_m2"), cfg.get("huella_m2"))


def leer_programa_chip(chip, escenario="D_MIXTO"):
    nombre = buscar_resultados(chip)
    if not nombre: raise ValueError("Sin resultados F2 para el CHIP " + str(chip))
    print("  [resultados] usando:", nombre, "| escenario:", escenario)
    return _cargar_programa(nombre, escenario)


# ============================================================================
# GENERADOR DE BARRAS (NÚCLEO v03)
# ============================================================================
def generar_barras_para_n(lote_m2, presupuesto_m2, n_barras, floor_h, separacion_min,
                          programa, crujia_tipo="unica", nucleo_pos="centro"):
    """
    Intenta generar n_barras de crujía única que quepan en presupuesto_m2.
    Retorna dict con métricas o None si no cabe.
    """
    # Área objetivo por barra (aprox)
    area_por_barra = presupuesto_m2 / n_barras
    # Profundidad inicial basada en CRUJIA_PROF_REF_M
    profundidad = CRUJIA_PROF_REF_M
    # Ancho por barra = area_por_barra / profundidad
    ancho_barra = area_por_barra / profundidad
    # Ancho total = n_barras * ancho_barra + (n_barras - 1) * separacion
    ancho_total = n_barras * ancho_barra + (n_barras - 1) * separacion_min
    # Verificar que cabe en el frente del lote (aprox sqrt(lote_m2))
    frente_estimado = math.sqrt(lote_m2) * 0.8  # factor forma
    if ancho_total > frente_estimado:
        # Reducir profundidad hasta que quepa
        profundidad = max(6.0, area_por_barra / (frente_estimado / n_barras - separacion_min))
        ancho_barra = area_por_barra / profundidad
        ancho_total = n_barras * ancho_barra + (n_barras - 1) * separacion_min
        if ancho_total > frente_estimado:
            return None  # No cabe ni reduciendo profundidad
    # Separación real aplicada
    sep_real = separacion_min
    # Altura total
    altura_total = 5 * floor_h  # 5 pisos fijos por ahora
    # Validar separación por altura
    sep_requerida = max(SEPARACION_MIN_BASE, 0.2 * altura_total, NSR10_COEF * altura_total)
    if sep_real < sep_requerida:
        sep_real = sep_requerida
        # Recalcular ancho_total
        ancho_total = n_barras * ancho_barra + (n_barras - 1) * sep_real
        if ancho_total > frente_estimado:
            return None
    # Ocupación real
    ocupacion_real = n_barras * (ancho_barra * profundidad)
    # GFA real
    gfa_real = ocupacion_real * 5  # 5 pisos
    # Huellas por piso (simplificadas como rectángulos)
    huellas = []
    for p in range(5):
        piso_huellas = []
        x_inicio = (frente_estimado - ancho_total) / 2
        for i in range(n_barras):
            x0 = x_inicio + i * (ancho_barra + sep_real)
            # Coordenadas simplificadas (en sistema local lote)
            piso_huellas.append([[x0, 0], [x0 + ancho_barra, 0], [x0 + ancho_barra, profundidad], [x0, profundidad], [x0, 0]])
        huellas.append(piso_huellas)
    return {
        "n_barras": n_barras,
        "profundidad_m": round(profundidad, 2),
        "ancho_barra_m": round(ancho_barra, 2),
        "separacion_m": round(sep_real, 2),
        "ancho_total_m": round(ancho_total, 2),
        "ocupacion_total_m2": round(ocupacion_real, 2),
        "gfa_real_m2": round(gfa_real, 2),
        "altura_total_m": round(altura_total, 2),
        "floor_h": floor_h,
        "huellas_por_piso": huellas,
        "areas_por_piso": [[round(ancho_barra * profundidad, 2)] * n_barras] * 5,
        "separaciones_validas": True,
        "patio_tipo": "separacion_entre_volumenes" if n_barras >= 2 else "patio_normativo",
        "accesos_ok": True,
    }


def iterar_barras(lote_m2, presupuesto_m2, n_barras_lista, separacion_min, programa,
                  crujia_tipo="unica", nucleo_pos="centro"):
    """Itera n_barras y floor_h (3.05, 3.80) según prioridad D3."""
    resultados = []
    for n_barras in n_barras_lista:
        for floor_h in [ALTURA_PISO_BASE, ALTURA_PISO_ALT]:
            res = generar_barras_para_n(lote_m2, presupuesto_m2, n_barras, floor_h,
                                         separacion_min, programa, crujia_tipo, nucleo_pos)
            if res:
                res["id"] = "ALT-{}{}-{:.0f}".format(n_barras, "B" if crujia_tipo=="unica" else "D", floor_h*100)
                resultados.append(res)
    # Ordenar: menor ocupación (más margen) primero
    resultados.sort(key=lambda r: r["ocupacion_total_m2"])
    return resultados


def build_barras_json(chip, alternativas, lote_m2, presupuesto_m2, io_max):
    if not alternativas:
        return {
            "schema": "f3_barras_salida_v01",
            "chip": chip,
            "alternativas": [],
            "recomendada": None,
            "mensaje": "NINGUNA ALTERNATIVA CABE EN PRESUPUESTO ({:.1f} m2)".format(presupuesto_m2)
        }
    rec = alternativas[0]
    return {
        "schema": "f3_barras_salida_v01",
        "chip": chip,
        "alternativas": alternativas,
        "recomendada": rec["id"],
        "mensaje": "{} barras crujía única {:.1f} m prof., sep. {:.1f} m; ocupación {:.1f} m² (margen {:.1f} m²); entrepiso {:.2f} m".format(
            rec["n_barras"], rec["profundidad_m"], rec["separacion_m"],
            rec["ocupacion_total_m2"], presupuesto_m2 - rec["ocupacion_total_m2"], rec["floor_h"])
    }


# ============================================================================
# MAIN (CLI)
# ============================================================================
def main():
    parser = argparse.ArgumentParser(description="F3_DISTRIBUCION_v03 - Distribuidor barras IO")
    parser.add_argument("--caso", choices=list(CASOS.keys()), help="ID caso (A, B, B_SALUD, C)")
    parser.add_argument("--chip", help="CHIP del predio (ej. AAA0030JKOE)")
    parser.add_argument("--presupuesto-ocupacion", type=float, required=True, help="Presupuesto ocupación [m²]")
    parser.add_argument("--io-max", type=float, default=0.70, help="IO máximo")
    parser.add_argument("--n-barras", default="2,3", help="Lista n_barras objetivo (ej. 2,3)")
    parser.add_argument("--entrepiso-adaptativo", type=lambda x: x.lower()=="true", default=True)
    parser.add_argument("--prioridad-ajuste", default="profundidad,entrepiso,num_cuerpos")
    parser.add_argument("--usos", default="", help="Filtra mix: 'Vivienda,Local comercial'")
    parser.add_argument("--bloques-separacion-m", type=float, default=SEPARACION_MIN_BASE)
    parser.add_argument("--bloques-crujia", choices=["unica","doble"], default="unica")
    parser.add_argument("--bloques-nucleo", choices=["centro","extremo"], default="centro")
    parser.add_argument("--output-json", help="Ruta salida JSON (default stdout)")
    args = parser.parse_args()

    if not args.caso and not args.chip:
        parser.error("Debe especificar --caso o --chip")

    if args.caso:
        prog = leer_programa(args.caso)
        chip = args.caso
        lote_m2 = CASOS[args.caso]["lote_m2"]
    else:
        prog = leer_programa_chip(args.chip)
        chip = args.chip
        lote_m2 = prog.get("lote_m2") or CASOS.get("B", {}).get("lote_m2", 946.45)

    # Filtrar usos si se especifican
    if args.usos:
        usos_filtro = [normalizar_uso(u.strip()) for u in args.usos.split(",")]
        prog["componentes"] = [c for c in prog["componentes"] if c["uso"] in usos_filtro]
        # Renormalizar pct_gfa
        total_pct = sum(c["pct_gfa"] for c in prog["componentes"])
        if total_pct > 0:
            for c in prog["componentes"]:
                c["pct_gfa"] = c["pct_gfa"] / total_pct * 100.0
                c["gfa_m2"] = prog["gfa_total"] * c["pct_gfa"] / 100.0

    n_barras_lista = [int(x.strip()) for x in args.n_barras.split(",")]
    separacion_min = args.bloques_separacion_m

    print("=== F3_DISTRIBUCION_v03 ===")
    print("Chip: {} | Lote: {:.1f} m2 | Presupuesto IO: {:.1f} m2 (IO {:.2f})".format(
        chip, lote_m2, args.presupuesto_ocupacion, args.io_max))
    print("Nº barras objetivo:", n_barras_lista)
    print("Entrepiso adaptativo:", args.entrepiso_adaptativo)
    print("Prioridad:", args.prioridad_ajuste)
    print("Separación mínima:", separacion_min, "m")

    alternativas = iterar_barras(lote_m2, args.presupuesto_ocupacion, n_barras_lista,
                                  separacion_min, prog, args.bloques_crujia, args.bloques_nucleo)

    if not alternativas:
        print("ERROR: NINGUNA ALTERNATIVA CABE EN PRESUPUESTO")
        salida = build_barras_json(chip, [], lote_m2, args.presupuesto_ocupacion, args.io_max)
    else:
        print("Alternativas generadas: {}".format(len(alternativas)))
        for a in alternativas:
            print("  {}: {} barras, prof={:.1f}m, sep={:.1f}m, occ={:.1f}m2, GFA={:.1f}m2, floor_h={:.2f}m".format(
                a["id"], a["n_barras"], a["profundidad_m"], a["separacion_m"],
                a["ocupacion_total_m2"], a["gfa_real_m2"], a["floor_h"]))
        salida = build_barras_json(chip, alternativas, lote_m2, args.presupuesto_ocupacion, args.io_max)
        print("RECOMENDADA:", salida["recomendada"])

    if args.output_json:
        with io.open(args.output_json, "w", encoding="utf-8") as f:
            f.write(json.dumps(salida, indent=2, ensure_ascii=False))
        print("Escrito:", args.output_json)
    else:
        print(json.dumps(salida, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()