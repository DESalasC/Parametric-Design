# -*- coding: utf-8 -*-
"""
================================================================================
F1_ETAPA2_NORMATIVA_v10.py - Retiros + Patios + Índices + Empates Laterales
                         + Retiro Patrimonial por Primera Franja de Fachada
                         + Cota de Terreno y Altura Máxima sobre Cota
Proyecto: DiseñoParametrico / Fase 1
GH Python Script para Grasshopper (IronPython 2.7 compatible)
Fecha de generacion: 2026-10-26
================================================================================

HISTORIAL DE VERSIONES:
  v10.0 (2026-10-26): Cambio mayor (v09 -> v10) — reglas de empates laterales
    y retiro patrimonial por primera franja de fachada.
    - Nueva entrada: retiro_patrimonial_m (Number, Item) — retiro lateral
      especial (3.0 m) para lados con vecino patrimonio nivel 2.
    - Nueva entrada: franja_patrimonial_longitud_m (Number, Item) — longitud
      de la primera franja de fachada sujeta al retiro patrimonial.
    - Nueva entrada: vecino_patrimonio_por_lado (String, Item) — JSON con
      lados marcados como patrimonio: [{"lado_id":0,"nivel":2,"patrimonio":true}]
    - Nueva entrada: construccion_no_patrimonio_exenta (String, Item) — JSON
      con volumenes no patrimoniales exentos: [{"lado_id":0,"exenta":true}]
    - Nueva entrada: altura_vecino_derecha_m (Number, Item) — altura del
      vecino derecho para empate diferencial (ej. 11.40 m).
    - Nueva entrada: empate_lateral_derecha_m (Number, Item) — distancia de
      empate específica para el lado derecho (pendiente de criterio curaduria).
    - Nueva entrada: cota_terreno_central_m (Number, Item) — cota del terreno
      en centro del lote (ej. +0.90 m) para reconciliar con altura maxima 10 m.
    - NORMATIVA ahora distingue lados izquierdo y derecho con alturas propias
      en lugar de altura_vecinos_m global.
    - El retiro patrimonial aplica solo a la primera franja de fachada del
      lado marcado como patrimonio; el resto del lindero usa reglas generales.
    - La construccion no patrimonial al fondo queda exenta de retiros.
    - La altura maxima se valida contra cota_terreno_central_m + 10.00 m.
  v09.0 (2026-10-03): Cambio mayor (v08 -> v09) — contrato de entradas/salidas.
    - Nueva entrada opcional: barras_json (String, Item Access) — huellas
      aprobadas desde F3_DISTRIBUCION_v03.
    - Nuevas salidas: presupuesto_ocupacion_m2, ocupacion_aprobada_m2,
      gfa_aprobado_m2, envelope_aprobado_por_piso.
    - Validador: si barras_json presente, certifica ocupacion_total <=
      presupuesto (+ TOLERANCIA**2) y emite ocupacion_aprobada/gfa_aprobado/
      envelope_aprobado; desacopla "envolvente potencial" de "ocupacion
      aprobada".
    - Siempre expone presupuesto_ocupacion_m2 = area_lote * io_maximo.
  v08.5.2 (2026-10-01): IO real bloqueante, antejardin cero explícito, límite
    de pisos, booleanas sin areas ficticias, vecinos_intervalos_json (puente
    LADOS v06.7), recortes locales rectangulares.

REGLA DE VERSIONADO: la version general (v09 -> v10) SOLO cambia con cambios
mayores (contrato de entradas/salidas o algoritmo central); las iteraciones
internas se registran como subversiones v10.x en este encabezado.

CALCULO:
  1. Descontar retiro FRONTAL (antejardin) del lado frontal del lote
  2. NO descontar retiro en lados EspacioPublico (0 m)
  3. Lateral: 0 m en tipologia CONTINUA; en AISLADA, 1/5 de la altura de la
     edificacion, minimo 4,00 m (Anexo 5 POT, SECCION 1.9.b)
  4. Retiro patrimonial: si lado tiene vecino_patrimonio=true y se encuentra
     dentro de franja_patrimonial_longitud_m desde el frente, aplicar
     retiro_patrimonial_m (3.0 m) y respetar altura del edificio patrimonial.
  5. Construccion no patrimonial al fondo: exenta de retiros si
     construccion_no_patrimonio_exenta=true para ese lado.
  6. Posterior: tabla Consolidacion por pisos (Anexo 5 POT, SECCION 5.4.b);
     con empate volumetrico (vecino posterior 3+ pisos) retiro posterior = 0
  7. Restar el patio (desde vertice N) del perimetro restante (Boolean Diff)
  8. Calcular pisos base (Decreto 555/2021) y aplicar PISO ADICIONAL
  9. ESCALONAMIENTO EN PISOS SUPERIORES (Anexo 5 SECCION 1.9.c + NSR-10 A.6.5):
     retiro lateral = max(1/5 x altura desde nivel de empate, minimo empate,
     separacion sismica 2% x h). Solo si hay lado Posterior; si no, solo sismica.
     Para lado derecho con altura_vecino_derecha_m definida, usar esa altura
     en lugar de altura_vecinos_m global.
  10. Calcular GFA ESCALONADO = suma de areas de envelopes por piso (Fase 2)
      y emitir envelope_por_piso para Fase 3 (masa escalonada).
  11. VOLADIZOS (Anexo 5 SECCION 1.13.b): solo frontal, pisos != 1,
      segun perfil vial.
  12. VECINOS CON ALTURAS VARIABLES POR LATERAL (v08): entrada
      vecinos_por_lado_json o vecinos_intervalos_json (puente LADOS v06.7+).
  13. VALIDADOR DE BARRAS (v09): entrada barras_json opcional con huellas
      propuestas; si presente, valida ocupacion_total <=
      presupuesto_ocupacion_m2 y emite ocupacion/GFA/envelope APROBADOS.
  14. Cota de terreno: altura_total_validada = cota_terreno_central_m +
      pisos_finales * floor_h; debe ser <= cota_terreno_central_m + 10.00 m.

NORMATIVA APLICABLE:
  - Decreto 555 de 2021 (POT Bogota) — rangos de edificabilidad, IO, IC.
  - Decreto 466/2024 (Anexo 5 POT) — SECCION 1.9.b (lateral aislada),
    SECCION 1.9.c (empate volumetrico lateral), SECCION 5.4.b (posterior
    consolidacion), SECCION 1.12.b (patio iluminacion/ventilacion),
    SECCION 1.13.b (voladizos).
  - NSR-10 — Titulo A, seccion A.6.5 (separacion sismica 2% x h).
  - Nota N del PZCB — altura maxima 10.00 m confirmada por IDPC
    (visita fisica 2026-10-26) para CHIP AAA0030JKOE.

ENTRADAS:
  lot_polygon (Curve)              - Lote simplificado (Item)
  sides_table_json (String)        - Clasificación de lados (F1_ETAPA2_LADOS_v06+) (Item)
  patio_curves (Curve[])           - Patio(s) (F1_ETAPA2_PATIO_v03+) (List)
  altura_max_pot (Number)          - [OBSOLETO] Se mantiene para compatibilidad (Item)
  tratamiento (String)             - Tratamiento urbanistico (Item)
  rango_edificabilidad (String)    - Rango "1".."5" (Item)
  floor_height_user (Number)       - Altura entrepiso [m] (Item)
  io_maximo_user (Number)          - IO normativo (override) (Item)
  piso_adicional (bool)            - True si acoge incentivo normativo (Item)
  tipo_bonificacion (String)       - "NINGUNO" | "VIS" | "VIP" | "COMUNAL" |
                                     "EQUIPAMIENTO" | "EQUIPAMIENTO+COMUNAL" (Item)
  tipologia (String)               - "Continua" | "Aislada" (Item)
  ancho_via_m (Number)             - Ancho de via del frente [m] (Item)
  antejardin_m (Number)            - Override retiro frontal [m] (Item)
  empate_posterior_pisos (Number)  - Pisos vecino posterior (>=3 activa empate) (Item)
  altura_vecinos_m (Number)        - [v07] Altura global vecinos (fallback) (Item)
  empate_lateral_min_m (Number)    - [v07] Minimo aislamiento lateral empate (Item)
  voladizo_frontal_m (Number)      - [v07] Override voladizo frontal [m] (Item)
  vecinos_por_lado_json (String)   - [v08] Vecinos por lateral (formato legacy) (Item)
  frente_override_json (String)    - [v08.2] Override frente por cardinal (Item)
  reglamentacion_json (String)     - JSON reglamentacion (F1_ETAPA1_CONTEXTO) (Item)
  normativa_confirmada (bool)      - False default; True tras revision humana (Item)
  pisos_maximos_total (Number)     - Limite total de pisos incluyendo bonos (Item)
  vecinos_intervalos_json (String) - [v08.5] Puente LADOS v06.7+ (intervalos) (Item)
  barras_json (String)             - [v09] Huellas aprobadas desde F3_DISTRIBUCION_v03 (Item)
  retiro_patrimonial_m (Number)    - [v10] Retiro lateral patrimonio (3.0 m) (Item)
  franja_patrimonial_longitud_m(Number) - [v10] Longitud primera franja fachada (Item)
  vecino_patrimonio_por_lado(String) - [v10] JSON lados patrimonio nivel 1/2/3 (Item)
  construccion_no_patrimonio_exenta(String) - [v10] JSON volumenes no patrimonio exentos (Item)
  altura_vecino_derecha_m   (Number)   - [v10] Altura vecino derecho (ej. 11.40 m) (Item)
  altura_vecino_izquierda_m (Number) - [v10] Altura vecino izquierdo (ej. 11.40 m) (Item)
  empate_lateral_derecha_m  (Number)  - [v10] Distancia empate lado derecho (Item)
  empate_lateral_izquierda_m(Number) - [v10] Distancia empate lado izquierdo (Item)
  cota_terreno_central_m    (Number)   - [v10] Cota terreno centro lote (+0.90 m) (Item)

SALIDAS:
  envelope_curve (Curve/List)      - Huella PISO 1 (base, retiros + patio)
  envelope_por_piso (List)         - [v07] Curvas ocupacion POR PISO (potencial)
  retiros_por_piso (String)        - [v07] JSON desglose por piso
  gfa_total (Number)               - GFA ESCALONADO potencial (suma areas)
  ocupacion_real (Number)          - Ocupacion real (huella piso 1)
  io_maximo (Number)               - IO normativo aplicado
  ic_real (Number)                 - IC real (gfa_total / area_lote)
  ic_maximo (Number)               - IC max (pisos_finales, legacy)
  altura_total (Number)            - Altura total [m]
  altura_total_validada (Number)   - [v10] Altura total + cota terreno [m]
  pisos_finales (Number)           - Pisos aplicados
  valido (bool)                    - Controles implementados OK (no certificacion)
  mensaje (String)                 - Diagnostico completo
  recortes_intervalos_json (String)- [v08.5] Diagnostico numerico por piso
  presupuesto_ocupacion_m2 (Number)- [v09] area_lote * io_maximo (siempre)
  ocupacion_aprobada_m2 (Number)   - [v09] Ocupacion aprobada (si barras_json)
  gfa_aprobado_m2 (Number)         - [v09] GFA aprobado (si barras_json + valido)
  envelope_aprobado_por_piso (List)- [v09] Curvas aprobadas por piso (si valido)
  alertas_patrimonio (String)      - [v10] Alertas de retiros patrimoniales

FUNCIONES INTERNAS:
  unwrap(val)                      - Desenvuelve listas GH a valor unitario
  safe_list(val)                   - Convierte entrada a lista
  parse_gh_bool(val)               - Parsea booleano desde GH (True/1/verdadero)
  normalize_rango(val, warnings)   - Normaliza rango edificabilidad a "1".."5"
  normalize_bonificacion(val, w)   - Normaliza tipo bonificacion
  normalize_tipologia(val, warnings)- Normaliza tipologia Continua/Aislada
  parse_reglamentacion(raw)        - Parsea JSON reglamentacion (pot_data wrapper)
  dato_reglamentario_num(reg,campo,d) - Lee campo numerico de pot_data
  dato_reglamentario_str(reg,campo,d) - Lee campo string de pot_data
  numero_opcional(raw)             - Lee numero opcional (None si vacio)
  retiro_posterior_consolidacion(p) - Retiro posterior segun tabla 5.4.b
  retiro_lateral_empate(hp,hv,mm)  - Retiro lateral por empate volumetrico
  separacion_sismica_piso(hp,coef) - Separacion sismica NSR-10 A.6.5 (2% x h)
  retiro_frontal_por_ancho_via(av) - Antejardin segun ancho de via (tabla CU-5.5)
  voladizo_por_perfil_vial(av)     - Voladizo frontal segun perfil vial
  parsear_vecinos_por_lado(raw)    - Parsea vecinos por lado (legacy v08)
  parsear_vecino_patrimonio(raw)   - [v10] Parsea lados patrimonio nivel 2
  parsear_construccion_exenta(raw) - [v10] Parsea volumenes no patrimonio exentos
  _parsear_frente_override(raw)    - [v08.2] Override frente por cardinal
  _cardinal_normal(nx,ny)          - Cardinalidad desde normal
  _cardinal_lado(dx,dy,mx,my,cx,cy)- Cardinalidad de un lado del lote
  _poligono_ccw(curva)             - Verifica orientacion CCW de poligono
  _area_signada_puntos(puntos)     - Area signada de lista de puntos
  _curva_desde_puntos(puntos)      - Crea curva cerrada desde puntos
  _vertices_curva(curva)           - Extrae vertices de curva
  _recortar_puntos(puntos,subs)    - Recorte local de poligono por subtramos
  _region_area(curvas)             - Area total de regiones planas
  _recortar_regiones_locales(lote,subs,patios,ccw) - Recorte boolean con patios
  _subdividir_lado(p1,p2,vecinos)  - Subdivide lado por intervalos de vecinos
  _subsegmentos_piso(...)          - Genera subtramos con retiros por piso
  area_curvas(curva_o_lista)       - Area de curva o lista de curvas
  area_curve(crv)                  - Area de una curva Rhino
  parsear_barras_json(raw)         - [v09] Parsea barras_json de F3 v03
  calcular_altura_validada(cota,pisos,fh) - [v10] Altura total + cota terreno

================================================================================
"""

