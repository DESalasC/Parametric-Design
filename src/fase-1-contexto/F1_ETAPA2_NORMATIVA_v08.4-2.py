# -*- coding: utf-8 -*-
"""
================================================================================
F1_ETAPA2_NORMATIVA_v08.py - Retiros + Patios + Indices + Piso Adicional
                            + Ancho de via con respaldo desde LADOS
                            + ENVELOPE ESCALONADO por pisos superiores
                            + VECINOS CON ALTURAS VARIABLES por lateral
Proyecto: DisenoParametrico / Fase 1
GH Python Script para Grasshopper (IronPython 2.7 compatible)
================================================================================

SUBVERSIONES INTERNAS (v08.x: iteraciones sin cambio de version general):
  v08.4 PROPUESTA (sin validacion Rhino): IO real bloqueante, antejardin
         cero explicito, limite de pisos desde reglamentacion o entrada
         opcional pisos_maximos_total; booleanas sin areas ficticias.
         valido indica controles implementados, NO certificacion normativa.
         Pendientes: regiones por tramo, multivolumen, alturas e IDPC.
         Opcionales nuevos: pisos_maximos_total (Item Number),
         normativa_confirmada (Item Boolean, default False). Conectar el
         primero al total incluyendo bonificaciones; el segundo solo tras
         revision humana. No se crean estos puertos automaticamente.
  v08.1 (2026-08-16): correccion normativa del operador - el empate
         volumetrico lateral (Anexo 5, SECCION 1.9.c) aplica UNICAMENTE a
         predios con lado POSTERIOR (lote interior/fondo). Para predios con
         dos laterales y al menos una esquina (sin lado posterior) NO aplica:
         con vecinos construidos rige SIEMPRE el aislamiento sismorresistente
         (NSR-10 A.6.5, 2% x h). Entrada nueva `aplica_empate_lateral`
         (Boolean, override) + auto-deteccion por la clasificacion del LADOS
         (presencia de lado "Posterior"). Sin lado posterior, el retiro
         lateral = SOLO sismica 2% x h (caso A: GFA 1.501,2 m2 en el
         estimador; 1.469,2 m2 en el canvas con patio 9,0 m2).
  v08.2 (2026-08-23): regla de lote de esquina (2+ lados via/EP -> sin
         aislamiento posterior; la esquina interior lleva patio 3x3) +
         puente frente_override: entrada frente_override_json {cardinal:
         frente} (salida de F0_LOAD_PROYECTO v01.4); la clasificacion del
         operador manda sobre la geometrica, casada por cardinal (normal
         saliente del lado).
  v08.3 (2026-08-23): "via_no_frontal" cuenta como via en la regla de
         esquina (2+ lados de calle), evitando patio posterior en esquina
         con via secundaria sin antejardin. El codigo se integro el
         2026-08-23 (commit 3f3ff835) pero este encabezado no se
         actualizo; registrado el 2026-09-01.
Regla de versionado: la version general (v08 -> v09) SOLO cambia con cambios
mayores (contrato de entradas/salidas o algoritmo central); las iteraciones
internas se registran como subversiones v08.x en este encabezado (el mensaje
del componente reporta la subversion en curso).

CALCULO:
  1. Descontar retiro FRONTAL (antejardin) del lado frontal del lote
  2. NO descontar retiro en lados EspacioPublico (0m)
  3. Lateral: 0m en tipologia CONTINUA; en AISLADA, 1/5 de la altura de la
     edificacion, minimo 4,00m (Anexo 5 POT, SECCION 1.9.b) - se exige desde
     el segundo piso; el modelo de huella unica lo aplica en toda la huella
     (aproximacion conservadora documentada)
  4. Posterior: tabla Consolidacion por pisos (Anexo 5 POT, SECCION 5.4.b);
     con empate volumetrico (vecino posterior de 3+ pisos sin aislamiento,
     SECCION 5.4.c) el retiro posterior = 0 en la huella
  5. Restar el patio (desde vertice N) del perimetro restante (Boolean Diff)
  6. Calcular pisos base (Decreto 555/2021) y aplicar PISO ADICIONAL
  7. ESCALONAMIENTO EN PISOS SUPERIORES (v07/v08.1): cuando la edificacion supera la
     altura de las edificaciones colindantes sin aislamiento lateral (Anexo 5
     POT, SECCION 1.9.c - Empates de aislamientos laterales), los pisos por
     encima del nivel de empate se retiran con aislamiento lateral =
     max(1/5 x altura desde el nivel de empate, minimo del empate). Se toma el
     MAYOR entre ese retiro y la separacion sismica NSR-10 A.6.5 (Tabla
     A.6.5-1: 1-3% de la altura por piso) cuando aplica (>3 pisos, amenaza
     intermedia/alta, colindancia con predio). NO aplica en lados que
     colindan con via publica o espacio publico (excepcion A.6.5).
     NOTA v08.1 (correccion normativa del operador): la SECCION 1.9.c (empate
     volumetrico lateral) aplica SOLO a predios con lado POSTERIOR (lote
     interior/fondo). Para predios con dos laterales y al menos una esquina
     (sin lado posterior) NO aplica: con vecinos construidos rige SIEMPRE el
     aislamiento de las normas SISMORRESISTENTES (NSR-10 A.6.5, 2% x h).
     Entrada aplica_empate_lateral (Boolean): override manual; sin cablear,
     auto-deteccion por la clasificacion del LADOS (presencia de lado
     Posterior).
  8. Calcular GFA ESCALONADO = suma de las areas de los envelopes por piso
     (Fase 2) y emitir envelope_por_piso para Fase 3 (masa escalonada).
  9. VOLADIZOS (v07, Anexo 5 POT SECCION 1.13): en pisos diferentes del
     primero, la fachada frontal puede sobresalir del paramento de
     construccion sobre el antejardin/APAUP segun el perfil vial (SECCION
     1.13.b): <=6m no se permite; >6-10m 0,60m; >10-15m 0,80m; >15-22m
     1,00m; >22m/malla arterial 1,50m. El voladizo SE contabiliza en el
     indice de construccion (GFA) en pisos != 1 y NO en el area ocupada
     (definicion de Voladizo). NO se permite sobre cesiones publicas para
     parques/equipamientos ni EEP (lados EspacioPublico), ni sobre
     aislamientos laterales (lados Lateral). Implementacion: en pisos 2+ el
     retiro frontal del envelope se reduce a (antejardin - voladizo).
 10. VECINOS CON ALTURAS VARIABLES POR LATERAL (v08): NO todos los vecinos
     tienen la misma altura y sobre un mismo lado del predio puede haber
     VARIOS vecinos (como se modela en Fase 2). La entrada
     `vecinos_por_lado_json` define por cada lado Lateral la lista de vecinos
     (altura y longitud opcional). El retiro de empate (SECCION 1.9.c) se
     calcula POR SEGMENTO con la altura del vecino de ese segmento (el retiro
     del piso crece donde el vecino es mas bajo); el lado se subdivide en
     tantos sub-segmentos como vecinos (longitudes proporcionales si no se
     informan). El recorte de la huella pasa a SEMIPLANOS por sub-segmento
     (cajas exteriores + BooleanDifference), robusto en poligonos concavos
     (reemplaza al desplazamiento por interseccion de lineas, que solo es
     estable en convexos). Sin la entrada, el comportamiento es identico al
     v07 (altura_vecinos_m global).

NOTA NORMATIVA (antejardin / retiro frontal):
  En Consolidacion el antejardin se exige segun el mapa CU-5.5
  "Dimensionamiento de Antejardines" (Resolucion SDP 1631/2023). Cuando el
  mapa no determina la dimension, aplica la norma vigente antes del Decreto
  555/2021 (regla historica: vias < 12m -> 3,00m; 12-20m -> 5,00m; >=20m ->
  7,00m, parametrizable en FRONTAL_POR_ANCHO_VIA). La entrada antejardin_m
  permite fijar el valor oficial del mapa CU-5.5 por sector.
  En esquineros el mapa permite reducir a 2,00m por el lado de mayor
  dimension (usar antejardin_m para casos puntuales).

NOTA NORMATIVA (empate volumetrico lateral, SECCION 1.9.c - v07):
  "Cuando el proyecto supere la altura de las edificaciones colindantes sin
  aislamiento lateral existentes a la fecha [555/2021], con altura superior a
  la definida en los mapas CU-5.4.2 a CU-5.4.33, la edificacion de mayor
  altura debe prever aislamiento lateral por el costado que colinde con la
  edificacion de menor altura, calculado a partir de la altura de la menor."
  Dimension minima del aislamiento lateral: 1/5 de la altura en metros que
  alcance la edificacion medida desde el nivel de empate (SECCION 1.9.b /
  1.9.c), con minimo parametrizable (empate_lateral_min_m, default 3,00m).
  La separacion sismica NSR-10 A.6.5 (Tabla A.6.5-1, >3 pisos) se suma a la
  comparacion: se toma el MAYOR valor entre el retiro POT y la separacion
  sismica del piso (s_i = coeficiente x h_i).

NOTA NORMATIVA (empate volumetrico posterior):
  "En predios que colinden posteriormente con predios en los que a la fecha
  de entrada en vigencia del Decreto Distrital 555 de 2021, existan
  edificaciones de tres (3) o mas pisos sin aislamiento posterior, se
  permite prever empate volumetrico con la altura de dichas edificaciones,
  a partir de cuyo nivel se exige aislamiento posterior reglamentario
  aplicado a la altura maxima de la edificacion." (Anexo 5, SECCION 5.4.c)
  Entrada empate_posterior_pisos: pisos del vecino posterior existente.
  Si >= 3: retiro posterior = 0 en la huella (el aislamiento se exige solo
  por encima de la altura del vecino).

NOTA NORMATIVA (vecinos con alturas variables, SECCION 1.9.c - v08):
  El empate volumetrico lateral se calcula contra las edificaciones
  colindantes EXISTENTES por cada costado. Cuando un lateral colinda con
  VARIOS vecinos de alturas DIFERENTES, el retiro por piso se aplica por
  SEGMENTO: cada sub-segmento del lado usa la altura de su vecino (el retiro
  resultante es mayor donde el vecino es mas bajo, que es el caso mas
  desfavorable para el proyecto). La subdivision del lado se hace con las
  longitudes informadas o proporcional al numero de vecinos. Los lados
  Lateral sin vecinos informados usan altura_vecinos_m (global, v07).

ENTRADAS:
  lot_polygon (Curve)            - Lote simplificado
  sides_table_json (String)      - Clasificacion (F1_ETAPA2_LADOS_v03)
  patio_curves (Curve[])         - Patio(s) (F1_ETAPA2_PATIO_v02)
  altura_max_pot (Number)        - [OBSOLETO] Se mantiene para no romper canvas
  tratamiento (String)           - Tratamiento urbanistico
  rango_edificabilidad (String)  - Rango "1".."5" (tolerante a etiquetas)
  floor_height_user (Number)     - Altura entrepiso [m]
  io_maximo_user (Number)        - IO normativo (override)
  piso_adicional (bool)          - True si se acoge al incentivo normativo
  tipo_bonificacion (String)     - "NINGUNO" | "VIS" | "VIP" | "COMUNAL" |
                                   "EQUIPAMIENTO" | "EQUIPAMENTO+COMUNAL"
  tipologia (String)             - "Continua" (default) | "Aislada". Si es nula
                                   o vacia, se deriva de reglamentacion_json.
  ancho_via_m (Number)           - Ancho de via del frente [m] (medido entre
                                   bordes opuestos del perfil vial TOTAL;
                                   entrada del operador). Precedencia v06:
                                   operador > LADOS_v06 (sides_data) >
                                   reglamentacion > 0 (default).
  antejardin_m (Number)          - Override del retiro frontal [m] (valor
                                   oficial del mapa CU-5.5 si se conoce).
                                   Si 0/nulo, se deriva de reglamentacion_json
                                   o de la regla por ancho de via.
  empate_posterior_pisos (Number)- Pisos del vecino posterior existente
                                   (>=3 activa empate volumetrico)
  altura_vecinos_m (Number)      - [v07] Altura de las edificaciones
                                   colindantes (nivel de empate lateral,
                                   SECCION 1.9.c). Si 0/nulo: sin
                                   escalonamiento + aviso.
  empate_lateral_min_m (Number)  - [v07] Minimo del aislamiento lateral por
                                   empate (default 3,00m).
  voladizo_frontal_m (Number)    - [v07] Override del voladizo frontal [m]
                                   (SECCION 1.13.b). Si 0/nulo: se deriva del
                                   perfil vial (tabla 1.13.b, columna con
                                   antejardin). Aplica en pisos != 1, solo en
                                   lados Frontal (via).
  vecinos_por_lado_json (String) - [v08] Vecinos por lateral con alturas
                                   variables. JSON con dos formatos:
                                   (a) {"<id_lado>": [altura_m, ...], ...}
                                   (b) {"lados": [{"id": <id>,
                                       "vecinos": [{"altura_m": ..,
                                                     "longitud_m": ..}]}], ...}
                                   Cada lado Lateral listado se subdivide en
                                   tantos sub-segmentos como vecinos. Si no
                                   llega: comportamiento v07 (altura_vecinos_m
                                   global). El id del lado = indice del
                                   segmento del poligono (sides_table_json).
  frente_override_json (String)  - [v08.2] Override de frente por cardinal
                                   (salida de F0_LOAD_PROYECTO v01.4):
                                   {"<cardinal>": "via"|"via_no_frontal"|
                                   "predio"|"espacio_publico"}. La clasificacion
                                   confirmada por el operador manda sobre la
                                   geometrica; se casa por cardinal (normal
                                   saliente del lado). Sin cablear: se usa la
                                   clasificacion geometrica del LADOS.
  reglamentacion_json (String)   - JSON de reglamentacion (salida de
                                   F1_ETAPA1_CONTEXTO_v02: pot_data con
                                   tipologia/ancho_via_m/antejardin_m).
                                   Cadena de derivacion: operador >
                                   reglamentacion > default + aviso.

SALIDAS:
  envelope_curve (Curve/List)    - Huella del PISO 1 (base, con retiros y
                                   patio). Compatibilidad con F1_EXPORTAR_GFA
                                   y el contrato v06.
  envelope_por_piso (List)       - [v07] Curva de ocupacion POR PISO
                                   (escalonada + voladizos en pisos
                                   superiores). Fase 3 (VOLUM_GENERADOR_v07+)
                                   la consume.
  retiros_por_piso (String)      - [v07] JSON con el desglose por piso:
                                   altura, retiro lateral aplicado, voladizo,
                                   area, escalonado (bool).
  gfa_total (Number)             - GFA ESCALONADO = suma de areas por piso
                                   (incluye voladizos en pisos != 1)
  ocupacion_real, io_maximo, ic_real, ic_maximo,
  altura_total, pisos_finales, valido (bool), mensaje

VERSIONES:
  v08 (2026-08-16) - Vecinos con alturas VARIABLES por lateral (SECCION 1.9.c
                     por segmento) + recorte de la huella por SEMIPLANOS
                     (cajas exteriores + BooleanDifference), robusto en
                     concavos. Entrada vecinos_por_lado_json. Sin la entrada:
                     identico al v07.
  v07 (2026-08-16) - Envelope escalonado por pisos superiores (empate
                     volumetrico lateral Anexo 5 SECCION 1.9.c + separacion
                     sismica NSR-10 A.6.5; se toma el mayor) + VOLADIZOS
                     frontales (Anexo 5 SECCION 1.13.b) en pisos != 1.
================================================================================
"""

