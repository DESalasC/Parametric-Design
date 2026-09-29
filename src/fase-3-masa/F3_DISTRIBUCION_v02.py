# -*- coding: utf-8 -*-
"""
================================================================================
F3_DISTRIBUCION_v02.py — Distribucion espacial del USO-MULTIPLE (Fase 3, 1a parte)

CAMBIOS v02 (2026-09-29):
  - Acople con la seccion 2 del orquestador: nuevo --usos filtra el mix a los
    usos marcados por el operador (renormaliza pct_gfa/gfa_m2 y unidades).
  - Multivolumen (parametros basicos): --bloques N, --bloques-distribucion,
    --bloques-separacion-m (min normativo 6,00 m, Anexo 5 1.10.b) y
    --bloques-desnivel-m (+ --bloques-azimut) -> casos/<id>/bloques.json
    (franjas del lote via OBB; contrato para el canvas VOLUM v09).

CAMBIOS v02.1 (2026-09-29):
  - ORIENTACION REFERIDA AL PREDIO: --bloques-distribucion pasa a
    automatico | paralelo_calle_acceso | perpendicular_calle_acceso |
    paralelo_lindero (+ --bloques-lindero) | angulo (+ --bloques-angulo-ref /
    --bloques-angulo-grados). Las franjas se generan en la direccion real de la
    calle de acceso o del lindero elegido (lados del predio: override del
    operador si existe) y se ordenan desde la entrada hacia el interior; los
    modos v02 (longitudinal/transversal/azimut) siguen aceptandose (compat).
  - NIVELES AUTOMATICOS ENTRE CALLES: --bloques-desnivel auto (default) propone
    la cota de cada bloque interpolando la topografia MDT del contexto: B1 =
    0.00 en la calle de acceso (Entrada) y BN en el nivel final del lote (via
    posterior o extremo opuesto, Salida); los bloques intermedios se reparten
    uniformemente. Manual sigue disponible (--bloques-desnivel-m).
  - ANCHO MINIMO POR PROGRAMA: cada franja debe alojar nucleo + circulacion +
    crujia (unidad maxima del mix / profundidad de referencia); si el numero de
    bloques pedido no cabe, se reduce y se avisa (n_max_recomendado), con el
    desglose en bloques.json -> ancho_min. Cada bloque informa unidades
    estimadas min-max segun el GFA del bloque.
================================================================================
Toma el programa del escenario D_MIXTO (override de usuario) de cada caso y genera:

  1. PROGRAMA        : desglose de usos, unidades y areas por nivel
  2. MATRIZ DE ADYACENCIAS : relaciones entre usos (Requerida/Deseable/Indiferente/
     Incompatible) con justificacion funcional y normativa (NSR-10, POT, accesibilidad)
  3. LAYOUT ESPACIAL : distribucion vertical de los usos + nucleos de servicios
     (escaleras, ascensores/transporte vertical, cuartos tecnicos, ductos, basuras)
  4. PLANOS ESQUEMATICOS : SVG por nivel (losa, nucleo, unidades por uso)
  5. MASA 3D (.3dm)  : cajas por nivel + nucleo, con capas y colores por uso
     (rhino3dm; se omite si no esta instalado)

USO:
  python F3_DISTRIBUCION_v02.py <CASO_ID | --chip CHIP> [--escenario D_MIXTO]
      [--usos "Vivienda,Local comercial"] [--bloques N]
      [--bloques-distribucion longitudinal|transversal]
      [--bloques-separacion-m 6.0] [--bloques-desnivel-m 3.4] [--bloques-azimut G]
  CASO_ID: A | B | C | B_SALUD   (lee el D_MIXTO del JSON de resultados de F2)

SALIDAS en src/fase-3-masa/casos/<id>/ :
  programa.json, matriz_adyacencias.json, layout_espacial.json, bloques.json,
  planos_<id>.html, F3_<id>.3dm
================================================================================
"""
import argparse
import io
import json
import math
import os
import sys

# rhino3dm (opcional): exporta la masa 3D si esta disponible en el venv
try:
    import rhino3dm
    _HAY_RHINO = True
except ImportError:
    rhino3dm = None
    _HAY_RHINO = False

# shapely (opcional): corta los bloques del multivolumen sobre el poligono del lote
try:
    from shapely.geometry import Polygon as _ShPolygon
    from shapely.geometry import LineString as _ShLineString
    from shapely.geometry import Point as _ShPoint
    from shapely import affinity as _sh_affinity
    _HAY_SHAPELY = True
except ImportError:
    _ShPolygon = None
    _ShLineString = None
    _ShPoint = None
    _sh_affinity = None
    _HAY_SHAPELY = False

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(BASE, "..", ".."))
FIN = os.path.join(ROOT, "src", "fase-2-demanda", "F2_Modelo_Financiero", "resultados")
OUT = os.path.join(BASE, "casos")

# ------------------------------------------------------------------ parametros
ALTURA_PISO = 3.0          # m, vivienda tipica
ALTURA_PISO_1 = 3.6        # m, primer piso (usos publicos)
OCUPACION_POT = 0.70       # ocupacion maxima (tratamiento Consolidacion)
NUCLEO_M2 = 28.0           # nucleo tipico por piso (2 escaleras + 2 asc + ductos)
ESCALERA_M2 = 13.5         # modulo de escalera (3.0 x 4.5 m)
ASCENSOR_M2 = 4.8          # ascensor 8 personas (~2.0 x 2.4 m)
# Cajas del nucleo (F3_VOLUM_GENERADOR_v07): circulacion y servicios SEPARADOS
ESCALERA_ANCHO_M = 2.7     # caja de escalera (2 tramos)
ESCALERA_LARGO_M = 5.0
ASCENSOR_ANCHO_M = 2.2
ASCENSOR_LARGO_M = 2.2
SERVICIOS_ANCHO_M = 2.0    # ductos/basuras/cuarto tecnico (separado de circulacion)
SERVICIOS_LARGO_M = 4.0
UNID_POR_ASCENSOR = 40.0   # NSR-10 practica: 1 ascensor / ~40 unidades
PERS_VIVIENDA = 2.5        # ocupantes por unidad de vivienda (promedio Bogota)
PERS_SERVICIOS_M2 = 0.10   # 1 persona / 10 m2 (NSR-10 C.2.3 oficinas/servicios)

# --------------------------------------------------------- multivolumen (v02.1)
CIRC_MIN_M = 1.2           # circulacion minima por lado del nucleo (m)
CRUJIA_PROF_REF_M = 9.0    # profundidad de referencia para derivar la crujia de una unidad (m)
ANCHO_NUCLEO_FALLBACK_M = 6.4  # nucleo 2 escaleras + ascensor + servicios (si no hay layout)

# --------------------------------------------------------- matriz de adyacencias
# Niveles: 3 = Requerida, 2 = Deseable, 1 = Indiferente, 0 = Incompatible
ADY = {
    ("Vivienda", "Vivienda"): (1, "Agrupacion por niveles; sin relacion programatica directa."),
    ("Vivienda", "Local comercial"): (2, "Local en primer piso con acceso independiente; "
        "segregacion de flujos residencial/comercial (NSR-10 Título C)."),
    ("Vivienda", "Consultorios"): (1, "Consultorios en pisos bajos; evitar mezcla en el mismo piso."),
    ("Vivienda", "Oficinas"): (1, "Flujos independientes; núcleos compartidos aceptables."),
    ("Vivienda", "Institucional salud"): (0, "Incompatible en el mismo piso: pacientes, insumos y "
        "biotecnologia exigen sector independiente (habilitacion IPS)."),
    ("Vivienda", "Hogar geriatrico"): (0, "Incompatible: el geriatrico requiere operacion autonoma "
        "(permanencia, cuidados) y control de accesos propio."),
    ("Local comercial", "Local comercial"): (1, "Continuidad de fachada activa."),
    ("Local comercial", "Consultorios"): (2, "Deseable: el cluster salud-local comparte lobby y "
        "estacionamiento de visitantes."),
    ("Local comercial", "Oficinas"): (2, "Deseable: servicios complementarios (cafeteria, banco)."),
    ("Local comercial", "Institucional salud"): (3, "Requerida: la IPS/laboratorio se apoya en el "
        "local (farmacia, insumos) y comparte acceso de ambulancias."),
    ("Local comercial", "Hogar geriatrico"): (2, "Deseable: servicios para residentes y visitas."),
    ("Consultorios", "Consultorios"): (3, "Requerida: agrupacion del cluster de salud (sinergia de "
        "remision y pacientes)."),
    ("Consultorios", "Oficinas"): (2, "Deseable: servicios profesionales complementarios."),
    ("Consultorios", "Institucional salud"): (3, "Requerida: la IPS remite a consultorios y viceversa."),
    ("Consultorios", "Hogar geriatrico"): (3, "Requerida: el geriatrico demanda consulta externa "
        "cercana (medicina general, enfermeria)."),
    ("Oficinas", "Oficinas"): (1, "Plantas libres; flexible."),
    ("Oficinas", "Institucional salud"): (2, "Deseable: areas administrativas de la IPS como oficinas."),
    ("Oficinas", "Hogar geriatrico"): (1, "Sin relacion directa."),
    ("Institucional salud", "Institucional salud"): (3, "Requerida: laboratorio junto a consulta "
        "especializada (tomas y resultados en el mismo edificio)."),
    ("Institucional salud", "Hogar geriatrico"): (3, "Requerida: el hogar geriatrico se apoya en "
        "servicios de salud institucional (caso real: San Luis cronicos junto a geriatricos)."),
    ("Hogar geriatrico", "Hogar geriatrico"): (1, "Operadores independientes; sector propio."),
}

# Usos presentes en los casos (canonicos)
USOS = ["Vivienda", "Local comercial", "Consultorios", "Oficinas",
        "Institucional salud", "Hogar geriatrico"]

# Claves normalizadas (tuple ordenado) para lookup simetrico
ADY_NORM = {tuple(sorted(k)): v for k, v in ADY.items()}