import Rhino.Geometry as rg  # type: ignore[reportMissingImports]
import json
import math
import re
import os

# Rangos de edificabilidad corregidos según Decreto 555/2021
RANGO_PISOS = {"1": 1, "2": 2, "3": 4, "4": 5, "5": 7}
# Pisos extra por incentivo (Decreto 555/2021)
BONIFICACION_PISOS = {
    "NINGUNO": 0,
    "VIS": 2,
    "VIP": 2,
    "EQUIPAMIENTO+COMUNAL": 2,
    "COMUNAL": 1,
    "EQUIPAMIENTO": 1,
}
RANGO_DEFAULT = "3"
TOLERANCIA = 0.01

# Anexo 5 POT (Decreto 466/2024), SECCION 5.4.b - Consolidacion
POSTERIOR_CONSOLIDACION = [
    (3, 3.0), (6, 5.0), (9, 6.0), (12, 8.0), (15, 10.0),
    (18, 12.0), (22, 14.0), (25, 16.0), (28, 18.0), (99, 20.0),
]
# Anexo 5 POT, SECCION 1.9.b - lateral aislada
LATERAL_FRACCION_ALTURA = 0.2
LATERAL_MINIMO_M = 4.0
# Anexo 5 POT, SECCION 1.13.b - Voladizos
VOLADIZO_POR_ANCHO_VIA = [
    (6.0, 0.0), (10.0, 0.60), (15.0, 0.80), (22.0, 1.00), (999.0, 1.50),
]
# v07 - Empate volumetrico lateral + separacion sismica NSR-10 A.6.5
EMPATE_LATERAL_MIN_M = 3.0
NSR10_SEPARACION_COEF = 0.02
# Regla historica pre-555 (respaldo antejardin)
FRONTAL_POR_ANCHO_VIA = [
    (12.0, 3.0), (20.0, 5.0), (999.0, 7.0),
]
ANTEJARDIN_DEFAULT_M = 3.0
TIPOLOGIA_DEFAULT = "Continua"
ALTURA_MAXIMA_SOBRE_COTA_M = 10.0  # Altura maxima sobre cota del terreno


def _extraer_valor_gh(val):
    """Extrae el valor Python nativo de una entrada de Grasshopper.
    Maneja DataTree, listas, tuples y valores directos.
    """
    if val is None:
        return None
    # Intentar acceder a .Data (DataTree de GH)
    try:
        data_attr = getattr(val, 'Data', None)
        if data_attr is not None:
            data_list = list(data_attr)
            if len(data_list) > 0:
                return _extraer_valor_gh(data_list[0])
            return None
    except:
        pass
    # Si es lista o tupla de Python
    if isinstance(val, (list, tuple)):
        if len(val) > 0:
            return _extraer_valor_gh(val[0])
        return None
    # Valor directo
    return val


def unwrap(val):
    return _extraer_valor_gh(val)


def safe_list(val):
    if val is None:
        return []
    # Si es DataTree de Grasshopper
    try:
        data_attr = getattr(val, 'Data', None)
        if data_attr is not None:
            return list(data_attr)
    except:
        pass
    if isinstance(val, (list, tuple)):
        return list(val)
    return [val]


def parse_gh_bool(val):
    v = _extraer_valor_gh(val)
    if v is None:
        return False
    if isinstance(v, bool):
        return v
    s = str(v).strip().lower()
    if s in ("true", "1", "verdadero", "yes", "si"):
        return True
    return False


def normalize_rango(val, warnings):
    if val is None:
        return RANGO_DEFAULT
    s = str(unwrap(val)).strip()
    if s == "":
        return RANGO_DEFAULT
    m = re.search(r"(\d+)", s)
    if m and m.group(1) in RANGO_PISOS:
        return m.group(1)
    warnings.append("rango_edificabilidad no reconocido ('%s') -> default %s" % (s, RANGO_DEFAULT))
    return RANGO_DEFAULT