# Rhino.Geometry solo existe dentro de Rhino/Grasshopper (no en el .venv).
import Rhino.Geometry as rg  # type: ignore[reportMissingImports]
import json
import math
import re

# Rangos de edificabilidad corregidos según Decreto 555/2021
RANGO_PISOS = {"1": 1, "2": 2, "3": 4, "4": 5, "5": 7}
# Pisos extra por incentivo (Decreto 555/2021): normalizado a mayusculas
BONIFICACION_PISOS = {
    "NINGUNO": 0,
    "VIS": 2,
    "VIP": 2,
    "EQUIPAMENTO+COMUNAL": 2,
    "EQUIPAMIENTO+COMUNAL": 2,
    "COMUNAL": 1,
    "EQUIPAMIENTO": 1,
}
RANGO_DEFAULT = "3"
TOLERANCIA = 0.01

# Anexo 5 POT (Decreto 466/2024), SECCION 5.4.b - Consolidacion
# Altura maxima (pisos) -> dimension minima del aislamiento posterior [m]
POSTERIOR_CONSOLIDACION = [
    (3, 3.0), (6, 5.0), (9, 6.0), (12, 8.0), (15, 10.0),
    (18, 12.0), (22, 14.0), (25, 16.0), (28, 18.0), (99, 20.0),
]
# Anexo 5 POT, SECCION 1.9.b - lateral aislada: 1/5 altura, minimo
LATERAL_FRACCION_ALTURA = 0.2
LATERAL_MINIMO_M = 4.0
# Anexo 5 POT, SECCION 1.13.b - Voladizos (columna con antejardin/APAUP)
# Ancho de via [m] -> voladizo maximo [m] (pisos != 1, solo frontal)
VOLADIZO_POR_ANCHO_VIA = [
    (6.0, 0.0), (10.0, 0.60), (15.0, 0.80), (22.0, 1.00), (999.0, 1.50),
]
# v07 - Empate volumetrico lateral (SECCION 1.9.c) y separacion sismica NSR-10 A.6.5
EMPATE_LATERAL_MIN_M = 3.0        # minimo del aislamiento lateral por empate
NSR10_SEPARACION_COEF = 0.02      # Tabla A.6.5-1 >3 pisos: 0,01 sin vecina /
                                 # 0,02 losas coincidentes / 0,03 no coincidentes
                                 # (default 0,02, parametrizable via entrada)