def normalizar_uso(uso: str) -> str:
    u = uso.lower()
    if "vivienda" in u or "vis" in u or "estandar" in u:
        return "Vivienda"
    if "local" in u or "comercio" in u:
        return "Local comercial"
    if "consultorio" in u:
        return "Consultorios"
    if "oficina" in u:
        return "Oficinas"
    if "institucional" in u or "ips" in u or "laboratorio" in u:
        return "Institucional salud"
    if "salud" in u and "institucional" not in u:
        return "Consultorios"
    if "geriatrico" in u:
        return "Hogar geriatrico"
    return u


# ------------------------------------------------------------------ casos F2
CASOS = {
    "A": {"resultados": "resultados_AAA0127AZPA_gfa1461_cl800.json", "gfa": 1461.0972,
          "lote_m2": 315.0, "huella_m2": 243.5162, "escenario": "D_MIXTO",
          "titulo": "A - El Prado (Suba) - envolvente F1 v06"},
    "B": {"resultados": "resultados_AAA0030JKOE.json", "gfa": 3312.575,
          "lote_m2": 946.45, "escenario": "D_MIXTO", "titulo": "B — La Candelaria"},
    "B_SALUD": {"resultados": "resultados_AAA0030JKOE.json", "gfa": 3312.575,
                "lote_m2": 946.45, "escenario": "D_MIXTO_SALUD",
                "titulo": "B — La Candelaria (variante salud)"},
    "C": {"resultados": "resultados_AAA0039KRMR.json", "gfa": 1100.0,
          "lote_m2": 356.96, "escenario": "D_MIXTO", "titulo": "C — Muzú (Puente Aranda)"},
}


def _cargar_programa(resultados_file, escenario, gfa=None, lote_m2=None, huella_m2=None):
    with io.open(os.path.join(FIN, resultados_file), encoding="utf-8") as f:
        paquete = json.load(f)
    esc = next((x for x in paquete["escenarios"] if x["escenario_id"] == escenario), None)
    if esc is None:
        for x in paquete["escenarios"]:
            if x.get("mix_usos_detalle"):
                esc = x
                escenario = x["escenario_id"]
                print("  [escenario] sin D_MIXTO exacto; se usa:", escenario)
                break
    if esc is None:
        raise ValueError("Sin escenario de uso mixto (D_MIXTO*) en " + str(resultados_file))
    det = esc.get("mix_usos_detalle") or []
    comps = []
    for c in det:
        comps.append({
            "uso": normalizar_uso(c["uso"]),
            "uso_original": c["uso"],
            "pct_gfa": c["pct_gfa"],
            "gfa_m2": c["gfa_i"],
            "num_unidades": c["num_unidades"],
            "unidad_m2": round(c["area_vendible_m2"] / c["num_unidades"], 1)
                         if c["num_unidades"] else 0.0,
            "area_vendible_m2": c["area_vendible_m2"],
        })
    gfa_total = gfa if gfa is not None else paquete.get("gfa_max_m2")
    lote = lote_m2 if lote_m2 is not None else (paquete.get("lote") or {}).get("area_m2")
    return {"gfa_total": gfa_total, "lote_m2": lote,
            "huella_m2": huella_m2, "escenario": escenario, "componentes": comps}


def leer_programa(caso_id):
    cfg = CASOS[caso_id]
    return _cargar_programa(cfg["resultados"], cfg["escenario"],
                            cfg.get("gfa"), cfg.get("lote_m2"), cfg.get("huella_m2"))


def _tiene_mixto(ruta):
    """2026-09-28: True si el JSON de resultados contiene un escenario de uso mixto
    (mix_usos_detalle, p.ej. D_MIXTO*)."""
    try:
        with io.open(ruta, encoding="utf-8") as f:
            paquete = json.load(f)
        for x in (paquete.get("escenarios") or []):
            if x.get("mix_usos_detalle"):
                return True
    except Exception:
        return False
    return False


def buscar_resultados(chip):
    """Localiza el JSON de resultados F2 de un CHIP.

    2026-09-28: prioriza un archivo que CONTENGA escenario de uso mixto (D_MIXTO*).
    El motor F2 estandar solo produce A/B/C, por lo que las corridas recientes del
    canonico pueden no traer el mix; en ese caso se usa el dataset dedicado del chip
    (p.ej. resultados_<CHIP>_gfa1461_cl800.json, generado por las utilidades).
    Orden: canonico -> resultados_<CHIP>_* por mtime desc; primer archivo con mix.
    Si ninguno tiene mix, devuelve el canonico (el error queda claro en _cargar_programa).
    """
    if not chip:
        return None
    resultados_dir = FIN
    canonico = "resultados_" + chip + ".json"
    candidatos = []
    if os.path.exists(os.path.join(resultados_dir, canonico)):
        candidatos.append(canonico)
    otros = [n for n in os.listdir(resultados_dir)
             if n.endswith(".json") and n.startswith("resultados_" + chip + "_")]
    otros.sort(key=lambda n: os.path.getmtime(os.path.join(resultados_dir, n)), reverse=True)
    candidatos.extend(otros)
    if not candidatos:
        return None
    for n in candidatos:
        if _tiene_mixto(os.path.join(resultados_dir, n)):
            return n
    return candidatos[0]


def leer_programa_chip(chip, escenario="D_MIXTO"):
    nombre = buscar_resultados(chip)
    if not nombre:
        raise ValueError("Sin resultados F2 para el CHIP " + str(chip))
    print("  [resultados] usando:", nombre, "| escenario:", escenario)
    return _cargar_programa(nombre, escenario)


def _titulo(caso_id):
    return (CASOS.get(caso_id) or {}).get("titulo", str(caso_id))


def distribuir_niveles(prog):
    """Huella = ocupacion x lote (o huella_m2 real de Fase 1 si viene en el caso);
    niveles = ceil(GFA/huella); reparto de usos."""
    # 2026-09-28: sin redondeo a 1 decimal. Caso B: 946,45*0,70 = 662,515 -> x5 = 3312,575
    # = GFA exacto; el redondeo a 662,5 hacia que ceil() diera 6 niveles (0,075 m2 de ruido).
    huella = prog.get("huella_m2") or (prog["lote_m2"] * OCUPACION_POT)
    # tolerancia 1e-6: un cociente casi entero no debe redondear al piso siguiente
    # por ruido de punto flotante/redondeo de areas (2026-09-28: B daba 6 por 0,075 m2)
    niveles = max(2, math.ceil(prog["gfa_total"] / huella - 1e-6))
    # Reparto vertical: usos publicos/salud abajo, vivienda arriba
    orden = {"Local comercial": 0, "Consultorios": 1, "Institucional salud": 1,
             "Hogar geriatrico": 2, "Oficinas": 2, "Vivienda": 9}
    comps = sorted(prog["componentes"], key=lambda c: orden.get(c["uso"], 5))
    # Asignar usos a niveles: los no-vivienda ocupan los primeros niveles
    niveles_uso = {}
    idx = 1
    for c in comps:
        if c["uso"] == "Vivienda":
            continue
        n = max(1, math.ceil(c["gfa_m2"] / huella))
        niveles_uso[c["uso"]] = list(range(idx, idx + n))
        idx += n
    # La vivienda ocupa el resto
    niveles_uso["Vivienda"] = list(range(idx, niveles + 1)) if idx <= niveles else []
    return huella, niveles, niveles_uso


def matriz_adyacencias(usos_presentes):
    usos = sorted(set(usos_presentes))
    matriz = {u: {} for u in usos}
    just = {}
    for a in usos:
        for b in usos:
            clave = tuple(sorted((a, b)))
            valor, razon = ADY_NORM.get(clave, (1, "Sin relacion programatica directa."))
            matriz[a][b] = matriz[b][a] = valor
            just[f"{a}|{b}"] = {"nivel": valor, "razon": razon}
    return {"usos": usos, "matriz": matriz, "justificaciones": just,
            "escala": {"3": "Requerida", "2": "Deseable", "1": "Indiferente", "0": "Incompatible"}}


def _disponer_nucleo(n_esc, asc):
    """Cajas del nucleo (relativas al centro del bloque) en 2 filas:
    fila 1 = escaleras, fila 2 = ascensores + servicios. Devuelve el desglose
    circulacion (escaleras+ascensores) vs servicios (ductos/basuras/cuarto) y
    el area REAL del hueco (bloque contenedor; el aire interior del bloque se
    considera circulacion interna del nucleo)."""
    circulacion = n_esc * ESCALERA_M2 + asc * ASCENSOR_M2
    servicios = 8.0
    ancho_f1 = n_esc * ESCALERA_ANCHO_M
    ancho_f2 = asc * ASCENSOR_ANCHO_M + SERVICIOS_ANCHO_M
    ancho_bloque = round(max(ancho_f1, ancho_f2), 1)
    largo_bloque = round(ESCALERA_LARGO_M + SERVICIOS_LARGO_M, 1)  # 9,0 m
    hueco = round(ancho_bloque * largo_bloque, 1)
    disp = []
    # Fila 1: escaleras centradas (y = -2,0 -> caja largo 5,0 en [-4,5, +0,5])
    x0 = -ancho_f1 / 2.0
    for i in range(n_esc):
        cx = x0 + ESCALERA_ANCHO_M * (i + 0.5)
        disp.append({"tipo": "circulacion", "componente": "Escalera {}".format(i + 1),
                     "ancho_m": ESCALERA_ANCHO_M, "largo_m": ESCALERA_LARGO_M,
                     "dx": round(cx, 2), "dy": -2.0})
    # Fila 2: ascensores + servicios centrados (y = +2,5 -> caja alto 4,0 en [+0,5, +4,5])
    x0 = -ancho_f2 / 2.0
    for i in range(asc):
        cx = x0 + ASCENSOR_ANCHO_M * (i + 0.5)
        disp.append({"tipo": "circulacion", "componente": "Ascensor {}".format(i + 1),
                     "ancho_m": ASCENSOR_ANCHO_M, "largo_m": ASCENSOR_LARGO_M,
                     "dx": round(cx, 2), "dy": 2.5})
    cx = x0 + ASCENSOR_ANCHO_M * asc + SERVICIOS_ANCHO_M / 2.0
    disp.append({"tipo": "servicios", "componente": "Servicios/tecnicos",
                 "ancho_m": SERVICIOS_ANCHO_M, "largo_m": SERVICIOS_LARGO_M,
                 "dx": round(cx, 2), "dy": 2.5})
    return {
        "circulacion_m2": round(circulacion, 1),
        "servicios_m2": round(servicios, 1),
        "hueco_m2": hueco,
        "bloque": {"ancho_m": ancho_bloque, "largo_m": largo_bloque},
        "disposicion": disp,
    }