def normalize_bonificacion(val, warnings):
    if val is None:
        return "NINGUNO"
    s = str(unwrap(val)).strip()
    if s == "":
        return "NINGUNO"
    s = s.upper()
    s = re.sub(r"\s*\+\s*", "+", s)
    s = re.sub(r"\s+", " ", s)
    s = s.replace(u"\u00c1", "A").replace(u"\u00c9", "E").replace(u"\u00cd", "I")
    s = s.replace(u"\u00d3", "O").replace(u"\u00da", "U").replace(u"\u00d1", "N")
    if s not in BONIFICACION_PISOS:
        warnings.append("tipo_bonificacion desconocido ('%s') -> sin piso extra" % s)
        return "NINGUNO"
    return s


def normalize_tipologia(val, warnings):
    if val is None:
        return TIPOLOGIA_DEFAULT
    s = str(unwrap(val)).strip()
    if s == "":
        return TIPOLOGIA_DEFAULT
    s = s.replace(u"\u00c1", "A").replace(u"\u00cd", "I")
    s = s.title()
    if s not in ("Continua", "Aislada"):
        warnings.append("tipologia desconocida ('%s') -> %s" % (s, TIPOLOGIA_DEFAULT))
        return TIPOLOGIA_DEFAULT
    return s


def parse_reglamentacion(raw):
    if raw is None:
        return None
    try:
        s = str(raw[0]) if isinstance(raw, list) and raw else str(raw)
        data = json.loads(s)
        if isinstance(data, dict):
            return data if "pot_data" in data else {"pot_data": data}
        return None
    except:
        return None


def dato_reglamentario_num(reg_data, campo, default=0.0):
    if reg_data is None:
        return default
    v = reg_data.get("pot_data", {}).get(campo)
    if v is None or v == "":
        return default
    try:
        return float(v)
    except:
        return default


def dato_reglamentario_str(reg_data, campo, default=""):
    if reg_data is None:
        return default
    v = reg_data.get("pot_data", {}).get(campo)
    if v is None:
        return default
    s = str(v).strip()
    return s or default


def numero_opcional(raw):
    v = _extraer_valor_gh(raw)
    if v is None:
        return None
    try:
        s = str(v).strip()
        if s in ("", "None"):
            return None
        v = float(s)
        if math.isnan(v) or math.isinf(v):
            return None
        return v
    except (ValueError, TypeError):
        return None


def retiro_posterior_consolidacion(pisos):
    for limite, retiro in POSTERIOR_CONSOLIDACION:
        if pisos <= limite:
            return retiro
    return POSTERIOR_CONSOLIDACION[-1][1]


def retiro_lateral_empate(h_piso, h_vecino, min_m):
    if h_vecino <= 0 or h_piso <= h_vecino:
        return 0.0
    h_exc = h_piso - h_vecino
    return max(LATERAL_FRACCION_ALTURA * h_exc, min_m)


def separacion_sismica_piso(h_piso, coef):
    if coef <= 0:
        return 0.0
    return coef * h_piso


def retiro_frontal_por_ancho_via(ancho_via_m):
    if ancho_via_m is None or ancho_via_m <= 0:
        return ANTEJARDIN_DEFAULT_M
    for limite, retiro in FRONTAL_POR_ANCHO_VIA:
        if ancho_via_m < limite:
            return retiro
    return FRONTAL_POR_ANCHO_VIA[-1][1]


def voladizo_por_perfil_vial(ancho_via_m):
    if ancho_via_m is None or ancho_via_m <= 0:
        return 0.0
    for limite, vol in VOLADIZO_POR_ANCHO_VIA:
        if ancho_via_m <= limite:
            return vol
    return VOLADIZO_POR_ANCHO_VIA[-1][1]


def parsear_vecinos_por_lado(raw):
    if raw is None:
        return {}
    try:
        s = str(raw[0]) if isinstance(raw, list) and raw else str(raw)
        data = json.loads(s)
    except:
        return {}
    if not isinstance(data, dict):
        return {}
    out = {}
    entradas = []
    if "lados" in data and isinstance(data["lados"], list):
        for l in data["lados"]:
            if not isinstance(l, dict):
                continue
            try:
                lid = int(l.get("id", -1))
            except:
                continue
            vecs = l.get("vecinos", [])
            if lid >= 0 and isinstance(vecs, list):
                entradas.append((lid, vecs))
    else:
        for k, v in data.items():
            try:
                lid = int(k)
            except:
                continue
            if isinstance(v, list):
                entradas.append((lid, v))
    for lid, vecs in entradas:
        norm = []
        for v in vecs:
            if isinstance(v, (int, float)):
                norm.append((float(v), None))
            elif isinstance(v, dict):
                try:
                    h = float(v.get("altura_m", 0.0))
                except:
                    h = 0.0
                lon = v.get("longitud_m")
                try:
                    lon = float(lon) if lon is not None else None
                except:
                    lon = None
                if h > 0:
                    norm.append((h, lon))
        if norm:
            out[lid] = norm
    return out


def parsear_vecino_patrimonio(raw):
    """[v10] Parsea JSON de lados marcados como patrimonio nivel 2.
    Formato: [{"lado_id":0,"nivel":2,"patrimonio":true}]
    Retorna dict {lado_id: {"nivel": int, "patrimonio": bool}}
    """
    if raw is None:
        return {}
    try:
        s = str(raw[0]) if isinstance(raw, list) and raw else str(raw)
        data = json.loads(s)
    except:
        return {}
    if not isinstance(data, list):
        return {}
    out = {}
    for item in data:
        if not isinstance(item, dict):
            continue
        try:
            lid = int(item.get("lado_id", -1))
        except:
            continue
        if lid < 0:
            continue
        try:
            nivel = int(item.get("nivel", 0))
        except:
            nivel = 0
        patrimonio = bool(item.get("patrimonio", False))
        out[lid] = {"nivel": nivel, "patrimonio": patrimonio}
    return out


def parsear_construccion_exenta(raw):
    """[v10] Parsea JSON de volumenes no patrimonio exentos de retiros.
    Formato: [{"lado_id":0,"exenta":true}]
    Retorna dict {lado_id: bool}
    """
    if raw is None:
        return {}
    try:
        s = str(raw[0]) if isinstance(raw, list) and raw else str(raw)
        data = json.loads(s)
    except:
        return {}
    if not isinstance(data, list):
        return {}
    out = {}
    for item in data:
        if not isinstance(item, dict):
            continue
        try:
            lid = int(item.get("lado_id", -1))
        except:
            continue
        if lid < 0:
            continue
        exenta = bool(item.get("exenta", False))
        out[lid] = exenta
    return out


# v08.2 - Puente orquestador -> canvas: override de frente por cardinal
CARDINAL_BANDS = [
    ("Norte", 315.0, 45.0), ("Oriente", 45.0, 135.0),
    ("Sur", 135.0, 225.0), ("Occidente", 225.0, 315.0),
]
FRENTE_A_CLASIFICACION = {
    "via": "Frontal", "via_no_frontal": "EspacioPublico",
    "espacio_publico": "EspacioPublico", "predio": "Lateral",
}


def _parsear_frente_override(raw):
    if raw is None:
        return {}
    try:
        s = str(raw[0]) if isinstance(raw, list) and raw else str(raw)
        data = json.loads(s)
    except Exception:
        return {}
    if not isinstance(data, dict):
        return {}
    out = {}
    for k, v in data.items():
        if str(v) in FRENTE_A_CLASIFICACION:
            out[str(k)] = str(v)
    return out


def _cardinal_normal(nx, ny):
    if nx == 0.0 and ny == 0.0:
        return "Norte"
    az = math.degrees(math.atan2(nx, ny)) % 360.0
    for name, lo, hi in CARDINAL_BANDS:
        if lo <= hi:
            if lo <= az < hi:
                return name
        else:
            if az >= lo or az < hi:
                return name
    return "Norte"


def _cardinal_lado(dx, dy, mx, my, cx, cy):
    n1 = (-dy, dx)
    n2 = (dy, -dx)
    vx = mx - cx
    vy = my - cy
    d1 = vx * n1[0] + vy * n1[1]
    d2 = vx * n2[0] + vy * n2[1]
    nx, ny = (n1 if d1 >= d2 else n2)
    return _cardinal_normal(nx, ny)


def _poligono_ccw(curva):
    success, poly = curva.TryGetPolyline()
    if not success or poly is None:
        return True
    s = 0.0
    c = poly.Count
    for i in range(c - 1):
        s += poly[i].X * poly[i + 1].Y - poly[i + 1].X * poly[i].Y
    return s > 0


def _area_signada_puntos(puntos):
    s = 0.0
    n = len(puntos)
    for i in range(n):
        p = puntos[i]
        q = puntos[(i + 1) % n]
        s += p.X * q.Y - q.X * p.Y
    return s / 2.0


def _curva_desde_puntos(puntos):
    if puntos is None or len(puntos) < 3:
        return None
    poly = rg.Polyline(puntos)
    if not poly.IsClosed:
        poly.Add(poly[0])
    return rg.PolylineCurve(poly)


def _vertices_curva(curva):
    success, poly = curva.TryGetPolyline()
    if not success or poly is None:
        return []
    pts = [rg.Point3d(p.X, p.Y, 0.0) for p in poly]
    if len(pts) >= 2 and pts[0].DistanceTo(pts[-1]) > 0.001:
        pts.append(rg.Point3d(pts[0]))
    return pts


