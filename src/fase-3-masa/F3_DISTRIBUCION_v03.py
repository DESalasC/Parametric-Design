# -*- coding: utf-8 -*-
"""
================================================================================
F3_DISTRIBUCION_v03.py — v03.9 (genérica v03) — Distribuidor de barras por crujía con presupuesto IO
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

HISTORIAL DE VERSIONES (se conservan las últimas tres; anteriores en el Vault):
  v03.9 (2026-10-13): FIX de marcos en el ESCALONAMIENTO LATERAL: el recorte por
    piso usaba el poligono del lote (marco LOCAL) con el rango Y de la huella en
    marco CANVAS (mezcla de marcos) => los pisos 2..n quedaban desplazados (solo
    el piso base en su sitio). Ahora recorta el poligono de la FRANJA en marco
    local (cs[_k]) con su banda Y local; respaldo con aviso si queda degenerado.
    Mensajes v03.9.
  v03.8 (2026-10-11, noche 2): ESCALONAMIENTO LATERAL vs vecino (norma 1/5):
    `sep_lateral_json` = {"lado":"xmax"|"xmin", "h_vecino_m":6.0,
    "min_retiro_m":0.0, "nsr_coef":0.02}. Retiro por piso: r=0 si z_piso
    <= h_vecino; si no r = max(0.2*(z-h_vecino), min_retiro_m, nsr_coef*z).
    Se agrega `huella_xy_por_piso` por bloque (huella_xy queda = piso base).
    Mensajes v03.8.
  v03.7 (2026-10-11, noche): Ajustes del operador —
    (a) ANCLAJE A FRENTES: las franjas se anclan al frente y al fondo del area
        util; el remanente se reparte uniformemente en las separaciones entre
        bloques (sin fondo libre; sin antejardines en frentes publicos);
    (b) PISOS POR BLOQUE: `pisos_por_bloque` ("4,4,6") o `limites_pisos_json`
        (bandas desde el frente con `max_pisos` + redistribucion del sobrante
        al ultimo bloque). GFA = suma(area x pisos); aviso de retiros.
  v03.6 y anteriores (v03.0-v03.6.1): historial completo en el Vault Obsidian y
    _legacy. Contrato vigente: huella_xy CERRADA (v03.6.1, "Implantacion" F3_VOLUM).

REGLAS DE PATIOS/SEPARACIONES (aprobadas operador 2026-10-03; confirmadas 2026-10-13):
  - 1 VOLUMEN: patio normativo Anexo 5 §1.12.b (H/3, min 9 m², 3 ml lado).
  - >=2 VOLÚMENES: NO se generan patios independientes; las separaciones entre
    volúmenes rigen y COMPUTAN EN IO.
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
  layout_espacial_json     Text      Consumidores F3 (UNIDADES/ACCESOS) - casos/<chip>/layout_espacial.json

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

# v03.6: cap de profundidad de plataforma (crujía única) y límites de ajuste
CRUJIA_MAX_M_DEF = 10.0      # cap por defecto (skills: crujía única 6-9 m + circulación)
CRUJIA_MAX_M_TOPE = 12.0     # tope duro configurable
CRUJIA_MIN_M = 6.0           # profundidad mínima utilizable
N_BARRAS_MAX = 5             # máximo de franjas al auto-subir n

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
    # Crear directorio si no existe
    dir_path = os.path.dirname(ruta_t)
    if dir_path and not os.path.exists(dir_path):
        os.makedirs(dir_path)
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


def _leer_layout_casos(chip):
    """v03.5 - Lee casos/<chip>/layout_espacial.json (o el mas reciente)."""
    if not OUT or not os.path.isdir(OUT):
        return u"", u""
    chip_t = _texto_seguro(chip) if chip else u""
    if chip_t:
        ruta = os.path.join(OUT, chip_t, u"layout_espacial.json")
        if os.path.isfile(ruta):
            try:
                with open(ruta, "rb") as f:
                    return _decodificar_cascada(f.read(), ruta), ruta
            except Exception:
                pass
    candidatos = []
    try:
        for nombre in os.listdir(OUT):
            ruta = os.path.join(OUT, nombre, u"layout_espacial.json")
            if os.path.isfile(ruta):
                candidatos.append(ruta)
    except Exception:
        pass
    mejor = None
    for ruta in candidatos:
        try:
            m = os.path.getmtime(ruta)
        except Exception:
            m = 0
        if mejor is None or m > mejor[0]:
            mejor = (m, ruta)
    if mejor is None:
        return u"", u""
    try:
        with open(mejor[1], "rb") as f:
            return _decodificar_cascada(f.read(), mejor[1]), mejor[1]
    except Exception:
        return u"", u""


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
def _clip_rect(pol, x0, y0, x1, y1):
    """v03.6: recorte de poligono (lista de (x,y)) contra rectangulo CONVEXO
    con Sutherland-Hodgman en Python puro (sin Rhino). Devuelve lista de
    puntos o [] si no hay interseccion."""
    def _recorte(poly, dentro, inter):
        out = []
        m = len(poly)
        if m == 0:
            return out
        for i in range(m):
            a = poly[i]
            b = poly[(i + 1) % m]
            da = dentro(a)
            db = dentro(b)
            if da and db:
                out.append(b)
            elif da and not db:
                out.append(inter(a, b))
            elif (not da) and db:
                out.append(inter(a, b))
                out.append(b)
        return out

    def _ix(a, b, xc):
        t = (xc - a[0]) / (b[0] - a[0]) if abs(b[0] - a[0]) > 1e-12 else 0.0
        return (xc, a[1] + t * (b[1] - a[1]))

    def _iy(a, b, yc):
        t = (yc - a[1]) / (b[1] - a[1]) if abs(b[1] - a[1]) > 1e-12 else 0.0
        return (a[0] + t * (b[0] - a[0]), yc)

    poly = [(float(p[0]), float(p[1])) for p in pol]
    poly = _recorte(poly, lambda p: p[0] >= x0, lambda a, b: _ix(a, b, x0))
    poly = _recorte(poly, lambda p: p[0] <= x1, lambda a, b: _ix(a, b, x1))
    poly = _recorte(poly, lambda p: p[1] >= y0, lambda a, b: _iy(a, b, y0))
    poly = _recorte(poly, lambda p: p[1] <= y1, lambda a, b: _iy(a, b, y1))
    limpio = []
    for p in poly:
        if not limpio or abs(p[0] - limpio[-1][0]) > 1e-9 or abs(p[1] - limpio[-1][1]) > 1e-9:
            limpio.append(p)
    if len(limpio) >= 2 and abs(limpio[0][0] - limpio[-1][0]) < 1e-9 and abs(limpio[0][1] - limpio[-1][1]) < 1e-9:
        limpio.pop()
    if len(limpio) < 3:
        return []
    return limpio


def _area_pts(pts):
    s = 0.0
    n = len(pts)
    for i in range(n):
        p = pts[i]
        q = pts[(i + 1) % n]
        s += p[0] * q[1] - q[0] * p[1]
    return abs(s) / 2.0


def _x_extent_en_y(pol, yq):
    """Extension en X del poligono a la altura yq (validacion de alcance)."""
    xs = []
    n = len(pol)
    for i in range(n):
        a = pol[i]
        b = pol[(i + 1) % n]
        if abs(a[1] - yq) <= 1e-9:
            xs.append(a[0])
        if (a[1] - yq) * (b[1] - yq) < 0.0:
            t = (yq - a[1]) / (b[1] - a[1])
            xs.append(a[0] + t * (b[0] - a[0]))
    if not xs:
        return None
    return (min(xs), max(xs))


def generar_barras_para_n(lote_m2, presupuesto_m2, n_barras, floor_h, separacion_min,
                          programa, crujia_tipo="unica", nucleo_pos="centro"):
    """v03.6: franjas de crujia unica a ANCHO COMPLETO (sin reduccion centrada),
    con cap de profundidad `crujia_max_m` (def. 10 m) y n auto-ajustado.
    Recorte en Python puro; cota de arranque tolerante (topografia opcional)."""
    base_raw = globals().get("base_normativa_json")
    if not base_raw:
        raise ValueError(u"Conectar base_normativa_json (F1_ETAPA2_NORMATIVA_v10.base_json): "
                         u"no se permiten dimensiones ni pisos fijos")
    base = json.loads(_gh_str(base_raw))

    pisos = int(base["pisos_limite"])
    floor_h = float(base["floor_h"])
    sep = max(float(separacion_min), SEPARACION_MIN_BASE, 0.2 * pisos * floor_h)

    crujia_max = _gh_num(globals().get("crujia_max_m"), None)
    if not crujia_max or crujia_max <= 0:
        crujia_max = CRUJIA_MAX_M_DEF
    crujia_max = min(max(float(crujia_max), CRUJIA_MIN_M), CRUJIA_MAX_M_TOPE)

    avisos = []
    n_pedido = max(1, int(round(n_barras)))

    pol = base["poligono_local"]
    xmin0 = min(p[0] for p in pol); xmax0 = max(p[0] for p in pol)
    ymin0 = min(p[1] for p in pol); ymax0 = max(p[1] for p in pol)
    ymin = ymin0 + float(base["retiro_frontal_m"])
    ymax = ymax0 - float(base["retiro_posterior_m"])
    xmin = xmin0 + float(base["retiro_lateral_m"])
    xmax = xmax0 - float(base["retiro_lateral_m"])
    if xmax <= xmin or ymax <= ymin:
        return None
    W = xmax - xmin
    Y = ymax - ymin
    limite = min(float(presupuesto_m2), float(base["presupuesto_ocupacion_m2"]))
    if float(base["retiro_frontal_m"]) > 1e-9 or float(base["retiro_posterior_m"]) > 1e-9:
        avisos.append(u"retiros frente/fondo > 0 en base: revisar 'sin antejardin' en frentes publicos")

    # --- n: subir hasta que la profundidad de llenado <= crujia_max ---
    def _d_fill(k):
        return (Y - (k - 1) * sep) / k

    n = n_pedido
    while n < N_BARRAS_MAX and _d_fill(n) > crujia_max + 1e-9:
        n += 1
    if n != n_pedido:
        avisos.append(u"n {} -> {} (profundidad>cap {:.1f} m)".format(n_pedido, n, crujia_max))
    d_hi = min(crujia_max, _d_fill(n))
    if d_hi < CRUJIA_MIN_M:
        avisos.append(u"no cabe con ancho completo (Y {:.1f} m, n {} <= {})".format(Y, n, N_BARRAS_MAX))
        return None

    def _construir(d):
        # v03.7: anclaje a frente y fondo; separacion uniforme g = (Y - n*d)/(n-1)
        g = (Y - n * d) / (n - 1.0) if n > 1 else 0.0
        if n > 1 and g < sep - 1e-9:
            return None
        cs = []
        for b in range(n):
            y0 = ymin + b * (d + g)
            y1 = y0 + d
            if y1 > ymax + 1e-9:
                return None
            pts = _clip_rect(pol, xmin, y0, xmax, y1)
            if pts:
                cs.append((b + 1, y0, y1, pts))
            else:
                avisos.append(u"franja {} vacia (fuera del lote)".format(b + 1))
        if not cs:
            return None
        if n == 1:
            avisos.append(u"n=1: sin separaciones; revisar fondo util")
        return cs

    d_target = limite / (W * n)
    d_used = min(d_hi, max(d_target, 0.0))
    if d_used < CRUJIA_MIN_M:
        d_used = CRUJIA_MIN_M
    cs = _construir(d_used)
    if cs is None:
        return None
    occ = 0.0
    for _b, _y0, _y1, _p in cs:
        occ += _area_pts(_p)
    if occ > limite:
        lo = CRUJIA_MIN_M
        hi = d_used
        cs_lo = _construir(lo)
        if cs_lo is None:
            return None
        occ_lo = 0.0
        for _b, _y0, _y1, _p in cs_lo:
            occ_lo += _area_pts(_p)
        if occ_lo > limite:
            avisos.append(u"ancho completo excede presupuesto a profundidad minima (occ {:.1f} > {:.1f})".format(occ_lo, limite))
            return None
        for _it in range(30):
            mid = (lo + hi) / 2.0
            t = _construir(mid)
            if t is not None:
                _acc = 0.0
                for _b, _y0, _y1, _p in t:
                    _acc += _area_pts(_p)
                if _acc <= limite:
                    lo = mid
                    cs = t
                else:
                    hi = mid
            else:
                hi = mid
        d_used = lo
        cs = _construir(d_used)
        occ = 0.0
        for _b, _y0, _y1, _p in cs:
            occ += _area_pts(_p)

    if occ < limite * 0.98:
        avisos.append(u"margen {:.1f} m2 (cap de crujia/frente: no se consume todo el presupuesto)".format(limite - occ))

    g_final = (Y - n * d_used) / (n - 1.0) if n > 1 else 0.0
    if n > 1 and g_final > sep + 0.5:
        avisos.append(u"separaciones entre bloques ajustadas a {:.2f} m (anclaje frente/fondo)".format(g_final))
    anclaje_ok = True
    if cs:
        if abs(cs[0][1] - ymin) > 1e-6:
            anclaje_ok = False
        if abs(cs[-1][2] - ymax) > 1e-6:
            anclaje_ok = False
    if not anclaje_ok:
        avisos.append(u"anclaje a frentes incompleto (revisar)")

    # --- marco -> canvas y cota de arranque (topografia opcional) ---
    marco = base["marco"]
    ox = marco["origen"][0]; oy = marco["origen"][1]
    ux = marco["x"][0]; uy = marco["x"][1]
    vx = marco["y"][0]; vy = marco["y"][1]

    def _mundo(p):
        return (ox + p[0] * ux + p[1] * vx, oy + p[0] * uy + p[1] * vy)

    rg = None
    rs = None
    try:
        import Rhino.Geometry as rg
    except Exception:
        rg = None
    try:
        import rhinoscriptsyntax as rs
    except Exception:
        rs = None
    mesh = globals().get("topo_mesh")
    if hasattr(mesh, "Value"):
        mesh = mesh.Value
    mesh_ok = False
    bbox = None
    if mesh is not None and rg is not None:
        try:
            if rs is not None and not isinstance(mesh, rg.Mesh):
                mesh = rs.coercemesh(mesh)
            bbox = mesh.GetBoundingBox(True)
            mesh_ok = True
        except Exception:
            mesh_ok = False
    if not mesh_ok:
        avisos.append(u"sin topografia utilizable: cota de arranque provisional (z0=0 o cota fija)")

    z_fija = _gh_num(globals().get("cota_arranque_m"), None)

    def _terreno(cx, cy):
        if z_fija is not None:
            return float(z_fija)
        if not mesh_ok:
            return None
        try:
            ray = rg.Ray3d(rg.Point3d(cx, cy, bbox.Max.Z + 100.0), rg.Vector3d(0.0, 0.0, -1.0))
            t = rg.Intersect.Intersection.MeshRay(mesh, ray)
            if t < 0:
                return None
            return ray.PointAt(t).Z
        except Exception:
            return None

    # --- bloques (ancho completo; alcance validado por banda) ---
    bloques = []
    alcance = []
    for (b, y0, y1, pts) in cs:
        pts_m = [_mundo(p) for p in pts]
        xs = [p[0] for p in pts_m]
        ys = [p[1] for p in pts_m]
        cx = sum(xs) / len(xs)
        cy = sum(ys) / len(ys)
        z0 = _terreno(cx, cy)
        if z0 is None:
            z0 = 0.0
            avisos.append(u"B{}-R1: sin cota de terreno (z0=0 provisional)".format(b))
        bx0 = min(xs); bx1 = max(xs)
        ext = _x_extent_en_y(pol, (y0 + y1) / 2.0)
        al_izq = al_der = None
        if ext is not None:
            ref_izq = max(ext[0], xmin0 + float(base["retiro_lateral_m"]))
            ref_der = min(ext[1], xmax0 - float(base["retiro_lateral_m"]))
            al_izq = (bx0 <= ref_izq + 0.02)
            al_der = (bx1 >= ref_der - 0.02)
            if not (al_izq and al_der):
                avisos.append(u"B{}: no alcanza borde {} (revisar lote/bordes)".format(
                    b, "izquierdo" if not al_izq else "derecho"))
        _pts_r = []
        for p in pts_m:
            q = [round(p[0], 4), round(p[1], 4)]
            if not _pts_r or q != _pts_r[-1]:
                _pts_r.append(q)
        if len(_pts_r) >= 3:
            _pts_r.append(list(_pts_r[0]))  # cierre explicito (polilinea del contrato)
        else:
            avisos.append(u"B{}-R1: huella degenerada ({} pts)".format(b, len(_pts_r)))
        alcance.append({"id": "B%d" % b, "izq": al_izq, "der": al_der,
                        "x_min": round(bx0, 3), "x_max": round(bx1, 3)})
        bloques.append({
            "id": "B{}-R1".format(b),
            "huella_xy": _pts_r,
            "cota_arranque_m": round(float(z0), 3),
            "criterio_arranque": u"terreno en centroide (o cota fija); plataforma horizontal preliminar",
            "area_m2": round(_area_pts(pts), 2),
            "pisos": pisos,
            "floor_h": floor_h,
        })

    # v03.7: pisos por bloque (override directo o bandas con redistribucion)
    pisos_bloques = [pisos] * len(bloques)
    _ppb = globals().get("pisos_por_bloque")
    _lim = globals().get("limites_pisos_json")
    if _ppb:
        _vals = _gh_ints(_ppb, None) or []
        if len(_vals) == len(bloques):
            pisos_bloques = [max(1, int(v)) for v in _vals]
        else:
            avisos.append(u"pisos_por_bloque: {} valores != {} bloques (ignorado)".format(len(_vals), len(bloques)))
    elif _lim:
        try:
            _L = json.loads(_gh_str(_lim))
            _bandas = _L.get("bandas", [])
            _caps = []
            for (b, y0, y1, _p) in cs:
                _dist = y0 - ymin
                _cap = None
                for _bd in _bandas:
                    _d0 = float(_bd.get("desde_m", 0.0))
                    _d1 = float(_bd.get("hasta_m", 1e9))
                    if (_d0 - 1e-9) <= _dist <= (_d1 + 1e-9):
                        _mp = int(_bd.get("max_pisos", pisos))
                        _cap = _mp if _cap is None else min(_cap, _mp)
                _caps.append(_cap if _cap is not None else pisos)
            pisos_bloques = [min(pisos, c) for c in _caps]
            _rem = sum(pisos - p for p in pisos_bloques)
            if _rem > 0 and bool(_L.get("redistribuir_ultimo", True)):
                pisos_bloques[-1] += _rem
                avisos.append(u"redistribucion: +{} pisos al ultimo bloque (B{})".format(_rem, len(bloques)))
        except Exception as _e_lim:
            avisos.append(u"limites_pisos_json invalido: {}".format(_gh_str(_e_lim)))
    for _k in range(len(bloques)):
        bloques[_k]["pisos"] = pisos_bloques[_k]

    # v03.9: escalonamiento lateral (1/5 sobre empate) si hay sep_lateral_json (marco local)
    sep_lat = None
    _sl_raw = globals().get("sep_lateral_json")
    if _sl_raw:
        try:
            sep_lat = json.loads(_gh_str(_sl_raw))
        except Exception as _e_sl:
            avisos.append(u"sep_lateral_json invalido: {}".format(_gh_str(_e_sl)))
    if sep_lat:
        _lado = _gh_str(sep_lat.get("lado", "xmax")).strip().lower()
        if _lado not in ("xmin", "xmax"):
            _lado = "xmax"
        _hv = float(sep_lat.get("h_vecino_m", 6.0))
        _rmin = float(sep_lat.get("min_retiro_m", 0.0))
        _nsr = float(sep_lat.get("nsr_coef", 0.02))
        _resumen = []
        for _k in range(len(bloques)):
            _pisos_k = int(pisos_bloques[_k])
            _rows = []
            _ret = []
            # v03.9 FIX: poligono de la FRANJA en marco LOCAL y su banda Y local
            # (v03.8 tomaba el Y de la huella en marco CANVAS: pisos 2+ desplazados)
            _banda = cs[_k]
            _y0b = _banda[1]; _y1b = _banda[2]
            _poly_local = _banda[3]
            for f in range(_pisos_k):
                _zf = (f + 1) * floor_h
                if _zf <= _hv + 1e-9:
                    _r = 0.0
                else:
                    _r = max(0.2 * (_zf - _hv), _rmin, _nsr * _zf)
                _r = round(_r, 3)
                _ret.append(_r)
                if _r <= 1e-9:
                    _rows.append([list(p) for p in bloques[_k]["huella_xy"]])
                else:
                    _x0 = xmin + (_r if _lado == "xmin" else 0.0)
                    _x1 = xmax - (_r if _lado == "xmax" else 0.0)
                    _poly = _clip_rect(_poly_local, _x0, _y0b, _x1, _y1b)
                    _pm = [_mundo(p) for p in _poly]
                    _rr = []
                    for p in _pm:
                        q = [round(p[0], 4), round(p[1], 4)]
                        if not _rr or q != _rr[-1]:
                            _rr.append(q)
                    if len(_rr) >= 3:
                        _rr.append(list(_rr[0]))
                    else:
                        _rr = [list(p) for p in bloques[_k]["huella_xy"]]
                        avisos.append(u"B{}: escalonamiento piso {} sin recorte valido; huella base usada".format(_k + 1, f + 1))
                    _rows.append(_rr)
            bloques[_k]["huella_xy_por_piso"] = _rows
            bloques[_k]["retiros_por_piso_m"] = _ret
            _resumen = _ret
        if _resumen:
            avisos.append(u"escalonamiento lateral ({}): retiros por piso {}".format(
                _lado, u", ".join(u"{:.2f}".format(r) for r in _resumen)))

    # GFA real con pisos por bloque
    gfa_total = 0.0
    for _k in range(len(bloques)):
        gfa_total += float(bloques[_k]["area_m2"]) * float(pisos_bloques[_k])
    altura_max_m = 0.0
    for _k in range(len(bloques)):
        if pisos_bloques[_k] * floor_h > altura_max_m:
            altura_max_m = pisos_bloques[_k] * floor_h

    huellas = []
    for _k in range(len(bloques)):
        _blk = bloques[_k]
        for f in range(int(pisos_bloques[_k])):
            huellas.append([[p[0], p[1], _blk["cota_arranque_m"] + f * floor_h]
                            for p in _blk["huella_xy"]])
    _area_rows = []
    for _k in range(len(bloques)):
        for _f in range(int(pisos_bloques[_k])):
            _area_rows.append([bloques[_k]["area_m2"]])

    return {
        "n_barras": n,
        "n_pedido": n_pedido,
        "profundidad_m": round(d_used, 2),
        "ancho_barra_m": round(W, 2),
        "separacion_m": round(g_final, 2),
        "separacion_min_m": round(sep, 2),
        "ancho_total_m": round(W, 2),
        "ocupacion_total_m2": round(occ, 2),
        "gfa_real_m2": round(gfa_total, 2),
        "altura_total_m": round(altura_max_m, 2),
        "altura_max_m": round(altura_max_m, 2),
        "floor_h": floor_h,
        "pisos": pisos,
        "pisos_por_bloque": list(pisos_bloques),
        "crujia_max_m": round(crujia_max, 2),
        "anclaje_frentes": anclaje_ok,
        "huellas_por_piso": huellas,
        "areas_por_piso": _area_rows,
        "bloques": bloques,
        "marco": marco,
        "alcance_lados": alcance,
        "avisos": avisos,
        "separaciones_validas": True,
        "patio_tipo": "separacion_entre_volumenes",
        "accesos_ok": None,
        "estado": u"v03.9: anclaje a frentes, separaciones ajustadas, pisos por bloque, escalonamiento 1/5 (marco local corregido); pendiente accesos/nucleo/normativa",
    }


def iterar_barras(lote_m2, presupuesto_m2, n_barras_lista, separacion_min, programa,
                  crujia_tipo="unica", nucleo_pos="centro"):
    """v03.6: itera n_barras (el generador auto-ajusta n y floor_h viene de
    base_normativa_json); elimina duplicados de alternativas equivalentes."""
    _floor_h = float(json.loads(_gh_str(globals()["base_normativa_json"]))["floor_h"])
    resultados = []
    vistos = set()
    for n_barras in n_barras_lista:
        res = generar_barras_para_n(lote_m2, presupuesto_m2, n_barras, _floor_h,
                                     separacion_min, programa, crujia_tipo, nucleo_pos)
        if res:
            key = (res["n_barras"], round(res["floor_h"], 2), round(res["ocupacion_total_m2"], 2))
            if key in vistos:
                continue
            vistos.add(key)
            res["id"] = "ALT-{}{}-{:.0f}".format(res["n_barras"],
                                                 "B" if crujia_tipo == "unica" else "D",
                                                 res["floor_h"] * 100)
            resultados.append(res)
    # Ordenar: mayor GFA primero; a igual, menor n
    resultados.sort(key=lambda r: (-r["gfa_real_m2"], r["n_barras"]))
    return resultados


def build_barras_json(chip, alternativas, lote_m2, presupuesto_m2, io_max):
    if not alternativas:
        return {
            "schema": "f3_barras_salida_v01",
            "chip": chip,
            "alternativas": [],
            "recomendada": None,
            "mensaje": "NINGUNA ALTERNATIVA CABE EN PRESUPUESTO ({:.1f} m2) - revisar cap de crujia/n/frente".format(presupuesto_m2)
        }
    rec = alternativas[0]
    _avisos = rec.get("avisos", [])
    _txt_av = (u" | avisos: " + u"; ".join(_avisos)) if _avisos else u""
    _pisos_txt = u"/".join(str(p) for p in rec.get("pisos_por_bloque", [rec.get("pisos", 0)]))
    return {
        "schema": "f3_barras_salida_v01",
        "chip": chip,
        "alternativas": alternativas,
        "recomendada": rec["id"],
        "mensaje": u"{} barras crujía única {:.1f} m prof. (cap {:.1f} m), sep. {:.1f} m; ocupación {:.1f} m² (margen {:.1f} m²); entrepiso {:.2f} m; pisos {}{}".format(
            rec["n_barras"], rec["profundidad_m"], rec.get("crujia_max_m", CRUJIA_MAX_M_DEF),
            rec["separacion_m"], rec["ocupacion_total_m2"],
            presupuesto_m2 - rec["ocupacion_total_m2"], rec["floor_h"], _pisos_txt, _txt_av)
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
layout_espacial_json = ""

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
            _gh_leer(3, ["n_barras_objetivo", "n_barras", "n-barras"]), [2, 3, 4])
        if not _n_barras:
            _n_barras = [2, 3, 4]

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

        _paso = u"leer base normativa"
        _base_txt = _gh_str(globals().get("base_normativa_json") or "")
        if not _base_txt:
            raise ValueError(u"base_normativa_json vacío: cablear la salida base_json de F1_ETAPA2_NORMATIVA_v10 (#199)")
        _lote_m2 = json.loads(_base_txt)["area_lote_m2"]
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
        _crujia_max_in = _gh_num(_gh_leer(11, ["crujia_max_m", "crujia-max-m"]), None)
        if _crujia_max_in:
            globals()["crujia_max_m"] = _crujia_max_in
        _alternativas = iterar_barras(
            _lote_m2, _presupuesto, _n_barras, _sep_real, _prog, _crujia, _nucleo)
        _salida = build_barras_json(_chip, _alternativas, _lote_m2, _presupuesto, _io_max)

        _paso = u"publicar salidas: json"
        barras_json = _json_dumps_ascii(_salida)
        _paso = u"publicar salidas: mensaje"
        mensaje = u"F3 v03.9 | " + _gh_str(_salida.get("mensaje", ""))
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

        _paso = u"publicar salidas: layout"
        _lay_txt = u""
        _lay_ruta = u""
        try:
            _lay_txt, _lay_ruta = _leer_layout_casos(_chip)
        except Exception:
            _lay_txt, _lay_ruta = u"", u""
        layout_espacial_json = _lay_txt
        if _lay_txt:
            mensaje += u" | layout: " + _texto_seguro(_lay_ruta)
        else:
            mensaje += u" | layout: no encontrado en casos/"
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
        mensaje = u"F3 v03.9 | ERROR en [{}]: {}{}".format(_paso, _gh_str(_e_gh), _detalle)


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
    parser.add_argument("--base-normativa-json", help="Ruta o contenido JSON base_normativa_predio_v1 (v10)")
    parser.add_argument("--crujia-max-m", type=float, default=CRUJIA_MAX_M_DEF,
                        help="Cap de profundidad de crujia unica [m] (rango 9-12; default 10)")
    parser.add_argument("--pisos-por-bloque", help="Pisos por bloque (ej. '4,4,6')")
    parser.add_argument("--limites-pisos-json", help='Bandas desde el frente (ej. {\"bandas\":[{\"hasta_m\":15,\"max_pisos\":4}]})')
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

    # v03.6: base normativa y crujia_max para el generador (CLI)
    _g = globals()
    if args.base_normativa_json:
        _btxt = args.base_normativa_json
        if os.path.isfile(_btxt):
            try:
                _fh = io.open(_btxt, "rb")
                _raw = _fh.read()
                _fh.close()
                try:
                    _btxt = _raw.decode("utf-8")
                except Exception:
                    _btxt = _raw.decode("latin-1")
            except Exception:
                pass
        _g["base_normativa_json"] = _btxt
    if not _g.get("base_normativa_json"):
        parser.error("el generador v03.6 requiere --base-normativa-json (F1_ETAPA2_NORMATIVA_v10.base_json); no usa dimensiones ni pisos fijos")
    _g["crujia_max_m"] = args.crujia_max_m
    if args.pisos_por_bloque:
        _g["pisos_por_bloque"] = args.pisos_por_bloque
    if args.limites_pisos_json:
        _g["limites_pisos_json"] = args.limites_pisos_json

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
    print("Crujía máxima (cap):", args.crujia_max_m, "m")

    alternativas = iterar_barras(lote_m2, args.presupuesto_ocupacion, n_barras_lista,
                                  separacion_min, prog, args.bloques_crujia, args.bloques_nucleo)

    if not alternativas:
        print("ERROR: NINGUNA ALTERNATIVA CABE EN PRESUPUESTO")
        salida = build_barras_json(chip, [], lote_m2, args.presupuesto_ocupacion, args.io_max)
    else:
        print("Alternativas generadas: {}".format(len(alternativas)))
        for a in alternativas:
            print("  {}: {} barras, prof={:.1f}m, sep={:.1f}m, occ={:.1f}m2, GFA={:.1f}m2, floor_h={:.2f}m | avisos: {}".format(
                a["id"], a["n_barras"], a["profundidad_m"], a["separacion_m"],
                a["ocupacion_total_m2"], a["gfa_real_m2"], a["floor_h"],
                "; ".join(a.get("avisos", [])) or "-"))
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
    mensaje = (u"F3 v03.9 | aviso: entorno Rhino/.NET detectado pero 'ghenv' no "
               u"está disponible en el script; revisar el componente")

if _ES_MAIN and not _EN_GH and not _ES_IRON and not _ES_CLR:
    main()
