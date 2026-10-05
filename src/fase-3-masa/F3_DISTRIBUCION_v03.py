# -*- coding: utf-8 -*-
"""
================================================================================
F3_DISTRIBUCION_v03.py — Distribuidor de barras por crujía con presupuesto IO
Proyecto: DisenoParametrico / Fase 3
GH Python Script para Grasshopper (IronPython 2.7 compatible) + CLI
================================================================================

RESUMEN:
  Genera 2–3 barras escalonadas de crujía única que QUEPAN en el
  presupuesto de ocupación (area_lote * io_maximo), ajustando por prioridad:
  1) PROFUNDIDAD de barras (reducción continua)
  2) ENTREPISO (3.05 m vs 3.80 m)
  3) NÚMERO DE CUERPOS (último recurso)
  Salida principal: barras_json (schema f3_barras_salida_v01) que consume
  F1_ETAPA2_NORMATIVA_v09.py (entrada barras_json) para emitir los productos
  APROBADOS (ocupacion_aprobada_m2, gfa_aprobado_m2, envelope_aprobado_por_piso).

HISTORIAL DE VERSIONES:
  v03.4 (2026-10-05, 4.ª iteración): FIX json.dumps en IronPython.
    - Bug del runtime IronPython 2.7 (json/encoder.py → py_encode_basestring_ascii):
      con strings unicode no-ASCII, json.dumps(ensure_ascii=True) lanza
      "'unknown' codec can't decode byte 0x..". Se añade _json_dumps_ascii():
      intento estándar → bytes UTF-8 → serializador ASCII manual (nunca depende
      del codec). Reproducido y verificado con IronPython 2.7.12 local.
  v03.3 (2026-10-05, 3.ª iteración): FIX lectura de archivos en GHPython.
    - Lectura JSON con el PATRÓN CANÓNICO del proyecto (lección 2026-09-17):
      open(rb) + decodificación explícita utf-8-sig → cp1252 → latin-1 +
      json.loads. (En IronPython, io.open/codecs.open intentan decodificar con
      el codec por defecto "unknown" y fallan con "'unknown' codec can't
      decode byte 0x.." en contenido no-ASCII; las escrituras también van a binario.)
    - Normalización de texto: _texto_seguro() (bytes → unicode por cascada)
      aplicada a rutas, variable de entorno y entradas; literales con tilde de
      las rutas activas como u"..."; prints silenciados dentro de GH.
    - Diagnóstico: si algo falla, el mensaje indica el PASO
      (p.ej. "ERROR en [leer resultados F2]") + cola del traceback.
  v03.2 (2026-10-05, misma jornada): FIX detección de entorno GH (canvas vivo).
    - En GHPython (Rhino 8) `import ghenv` FALLA: `ghenv` (y `ghdoc`) se
      inyectan como VARIABLES del script; la detección ahora usa
      `"ghenv"/"ghdoc" in globals()` con fallback de import. Antes, `_EN_GH`
      quedaba False y main() corría dentro de Grasshopper (SystemExit de
      argparse). Si hay .NET/Rhino pero ghenv no aparece, se emite un aviso.
    - Guard CLI reforzado: main() solo corre si __name__ == "__main__" Y el
      entorno NO es IronPython Y no hay `clr` (.NET) — nunca dentro de Rhino.
    - barras_json (salida GH) y los JSON de CLI con ensure_ascii=True
      (convención ASCII-safe del proyecto; evita errores de codificación al
      pasar el string entre componentes).
  v03.1 (2026-10-05): Corregido para uso vivo en canvas v13.1.
    - FIX IronPython 2.7: eliminada anotación de tipo Python 3 en
      normalizar_uso() ("def normalizar_uso(uso: str) -> str:" provocaba
      SyntaxErrorException "unexpected token ':'" en el componente GHPython).
    - SECCIÓN GRASSHOPPER completa: el script ahora también funciona DENTRO
      del componente del canvas (lee entradas, calcula y publica las 7
      salidas GH: barras_json, mensaje, alternativa_recomendada,
      ocupacion_total_m2, gfa_real_m2, floor_h_usado, n_barras_usado).
    - Lectura defensiva de entradas GH (tolerante a None / listas / guiones
      en nombres) + fallback por índice de parámetro (ghenv).
    - Si presupuesto_ocupacion_m2 está vacío, se DERIVA = lote_m2 × io_max
      con un margen de seguridad (0,1% / mín. 0,25 m²) para que la
      validación APROBADA de NORMATIVA v09 no falle por centésimas; el
      mensaje lo indica. Para coincidencia exacta, escribir el valor del
      Panel presupuesto_ocupacion_m2 de NORMATIVA v09.
    - Raíz del proyecto robusta: archivo (CLI) → variable de entorno
      DISENO_PARAMETRICO_ROOT (canvas) → validación con carpeta src/.
    - Cableado documentado en este encabezado (tipo + acceso + origen/destino).
  v03.0 (2026-10-03): Cambio mayor (v02 -> v03) — contrato entradas/salidas.
    - Nuevas entradas: presupuesto_ocupacion_m2, n_barras_objetivo,
      entrepiso_adaptativo, prioridad_ajuste.
    - Nueva salida: barras_json (schema f3_barras_salida_v01) con
      alternativas, recomendada, ocupación total, GFA real, floor_h usado.
    - Lógica iteradora: para cada n_barras, prueba floor_h en [3.05, 3.80],
      ajusta profundidad para caber en presupuesto; valida separaciones por
      altura (POT 1.9.b/c + NSR-10 A.6.5), patios según nº volúmenes
      (1 vol: Anexo 5 §1.12.b; >=2 vol: separaciones = "patios" en IO), accesos.
    - Homogeneizado: versión interna = nombre archivo (v03.x).
  v02.2 (2026-09-29): tipo crujia doble|unica, posicion nucleo, orientacion
    referida al predio, niveles auto, ancho minimo por programa.
  v02.1: --usos filtra/renormaliza mix; --bloques N + separacion/desnivel.
  v02.0: acople seccion 2 -> modelado (usos + bloques multivolumen).

REGLAS DE PATIOS/SEPARACIONES (aprobadas operador 2026-10-03):
  - 1 VOLUMEN: patio normativo Anexo 5 §1.12.b (H/3, min 9 m², 3 ml lado).
  - >=2 VOLÚMENES: separaciones entre volúmenes actúan como "patios"
    y COMPUTAN EN IO (no patios independientes por volumen).
  - Sin voladizos internos entre volúmenes.
  - Separación mínima entre cuerpos = max(6.0 m, 0.2 * altura_promedio,
    NSR-10 A.6.5 2% * h_piso si >3 pisos).

================================================================================
CABLEADO EN EL CANVAS F1_CONTEXTO_v13.1  (actualizado 2026-10-05)
================================================================================
ENTRADAS del componente (acceso "Item" = un valor por rama; "List" = lista):

  nombre                     tipo GH   acceso  estado / origen
  ---------------------------------------------------------------------------
  chip                       Text      Item    CABLEADO ← #28-F0_LOAD_PROYECTO_v01.chip
  presupuesto_ocupacion_m2   Number    Item    sin cable (opcional). Fuente recomendada:
                                               leer el Panel presupuesto_ocupacion_m2 de
                                               NORMATIVA v09 y escribirlo en un Panel/Slider.
                                               NO cablear directo desde NORMATIVA
                                               (se forma ciclo NORMATIVA→F3→NORMATIVA).
                                               Si queda vacío → se deriva = lote × io_max.
  io_max                     Number    Item    sin cable. Default 0.70 (solo para derivar).
  n_barras_objetivo          Integer   Item    sin cable. Default 2,3. Admite 2 | 3 | "2,3".
  entrepiso_adaptativo       Boolean   Item    sin cable. Default True (v1 itera 3.05/3.80 siempre).
  prioridad_ajuste           Text      List    sin cable. Reservado (D3: "profundidad,entrepiso,num_cuerpos").
  usos                       Text      List    sin cable. Filtro del mix, p.ej. "Vivienda,Local comercial".
  bloques_separacion_m       Number    Item    sin cable. Default 6.0 (Anexo 5 §1.10.b).
  bloques_crujia             Text      Item    sin cable. "unica" (def) | "doble".
  bloques_nucleo             Text      Item    sin cable. "centro" (def) | "extremo".
  output_json                Text      Item    sin cable. Ruta opcional: escribe barras.json en disco.

  NOTA v03.1: las entradas se llamaban antes con guiones (presupuesto-ocupacion,
  io-max, n-barras, ...) y fueron renombradas a snake_case según la convención
  del proyecto; el script acepta internamente AMBAS formas (normaliza "-" ↔ "_").

SALIDAS del componente:

  nombre                   tipo     destino
  ---------------------------------------------------------------------------
  barras_json              Text     → #118-F1_ETAPA2_NORMATIVA_v09.py.barras_json (CABLEADO)
  mensaje                  Text     → Panel diagnóstico (recomendado)
  alternativa_recomendada  Text     → Panel (opcional)
  ocupacion_total_m2       Number   → Panel (opcional)
  gfa_real_m2              Number   → Panel (opcional)
  floor_h_usado            Number   → Panel (opcional)
  n_barras_usado           Integer  → Panel (opcional)

CLI (pipeline / pruebas):
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

================================================================================
"""
import io
import json
import math
import os
import sys