NSR10_SEPARACION_COEF_RAW = None
# Regla historica pre-555 (respaldo cuando el mapa CU-5.5 no senala):
# ancho de via [m] -> antejardin [m]
FRONTAL_POR_ANCHO_VIA = [
    (12.0, 3.0), (20.0, 5.0), (999.0, 7.0),
]
ANTEJARDIN_DEFAULT_M = 3.0
TIPOLOGIA_DEFAULT = "Continua"


def unwrap(val):
    if val is None: return None
    if isinstance(val, list): return val[0] if len(val) > 0 else None
    return val


def safe_list(val):
    if val is None: return []
    if isinstance(val, list): return val
    return [val]


def parse_gh_bool(val):
    """Funcion a prueba de fallos para leer Toggles de Grasshopper"""
    if val is None: return False
    if isinstance(val, list): val = val[0] if len(val) > 0 else None
    if val is None: return False
    if isinstance(val, bool): return val
    s = str(val).strip().lower()
    if s in ("true", "1", "verdadero", "yes", "si"):
        return True
    return False


def normalize_rango(val, warnings):
    """Extrae el digito del rango aceptando etiquetas del Value List."""
    if val is None:
        return RANGO_DEFAULT
    s = str(unwrap(val)).strip()
    if s == "":
        return RANGO_DEFAULT
    m = re.search(r"(\d+)", s)
    if m and m.group(1) in RANGO_PISOS:
        return m.group(1)
    warnings.append(
        "rango_edificabilidad no reconocido ('%s') -> default %s"
        % (s, RANGO_DEFAULT))
    return RANGO_DEFAULT


def normalize_bonificacion(val, warnings):
    """Normaliza tipo_bonificacion a mayusculas sin espacios alrededor de +."""
    if val is None:
        return "NINGUNO"
    s = str(unwrap(val)).strip()
    if s == "":
        return "NINGUNO"
    s = s.upper()
    s = re.sub(r"\s*\+\s*", "+", s)
    s = re.sub(r"\s+", " ", s)
    s = s.replace("\u00c1", "A").replace("\u00c9", "E").replace("\u00cd", "I")
    s = s.replace("\u00d3", "O").replace("\u00da", "U").replace("\u00d1", "N")
    if s not in BONIFICACION_PISOS:
        warnings.append(
            "tipo_bonificacion desconocido ('%s') -> sin piso extra" % s)
        return "NINGUNO"
    return s


def normalize_tipologia(val, warnings):
    """Normaliza tipologia: 'Continua' (default) | 'Aislada'."""
    if val is None:
        return TIPOLOGIA_DEFAULT
    s = str(unwrap(val)).strip()
    if s == "":
        return TIPOLOGIA_DEFAULT
    s = s.replace("\u00c1", "A").replace("\u00cd", "I")
    s = s.title()
    if s not in ("Continua", "Aislada"):
        warnings.append(
            "tipologia desconocida ('%s') -> %s" % (s, TIPOLOGIA_DEFAULT))
        return TIPOLOGIA_DEFAULT
    return s


def parse_reglamentacion(raw):
    """Parsea la reglamentacion_json (salida de ETAPA1_v02).

    Retorna dict con pot_data o None si no es JSON valido.
    """
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
    """Lee un numero de reglamentacion_json (pot_data)."""
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
    """Lee un string de reglamentacion_json (pot_data)."""
    if reg_data is None:
        return default
    v = reg_data.get("pot_data", {}).get(campo)
    if v is None:
        return default
    s = str(v).strip()
    return s or default