def layout_espacial(prog, huella, niveles, niveles_uso):
    n_comp = {u: sum(c["num_unidades"] for c in prog["componentes"]
                     if c["uso"] == u) for u in set(c["uso"] for c in prog["componentes"])}
    pob_viv = n_comp.get("Vivienda", 0) * PERS_VIVIENDA
    area_serv = sum(c["gfa_m2"] for c in prog["componentes"] if c["uso"] != "Vivienda")
    pob_serv = area_serv * PERS_SERVICIOS_M2
    asc = max(1, math.ceil((pob_viv + pob_serv) / (UNID_POR_ASCENSOR * PERS_VIVIENDA)))
    if niveles > 6:
        esc = "presurizada (NSR-10 K.3.6: > 6 pisos o > 21 m)"
        n_esc = 2
    else:
        esc = "comun de evacuacion (NSR-10 Titulo K)"
        n_esc = 2
    nucleo_m2 = n_esc * ESCALERA_M2 + asc * ASCENSOR_M2 + 8.0  # ductos/basuras/cuarto
    nucleo_det = _disponer_nucleo(n_esc, asc)
    hueco_m2 = nucleo_det["hueco_m2"]
    niveles_out = []
    z_acum = 0.0
    for nv in range(1, niveles + 1):
        usos_nv = [u for u, ns in niveles_uso.items() if nv in ns]
        # GFA del nivel: huella si no es el ultimo (ajuste al GFA real)
        gfa_nv = huella if nv < niveles else round(prog["gfa_total"] - huella * (niveles - 1), 1)
        alt_nv = ALTURA_PISO_1 if nv == 1 else ALTURA_PISO
        niveles_out.append({
            "nivel": nv,
            "z_base_m": round(z_acum, 2),
            "altura_m": alt_nv,
            "usos": usos_nv,
            "gfa_m2": gfa_nv,
            "nucleo_m2": round(hueco_m2, 1),          # hueco REAL del nucleo
            "nucleo_solidos_m2": round(nucleo_m2, 1),  # circulacion + servicios
            "eficiencia_losa_pct": round(100 * (1 - hueco_m2 / gfa_nv), 1),
        })
        z_acum += alt_nv
    return {
        "huella_m2": huella, "niveles_total": niveles,
        "nucleos": {
            "escaleras": {"cantidad": n_esc, "tipo": esc, "modulo_m2": ESCALERA_M2},
            "ascensores": {"cantidad": asc, "capacidad_personas": 8, "modulo_m2": ASCENSOR_M2,
                           "criterio": "poblacion {:.0f} pers; 1 asc / ~{:.0f} unid".format(
                               pob_viv + pob_serv, UNID_POR_ASCENSOR)},
            "servicios": {"ductos_basuras_cuarto_m2": 8.0},
            "total_m2_piso": round(nucleo_m2, 1),     # solidos (compat v06)
            "circulacion_m2": nucleo_det["circulacion_m2"],
            "servicios_m2": nucleo_det["servicios_m2"],
            "hueco_m2_piso": hueco_m2,                # area real del hueco (bloque)
            "bloque": nucleo_det["bloque"],
            "disposicion": nucleo_det["disposicion"],
            "nota": "aire interior del bloque = circulacion interna del nucleo",
        },
        "reparto_vertical": niveles_uso,
        "poblacion_estimada": {"vivienda": round(pob_viv), "servicios": round(pob_serv),
                               "total": round(pob_viv + pob_serv)},
        "niveles": niveles_out,
    }


# ------------------------------------------------------------------ SVG planos
# --------------------------------------------------- usos / multivolumen (v02)
def filtrar_usos_programa(prog, usos_sel):
    """v02: filtra el mix del escenario a los usos elegidos en la seccion 2.

    usos_sel: lista de usos (etiquetas UI o canonicos; se normalizan). Vacio/None
    = sin filtro. Renormaliza pct_gfa/gfa_m2 (conserva el GFA total) y reescala
    las unidades. Devuelve (prog, aviso)."""
    if not usos_sel:
        return prog, ""
    sel = set(normalizar_uso(u) for u in usos_sel)
    comps = [c for c in prog["componentes"] if c["uso"] in sel]
    if not comps:
        return prog, "AVISO: los usos {} no aparecen en el mix; sin filtro.".format(
            ", ".join(sorted(sel)))
    quitados = [c["uso"] for c in prog["componentes"] if c["uso"] not in sel]
    if not quitados:
        return prog, ""
    tot = sum(c["pct_gfa"] for c in comps) or 1.0
    for c in comps:
        f = c["pct_gfa"] / tot
        c["pct_gfa"] = round(f, 6)
        c["gfa_m2"] = round(prog["gfa_total"] * f, 2)
        if c.get("num_unidades"):
            c["num_unidades"] = max(1, int(round(c["num_unidades"] * f)))
    prog = dict(prog)
    prog["componentes"] = comps
    prog["usos_filtrados"] = [c["uso"] for c in comps]
    return prog, "filtro de usos: {} (quitados: {})".format(
        ", ".join(c["uso"] for c in comps), ", ".join(quitados))


def _leer_lote_local(chip):
    """v02: poligono del lote (marco local) desde el contexto del CHIP o el activo."""
    for nombre in ("{}-contexto.json".format(chip), "CHIP-contexto.json"):
        ruta = os.path.join(ROOT, "data", "pot-cache", nombre)
        if not os.path.exists(ruta):
            continue
        try:
            with io.open(ruta, encoding="utf-8") as f:
                data = json.load(f)
            verts = ((data.get("lote_objetivo") or {}).get("vertices_3d_local")) or []
            pts = [(float(v[0]), float(v[1])) for v in verts if len(v) >= 2]
            if len(pts) >= 3:
                return pts, ruta
        except Exception:
            continue
    return None, None