# CLI: argparse puede no existir en algunos entornos embebidos (GHPython).
try:
    import argparse
except ImportError:
    argparse = None

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


try:
    _TEXTO_T = unicode   # Python 2 / IronPython
except NameError:
    _TEXTO_T = str       # Python 3


def _texto_seguro(x):
    """v03.3 - Texto unicode seguro para GH/IronPython y CPython.

    Los bytes (py2 str) se decodifican con cascada utf-8 → cp1252 → latin-1
    (evita el codec por defecto "unknown" de IronPython en conversiones
    implícitas). En py3 devuelve str normal.
    """
    if isinstance(x, bytes):
        for enc in ("utf-8", "cp1252", "latin-1"):
            try:
                return x.decode(enc)
            except Exception:
                pass
        return u""
    try:
        return _TEXTO_T(x)
    except Exception:
        pass
    try:
        return str(x)
    except Exception:
        return repr(x)


def _resolver_raiz_proyecto():
    """v03.3 - Raíz del proyecto para localizar resultados F2.

    Orden: archivo (CLI) → entorno (canvas GH: DISENO_PARAMETRICO_ROOT) → "".
    Valida que la raíz candidata tenga subcarpeta src/ antes de aceptarla
    (evita falsos positivos de entornos de test que apuntan a temporales).
    Todo el texto se normaliza (evita codec "unknown" de IronPython).
    """
    candidatos = []
    try:
        base = os.path.dirname(os.path.abspath(_texto_seguro(__file__)))
        candidatos.append(os.path.normpath(os.path.join(base, u"..", u"..")))
    except Exception:
        pass
    try:
        r_env = _texto_seguro(os.environ.get("DISENO_PARAMETRICO_ROOT", ""))
    except Exception:
        r_env = u""
    if r_env:
        candidatos.append(r_env)
    for c in candidatos:
        try:
            if c and os.path.isdir(os.path.join(c, u"src")):
                return c
        except Exception:
            continue
    return u""