def _recortar_puntos(puntos, sub_segmentos):
    poly = [rg.Point3d(p.X, p.Y, 0.0) for p in puntos]
    if len(poly) < 3:
        return None
    ccw = _area_signada_puntos(poly) > 0
    for (a, b), r in sub_segmentos:
        if r <= 0.0:
            continue
        dx = b.X - a.X
        dy = b.Y - a.Y
        largo = math.hypot(dx, dy)
        if largo < 1e-9:
            continue
        ux, uy = dx / largo, dy / largo
        nx, ny = (-uy, ux) if ccw else (uy, -ux)
        k = nx * (a.X + nx * r) + ny * (a.Y + ny * r)
        nuevo = []
        m = len(poly)
        for j in range(m):
            p = poly[j]
            q = poly[(j + 1) % m]
            dp = nx * p.X + ny * p.Y - k
            dq = nx * q.X + ny * q.Y - k
            dentro_p = dp >= -1e-9
            dentro_q = dq >= -1e-9
            if dentro_p:
                nuevo.append(p)
            if dentro_p != dentro_q:
                t = dp / (dp - dq)
                nuevo.append(rg.Point3d(p.X + t * (q.X - p.X), p.Y + t * (q.Y - p.Y), 0.0))
        poly = nuevo
        if len(poly) < 3:
            return None
    return poly


def _region_area(curvas):
    regiones = rg.Brep.CreatePlanarBreps(list(curvas), TOLERANCIA)
    if not regiones:
        raise ValueError('No se pudieron medir regiones con huecos')
    total = 0.0
    for region in regiones:
        props = rg.AreaMassProperties.Compute(region)
        if props is None:
            raise ValueError('Region sin area')
        total += props.Area
    return total


def _recortar_regiones_locales(lote, subs, patios, ccw):
    grouped = []
    for (a, b), r in subs:
        if r <= 0:
            continue
        if grouped:
            (p, q), previous_r = grouped[-1]
            ux, uy = q.X - p.X, q.Y - p.Y
            vx, vy = b.X - a.X, b.Y - a.Y
            lu, lv = math.hypot(ux, uy), math.hypot(vx, vy)
            aligned = (lu > 1e-8 and lv > 1e-8 and
                       abs(ux * vy - uy * vx) / (lu * lv) < 1e-6 and ux * vx + uy * vy > 0)
            if (abs(previous_r - r) < 1e-8 and q.DistanceTo(a) < 1e-6 and aligned):
                grouped[-1] = ((p, b), r)
                continue
        grouped.append(((a, b), r))
    cutters = list(patios)
    for (a, b), r in grouped:
        if r <= 0:
            continue
        dx, dy = b.X - a.X, b.Y - a.Y
        length = math.hypot(dx, dy)
        if length <= 1e-8:
            continue
        nx, ny = (-dy / length, dx / length) if ccw else (dy / length, -dx / length)
        margen_exterior = 5.0 * TOLERANCIA
        pts = [
            rg.Point3d(a.X - nx * margen_exterior, a.Y - ny * margen_exterior, 0),
            rg.Point3d(b.X - nx * margen_exterior, b.Y - ny * margen_exterior, 0),
            rg.Point3d(b.X + nx * r, b.Y + ny * r, 0),
            rg.Point3d(a.X + nx * r, a.Y + ny * r, 0),
        ]
        cutters.append(_curva_desde_puntos(pts))
    if not cutters:
        return [lote], area_curve(lote)
    for index, cutter in enumerate(cutters):
        if cutter is None or not cutter.IsClosed or not cutter.IsValid:
            raise ValueError('cortador {} no cerrado/valido'.format(index))
    merged = rg.Curve.CreateBooleanUnion(cutters, TOLERANCIA)
    if not merged:
        raise ValueError('Union fallida: {} subtramos'.format(len(subs)))
    diff = rg.Curve.CreateBooleanDifference(lote, list(merged), TOLERANCIA)
    if not diff:
        raise ValueError('Diferencia vacia/fallida')
    diff = list(diff)
    area = _region_area(diff)
    if area > area_curve(lote) + TOLERANCIA**2:
        raise ValueError('Recurso aumento el area')
    return diff, area


def _subdividir_lado(p1, p2, vecinos):
    n = len(vecinos)
    if n <= 1:
        return [rg.Point3d(p1.X, p1.Y, 0.0), rg.Point3d(p2.X, p2.Y, 0.0)]
    longs = [v[1] for v in vecinos]
    total = sum([lo for lo in longs if lo is not None and lo > 0])
    if total <= 0:
        fracciones = [1.0 / n] * n
    else:
        fracciones = []
        for lo in longs:
            if lo is not None and lo > 0:
                fracciones.append(lo / total)
            else:
                fracciones.append(0.0)
        suma = sum(fracciones)
        if suma <= 0:
            fracciones = [1.0 / n] * n
        else:
            fracciones = [f / suma for f in fracciones]
    pts = [rg.Point3d(p1.X, p1.Y, 0.0)]
    for f in fracciones:
        ult = pts[-1]
        pts.append(rg.Point3d(ult.X + (p2.X - p1.X) * f, ult.Y + (p2.Y - p1.Y) * f, 0.0))
    if pts[-1].DistanceTo(rg.Point3d(p2.X, p2.Y, 0.0)) > 0.01:
        pts[-1] = rg.Point3d(p2.X, p2.Y, 0.0)
    return pts


def _subsegmentos_piso(nv, lados, vertices, retiros_base, vecinos_por_lado,
                       altura_vecinos_m, empate_lateral_min, nsr_coef,
                       pisos_finales, floor_h, voladizo_frontal,
                       vecino_patrimonio, retiro_patrimonial_m,
                       franja_patrimonial_longitud_m, franja_t1, longitud_lado_0,
                       construccion_exenta, altura_vecino_derecha_m,
                       empate_lateral_derecha_m, empate_activo=True):
    """Genera subtramos con retiros por lado, considerando retiro patrimonial
    limitado a la primera franja [0, franja_t1] del lado 0 (norte-occidental)
    y altura diferencial por lado derecho."""
    h_piso = nv * floor_h
    r_sismica = separacion_sismica_piso(h_piso, nsr_coef) \
        if (pisos_finales > 3 and nv > 1) else 0.0
    subs = []
    n = len(vertices) - 1
    for i in range(n):
        p1, p2 = vertices[i], vertices[(i + 1) % n]
        cls = "Lateral"
        for lado in lados:
            if lado.get("id", 0) == i:
                cls = lado.get("clasificacion", "Lateral")
                break
        retiro_base = retiros_base.get(i, 0.0)
        if cls == "Lateral" and i in vecinos_por_lado:
            vecs = vecinos_por_lado[i]
            sub_pts = _subdividir_lado(p1, p2, vecs)
            # parametro t acumulado de cada punto en [0,1] sobre el lado p1->p2
            lado_len = p1.DistanceTo(p2)
            ts = [0.0]
            for jj in range(1, len(sub_pts)):
                ts.append(min(1.0, ts[-1] + sub_pts[jj-1].DistanceTo(sub_pts[jj]) / max(lado_len, 1e-8)))
            for j in range(len(sub_pts) - 1):
                r = max(retiro_base, r_sismica)
                if empate_activo:
                    h_vec = vecs[j][0]
                    # Si el lado es derecho y tiene altura_vecino_derecha_m, usarla
                    if i in [lado.get("id") for lado in lados
                             if lado.get("clasificacion") == "Lateral"
                             and lado.get("lado_especifico") == "derecha"]:
                        if altura_vecino_derecha_m and altura_vecino_derecha_m > 0:
                            h_vec = altura_vecino_derecha_m
                    r = max(r, retiro_lateral_empate(h_piso, h_vec, empate_lateral_min))
                # Retiro patrimonial: solo si lado es patrimonio y, para el lado 0,
                # el subtramo inicia dentro de la primera franja [0, franja_t1]
                if i in vecino_patrimonio and vecino_patrimonio[i].get("patrimonio", False):
                    if retiro_patrimonial_m and retiro_patrimonial_m > 0:
                        dentro_franja = True
                        if i == 0 and longitud_lado_0 > 1e-8:
                            dentro_franja = 0 <= ts[j] < franja_t1
                        if dentro_franja:
                            r = max(r, retiro_patrimonial_m)
                subs.append(((sub_pts[j], sub_pts[j + 1]), r))
        elif cls == "Lateral":
            r = max(retiro_base, r_sismica)
            if empate_activo:
                # Usar altura_vecino_derecha_m si corresponde al lado derecho
                h_vec = altura_vecinos_m
                if altura_vecino_derecha_m and altura_vecino_derecha_m > 0:
                    # Detectar si este lado es el derecho por aproximacion (ultimo lateral)
                    h_vec = altura_vecino_derecha_m
                r = max(r, retiro_lateral_empate(h_piso, h_vec, empate_lateral_min))
            # Retiro patrimonial si aplica (solo lado completo; para el lado 0 con
            # franja parcial [0, franja_t1<1] no se aplica al lado entero para
            # evitar el aislamiento cruzado fuera de la franja)
            if i in vecino_patrimonio and vecino_patrimonio[i].get("patrimonio", False):
                if retiro_patrimonial_m and retiro_patrimonial_m > 0:
                    if i != 0:
                        # Lados distintos a 0: aplica retiro patrimonial completo (legacy)
                        r = max(r, retiro_patrimonial_m)
                    elif 0 <= ts[j] < franja_t1:
                        # Lado 0: aplica solo dentro de la primera franja [0, franja_t1]
                        r = max(r, retiro_patrimonial_m)
            subs.append(((p1, p2), r))
        elif cls == "Frontal" and nv > 1 and voladizo_frontal > 0:
            r = max(0.0, retiro_base - voladizo_frontal)
            subs.append(((p1, p2), r))
        else:
            subs.append(((p1, p2), retiro_base))
    return subs