def numero_opcional(raw):
    """None = ausente/invalido; cero es un valor explicito, no un default."""
    v = unwrap(raw)
    if v is None or str(v).strip() in ("", "None"):
        return None
    try:
        v = float(v)
        return v if not (math.isnan(v) or math.isinf(v)) else None
    except (ValueError, TypeError):
        return None


def retiro_posterior_consolidacion(pisos):
    """Tabla Consolidacion (Anexo 5 SECCION 5.4.b): pisos -> retiro [m]."""
    for limite, retiro in POSTERIOR_CONSOLIDACION:
        if pisos <= limite:
            return retiro
    return POSTERIOR_CONSOLIDACION[-1][1]


def retiro_lateral_empate(h_piso, h_vecino, min_m):
    """v07 - Aislamiento lateral por empate volumetrico (Anexo 5 SECCION 1.9.c):
    1/5 de la altura medida desde el nivel de empate, con minimo.
    Si el piso no supera al vecino colindante, retorno 0."""
    if h_vecino <= 0 or h_piso <= h_vecino:
        return 0.0
    h_exc = h_piso - h_vecino
    return max(LATERAL_FRACCION_ALTURA * h_exc, min_m)


def separacion_sismica_piso(h_piso, coef):
    """v07 - NSR-10 A.6.5 (Tabla A.6.5-1, >3 pisos aereos): s_i = coef x h_i."""
    if coef <= 0:
        return 0.0
    return coef * h_piso


def retiro_frontal_por_ancho_via(ancho_via_m):
    """Regla historica pre-555: ancho de via [m] -> antejardin [m]."""
    if ancho_via_m is None or ancho_via_m <= 0:
        return ANTEJARDIN_DEFAULT_M
    for limite, retiro in FRONTAL_POR_ANCHO_VIA:
        if ancho_via_m < limite:
            return retiro
    return FRONTAL_POR_ANCHO_VIA[-1][1]


def voladizo_por_perfil_vial(ancho_via_m):
    """v07 - Anexo 5 SECCION 1.13.b: voladizo frontal maximo segun el perfil
    vial (columna con antejardin/APAUP). 0 si no se permite."""
    if ancho_via_m is None or ancho_via_m <= 0:
        return 0.0
    for limite, vol in VOLADIZO_POR_ANCHO_VIA:
        if ancho_via_m <= limite:
            return vol
    return VOLADIZO_POR_ANCHO_VIA[-1][1]


def parsear_vecinos_por_lado(raw):
    """v08 - Parsea vecinos_por_lado_json a {lado_id: [(altura_m, longitud_m o
    None), ...]}. Acepta: (a) {"<id>": [altura, ...]}, (b) {"lados":
    [{"id": .., "vecinos": [{"altura_m": .., "longitud_m": ..}]}]}.
    Devuelve {} si no hay datos validos."""
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


# v08.2 - Puente orquestador -> canvas: override de frente por cardinal
# (misma convencion de azimut/cardinal que vecinos_por_lado.py).
CARDINAL_BANDS = [
    ("Norte", 315.0, 45.0),
    ("Oriente", 45.0, 135.0),
    ("Sur", 135.0, 225.0),
    ("Occidente", 225.0, 315.0),
]
FRENTE_A_CLASIFICACION = {
    "via": "Frontal",
    "via_no_frontal": "EspacioPublico",
    "espacio_publico": "EspacioPublico",
    "predio": "Lateral",
}


def _parsear_frente_override(raw):
    """v08.2 - Parsea frente_override_json {cardinal: frente}."""
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
    """v08.2 - Cardinal desde una normal (azimut = atan2(nx,ny) % 360)."""
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
    """v08.2 - Cardinal de un lado (normal saliente respecto al centroide)."""
    n1 = (-dy, dx)
    n2 = (dy, -dx)
    vx = mx - cx
    vy = my - cy
    d1 = vx * n1[0] + vy * n1[1]
    d2 = vx * n2[0] + vy * n2[1]
    nx, ny = (n1 if d1 >= d2 else n2)
    return _cardinal_normal(nx, ny)


def _poligono_ccw(curva):
    """v08 - True si la polilinea esta en sentido antihorario (area signada)."""
    success, poly = curva.TryGetPolyline()
    if not success or poly is None:
        return True
    s = 0.0
    c = poly.Count
    for i in range(c - 1):
        s += poly[i].X * poly[i + 1].Y - poly[i + 1].X * poly[i].Y
    return s > 0


def _area_signada_puntos(puntos):
    """v08 - Area con signo de una lista de Point3d (positiva = CCW)."""
    s = 0.0
    n = len(puntos)
    for i in range(n):
        p = puntos[i]
        q = puntos[(i + 1) % n]
        s += p.X * q.Y - q.X * p.Y
    return s / 2.0


def _curva_desde_puntos(puntos):
    """v08 - PolylineCurve cerrada desde una lista de Point3d."""
    if puntos is None or len(puntos) < 3:
        return None
    poly = rg.Polyline(puntos)
    if not poly.IsClosed:
        poly.Add(poly[0])
    return rg.PolylineCurve(poly)


def _vertices_curva(curva):
    """v08 - Vertices de la polilinea (con cierre)."""
    success, poly = curva.TryGetPolyline()
    if not success or poly is None:
        return []
    pts = [rg.Point3d(p.X, p.Y, 0.0) for p in poly]
    if len(pts) >= 2 and pts[0].DistanceTo(pts[-1]) > 0.001:
        pts.append(rg.Point3d(pts[0]))
    return pts


def _recortar_puntos(puntos, sub_segmentos):
    """v08 - Sutherland-Hodgman por semiplanos sobre PUNTOS (sin cajas ni
    booleanos): cada sub-segmento con retiro > 0 recorta el poligono contra la
    linea desplazada hacia adentro. Robusto en concavos, chaflanes exactos y
    SIEMPRE devuelve un poligono CONEXO (una curva por piso). Devuelve lista
    de Point3d (cerrada) o None si se degenera."""
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
        if ccw:
            nx, ny = -uy, ux
        else:
            nx, ny = uy, -ux
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
                nuevo.append(rg.Point3d(p.X + t * (q.X - p.X),
                                        p.Y + t * (q.Y - p.Y), 0.0))
        poly = nuevo
        if len(poly) < 3:
            return None
    return poly