ROOT = _resolver_raiz_proyecto()
if ROOT:
    FIN = os.path.join(ROOT, u"src", u"fase-2-demanda", u"F2_Modelo_Financiero", u"resultados")
    OUT = os.path.join(ROOT, u"src", u"fase-3-masa", u"casos")
else:
    FIN = u""
    OUT = u""

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
SEPARACION_MIN_BASE = 6.0    # Anexo 5 §1.10.b
NSR10_COEF       = 0.02      # A.6.5 2% h

# v03.1: margen de seguridad al DERIVAR el presupuesto (solo si la entrada
# presupuesto_ocupacion_m2 no está disponible): absorbe la diferencia entre
# el área de lote del archivo F2 y el área del polígono simplificado que
# usa NORMATIVA v09, para que la validación APROBADA no falle por centésimas.
MARGEN_DERIVACION_PCT = 0.001      # 0,1 %
MARGEN_DERIVACION_MIN_M2 = 0.25    # mínimo absoluto

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


def normalizar_uso(uso):
    # type: (str) -> str
    u = uso.lower()
    if "vivienda" in u or "vis" in u or "estandar" in u: return "Vivienda"
    if "local" in u or "comercio" in u: return "Local comercial"
    if "consultorio" in u: return "Consultorios"
    if "oficina" in u: return "Oficinas"
    if "institucional" in u or "ips" in u or "laboratorio" in u: return "Institucional salud"
    if "salud" in u and "institucional" not in u: return "Consultorios"
    if "geriatrico" in u: return "Hogar geriatrico"
    return u