def area_curvas(curva_o_lista):
    if curva_o_lista is None:
        return 0.0
    if isinstance(curva_o_lista, list):
        return sum([area_curve(c) for c in curva_o_lista])
    return area_curve(curva_o_lista)


def area_curve(crv):
    if crv is None:
        return 0.0
    area_props = rg.AreaMassProperties.Compute(crv)
    return area_props.Area if area_props else 0.0


# v09 - Parser de barras_json
def parsear_barras_json(raw):
    """v09 - Parsea barras_json desde F3_DISTRIBUCION_v03.
    Espera schema f3_barras_salida_v01 con alternativas y recomendada.
    """
    if raw is None:
        return None, None, None, None, None
    try:
        s = str(raw[0]) if isinstance(raw, list) and raw else str(raw)
        data = json.loads(s)
    except:
        return None, None, None, None, None
    if not isinstance(data, dict):
        return None, None, None, None, None
    if data.get("schema") != "f3_barras_salida_v01":
        return None, None, None, None, None
    rec = data.get("recomendada")
    if not rec:
        return None, None, None, None, None
    for alt in data.get("alternativas", []):
        if alt.get("id") == rec:
            occ = alt.get("ocupacion_total_m2")
            gfa = alt.get("gfa_real_m2")
            huellas = alt.get("huellas_por_piso")
            altura_tot = alt.get("altura_total_m")
            floor_h = alt.get("floor_h")
            if occ is not None and gfa is not None and huellas is not None:
                return float(occ), float(gfa), huellas, \
                    float(altura_tot) if altura_tot else None, \
                    float(floor_h) if floor_h else None
    return None, None, None, None, None


def calcular_altura_validada(cota_terreno, pisos, floor_h):
    """[v10] Calcula altura total + cota de terreno para validar contra
    cota_terreno + 10.00 m."""
    if cota_terreno is None:
        cota_terreno = 0.0
    return cota_terreno + pisos * floor_h


# ==============================================================================
# MAIN
# ==============================================================================

lot_polygon = globals().get("lot_polygon", None)
sides_raw = globals().get("sides_table_json", None)
patio_raw = globals().get("patio_curves", None)
altura_raw = globals().get("altura_max_pot", None)
tratamiento_raw = globals().get("tratamiento", None)
rango_raw = globals().get("rango_edificabilidad", None)
floor_h_raw = globals().get("floor_height_user", None)
io_user_raw = globals().get("io_maximo_user", None)
tipologia_raw = globals().get("tipologia", None)
ancho_via_raw = globals().get("ancho_via_m", None)
antejardin_raw = globals().get("antejardin_m", None)
empate_posterior_raw = globals().get("empate_posterior_pisos", None)
altura_vecinos_raw = globals().get("altura_vecinos_m", None)
empate_lateral_min_raw = globals().get("empate_lateral_min_m", None)
nsr_coef_raw = globals().get("nsr10_separacion_coef", None)
voladizo_raw = globals().get("voladizo_frontal_m", None)
vecinos_raw = globals().get("vecinos_por_lado_json", None)
frente_override_raw = globals().get("frente_override_json", None)
reglamentacion_raw = globals().get("reglamentacion_json", None)
barras_raw = globals().get("barras_json", None)           # v09 NUEVA
retiro_patrimonial_raw = globals().get("retiro_patrimonial_m", None)   # v10
franja_patrimonial_raw = globals().get("franja_patrimonial_longitud_m", None)  # v10
vecino_patrimonio_raw = globals().get("vecino_patrimonio_por_lado", None)  # v10
construccion_exenta_raw = globals().get("construccion_no_patrimonio_exenta", None)  # v10
altura_vecino_derecha_raw = globals().get("altura_vecino_derecha_m", None)  # v10
altura_vecino_izquierda_raw = globals().get("altura_vecino_izquierda_m", None)  # v10
empate_lateral_derecha_raw = globals().get("empate_lateral_derecha_m", None)  # v10
empate_lateral_izquierda_raw = globals().get("empate_lateral_izquierda_m", None)  # v10
cota_terreno_raw = globals().get("cota_terreno_central_m", None)  # v10

warnings = []
bloqueos = []
reglamentacion_data = parse_reglamentacion(reglamentacion_raw)
normativa_confirmada = parse_gh_bool(globals().get("normativa_confirmada", False))
if not normativa_confirmada:
    bloqueos.append("regimen/alturas/empates pendientes de revision humana")
if reglamentacion_data is None:
    bloqueos.append("reglamentacion_json ausente o invalida")

piso_adicional = parse_gh_bool(globals().get("piso_adicional", False))
tipo_bonif_raw = globals().get("tipo_bonificacion", "Ninguno")
tipo_bonificacion = normalize_bonificacion(tipo_bonif_raw, warnings)
rango = normalize_rango(rango_raw, warnings)

sides_data = None
if sides_raw is not None:
    try:
        s = str(sides_raw[0]) if isinstance(sides_raw, list) and sides_raw else str(sides_raw)
        sides_data = json.loads(s)
    except:
        sides_data = None

lados = sides_data.get("lados", []) if isinstance(sides_data, dict) else []
if not lados:
    bloqueos.append("clasificacion de lados ausente")

es_esquina = bool(sides_data.get("es_esquina", False)) if sides_data else False
frente_override = _parsear_frente_override(frente_override_raw)
if frente_override:
    _n_vias = sum(1 for v in frente_override.values() if v in ("via", "via_no_frontal"))
    if _n_vias >= 2:
        es_esquina = True

es_esquina_raw = globals().get("es_esquina_confirmada", None)
if es_esquina_raw is not None:
    es_esquina = parse_gh_bool(es_esquina_raw)
else:
    es_esquina = False
    warnings.append("esquina normativa sin confirmar: no se elimina retiro posterior por esa regla")

aplica_empate_raw = globals().get("aplica_empate_lateral", None)
if aplica_empate_raw is not None and str(unwrap(aplica_empate_raw)).strip() not in ("", "None"):
    empate_activo = parse_gh_bool(aplica_empate_raw)
    warnings.append("empate 1.9.c %s por entrada" % ("activo" if empate_activo else "inactivo"))
else:
    empate_activo = any(str(lado.get("clasificacion", "")).strip().lower() == "posterior" for lado in lados)
    if empate_activo:
        warnings.append("empate 1.9.c activo: predio con lado posterior")
    else:
        warnings.append("empate 1.9.c NO aplica: predio sin lado posterior (dos laterales y esquina) -> solo sismica NSR-10 A.6.5")

tipologia = normalize_tipologia(tipologia_raw, warnings)
if tipologia == TIPOLOGIA_DEFAULT:
    tipologia_reg = dato_reglamentario_str(reglamentacion_data, "tipologia")
    if tipologia_reg:
        tipologia = normalize_tipologia(tipologia_reg, warnings)
        warnings.append("tipologia desde reglamentacion ('%s')" % tipologia)
    elif tipologia_raw is None or str(unwrap(tipologia_raw)).strip() == "":
        warnings.append("tipologia no definida y sin dato reglamentario -> %s" % TIPOLOGIA_DEFAULT)

try:
    ancho_via_m = float(unwrap(ancho_via_raw)) if ancho_via_raw else 0.0
except:
    ancho_via_m = 0.0

if ancho_via_m <= 0:
    ancho_via_m = dato_reglamentario_num(reglamentacion_data, "ancho_via_m", 0.0)
    if ancho_via_m > 0:
        warnings.append("ancho_via_m desde reglamentacion ({:.1f}m)".format(ancho_via_m))
if ancho_via_m <= 0 and sides_data:
    ancho_via_m = float(sides_data.get("ancho_via_m") or 0.0)
    if ancho_via_m > 0:
        warnings.append("ancho_via_m desde LADOS_v06 ({:.1f}m; antejardin por tabla)".format(ancho_via_m))

antejardin_m = numero_opcional(antejardin_raw)
if antejardin_m is None:
    antejardin_m = numero_opcional((reglamentacion_data or {}).get("pot_data", {}).get("antejardin_m"))
    if antejardin_m is not None:
        warnings.append("antejardin_m desde reglamentacion ({:.1f}m)".format(antejardin_m))
if antejardin_m is not None and antejardin_m < 0:
    bloqueos.append("antejardin negativo")
    antejardin_m = None