# PROPUESTA v08.5: nueva entrada Item/No Type Hint vecinos_intervalos_json
# desde F1_ETAPA2_LADOS_v06.py v06.7. Recortes locales rectangulares en XY;
# extremos a escuadra (no resuelve encuentros/miter ni regimen patrimonial).
# NUEVA salida recortes_intervalos_json: diagnostico numerico por piso.
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
    """Resta tiras limitadas al tramo; mantiene exteriores y huecos.
    BooleanDifference se aplica a la coleccion de contornos como region.
    Una operacion no verificable rechaza el piso, no inventa area.
    """
    cutters = list(patios)
    for (a, b), r in subs:
        if r <= 0:
            continue
        dx, dy = b.X-a.X, b.Y-a.Y
        length = math.hypot(dx, dy)
        if length <= 1e-8:
            continue
        nx, ny = (-dy/length, dx/length) if ccw else (dy/length, -dx/length)
        # Ligero solape hacia fuera; no alargar el tramo longitudinalmente.
        margen_exterior = 5.0 * TOLERANCIA
        pts = [rg.Point3d(a.X-nx*margen_exterior, a.Y-ny*margen_exterior, 0),
               rg.Point3d(b.X-nx*margen_exterior, b.Y-ny*margen_exterior, 0),
               rg.Point3d(b.X+nx*r, b.Y+ny*r, 0),
               rg.Point3d(a.X+nx*r, a.Y+ny*r, 0)]
        cutters.append(_curva_desde_puntos(pts))
    if not cutters:
        return [lote], area_curve(lote)
    # Tiras contiguas y patios pueden solaparse: unir ANTES de restar.
    # Solape hacia fuera > tolerancia evita contactos numericamente coincidentes.
    for index, cutter in enumerate(cutters):
        if cutter is None or not cutter.IsClosed or not cutter.IsValid:
            raise ValueError('cortador {} no cerrado/valido'.format(index))
    merged = rg.Curve.CreateBooleanUnion(cutters, TOLERANCIA)
    if not merged:
        raise ValueError('Union de {} cortadores fallida'.format(len(cutters)))
    diff = rg.Curve.CreateBooleanDifference(lote, list(merged), TOLERANCIA)
    if not diff:
        raise ValueError('Diferencia vacia/fallida: {} cortadores -> {} contornos unidos'.format(
            len(cutters),len(merged)))
    diff = list(diff)
    area = _region_area(diff)
    if area > area_curve(lote) + TOLERANCIA**2:
        raise ValueError('Recorte aumento el area')
    return diff, area


def _subdividir_lado(p1, p2, vecinos):
    """v08 - Subdivide el segmento (p1,p2) en tantas partes como vecinos.
    Longitudes proporcionales a las informadas; si ninguna se informa, partes
    iguales. Devuelve lista de puntos (len = len(vecinos)+1)."""
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
        # normalizar (si alguna es 0, repartir el resto proporcional)
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
                       empate_activo=True):
    """v08.1 - Construye la lista de (sub-segmento, retiro) para un piso.
    Lados Lateral con vecinos informados: un sub-segmento por vecino (retiro
    por empate con SU altura). Lados Lateral sin vecinos: altura_vecinos_m
    global (v07). Frontal en pisos != 1: antejardin - voladizo.
    Anexo 5, SECCION 1.9.c: el empate volumetrico lateral aplica SOLO a
    predios con lado POSTERIOR; para predios con dos laterales y al menos
    una esquina (sin lado posterior) NO aplica -> rige SOLO la separacion
    sismica NSR-10 A.6.5 (2% x h) con vecinos construidos."""
    h_piso = nv * floor_h
    # La separacion sismica no toca el piso 1: la huella define la OCUPACION
    # del lote (IO); el escalonamiento por sismica/empate actua de N2 en
    # adelante.
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
            for j in range(len(sub_pts) - 1):
                r = max(retiro_base, r_sismica)
                if empate_activo:
                    h_vec = vecs[j][0]
                    r = max(r, retiro_lateral_empate(h_piso, h_vec, empate_lateral_min))
                subs.append(((sub_pts[j], sub_pts[j + 1]), r))
        elif cls == "Lateral":
            r = max(retiro_base, r_sismica)
            if empate_activo:
                r = max(r, retiro_lateral_empate(h_piso, altura_vecinos_m, empate_lateral_min))
            subs.append(((p1, p2), r))
        elif cls == "Frontal" and nv > 1 and voladizo_frontal > 0:
            r = max(0.0, retiro_base - voladizo_frontal)
            subs.append(((p1, p2), r))
        else:
            subs.append(((p1, p2), retiro_base))
    return subs


def area_curvas(curva_o_lista):
    """v08 - Area de una curva o lista de curvas (piso partido en piezas)."""
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


def extract_segments(curve):
    if curve is None: return []
    success, poly = curve.TryGetPolyline()
    if not success or poly is None: return []
    c = poly.Count
    is_closed = (c >= 2 and poly[0].DistanceTo(poly[c-1]) < 0.001)
    n = c - 1 if is_closed else c
    return [rg.Line(poly[i], poly[(i+1) % c]) for i in range(n)]


def centroide_puntos(puntos):
    sx = sum(p.X for p in puntos)
    sy = sum(p.Y for p in puntos)
    n = len(puntos)
    return rg.Point3d(sx / n, sy / n, 0)


def interseccion_lineas_2d(a1, a2, b1, b2):
    dx1 = a2.X - a1.X; dy1 = a2.Y - a1.Y
    dx2 = b2.X - b1.X; dy2 = b2.Y - b1.Y
    denom = dx1 * dy2 - dy1 * dx2
    if abs(denom) < 1e-9:
        return None
    t = ((b1.X - a1.X) * dy2 - (b1.Y - a1.Y) * dx2) / denom
    return rg.Point3d(a1.X + t * dx1, a1.Y + t * dy1, 0)


def build_footprint_retiros(lot_polygon, retiros):
    segs = extract_segments(lot_polygon)
    if not segs:
        return lot_polygon

    n = len(segs)
    ctr = centroide_puntos([seg.From for seg in segs])

    lineas_desplazadas = []
    for i, seg in enumerate(segs):
        sb = retiros.get(i, 0.0)
        if sb < 0.01:
            lineas_desplazadas.append((seg.From, seg.To))
            continue
        normal = inward_normal(seg, ctr)
        p1 = rg.Point3d(seg.From.X + normal.X * sb, seg.From.Y + normal.Y * sb, 0)
        p2 = rg.Point3d(seg.To.X + normal.X * sb, seg.To.Y + normal.Y * sb, 0)
        lineas_desplazadas.append((p1, p2))

    pts_nuevos = []
    for i in range(n):
        j = (i + 1) % n
        a1, a2 = lineas_desplazadas[i]
        b1, b2 = lineas_desplazadas[j]
        inter = interseccion_lineas_2d(a1, a2, b1, b2)
        if inter is None:
            inter = a2
        pts_nuevos.append(inter)

    poly = rg.Polyline()
    for p in pts_nuevos:
        poly.Add(p.X, p.Y, p.Z)
    if not poly.IsClosed:
        poly.Add(poly[0])
    return rg.PolylineCurve(poly)


def inward_normal(seg, centroid):
    mid = rg.Point3d((seg.From.X + seg.To.X) / 2.0,
                     (seg.From.Y + seg.To.Y) / 2.0, 0)
    to_ctr = rg.Vector3d(centroid.X - mid.X, centroid.Y - mid.Y, 0)
    sd = rg.Vector3d(seg.To.X - seg.From.X, seg.To.Y - seg.From.Y, 0)
    sd.Unitize()
    n1 = rg.Vector3d(-sd.Y, sd.X, 0)
    n2 = rg.Vector3d(sd.Y, -sd.X, 0)
    return n1 if (n1.X * to_ctr.X + n1.Y * to_ctr.Y) > (n2.X * to_ctr.X + n2.Y * to_ctr.Y) else n2