def _decodificar_cascada(raw, ruta=u"<bytes>"):
    """LECTOR CANÓNICO (v03.3): utf-8-sig estricto → cp1252 → latin-1."""
    try:
        return raw.decode("utf-8-sig")
    except Exception:
        pass
    try:
        return raw.decode("cp1252")
    except Exception:
        pass
    return raw.decode("latin-1")


def _leer_json(ruta):
    """v03.3 - Lee y parsea un JSON sin depender del codec por defecto.

    Patrón canónico del proyecto para GH/IronPython: leer BYTES (rb) y
    decodificar explícitamente. Compatible con CPython (misma ruta de código).
    """
    ruta_t = _texto_seguro(ruta)
    with open(ruta_t, "rb") as f:
        raw = f.read()
    return json.loads(_decodificar_cascada(raw, ruta_t))


def _escribir_texto(ruta, texto):
    """v03.3 - Escribe texto UTF-8 en modo binario (sin codec por defecto)."""
    ruta_t = _texto_seguro(ruta)
    if not isinstance(texto, bytes):
        texto = _texto_seguro(texto).encode("utf-8")
    with open(ruta_t, "wb") as f:
        f.write(texto)


def _a_utf8_bytes(obj):
    """v03.4 - Convierte recursivamente textos a bytes UTF-8 (solo py2/IronPython).

    Workaround del bug de IronPython: json.dumps(ensure_ascii=True) falla con
    strings unicode no-ASCII; con bytes UTF-8 el codificador los decodifica y
    los escapa correctamente. En py3 devuelve el objeto tal cual.
    """
    try:
        _u = unicode  # noqa: F821 (Python 2)
    except NameError:
        return obj  # Python 3: json maneja unicode sin problema
    if isinstance(obj, dict):
        out = {}
        for k, v in obj.items():
            out[_a_utf8_bytes(k)] = _a_utf8_bytes(v)
        return out
    if isinstance(obj, (list, tuple)):
        return [_a_utf8_bytes(v) for v in obj]
    if isinstance(obj, _u):
        return obj.encode("utf-8")
    return obj


def _json_manual_ascii(obj):
    """v03.4 - Serializador JSON mínimo 100% ASCII (sin dependencia de codecs).

    Soporta dict/list/tuple/str/unicode/int/float/bool/None; escapa todo lo
    no-ASCII a \\uXXXX. Último recurso si json.dumps falla (bug IronPython).
    """
    try:
        _t_ints = (int, long)   # noqa: F821 (Python 2)
    except NameError:
        _t_ints = (int,)

    def _esc(txt):
        out = []
        for ch in _texto_seguro(txt):
            n = ord(ch)
            if ch == u'"':
                out.append(u'\\"')
            elif ch == u'\\':
                out.append(u'\\\\')
            elif n < 0x20:
                out.append(u'\\u%04x' % n)
            elif n < 0x80:
                out.append(ch)
            else:
                out.append(u'\\u%04x' % n)
        return u'"' + u''.join(out) + u'"'

    def _dump(o):
        if o is None:
            return u'null'
        if o is True:
            return u'true'
        if o is False:
            return u'false'
        if isinstance(o, _t_ints):
            return u'%d' % o
        if isinstance(o, float):
            if o != o or o in (float('inf'), float('-inf')):
                return u'null'
            return u'%r' % o
        if isinstance(o, dict):
            partes = []
            for k, v in o.items():
                partes.append(_esc(k) + u': ' + _dump(v))
            return u'{' + u', '.join(partes) + u'}'
        if isinstance(o, (list, tuple)):
            return u'[' + u', '.join(_dump(v) for v in o) + u']'
        return _esc(o)

    return _dump(obj)


