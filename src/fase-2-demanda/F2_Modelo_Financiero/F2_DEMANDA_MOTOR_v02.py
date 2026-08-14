# -*- coding: utf-8 -*-
"""
================================================================================
F2_DEMANDA_MOTOR_v02.py — Modelo Financiero Inmobiliario de Prefactibilidad (Fase 2)
Proyecto: Catalogo / DiseñoParametrico — Fase 2
Python 3.8+ Standalone (sin dependencias externas)
================================================================================

OBJETIVO:
  Determinar el producto inmobiliario optimo (tipologia, nivel de acabados,
  numero de unidades) que maximiza la rentabilidad del lote, respetando la
  envolvente normativa (GFA maximo de Fase 1), evaluando 3 escenarios para el
  mismo GFA: A (VIS/VIP), B (Estandar) y C (Lujo).

ALCANCE (prefactibilidad):
  - Un solo ciclo de desarrollo (~2 anos), flujo de caja estatico, sin
    financiacion, sin TIR/VPN (reservados para Fase 3).
  - No redefine el GFA maximo (dato de entrada de Fase 1).
  - No emite concepto legal, urbanistico o de uso de suelo.

USO:
  python F2_DEMANDA_MOTOR_v02.py
  python F2_DEMANDA_MOTOR_v02.py --parametros parametros_entrada.json
  python F2_DEMANDA_MOTOR_v02.py --parametros parametros_entrada.json --chip AAA0127AZPA

SALIDAS (carpeta resultados/):
  - resultados_completos.json   : todos los calculos (auditable)
  - comparativo_escenarios.csv  : tabla comparativa de KPIs
  - sensibilidad.csv            : analisis de sensibilidad +-10%
  - informe_F2_prefactibilidad.html : informe ejecutivo autocontenido

ESTRUCTURA DE CALCULO (prefactibilidad estatica):
  NGA        = GFA * eficiencia_NTG (por escenario)
  Unidades   = floor(NGA / tamano_unidad); area_vendible = unidades * tamano
  Ingresos   = area_vendible * precio_venta_m2
  CostoDuro  = GFA * costo_construccion_m2
  CostosBlandos = 13% del CostoDuro (rango 12-15%)
  Marketing  = 3,5% de los Ingresos (rango 3-4%)
  CostoLote  = area_lote * precio_suelo_m2 * (1 + impuestos 4%)
  CTD        = CostoLote + CostoDuro + CostosBlandos + Marketing
  UB         = Ingresos - CTD
  MUB        = UB / Ingresos * 100        (regla: <18% alto riesgo, >25% atractivo)
  ROI        = UB / CTD * 100             (regla: minimo 22%)
  CL/IT      = CostoLote / Ingresos * 100 (regla: >25-30% inviable, evaluar arriendo)

SENSIBILIDAD +-10% (unidades continuas, efecto marginal):
  Variables: precio de venta, costo duro, eficiencia NGA, costo del lote, absorcion.
  El ranking de prioridad de fetch combina el impacto medido con el rango
  plausible de variacion y la controlabilidad de cada variable.

FUENTES DE MERCADO (consultadas 2026-08-12):
  - SMMLV 2026 = $1.750.905 (Decreto 1469/2025, ratificado Decreto 0159/2026)
  - Tope VIS 2026 = 135 SMMLV = $236.372.175
  - Precio venta Bogota 2026: Terraes ~$6,0 M/m2 (50% mercado $4,5-7,9 M/m2);
    Ciencuadras Q1-2026 $7,42 M/m2 apartamentos; premium >$11 M/m2
    (Metrocuadrado: La Cabrera/El Retiro).
  - Costo construccion Bogota 2026: obra gris desde ~$1,3 M/m2; terminada con
    acabados medios $2,2-3,5 M/m2 (Konstruing, 07-ago-2026); rango general
    $2,2-3,8 M/m2 (Aliados de Obras 2026); CAMACOL proyecta +15% costos 2026.
  - Suelo: referencia Catastro Distrital (Visor Inmobiliario Bogota-Region) e
    IDECA (mediana valor comercial m2 de terreno); supuesto de referencia.
  Cada parametro lleva su fuente y URL dentro de parametros_entrada.json.
================================================================================
"""

import argparse
import csv
import json
import os
import sys
from datetime import date

# ----------------------------------------------------------------------------
# Utilidades de formato
# ----------------------------------------------------------------------------

def _fmt_cop(valor: float) -> str:
    """Formatea COP con separadores de miles y sin decimales."""
    return f"{round(valor):,}".replace(",", ".")

def _fmt_m(valor: float, dec: int = 1) -> str:
    """Formatea en millones de COP con 1 decimal."""
    return f"{valor / 1e6:,.{dec}f}".replace(",", ".")

def _fmt_pct(valor: float, dec: int = 1) -> str:
    return f"{valor:.{dec}f}"