# ==============================================================================
# MAIN
# ==============================================================================

lot_polygon = globals().get("lot_polygon", None)
sides_raw = globals().get("sides_table_json", None)
patio_raw = globals().get("patio_curves", None)
altura_raw = globals().get("altura_max_pot", None) # Se ignora, pero se mantiene para no romper el input del canvas
tratamiento_raw = globals().get("tratamiento", None)
rango_raw = globals().get("rango_edificabilidad", None)
floor_h_raw = globals().get("floor_height_user", None)
io_user_raw = globals().get("io_maximo_user", None)
tipologia_raw = globals().get("tipologia", None)
ancho_via_raw = globals().get("ancho_via_m", None)
antejardin_raw = globals().get("antejardin_m", None)
empate_posterior_raw = globals().get("empate_posterior_pisos", None)
altura_vecinos_raw = globals().get("altura_vecinos_m", None)       # v07
empate_lateral_min_raw = globals().get("empate_lateral_min_m", None)  # v07
nsr_coef_raw = globals().get("nsr10_separacion_coef", None)        # v07
voladizo_raw = globals().get("voladizo_frontal_m", None)           # v07
vecinos_raw = globals().get("vecinos_por_lado_json", None)         # v08
frente_override_raw = globals().get("frente_override_json", None)  # v08.2
reglamentacion_raw = globals().get("reglamentacion_json", None)

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

# sides_data se parsea ANTES del ancho: en v06 es respaldo de ancho_via_m
# (la salida del LADOS_v06 ya transporta ancho_via_m dentro del JSON)
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
# v08.2 (2026-08-23): lote de esquina (2+ vertices con contacto real a
# via/EP) -> sin aislamiento posterior; solo el frente lleva antejardin y
# la esquina interior lleva patio 3x3 (PATIO).
es_esquina = bool(sides_data.get("es_esquina", False)) if sides_data else False
frente_override = _parsear_frente_override(frente_override_raw)
if frente_override:
    # la regla de esquina sigue al override del operador (2+ lados de calle).
    # v08.3: "via_no_frontal" tambien cuenta como via (el lote es esquina
    # si tiene 2+ lados de calle, aunque uno no sea el frente principal),
    # para no generar patio posterior en esquina con via secundaria sin antejardin.
    _n_vias = sum(1 for v in frente_override.values()
                  if v in ("via", "via_no_frontal"))
    if _n_vias >= 2:
        es_esquina = True

# No deducir esquina normativa de dos frentes: requerir decision explicita.
es_esquina_raw = globals().get("es_esquina_confirmada", None)
if es_esquina_raw is not None:
    es_esquina = parse_gh_bool(es_esquina_raw)
else:
    es_esquina = False
    warnings.append("esquina normativa sin confirmar: no se elimina retiro posterior por esa regla")

# --- Anexo 5, SECCION 1.9.c (v08.1): el empate volumetrico lateral aplica
# SOLO a predios con lado POSTERIOR (lote interior/fondo). Para predios con
# dos laterales y al menos una esquina (sin lado posterior) NO aplica: rige
# SOLO la separacion sismica NSR-10 A.6.5 (2% x h) con vecinos construidos.
aplica_empate_raw = globals().get("aplica_empate_lateral", None)
if aplica_empate_raw is not None and str(unwrap(aplica_empate_raw)).strip() not in ("", "None"):
    empate_activo = parse_gh_bool(aplica_empate_raw)
    warnings.append("empate 1.9.c %s por entrada" % ("activo" if empate_activo else "inactivo"))
else:
    empate_activo = any(
        str(lado.get("clasificacion", "")).strip().lower() == "posterior"
        for lado in lados)
    if empate_activo:
        warnings.append("empate 1.9.c activo: predio con lado posterior")
    else:
        warnings.append("empate 1.9.c NO aplica: predio sin lado posterior "
                        "(dos laterales y esquina) -> solo sismica NSR-10 A.6.5")

# --- Tipologia: operador > reglamentacion > Continua ---
tipologia = normalize_tipologia(tipologia_raw, warnings)
if tipologia == TIPOLOGIA_DEFAULT:
    tipologia_reg = dato_reglamentario_str(reglamentacion_data, "tipologia")
    if tipologia_reg:
        tipologia = normalize_tipologia(tipologia_reg, warnings)
        warnings.append("tipologia desde reglamentacion ('%s')" % tipologia)
    elif tipologia_raw is None or str(unwrap(tipologia_raw)).strip() == "":
        warnings.append(
            "tipologia no definida y sin dato reglamentario -> %s" % TIPOLOGIA_DEFAULT)

# --- Entradas numericas nuevas (v06) ---
try:
    ancho_via_m = float(unwrap(ancho_via_raw)) if ancho_via_raw else 0.0
except:
    ancho_via_m = 0.0

# --- Ancho de via: operador > LADOS_v06 (sides_data) > reglamentacion > 0 ---
if ancho_via_m <= 0:
    ancho_via_m = dato_reglamentario_num(reglamentacion_data, "ancho_via_m", 0.0)
    if ancho_via_m > 0:
        warnings.append("ancho_via_m desde reglamentacion ({:.1f}m)".format(ancho_via_m))
if ancho_via_m <= 0 and sides_data:
    ancho_via_m = float(sides_data.get("ancho_via_m") or 0.0)
    if ancho_via_m > 0:
        warnings.append(
            "ancho_via_m desde LADOS_v06 ({:.1f}m; antejardin por tabla)".format(ancho_via_m))

# Cero explicito se conserva; solo None permite derivacion.
antejardin_m = numero_opcional(antejardin_raw)
if antejardin_m is None:
    antejardin_m = numero_opcional(
        (reglamentacion_data or {}).get("pot_data", {}).get("antejardin_m"))
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
# Voladizo frontal: override del operador > perfil vial (SECCION 1.13.b)
voladizo_frontal = voladizo_override if voladizo_override > 0 else \
    voladizo_por_perfil_vial(ancho_via_m)
if voladizo_override <= 0 and voladizo_frontal > 0:
    warnings.append(
        "voladizo frontal {:.2f}m por perfil vial (SECCION 1.13.b)".format(
            voladizo_frontal))

# v08 - Vecinos con alturas variables por lateral (SECCION 1.9.c por segmento)
vecinos_por_lado = parsear_vecinos_por_lado(vecinos_raw)
total_vecinos = sum([len(v) for v in vecinos_por_lado.values()])
if total_vecinos > 0:
    warnings.append(
        "vecinos por lado (v08): {} lados, {} vecinos".format(
            len(vecinos_por_lado), total_vecinos))
elif vecinos_raw is not None and str(vecinos_raw).strip() != "":
    warnings.append(
        "vecinos_por_lado_json sin datos validos -> modo v07 (altura global)")

try:
    floor_h = float(unwrap(floor_h_raw)) if floor_h_raw else 3.0
except:
    floor_h = 3.0

try:
    io_user = float(unwrap(io_user_raw)) if io_user_raw else 0.0
except:
    io_user = 0.0