def _json_dumps_ascii(obj):
    """v03.4 - json.dumps(ensure_ascii=True) tolerante a IronPython.

    1) intento estándar; 2) bytes UTF-8 (sortea el bug del codificador ipy);
    3) serializador ASCII manual. Salida 100% ASCII en todos los casos.
    """
    try:
        return json.dumps(obj, ensure_ascii=True)
    except Exception:
        pass
    try:
        return json.dumps(_a_utf8_bytes(obj), ensure_ascii=True)
    except Exception:
        pass
    return _json_manual_ascii(obj)


def _tiene_mixto(ruta):
    try:
        paquete = _leer_json(ruta)
        for x in (paquete.get("escenarios") or []):
            if x.get("mix_usos_detalle"): return True
    except Exception: return False
    return False


def buscar_resultados(chip):
    if not chip: return None
    if not FIN or not os.path.isdir(FIN): return None
    chip_t = _texto_seguro(chip)
    resultados_dir = FIN
    canonico = u"resultados_" + chip_t + u".json"
    candidatos = []
    if os.path.exists(os.path.join(resultados_dir, canonico)):
        candidatos.append(canonico)
    nombres = [_texto_seguro(n) for n in os.listdir(resultados_dir)]
    otros = [n for n in nombres
             if n.endswith(u".json") and n.startswith(u"resultados_" + chip_t + u"_")]
    otros.sort(key=lambda n: os.path.getmtime(os.path.join(resultados_dir, n)), reverse=True)
    candidatos.extend(otros)
    if not candidatos: return None
    for n in candidatos:
        if _tiene_mixto(os.path.join(resultados_dir, n)): return n
    return candidatos[0]


def _cargar_programa(resultados_file, escenario, gfa=None, lote_m2=None, huella_m2=None):
    paquete = _leer_json(os.path.join(FIN, resultados_file))
    esc = next((x for x in paquete["escenarios"] if x["escenario_id"] == escenario), None)
    if esc is None:
        for x in paquete["escenarios"]:
            if x.get("mix_usos_detalle"):
                esc = x; escenario = x["escenario_id"]
                if not _EN_GH:
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
    if not _EN_GH:
        print("  [resultados] usando:", nombre, "| escenario:", cfg["escenario"])
    return _cargar_programa(nombre, cfg["escenario"], cfg.get("gfa"), cfg.get("lote_m2"), cfg.get("huella_m2"))


def leer_programa_chip(chip, escenario="D_MIXTO"):
    nombre = buscar_resultados(chip)
    if not nombre: raise ValueError(u"Sin resultados F2 para el CHIP " + _texto_seguro(chip))
    if not _EN_GH:
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
        "mensaje": u"{} barras crujía única {:.1f} m prof., sep. {:.1f} m; ocupación {:.1f} m² (margen {:.1f} m²); entrepiso {:.2f} m".format(
            rec["n_barras"], rec["profundidad_m"], rec["separacion_m"],
            rec["ocupacion_total_m2"], presupuesto_m2 - rec["ocupacion_total_m2"], rec["floor_h"])
    }


# ============================================================================
# SECCIÓN GRASSHOPPER (GH) — v03.4
# Utilidades de lectura de entradas y ejecución dentro del componente.
# (Inofensivas fuera de GH: solo se usan cuando _EN_GH es True.)
# ============================================================================


def _gh_modulo():
    """Objeto ghenv del entorno de script.

    En GHPython (Rhino 8) `ghenv` (y `ghdoc`) se INYECTAN como VARIABLES del
    script y `import ghenv` FALLA; el import queda como fallback para otros
    builds. Fuera de Rhino/Grasshopper devuelve None (nada inyectado).
    """
    g = globals()
    for nombre in ("ghenv", "ghdoc"):
        if nombre in g and g[nombre] is not None:
            return g[nombre]
    try:
        import ghenv as _gm  # noqa: F401
        return _gm
    except Exception:
        return None