try:
    empate_posterior_pisos = float(unwrap(empate_posterior_raw)) if empate_posterior_raw else 0.0
except:
    empate_posterior_pisos = 0.0

try:
    altura_vecinos_m = float(unwrap(altura_vecinos_raw)) if altura_vecinos_raw else 0.0
except:
    altura_vecinos_m = 0.0

try:
    empate_lateral_min = float(unwrap(empate_lateral_min_raw)) if empate_lateral_min_raw else 0.0
except:
    empate_lateral_min = 0.0
if empate_lateral_min <= 0:
    empate_lateral_min = EMPATE_LATERAL_MIN_M

try:
    nsr_coef = float(unwrap(nsr_coef_raw)) if nsr_coef_raw else 0.0
except:
    nsr_coef = 0.0
if nsr_coef <= 0:
    nsr_coef = NSR10_SEPARACION_COEF

try:
    voladizo_override = float(unwrap(voladizo_raw)) if voladizo_raw else 0.0
except:
    voladizo_override = 0.0
voladizo_frontal = voladizo_override if voladizo_override > 0 else voladizo_por_perfil_vial(ancho_via_m)
if voladizo_override <= 0 and voladizo_frontal > 0:
    warnings.append("voladizo frontal {:.2f}m por perfil vial (SECCION 1.13.b)".format(voladizo_frontal))

vecinos_por_lado = parsear_vecinos_por_lado(vecinos_raw)
total_vecinos = sum([len(v) for v in vecinos_por_lado.values()])
if total_vecinos > 0:
    warnings.append("vecinos por lado (v08): {} lados, {} vecinos".format(len(vecinos_por_lado), total_vecinos))
elif vecinos_raw is not None and str(vecinos_raw).strip() != "":
    warnings.append("vecinos_por_lado_json sin datos validos -> modo v07 (altura global)")

# v10 - Parsear patrimonio y construccion exenta
vecino_patrimonio = parsear_vecino_patrimonio(vecino_patrimonio_raw)
construccion_exenta = parsear_construccion_exenta(construccion_exenta_raw)
patrimonio_alertas = []
if vecino_patrimonio:
    for lid, info in vecino_patrimonio.items():
        if info.get("patrimonio", False):
            patrimonio_alertas.append("Lado {}: patrimonio nivel {} -> retiro {:.1f}m en primera franja".format(
                lid, info.get("nivel", 0),
                retiro_patrimonial_raw if retiro_patrimonial_raw else 3.0))
if construccion_exenta:
    for lid, exenta in construccion_exenta.items():
        if exenta:
            patrimonio_alertas.append("Lado {}: construccion no patrimonial al fondo -> EXENTA de retiros".format(lid))

try:
    floor_h = float(unwrap(floor_h_raw)) if floor_h_raw else 3.0
except:
    floor_h = 3.0
if floor_h <= 0:
    floor_h = 3.0

try:
    io_user = float(unwrap(io_user_raw)) if io_user_raw else 0.0
except:
    io_user = 0.0

tratamiento = str(unwrap(tratamiento_raw)) if tratamiento_raw else "Consolidacion"

# IO MAXIMO
if io_user > 0:
    io_maximo = io_user
elif tratamiento == "Consolidacion":
    io_maximo = 0.70
elif tratamiento in ("Desarrollo", "Mejoramiento"):
    io_maximo = 0.60
else:
    io_maximo = 0.70

# PISOS Y ALTURA
ic_maximo_base = RANGO_PISOS.get(rango, RANGO_PISOS[RANGO_DEFAULT])
pisos_extra = BONIFICACION_PISOS.get(tipo_bonificacion, 0) if piso_adicional else 0
pisos_propuestos = ic_maximo_base + pisos_extra
pisos_limite = numero_opcional(globals().get("pisos_maximos_total", None))
if pisos_limite is None:
    pisos_limite = numero_opcional((reglamentacion_data or {}).get("pot_data", {}).get("altura_maxima_pisos"))
if pisos_limite is not None:
    if pisos_limite < 1 or abs(pisos_limite - round(pisos_limite)) > 1e-6:
        bloqueos.append("limite de pisos no entero positivo")
    else:
        pisos_limite = int(round(pisos_limite))
        if pisos_propuestos > pisos_limite:
            warnings.append("{} pisos solicitados -> {} total incluyendo bonos; no se acumulan adicionales fuera del limite".format(
                pisos_propuestos, pisos_limite))
        pisos_propuestos = min(pisos_propuestos, pisos_limite)
else:
    bloqueos.append("falta total de pisos incluyendo bonificaciones")
if floor_h <= 0:
    bloqueos.append("altura entrepiso no positiva")
    floor_h = 3.0
pisos_finales = pisos_propuestos
pisos_extra = max(0, pisos_finales - ic_maximo_base)
ic_maximo = pisos_finales
altura_total = pisos_finales * floor_h

# v10 - Altura validada con cota de terreno
cota_terreno_central = numero_opcional(cota_terreno_raw)
altura_total_validada = calcular_altura_validada(cota_terreno_central, pisos_finales, floor_h)
if cota_terreno_central is not None:
    altura_limite = cota_terreno_central + ALTURA_MAXIMA_SOBRE_COTA_M
    if altura_total_validada > altura_limite + TOLERANCIA**2:
        bloqueos.append("altura total {:.2f}m (cota {:.2f}m + {}) excede limite {:.2f}m (cota + 10.00m)".format(
            altura_total_validada, cota_terreno_central, pisos_finales * floor_h, altura_limite))
    else:
        warnings.append("altura total {:.2f}m dentro de limite {:.2f}m (cota terreno + 10.00m)".format(
            altura_total_validada, altura_limite))
else:
    warnings.append("sin cota_terreno_central_m: altura validada usa cota 0.0")

# RETIROS BASE
if antejardin_m is not None:
    antejardin = antejardin_m
else:
    antejardin = retiro_frontal_por_ancho_via(ancho_via_m)
    if ancho_via_m <= 0:
        warnings.append("sin ancho_via_m -> antejardin provisional {:.1f}m (ver mapa CU-5.5)".format(antejardin))
        bloqueos.append("antejardin sin dato explicito y ancho vial desconocido")

empate_posterior = empate_posterior_pisos >= 3.0
if es_esquina:
    retiro_posterior = 0.0
    warnings.append("lote de esquina: sin aislamiento posterior (patio 3x3 en esquina interior)")
elif empate_posterior:
    retiro_posterior = 0.0
else:
    retiro_posterior = retiro_posterior_consolidacion(pisos_finales)

if tipologia == "Aislada":
    retiro_lateral = max(LATERAL_FRACCION_ALTURA * altura_total, LATERAL_MINIMO_M)
else:
    retiro_lateral = 0.0

# Inicializar outputs
envelope_curve = None
envelope_por_piso = []
retiros_por_piso = ""
ocupacion_real = 0.0
gfa_total = 0.0
ic_real = 0.0
valido = False
area_lote = area_curve(lot_polygon) if lot_polygon else 0.0
presupuesto_ocupacion_m2 = area_lote * io_maximo

# v10 - Retiro patrimonial valor
retiro_patrimonial_m = numero_opcional(retiro_patrimonial_raw)
if retiro_patrimonial_m is None:
    retiro_patrimonial_m = 3.0  # default reglamento patrimonial

franja_patrimonial_longitud = numero_opcional(franja_patrimonial_raw)
altura_vecino_derecha_m = numero_opcional(altura_vecino_derecha_raw)
altura_vecino_izquierda_m = numero_opcional(altura_vecino_izquierda_raw)
empate_lateral_derecha_m = numero_opcional(empate_lateral_derecha_raw)
empate_lateral_izquierda_m = numero_opcional(empate_lateral_izquierda_raw)

# v10 - Franja patrimonial del lado 0 (norte-occidental): el retiro patrimonial
# se aplica SOLO al subsegmento [0, t1] del lado 0, limitado por
# franja_patrimonial_longitud_m. Si no hay franja definida, comportamiento legacy
# (retiro sobre todo el lado patrimonio).
franja_t1 = 1.0
longitud_lado_0 = 0.0
if franja_patrimonial_longitud and franja_patrimonial_longitud > 0:
    try:
        v0 = vertices_lote[0]
        v1 = vertices_lote[1] if len(vertices_lote) > 1 else None
        if v1 is not None:
            longitud_lado_0 = v0.DistanceTo(v1)
            if longitud_lado_0 > 1e-8 and 0 in vecino_patrimonio and vecino_patrimonio[0].get("patrimonio", False):
                franja_t1 = min(1.0, franja_patrimonial_longitud / longitud_lado_0)
            else:
                franja_t1 = 0.0
    except Exception:
        franja_t1 = 1.0

# Patios
patios_list = [p for p in safe_list(patio_raw) if p is not None]
patio_area_total = sum(area_curve(p) for p in patios_list)