tratamiento = str(unwrap(tratamiento_raw)) if tratamiento_raw else "Consolidacion"

# --- PISOS Y ALTURA (antes que retiros: el posterior/lateral dependen de pisos) ---
ic_maximo_base = RANGO_PISOS.get(rango, RANGO_PISOS[RANGO_DEFAULT])

pisos_extra = 0
if piso_adicional:
    pisos_extra = BONIFICACION_PISOS.get(tipo_bonificacion, 0)

pisos_propuestos = ic_maximo_base + pisos_extra
pisos_limite = numero_opcional(globals().get("pisos_maximos_total", None))
if pisos_limite is None:
    pisos_limite = numero_opcional((reglamentacion_data or {}).get(
        "pot_data", {}).get("altura_maxima_pisos"))
if pisos_limite is not None:
    if pisos_limite < 1 or abs(pisos_limite - round(pisos_limite)) > 1e-6:
        bloqueos.append("limite de pisos no entero positivo")
    else:
        pisos_limite = int(round(pisos_limite))
        if pisos_propuestos > pisos_limite:
            warnings.append("{} pisos solicitados -> {} total incluyendo bonos; "
                            "no se acumulan adicionales fuera del limite".format(
                                pisos_propuestos, pisos_limite))
        pisos_propuestos = min(pisos_propuestos, pisos_limite)
else:
    bloqueos.append("falta total de pisos incluyendo bonificaciones")
if floor_h <= 0:
    bloqueos.append("altura entrepiso no positiva")
    floor_h = 3.0
pisos_finales = pisos_propuestos
pisos_extra = max(0, pisos_finales - ic_maximo_base)
ic_maximo = pisos_finales  # compat legacy: este puerto es PISOS, no un IC legal
altura_total = pisos_finales * floor_h

# --- RETIROS POR CLASIFICACION (v06) ---
# Antejardin frontal: override del mapa CU-5.5 > regla por ancho de via
if antejardin_m is not None:
    antejardin = antejardin_m
else:
    antejardin = retiro_frontal_por_ancho_via(ancho_via_m)
    if ancho_via_m <= 0:
        warnings.append(
            "sin ancho_via_m -> antejardin provisional {:.1f}m (ver mapa CU-5.5)".format(antejardin))
        bloqueos.append("antejardin sin dato explicito y ancho vial desconocido")

# Posterior: empate volumetrico (SECCION 5.4.c) si el vecino tiene 3+ pisos.
# v08.2: en lote de esquina NO aplica aislamiento posterior (solo el frente
# lleva antejardin); el lado "Posterior" se trata como colindante sin retiro
# y la esquina interior lleva patio 3x3 (PATIO).
empate_posterior = empate_posterior_pisos >= 3.0
if es_esquina:
    retiro_posterior = 0.0
    warnings.append(
        "lote de esquina: sin aislamiento posterior (patio 3x3 en esquina interior)")
elif empate_posterior:
    retiro_posterior = 0.0
else:
    retiro_posterior = retiro_posterior_consolidacion(pisos_finales)

# Lateral: 0 en continua; 1/5 altura min 4m en aislada (SECCION 1.9.b)
if tipologia == "Aislada":
    retiro_lateral = max(LATERAL_FRACCION_ALTURA * altura_total, LATERAL_MINIMO_M)
else:
    retiro_lateral = 0.0

# --- Inicializar outputs ---
envelope_curve = None
envelope_por_piso = []
retiros_por_piso = ""
ocupacion_real = 0.0
valido = False
area_lote = area_curve(lot_polygon) if lot_polygon else 0.0

# --- 1. Patios (lista + area) ---
patios_list = [p for p in safe_list(patio_raw) if p is not None]
patio_area_total = 0.0
for patio in patios_list:
    patio_area_total += area_curve(patio)


def envelope_final(huella):
    """Aplica la resta de patios a una huella; devuelve (curva, area)."""
    if huella is None:
        return None, 0.0
    if not patios_list:
        return huella, area_curve(huella)
    try:
        diff = rg.Curve.CreateBooleanDifference(huella, patios_list, TOLERANCIA)
        if diff and len(diff) > 0:
            # Medir regiones con huecos, no sumar areas absolutas de contornos.
            breps = rg.Brep.CreatePlanarBreps(list(diff), TOLERANCIA)
            if not breps:
                raise ValueError("no se pudieron construir regiones planas")
            area = 0.0
            for brep in breps:
                props = rg.AreaMassProperties.Compute(brep)
                if props is None:
                    raise ValueError("region sin area verificable")
                area += props.Area
            if area < 0 or area > area_curve(huella) + TOLERANCIA ** 2:
                raise ValueError("area de diferencia incoherente")
            return (list(diff) if len(diff) > 1 else diff[0]), area
        raise ValueError("diferencia vacia o fallida")
    except Exception as exc:
        bloqueos.append("booleana de patios no verificable: {}".format(str(exc)))
        # No devolver curva intacta con area descontada ficticiamente.
        return None, 0.0

# --- 2. Retiros base por lado (v06) + override del operador (v08.2) ---
# v08.2: la clasificacion confirmada en 1b·1c manda sobre la geometrica;
# se casa por cardinal (normal saliente del lado respecto al centroide).
_centroide_lote = None
if lot_polygon is not None and frente_override:
    _vpre = _vertices_curva(lot_polygon)
    if _vpre:
        _npre = len(_vpre)
        _centroide_lote = (sum(v.X for v in _vpre) / _npre,
                           sum(v.Y for v in _vpre) / _npre)

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
            _card = _cardinal_lado(_dx, _dy, _mx, _my,
                                   _centroide_lote[0], _centroide_lote[1])
            if _card in frente_override:
                cls = FRENTE_A_CLASIFICACION[frente_override[_card]]
        except Exception:
            pass
    if cls == "Frontal":
        retiros_base[idx] = antejardin
    elif cls == "Posterior":
        retiros_base[idx] = retiro_posterior
    elif cls == "EspacioPublico":
        retiros_base[idx] = 0.0
    else:
        retiros_base[idx] = retiro_lateral

# --- 3. Envelopes: contrato de intervalos verificado o fallback provisional ---
huellas_por_piso = []
areas_por_piso = []
recortes_intervalos_json = '[]'
diag_recortes = []
intervalos = {}
vertices_lote = _vertices_curva(lot_polygon) if lot_polygon is not None else []
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
    n_edges = len(vertices_lote)-1
    for entry in data_int.get('lados') or []:
        lid = entry.get('id')
        if not isinstance(lid, int) or not 0 <= lid < n_edges or lid in intervalos:
            raise ValueError('id de intervalo invalido/duplicado')
        spans = sorted(entry.get('subtramos') or [], key=lambda s: s['t0'])
        cursor = 0.0
        if entry.get('es_colindancia_predial'):
            for span in spans:
                t0, t1 = float(span['t0']), float(span['t1'])
                if not 0 <= t0 < t1 <= 1 or abs(t0-cursor) > 0.01:
                    raise ValueError('intervalos con huecos/solapes en L{}'.format(lid))
                cursor = t1
                if span.get('altura_m') is None or float(span['altura_m']) <= 0:
                    bloqueos.append('altura pendiente L{} raw {}'.format(lid,span.get('segmento_raw')))
            if abs(cursor-1.0) > 0.01:
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