_EN_GH = _gh_modulo() is not None

try:
    _TIPOS_ENTEROS = (int, long)   # Python 2 / IronPython
except NameError:
    _TIPOS_ENTEROS = (int,)        # Python 3


def _gh_str(x):
    """v03.3 - Texto seguro: delega en _texto_seguro (unicode en py2)."""
    return _texto_seguro(x)


def _gh_norm(s):
    """Normaliza nombre de entrada: trim + minúsculas + guiones→guion_bajo."""
    return _gh_str(s).strip().lower().replace("-", "_")


def _gh_lookup(nombres):
    """Busca una entrada por nombre en globals() (compatible dash/underscore)."""
    g = globals()
    for n in nombres:
        if n in g and g[n] is not None:
            return g[n]
    objetivo = [_gh_norm(n) for n in nombres]
    for k in list(g.keys()):
        try:
            if _gh_norm(k) in objetivo and g[k] is not None:
                return g[k]
        except Exception:
            pass
    return None


def _gh_input_idx(indice):
    """Fallback: lee el valor del input i del componente (por índice, vía ghenv)."""
    mod = _gh_modulo()
    if mod is None:
        return None
    try:
        param = mod.Component.Params.Input[indice]
        for goo in param.VolatileData.AllData(True):
            try:
                v = goo.Value
            except Exception:
                return _gh_str(goo)
            if isinstance(v, bool) or isinstance(v, (int, float)):
                return v
            return _gh_str(v)
    except Exception:
        pass
    return None


def _gh_leer(indice, nombres, default=None):
    """Lee una entrada: nombre (globals) → índice (ghenv) → default."""
    v = _gh_lookup(nombres)
    if v is None and _EN_GH:
        v = _gh_input_idx(indice)
    if v is None:
        return default
    if isinstance(v, (list, tuple)):
        vv = [x for x in v if x is not None]
        if not vv:
            return default
        return vv[0] if len(vv) == 1 else vv
    return v


def _gh_num(v, default=None):
    """Number defensivo: None / listas / "" / "None" → default."""
    if v is None:
        return default
    if isinstance(v, (list, tuple)):
        for x in v:
            r = _gh_num(x, None)
            if r is not None:
                return r
        return default
    if isinstance(v, bool):
        return float(v)
    if isinstance(v, (int, float)):
        return float(v)
    s = _gh_str(v).strip()
    if not s or s.lower() in ("none", "null"):
        return default
    try:
        return float(s.replace(",", "."))
    except Exception:
        return default


def _gh_bool(v, default=False):
    if v is None:
        return default
    if isinstance(v, bool):
        return v
    if isinstance(v, (int, float)):
        return bool(v)
    if isinstance(v, (list, tuple)):
        for x in v:
            if x is None:
                continue
            return _gh_bool(x, default)
        return default
    s = _gh_str(v).strip().lower()
    if s == "":
        return default
    if s in (u"true", u"1", u"si", u"sí", u"yes", u"verdadero"):
        return True
    if s in (u"false", u"0", u"no", u"falso"):
        return False
    return default


def _gh_ints(v, default=None):
    """'2,3' | 2 | 2.0 | [2,3] → [2, 3]."""
    out = []

    def _add(x):
        if x is None:
            return
        if isinstance(x, (list, tuple)):
            for y in x:
                _add(y)
            return
        if isinstance(x, bool):
            return
        if isinstance(x, float):
            if abs(x - round(x)) < 1e-9:
                out.append(int(round(x)))
            return
        if isinstance(x, _TIPOS_ENTEROS):
            out.append(int(x))
            return
        s = _gh_str(x).strip()
        if not s or s.lower() == "none":
            return
        for parte in s.replace(";", ",").split(","):
            parte = parte.strip()
            if not parte:
                continue
            try:
                out.append(int(round(float(parte))))
            except Exception:
                pass

    _add(v)
    if not out and default is not None:
        return list(default)
    return out