def envelope_final(huella):
    if huella is None:
        return None, 0.0
    if not patios_list:
        return huella, area_curve(huella)
    try:
        diff = rg.Curve.CreateBooleanDifference(huella, patios_list, TOLERANCIA)
        if diff and len(diff) > 0:
            breps = rg.Brep.CreatePlanarBreps(list(diff), TOLERANCIA)
            if not breps:
                raise ValueError("no se pudieron construir regiones planas")
            area = sum(rg.AreaMassProperties.Compute(b).Area for b in breps if rg.AreaMassProperties.Compute(b))
            if area < 0 or area > area_curve(huella) + TOLERANCIA**2:
                raise ValueError("area de diferencia incoherente")
            return (list(diff) if len(diff) > 1 else diff[0]), area
        raise ValueError("diferencia vacia o fallida")
    except Exception as exc:
        bloqueos.append("booleana de patios no verificable: {}".format(str(exc)))
        return None, 0.0


# Retiros base por lado + override operador + patrimonio
_centroide_lote = None
if lot_polygon is not None and frente_override:
    _vpre = _vertices_curva(lot_polygon)
    if _vpre:
        _npre = len(_vpre)
        _centroide_lote = (sum(v.X for v in _vpre) / _npre, sum(v.Y for v in _vpre) / _npre)

retiros_base = {}
for lado in lados:
    idx = lado.get("id", 0)
    cls = lado.get("clasificacion", "Lateral")
    if _centroide_lote is not None:
        try:
            _dx = float(lado.get("dx", 0.0) or 0.0)
            _dy = float(lado.get("dy", 0.0) or 0.0)
            _mx = float(lado.get("mx", 0.0) or 0.0)
            _my = float(lado.get("my", 0.0) or 0.0)
            _card = _cardinal_lado(_dx, _dy, _mx, _my, _centroide_lote[0], _centroide_lote[1])
            if _card in frente_override:
                cls = FRENTE_A_CLASIFICACION[frente_override[_card]]
        except Exception:
            pass
    # v10: si lado es patrimonio y dentro de franja, usar retiro patrimonial
    if cls == "Lateral" and idx in vecino_patrimonio and vecino_patrimonio[idx].get("patrimonio", False):
        if retiro_patrimonial_m and retiro_patrimonial_m > 0:
            retiros_base[idx] = retiro_patrimonial_m
            warnings.append("Lado {}: retiro patrimonial {:.1f}m aplicado (primera franja {:.1f}m)".format(
                idx, retiro_patrimonial_m,
                franja_patrimonial_longitud if franja_patrimonial_longitud else 0.0))
        elif cls == "Frontal":
            retiros_base[idx] = antejardin
        elif cls == "Posterior":
            retiros_base[idx] = retiro_posterior
        elif cls == "EspacioPublico":
            retiros_base[idx] = 0.0
        else:
            retiros_base[idx] = retiro_lateral
    elif cls == "Frontal":
        retiros_base[idx] = antejardin
    elif cls == "Posterior":
        retiros_base[idx] = retiro_posterior
    elif cls == "EspacioPublico":
        retiros_base[idx] = 0.0
    else:
        retiros_base[idx] = retiro_lateral

# Envelopes
huellas_por_piso = []
areas_por_piso = []
recortes_intervalos_json = '[]'
diag_recortes = []
intervalos = {}
vertices_lote = _vertices_curva(lot_polygon) if lot_polygon is not None else []

# VALIDADOR DE BARRAS (v09)
barras_ocupacion = None
barras_gfa = None
barras_huellas = None
barras_altura = None
barras_floor_h = None
if barras_raw is not None:
    barras_ocupacion, barras_gfa, barras_huellas, barras_altura, barras_floor_h = parsear_barras_json(barras_raw)
    if barras_ocupacion is not None:
        warnings.append("VALIDADOR v09: barras_json presente -> modo APROBADO (ocupacion={:.2f}, gfa={:.2f})".format(
            barras_ocupacion, barras_gfa))

try:
    raw_int = unwrap(globals().get('vecinos_intervalos_json', None))
    if not raw_int:
        raise ValueError('vecinos_intervalos_json sin conectar')
    data_int = json.loads(raw_int)
    if data_int.get('schema') != 'vecinos_intervalos_canvas_v02':
        raise ValueError('schema de intervalos incorrecto')
    if not sides_data or not sides_data.get('puente_lados_ok'):
        raise ValueError('puente LADOS no verificado')
    if not data_int.get('chip') or data_int.get('chip') != sides_data.get('chip'):
        raise ValueError('CHIP de intervalos/LADOS distinto')
    n_edges = len(vertices_lote) - 1
    for entry in data_int.get('lados') or []:
        lid = entry.get('id')
        if not isinstance(lid, int) or not 0 <= lid < n_edges or lid in intervalos:
            raise ValueError('id de intervalo invalido/duplicado')
        spans = sorted(entry.get('subtramos') or [], key=lambda s: s['t0'])
        cursor = 0.0
        if entry.get('es_colindancia_predial'):
            for span in spans:
                t0, t1 = float(span['t0']), float(span['t1'])
                if not 0 <= t0 < t1 <= 1 or abs(t0 - cursor) > 0.01:
                    raise ValueError('intervalos con huecos/solapes en L{}'.format(lid))
                cursor = t1
                if span.get('altura_m') is None or float(span['altura_m']) <= 0:
                    bloqueos.append('altura pendiente L{} raw {}'.format(lid, span.get('segmento_raw')))
            if abs(cursor - 1.0) > 0.01:
                raise ValueError('cobertura incompleta en L{}'.format(lid))
        intervalos[lid] = entry
    if len(intervalos) != n_edges:
        raise ValueError('faltan lados en contrato de intervalos')
    if data_int.get('pendientes'):
        bloqueos.append('{} pendientes en contrato de vecinos'.format(len(data_int['pendientes'])))
    warnings.append('vecinos por intervalos: {} lados; recortes locales activos'.format(len(intervalos)))
except Exception as exc:
    intervalos = {}
    bloqueos.append('intervalos no verificables: {}'.format(str(exc)))

# Si hay barras validas -> MODO APROBADO
if barras_ocupacion is not None and barras_huellas is not None:
    if area_lote > 0 and barras_ocupacion > presupuesto_ocupacion_m2 + TOLERANCIA**2:
        bloqueos.append("VALIDADOR v09: ocupacion_total {:.2f} > presupuesto {:.2f}; excedente {:.2f} m2".format(
            barras_ocupacion, presupuesto_ocupacion_m2, barras_ocupacion - presupuesto_ocupacion_m2))
        valido = False
    else:
        bloqueos = [b for b in bloqueos if "regimen/alturas/empates" not in b and "intervalos no verificables" not in b]
        ocupacion_real = barras_ocupacion
        gfa_total = barras_gfa
        envelope_por_piso = barras_huellas
        envelope_curve = envelope_por_piso[0] if envelope_por_piso else None
        altura_total = barras_altura if barras_altura else pisos_finales * (barras_floor_h if barras_floor_h else floor_h)
        altura_total_validada = calcular_altura_validada(cota_terreno_central, pisos_finales,
                                                         barras_floor_h if barras_floor_h else floor_h)
        valido = True
else:
    # MODO POTENCIAL
    if lot_polygon is not None and vertices_lote:
        for nv in range(1, pisos_finales + 1):
            if intervalos:
                subs = []
                for i in range(len(vertices_lote) - 1):
                    a, b = vertices_lote[i], vertices_lote[i + 1]
                    cls = next((l.get('clasificacion') for l in lados if l.get('id') == i), 'Lateral')
                    base = retiros_base.get(i, 0.0)
                    seismic = separacion_sismica_piso(nv * floor_h, nsr_coef) if pisos_finales > 3 and nv > 1 else 0.0
                    if cls in ('Lateral', 'Posterior'):
                        for span in intervalos[i].get('subtramos') or []:
                            t0, t1 = float(span['t0']), float(span['t1'])
                            p = rg.Point3d(a.X + (b.X - a.X) * t0, a.Y + (b.Y - a.Y) * t0, 0)
                            q = rg.Point3d(a.X + (b.X - a.X) * t1, a.Y + (b.Y - a.Y) * t1, 0)
                            r = max(base, seismic) if cls == 'Lateral' else base
                            h = span.get('altura_m')
                            if cls == 'Lateral' and empate_activo and h is not None:
                                r = max(r, retiro_lateral_empate(nv * floor_h, float(h), empate_lateral_min))
                            # v10: retiro patrimonial en intervalos (solo lado 0 dentro
                            # de la primera franja [0, franja_t1])
                            if i in vecino_patrimonio and vecino_patrimonio[i].get('patrimonio', False):
                                if retiro_patrimonial_m and retiro_patrimonial_m > 0:
                                    dentro_franja = True
                                    if i == 0 and longitud_lado_0 > 1e-8:
                                        dentro_franja = 0 <= t0 < franja_t1
                                    if dentro_franja:
                                        r = max(r, retiro_patrimonial_m)
                            subs.append(((p, q), r))
                            diag_recortes.append({'piso': nv, 'id': i, 't0': t0, 't1': t1,
                                                  'retiro_m': r, 'altura_vecino_m': h})
                    else:
                        r = max(0.0, base - voladizo_frontal) if cls == 'Frontal' and nv > 1 else base
                        subs.append(((a, b), r))
            else:
                subs = _subsegmentos_piso(nv, lados, vertices_lote, retiros_base, vecinos_por_lado,
                                          altura_vecinos_m, empate_lateral_min, nsr_coef,
                                          pisos_finales, floor_h, voladizo_frontal,
                                          vecino_patrimonio, retiro_patrimonial_m,
                                          franja_patrimonial_longitud, franja_t1, longitud_lado_0,
                                          construccion_exenta, altura_vecino_derecha_m,
                                          empate_lateral_derecha_m, empate_activo)
            try:
                envs, area = _recortar_regiones_locales(lot_polygon, subs, patios_list,
                                                        _area_signada_puntos(vertices_lote) > 0)
                huellas_por_piso.append(envs[0] if len(envs) == 1 else envs)
                areas_por_piso.append(area)
            except Exception as exc:
                huellas_por_piso.append(None)
                areas_por_piso.append(0.0)
                bloqueos.append('piso {} recorte no verificable: {}'.format(nv, str(exc)))
    recortes_intervalos_json = json.dumps(diag_recortes, ensure_ascii=True)
    envelope_por_piso = huellas_por_piso
    if envelope_por_piso:
        envelope_curve = envelope_por_piso[0]
    ocupacion_real = areas_por_piso[0] if areas_por_piso else 0.0
    gfa_total = sum(areas_por_piso)
    if io_user > 0:
        io_maximo = io_user
    elif tratamiento == "Consolidacion":
        io_maximo = 0.70
    elif tratamiento in ("Desarrollo", "Mejoramiento"):
        io_maximo = 0.60
    else:
        io_maximo = 0.70
    io_real = ocupacion_real / area_lote if area_lote > 0 else 0.0
    if area_lote <= 0 or ocupacion_real <= 0:
        bloqueos.append("lote u ocupacion nulos")
    if not 0 < io_maximo <= 1:
        bloqueos.append("IO maximo fuera de (0,1]")
    if area_lote > 0 and ocupacion_real > area_lote * io_maximo + TOLERANCIA**2:
        bloqueos.append("IO real {:.4f} > limite {:.4f}; excedente {:.2f} m2".format(
            io_real, io_maximo, ocupacion_real - area_lote * io_maximo))
    if len(areas_por_piso) != pisos_finales or any(a <= 0 for a in areas_por_piso):
        bloqueos.append("uno o mas niveles sin region valida")
    valido = not bloqueos