def _h(texto: str) -> str:
    """Escapa texto para HTML."""
    return (str(texto)
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;"))

# ----------------------------------------------------------------------------
# Carga de parametros
# ----------------------------------------------------------------------------

_DEFAULT_PARAMS = {
    "gfa_max_m2": 1200.0,
    "lote": {"area_m2": 450.0, "precio_suelo_m2": 2600000.0,
             "impuestos_escritura_pct": 4.0},
    "financiero": {"costos_blandos_pct": 13.0, "marketing_ventas_pct": 3.5},
    "reglas_decision": {"mub_riesgo_pct": 18.0, "mub_atractivo_pct": 25.0,
                        "roi_minimo_pct": 22.0, "cl_it_precaucion_pct": 25.0,
                        "cl_it_inviable_pct": 30.0},
    "sensibilidad": {"variacion_pct": 10.0},
    "flujo_caja": {
        "trimestres": 8,
        "nota": "Programa de flujo de caja por trimestre (0-7 = 24 meses). Cada lista suma 100%. "
                 "Ingresos: 20% preventa (t1-2), 40% durante obra (t3-6), 40% entrega (t7). "
                 "CD: 30% t1-2, 40% t3-4, 30% t5-6. CB: 25% por trimestre t0-3. CMV sigue a los ingresos.",
        "ingresos_pct": [0, 10, 10, 10, 10, 10, 10, 40],
        "cd_pct": [0, 15, 15, 20, 20, 15, 15, 0],
        "cb_pct": [25, 25, 25, 25, 0, 0, 0, 0],
        "cmv_pct": None,
        "cl_pct": [100, 0, 0, 0, 0, 0, 0, 0],
        "reparto_dueno_trimestre": 7
    },
    "aporte_suelo": {
        "nota": "Escenario D: el dueno del lote lo aporta al proyecto y participa en las utilidades finales "
                 "(no recibe el precio de venta por adelantado). Se calcula la ventana de negociacion: "
                 "pct maximo que deja ROI del desarrollador >= minimo, y pct minimo para que el dueno "
                 "reciba al menos el valor del suelo soportable por el mercado (CL que daria ROI 22%).",
        "pct_socio": None,
        "renta_anual_dueno_pct": 8.0
    },
    "arriendo_lote": {
        "nota": "Escenario E: el lote se arrienda durante el ciclo (24 meses) en lugar de comprarse. "
                 "El canon mensual se expresa como % del valor del lote; se evalua sobre el precio "
                 "pedido y sobre el valor soportable por el mercado.",
        "mensual_pct_cl": 0.75,
        "meses": 24
    },
    "escenarios": {},
}


def cargar_parametros(ruta: str) -> dict:
    """Carga parametros desde JSON; completa con valores por defecto."""
    with open(ruta, "r", encoding="utf-8") as f:
        data = json.load(f)
    params = dict(_DEFAULT_PARAMS)
    params.update(data)
    params.setdefault("meta", {})
    return params


def costo_lote_total(lote_cfg: dict) -> float:
    """CL = area * precio_m2 * (1 + impuestos_pct/100).
    Si el config trae 'costo_lote_total_cop', se usa directo (compatibilidad con
    el pipeline original, donde --costo-lote era el CL total incluido impuestos)."""
    if lote_cfg.get("costo_lote_total_cop"):
        return float(lote_cfg["costo_lote_total_cop"])
    imp = lote_cfg.get("impuestos_escritura_pct", 4.0) / 100.0
    return lote_cfg["area_m2"] * lote_cfg["precio_suelo_m2"] * (1.0 + imp)


# ----------------------------------------------------------------------------
# Motor de escenario (caso base: unidades enteras vendibles)
# ----------------------------------------------------------------------------

def run_scenario(gfa: float, cl: float, esc: dict, fin: dict) -> dict:
    """
    Calcula KPIs de un escenario con unidades enteras (floor).
    Mantiene la logica del v01 original (area vendible real = unidades * tamano).
    Si el escenario trae 'mix_usos' (override de uso multiple), el GFA se reparte
    por componente (pct_gfa) con precio/costo/eficiencia propios de cada uso y los
    KPIs se agregan (IT, CD, unidades, area vendible).
    """
    mix_detalle = None
    if esc.get("mix_usos"):
        nga = 0.0
        unidades = 0
        area_vendible = 0.0
        ingresos = 0.0
        costo_duro = 0.0
        absorcion_pond = 0.0
        comps = []
        for m in esc["mix_usos"]:
            gfa_i = gfa * m["pct_gfa"]
            nga_i = gfa_i * m["eficiencia_nga"]
            unid = int(nga_i // m["unidad_m2"])
            area_i = unid * m["unidad_m2"]
            it_i = area_i * m["precio_venta_m2"]
            cd_i = gfa_i * m["costo_construccion_m2"]
            nga += nga_i
            unidades += unid
            area_vendible += area_i
            ingresos += it_i
            costo_duro += cd_i
            absorcion_pond += unid / max(m.get("absorcion_unid_mes", 2.0), 0.1)
            comps.append({
                "uso": m.get("uso", "?"),
                "pct_gfa": m["pct_gfa"],
                "gfa_i": round(gfa_i, 2),
                "nga_i": round(nga_i, 2),
                "num_unidades": unid,
                "area_vendible_m2": round(area_i, 2),
                "precio_venta_m2": m["precio_venta_m2"],
                "costo_construccion_m2": m["costo_construccion_m2"],
                "ingresos_cop": round(it_i, 2),
            })
        mix_detalle = comps
        absorcion = unidades / absorcion_pond if absorcion_pond > 0 else 0.0
        tamano_prom = area_vendible / unidades if unidades > 0 else 0.0
        precio_prom = ingresos / area_vendible if area_vendible > 0 else 0.0
        costo_prom = costo_duro / gfa if gfa > 0 else 0.0
    else:
        nga = gfa * esc["eficiencia_nga"]
        unidades = int(nga // esc["unidad_m2"])
        area_vendible = unidades * esc["unidad_m2"]
        ingresos = area_vendible * esc["precio_venta_m2"]
        costo_duro = gfa * esc["costo_construccion_m2"]
        absorcion = esc.get("absorcion_unid_mes", 2.0)
        tamano_prom = esc["unidad_m2"]
        precio_prom = esc["precio_venta_m2"]
        costo_prom = esc["costo_construccion_m2"]

    costo_blando = costo_duro * fin["costos_blandos_pct"] / 100.0
    costo_mkt = ingresos * fin["marketing_ventas_pct"] / 100.0
    costo_total = cl + costo_duro + costo_blando + costo_mkt
    utilidad = ingresos - costo_total

    mub = (utilidad / ingresos * 100.0) if ingresos > 0 else 0.0
    roi = (utilidad / costo_total * 100.0) if costo_total > 0 else 0.0
    cl_it = (cl / ingresos * 100.0) if ingresos > 0 else 0.0

    meses_venta = (unidades / absorcion) if absorcion > 0 else float("inf")

    return {
        "escenario_id": esc.get("id", "?"),
        "producto": esc["nombre"],
        "nivel_acabados": esc.get("nivel_acabados", ""),
        "gfa_m2": round(gfa, 2),
        "nga_m2": round(nga, 2),
        "eficiencia_nga": esc.get("eficiencia_nga", 0.0),
        "tamano_unidad_m2": round(tamano_prom, 2),
        "num_unidades": unidades,
        "area_vendible_m2": round(area_vendible, 2),
        "precio_venta_m2": round(precio_prom, 2),
        "costo_construccion_m2": round(costo_prom, 2),
        "absorcion_unid_mes": round(absorcion, 2),
        "meses_venta_estimados": round(meses_venta, 1),
        "mix_usos_detalle": mix_detalle,
        "ingresos_totales_cop": round(ingresos, 2),
        "costo_lote_cop": round(cl, 2),
        "costo_duro_cop": round(costo_duro, 2),
        "costo_blando_cop": round(costo_blando, 2),
        "costo_mkt_cop": round(costo_mkt, 2),
        "costo_total_cop": round(costo_total, 2),
        "utilidad_bruta_cop": round(utilidad, 2),
        "MUB_pct": round(mub, 2),
        "ROI_pct": round(roi, 2),
        "CL_IT_pct": round(cl_it, 2),
        "fuente_precio": esc.get("fuente_precio", ""),
        "fuente_precio_url": esc.get("fuente_precio_url", ""),
        "fuente_costo": esc.get("fuente_costo", ""),
        "fuente_costo_url": esc.get("fuente_costo_url", ""),
        "nota": esc.get("nota", ""),
    }


# ----------------------------------------------------------------------------
# Alertas de viabilidad
# ----------------------------------------------------------------------------

def evaluar_alertas(res: dict, reglas: dict) -> list:
    """Evalua reglas de decision y devuelve lista de alertas textuales."""
    alertas = []
    mub = res["MUB_pct"]
    roi = res["ROI_pct"]
    cl_it = res["CL_IT_pct"]

    if mub < reglas["mub_riesgo_pct"]:
        alertas.append({"nivel": "critica",
                        "kpi": "MUB",
                        "texto": f"MUB {_fmt_pct(mub)}% < {reglas['mub_riesgo_pct']}%: "
                                 "margen bruto de alto riesgo en Bogota."})
    elif mub > reglas["mub_atractivo_pct"]:
        alertas.append({"nivel": "positiva",
                        "kpi": "MUB",
                        "texto": f"MUB {_fmt_pct(mub)}% > {reglas['mub_atractivo_pct']}%: margen atractivo."})

    if roi < reglas["roi_minimo_pct"]:
        alertas.append({"nivel": "critica",
                        "kpi": "ROI",
                        "texto": f"ROI {_fmt_pct(roi)}% < {reglas['roi_minimo_pct']}%: "
                                 "por debajo del minimo estandar para desarrollar."})

    if cl_it > reglas["cl_it_inviable_pct"]:
        alertas.append({"nivel": "critica",
                        "kpi": "CL/IT",
                        "texto": f"CL/IT {_fmt_pct(cl_it)}% > {reglas['cl_it_inviable_pct']}%: "
                                 "el suelo absorbe mas del 30% de los ingresos; "
                                 "proyecto no viable para desarrollo y venta (evaluar arrendar el lote)."})
    elif cl_it > reglas["cl_it_precaucion_pct"]:
        alertas.append({"nivel": "advertencia",
                        "kpi": "CL/IT",
                        "texto": f"CL/IT {_fmt_pct(cl_it)}% > {reglas['cl_it_precaucion_pct']}%: "
                                 "el suelo pesa sobre las ventas; revisar precio de compra."})

    if res["meses_venta_estimados"] > 24.0:
        alertas.append({"nivel": "advertencia",
                        "kpi": "Absorcion",
                        "texto": f"Absorcion: {res['meses_venta_estimados']} meses estimados de venta "
                                 "> 24 meses del ciclo; liquidez comprometida."})

    return alertas


# ----------------------------------------------------------------------------
# Sensibilidad +-10% (unidades continuas: efecto marginal)
# ----------------------------------------------------------------------------

def _ub_marginal(gfa: float, cl: float, esc: dict, fin: dict,
                 precio=None, costo=None, eficiencia=None) -> float:
    """UB con unidades continuas (sin redondeo) para sensibilidad marginal."""
    pv = esc["precio_venta_m2"] if precio is None else precio
    cd = esc["costo_construccion_m2"] if costo is None else costo
    ef = esc["eficiencia_nga"] if eficiencia is None else eficiencia
    nga = gfa * ef
    area = nga  # unidades continuas
    ingresos = area * pv
    costo_duro = gfa * cd
    costo_blando = costo_duro * fin["costos_blandos_pct"] / 100.0
    costo_mkt = ingresos * fin["marketing_ventas_pct"] / 100.0
    costo_total = cl + costo_duro + costo_blando + costo_mkt
    return ingresos - costo_total


def analizar_sensibilidad(gfa: float, cl: float, escenarios: dict, fin: dict,
                          variacion_pct: float) -> dict:
    """
    Cuantifica el impacto de +-10% de cada variable sobre la utilidad bruta.
    Devuelve, por variable y escenario, el impacto en % del IT base (estable)
    y el impacto absoluto. La absorcion no altera la UB estatica (documentado).
    """
    delta = variacion_pct / 100.0
    variables = [
        ("precio_venta", "Precio de venta (m2)", "Critica: definir precio exacto por tipologia en el sector; dato de mercado no controlable."),
        ("costo_construccion", "Costo duro construccion (m2)", "Critica: definir costo VIS vs Estandar vs Lujo; depende del producto y del mercado de insumos."),
        ("eficiencia_nga", "NGA (eficiencia de diseno)", "Alta: controlable por diseno; optimizar para mejorar la eficiencia sin incertidumbre de mercado."),
        ("costo_lote", "Costo del lote", "Media: dato real del lote, no modificable en el corto plazo."),
        ("absorcion", "Velocidad de absorcion", "Baja en UB estatica; alta en TIR real (afecta costos financieros en Fase 3)."),
    ]

    # Rangos plausibles de variacion (documentados) para ponderar el riesgo.
    rangos_plausibles = {
        "precio_venta": 1.00,           # +-10% del mercado es comun
        "costo_construccion": 1.00,     # +-10% por insumos y mano de obra
        "eficiencia_nga": 0.50,         # +-5% realista por diseno (acotado)
        "costo_lote": 0.30,             # lote casi fijo (negociacion)
        "absorcion": 0.00,              # sin efecto en UB estatica
    }

    filas = []
    for var_id, etiqueta, prioridad in variables:
        impactos_pct_it = []
        impactos_abs = []
        por_escenario = {}
        for esc_id, esc in escenarios.items():
            base = _ub_marginal(gfa, cl, esc, fin)
            it_base = gfa * esc["eficiencia_nga"] * esc["precio_venta_m2"]
            it_base = it_base if it_base != 0 else 1.0

            if var_id == "precio_venta":
                ub_lo = _ub_marginal(gfa, cl, esc, fin, precio=esc["precio_venta_m2"] * (1 - delta))
                ub_hi = _ub_marginal(gfa, cl, esc, fin, precio=esc["precio_venta_m2"] * (1 + delta))
            elif var_id == "costo_construccion":
                ub_lo = _ub_marginal(gfa, cl, esc, fin, costo=esc["costo_construccion_m2"] * (1 - delta))
                ub_hi = _ub_marginal(gfa, cl, esc, fin, costo=esc["costo_construccion_m2"] * (1 + delta))
            elif var_id == "eficiencia_nga":
                ub_lo = _ub_marginal(gfa, cl, esc, fin, eficiencia=esc["eficiencia_nga"] * (1 - delta))
                ub_hi = _ub_marginal(gfa, cl, esc, fin, eficiencia=esc["eficiencia_nga"] * (1 + delta))
            elif var_id == "costo_lote":
                cl_lo = cl * (1 - delta)
                cl_hi = cl * (1 + delta)
                ub_lo = _ub_marginal(gfa, cl_lo, esc, fin)
                ub_hi = _ub_marginal(gfa, cl_hi, esc, fin)
            else:  # absorcion: sin efecto en UB estatica
                ub_lo = base
                ub_hi = base

            d_lo = abs(ub_lo - base) / it_base * 100.0
            d_hi = abs(ub_hi - base) / it_base * 100.0
            impacto_pct = max(d_lo, d_hi)
            impacto_abs = max(abs(ub_lo - base), abs(ub_hi - base))
            impactos_pct_it.append(impacto_pct)
            impactos_abs.append(impacto_abs)
            por_escenario[esc_id] = {
                "impacto_pct_IT": round(impacto_pct, 2),
                "delta_abs_cop": round(impacto_abs, 2),
                "ub_base_cop": round(base, 2),
                "ub_minus_cop": round(ub_lo, 2),
                "ub_plus_cop": round(ub_hi, 2),
            }

        prom = sum(impactos_pct_it) / len(impactos_pct_it) if impactos_pct_it else 0.0
        riesgo = prom * rangos_plausibles[var_id]
        filas.append({
            "variable": var_id,
            "etiqueta": etiqueta,
            "impacto_pct_IT_promedio": round(prom, 2),
            "riesgo_esperado": round(riesgo, 2),
            "rango_plausible_x": rangos_plausibles[var_id],
            "prioridad_fetch": prioridad,
            "por_escenario": por_escenario,
        })

    # Ranking por riesgo esperado (impacto x rango plausible)
    filas_rank = sorted(filas, key=lambda f: f["riesgo_esperado"], reverse=True)
    for i, fila in enumerate(filas_rank, start=1):
        fila["puesto"] = i

    return {"variacion_pct": variacion_pct,
            "nota_metodologica": ("Sensibilidad marginal con unidades continuas; impacto medido como "
                                  "variacion de la utilidad bruta en % de los ingresos totales base. "
                                  "La absorcion no altera la UB estatica (afecta TIR/costos financieros en Fase 3)."),
            "ranking": filas_rank}


# ----------------------------------------------------------------------------
# Recomendacion
# ----------------------------------------------------------------------------

def recomendar(resultados: list, alertas_por_esc: dict, reglas: dict) -> dict:
    """Selecciona el escenario viable con mayor ROI (desempate: liquidez)."""
    viables = []
    for res in resultados:
        criticas = [a for a in alertas_por_esc[res["escenario_id"]] if a["nivel"] == "critica"]
        if not criticas:
            viables.append(res)

    if viables:
        viables_orden = sorted(viables, key=lambda r: (-r["ROI_pct"], r["meses_venta_estimados"]))
        mejor = viables_orden[0]
        texto = (
            f"El escenario {mejor['producto']} proyecta un ROI del {_fmt_pct(mejor['ROI_pct'])}%, "
            f"superando a {' y '.join([r['producto'] for r in resultados if r['escenario_id'] != mejor['escenario_id']])}."
        )
        texto += (
            f" Se recomienda disenar aproximadamente {mejor['num_unidades']} unidades de "
            f"{mejor['tamano_unidad_m2']:.0f} m2 con acabados {mejor['nivel_acabados'].lower()}. "
            f"Rentabilidad esperada: utilidad bruta de {_fmt_cop(mejor['utilidad_bruta_cop'])} COP "
            f"(MUB {_fmt_pct(mejor['MUB_pct'])}%, CL/IT {_fmt_pct(mejor['CL_IT_pct'])}%)."
        )
        texto += (" Mix de usos: los 3 escenarios son residenciales puros; un escenario mixto "
                  "(p.ej. local comercial en primer piso) se modela duplicando un escenario con "
                  "precio y costo propios del uso adicional.")
        estado = "VIABLE"
    else:
        mejor = None
        # Buscar el menos malo para orientar la conclusion
        orden = sorted(resultados, key=lambda r: r["ROI_pct"], reverse=True)
        texto = (
            "Ningun escenario cumple las reglas de viabilidad (MUB >= 18%, ROI >= 22%, CL/IT <= 30%). "
            "Conclusion: con los parametros actuales el lote no soporta desarrollo y venta bajo las reglas "
            "de Bogota. Opciones: (1) renegociar el precio del suelo, (2) validar precios de venta reales "
            "con comparables de radio 5 km (el precio y el costo duro son las variables de mayor impacto), "
            "(3) evaluar alternativa de arriendo del lote."
        )
        estado = "NO VIABLE"

    return {
        "estado": estado,
        "recomendado": mejor,
        "ranking_roi": [{"escenario_id": r["escenario_id"], "producto": r["producto"],
                         "ROI_pct": r["ROI_pct"], "MUB_pct": r["MUB_pct"]}
                        for r in sorted(resultados, key=lambda x: x["ROI_pct"], reverse=True)],
        "veredicto_textual": texto,
    }


# ----------------------------------------------------------------------------
# Exportaciones
# ----------------------------------------------------------------------------

def exportar_csv_comparativo(resultados: list, ruta: str) -> None:
    campos = ["escenario_id", "producto", "nivel_acabados", "gfa_m2", "nga_m2",
              "eficiencia_nga", "tamano_unidad_m2", "num_unidades",
              "area_vendible_m2", "precio_venta_m2", "costo_construccion_m2",
              "ingresos_totales_cop", "costo_lote_cop", "costo_duro_cop",
              "costo_blando_cop", "costo_mkt_cop", "costo_total_cop",
              "utilidad_bruta_cop", "MUB_pct", "ROI_pct", "CL_IT_pct",
              "absorcion_unid_mes", "meses_venta_estimados"]
    with open(ruta, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=campos, delimiter=";")
        w.writeheader()
        for r in resultados:
            w.writerow({c: r.get(c, "") for c in campos})


def exportar_csv_sensibilidad(sens: dict, ruta: str) -> None:
    filas = []
    for fila in sens["ranking"]:
        for esc_id, det in fila["por_escenario"].items():
            filas.append({
                "puesto_riesgo": fila["puesto"],
                "variable": fila["variable"],
                "etiqueta": fila["etiqueta"],
                "escenario": esc_id,
                "impacto_pct_IT": det["impacto_pct_IT"],
                "delta_abs_cop": det["delta_abs_cop"],
                "ub_base_cop": det["ub_base_cop"],
                "ub_minus10_cop": det["ub_minus_cop"],
                "ub_plus10_cop": det["ub_plus_cop"],
            })
        filas.append({
            "puesto_riesgo": fila["puesto"],
            "variable": fila["variable"],
            "etiqueta": fila["etiqueta"],
            "escenario": "PROMEDIO",
            "impacto_pct_IT": fila["impacto_pct_IT_promedio"],
            "delta_abs_cop": "",
            "ub_base_cop": "",
            "ub_minus10_cop": "",
            "ub_plus10_cop": "",
        })
    with open(ruta, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=list(filas[0].keys()), delimiter=";")
        w.writeheader()
        w.writerows(filas)


def analizar_aporte_suelo(resultados: list, params: dict) -> dict:
    """Escenario D: el dueno del lote lo aporta y participa en las utilidades finales.

    Con el suelo aportado, el costo del lote sale del flujo del desarrollador y el
    dueno recibe un porcentaje de la utilidad bruta (UB) del proyecto al cierre.
    Para cada escenario se calcula:
      - UB sin costo de suelo (UB_nl) y ROI maximo del desarrollador (socio 0%)
      - pct_socio_max: mayor porcentaje que deja al desarrollador ROI >= minimo
      - pct_socio_min: menor porcentaje con el que el dueno recupera al menos el
        valor del suelo soportable por el mercado (CL que daria ROI minimo comprando)
      - ventana de negociacion [min, max] y pct recomendado (punto medio)
    """
    reglas = params["reglas_decision"]
    cl_pedido = costo_lote_total(params["lote"])
    cfg = params.get("aporte_suelo") or {}
    pct_cfg = cfg.get("pct_socio")

    filas = []
    for r in resultados:
        esc_id = r["escenario_id"]
        it = r["ingresos_totales_cop"]
        cd = r["costo_duro_cop"]
        cb = r["costo_blando_cop"]
        cmv = r["costo_mkt_cop"]
        ctd_nl = cd + cb + cmv
        ub_nl = it - ctd_nl

        # CL soportable: CL que con compra dejaria ROI == minimo (maximo que pagaria un comprador)
        denom = 1.0 + reglas["roi_minimo_pct"] / 100.0
        cl_soportable = max(0.0, it / denom - ctd_nl)

        if ub_nl > 0 and ctd_nl > 0:
            roi_max_dev = ub_nl / ctd_nl * 100.0
            pct_max = 100.0 * (1.0 - (reglas["roi_minimo_pct"] / 100.0) * ctd_nl / ub_nl)
        else:
            roi_max_dev = 0.0
            pct_max = None

        pct_min = None
        if ub_nl > 0 and cl_soportable > 0:
            pct_min = cl_soportable / ub_nl * 100.0

        ventana = None
        pct_rec = None
        if pct_max is not None and pct_max > 0 and pct_min is not None and pct_min <= pct_max:
            ventana = {"min_pct": pct_min, "max_pct": pct_max}
            pct_rec = (pct_min + pct_max) / 2.0
        elif pct_max is not None and pct_max > 0 and pct_min is None:
            # Sin referencia de suelo soportable: el dueno negocia desde 0%
            ventana = {"min_pct": 0.0, "max_pct": pct_max}
            pct_min = 0.0
            pct_rec = pct_max * 0.5
        if pct_cfg is not None:
            pct_rec = float(pct_cfg)

        fila = {
            "escenario_id": esc_id,
            "ub_sin_suelo_cop": ub_nl,
            "ctd_sin_suelo_cop": ctd_nl,
            "roi_max_dev_pct": roi_max_dev,
            "cl_soportable_cop": cl_soportable,
            "pct_socio_min_pct": pct_min,
            "pct_socio_max_pct": pct_max,
            "ventana_posible": ventana is not None,
            "pct_socio_recomendado_pct": round(pct_rec, 1) if pct_rec is not None else None,
        }
        if pct_rec is not None and ub_nl > 0:
            dev_ub = ub_nl * (1.0 - pct_rec / 100.0)
            dev_roi = dev_ub / ctd_nl * 100.0
            socio_recibe = ub_nl * pct_rec / 100.0
            fila.update({
                "dev_ub_cop": dev_ub,
                "dev_roi_pct": dev_roi,
                "socio_recibe_cop": socio_recibe,
                "socio_retorno_vs_pedido_pct": (socio_recibe / cl_pedido * 100.0) if cl_pedido else None,
                "socio_retorno_vs_soportable_pct": (socio_recibe / cl_soportable * 100.0) if cl_soportable else None,
            })
        else:
            fila.update({"dev_ub_cop": None, "dev_roi_pct": None, "socio_recibe_cop": None,
                         "socio_retorno_vs_pedido_pct": None, "socio_retorno_vs_soportable_pct": None})
        filas.append(fila)

    mejor = max(filas, key=lambda f: f["roi_max_dev_pct"] or 0.0)
    return {
        "descripcion": ("Escenario D: el dueno del lote lo aporta al proyecto y participa "
                        "en las utilidades finales en lugar de recibir el precio de venta por adelantado."),
        "cl_pedido_cop": cl_pedido,
        "roi_minimo_pct": reglas["roi_minimo_pct"],
        "pct_socio_manual": pct_cfg,
        "escenarios": filas,
        "mejor_escenario": mejor["escenario_id"],
    }


def analizar_arriendo(resultados: list, params: dict) -> dict:
    """Escenario E: el lote se arrienda durante el ciclo (24 meses) en vez de comprarse.

    El costo del suelo pasa de ser un desembolso inicial (CL) a un canon de arrendamiento.
    Se evalua con el canon sobre el precio pedido (base) y sobre el valor de suelo
    soportable por el mercado (CL que daria ROI minimo comprando), porque el canon se
    negocia tipicamente sobre el valor realizable, no sobre el precio pedido.
    """
    cl = costo_lote_total(params["lote"])
    cfg = params.get("arriendo_lote") or {}
    mensual_pct = float(cfg.get("mensual_pct_cl", 0.75))
    meses = int(cfg.get("meses", 24))
    reglas = params["reglas_decision"]

    filas = []
    for r in resultados:
        it = r["ingresos_totales_cop"]
        ctd = r["costo_total_cop"]
        cl_esc = r["costo_lote_cop"]
        ctd_sin_tierra = ctd - cl_esc
        denom = 1.0 + reglas["roi_minimo_pct"] / 100.0
        cl_sop = max(0.0, it / denom - ctd_sin_tierra)

        fila = {"escenario_id": r["escenario_id"]}
        for nombre, cl_base in (("pedido", cl), ("soportable", cl_sop)):
            canon = cl_base * mensual_pct / 100.0 * meses
            ctd_a = ctd_sin_tierra + canon
            ub_a = it - ctd_a
            roi = (ub_a / ctd_a * 100.0) if ctd_a > 0 else 0.0
            mub = (ub_a / it * 100.0) if it > 0 else 0.0
            fila.update({
                "canon_%s_cop" % nombre: canon,
                "ub_%s_cop" % nombre: ub_a,
                "roi_%s_pct" % nombre: roi,
                "mub_%s_pct" % nombre: mub,
                "canon_it_%s_pct" % nombre: (canon / it * 100.0) if it > 0 else 0.0,
                "viable_%s" % nombre: (roi >= reglas["roi_minimo_pct"]
                                        and mub >= reglas["mub_riesgo_pct"]),
            })
        filas.append(fila)

    return {
        "descripcion": ("Escenario E: el lote se arrienda durante el ciclo (%d meses) en lugar de "
                        "comprarse; el canon reemplaza el desembolso del CL y el lote vuelve al dueno." % meses),
        "cl_pedido_cop": cl,
        "mensual_pct_cl": mensual_pct,
        "meses": meses,
        "canon_base_cop": cl * mensual_pct / 100.0 * meses,
        "escenarios": filas,
        "mejor_escenario": max(filas, key=lambda f: f["roi_soportable_pct"] or 0.0)["escenario_id"],
    }


def flujo_caja_estimado(res: dict, params: dict, pct_socio: float, modalidad: str,
                         canon_total: float = None) -> dict:
    """Flujo de caja trimestral estimado (24 meses) para un escenario.

    modalidad = "compra"  -> el lote se paga al inicio (CL) y el dueno sale del proyecto.
    modalidad = "aporte"  -> el dueno aporta el lote y recibe pct_socio % de la UB al
                             cierre (solo si la UB es positiva).
    modalidad = "arriendo" -> el lote se arrienda; se paga un canon por trimestre y el
                             lote vuelve al dueno al final (canon_total opcional; si no
                             se pasa, se calcula con arriendo_lote.mensual_pct_cl).

    Chequeo de consistencia: el acumulado final debe coincidir con la UB del modelo
    estatico (compra -> UB; aporte -> UB + CL - reparto; arriendo -> UB + CL - canon).
    """
    fc = params.get("flujo_caja") or {}
    n = int(fc.get("trimestres", 8))

    def _norm(lista):
        lst = list(lista or []) + [0.0] * (n - len(lista or []))
        lst = lst[:n]
        total = sum(lst)
        if total <= 0:
            raise ValueError("flujo_caja: las listas de porcentajes deben sumar > 0")
        return [x / total for x in lst]

    ing_pct = _norm(fc.get("ingresos_pct", [0, 10, 10, 10, 10, 10, 10, 40]))
    cd_pct = _norm(fc.get("cd_pct", [0, 15, 15, 20, 20, 15, 15, 0]))
    cb_pct = _norm(fc.get("cb_pct", [25, 25, 25, 25, 0, 0, 0, 0]))
    cmv_pct = _norm(fc.get("cmv_pct") or fc.get("ingresos_pct", [0, 10, 10, 10, 10, 10, 10, 40]))
    cl_pct = _norm(fc.get("cl_pct", [100, 0, 0, 0, 0, 0, 0, 0]))
    canon_pct = _norm(fc.get("canon_pct", [12.5] * 8))
    rep_trim = int(fc.get("reparto_dueno_trimestre", n - 1))

    it = res["ingresos_totales_cop"]
    cd = res["costo_duro_cop"]
    cb = res["costo_blando_cop"]
    cmv = res["costo_mkt_cop"]
    cl = res["costo_lote_cop"]
    ub = res["utilidad_bruta_cop"]
    ub_nl = ub + cl
    reparto = max(ub_nl, 0.0) * pct_socio / 100.0 if modalidad == "aporte" else 0.0
    if modalidad == "arriendo" and canon_total is None:
        cfg_ar = params.get("arriendo_lote") or {}
        canon_total = cl * float(cfg_ar.get("mensual_pct_cl", 0.75)) / 100.0 * int(cfg_ar.get("meses", 24))

    filas = []
    acum = 0.0
    for t in range(n):
        cl_t = cl * cl_pct[t] if modalidad == "compra" else 0.0
        canon_t = (canon_total or 0.0) * canon_pct[t] if modalidad == "arriendo" else 0.0
        rep_t = reparto if (modalidad == "aporte" and t == rep_trim) else 0.0
        neto = (it * ing_pct[t]) - (cd * cd_pct[t]) - (cb * cb_pct[t]) - (cmv * cmv_pct[t]) - cl_t - canon_t - rep_t
        acum += neto
        filas.append({
            "trimestre": t,
            "meses": "%02d-%02d" % (t * 3, t * 3 + 3),
            "ingresos_cop": it * ing_pct[t],
            "costo_lote_cop": cl_t,
            "canon_arriendo_cop": canon_t,
            "costo_duro_cop": cd * cd_pct[t],
            "costo_blando_cop": cb * cb_pct[t],
            "costo_mkt_cop": cmv * cmv_pct[t],
            "reparto_dueno_cop": rep_t,
            "flujo_neto_cop": neto,
            "acumulado_cop": acum,
        })
    if modalidad == "compra":
        esperado = ub
    elif modalidad == "aporte":
        esperado = ub_nl - reparto
    else:
        esperado = ub + cl - (canon_total or 0.0)
    consistente = abs(acum - esperado) <= max(1.0, abs(esperado) * 1e-9)
    return {
        "escenario_id": res["escenario_id"],
        "modalidad": modalidad,
        "pct_socio_pct": pct_socio if modalidad == "aporte" else None,
        "canon_total_cop": canon_total if modalidad == "arriendo" else None,
        "filas": filas,
        "totales": {
            "ingresos_cop": it,
            "costos_cop": cd + cb + cmv + (cl if modalidad == "compra" else 0.0)
                          + (canon_total or 0.0 if modalidad == "arriendo" else 0.0) + reparto,
            "reparto_dueno_cop": reparto,
            "flujo_neto_total_cop": acum,
        },
        "ub_esperada_cop": esperado,
        "consistente": consistente,
    }


def exportar_csv_flujo(fc: dict, ruta: str) -> None:
    filas = []
    for f in fc["filas"]:
        filas.append({
            "trimestre": f["trimestre"],
            "meses": f["meses"],
            "ingresos_cop": f["ingresos_cop"],
            "costo_lote_cop": f["costo_lote_cop"],
            "canon_arriendo_cop": f["canon_arriendo_cop"],
            "costo_duro_cop": f["costo_duro_cop"],
            "costo_blando_cop": f["costo_blando_cop"],
            "costo_mkt_cop": f["costo_mkt_cop"],
            "reparto_dueno_cop": f["reparto_dueno_cop"],
            "flujo_neto_cop": f["flujo_neto_cop"],
            "acumulado_cop": f["acumulado_cop"],
        })
    filas.append({"trimestre": "TOTAL", "flujo_neto_cop": fc["totales"]["flujo_neto_total_cop"]})
    with open(ruta, "w", newline="", encoding="utf-8-sig") as fh:
        w = csv.DictWriter(fh, fieldnames=list(filas[0].keys()), delimiter=";")
        w.writeheader()
        w.writerows(filas)


# ----------------------------------------------------------------------------
# Informe HTML (estetica: Fathom Information Design — publicacion cientifica)
# ----------------------------------------------------------------------------

_CSS = """
:root{--papel:#FAF9F6;--tinta:#1C1C1A;--gris:#6B6B66;--linea:#D8D5CD;--navy:#1F3A5F;
--rojo:#B0413E;--verde:#3E6B4F;--amarillo:#9A7B2D;--celda:#F1EFE9;}
*{box-sizing:border-box;margin:0;padding:0;}
body{background:var(--papel);color:var(--tinta);
font-family:"Helvetica Neue",Helvetica,Arial,"Segoe UI",sans-serif;
line-height:1.55;padding:0 0 80px 0;}
.wrap{max-width:1080px;margin:0 auto;padding:0 28px;}
header{padding:56px 0 30px;border-bottom:3px solid var(--tinta);margin-bottom:34px;}
.kicker{font-size:11px;letter-spacing:.22em;text-transform:uppercase;color:var(--gris);margin-bottom:10px;}
h1{font-size:30px;font-weight:700;letter-spacing:-.01em;line-height:1.2;}
.sub{color:var(--gris);font-size:14px;margin-top:8px;}
.meta{display:flex;flex-wrap:wrap;gap:8px 26px;margin-top:18px;font-size:12.5px;color:var(--gris);}
.meta b{color:var(--tinta);font-weight:600;}
h2{font-size:17px;font-weight:700;letter-spacing:.02em;text-transform:uppercase;
margin:44px 0 14px;padding-top:20px;border-top:1px solid var(--linea);}
.veredicto{background:var(--tinta);color:var(--papel);padding:26px 30px;border-radius:2px;}
.veredicto .tag{display:inline-block;font-size:11px;letter-spacing:.18em;text-transform:uppercase;
border:1px solid currentColor;padding:3px 10px;margin-bottom:12px;border-radius:2px;}
.veredicto.viable .tag{color:#A9CBB4;}
.veredicto.no-viable .tag{color:#E0A9A6;}
.veredicto p{font-size:15.5px;max-width:64ch;}
table{width:100%;border-collapse:collapse;font-size:13.5px;margin:10px 0 6px;}
th{background:var(--celda);text-align:left;font-weight:600;padding:9px 10px;
border-bottom:2px solid var(--tinta);font-size:12px;letter-spacing:.03em;}
td{padding:8px 10px;border-bottom:1px solid var(--linea);vertical-align:top;}
td.num,th.num{text-align:right;font-variant-numeric:tabular-nums;}
tr.ultimo td{border-bottom:2px solid var(--tinta);}
.estado{padding:2px 8px;border-radius:2px;font-size:11.5px;font-weight:600;letter-spacing:.04em;white-space:nowrap;}
.ok{background:#E3EDE6;color:var(--verde);}
.bad{background:#F6E4E3;color:var(--rojo);}
.warn{background:#F4EDDC;color:var(--amarillo);}
.alertas{margin:8px 0 4px;padding:0;list-style:none;font-size:13px;}
.alertas li{padding:7px 12px 7px 14px;border-left:3px solid var(--linea);margin-bottom:6px;background:var(--celda);}
.alertas .critica{border-left-color:var(--rojo);}
.alertas .advertencia{border-left-color:var(--amarillo);}
.alertas .positiva{border-left-color:var(--verde);}
.alertas b{font-size:11px;letter-spacing:.1em;text-transform:uppercase;margin-right:8px;}
.fuente{font-size:12px;color:var(--gris);margin:4px 0 10px;}
.fuente a{color:var(--navy);}
.nota{background:var(--celda);border-left:3px solid var(--navy);padding:12px 16px;
font-size:13px;margin:12px 0;color:#33332F;}
.tabla-scroll{overflow-x:auto;}
.mini{font-size:12px;color:var(--gris);}
footer{margin-top:56px;padding-top:18px;border-top:1px solid var(--linea);
font-size:11.5px;color:var(--gris);}
.grid-sens{display:grid;grid-template-columns:1fr 1fr;gap:26px;}
@media(max-width:860px){.grid-sens{grid-template-columns:1fr;}}
.tornado{width:100%;height:auto;}
.leyenda{font-size:12px;color:var(--gris);margin-top:6px;}
.kpi-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin:12px 0;}
@media(max-width:720px){.kpi-grid{grid-template-columns:1fr;}}
.kpi-card{border:1px solid var(--linea);padding:14px 16px;background:#fff;}
.kpi-card .k{font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--gris);}
.kpi-card .v{font-size:22px;font-weight:700;font-variant-numeric:tabular-nums;margin-top:4px;}
.kpi-card .d{font-size:12px;color:var(--gris);margin-top:2px;}
"""


def _barra_svg_mub_roi(resultados: list, reglas: dict) -> str:
    """Barras horizontales de MUB y ROI con lineas de umbral."""
    partes = []
    max_val = max([r["MUB_pct"] for r in resultados] +
                  [r["ROI_pct"] for r in resultados] + [35.0]) * 1.15
    w = 460
    for kpi, umbrales, color_barra in (("MUB_pct", [reglas["mub_riesgo_pct"], reglas["mub_atractivo_pct"]], "#1F3A5F"),
                                       ("ROI_pct", [reglas["roi_minimo_pct"]], "#3E6B4F")):
        partes.append(f'<text x="0" y="0" font-size="11" fill="#6B6B66" '
                      f'text-transform="uppercase" letter-spacing="1.5">{kpi}</text>')
        y = 10
        for r in resultados:
            v = max(r[kpi], 0.0)
            lw = (v / max_val) * w
            partes.append(f'<rect x="0" y="{y}" width="{lw:.1f}" height="16" fill="{color_barra}"/>')
            partes.append(f'<text x="{lw + 8:.1f}" y="{y + 12}" font-size="12" fill="#1C1C1A" '
                          f'font-variant-numeric="tabular-nums">{r[kpi]:.1f}%</text>')
            partes.append(f'<text x="{w + 8}" y="{y + 12}" font-size="11" fill="#6B6B66">'
                          f'{r["producto"].split("—")[0].strip()}</text>')
            y += 26
        for um in umbrales:
            x = (um / max_val) * w
            partes.append(f'<line x1="{x:.1f}" y1="0" x2="{x:.1f}" y2="{y - 6}" '
                          f'stroke="#B0413E" stroke-dasharray="4 3" stroke-width="1.2"/>')
            partes.append(f'<text x="{x:.1f}" y="{y + 6}" font-size="10" fill="#B0413E">'
                          f'umbral {um:.0f}%</text>')
        partes.append(f'<line x1="0" y1="{y + 14}" x2="{w + 120}" y2="{y + 14}" stroke="#D8D5CD"/>')
    altura = 2 * 130
    return (f'<svg class="tornado" viewBox="0 0 {w + 130} {altura}" '
            f'xmlns="http://www.w3.org/2000/svg">{"".join(partes)}</svg>')


def _svg_tornado(sens: dict) -> str:
    """Tornado de sensibilidad: impacto +-10% (promedio % del IT) por variable."""
    filas = sens["ranking"]
    max_imp = max([f["impacto_pct_IT_promedio"] for f in filas] + [1.0])
    w = 460
    h = 30
    altura = len(filas) * h + 20
    partes = []
    partes.append(f'<text x="0" y="12" font-size="11" fill="#6B6B66" letter-spacing="1.5">'
                  f'IMPACTO EN UTILIDAD BRUTA (% DE INGRESOS) ANTE VARIACION +-10%</text>')
    y = 30
    for fila in filas:
        imp = fila["impacto_pct_IT_promedio"]
        lw = (imp / max_imp) * w
        color = "#1F3A5F"
        if fila["variable"] == "absorcion":
            color = "#B9B4A8"
        # barra izquierda (-)
        partes.append(f'<rect x="{w / 2 - lw / 2:.1f}" y="{y}" width="{lw:.1f}" height="14" '
                      f'fill="{color}" opacity="0.55"/>')
        partes.append(f'<text x="{w / 2 + 8}" y="{y + 11}" font-size="11.5" fill="#1C1C1A" '
                      f'font-variant-numeric="tabular-nums">{imp:.1f}%</text>')
        partes.append(f'<text x="{w / 2 + 52}" y="{y + 11}" font-size="11.5" fill="#1C1C1A">'
                      f'{_h(fila["etiqueta"])}</text>')
        y += h
    partes.append(f'<line x1="{w / 2}" y1="20" x2="{w / 2}" y2="{y}" stroke="#1C1C1A" stroke-width="1"/>')
    return (f'<svg class="tornado" viewBox="0 0 {w + 260} {altura}" '
            f'xmlns="http://www.w3.org/2000/svg">{"".join(partes)}</svg>')


def generar_informe_html(params: dict, resultados: list, alertas_por_esc: dict,
                         sens: dict, recomendacion: dict, aporte: dict, arriendo: dict,
                         flujos: list, ruta: str) -> None:
    meta = params["meta"]
    gfa = params["gfa_max_m2"]
    lote = params["lote"]
    reglas = params["reglas_decision"]
    cl_total = costo_lote_total(lote)

    # --- Veredicto ---
    cls_v = "viable" if recomendacion["estado"] == "VIABLE" else "no-viable"
    veredicto_html = (f'<div class="veredicto {cls_v}">'
                      f'<span class="tag">Recomendacion: {recomendacion["estado"]}</span>'
                      f'<p>{_h(recomendacion["veredicto_textual"])}</p></div>')

    # --- Tabla comparativa ---
    filas_tabla = []
    for r in resultados:
        criticas = [a for a in alertas_por_esc[r["escenario_id"]] if a["nivel"] == "critica"]
        advertencias = [a for a in alertas_por_esc[r["escenario_id"]] if a["nivel"] == "advertencia"]
        if criticas:
            estado = '<span class="estado bad">NO VIABLE</span>'
        elif advertencias:
            estado = '<span class="estado warn">PRECAUCION</span>'
        else:
            estado = '<span class="estado ok">VIABLE</span>'
        filas_tabla.append(f"""<tr>
<td><b>{_h(r['producto'])}</b><br><span class="mini">{_h(r['nivel_acabados'])}</span></td>
<td class="num">{r['nga_m2']:.0f}</td>
<td class="num">{r['num_unidades']}</td>
<td class="num">{r['tamano_unidad_m2']:.0f}</td>
<td class="num">{_fmt_m(r['ingresos_totales_cop'])}</td>
<td class="num">{_fmt_m(r['costo_total_cop'])}</td>
<td class="num">{_fmt_m(r['utilidad_bruta_cop'])}</td>
<td class="num">{r['MUB_pct']:.1f}%</td>
<td class="num">{r['ROI_pct']:.1f}%</td>
<td class="num">{r['CL_IT_pct']:.1f}%</td>
<td class="num">{r['meses_venta_estimados']:.0f}</td>
<td>{estado}</td></tr>""")
    tabla = f"""<div class="tabla-scroll"><table>
<tr><th>Escenario</th><th class="num">NGA (m2)</th><th class="num">Unid.</th>
<th class="num">m2/unid</th><th class="num">Ingresos (M$)</th><th class="num">CTD (M$)</th>
<th class="num">UB (M$)</th><th class="num">MUB</th><th class="num">ROI</th>
<th class="num">CL/IT</th><th class="num">Meses venta</th><th>Estado</th></tr>
{''.join(filas_tabla)}</table></div>
<p class="fuente">Cifras en millones de COP. CTD = costo total de desarrollo; UB = utilidad bruta;
MUB = margen bruto sobre ingresos; CL/IT = costo del lote sobre ingresos.</p>"""

    # --- Alertas por escenario ---
    alertas_html = ""
    for r in resultados:
        items = "".join(
            f'<li class="{a["nivel"]}"><b>{a["kpi"]}</b>{_h(a["texto"])}</li>'
            for a in alertas_por_esc[r["escenario_id"]])
        alertas_html += f'<h3 style="margin-top:18px;font-size:14px;">{_h(r["producto"])}</h3><ul class="alertas">{items}</ul>'

    # --- Sensibilidad ---
    filas_sens = ""
    for f in sens["ranking"]:
        filas_sens += (f'<tr><td class="num">{f["puesto"]}</td><td><b>{_h(f["etiqueta"])}</b></td>'
                       f'<td class="num">{f["impacto_pct_IT_promedio"]:.1f}%</td>'
                       f'<td class="num">{f["rango_plausible_x"]:.2f}x</td>'
                       f'<td class="num">{f["riesgo_esperado"]:.1f}</td>'
                       f'<td>{_h(f["prioridad_fetch"])}</td></tr>')
    tabla_sens = f"""<div class="tabla-scroll"><table>
<tr><th class="num">#</th><th>Variable</th><th class="num">Impacto +-10% en UB<br>(% de ingresos)</th>
<th class="num">Rango plausible<br>de variacion</th><th class="num">Riesgo<br>esperado</th>
<th>Prioridad de fetch de datos</th></tr>{filas_sens}</table></div>
<div class="nota">{_h(sens['nota_metodologica'])}<br><br>
<b>Lectura:</b> precio de venta y eficiencia NGA tienen la misma elasticidad en la UB estatica
(ambos escalan los ingresos), pero el precio es una variable de mercado no controlable y con mayor
rango de variacion, por lo que la prioridad de fetch es critica; el costo duro la sigue de cerca.
La absorcion no afecta la UB estatica (su efecto aparece en TIR y costos financieros, Fase 3).</div>"""

    # --- Supuestos y fuentes ---
    filas_fuentes = ""
    for esc_id, esc in params["escenarios"].items():
        filas_fuentes += f"""<tr>
<td><b>{_h(esc['nombre'])}</b></td>
<td class="num">{_fmt_cop(esc['precio_venta_m2'])}</td>
<td class="num">{_fmt_cop(esc['costo_construccion_m2'])}</td>
<td>{_h(esc.get('fuente_precio', ''))}<br>
<a href="{_h(esc.get('fuente_precio_url', '#'))}">{_h(esc.get('fuente_precio_url', ''))}</a></td>
<td>{_h(esc.get('fuente_costo', ''))}<br>
<a href="{_h(esc.get('fuente_costo_url', '#'))}">{_h(esc.get('fuente_costo_url', ''))}</a></td>
</tr>"""
    fuentes_html = f"""<div class="tabla-scroll"><table>
<tr><th>Escenario</th><th class="num">Precio venta (COP/m2)</th><th class="num">Costo duro (COP/m2)</th>
<th>Fuente precio (fecha consulta: {_h(meta.get('fecha_ejecucion', ''))})</th>
<th>Fuente costo</th></tr>{filas_fuentes}</table></div>
<p class="fuente">Suelo: {_h(lote.get('fuente', ''))} — {_h(lote.get('fuente_url', ''))}.
Costos blandos {params['financiero']['costos_blandos_pct']:.0f}% del costo duro; marketing
{params['financiero']['marketing_ventas_pct']:.1f}% de los ingresos; impuestos de escrituracion
{lote['impuestos_escritura_pct']:.0f}%.</p>"""

    # --- KPI cards ---
    mejor = recomendacion.get("recomendado")
    cards = ""
    if mejor:
        cards = f"""<div class="kpi-grid">
<div class="kpi-card"><div class="k">ROI esperado</div><div class="v">{mejor['ROI_pct']:.1f}%</div>
<div class="d">umbral minimo {reglas['roi_minimo_pct']:.0f}%</div></div>
<div class="kpi-card"><div class="k">Utilidad bruta</div><div class="v">${_fmt_m(mejor['utilidad_bruta_cop'])} M</div>
<div class="d">{_fmt_cop(mejor['utilidad_bruta_cop'])} COP</div></div>
<div class="kpi-card"><div class="k">Producto</div><div class="v">{mejor['num_unidades']} unid. de {mejor['tamano_unidad_m2']:.0f} m2</div>
<div class="d">{_h(mejor['nivel_acabados'])} · MUB {mejor['MUB_pct']:.1f}% · CL/IT {mejor['CL_IT_pct']:.1f}%</div></div>
</div>"""

    # --- Escenario D: participacion del dueno del lote en utilidades ---
    filas_aporte = ""
    for f in aporte["escenarios"]:
        if f["ventana_posible"]:
            ventana = f"{f['pct_socio_min_pct']:.1f}% - {f['pct_socio_max_pct']:.1f}%"
        else:
            ventana = "sin acuerdo"
        rec = _fmt_pct(f["pct_socio_recomendado_pct"]) if f["pct_socio_recomendado_pct"] is not None else "—"
        pct_min_str = _fmt_pct(f["pct_socio_min_pct"]) if f["pct_socio_min_pct"] is not None else "—"
        pct_max_str = _fmt_pct(f["pct_socio_max_pct"]) if f["pct_socio_max_pct"] is not None else "—"
        roi_dev = f"{f['dev_roi_pct']:.1f}%" if f["dev_roi_pct"] is not None else "—"
        socio = _fmt_m(f["socio_recibe_cop"]) if f["socio_recibe_cop"] is not None else "—"
        ret_ped = f"{f['socio_retorno_vs_pedido_pct']:.1f}%" if f["socio_retorno_vs_pedido_pct"] is not None else "—"
        ret_sop = f"{f['socio_retorno_vs_soportable_pct']:.1f}%" if f["socio_retorno_vs_soportable_pct"] is not None else "—"
        filas_aporte += f"""<tr>
<td><b>{_h(f['escenario_id'])}</b></td>
<td class="num">{_fmt_m(f['ub_sin_suelo_cop'])}</td>
<td class="num">{f['roi_max_dev_pct']:.1f}%</td>
<td class="num">{_fmt_m(f['cl_soportable_cop'])}</td>
<td class="num">{pct_min_str}</td>
<td class="num">{pct_max_str}</td>
<td>{ventana}</td>
<td class="num">{rec}</td>
<td class="num">{roi_dev}</td>
<td class="num">{socio}</td>
<td class="num">{ret_ped}</td>
<td class="num">{ret_sop}</td></tr>"""
    mejor_esc = aporte["mejor_escenario"]
    fila_mejor = next(f for f in aporte["escenarios"] if f["escenario_id"] == mejor_esc)
    if fila_mejor["pct_socio_recomendado_pct"] is not None:
        nota_mejor = (f"Para <b>{_h(mejor_esc)}</b> el pct recomendado es "
                      f"{_fmt_pct(fila_mejor['pct_socio_recomendado_pct'])}: el desarrollador obtiene ROI "
                      f"{fila_mejor['dev_roi_pct']:.1f}% y el dueno recibe "
                      f"{_fmt_m(fila_mejor['socio_recibe_cop'])} "
                      f"({fila_mejor['socio_retorno_vs_pedido_pct']:.0f}% del precio pedido del lote).")
    else:
        nota_mejor = (f"Para <b>{_h(mejor_esc)}</b> no hay ventana de acuerdo con las reglas actuales: "
                      "o el proyecto no genera utilidades suficientes o el desarrollador no alcanza el ROI minimo.")
    aporte_html = f"""<div class="tabla-scroll"><table>
<tr><th>Escenario</th><th class="num">UB sin suelo<br>(M$)</th><th class="num">ROI max<br>desarrollador</th>
<th class="num">CL soportable<br>por mercado (M$)</th><th class="num">pct min<br>dueno</th>
<th class="num">pct max<br>desarrollador</th><th>Ventana<br>de acuerdo</th>
<th class="num">pct<br>recomendado</th><th class="num">ROI dev<br>@ pct rec</th>
<th class="num">Socio<br>recibe (M$)</th><th class="num">Retorno socio<br>vs precio pedido</th>
<th class="num">Retorno socio<br>vs CL soportable</th></tr>{filas_aporte}</table></div>
<div class="nota"><b>Lectura:</b> si el dueno del lote lo aporta al proyecto y recibe un porcentaje de
las utilidades finales (en lugar de cobrar el precio de venta por adelantado), el desarrollador no
desembolsa el costo del lote y su ROI sube. El <b>pct minimo</b> es lo que necesita el dueno para
recibir al menos el valor del suelo que el mercado soportaria (CL que daria ROI
{reglas['roi_minimo_pct']:.0f}% comprando el lote); el <b>pct maximo</b> es lo que tolera el
desarrollador para conservar ROI >={reglas['roi_minimo_pct']:.0f}%. Si la ventana existe, el punto
medio es el punto de partida de negociacion. {nota_mejor}</div>"""

    # --- Flujo de caja estimado ---
    def _tabla_flujo(fc):
        filas = ""
        for fila in fc["filas"]:
            filas += f"""<tr>
<td class="num">{fila['trimestre']}</td><td>{fila['meses']}</td>
<td class="num">{_fmt_m(fila['ingresos_cop'])}</td>
<td class="num">{_fmt_m(fila['costo_lote_cop'])}</td>
<td class="num">{_fmt_m(fila['canon_arriendo_cop'])}</td>
<td class="num">{_fmt_m(fila['costo_duro_cop'])}</td>
<td class="num">{_fmt_m(fila['costo_blando_cop'])}</td>
<td class="num">{_fmt_m(fila['costo_mkt_cop'])}</td>
<td class="num">{_fmt_m(fila['reparto_dueno_cop'])}</td>
<td class="num">{_fmt_m(fila['flujo_neto_cop'])}</td>
<td class="num">{_fmt_m(fila['acumulado_cop'])}</td></tr>"""
        filas += f"""<tr class="ultimo"><td colspan="9"><b>TOTAL</b></td>
<td class="num"><b>{_fmt_m(fc['totales']['flujo_neto_total_cop'])}</b></td>
<td class="num"><b>{_fmt_m(fc['totales']['flujo_neto_total_cop'])}</b></td></tr>"""
        badge = "consistente" if fc["consistente"] else "INCONSISTENTE"
        color = "ok" if fc["consistente"] else "bad"
        return f"""<div class="tabla-scroll"><table>
<tr><th>#</th><th>Meses</th><th class="num">Ingresos</th><th class="num">Lote (CL)</th>
<th class="num">Canon</th><th class="num">Costo duro</th><th class="num">Blandos</th><th class="num">Mkt</th>
<th class="num">Reparto dueno</th><th class="num">Flujo neto</th><th class="num">Acumulado</th></tr>
{filas}</table></div>
<p class="mini">Cifras en millones de COP. Saldo final {_fmt_m(fc['totales']['flujo_neto_total_cop'])} M
= utilidad bruta del modelo estatico ({_fmt_m(fc['ub_esperada_cop'])} M) — chequeo
<span class="estado {color}">{badge}</span>.</p>"""

    fc_compra = next(f for f in flujos if f["modalidad"] == "compra")
    fc_aporte = next(f for f in flujos if f["modalidad"] == "aporte")
    fc_arriendo = next(f for f in flujos if f["modalidad"] == "arriendo")
    canon_mes = fc_arriendo["canon_total_cop"] / 8.0 if fc_arriendo["canon_total_cop"] else 0.0
    flujo_html = f"""<p class="mini"><b>Modalidad A — compra del lote</b> (el dueno vende y sale del proyecto):</p>
{_tabla_flujo(fc_compra)}
<p class="mini" style="margin-top:18px"><b>Modalidad B — el dueno aporta el lote</b> y recibe
{_fmt_pct(fc_aporte['pct_socio_pct'])} de las utilidades al cierre (solo si hay utilidades):</p>
{_tabla_flujo(fc_aporte)}
<p class="mini" style="margin-top:18px"><b>Modalidad C — el lote se arrienda</b> con canon de
{_fmt_m(fc_arriendo['canon_total_cop'])} M en 24 meses (~{_fmt_m(canon_mes)} M/trimestre):</p>
{_tabla_flujo(fc_arriendo)}"""

    # --- Arriendo del lote (Escenario E) ---
    filas_arriendo = ""
    for f in arriendo["escenarios"]:
        est_sop = "VIABLE" if f["viable_soportable"] else "no viable"
        filas_arriendo += f"""<tr>
<td><b>{_h(f['escenario_id'])}</b></td>
<td class="num">{_fmt_m(f['canon_pedido_cop'])}</td>
<td class="num">{f['roi_pedido_pct']:.1f}%</td>
<td class="num">{f['mub_pedido_pct']:.1f}%</td>
<td class="num">{f['canon_it_pedido_pct']:.1f}%</td>
<td class="num">{_fmt_m(f['canon_soportable_cop'])}</td>
<td class="num">{f['roi_soportable_pct']:.1f}%</td>
<td class="num">{f['mub_soportable_pct']:.1f}%</td>
<td>{est_sop}</td></tr>"""
    arriendo_html = f"""<div class="tabla-scroll"><table>
<tr><th>Escenario</th><th class="num">Canon s/ pedido<br>(M$, 24 meses)</th><th class="num">ROI</th>
<th class="num">MUB</th><th class="num">Canon/IT</th>
<th class="num">Canon s/ valor soportable<br>(M$, 24 meses)</th><th class="num">ROI</th>
<th class="num">MUB</th><th>Estado</th></tr>{filas_arriendo}</table></div>
<div class="nota"><b>Lectura:</b> con canon sobre el precio pedido
({_fmt_m(arriendo['canon_base_cop'])} M en {arriendo['meses']} meses =
{arriendo['mensual_pct_cl']:.2f}%/mes del valor), ningun escenario alcanza el ROI minimo; con canon
negociado sobre el valor de suelo soportable por el mercado, A y B resultan viables. La palanca es
sobre que valor se negocia el canon, no el producto. Canon, meses y porcentaje se editan en
<code>arriendo_lote</code> del JSON.</div>"""

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Prefactibilidad Fase 2 — {_h(meta.get('chip', ''))}</title>
<style>{_CSS}</style>
</head>
<body>
<div class="wrap">
<header>
<div class="kicker">Modelo Financiero Inmobiliario — Prefactibilidad (Fase 2)</div>
<h1>Producto optimo del lote: {_h(meta.get('chip', 'caso de referencia'))}</h1>
<div class="sub">Comparacion de escenarios VIS / Estandar / Lujo para un mismo GFA, con reglas de
decision de Bogota (MUB, ROI, CL/IT) y analisis de sensibilidad +-10%.</div>
<div class="meta">
<span><b>GFA maximo (Fase 1):</b> {gfa:.0f} m2</span>
<span><b>Lote:</b> {lote['area_m2']:.0f} m2 x {_fmt_cop(lote['precio_suelo_m2'])}/m2 + {lote['impuestos_escritura_pct']:.0f}%</span>
<span><b>Costo lote (CL):</b> {_fmt_cop(cl_total)} COP</span>
<span><b>Ciclo:</b> {meta.get('ciclo_desarrollo_anios', 2)} anos (estatico, sin financiacion)</span>
<span><b>Fecha:</b> {_h(meta.get('fecha_ejecucion', ''))}</span>
<span><b>Moneda:</b> COP</span>
</div>
</header>

{veredicto_html}
{cards}

<h2>1. Resumen ejecutivo</h2>
{veredicto_html}

<h2>2. Comparativo de escenarios (KPIs)</h2>
{tabla}

<h2>3. Margen y retorno frente a umbrales</h2>
{_barra_svg_mub_roi(resultados, reglas)}
<p class="leyenda">Lineas punteadas: umbrales de decision (MUB 18% y 25%; ROI 22%).</p>

<h2>4. Analisis de sensibilidad +-10%</h2>
<div class="grid-sens">
<div>{tabla_sens}</div>
<div>{_svg_tornado(sens)}</div>
</div>

<h2>5. Alertas de viabilidad por escenario</h2>
{alertas_html}

<h2>6. Alternativas de suelo: compra, aporte del dueno o arriendo</h2>
{aporte_html}
{arriendo_html}

<h2>7. Flujo de caja estimado (mejor alternativa, 24 meses)</h2>
{flujo_html}
<div class="nota"><b>Supuestos del flujo:</b> preventa/apartado 20% (meses 1-6), cuotas durante obra
40% (meses 7-18), saldo contra entrega 40% (meses 19-24); costo duro 30% en los trimestres 1-2,
40% en 3-4 y 30% en 5-6; blandos 25% por trimestre en el primer ano; marketing sigue a los ingresos;
el lote se paga al inicio en la modalidad compra. El programa es editable en el parametro
<code>flujo_caja</code> del JSON de parametros.</div>

<h2>8. Supuestos, fuentes y trazabilidad</h2>
{fuentes_html}
<div class="nota"><b>Alcance:</b> la envolvente normativa (GFA) se toma como restriccion de entrada de
Fase 1 y no se redefine; no se incluye financiacion, TIR ni VPN en esta version; no se emite concepto
legal, urbanistico o de uso de suelo. La absorcion solo informa liquidez comercial; su efecto
financiero se modelara en Fase 3.</div>

<h2>9. Como actualizar el modelo</h2>
<div class="nota">Edite <b>parametros_entrada.json</b> (GFA, lote, precios, costos, eficiencias,
absorcion o reglas) y vuelva a ejecutar: <code>python F2_DEMANDA_MOTOR_v02.py</code>. El script
recalcula escenarios, alertas, sensibilidad, recomendacion e informe sin tocar el codigo.</div>

<footer>Generado por F2_DEMANDA_MOTOR_v02.py — Fase 2, prefactibilidad.
Datos de mercado consultados el {_h(meta.get('fecha_ejecucion', ''))}; fuentes en la seccion 8.
La seccion 6 compara las alternativas de suelo (compra, aporte del dueno en utilidades o
arriendo) y la 7 el flujo de caja estimado (24 meses) de la mejor alternativa. Este documento es
una herramienta de decision preliminar; requiere validacion de comparables de radio 5 km y
revision especializada antes de decisiones de inversion.</footer>
</div>
</body>
</html>"""

    with open(ruta, "w", encoding="utf-8") as f:
        f.write(html)


def _normalizar_mix(escenarios: dict, gfa: float) -> None:
    """Para escenarios con mix_usos (override de uso multiple), agrega campos
    agregados (eficiencia, precio, costo, absorcion, unidad promedio) que usan la
    sensibilidad marginal y el informe. El calculo principal (run_scenario) usa la
    rama mix_usos con los componentes reales."""
    for esc in escenarios.values():
        if not esc.get("mix_usos"):
            continue
        area_v = 0.0
        it = 0.0
        cd = 0.0
        unid_t = 0
        abs_pond = 0.0
        ef_pond = 0.0
        for m in esc["mix_usos"]:
            gfa_i = gfa * m["pct_gfa"]
            nga_i = gfa_i * m["eficiencia_nga"]
            unid = int(nga_i // m["unidad_m2"])
            area_i = unid * m["unidad_m2"]
            area_v += area_i
            it += area_i * m["precio_venta_m2"]
            cd += gfa_i * m["costo_construccion_m2"]
            unid_t += unid
            abs_pond += unid / max(m.get("absorcion_unid_mes", 2.0), 0.1)
            ef_pond += m["pct_gfa"] * m["eficiencia_nga"]
        esc["eficiencia_nga"] = ef_pond
        esc["precio_venta_m2"] = it / area_v if area_v else 0.0
        esc["costo_construccion_m2"] = cd / gfa if gfa else 0.0
        esc["unidad_m2"] = area_v / unid_t if unid_t else 0.0
        esc["absorcion_unid_mes"] = unid_t / abs_pond if abs_pond else 0.0
        esc["_es_mixto"] = True


# ----------------------------------------------------------------------------
# Flujo principal
# ----------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Motor de demanda inmobiliaria — Prefactibilidad Fase 2 (3 escenarios, "
                    "KPIs, alertas, sensibilidad +-10% e informe HTML).")
    parser.add_argument("--parametros", default="parametros_entrada.json",
                        help="Ruta al JSON de parametros (default: parametros_entrada.json)")
    parser.add_argument("--chip", default=None,
                        help="Identificador CHIP del predio (opcional, sobreescribe meta.chip)")
    parser.add_argument("--gfa", type=float, default=None,
                        help="GFA maximo en m2 (opcional; sobreescribe gfa_max_m2). Compatibilidad CLI del pipeline.")
    parser.add_argument("--costo-lote", type=float, default=None,
                        help="Costo total de adquisicion del lote en COP, incluido impuestos (opcional; sobreescribe lote.costo_lote_total_cop). Compatibilidad CLI del pipeline.")
    parser.add_argument("--sin-informe", action="store_true",
                        help="No genera el informe HTML")
    parser.add_argument("--pct-socio", type=float, default=None,
                        help="Porcentaje de utilidades para el dueno del lote en el escenario D "
                             "(opcional; default: punto medio de la ventana de negociacion)")
    parser.add_argument("--outdir", default="resultados",
                        help="Carpeta de salida relativa al script (default: resultados)")
    args = parser.parse_args()

    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

    base_dir = os.path.dirname(os.path.abspath(__file__))
    ruta_params = args.parametros if os.path.isabs(args.parametros) else \
        os.path.join(base_dir, args.parametros)
    if not os.path.exists(ruta_params):
        print(f"[ERROR] No existe el archivo de parametros: {ruta_params}")
        return 2

    params = cargar_parametros(ruta_params)
    if args.chip:
        params.setdefault("meta", {})["chip"] = args.chip
    if args.gfa is not None:
        params["gfa_max_m2"] = args.gfa
    if args.costo_lote is not None:
        params.setdefault("lote", {})["costo_lote_total_cop"] = args.costo_lote

    meta = params["meta"]
    gfa = params["gfa_max_m2"]
    lote_cfg = params["lote"]
    fin = params["financiero"]
    reglas = params["reglas_decision"]
    sens_cfg = params["sensibilidad"]
    cl = costo_lote_total(lote_cfg)

    # 0) Normalizar escenarios mixtos (override de uso multiple) para sensibilidad e informe
    _normalizar_mix(params["escenarios"], gfa)

    # 1) Escenarios (unidades enteras)
    resultados = []
    for esc_id, esc in params["escenarios"].items():
        esc = dict(esc)
        esc["id"] = esc_id
        res = run_scenario(gfa, cl, esc, fin)
        resultados.append(res)

    # 2) Alertas
    alertas_por_esc = {r["escenario_id"]: evaluar_alertas(r, reglas) for r in resultados}

    # 3) Sensibilidad
    sens = analizar_sensibilidad(gfa, cl, params["escenarios"], fin,
                                 sens_cfg["variacion_pct"])

    # 4) Recomendacion
    recomendacion = recomendar(resultados, alertas_por_esc, reglas)

    # 4.5) Escenario D (aporte del dueno del lote) y flujo de caja de la mejor alternativa
    if args.pct_socio is not None:
        params.setdefault("aporte_suelo", {})["pct_socio"] = args.pct_socio
    aporte = analizar_aporte_suelo(resultados, params)
    arriendo = analizar_arriendo(resultados, params)
    esc_flujo = recomendacion.get("recomendado") or max(resultados, key=lambda r: r["ROI_pct"])
    fila_aporte_flujo = next(f for f in aporte["escenarios"]
                             if f["escenario_id"] == esc_flujo["escenario_id"])
    pct_flujo = fila_aporte_flujo["pct_socio_recomendado_pct"] or 0.0
    canon_flujo = arriendo["canon_base_cop"]
    flujos = [
        flujo_caja_estimado(esc_flujo, params, pct_flujo, "compra"),
        flujo_caja_estimado(esc_flujo, params, pct_flujo, "aporte"),
        flujo_caja_estimado(esc_flujo, params, pct_flujo, "arriendo", canon_flujo),
    ]

    # 5) Exportaciones
    out_dir = os.path.join(base_dir, args.outdir)
    os.makedirs(out_dir, exist_ok=True)
    ruta_json = os.path.join(out_dir, "resultados_completos.json")
    ruta_csv_comp = os.path.join(out_dir, "comparativo_escenarios.csv")
    ruta_csv_sens = os.path.join(out_dir, "sensibilidad.csv")
    ruta_html = os.path.join(out_dir, "informe_F2_prefactibilidad.html")

    paquete = {
        "meta": meta,
        "gfa_max_m2": gfa,
        "lote": lote_cfg,
        "costo_lote_total_cop": round(cl, 2),
        "reglas_decision": reglas,
        "escenarios": resultados,
        "alertas": {k: v for k, v in alertas_por_esc.items()},
        "sensibilidad": sens,
        "recomendacion": recomendacion,
        "aporte_suelo_analisis": aporte,
        "arriendo_analisis": arriendo,
        "flujo_caja": flujos,
        "generado_por": "F2_DEMANDA_MOTOR_v02.py",
    }
    with open(ruta_json, "w", encoding="utf-8") as f:
        json.dump(paquete, f, indent=2, ensure_ascii=False)

    exportar_csv_comparativo(resultados, ruta_csv_comp)
    exportar_csv_sensibilidad(sens, ruta_csv_sens)
    ruta_csv_fc_compra = os.path.join(out_dir, "flujo_caja_%s_compra.csv" % esc_flujo["escenario_id"])
    ruta_csv_fc_aporte = os.path.join(out_dir, "flujo_caja_%s_aporte.csv" % esc_flujo["escenario_id"])
    ruta_csv_fc_arriendo = os.path.join(out_dir, "flujo_caja_%s_arriendo.csv" % esc_flujo["escenario_id"])
    exportar_csv_flujo(flujos[0], ruta_csv_fc_compra)
    exportar_csv_flujo(flujos[1], ruta_csv_fc_aporte)
    exportar_csv_flujo(flujos[2], ruta_csv_fc_arriendo)
    if not args.sin_informe:
        generar_informe_html(params, resultados, alertas_por_esc, sens,
                             recomendacion, aporte, arriendo, flujos, ruta_html)

    # 6) Consola
    print("=" * 78)
    print("ANALISIS DE PREFACTIBILIDAD — FASE 2")
    print(f"CHIP: {meta.get('chip', 'sin asignar')} | GFA maximo: {gfa:.0f} m2 | "
          f"Costo lote: {_fmt_cop(cl)} COP")
    print(f"Fecha de datos: {meta.get('fecha_ejecucion', 'n/d')} | Moneda: COP")
    print("=" * 78)
    cab = (f"{'Escenario':<16}{'NGA':>7}{'Unid':>6}{'m2/u':>6}{'Ingresos M$':>13}"
           f"{'CTD M$':>11}{'UB M$':>11}{'MUB%':>8}{'ROI%':>8}{'CL/IT%':>8}  Estado")
    print(cab)
    print("-" * 78)
    for r in resultados:
        criticas = [a for a in alertas_por_esc[r["escenario_id"]] if a["nivel"] == "critica"]
        estado = "NO VIABLE" if criticas else "VIABLE"
        print(f"{r['producto']:<16}{r['nga_m2']:>7.0f}{r['num_unidades']:>6}"
              f"{r['tamano_unidad_m2']:>6.0f}{_fmt_m(r['ingresos_totales_cop']):>13}"
              f"{_fmt_m(r['costo_total_cop']):>11}{_fmt_m(r['utilidad_bruta_cop']):>11}"
              f"{r['MUB_pct']:>8.1f}{r['ROI_pct']:>8.1f}{r['CL_IT_pct']:>8.1f}  {estado}")
    print("-" * 78)
    print("ALERTAS DE VIABILIDAD:")
    for r in resultados:
        for a in alertas_por_esc[r["escenario_id"]]:
            print(f"  [{a['nivel'].upper():<11}] {r['producto']}: {a['texto']}")
    print("-" * 78)
    print("SENSIBILIDAD +-10% (impacto en UB, % de ingresos, promedio 3 escenarios):")
    for f in sens["ranking"]:
        print(f"  #{f['puesto']} {f['etiqueta']:<38} impacto {f['impacto_pct_IT_promedio']:>5.1f}%"
              f"  riesgo {f['riesgo_esperado']:>5.1f}")
    print("-" * 78)
    print("RECOMENDACION:")
    print(f"  [{recomendacion['estado']}] {recomendacion['veredicto_textual']}")
    print("-" * 78)
    print("ESCENARIO D — PARTICIPACION DEL DUENO DEL LOTE EN UTILIDADES (aporte de suelo):")
    for f in aporte["escenarios"]:
        win = f"[{f['pct_socio_min_pct']:.1f}% - {f['pct_socio_max_pct']:.1f}%]" if f["ventana_posible"] else "sin acuerdo"
        rec = f"{f['pct_socio_recomendado_pct']:.1f}%" if f["pct_socio_recomendado_pct"] is not None else "—"
        roi = f"{f['dev_roi_pct']:.1f}%" if f["dev_roi_pct"] is not None else "—"
        socio = _fmt_m(f["socio_recibe_cop"]) if f["socio_recibe_cop"] is not None else "—"
        print(f"  {f['escenario_id']:<10} UB sin suelo {_fmt_m(f['ub_sin_suelo_cop']):>10} M | "
              f"ROI max dev {f['roi_max_dev_pct']:>5.1f}% | ventana {win:<22} | "
              f"pct rec {rec:>5} | ROI dev {roi:>6} | socio recibe {socio:>8} M")
    print("-" * 78)
    print(f"FLUJO DE CAJA ESTIMADO (24 meses) — mejor alternativa: {esc_flujo['producto']}:")
    for fc in flujos:
        ok = "OK" if fc["consistente"] else "ERROR"
        print(f"  [{fc['modalidad'].upper():<7}] saldo final {_fmt_m(fc['totales']['flujo_neto_total_cop']):>10} M "
              f"| UB esperada {_fmt_m(fc['ub_esperada_cop']):>10} M | chequeo {ok}")
    print("-" * 78)
    print("ESCENARIO E — ARRIENDO DEL LOTE (canon mensual %.2f%% del valor, %d meses):" % (
        arriendo["mensual_pct_cl"], arriendo["meses"]))
    for f in arriendo["escenarios"]:
        est_ped = "VIABLE" if f["viable_pedido"] else "no viable"
        est_sop = "VIABLE" if f["viable_soportable"] else "no viable"
        print(f"  {f['escenario_id']:<10} canon s/pedido {_fmt_m(f['canon_pedido_cop']):>8} M -> ROI "
              f"{f['roi_pedido_pct']:>5.1f}% ({est_ped}) | canon s/soportable {_fmt_m(f['canon_soportable_cop']):>7} M "
              f"-> ROI {f['roi_soportable_pct']:>5.1f}% ({est_sop})")
    print("-" * 78)
    print("Archivos generados:")
    print(f"  JSON : {ruta_json}")
    print(f"  CSV  : {ruta_csv_comp}")
    print(f"  CSV  : {ruta_csv_sens}")
    print(f"  CSV  : {ruta_csv_fc_compra}")
    print(f"  CSV  : {ruta_csv_fc_aporte}")
    print(f"  CSV  : {ruta_csv_fc_arriendo}")
    if not args.sin_informe:
        print(f"  HTML : {ruta_html}")
    print("=" * 78)
    return 0


if __name__ == "__main__":
    sys.exit(main())