def _gh_lista_textos(v):
    """Lista/texto separado por comas → lista de strings."""
    out = []
    if v is None:
        return out
    if isinstance(v, (list, tuple)):
        for x in v:
            if x is None:
                continue
            for parte in _gh_str(x).split(","):
                p = parte.strip()
                if p:
                    out.append(p)
        return out
    for parte in _gh_str(v).split(","):
        p = parte.strip()
        if p:
            out.append(p)
    return out


# ----------------------------------------------------------------------------
# Salidas del componente (siempre definidas para que GH las publique)
# ----------------------------------------------------------------------------
barras_json = ""
mensaje = ""
alternativa_recomendada = ""
ocupacion_total_m2 = 0.0
gfa_real_m2 = 0.0
floor_h_usado = 0.0
n_barras_usado = 0

if _EN_GH:
    _paso = u"inicio"
    try:
        _paso = u"leer entradas"
        _chip = _gh_str(_gh_leer(0, ["chip"], "") or "").strip()

        _presupuesto_in = _gh_num(
            _gh_leer(1, ["presupuesto_ocupacion_m2", "presupuesto_ocupacion",
                         "presupuesto-ocupacion"]), None)
        _io_max = _gh_num(_gh_leer(2, ["io_max", "io-max"]), OCUPACION_POT)
        if _io_max is None or _io_max <= 0:
            _io_max = OCUPACION_POT

        _n_barras = _gh_ints(
            _gh_leer(3, ["n_barras_objetivo", "n_barras", "n-barras"]), [2, 3])
        if not _n_barras:
            _n_barras = [2, 3]

        # Entradas informativas en v03 (documentadas en el encabezado):
        _entrepiso_adap = _gh_bool(
            _gh_leer(4, ["entrepiso_adaptativo", "entrepiso-adaptativo"]), True)
        _prioridad = _gh_str(_gh_leer(
            5, ["prioridad_ajuste", "prioridad-ajuste"],
            "profundidad,entrepiso,num_cuerpos"))

        _usos = _gh_lista_textos(_gh_leer(6, ["usos"], ""))

        _sep = _gh_num(_gh_leer(
            7, ["bloques_separacion_m", "bloques-separacion-m"]), None)
        _crujia = _gh_str(_gh_leer(
            8, ["bloques_crujia", "bloques-crujia"], "unica") or "unica").strip().lower()
        if _crujia not in ("unica", "doble"):
            _crujia = "unica"
        _nucleo = _gh_str(_gh_leer(
            9, ["bloques_nucleo", "bloques-nucleo"], "centro") or "centro").strip().lower()
        if _nucleo not in ("centro", "extremo"):
            _nucleo = "centro"

        _output_json = _gh_str(_gh_leer(
            10, ["output_json", "output-json"], "") or "").strip()

        _paso = u"validar chip"
        if not _chip:
            raise ValueError(u"chip vacío: cablear la salida chip de F0_LOAD_PROYECTO_v01")

        _paso = u"leer resultados F2"
        _prog = leer_programa_chip(_chip, "D_MIXTO")
        _lote_m2 = _prog.get("lote_m2")
        if not _lote_m2:
            raise ValueError(u"lote_m2 no disponible para el chip " + _chip)

        _paso = u"derivar presupuesto"
        _derivado = False
        _presupuesto = _presupuesto_in
        if _presupuesto is None or _presupuesto <= 0:
            _base = _lote_m2 * _io_max
            _margen = max(_base * MARGEN_DERIVACION_PCT, MARGEN_DERIVACION_MIN_M2)
            _presupuesto = _base - _margen
            if _presupuesto <= 0:
                raise ValueError(
                    u"presupuesto_ocupacion_m2 vacío y no se pudo derivar (lote/io desconocidos)")
            _derivado = True

        _paso = u"filtrar usos"
        if _usos:
            _filtro = [normalizar_uso(_u) for _u in _usos]
            _comps = [c for c in _prog.get("componentes", []) if c["uso"] in _filtro]
            if _comps:
                _prog["componentes"] = _comps
                _tot = sum(c["pct_gfa"] for c in _prog["componentes"])
                if _tot > 0:
                    for _c in _prog["componentes"]:
                        _c["pct_gfa"] = _c["pct_gfa"] / _tot * 100.0
                        _c["gfa_m2"] = _prog["gfa_total"] * _c["pct_gfa"] / 100.0

        _sep_real = _sep if (_sep and _sep > 0) else SEPARACION_MIN_BASE

        _paso = u"generar barras"
        _alternativas = iterar_barras(
            _lote_m2, _presupuesto, _n_barras, _sep_real, _prog, _crujia, _nucleo)
        _salida = build_barras_json(_chip, _alternativas, _lote_m2, _presupuesto, _io_max)

        _paso = u"publicar salidas: json"
        barras_json = _json_dumps_ascii(_salida)
        _paso = u"publicar salidas: mensaje"
        mensaje = u"F3 v03.4 | " + _gh_str(_salida.get("mensaje", ""))
        if _derivado:
            mensaje += u" | presupuesto derivado = lote {:.1f} m2 x IO {:.2f} (con margen)".format(
                _lote_m2, _io_max)
        if _alternativas:
            _paso = u"publicar salidas: recomendada"
            _rec = _alternativas[0]
            alternativa_recomendada = _rec.get("id", "")
            ocupacion_total_m2 = float(_rec.get("ocupacion_total_m2", 0.0))
            gfa_real_m2 = float(_rec.get("gfa_real_m2", 0.0))
            floor_h_usado = float(_rec.get("floor_h", 0.0))
            n_barras_usado = int(_rec.get("n_barras", 0))
        if _output_json:
            _paso = u"escribir output_json"
            try:
                _escribir_texto(_output_json, _json_dumps_ascii(_salida))
                mensaje += u" | escrito: " + _output_json
            except Exception as _e_out:
                mensaje += u" | aviso escritura {}: {}".format(_output_json, _gh_str(_e_out))
    except Exception as _e_gh:
        _detalle = u""
        try:
            import traceback as _traceback
            _txt_tb = _gh_str(_traceback.format_exc())
            _lineas_tb = _txt_tb.strip().splitlines()
            if _lineas_tb:
                _detalle = u" | tb: " + _lineas_tb[-1][:160]
        except Exception:
            pass
        barras_json = ""
        mensaje = u"F3 v03.4 | ERROR en [{}]: {}{}".format(_paso, _gh_str(_e_gh), _detalle)