# SALIDAS APROBADAS (v09)
if barras_ocupacion is not None and valido:
    ocupacion_aprobada_m2 = barras_ocupacion
    gfa_aprobado_m2 = barras_gfa
    envelope_aprobado_por_piso = barras_huellas
    io_real = barras_ocupacion / area_lote if area_lote > 0 else 0.0
else:
    ocupacion_aprobada_m2 = 0.0
    gfa_aprobado_m2 = 0.0
    envelope_aprobado_por_piso = []
    if barras_ocupacion is not None:
        io_real = barras_ocupacion / area_lote if area_lote > 0 else 0.0

# Desglose por piso
escalonados = []
for nv in range(1, pisos_finales + 1):
    h_piso = nv * floor_h
    r_sismica = separacion_sismica_piso(h_piso, nsr_coef) if (pisos_finales > 3 and nv > 1) else 0.0
    retiro_max = 0.0
    for i, lado in enumerate(lados):
        if lado.get("clasificacion", "Lateral") != "Lateral":
            continue
        lid = lado.get("id", i)
        r_l = 0.0
        if empate_activo:
            if lid in vecinos_por_lado:
                r_l = max([retiro_lateral_empate(h_piso, v[0], empate_lateral_min) for v in vecinos_por_lado[lid]] or [0.0])
            else:
                r_l = retiro_lateral_empate(h_piso, altura_vecinos_m, empate_lateral_min)
        # v10: retiro patrimonial (solo lado 0 limitado a la primera franja;
        # si no hay franja definida, comportamiento legacy sobre todo el lado)
        if lid in vecino_patrimonio and vecino_patrimonio[lid].get("patrimonio", False):
            if retiro_patrimonial_m and retiro_patrimonial_m > 0:
                if lid != 0 or franja_patrimonial_longitud and franja_patrimonial_longitud > 0:
                    r_l = max(r_l, retiro_patrimonial_m)
        retiro_max = max(retiro_max, r_l, r_sismica)
    if retiro_max > 0:
        escalonados.append(nv)

try:
    retiros_por_piso = json.dumps([
        {
            "piso": i + 1,
            "altura_m": round((i + 1) * floor_h, 2),
            "area_m2": round(areas_por_piso[i], 2),
            "escalonado": (i + 1) in escalonados,
            "voladizo_frontal_m": round(voladizo_frontal if i > 0 else 0.0, 2),
            "vecinos_por_lado": {str(k): [round(v[0], 2) for v in vs] for k, vs in vecinos_por_lado.items()},
            "retiro_patrimonial_m": round(retiro_patrimonial_m, 2),
            "cota_terreno_central_m": round(cota_terreno_central, 2) if cota_terreno_central is not None else None,
            "altura_total_validada_m": round(altura_total_validada, 2)
        }
        for i in range(pisos_finales)
    ], ensure_ascii=False)
except:
    retiros_por_piso = "[]"

# CALCULAR ic_real FINAL
if area_lote > 0:
    ic_real = float((gfa_aprobado_m2 if gfa_aprobado_m2 else gfa_total) / area_lote)
else:
    ic_real = 0.0

# Mensaje final
if io_user > 0:
    io_maximo = io_user
elif tratamiento == "Consolidacion":
    io_maximo = 0.70
elif tratamiento in ("Desarrollo", "Mejoramiento"):
    io_maximo = 0.60
else:
    io_maximo = 0.70

if valido:
    modo = "APROBADO (barras_json)" if barras_ocupacion is not None else "POTENCIAL"
    empate_txt = "NO aplica (sin lado posterior): solo sismica 2%xh" if not empate_activo else "activo (lado posterior)"
    patrimonio_txt = "; ".join(patrimonio_alertas) if patrimonio_alertas else "sin retiros patrimoniales activos"
    gfa_valido = float(gfa_aprobado_m2 if gfa_aprobado_m2 else gfa_total)
    ic_valido = gfa_valido / area_lote if area_lote > 0 else 0
    mensaje = "NORMATIVA v10.0 | {modo} | Lote: {area:.1f}m2 | Ocup: {ocup:.1f}m2 | IO max {io:.2f} | Presupuesto: {presup:.1f}m2 | IC {ic:.2f} (+{bon}) | Alt {alt:.1f}m | AltVal {altv:.1f}m | {pisos} pisos | GFA: {gfa:.1f}m2 | Esc: {esc} pisos | Vol: {vol:.2f}m | Vec: {nv} lados, {nvec} vecinos | Empate: {emp} | Patios: {pat:.1f}m2 | Tipo: {tip} | Antejard: {ant:.1f}m (via {av:.1f}m) | Lat: {lat:.1f}m | Post: {pos:.1f}m | Patrimonio: {patr}".format(
        modo=modo, area=area_lote, ocup=ocupacion_real, io=io_maximo, presup=presupuesto_ocupacion_m2,
        ic=ic_valido, bon=pisos_extra, alt=altura_total, altv=altura_total_validada, pisos=pisos_finales,
        gfa=gfa_valido, esc=len(escalonados), vol=voladizo_frontal, nv=len(vecinos_por_lado), nvec=total_vecinos,
        emp=empate_txt, pat=patio_area_total, tip=tipologia, ant=antejardin, av=ancho_via_m,
        lat=retiro_lateral, pos=retiro_posterior, patr=patrimonio_txt)
else:
    gfa_err = float(gfa_total if 'gfa_total' in locals() else 0)
    bloqueos_txt = "; ".join(sorted(set(bloqueos)))
    mensaje = "NORMATIVA v10.0 | NO VALIDADO | Lote {area:.2f} m2 | Ocup {ocup:.2f} m2 | IO real {io:.4f} / max {iom:.4f} | Presupuesto {presup:.2f} m2 | {pisos} pisos | Alt {alt:.2f} m | AltVal {altv:.2f} m | GFA {gfa:.2f} m2 | {bloq}".format(
        area=area_lote, ocup=ocupacion_real, io=io_real, iom=io_maximo, presup=presupuesto_ocupacion_m2,
        pisos=pisos_finales, alt=altura_total, altv=altura_total_validada, gfa=gfa_err, bloq=bloqueos_txt)

if altura_vecinos_m <= 0 and not altura_vecino_derecha_m:
    warnings.append("sin altura_vecinos_m ni altura_vecino_derecha_m -> sin escalonamiento lateral (SECCION 1.9.c)")

if warnings:
    mensaje += " | AVISOS: " + "; ".join(warnings)

# ASIGNAR SALIDAS GLOBALES PARA GRASSHOPPER
# envelope_curve, envelope_por_piso, retiros_por_piso, gfa_total, ocupacion_real,
# io_maximo, ic_real, ic_maximo, altura_total, altura_total_validada, pisos_finales,
# valido, mensaje, recortes_intervalos_json, presupuesto_ocupacion_m2,
# ocupacion_aprobada_m2, gfa_aprobado_m2, envelope_aprobado_por_piso, alertas_patrimonio

alertas_patrimonio = "; ".join(patrimonio_alertas) if patrimonio_alertas else ""
