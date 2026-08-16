# -*- coding: utf-8 -*-
"""
================================================================================
F3_DISTRIBUCION_v01.py — Distribucion espacial del USO-MULTIPLE (Fase 3, 1a parte)
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
  python F3_DISTRIBUCION_v01.py <CASO_ID> [--gfa <m2>] [--lote <m2>] [--niveles N]
  CASO_ID: A | B | C | B_SALUD   (lee el D_MIXTO del JSON de resultados de F2)

SALIDAS en src/fase-3-masa/casos/<id>/ :
  programa.json, matriz_adyacencias.json, layout_espacial.json,
  planos_<id>.html, F3_<id>.3dm
================================================================================
"""
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
    if "local" in u:
        return "Local comercial"
    if "consultorio" in u:
        return "Consultorios"
    if "oficina" in u:
        return "Oficinas"
    if "institucional" in u or "ips" in u or "laboratorio" in u:
        return "Institucional salud"
    if "geriatrico" in u:
        return "Hogar geriatrico"
    return u


# ------------------------------------------------------------------ casos F2
CASOS = {
    "A": {"resultados": "resultados_AAA0127AZPA_gfa1461_cl800.json", "gfa": 1461.0972,
          "lote_m2": 315.0, "huella_m2": 243.5162, "escenario": "D_MIXTO",
          "titulo": "A - El Prado (Suba) - envolvente F1 v06"},
    "B": {"resultados": "resultados_AAA0030JKOE.json", "gfa": 3312.575,
          "lote_m2": 931.0, "escenario": "D_MIXTO", "titulo": "B — La Candelaria"},
    "B_SALUD": {"resultados": "resultados_AAA0030JKOE.json", "gfa": 3312.575,
                "lote_m2": 931.0, "escenario": "D_MIXTO_SALUD",
                "titulo": "B — La Candelaria (variante salud)"},
    "C": {"resultados": "resultados_AAA0039KRMR.json", "gfa": 1100.0,
          "lote_m2": 356.96, "escenario": "D_MIXTO", "titulo": "C — Muzú (Puente Aranda)"},
}


def leer_programa(caso_id):
    cfg = CASOS[caso_id]
    with io.open(os.path.join(FIN, cfg["resultados"]), encoding="utf-8") as f:
        paquete = json.load(f)
    esc = next(x for x in paquete["escenarios"] if x["escenario_id"] == cfg["escenario"])
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
    return {"gfa_total": cfg["gfa"], "lote_m2": cfg["lote_m2"],
            "huella_m2": cfg.get("huella_m2"),
            "escenario": cfg["escenario"], "componentes": comps}


def distribuir_niveles(prog):
    """Huella = ocupacion x lote (o huella_m2 real de Fase 1 si viene en el caso);
    niveles = ceil(GFA/huella); reparto de usos."""
    huella = prog.get("huella_m2") or round(prog["lote_m2"] * OCUPACION_POT, 1)
    # tolerancia 1e-9: un cociente exactamente entero (p. ej. 6 losas de 243,5162 m2)
    # no debe redondear al piso siguiente por error de punto flotante
    niveles = max(2, math.ceil(prog["gfa_total"] / huella - 1e-9))
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
<h1>F3 — Distribución espacial <span class="badge">{CASOS[caso_id]['titulo']}</span></h1>
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


def exportar_programa_areas(carpeta, prog, layout, matriz):
    """Escribe programa-areas.json (esquema VOLUM_GENERADOR_v04/v05) balanceado."""
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
        "origen": "F3_DISTRIBUCION_v01 (balanceado; nucleo circulacion/servicios separados)",
    }
    with io.open(os.path.join(carpeta, "programa-areas.json"), "w",
                 encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False, indent=2)
    return doc


# ------------------------------------------------------------------ main
def main():
    caso_id = sys.argv[1] if len(sys.argv) > 1 else "A"
    if caso_id not in CASOS:
        print("CASO_ID invalido:", caso_id, "| opciones:", list(CASOS))
        return
    os.makedirs(OUT, exist_ok=True)
    carpeta = os.path.join(OUT, caso_id)
    os.makedirs(carpeta, exist_ok=True)

    prog = leer_programa(caso_id)
    huella, niveles, niveles_uso = distribuir_niveles(prog)
    usos = sorted(set(c["uso"] for c in prog["componentes"]))
    matriz = matriz_adyacencias(usos)
    layout = layout_espacial(prog, huella, niveles, niveles_uso)

    for nombre, obj in (("programa.json", prog), ("matriz_adyacencias.json", matriz),
                        ("layout_espacial.json", layout)):
        with io.open(os.path.join(carpeta, nombre), "w", encoding="utf-8") as f:
            json.dump(obj, f, ensure_ascii=False, indent=2)

    pa = exportar_programa_areas(carpeta, prog, layout, matriz)
    print("  [programa-areas.json] balance:",
          round(sum(p["usos"][0]["area_bruta"] for p in pa["programa_pisos"]) + 0, 1),
          "(huella por piso)")

    html = generar_html(caso_id, prog, matriz, layout)
    with io.open(os.path.join(carpeta, f"planos_{caso_id}.html"), "w", encoding="utf-8") as f:
        f.write(html)

    exportar_3dm(caso_id, prog, layout, os.path.join(carpeta, f"F3_{caso_id}.3dm"))
    print(f"OK {caso_id}: {niveles} niveles, huella {huella:.0f} m², "
          f"ascensores {layout['nucleos']['ascensores']['cantidad']}, "
          f"nucleo {layout['nucleos']['total_m2_piso']:.0f} m²/piso")


if __name__ == "__main__":
    main()