def _leer_contexto_chip(chip):
    """v02.1: contexto completo del CHIP (topografia, vias_oficiales, lote)."""
    for nombre in ("{}-contexto.json".format(chip), "CHIP-contexto.json"):
        ruta = os.path.join(ROOT, "data", "pot-cache", nombre)
        if not os.path.exists(ruta):
            continue
        try:
            with io.open(ruta, encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            continue
    return None


def _leer_lados_chip(chip):
    """v02.1: lados del predio (override del operador si existe; si no, auto)."""
    for nombre in ("{}-vecinos-por-lado-override.json".format(chip),
                   "{}-vecinos-por-lado.json".format(chip),
                   "CHIP-vecinos-por-lado.json"):
        ruta = os.path.join(ROOT, "data", "pot-cache", nombre)
        if not os.path.exists(ruta):
            continue
        try:
            with io.open(ruta, encoding="utf-8") as f:
                data = json.load(f)
            lados = data.get("lados") or []
            if lados:
                return lados, ruta
        except Exception:
            continue
    return [], None


def _lado_por_cardinal(lados, cardinal):
    """v02.1: lado cuyo cardinal empieza por `cardinal` (el mas largo si hay varios)."""
    c = (cardinal or "").strip().lower()
    if not c:
        return None
    cands = []
    for l in (lados or []):
        card = str(l.get("cardinal") or "").lower()
        lbl = str(l.get("cardinal_label") or "").lower()
        if card.startswith(c) or lbl.startswith(c):
            cands.append(l)
    if not cands:
        return None
    cands.sort(key=lambda l: float(l.get("longitud_m") or 0.0), reverse=True)
    return cands[0]


def _lado_calle_acceso(lados):
    """v02.1: lado de la calle de acceso (frente_override='via' o frente='via')."""
    cands = [l for l in (lados or [])
             if l.get("frente_override") == "via" or l.get("frente") == "via"]
    if not cands:
        return None
    cands.sort(key=lambda l: float(l.get("longitud_m") or 0.0), reverse=True)
    return cands[0]


def _lado_via_posterior(lados, lado_acceso):
    """v02.1: via posterior (frente_override='via_no_frontal') opuesta a la de acceso."""
    if not lado_acceso or lado_acceso.get("azimut_grados") is None:
        return None
    op = (float(lado_acceso["azimut_grados"]) + 180.0) % 360.0

    def _dif(a, b):
        d = abs((float(a) - float(b)) % 360.0)
        return min(d, 360.0 - d)

    cands = [l for l in (lados or [])
             if l.get("frente_override") == "via_no_frontal"
             and l.get("azimut_grados") is not None]
    if not cands:
        return None
    cands.sort(key=lambda l: _dif(l["azimut_grados"], op))
    return cands[0] if _dif(cands[0]["azimut_grados"], op) <= 75.0 else None


def _dir_y_ancla_lado(lado, pts):
    """v02.1: direccion media (grados locales) y punto medio del lado
    (segmentos = indices de arista del poligono del lote)."""
    n = len(pts)
    dx = dy = mx = my = 0.0
    k = 0
    for s in (lado.get("segmentos") or []):
        i = int(s) % n
        a = pts[i]
        b = pts[(i + 1) % n]
        dx += b[0] - a[0]
        dy += b[1] - a[1]
        mx += (a[0] + b[0]) / 2.0
        my += (a[1] + b[1]) / 2.0
        k += 1
    if k == 0:
        return None, None
    return math.degrees(math.atan2(dy, dx)) % 360.0, (mx / k, my / k)


def _normal_interna(ang_lado, ancla, pts):
    """v02.1: normal al lado que apunta hacia el INTERIOR del lote (grados locales)."""
    if ang_lado is None or ancla is None or not pts:
        return None
    cx = sum(p[0] for p in pts) / float(len(pts))
    cy = sum(p[1] for p in pts) / float(len(pts))
    vx, vy = cx - ancla[0], cy - ancla[1]
    for cand in (ang_lado + 90.0, ang_lado - 90.0):
        nx, ny = math.cos(math.radians(cand)), math.sin(math.radians(cand))
        if (nx * vx + ny * vy) > 0:
            return cand % 360.0
    return None


def _azimut_de_local(ang_local):
    """v02.1: angulo local -> azimut geografico del proyecto (0=norte, horario)."""
    return (90.0 - float(ang_local)) % 360.0


def _local_de_azimut(az):
    """v02.1: azimut geografico -> angulo local (marco del contexto)."""
    return (90.0 - float(az)) % 360.0


def _ejes_obb_local(pts):
    """v02.1: direcciones locales del eje largo y corto del OBB del lote."""
    poly = _ShPolygon(pts)
    if not poly.is_valid:
        poly = poly.buffer(0)
    oc = list(poly.minimum_rotated_rectangle.exterior.coords)
    lados_ = []
    for i in range(4):
        (x1, y1), (x2, y2) = oc[i], oc[i + 1]
        lados_.append((math.hypot(x2 - x1, y2 - y1),
                       math.degrees(math.atan2(y2 - y1, x2 - x1)) % 360.0))
    lados_.sort(key=lambda t: t[0], reverse=True)
    return lados_[0][1], lados_[2][1]


def _via_cercana(ctx, pts):
    """v02.1: via oficial mas cercana al lote -> (nombre, distancia_m) o None."""
    if not ctx or not _HAY_SHAPELY or not pts:
        return None
    poly = _ShPolygon(pts)
    if not poly.is_valid:
        poly = poly.buffer(0)
    mejor = None
    for v in (ctx.get("vias_oficiales") or []):
        pares = []
        for c in (v.get("coordenadas_local") or []):
            try:
                if isinstance(c, dict):
                    pares.append((float(c.get("x")), float(c.get("y"))))
                else:
                    pares.append((float(c[0]), float(c[1])))
            except Exception:
                continue
        pares = [p for p in pares if not (math.isnan(p[0]) or math.isnan(p[1]))]
        if len(pares) < 2:
            continue
        try:
            d = float(poly.distance(_ShLineString(pares)))
        except Exception:
            continue
        nombre = str(v.get("nombre") or v.get("codigo") or "").strip()
        if nombre and (mejor is None or d < mejor[1]):
            mejor = (nombre, round(d, 1))
    if mejor and mejor[1] <= 60.0:
        return mejor
    return None


def _resumen_lado(lado, via=None):
    """v02.1: resumen serializable de un lado (para bloques.json)."""
    if not lado:
        return None
    out = {"lado_id": lado.get("lado_id"),
           "cardinal_label": lado.get("cardinal_label") or lado.get("cardinal"),
           "azimut_grados": lado.get("azimut_grados"),
           "longitud_m": lado.get("longitud_m"),
           "frente_override": lado.get("frente_override")}
    if via:
        out["via_cercana_nombre"] = via[0]
        out["via_cercana_dist_m"] = via[1]
    return out


def _resolver_orientacion(pts, lados, dist, lindero_sel, ang_ref, ang_deg,
                          azimut_in, lado_acc, via, avisos):
    """v02.1: traduce el modo de distribucion (referencias del predio) a la
    direccion local de las franjas (franja_local) y del reparto (reparto_local),
    con descripciones para el operador. Sin datos del predio cae al eje del lote."""
    acc_lbl = None
    if lado_acc:
        acc_lbl = lado_acc.get("cardinal_label") or "lado {}".format(lado_acc.get("lado_id"))
        if via and via[1] is not None and via[1] <= 15.0:
            acc_lbl = "{} ({})".format(acc_lbl, via[0])
    res = {"modo": dist, "referencia": None, "ancla": None,
           "franja_local": None, "reparto_local": None,
           "desc_franja": "", "desc_reparto": "",
           "calle_acceso": _resumen_lado(lado_acc, via)}

    ang_acc, ancla_acc = (None, None)
    if lado_acc and pts:
        ang_acc, ancla_acc = _dir_y_ancla_lado(lado_acc, pts)

    if dist in ("automatico", "paralelo_calle_acceso", "perpendicular_calle_acceso"):
        if ang_acc is None:
            eje_largo, eje_corto = _ejes_obb_local(pts)
            avisos.append("Sin lado con frente a via (frente_override='via'); se usa el eje del lote.")
            res["modo"] = "longitudinal"
            res["franja_local"] = eje_corto
            res["reparto_local"] = (eje_corto + 90.0) % 360.0
            res["referencia"] = "eje corto del lote (sin calle de acceso)"
            res["desc_franja"] = "franjas a lo largo del lote (sin referencia de via)"
            res["desc_reparto"] = "reparto sobre el eje largo del lote"
            return res
        if dist == "perpendicular_calle_acceso":
            res["reparto_local"] = ang_acc
            res["franja_local"] = _normal_interna(ang_acc, ancla_acc, pts)
            res["referencia"] = "calle de acceso ({})".format(acc_lbl)
            res["desc_franja"] = "franjas perpendiculares a la calle de acceso ({})".format(acc_lbl)
            res["desc_reparto"] = "reparto paralelo a la calle de acceso"
        else:
            res["franja_local"] = ang_acc
            res["reparto_local"] = _normal_interna(ang_acc, ancla_acc, pts)
            res["referencia"] = "calle de acceso ({})".format(acc_lbl)
            res["desc_franja"] = "franjas paralelas a la calle de acceso ({})".format(acc_lbl)
            res["desc_reparto"] = "reparto desde la calle hacia el interior del lote (subiendo)"
        res["ancla"] = ancla_acc
        return res

    if dist == "paralelo_lindero":
        lado = _lado_por_cardinal(lados, lindero_sel)
        if lado and pts:
            ang, ancla = _dir_y_ancla_lado(lado, pts)
            lbl = lado.get("cardinal_label") or "lado {}".format(lado.get("lado_id"))
            res["franja_local"] = ang
            res["reparto_local"] = _normal_interna(ang, ancla, pts)
            res["referencia"] = "lindero {}".format(lbl)
            res["ancla"] = ancla
            res["desc_franja"] = "franjas paralelas al lindero {}".format(lbl)
            res["desc_reparto"] = "reparto desde el lindero hacia el interior del lote"
            return res
        eje_largo, eje_corto = _ejes_obb_local(pts)
        avisos.append("Lindero '{}' no encontrado en los lados del predio; se usa el eje del lote.".format(lindero_sel))
        res["modo"] = "longitudinal"
        res["franja_local"] = eje_corto
        res["reparto_local"] = (eje_corto + 90.0) % 360.0
        res["referencia"] = "eje corto del lote"
        res["desc_franja"] = "franjas a lo largo del lote"
        res["desc_reparto"] = "reparto sobre el eje largo del lote"
        return res

    if dist == "angulo":
        base_az = 0.0
        ref_txt = "norte del plano"
        ancla = None
        if ang_ref == "calle_acceso" and ang_acc is not None:
            base_az = _azimut_de_local(ang_acc)
            ref_txt = "calle de acceso ({})".format(acc_lbl)
            ancla = ancla_acc
        elif ang_ref == "lindero":
            lado = _lado_por_cardinal(lados, lindero_sel)
            if lado and pts:
                ang_l, ancla = _dir_y_ancla_lado(lado, pts)
                base_az = _azimut_de_local(ang_l)
                ref_txt = "lindero {}".format(lado.get("cardinal_label") or lado.get("lado_id"))
            else:
                avisos.append("Lindero '{}' no encontrado; angulo referido al norte.".format(lindero_sel))
        franja_az = (base_az + float(ang_deg or 0.0)) % 360.0
        res["franja_local"] = _local_de_azimut(franja_az)
        res["reparto_local"] = (res["franja_local"] + 90.0) % 360.0
        res["referencia"] = ref_txt
        res["ancla"] = ancla
        res["desc_franja"] = "franjas a {}° (horario) respecto a {}".format(round(float(ang_deg or 0.0), 1), ref_txt)
        if ang_acc is not None:
            rel = (franja_az - _azimut_de_local(ang_acc)) % 360.0
            res["desc_franja"] += "; angulo respecto a la calle de acceso: {}°".format(round(rel, 1))
        res["desc_reparto"] = "reparto perpendicular a las franjas"
        return res

    # compat v02: --bloques-azimut (angulo local del reparto)
    if azimut_in is not None:
        res["reparto_local"] = float(azimut_in) % 360.0
        res["franja_local"] = (res["reparto_local"] + 90.0) % 360.0
        res["referencia"] = "azimut local (compat v02)"
        res["desc_franja"] = "franjas a {}° locales (compat v02)".format(round(float(azimut_in), 1))
        res["desc_reparto"] = "reparto perpendicular a las franjas"
        return res

    if dist in ("longitudinal", "transversal"):
        eje_largo, eje_corto = _ejes_obb_local(pts)
        res["franja_local"] = eje_corto if dist == "longitudinal" else eje_largo
        res["reparto_local"] = (res["franja_local"] + 90.0) % 360.0
        res["referencia"] = "eje {} del lote".format("corto" if dist == "longitudinal" else "largo")
        res["desc_franja"] = "franjas a lo {} del lote (compat v02)".format(
            "largo" if dist == "longitudinal" else "ancho")
        res["desc_reparto"] = "reparto sobre el eje {} del lote".format(
            "largo" if dist == "longitudinal" else "corto")
        return res

    eje_largo, eje_corto = _ejes_obb_local(pts)
    res["modo"] = "longitudinal"
    res["franja_local"] = eje_corto
    res["reparto_local"] = (eje_corto + 90.0) % 360.0
    res["referencia"] = "eje corto del lote"
    res["desc_franja"] = "franjas a lo largo del lote"
    res["desc_reparto"] = "reparto sobre el eje largo del lote"
    return res


def _niveles_terreno_chip(ctx, pts, lado_entrada, lado_salida):
    """v02.1: cotas MDT de ENTRADA (calle de acceso) y SALIDA (via posterior o
    extremo opuesto del lote). perfil_lados.id = indice de arista del poligono.
    Devuelve {'entrada_m','salida_m','delta_m','fuente'} o None."""
    if not ctx or not pts:
        return None
    top = ctx.get("topografia") or {}
    perf = {}
    for p in (top.get("perfil_lados") or []):
        try:
            if p.get("z_media_m") is not None:
                perf[int(p["id"])] = float(p["z_media_m"])
        except Exception:
            continue
    if not perf:
        return None

    def _z_lado(lado):
        segs = []
        for s in ((lado or {}).get("segmentos") or []):
            try:
                s = int(s)
            except Exception:
                continue
            if s in perf:
                segs.append(s)
        if not segs:
            return None
        return sum(perf[s] for s in segs) / len(segs)

    z_ent = _z_lado(lado_entrada)
    if z_ent is None:
        return None
    z_sal = _z_lado(lado_salida) if lado_salida is not None else None
    fuente = "topografia.perfil_lados (MDT Catastro)"
    if z_sal is None:
        ang, ancla = _dir_y_ancla_lado(lado_entrada, pts)
        inward = _normal_interna(ang, ancla, pts)
        if inward is None:
            return None
        ux, uy = math.cos(math.radians(inward)), math.sin(math.radians(inward))
        n = len(pts)
        proys = []
        for i in range(n):
            a, b = pts[i], pts[(i + 1) % n]
            mx, my = (a[0] + b[0]) / 2.0, (a[1] + b[1]) / 2.0
            proys.append(mx * ux + my * uy)
        pmax = max(proys)
        segs = [i for i, p in enumerate(proys) if p >= pmax - 3.0 and i in perf]
        if not segs:
            return None
        z_sal = sum(perf[s] for s in segs) / len(segs)
        fuente += " (salida = extremo opuesto del lote)"
    else:
        fuente += " (salida = via posterior)"
    return {"entrada_m": round(z_ent, 2), "salida_m": round(z_sal, 2),
            "delta_m": round(z_sal - z_ent, 2), "fuente": fuente}


def _ancho_min_programa(prog, layout=None):
    """v02.1: ancho minimo de bloque para alojar el programa basico:
    nucleo + 2 x circulacion + crujia de la unidad mas grande del mix."""
    bloque = ((layout or {}).get("nucleos") or {}).get("bloque") or {}
    ancho_nucleo = float(bloque.get("ancho_m") or ANCHO_NUCLEO_FALLBACK_M)
    unidades = [(c.get("uso"), float(c.get("unidad_m2") or 0.0))
                for c in (prog.get("componentes") or [])]
    unidades = [(u, a) for u, a in unidades if a > 0]
    crujia_por_uso = {u: round(a / CRUJIA_PROF_REF_M, 2) for u, a in unidades}
    unidad_max = max([a for _u, a in unidades], default=0.0)
    crujia_min = round(max(unidad_max / CRUJIA_PROF_REF_M, 4.0), 2)
    ancho_min = round(ancho_nucleo + 2.0 * CIRC_MIN_M + crujia_min, 2)
    return {
        "ancho_min_m": ancho_min,
        "nucleo_m": round(ancho_nucleo, 2),
        "circulacion_m": CIRC_MIN_M,
        "crujia_min_m": crujia_min,
        "crujia_por_uso": crujia_por_uso,
        "unidad_max_m2": round(unidad_max, 1),
        "prof_ref_m": CRUJIA_PROF_REF_M,
        "formula": "ancho_min = nucleo + 2 x circulacion + crujia (unidad_max / prof_ref)",
    }


def _unidades_bloque(prog, gfa_bloque):
    """v02.1: unidades estimadas min-max por uso para el GFA de un bloque."""
    out = {}
    for c in (prog.get("componentes") or []):
        u = float(c.get("unidad_m2") or 0.0)
        if u <= 0 or not c.get("num_unidades"):
            continue
        gfa_u = float(gfa_bloque) * float(c.get("pct_gfa") or 0.0)
        n_min = int(math.floor(gfa_u / u + 1e-9))
        n_max = int(math.ceil(gfa_u / u - 1e-9))
        out[c["uso"]] = {"unidad_m2": round(u, 1), "min": n_min, "max": max(n_min, n_max)}
    return out


def _bandas_dir(pts, n, sep, franja_dir_deg, malla_pts=None):
    """v02.1: divide el lote en n franjas cuya direccion LARGA es `franja_dir_deg`
    (grados locales); el reparto es perpendicular a esa direccion con separacion
    `sep` entre franjas. Devuelve (franjas, aviso). Cada franja incluye el ancho
    (lado corto de su OBB), el centro y la cota media local de la malla MDT."""
    poly = _ShPolygon(pts)
    if not poly.is_valid:
        poly = poly.buffer(0)
    obb_r = _sh_affinity.rotate(poly, -float(franja_dir_deg), origin=(0, 0), use_radians=False)
    br = list(obb_r.exterior.coords)
    xmin = min(p[0] for p in br); xmax = max(p[0] for p in br)
    ymin = min(p[1] for p in br); ymax = max(p[1] for p in br)
    usable = (ymax - ymin) - (n - 1) * sep
    if usable <= 0.5:
        return [], ("AVISO: {} bloques con separacion {:.2f} m no caben en "
                    "{:.1f} m; se reduce a 1 bloque.".format(n, sep, ymax - ymin))
    alto = usable / n
    franjas = []
    y = ymin
    for _i in range(n):
        rect = _ShPolygon([(xmin, y), (xmax, y), (xmax, y + alto), (xmin, y + alto)])
        rect = _sh_affinity.rotate(rect, float(franja_dir_deg), origin=(0, 0), use_radians=False)
        inter = poly.intersection(rect)
        if inter.is_empty or inter.area < 5.0:
            y += alto + sep
            continue
        coords = list(inter.exterior.coords)
        if coords and coords[0] == coords[-1]:
            coords = coords[:-1]
        sc = list(inter.minimum_rotated_rectangle.exterior.coords)
        lados_s = [math.hypot(sc[k + 1][0] - sc[k][0], sc[k + 1][1] - sc[k][1])
                   for k in range(4)]
        ancho = min(lados_s)
        z_med = None
        if malla_pts:
            zs = [p[2] for p in malla_pts if inter.contains(_ShPoint(p[0], p[1]))]
            if zs:
                z_med = round(sum(zs) / len(zs), 2)
        franjas.append({"poligono_local": [[round(px, 3), round(py, 3)] for px, py in coords],
                        "area": float(inter.area),
                        "ancho_m": round(float(ancho), 2),
                        "centro": [round(inter.centroid.x, 2), round(inter.centroid.y, 2)],
                        "z_medio_local_m": z_med})
        y += alto + sep
    return franjas, ""


def generar_bloques(chip, prog, huella, niveles, cfg, layout=None):
    """v02.1: propuesta de multivolumen referida al predio (ver CAMBIOS v02.1).

    cfg: {n, distribucion, lindero, angulo_ref, angulo_grados, separacion_m,
    desnivel_auto, desnivel_m, azimut_grados}. Franjas dirigidas por la calle de
    acceso o el lindero elegido (o ejes del lote en compat v02); ordenadas desde
    la entrada hacia el interior; z_base_m relativo a la cota de ENTRADA (B1 =
    0.00); el modo auto interpola la topografia MDT (Entrada -> Salida)."""
    n_req = max(1, min(6, int(cfg.get("n") or 1)))
    dist = (cfg.get("distribucion") or "automatico").strip().lower()
    sep = float(cfg.get("separacion_m") if cfg.get("separacion_m") is not None else 6.0)
    azimut_in = cfg.get("azimut_grados")
    lindero_sel = cfg.get("lindero")
    ang_ref = (cfg.get("angulo_ref") or "calle_acceso").strip().lower()
    ang_deg = float(cfg.get("angulo_grados") or 0.0)
    desn_auto = bool(cfg.get("desnivel_auto"))
    desn_man = cfg.get("desnivel_m")
    if isinstance(desn_man, str):
        try:
            desn_man = float(desn_man)
        except ValueError:
            desn_man = None
    if desn_auto:
        desn_man = None
    if not desn_auto and desn_man is None:
        desn_man = 0.0
    SEP_MIN = 6.0
    avisos = []
    if n_req > 1 and sep < SEP_MIN:
        avisos.append("Separacion {:.2f} m < minimo 6.00 m (Anexo 5 1.10.b); "
                      "se usa {:.2f} m.".format(sep, SEP_MIN))
        sep = SEP_MIN

    # --- datos del predio (lote, lados, topografia, via de acceso)
    pts, ruta_ctx_lote = _leer_lote_local(chip)
    ctx = _leer_contexto_chip(chip)
    lados, ruta_lados = _leer_lados_chip(chip)
    lado_acc = _lado_calle_acceso(lados)
    lado_post = _lado_via_posterior(lados, lado_acc)
    via = _via_cercana(ctx, pts) if (ctx and pts) else None
    malla = None
    z_ref_lote = None
    if ctx:
        malla = [(p["x_local"], p["y_local"], p["z_local"])
                 for p in ((ctx.get("topografia") or {}).get("malla_terreno") or [])
                 if p.get("z_local") is not None]
        z_ref_lote = (((ctx.get("metadata") or {}).get("origen_sirgas") or {}).get("z"))

    orient = _resolver_orientacion(pts, lados, dist, lindero_sel, ang_ref, ang_deg,
                                   azimut_in, lado_acc, via, avisos)
    ancho_min = _ancho_min_programa(prog, layout)

    # --- geometria: franjas dirigidas + reduccion por ancho minimo
    fuente = "esquema (cuadrado de referencia)"
    franjas = []
    n = n_req
    first_fail = None
    if pts and _HAY_SHAPELY and orient["franja_local"] is not None:
        while True:
            franjas, av = _bandas_dir(pts, n, sep, orient["franja_local"], malla)
            if av:
                avisos.append(av)
                n = 1
                franjas, _ = _bandas_dir(pts, 1, sep, orient["franja_local"], malla)
                break
            angostas = [f["ancho_m"] for f in franjas
                        if f["ancho_m"] < ancho_min["ancho_min_m"] - 0.05]
            if not angostas or n <= 1:
                break
            if first_fail is None:
                first_fail = min(angostas)
            n -= 1
        if franjas:
            if len(franjas) < n:
                n = len(franjas)
            fuente = "lote_objetivo (franjas dirigidas {:.1f} deg; ref: {}) - {}".format(
                orient["franja_local"], orient["referencia"] or "eje del lote",
                os.path.basename(ruta_ctx_lote or ""))
            if ruta_lados:
                fuente += "; lados: {}".format(os.path.basename(ruta_lados))
        else:
            n = 1
    if n < n_req and franjas:
        extra = ("; franja mas angosta al solicitado: {:.1f} m".format(first_fail)
                 if first_fail is not None else "")
        avisos.append("Bloques solicitados: {} -> usados {} por ancho minimo por programa "
                      "({:.1f} m = nucleo {:.1f} + 2x circulacion {:.1f} + crujia {:.1f}){}.".format(
                          n_req, n, ancho_min["ancho_min_m"], ancho_min["nucleo_m"],
                          ancho_min["circulacion_m"], ancho_min["crujia_min_m"], extra))
    if not franjas:
        ref = math.sqrt(max(float(prog.get("lote_m2") or huella or 1.0), 1.0))
        usable = ref - (n - 1) * sep
        ancho = usable / n if n > 1 else ref
        x = 0.0
        for _i in range(n):
            franjas.append({
                "poligono_local": [[round(x, 3), 0.0],
                                   [round(x + ancho, 3), 0.0],
                                   [round(x + ancho, 3), round(ref, 3)],
                                   [round(x, 3), round(ref, 3)]],
                "area": round(ancho * ref, 2),
                "ancho_m": round(min(ancho, ref), 2),
                "centro": [round(x + ancho / 2.0, 2), round(ref / 2.0, 2)],
                "z_medio_local_m": None})
            x += ancho + sep

    # --- orden desde la entrada (ancla) hacia el interior
    ancla = orient.get("ancla")
    if ancla is not None and len(franjas) > 1:
        franjas.sort(key=lambda f: math.hypot(f["centro"][0] - ancla[0],
                                              f["centro"][1] - ancla[1]))
    if len(franjas) > n and n > 0:
        franjas = franjas[:n]

    # --- niveles: auto (topografia Entrada -> Salida) o manual
    terreno = _niveles_terreno_chip(ctx, pts, lado_acc, lado_post) if (ctx and pts) else None
    niveles_info = {"modo": "manual",
                    "desnivel_m": (desn_man if len(franjas) > 1 else 0.0),
                    "entrada_m": None, "salida_m": None, "delta_m": None,
                    "fuente": "manual (paso entre bloques)"}
    z_rel = [0.0] * len(franjas)
    if len(franjas) > 1:
        if desn_auto:
            if terreno and terreno.get("delta_m") is not None:
                paso = terreno["delta_m"] / float(len(franjas) - 1)
                z_rel = [round(paso * i, 2) for i in range(len(franjas))]
                niveles_info = {"modo": "auto", "desnivel_m": round(paso, 2),
                                "entrada_m": terreno["entrada_m"],
                                "salida_m": terreno["salida_m"],
                                "delta_m": terreno["delta_m"],
                                "fuente": terreno["fuente"]}
            else:
                avisos.append("Sin topografia/lado de salida para niveles automaticos; "
                              "se usa paso 0.00 m (use --bloques-desnivel-m para override).")
        else:
            z_rel = [round(desn_man * i, 2) for i in range(len(franjas))]
            if terreno and terreno.get("delta_m") is not None:
                niveles_info.update({"entrada_m": terreno["entrada_m"],
                                     "salida_m": terreno["salida_m"],
                                     "delta_m": terreno["delta_m"]})

    # --- ensamble de bloques
    area_total = sum(f["area"] for f in franjas) or 0.0
    bloques = []
    for i, f in enumerate(franjas):
        huella_i = round(huella * f["area"] / area_total, 2) if area_total else 0.0
        gfa_i = round(huella_i * niveles, 2)
        z_terreno_abs = None
        if f.get("z_medio_local_m") is not None and z_ref_lote is not None:
            z_terreno_abs = round(float(f["z_medio_local_m"]) + float(z_ref_lote), 2)
        bloques.append({
            "id": "B{}".format(i + 1), "orden": i + 1,
            "poligono_local": f["poligono_local"],
            "area_lote_m2": round(f["area"], 2),
            "ancho_m": f.get("ancho_m"),
            "huella_objetivo_m2": huella_i,
            "pisos": niveles,
            "z_base_m": z_rel[i],
            "z_terreno_medio_m": z_terreno_abs,
            "gfa_objetivo_m2": gfa_i,
            "unidades_estimadas": _unidades_bloque(prog, gfa_i),
        })

    # --- n max recomendado por ancho (para la UI)
    n_max = len(franjas)
    if pts and _HAY_SHAPELY and orient["franja_local"] is not None and len(franjas) >= 1:
        try:
            for n_try in range(len(franjas) + 1, 7):
                fj, av = _bandas_dir(pts, n_try, sep, orient["franja_local"], malla)
                if av or not fj:
                    break
                if all(x["ancho_m"] >= ancho_min["ancho_min_m"] - 0.05 for x in fj):
                    n_max = n_try
                else:
                    break
        except Exception:
            pass

    orient_json = {
        "modo": orient["modo"],
        "referencia": orient["referencia"],
        "franja_descripcion": orient["desc_franja"],
        "reparto_descripcion": orient["desc_reparto"],
        "franja_dir_local_deg": (round(orient["franja_local"], 2)
                                 if orient["franja_local"] is not None else None),
        "azimut_franja_deg": (round(_azimut_de_local(orient["franja_local"]), 1)
                              if orient["franja_local"] is not None else None),
        "azimut_reparto_deg": (round(_azimut_de_local(orient["reparto_local"]), 1)
                               if orient["reparto_local"] is not None else None),
        "calle_acceso": orient.get("calle_acceso"),
    }
    nota = ("Propuesta de multivolumen v02.1: franjas referidas al predio y ordenadas desde "
            "la entrada; z_base_m relativo a la cota de ENTRADA (B1 = 0.00); auto interpola la "
            "topografia MDT (Entrada -> nivel final del lote). Poligonos esquematicos: el canvas "
            "(VOLUM v09) los re-encaja en la envolvente F1. z_terreno_medio_m = MDT absoluto (m); "
            "z_local del marco del canvas = MDT - origen_sirgas.z.")
    return {
        "chip": chip, "n": len(bloques), "n_solicitado": n_req, "n_max_recomendado": n_max,
        "distribucion": dist, "orientacion": orient_json,
        "lindero": lindero_sel,
        "angulo": ({"referencia": ang_ref, "grados": ang_deg} if dist == "angulo" else None),
        "azimut_grados": azimut_in,
        "separacion_m": (sep if len(bloques) > 1 else 0.0),
        "separacion_min_norma_m": SEP_MIN,
        "desnivel_m": ((niveles_info.get("desnivel_m") or 0.0) if len(bloques) > 1 else 0.0),
        "niveles": niveles_info,
        "ancho_min": ancho_min,
        "fuente_geometria": fuente, "avisos": avisos, "nota": nota,
        "bloques": bloques,
    }


COLORES = {"Vivienda": "#8FB8DE", "Local comercial": "#F2C14E",
           "Consultorios": "#7BC8A4", "Oficinas": "#C9A8E0",
           "Institucional salud": "#E8877C", "Hogar geriatrico": "#E8B4D0",
           "Nucleo": "#555555", "Circulacion": "#EEEEEE"}


def plano_nivel_svg(nv, huella, nucleo_info, usos_nv, unidades_uso, escala=2.0):
    """Planta esquematica SVG: losa + bloque del nucleo (cajas de circulacion y
    servicios separadas) + unidades por uso (grid simple)."""
    w, h = huella * escala, huella * escala
    bloque = nucleo_info.get("bloque", {})
    bw = bloque.get("ancho_m", 6.0) * escala
    bl = bloque.get("largo_m", 9.0) * escala
    bx0 = w - bw - 4
    by0 = 4
    nuc_svg = ""
    for c in nucleo_info.get("disposicion", []):
        if c["tipo"] == "circulacion":
            fill, st = "#555555", "#222"
        else:
            fill, st = "#999999", "#444"
        cx = bx0 + bw / 2.0 + c["dx"] * escala
        cy = by0 + bl / 2.0 + c["dy"] * escala
        cw = c["ancho_m"] * escala
        ch = c["largo_m"] * escala
        nuc_svg += (f"<rect x='{cx - cw / 2:.1f}' y='{cy - ch / 2:.1f}' "
                    f"width='{cw:.1f}' height='{ch:.1f}' fill='{fill}' stroke='{st}' "
                    f"stroke-width='1'/>")
    # Grid de unidades: una caja por uso dominante del nivel (representacion)
    filas = ""
    x, y = 0, 0
    for uso, n in unidades_uso.items():
        color = COLORES.get(uso, "#CCCCCC")
        filas += (f"<rect x='{x + 4}' y='{y + 4}' width='{w - bw - 12}' "
                  f"height='{max(24, (h - bl - 8) / max(1, n) - 6)}' fill='{color}' "
                  f"stroke='#333' stroke-width='1'/><text x='{x + 10}' y='{y + 22}' "
                  f"font-size='11'>{uso} ({n})</text>")
    return f"""<svg viewBox="0 0 {w} {h}" style="width:100%;max-width:420px">
<rect x='0' y='0' width='{w}' height='{h}' fill='#FAFAFA' stroke='#333' stroke-width='2'/>
<rect x='{bx0}' y='{by0}' width='{bw:.1f}' height='{bl:.1f}' fill='#EDEDED' stroke='#222' stroke-width='2'/>
{nuc_svg}
<text x='{bx0 + 6}' y='{by0 + bl + 12}' fill='#555' font-size='10'>NUCLEO {nv}</text>
{filas}
<text x='6' y='{h - 6}' font-size='10' fill='#666'>Losa {huella:.0f} m² · núcleo {nucleo_info.get('hueco_m2_piso', nucleo_info.get('total_m2_piso', 0)):.0f} m² (circ {nucleo_info.get('circulacion_m2', 0):.0f} + serv {nucleo_info.get('servicios_m2', 0):.0f}) · {usos_nv}</text>
</svg>"""


def generar_html(caso_id, prog, matriz, layout):
    planos = ""
    for nv in layout["niveles"]:
        unidades = {u: 0 for u in nv["usos"]}
        for c in prog["componentes"]:
            if c["uso"] in nv["usos"]:
                unidades[c["uso"]] = unidades.get(c["uso"], 0) + c["num_unidades"]
        planos += (f"<h4>Nivel {nv['nivel']} — {', '.join(nv['usos'])}</h4>"
                   f"<p class='mini'>GFA {nv['gfa_m2']:.0f} m² · núcleo {nv['nucleo_m2']:.0f} m² (hueco, circ {layout['nucleos']['circulacion_m2']:.0f} + serv {layout['nucleos']['servicios_m2']:.0f}) · "
                   f"eficiencia {nv['eficiencia_losa_pct']:.0f}% · altura {nv['altura_m']:.1f} m</p>"
                   f"{plano_nivel_svg(nv['nivel'], layout['huella_m2'], layout['nucleos'], nv['usos'], unidades)}")
    filas_matriz = ""
    for a in matriz["usos"]:
        filas_matriz += "<tr><td><b>" + a + "</b></td>" + "".join(
            f"<td class='num'>{matriz['matriz'][a][b]}</td>" for b in matriz["usos"]) + "</tr>"
    cab = "".join(f"<th>{u}</th>" for u in matriz["usos"])
    just = "".join(f"<li><b>{k.replace('|', ' ↔ ')}</b> ({matriz['escala'][str(v['nivel'])]}): {v['razon']}</li>"
                   for k, v in matriz["justificaciones"].items() if v["nivel"] in (2, 3))
    nuc = layout["nucleos"]
    return f"""<!DOCTYPE html><html lang="es"><head><meta charset="utf-8">
<title>F3 — Distribución {caso_id} ({prog['escenario']})</title>
<style>body{{font-family:Segoe UI,Arial,sans-serif;margin:0;background:#F4F6F8;color:#223}}
.wrap{{max-width:960px;margin:auto;padding:24px}}h1{{font-size:22px}}
h3{{margin-top:28px;border-bottom:2px solid #1F3A5F;padding-bottom:4px}}
.mini{{font-size:12px;color:#555}}table{{border-collapse:collapse;width:100%;font-size:13px}}
th,td{{border:1px solid #ccc;padding:5px 8px;text-align:left}}th{{background:#1F3A5F;color:#fff}}
.num{{text-align:center}}.leyenda span{{display:inline-block;padding:2px 8px;margin:2px;border-radius:4px;font-size:11px}}
.badge{{background:#1F3A5F;color:#fff;padding:2px 10px;border-radius:12px;font-size:12px}}</style></head>
<body><div class="wrap">
<h1>F3 — Distribución espacial <span class="badge">{_titulo(caso_id)}</span></h1>
<p class="mini">Escenario {prog['escenario']} · GFA {prog['gfa_total']:.0f} m² · lote {prog['lote_m2']:.0f} m² ·
huella {layout['huella_m2']:.0f} m² · {layout['niveles_total']} niveles · población est. {layout['poblacion_estimada']['total']}</p>
<h3>1. Programa</h3>
<table><tr><th>Uso</th><th>% GFA</th><th>GFA (m²)</th><th>Unid.</th><th>Unidad (m²)</th><th>Vendible (m²)</th></tr>
{''.join(f"<tr><td>{c['uso']}</td><td class='num'>{c['pct_gfa']*100:.0f}%</td><td class='num'>{c['gfa_m2']:.0f}</td>"
         f"<td class='num'>{c['num_unidades']}</td><td class='num'>{c['unidad_m2']:.0f}</td>"
         f"<td class='num'>{c['area_vendible_m2']:.0f}</td></tr>" for c in prog['componentes'])}</table>
<h3>2. Matriz de adyacencias</h3>
<p class="mini">3 Requerida · 2 Deseable · 1 Indiferente · 0 Incompatible</p>
<table><tr><th></th>{cab}</tr>{filas_matriz}</table>
<h3>Justificaciones (requeridas y deseables)</h3><ul>{just}</ul>
<h3>3. Núcleos de servicios y transporte vertical</h3>
<table><tr><th>Componente</th><th>Cant.</th><th>Detalle</th></tr>
<tr><td>Escaleras</td><td class='num'>{nuc['escaleras']['cantidad']}</td><td>{nuc['escaleras']['tipo']}</td></tr>
<tr><td>Ascensores</td><td class='num'>{nuc['ascensores']['cantidad']}</td><td>{nuc['ascensores']['criterio']}</td></tr>
<tr><td>Servicios</td><td class='num'>—</td><td>ductos, basuras y cuarto técnico: 8 m²/piso</td></tr>
<tr><td><b>Total núcleo</b></td><td class='num'>—</td><td><b>{nuc['total_m2_piso']:.0f} m²/piso</b> ({(nuc['total_m2_piso']/layout['huella_m2'])*100:.0f}% de la losa)</td></tr>
</table>
<h3>4. Planos esquemáticos por nivel</h3>
<div class="leyenda">{''.join(f"<span style='background:{c};color:#222'>{u}</span>" for u, c in COLORES.items() if u != 'Circulacion')}</div>
{planos}
</div></body></html>"""


# ------------------------------------------------------------------ masa 3D
def _caja_brep(x0, y0, z0, x1, y1, z1):
    """Brep de caja ortogonal con rhino3dm (Box solo acepta BoundingBox en 8.x)."""
    bb = rhino3dm.BoundingBox(rhino3dm.Point3d(x0, y0, z0), rhino3dm.Point3d(x1, y1, z1))
    return rhino3dm.Brep.CreateFromBox(rhino3dm.Box(bb))


def exportar_3dm(caso_id, prog, layout, ruta):
    if not _HAY_RHINO:
        print("  [3dm] rhino3dm no disponible; se omite la masa 3D")
        return
    model = rhino3dm.File3dm()
    z = 0.0
    lado = math.sqrt(layout["huella_m2"])
    for nv in layout["niveles"]:
        h = nv["altura_m"]
        br = _caja_brep(0, 0, z, lado, lado, z + h)
        layer = rhino3dm.Layer()
        layer.Name = f"N{nv['nivel']}"
        idx = model.Layers.Add(layer)
        attr = rhino3dm.ObjectAttributes()
        attr.LayerIndex = idx
        model.Objects.AddBrep(br, attr)
        z += h
    # Nucleo vertical (franja central)
    nl = math.sqrt(layout["nucleos"]["total_m2_piso"])
    br_n = _caja_brep(lado - nl, 0, 0, lado, lado, z)
    layer_n = rhino3dm.Layer()
    layer_n.Name = "NUCLEO"
    idx_n = model.Layers.Add(layer_n)
    attr_n = rhino3dm.ObjectAttributes()
    attr_n.LayerIndex = idx_n
    model.Objects.AddBrep(br_n, attr_n)
    model.Write(ruta)
    print(f"  [3dm] {ruta}")


# ------------------------------------------------------------------ programa-areas
# Esquema compatible con VOLUM_GENERADOR_v04/v05 (GH): programa_pisos + matriz.
# Balanceado: la suma de areas brutas por piso = GFA real del layout (a diferencia
# del F3_PROGRAMA_AREAS_v01 original, que solo construia ~36% del GFA).
EFICIENCIA_POR_USO = {"Vivienda": 0.78, "Local comercial": 0.85, "Consultorios": 0.75,
                     "Oficinas": 0.80, "Institucional salud": 0.75,
                     "Hogar geriatrico": 0.80}
# Proyeccion de la matriz 0-3 a la escala -1/0/1 del VOLUM_GENERADOR_v04
ESCALA_V04 = {0: -1, 1: 0, 2: 1, 3: 1}
USOS_V04 = {"Vivienda": "Vivienda", "Local comercial": "Comercio",
            "Consultorios": "Salud", "Oficinas": "Comercio",
            "Institucional salud": "Salud", "Hogar geriatrico": "Salud"}


def exportar_programa_areas(carpeta, prog, layout, matriz, bloques=None):
    """Escribe programa-areas.json (esquema VOLUM_GENERADOR_v04/v05) balanceado.
    v02: adjunta el resumen de bloques (multivolumen) si viene."""
    # Peso de cada uso en el programa (por area bruta total)
    peso = {c["uso"]: c["gfa_m2"] for c in prog["componentes"]}
    tot_peso = sum(peso.values()) or 1.0
    # Area neta por uso segun eficiencia real del componente
    efic = {c["uso"]: c.get("eficiencia", EFICIENCIA_POR_USO.get(c["uso"], 0.8))
            for c in prog["componentes"]}
    programa = []
    for nv in layout["niveles"]:
        usos = []
        resto = nv["gfa_m2"] - nv["nucleo_m2"]
        # Pesos normalizados dentro del nivel (suma de usos = resto exacto)
        pesos_nv = {u: peso.get(u, 0) for u in nv["usos"]}
        tot_nv = sum(pesos_nv.values()) or 1.0
        for u in nv["usos"]:
            area = round(resto * pesos_nv[u] / tot_nv, 2)
            usos.append({"uso": u, "area_bruta": area,
                         "area_neta": round(area * efic.get(u, 0.8), 2)})
        usos.append({"uso": "Nucleo", "area_bruta": round(nv["nucleo_m2"], 2),
                     "area_neta": round(nv["nucleo_m2"], 2)})
        programa.append({"piso": nv["nivel"], "altura_z": nv.get("z_base_m", 0.0),
                         "altura_piso": nv["altura_m"], "usos": usos})
    # Matriz en escala v04 (-1/0/1) con categorias v04: el valor entre categorias
    # es el maximo sobre los usos originales que mapean a cada categoria.
    usos_v04 = sorted({USOS_V04.get(u, u) for u in matriz["usos"]})
    orig = {c: [u for u in matriz["usos"] if USOS_V04.get(u, u) == c] for c in usos_v04}
    matriz_v04 = {}
    for a in usos_v04:
        matriz_v04[a] = {}
        for b in usos_v04:
            vals = [ESCALA_V04.get(matriz["matriz"][ua][ub], 0)
                    for ua in orig[a] for ub in orig[b]]
            matriz_v04[a][b] = max(vals) if vals else 0
    doc = {
        "gfa_total": round(prog["gfa_total"], 2),
        "pisos": layout["niveles_total"],
        "area_por_piso": round(layout["huella_m2"], 2),
        "programa_pisos": programa,
        "matriz_adyacencia": matriz_v04,
        "nucleo": {"total_m2_piso": round(layout["nucleos"]["total_m2_piso"], 2),
                    "hueco_m2_piso": round(layout["nucleos"]["hueco_m2_piso"], 2),
                    "circulacion_m2": round(layout["nucleos"]["circulacion_m2"], 2),
                    "servicios_m2": round(layout["nucleos"]["servicios_m2"], 2),
                    "bloque": layout["nucleos"]["bloque"],
                    "disposicion": layout["nucleos"]["disposicion"],
                    "lado_m": round(math.sqrt(layout["nucleos"]["total_m2_piso"]), 2),
                    "escaleras": layout["nucleos"]["escaleras"],
                    "ascensores": layout["nucleos"]["ascensores"]},
        "origen": "F3_DISTRIBUCION_v02 (balanceado; nucleo circulacion/servicios separados)",
    }
    if bloques:
        doc["bloques"] = {"n": bloques.get("n"), "distribucion": bloques.get("distribucion"),
                          "separacion_m": bloques.get("separacion_m"),
                          "desnivel_m": bloques.get("desnivel_m"),
                          "orientacion": (bloques.get("orientacion") or {}).get("franja_descripcion"),
                          "niveles_modo": (bloques.get("niveles") or {}).get("modo"),
                          "resumen": [{"id": b["id"], "pisos": b["pisos"],
                                       "z_base_m": b["z_base_m"],
                                       "area_lote_m2": b["area_lote_m2"]}
                                      for b in (bloques.get("bloques") or [])]}
    with io.open(os.path.join(carpeta, "programa-areas.json"), "w",
                 encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False, indent=2)
    return doc


# ------------------------------------------------------------------ main
def _computar(args):
    """v02.1: calcula programa/layout/bloques sin escribir archivos.

    En modo --json el stdout lo captura main() para que la unica salida sea el
    JSON (lo consume el orquestador en /api/proponer-bloques)."""
    if args.chip:
        prog = leer_programa_chip(args.chip, args.escenario)
        carpeta_id = args.chip
    else:
        caso_id = args.caso_id or "A"
        if caso_id not in CASOS:
            raise ValueError("CASO_ID invalido: {} | opciones: {}".format(caso_id, list(CASOS)))
        prog = leer_programa(caso_id)
        carpeta_id = caso_id

    usos_sel = None
    if getattr(args, "usos", None):
        usos_sel = [u.strip() for u in args.usos.split(",") if u.strip()]
    prog, aviso_usos = filtrar_usos_programa(prog, usos_sel)
    if aviso_usos:
        print("  [usos]", aviso_usos)

    huella, niveles, niveles_uso = distribuir_niveles(prog)
    usos = sorted(set(c["uso"] for c in prog["componentes"]))
    matriz = matriz_adyacencias(usos)
    layout = layout_espacial(prog, huella, niveles, niveles_uso)

    # v02.1: desnivel 'auto' (topografia) o manual (m); --bloques-desnivel-m gana si viene
    desn_str = (args.bloques_desnivel or "").strip().lower()
    if args.bloques_desnivel_m is not None:
        desn_auto, desn_man = False, float(args.bloques_desnivel_m)
    elif desn_str in ("", "auto"):
        desn_auto, desn_man = True, None
    else:
        desn_auto, desn_man = False, float(desn_str)

    bloques = generar_bloques(carpeta_id, prog, huella, niveles, {
        "n": args.bloques,
        "distribucion": args.bloques_distribucion,
        "lindero": args.bloques_lindero,
        "angulo_ref": args.bloques_angulo_ref,
        "angulo_grados": args.bloques_angulo_grados,
        "separacion_m": args.bloques_separacion_m,
        "desnivel_auto": desn_auto,
        "desnivel_m": desn_man,
        "azimut_grados": args.bloques_azimut,
    }, layout=layout)
    return {"carpeta_id": carpeta_id, "prog": prog, "matriz": matriz,
            "huella": huella, "niveles": niveles, "layout": layout, "bloques": bloques}


def main():
    parser = argparse.ArgumentParser(description="F3 distribución espacial (masa)")
    parser.add_argument("caso_id", nargs="?", default=None,
                        help="Caso pre-generado: A | B | B_SALUD | C")
    parser.add_argument("--chip", default=None,
                        help="CHIP del lote (genera el caso desde resultados F2)")
    parser.add_argument("--escenario", default="D_MIXTO",
                        help="Escenario F2 a distribuir (default D_MIXTO)")
    parser.add_argument("--usos", default=None,
                        help="Usos de la seccion 2 (separados por coma); filtra el mix")
    parser.add_argument("--bloques", type=int, default=1,
                        help="Numero de bloques del multivolumen (1-6; default 1)")
    parser.add_argument("--bloques-distribucion", default="automatico",
                        choices=["automatico", "paralelo_calle_acceso",
                                 "perpendicular_calle_acceso", "paralelo_lindero",
                                 "angulo", "longitudinal", "transversal"],
                        help="Orientacion del reparto (default automatico: franjas "
                             "paralelas a la calle de acceso del predio)")
    parser.add_argument("--bloques-lindero", default=None,
                        help="Cardinal del lindero de referencia (Norte|Sur|Oriente|Occidente)")
    parser.add_argument("--bloques-angulo-ref", default="calle_acceso",
                        choices=["norte", "calle_acceso", "lindero"],
                        help="Referencia del angulo manual (default calle_acceso)")
    parser.add_argument("--bloques-angulo-grados", type=float, default=0.0,
                        help="Angulo del reparto en grados horarios respecto a la referencia")
    parser.add_argument("--bloques-separacion-m", type=float, default=6.0,
                        help="Separacion entre bloques en m (min normativo 6.0)")
    parser.add_argument("--bloques-desnivel", default="auto",
                        help="'auto' (default): propone niveles desde la topografia "
                             "(B1 = 0.00 en la calle de acceso -> BN en el nivel final); "
                             "o un numero = paso manual en m entre bloques")
    parser.add_argument("--bloques-desnivel-m", type=float, default=None,
                        help="(compat v02) paso manual entre bloques en m; gana sobre "
                             "--bloques-desnivel si se indica")
    parser.add_argument("--bloques-azimut", type=float, default=None,
                        help="(compat v02) angulo LOCAL del reparto en grados")
    parser.add_argument("--dry-run", action="store_true",
                        help="No escribe archivos; solo calcula e imprime el resumen")
    parser.add_argument("--json", action="store_true",
                        help="Imprime SOLO el resumen JSON (impli-cito: --dry-run)")
    args = parser.parse_args()
    if args.json:
        args.dry_run = True

    _out_real = sys.stdout
    if args.json:
        sys.stdout = io.StringIO()
    error = None
    r = None
    try:
        try:
            r = _computar(args)
        except ValueError as ex:
            error = str(ex)
    finally:
        if args.json:
            sys.stdout = _out_real
    if error:
        print("ERROR: " + error, file=sys.stderr)
        sys.exit(2)

    prog, layout, matriz = r["prog"], r["layout"], r["matriz"]
    bloques, huella, niveles = r["bloques"], r["huella"], r["niveles"]
    carpeta_id = r["carpeta_id"]

    if not args.dry_run:
        os.makedirs(OUT, exist_ok=True)
        carpeta = os.path.join(OUT, carpeta_id)
        os.makedirs(carpeta, exist_ok=True)
        with io.open(os.path.join(carpeta, "bloques.json"), "w", encoding="utf-8") as f:
            json.dump(bloques, f, ensure_ascii=False, indent=2)
        for nombre, obj in (("programa.json", prog), ("matriz_adyacencias.json", matriz),
                            ("layout_espacial.json", layout)):
            with io.open(os.path.join(carpeta, nombre), "w", encoding="utf-8") as f:
                json.dump(obj, f, ensure_ascii=False, indent=2)
        pa = exportar_programa_areas(carpeta, prog, layout, matriz, bloques)
        print("  [programa-areas.json] balance:",
              round(sum(p["usos"][0]["area_bruta"] for p in pa["programa_pisos"]) + 0, 1),
              "(huella por piso)")
        html = generar_html(carpeta_id, prog, matriz, layout)
        with io.open(os.path.join(carpeta, f"planos_{carpeta_id}.html"), "w", encoding="utf-8") as f:
            f.write(html)
        exportar_3dm(carpeta_id, prog, layout, os.path.join(carpeta, f"F3_{carpeta_id}.3dm"))

    if args.json:
        print(json.dumps({"ok": True, "chip": carpeta_id, "escenario": args.escenario,
                          "bloques": bloques}, ensure_ascii=False))
        return

    if bloques.get("n", 1) > 1:
        ni = bloques.get("niveles") or {}
        if ni.get("modo") == "auto":
            nivel_txt = "niveles auto: B1 0.00 -> B{} {:+.2f} m (paso {:.2f})".format(
                bloques["n"], ni.get("delta_m") or 0.0, ni.get("desnivel_m") or 0.0)
        else:
            nivel_txt = "paso manual {:.2f} m".format(bloques.get("desnivel_m") or 0.0)
        print("  [bloques] {} bloques | sep {:.2f} m | {} | {}".format(
            bloques["n"], bloques.get("separacion_m") or 0.0, nivel_txt,
            (bloques.get("orientacion") or {}).get("franja_descripcion", "")))
        for a in bloques.get("avisos") or []:
            print("  [bloques][aviso]", a)
    print(f"OK {carpeta_id}: {niveles} niveles, huella {huella:.0f} m², "
          f"ascensores {layout['nucleos']['ascensores']['cantidad']}, "
          f"nucleo {layout['nucleos']['total_m2_piso']:.0f} m²/piso")


if __name__ == "__main__":
    main()