if lot_polygon is not None and vertices_lote:
    for nv in range(1, pisos_finales + 1):
        if intervalos:
            subs = []
            for i in range(len(vertices_lote)-1):
                a, b = vertices_lote[i], vertices_lote[i+1]
                cls = next((l.get('clasificacion') for l in lados if l.get('id') == i), 'Lateral')
                base = retiros_base.get(i, 0.0)
                seismic = separacion_sismica_piso(nv*floor_h, nsr_coef) if pisos_finales > 3 and nv > 1 else 0.0
                if cls in ('Lateral','Posterior'):
                    for span in intervalos[i].get('subtramos') or []:
                        t0, t1 = float(span['t0']), float(span['t1'])
                        p = rg.Point3d(a.X+(b.X-a.X)*t0,a.Y+(b.Y-a.Y)*t0,0)
                        q = rg.Point3d(a.X+(b.X-a.X)*t1,a.Y+(b.Y-a.Y)*t1,0)
                        r = max(base, seismic) if cls == 'Lateral' else base
                        h = span.get('altura_m')
                        if cls == 'Lateral' and empate_activo and h is not None:
                            r = max(r,retiro_lateral_empate(nv*floor_h,float(h),empate_lateral_min))
                        subs.append(((p,q),r))
                        diag_recortes.append({'piso':nv,'id':i,'t0':t0,'t1':t1,
                                              'retiro_m':r,'altura_vecino_m':h})
                else:
                    r = max(0.,base-voladizo_frontal) if cls == 'Frontal' and nv > 1 else base
                    subs.append(((a,b),r))
        else:
            subs = _subsegmentos_piso(nv,lados,vertices_lote,retiros_base,
                vecinos_por_lado,altura_vecinos_m,empate_lateral_min,nsr_coef,
                pisos_finales,floor_h,voladizo_frontal,empate_activo)
        try:
            envs, area = _recortar_regiones_locales(lot_polygon,subs,patios_list,
                                                   _area_signada_puntos(vertices_lote)>0)
            huellas_por_piso.append(envs[0] if len(envs)==1 else envs)
            areas_por_piso.append(area)
        except Exception as exc:
            huellas_por_piso.append(None)
            areas_por_piso.append(0.0)
            bloqueos.append('piso {} recorte no verificable: {}'.format(nv,str(exc)))
recortes_intervalos_json = json.dumps(diag_recortes,ensure_ascii=True)

envelope_por_piso = huellas_por_piso
if envelope_por_piso:
    envelope_curve = envelope_por_piso[0]
ocupacion_real = areas_por_piso[0] if areas_por_piso else 0.0

# Desglose por piso: retiro lateral maximo por lado (para diagnostico)
escalonados = []
for nv in range(1, pisos_finales + 1):
    h_piso = nv * floor_h
    r_sismica = separacion_sismica_piso(h_piso, nsr_coef) \
        if (pisos_finales > 3 and nv > 1) else 0.0
    retiro_max = 0.0
    for i, lado in enumerate(lados):
        if lado.get("clasificacion", "Lateral") != "Lateral":
            continue
        lid = lado.get("id", i)
        r_l = 0.0
        if empate_activo:
            if lid in vecinos_por_lado:
                r_l = max([retiro_lateral_empate(h_piso, v[0], empate_lateral_min)
                           for v in vecinos_por_lado[lid]] or [0.0])
            else:
                r_l = retiro_lateral_empate(h_piso, altura_vecinos_m, empate_lateral_min)
        retiro_max = max(retiro_max, r_l, r_sismica)
    if retiro_max > 0:
        escalonados.append(nv)

try:
    retiros_por_piso = json.dumps([
        {"piso": i + 1, "altura_m": round((i + 1) * floor_h, 2),
         "area_m2": round(areas_por_piso[i], 2),
         "escalonado": (i + 1) in escalonados,
         "voladizo_frontal_m": round(voladizo_frontal if i > 0 else 0.0, 2),
         "vecinos_por_lado": {str(k): [round(v[0], 2) for v in vs]
                               for k, vs in vecinos_por_lado.items()}}
        for i in range(pisos_finales)
    ], ensure_ascii=False)
except:
    retiros_por_piso = "[]"

# --- 4. Validacion y Indices ---
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
if area_lote > 0 and ocupacion_real > area_lote * io_maximo + TOLERANCIA ** 2:
    bloqueos.append("IO real {:.4f} > limite {:.4f}; excedente {:.2f} m2".format(
        io_real, io_maximo, ocupacion_real - area_lote * io_maximo))
if len(areas_por_piso) != pisos_finales or any(a <= 0 for a in areas_por_piso):
    bloqueos.append("uno o mas niveles sin region valida")
valido = not bloqueos

# --- 5. GFA ESCALONADO (suma de areas por piso) e indices ---
gfa_total = sum(areas_por_piso)
ic_real = (gfa_total / area_lote) if area_lote > 0 else 0.0

gfa_base = ocupacion_real * pisos_finales

if valido:
    empate_txt = "NO aplica (sin lado posterior): solo sismica 2%xh" \
        if not empate_activo else "activo (lado posterior)"
    mensaje = ("NORMATIVA v08.5.1 | CONTROLES IMPLEMENTADOS OK (no certificacion) | Lote: {:.1f}m2 | Ocup: {:.1f}m2 | IO max {:.2f} | "
               "IC {:.2f} (+{}) | Alt {:.1f}m | {} pisos | GFA escalonado: {:.1f}m2 "
               "(base {:.1f}m2) | Escalonados: {} pisos | "
               "Voladizo frontal {:.2f}m (piso 2+) | Vecinos por lado: {} lados, {} vecinos | "
               "Empate 1.9.c: {} | "
               "Patios {:.1f}m2 | Tipo:{} | Antejardin {:.1f}m (via {:.1f}m) | "
               "Lat {:.1f}m | Post {:.1f}m{}").format(
        area_lote, ocupacion_real, io_maximo, ic_real, pisos_extra, altura_total,
        pisos_finales, gfa_total, gfa_base, len(escalonados),
        voladizo_frontal, len(vecinos_por_lado), total_vecinos, empate_txt,
        patio_area_total, tipologia, antejardin,
        ancho_via_m, retiro_lateral, retiro_posterior,
        " (empate)" if empate_posterior else "")
else:
    mensaje = ("NORMATIVA v08.5.1 | NO VALIDADO | Lote {:.2f} m2 | "
               "Ocup {:.2f} m2 | IO real {:.4f} / max {:.4f} | {} pisos | "
               "Alt {:.2f} m | GFA geometrico provisional {:.2f} m2 | {}").format(
                   area_lote, ocupacion_real, io_real, io_maximo,
                   pisos_finales, altura_total, gfa_total,
                   "; ".join(sorted(set(bloqueos))))

if altura_vecinos_m <= 0:
    warnings.append(
        "sin altura_vecinos_m -> sin escalonamiento lateral (SECCION 1.9.c)")

if warnings:
    mensaje += " | AVISOS: " + "; ".join(warnings)