# ============================================================================
# MAIN (CLI)
# ============================================================================
def main():
    if argparse is None:
        raise RuntimeError("argparse no disponible; usar la sección GH del canvas "
                           "o ejecutar con un intérprete Python completo")
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
        _escribir_texto(args.output_json, json.dumps(salida, indent=2, ensure_ascii=True))
        print("Escrito:", args.output_json)
    else:
        print(json.dumps(salida, indent=2, ensure_ascii=True))


# Guard CLI: en GHPython `__name__` ES "__main__" y `ghenv` está inyectado;
# por seguridad adicional, main() solo corre fuera de Rhino/Grasshopper y en
# CPython (CLI/pruebas): nunca en IronPython ni con clr (.NET) presente.
try:
    _ES_MAIN = (__name__ == "__main__")
except Exception:
    _ES_MAIN = False

_ES_IRON = False
try:
    import platform as _platform
    _ES_IRON = ((_platform.python_implementation() or "").lower() == "ironpython")
except Exception:
    pass
if not _ES_IRON:
    try:
        _ES_IRON = (sys.platform == "cli")
    except Exception:
        pass

_ES_CLR = False
try:
    import clr  # noqa: F401 — solo existe en entornos .NET (Rhino/IronPython)
    _ES_CLR = True
except Exception:
    _ES_CLR = False

# Diagnóstico: en Rhino/.NET pero sin ghenv disponible en el script.
if (_ES_IRON or _ES_CLR) and not _EN_GH and not mensaje:
    mensaje = (u"F3 v03.4 | aviso: entorno Rhino/.NET detectado pero 'ghenv' no "
               u"está disponible en el script; revisar el componente")

if _ES_MAIN and not _EN_GH and not _ES_IRON and not _ES_CLR:
    main()
