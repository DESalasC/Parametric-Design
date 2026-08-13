# -*- coding: utf-8 -*-
"""
================================================================================
F2_RENTA_MOTOR_v01.py — Modelo Financiero Build-to-Rent (Fase 2)
Proyecto: DiseñoParametrico — Fase 2 (ampliación del F2_Modelo_Financiero)
Python 3.8+ Standalone (sin dependencias externas)
================================================================================

OBJETIVO:
  Desarrollar la recomendacion del F2 ("si CL/IT > 30%, evaluar arriendo"):
  modelar la estrategia de CONSTRUIR PARA ARRENDAR (Build-to-Rent) en lugar de
  construir para vender, con dos horizontes de inversion:

    - CP (corto plazo): arriendo temporal amoblado (dias/semanas/meses),
      mayor canon por m2, mayor vacancia y mayores gastos de operacion y
      gestion; requiere inversion en mobiliario.
    - LP (largo plazo): arriendo residencial tradicional (contratos 12+ meses),
      canon de mercado, vacancia baja y gastos estandar; incremento anual IPC.

  Para cada escenario de producto (A VIS / B Estandar / C Lujo) y cada
  estrategia se proyectan flujos anuales a 10 anos (horizonte configurable),
  con valor de salida por capitalizacion del NOI, y se calculan KPIs de
  inversion en renta: yield bruto/neto (cap rate de entrada), TIR, VPN,
  payback, multiplo, punto de equilibrio de ocupacion y suelo soportable.

ALCANCE (prefactibilidad):
  - Inversion 100% con recursos propios (sin deuda; el apalancamiento y su
    efecto sobre el ROE se documentan como extension para Fase 3).
  - Ocupacion promedio anual constante (sin rampa de leasing del primer ano;
    documentado como supuesto conservador).
  - No redefine el GFA maximo (dato de entrada de Fase 1).
  - No emite concepto legal, urbanistico, tributario o de uso de suelo.

USO:
  python F2_RENTA_MOTOR_v01.py
  python F2_RENTA_MOTOR_v01.py --parametros parametros_AAA0127AZPA_renta.json
  python F2_RENTA_MOTOR_v01.py --parametros parametros_AAA0127AZPA_renta.json --estrategia LP
  python F2_RENTA_MOTOR_v01.py --chip AAA0127AZPA --gfa 632.695061 --costo-lote 1200000000

SALIDAS (carpeta resultados/ o --outdir):
  - resultados_completos.json   : todos los calculos (auditable)
  - comparativo_renta.csv       : KPIs por estrategia x escenario
  - sensibilidad.csv            : impacto +-10% sobre VPN y TIR
  - flujo_caja_<ESTRATEGIA>_<ESCENARIO>.csv : flujo anual del mejor caso
  - informe_F2_renta.html       : informe ejecutivo autocontenido

ESTRUCTURA DE CALCULO (flujo descontado anual, 10 anos):
  NGA         = GFA * eficiencia_nga (por escenario)
  Unidades    = floor(NGA / unidad_m2); area_arrendable = unidades * unidad_m2
  Inversion0  = CL + CD + CB + MKT + Mobiliario(CP)
                CD = GFA * costo_construccion_m2 ; CB = CD * blandos_pct
                MKT = GPI_1 * marketing_leasing_pct
  Por ano t (1..H):
    GPI_t = area * canon_m2_mes * 12 * (1+inc_canon)^(t-1)
    EGI_t = GPI_t * ocupacion_pct
    Adm_t = area * administracion_m2_mes * 12 * (1+inc_gastos)^(t-1)
    Gastos_t = EGI_t * (gastos_operativos_pct + capex_pct) / 100
    NOI_t = EGI_t - Adm_t - Gastos_t
  Salida(H) = NOI_H * (1+inc_canon) / cap_rate_salida_pct
  Flujos: [-Inversion0, NOI_1 .. NOI_{H-1}, NOI_H + Salida]
  KPIs: yield bruto = GPI_1/Inv ; cap rate entrada = NOI_1/Inv ;
        TIR (con salida) ; VPN @ tasa_descuento ; payback simple/descontado ;
        multiplo = (sum NOI + Salida)/Inv ; CL/Inv ; suelo soportable.

SENSIBILIDAD +-10% (efecto marginal sobre VPN y TIR):
  Variables: canon m2, ocupacion, costo duro, cap rate de salida, tasa de
  descuento, gastos operativos, incremento de canon.

FUENTES DE MERCADO (consultadas 2026-08-13):
  - Canon Bogota 2026: Ciencuadras Q1-2026 canon promedio $3.761.958/mes con
    79 m2 ($47.821/m2/mes); FincaRaiz Bogota promedio $5.530.543/mes en 66 m2;
    FincaRaiz Prado Veraniego-Canodromo promedio $1.841.565/mes; comparables
    de la zona (Properati 80 m2 @ $3,0 M; MercadoLibre 47 m2 @ $2,7 M).
  - Vacancia: Bogota 1,9% (inversionistas, 2026); el modelo usa 5% LP
    (incluye rotacion) y 25% CP (temporal amoblado).
  - Cap rates vivienda Colombia: 5,4-6% (Tinsa, inversionistas 2026);
    el modelo usa cap rate de entrada implicito y de salida 6,2% conservador.
  - IPC 2026: 5,56% (DANE, via IPVN Q1-2026); incremento de canon LP 5,5%.
  - Regla de mercado: canon mensual ~1% del valor del inmueble (PADS 2025).
  Cada parametro lleva su fuente y URL dentro de los JSON de parametros.
================================================================================
"""

import argparse
import csv
import json
import os
import sys

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


def _h(texto) -> str:
    """Escapa texto para HTML."""
    return (str(texto)
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;"))


# ----------------------------------------------------------------------------
# Parametros por defecto
# ----------------------------------------------------------------------------

_DEFAULT_PARAMS = {
    "gfa_max_m2": 1200.0,
    "lote": {"area_m2": 450.0, "precio_suelo_m2": 2600000.0,
             "impuestos_escritura_pct": 4.0,
             "fuente": "Supuesto de referencia (reemplazar por dato real del lote).",
             "fuente_url": ""},
    "financiero": {"costos_blandos_pct": 15.0, "marketing_leasing_pct": 2.0},
    "renta": {"horizonte_anios": 10,
              "incremento_canon_pct": 5.5,
              "incremento_gastos_pct": 6.5,
              "cap_rate_salida_pct": 6.2,
              "nota": "Horizonte de inversion y parametros macro (IPC 2026 5,56% DANE; "
                      "gastos crecen con SMMLV)."},
    "reglas_renta": {"tasa_descuento_pct": 10.0,
                     "tir_minima_pct": 10.0,
                     "cap_rate_entrada_min_pct": 5.0,
                     "payback_max_anios": 8.0,
                     "cl_inversion_precaucion_pct": 25.0,
                     "cl_inversion_inviable_pct": 30.0,
                     "nota": "Reglas de decision para inversion en renta (Bogota 2026)."},
    "sensibilidad": {"variacion_pct": 10.0},
    "estrategias": {
        "CP": {"nombre": "Corto plazo — temporal amoblado",
               "ocupacion_pct": 75.0,
               "administracion_m2_mes": 8000.0,
               "gastos_operativos_pct_egi": 25.0,
               "capex_pct_egi": 3.0,
               "mobiliario_cop_m2": 500000.0,
               "nota": "Arriendo temporal amoblado (apartahotel/coliving). Canon prima "
                       "sobre LP, vacancia 25%, gestion intensiva (plataforma, limpieza, "
                       "suministros) y renovacion de mobiliario."},
        "LP": {"nombre": "Largo plazo — arriendo tradicional",
               "ocupacion_pct": 95.0,
               "administracion_m2_mes": 6000.0,
               "gastos_operativos_pct_egi": 12.0,
               "capex_pct_egi": 1.0,
               "mobiliario_cop_m2": 0.0,
               "nota": "Contratos 12+ meses. Vacancia 5% (Bogota 1,9% real + rotacion). "
                       "Gastos: predial, mantenimiento, seguros, corretaje de renovacion."}
    },
    "escenarios": {},
    "referencia_venta": None,
}


def cargar_parametros(ruta: str) -> dict:
    """Carga parametros desde JSON; completa con valores por defecto."""
    with open(ruta, "r", encoding="utf-8") as f:
        data = json.load(f)
    params = json.loads(json.dumps(_DEFAULT_PARAMS))
    params.update(data)
    params.setdefault("meta", {})
    return params


def costo_lote_total(lote_cfg: dict) -> float:
    """CL = area * precio_m2 * (1 + impuestos_pct/100); o directo si viene
    costo_lote_total_cop (compatibilidad con el pipeline --costo-lote)."""
    if lote_cfg.get("costo_lote_total_cop"):
        return float(lote_cfg["costo_lote_total_cop"])
    imp = lote_cfg.get("impuestos_escritura_pct", 4.0) / 100.0
    return lote_cfg["area_m2"] * lote_cfg["precio_suelo_m2"] * (1.0 + imp)


# ----------------------------------------------------------------------------
# Motor de escenario x estrategia
# ----------------------------------------------------------------------------

def area_arrendable(gfa: float, esc: dict) -> tuple:
    """NGA = GFA * eficiencia; unidades enteras; area arrendable real."""
    nga = gfa * esc["eficiencia_nga"]
    unidades = int(nga // esc["unidad_m2"])
    return unidades, unidades * esc["unidad_m2"]


def inversion_inicial(gfa: float, cl: float, esc: dict, estr: dict, fin: dict,
                      area: float, gp1: float) -> dict:
    """Inversion del ano 0: CL + CD + CB + MKT (leasing) + mobiliario (CP)."""
    cd = gfa * esc["costo_construccion_m2"]
    cb = cd * fin["costos_blandos_pct"] / 100.0
    mkt = gp1 * fin["marketing_leasing_pct"] / 100.0
    mob = area * float(estr.get("mobiliario_cop_m2", 0.0))
    total = cl + cd + cb + mkt + mob
    return {
        "costo_lote_cop": cl,
        "costo_duro_cop": cd,
        "costo_blando_cop": cb,
        "marketing_leasing_cop": mkt,
        "mobiliario_cop": mob,
        "total_cop": total,
        "sin_lote_cop": total - cl,
    }


def flujo_anual(area: float, esc: dict, estr: dict, renta: dict,
                horizonte: int) -> dict:
    """NOI por ano + valor de salida. Devuelve listas anuales y resumen."""
    canon = esc["canon_m2_mes"][estr["_id"]]
    ocup = estr["ocupacion_pct"] / 100.0
    adm_m2 = estr["administracion_m2_mes"]
    gastos_pct = (estr["gastos_operativos_pct_egi"] + estr["capex_pct_egi"]) / 100.0
    inc_c = renta["incremento_canon_pct"] / 100.0
    inc_g = renta["incremento_gastos_pct"] / 100.0
    cap_sal = renta["cap_rate_salida_pct"] / 100.0

    anos = []
    gpi_1 = egi_1 = noi_1 = 0.0
    for t in range(1, horizonte + 1):
        gpi = area * canon * 12.0 * (1.0 + inc_c) ** (t - 1)
        egi = gpi * ocup
        adm = area * adm_m2 * 12.0 * (1.0 + inc_g) ** (t - 1)
        gastos = egi * gastos_pct
        noi = egi - adm - gastos
        if t == 1:
            gpi_1, egi_1, noi_1 = gpi, egi, noi
        anos.append({"ano": t, "gpi_cop": gpi, "egi_cop": egi,
                     "administracion_cop": adm, "gastos_cop": gastos,
                     "noi_cop": noi})
    salida = anos[-1]["noi_cop"] * (1.0 + inc_c) / cap_sal
    return {"gpi_1_cop": gpi_1, "egi_1_cop": egi_1, "noi_1_cop": noi_1,
            "salida_cop": salida, "anos": anos,
            "sum_noi_cop": sum(a["noi_cop"] for a in anos)}


# ----------------------------------------------------------------------------
# Finanzas: VPN, TIR, payback
# ----------------------------------------------------------------------------

def vpn(flujos: list, tasa: float) -> float:
    """VPN de una lista de flujos (flujo[0] en t=0)."""
    return sum(f / (1.0 + tasa) ** i for i, f in enumerate(flujos))


def tir(flujos: list, lo: float = -0.90, hi: float = 5.0) -> float:
    """TIR por biseccion. Devuelve la tasa (fraccion) o None si no cruza cero."""
    f_lo = vpn(flujos, lo)
    f_hi = vpn(flujos, hi)
    if f_lo * f_hi > 0:
        # Sin cambio de signo: no hay TIR en el rango (flujo no convencional
        # o proyecto que nunca recupera). Devolvemos el valor mas cercano a cero.
        return None
    for _ in range(200):
        mid = (lo + hi) / 2.0
        f_mid = vpn(flujos, mid)
        if abs(f_mid) < 1e-9:
            return mid
        if f_lo * f_mid < 0:
            hi = mid
        else:
            lo = mid
            f_lo = f_mid
    return (lo + hi) / 2.0


def payback_descontado(flujos: list, tasa: float) -> tuple:
    """(payback simple, payback descontado) en anos, interpolado. None si no recupera."""
    acum_s = 0.0
    acum_d = 0.0
    pb_s = pb_d = None
    for i, f in enumerate(flujos):
        if i == 0:
            acum_s += f
            acum_d += f
            continue
        prev_s, prev_d = acum_s, acum_d
        acum_s += f
        acum_d += f / (1.0 + tasa) ** i
        if pb_s is None and prev_s < 0 <= acum_s:
            pb_s = (i - 1) + (-prev_s) / (acum_s - prev_s)
        if pb_d is None and prev_d < 0 <= acum_d:
            pb_d = (i - 1) + (-prev_d) / (acum_d - prev_d)
    return pb_s, pb_d


def suelo_soportable(vp_ingresos: float, inv_sin_lote: float) -> float:
    """Maximo CL que deja VPN >= 0 con la tasa de descuento exigida."""
    return max(0.0, vp_ingresos - inv_sin_lote)


def ocupacion_breakeven(gpi_1: float, adm_1: float, gastos_pct: float) -> float:
    """Ocupacion minima para NOI >= 0 (GPI y Adm del ano 1; gastos % del EGI)."""
    if gpi_1 <= 0:
        return float("inf")
    denom = gpi_1 * (1.0 - gastos_pct)
    if denom <= 0:
        return float("inf")
    return max(0.0, min(1.0, adm_1 / denom))


# ----------------------------------------------------------------------------
# KPI completo de una combinacion estrategia x escenario
# ----------------------------------------------------------------------------

def run_combinacion(gfa: float, cl: float, esc: dict, estr_id: str, estr: dict,
                    fin: dict, renta: dict, reglas: dict) -> dict:
    """Calcula todos los KPIs de una combinacion."""
    unidades, area = area_arrendable(gfa, esc)
    estr = dict(estr)
    estr["_id"] = estr_id
    horizonte = int(renta["horizonte_anios"])

    fl = flujo_anual(area, esc, estr, renta, horizonte)
    gp1, noi1 = fl["gpi_1_cop"], fl["noi_1_cop"]
    inv = inversion_inicial(gfa, cl, esc, estr, fin, area, gp1)
    inv_total = inv["total_cop"]

    flujos = [-inv_total] + [a["noi_cop"] for a in fl["anos"]]
    flujos[-1] += fl["salida_cop"]

    tasa = reglas["tasa_descuento_pct"] / 100.0
    vpn_val = vpn(flujos, tasa)
    tir_val = tir(flujos)
    tir_pct = tir_val * 100.0 if tir_val is not None else None
    pb_s, pb_d = payback_descontado(flujos, tasa)
    vp_ingresos = vpn([0.0] + [a["noi_cop"] for a in fl["anos"]], tasa) \
        + fl["salida_cop"] / (1.0 + tasa) ** horizonte
    suelo_sop = suelo_soportable(vp_ingresos, inv["sin_lote_cop"])
    adm_1 = fl["anos"][0]["administracion_cop"]
    gastos_pct_tot = (estr["gastos_operativos_pct_egi"] + estr["capex_pct_egi"]) / 100.0
    ocup_be = ocupacion_breakeven(gp1, adm_1, gastos_pct_tot)

    yield_bruto = gp1 / inv_total * 100.0 if inv_total > 0 else 0.0
    cap_entrada = noi1 / inv_total * 100.0 if inv_total > 0 else 0.0
    multiplo = (fl["sum_noi_cop"] + fl["salida_cop"]) / inv_total if inv_total > 0 else 0.0
    cl_inv = cl / inv_total * 100.0 if inv_total > 0 else 0.0

    return {
        "estrategia": estr_id,
        "estrategia_nombre": estr["nombre"],
        "escenario_id": esc["id"],
        "producto": esc["nombre"],
        "gfa_m2": round(gfa, 2),
        "nga_m2": round(gfa * esc["eficiencia_nga"], 2),
        "unidad_m2": esc["unidad_m2"],
        "num_unidades": unidades,
        "area_arrendable_m2": round(area, 2),
        "canon_m2_mes": esc["canon_m2_mes"][estr_id],
        "ocupacion_pct": estr["ocupacion_pct"],
        "horizonte_anios": horizonte,
        "gpi_1_cop": round(gp1, 2),
        "egi_1_cop": round(fl["egi_1_cop"], 2),
        "noi_1_cop": round(noi1, 2),
        "inversion_total_cop": round(inv_total, 2),
        "costo_lote_cop": round(inv["costo_lote_cop"], 2),
        "costo_duro_cop": round(inv["costo_duro_cop"], 2),
        "costo_blando_cop": round(inv["costo_blando_cop"], 2),
        "marketing_leasing_cop": round(inv["marketing_leasing_cop"], 2),
        "mobiliario_cop": round(inv["mobiliario_cop"], 2),
        "salida_cop": round(fl["salida_cop"], 2),
        "sum_noi_cop": round(fl["sum_noi_cop"], 2),
        "yield_bruto_pct": round(yield_bruto, 2),
        "cap_rate_entrada_pct": round(cap_entrada, 2),
        "cap_rate_salida_pct": renta["cap_rate_salida_pct"],
        "TIR_pct": round(tir_pct, 2) if tir_pct is not None else None,
        "VPN_cop": round(vpn_val, 2),
        "payback_anios": round(pb_s, 1) if pb_s is not None else None,
        "payback_descontado_anios": round(pb_d, 1) if pb_d is not None else None,
        "multiplico_x": round(multiplo, 2),
        "CL_inversion_pct": round(cl_inv, 2),
        "suelo_soportable_cop": round(suelo_sop, 2),
        "ocupacion_breakeven_pct": round(ocup_be * 100.0, 1),
        "flujos": flujos,
        "anos": fl["anos"],
        "fuente_canon": esc.get("fuente_canon", ""),
        "fuente_canon_url": esc.get("fuente_canon_url", ""),
        "nota": esc.get("nota", ""),
    }


# ----------------------------------------------------------------------------
# Alertas
# ----------------------------------------------------------------------------

def evaluar_alertas(res: dict, reglas: dict) -> list:
    """Evalua reglas de decision y devuelve lista de alertas textuales."""
    alertas = []
    tir = res["TIR_pct"]
    if tir is None or tir < reglas["tir_minima_pct"]:
        nivel = "critica" if tir is None else (
            "critica" if tir < reglas["tir_minima_pct"] else "advertencia")
        txt = (f"TIR {tir:.1f}% < {reglas['tir_minima_pct']:.0f}%: no alcanza la tasa "
               "exigida por el inversionista para activos en renta en Bogota."
               if tir is not None else
               "TIR no calculable (el proyecto no recupera la inversion): flujo no convencional.")
        alertas.append({"nivel": nivel, "kpi": "TIR", "texto": txt})

    if res["VPN_cop"] < 0:
        alertas.append({"nivel": "critica", "kpi": "VPN",
                        "texto": f"VPN {_fmt_m(res['VPN_cop'])} M < 0 a la tasa de descuento "
                                 f"de {reglas['tasa_descuento_pct']:.0f}%: el proyecto destruye valor."})

    if res["cap_rate_entrada_pct"] < reglas["cap_rate_entrada_min_pct"]:
        alertas.append({"nivel": "critica", "kpi": "Cap rate",
                        "texto": f"Cap rate de entrada {res['cap_rate_entrada_pct']:.1f}% < "
                                 f"{reglas['cap_rate_entrada_min_pct']:.0f}%: el NOI inicial no cubre "
                                 "el costo de capital."})

    if res["payback_descontado_anios"] is not None and \
            res["payback_descontado_anios"] > reglas["payback_max_anios"]:
        alertas.append({"nivel": "advertencia", "kpi": "Payback",
                        "texto": f"Payback descontado {res['payback_descontado_anios']:.1f} anos > "
                                 f"{reglas['payback_max_anios']:.0f} anos: recuperacion lenta."})

    if res["CL_inversion_pct"] > reglas["cl_inversion_inviable_pct"]:
        alertas.append({"nivel": "critica", "kpi": "CL/Inv",
                        "texto": f"CL/inversion {res['CL_inversion_pct']:.1f}% > "
                                 f"{reglas['cl_inversion_inviable_pct']:.0f}%: el suelo absorbe mas "
                                 "del 30% de la inversion; el arriendo del lote o la renegociacion "
                                 "son palancas criticas."})
    elif res["CL_inversion_pct"] > reglas["cl_inversion_precaucion_pct"]:
        alertas.append({"nivel": "advertencia", "kpi": "CL/Inv",
                        "texto": f"CL/inversion {res['CL_inversion_pct']:.1f}% > "
                                 f"{reglas['cl_inversion_precaucion_pct']:.0f}%: el suelo pesa "
                                 "sobre la inversion."})

    if res["ocupacion_breakeven_pct"] > res["ocupacion_pct"]:
        alertas.append({"nivel": "critica", "kpi": "Ocupacion",
                        "texto": f"Ocupacion de equilibrio {res['ocupacion_breakeven_pct']:.0f}% > "
                                 f"ocupacion asumida {res['ocupacion_pct']:.0f}%: el activo pierde "
                                 "dinero en operacion."})

    return alertas


# ----------------------------------------------------------------------------
# Sensibilidad +-10%
# ----------------------------------------------------------------------------

def analizar_sensibilidad(gfa: float, cl: float, escenarios: dict, estrategias: dict,
                          fin: dict, renta: dict, reglas: dict,
                          variacion_pct: float) -> dict:
    """
    Impacto de +-10% de cada variable sobre el VPN (y TIR) de cada combinacion.
    Variables: canon m2, ocupacion, costo duro, cap rate de salida, tasa de
    descuento, gastos operativos, incremento de canon.
    """
    delta = variacion_pct / 100.0
    variables = [
        ("canon_m2_mes", "Canon de arriendo (m2/mes)", "Critica: dato de mercado por zona y tipologia; no controlable."),
        ("ocupacion_pct", "Ocupacion promedio", "Critica: depende de la gestion (CP) o del mercado (LP); rango plausible amplio."),
        ("costo_construccion_m2", "Costo duro construccion (m2)", "Critica: definir producto; depende del mercado de insumos (+15% 2026 CAMACOL)."),
        ("cap_rate_salida_pct", "Cap rate de salida", "Alta: variable de mercado; define el valor de reventa del activo."),
        ("tasa_descuento_pct", "Tasa de descuento", "Alta: costo de oportunidad del inversionista; politica."),
        ("gastos_operativos_pct_egi", "Gastos operativos (% EGI)", "Media: controlable parcialmente por gestion."),
        ("incremento_canon_pct", "Incremento anual del canon", "Media: atado al IPC; piso de rentabilidad real."),
    ]
    rangos_plausibles = {
        "canon_m2_mes": 1.0, "ocupacion_pct": 1.0, "costo_construccion_m2": 1.0,
        "cap_rate_salida_pct": 0.5, "tasa_descuento_pct": 0.3,
        "gastos_operativos_pct_egi": 0.5, "incremento_canon_pct": 0.5,
    }

    def _kpi(var_id: str, factor_lo: float, factor_hi: float,
             esc: dict, estr_id: str, estr: dict) -> tuple:
        esc_m = dict(esc)
        estr_m = dict(estr)
        renta_m = dict(renta)
        reglas_m = dict(reglas)
        if var_id == "canon_m2_mes":
            canon = dict(esc["canon_m2_mes"])
            canon[estr_id] = canon[estr_id] * factor_lo
            esc_m["canon_m2_mes"] = canon
        elif var_id == "ocupacion_pct":
            estr_m["ocupacion_pct"] = estr["ocupacion_pct"] * factor_lo
        elif var_id == "costo_construccion_m2":
            esc_m["costo_construccion_m2"] = esc["costo_construccion_m2"] * factor_lo
        elif var_id == "cap_rate_salida_pct":
            renta_m["cap_rate_salida_pct"] = renta["cap_rate_salida_pct"] * factor_lo
        elif var_id == "tasa_descuento_pct":
            reglas_m["tasa_descuento_pct"] = reglas["tasa_descuento_pct"] * factor_lo
        elif var_id == "gastos_operativos_pct_egi":
            estr_m["gastos_operativos_pct_egi"] = estr["gastos_operativos_pct_egi"] * factor_lo
        elif var_id == "incremento_canon_pct":
            renta_m["incremento_canon_pct"] = renta["incremento_canon_pct"] * factor_lo
        res = run_combinacion(gfa, cl, esc_m, estr_id, estr_m, fin, renta_m, reglas_m)
        return res["VPN_cop"], (res["TIR_pct"] or -99.0)

    filas = []
    for var_id, etiqueta, prioridad in variables:
        por_combo = {}
        impactos_vpn = []
        for esc_id, esc in escenarios.items():
            for estr_id, estr in estrategias.items():
                base_v, base_t = _kpi(var_id, 1.0, 1.0, esc, estr_id, estr)
                lo_v, lo_t = _kpi(var_id, 1 - delta, 1 - delta, esc, estr_id, estr)
                hi_v, hi_t = _kpi(var_id, 1 + delta, 1 + delta, esc, estr_id, estr)
                d_lo = abs(lo_v - base_v)
                d_hi = abs(hi_v - base_v)
                impacto = max(d_lo, d_hi)
                impactos_vpn.append(impacto)
                por_combo[f"{estr_id}_{esc_id}"] = {
                    "vpn_base_cop": round(base_v, 2),
                    "vpn_minus_cop": round(lo_v, 2),
                    "vpn_plus_cop": round(hi_v, 2),
                    "tir_base_pct": round(base_t, 2),
                    "tir_minus_pct": round(lo_t, 2),
                    "tir_plus_pct": round(hi_t, 2),
                    "impacto_vpn_cop": round(impacto, 2),
                }
        prom = sum(impactos_vpn) / len(impactos_vpn) if impactos_vpn else 0.0
        filas.append({
            "variable": var_id,
            "etiqueta": etiqueta,
            "impacto_vpn_promedio_cop": round(prom, 2),
            "riesgo_esperado": round(prom * rangos_plausibles[var_id], 2),
            "rango_plausible_x": rangos_plausibles[var_id],
            "prioridad_fetch": prioridad,
            "por_combo": por_combo,
        })

    filas_rank = sorted(filas, key=lambda f: f["riesgo_esperado"], reverse=True)
    for i, fila in enumerate(filas_rank, start=1):
        fila["puesto"] = i

    return {"variacion_pct": variacion_pct,
            "nota_metodologica": ("Sensibilidad marginal: impacto medido como variacion del VPN "
                                  "(COP) ante +-10% de cada variable, promediado sobre todas las "
                                  "combinaciones estrategia x escenario. El ranking pondera el "
                                  "impacto por el rango plausible de variacion de cada variable."),
            "ranking": filas_rank}


# ----------------------------------------------------------------------------
# Recomendacion
# ----------------------------------------------------------------------------

def recomendar(resultados: list, alertas_por_combo: dict, reglas: dict) -> dict:
    """Selecciona la combinacion viable con mayor TIR (desempate: VPN)."""
    viables = []
    for res in resultados:
        criticas = [a for a in alertas_por_combo[f"{res['estrategia']}_{res['escenario_id']}"]
                    if a["nivel"] == "critica"]
        if not criticas:
            viables.append(res)

    orden = sorted(resultados, key=lambda r: (r["TIR_pct"] is not None, r["TIR_pct"] or -99.0,
                                              r["VPN_cop"]), reverse=True)

    if viables:
        mejor = sorted(viables, key=lambda r: (r["TIR_pct"] or -99.0, r["VPN_cop"]),
                       reverse=True)[0]
        texto = (f"La combinacion {mejor['estrategia_nombre']} x {mejor['producto']} es la unica "
                 f"estrategia viable con TIR {mejor['TIR_pct']:.1f}% (VPN "
                 f"{_fmt_m(mejor['VPN_cop'])} M, cap rate de entrada "
                 f"{mejor['cap_rate_entrada_pct']:.1f}%). "
                 f"Producto: {mejor['num_unidades']} unidades de {mejor['unidad_m2']:.0f} m2 con canon "
                 f"{_fmt_cop(mejor['canon_m2_mes'])}/m2/mes y ocupacion {mejor['ocupacion_pct']:.0f}%.")
        estado = "VIABLE"
    else:
        mejor = orden[0] if orden else None
        texto = (
            "Ninguna combinacion de producto y estrategia cumple las reglas de inversion en renta "
            f"(TIR >= {reglas['tir_minima_pct']:.0f}%, cap rate de entrada >= "
            f"{reglas['cap_rate_entrada_min_pct']:.0f}%, VPN > 0). "
            "La mejor alternativa es la que reporta mayor TIR; las palancas que el analisis de "
            "sensibilidad identifica como criticas son: (1) canon de arriendo y ocupacion "
            "(gestion comercial y producto), (2) costo duro de construccion, (3) cap rate de salida "
            "(mercado de inversion) y (4) precio del suelo: el CL soportable se reporta por "
            "combinacion y es la vara de negociacion con el dueno del lote."
        )
        estado = "NO VIABLE"

    return {
        "estado": estado,
        "recomendado": mejor,
        "ranking": [{"combo": f"{r['estrategia']}_{r['escenario_id']}",
                     "estrategia": r["estrategia_nombre"], "producto": r["producto"],
                     "TIR_pct": r["TIR_pct"], "VPN_cop": r["VPN_cop"],
                     "cap_rate_entrada_pct": r["cap_rate_entrada_pct"]}
                    for r in orden],
        "veredicto_textual": texto,
    }


# ----------------------------------------------------------------------------
# Exportaciones CSV
# ----------------------------------------------------------------------------

def exportar_csv_comparativo(resultados: list, ruta: str) -> None:
    campos = ["estrategia", "estrategia_nombre", "escenario_id", "producto",
              "gfa_m2", "nga_m2", "unidad_m2", "num_unidades", "area_arrendable_m2",
              "canon_m2_mes", "ocupacion_pct", "horizonte_anios",
              "gpi_1_cop", "egi_1_cop", "noi_1_cop", "inversion_total_cop",
              "costo_lote_cop", "costo_duro_cop", "costo_blando_cop",
              "marketing_leasing_cop", "mobiliario_cop", "salida_cop", "sum_noi_cop",
              "yield_bruto_pct", "cap_rate_entrada_pct", "cap_rate_salida_pct",
              "TIR_pct", "VPN_cop", "payback_anios", "payback_descontado_anios",
              "multiplico_x", "CL_inversion_pct", "suelo_soportable_cop",
              "ocupacion_breakeven_pct"]
    with open(ruta, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=campos, delimiter=";")
        w.writeheader()
        for r in resultados:
            w.writerow({c: r.get(c, "") for c in campos})


def exportar_csv_sensibilidad(sens: dict, ruta: str) -> None:
    filas = []
    for fila in sens["ranking"]:
        for combo, det in fila["por_combo"].items():
            filas.append({
                "puesto_riesgo": fila["puesto"],
                "variable": fila["variable"],
                "etiqueta": fila["etiqueta"],
                "combinacion": combo,
                "impacto_vpn_cop": det["impacto_vpn_cop"],
                "vpn_base_cop": det["vpn_base_cop"],
                "vpn_minus10_cop": det["vpn_minus_cop"],
                "vpn_plus10_cop": det["vpn_plus_cop"],
                "tir_base_pct": det["tir_base_pct"],
            })
        filas.append({
            "puesto_riesgo": fila["puesto"],
            "variable": fila["variable"],
            "etiqueta": fila["etiqueta"],
            "combinacion": "PROMEDIO",
            "impacto_vpn_cop": "",
            "vpn_base_cop": "",
            "vpn_minus10_cop": "",
            "vpn_plus10_cop": "",
            "tir_base_pct": "",
        })
    with open(ruta, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=list(filas[0].keys()), delimiter=";")
        w.writeheader()
        w.writerows(filas)


def exportar_csv_flujo(res: dict, ruta: str) -> None:
    filas = []
    acum = -res["inversion_total_cop"]
    for a in res["anos"]:
        acum += a["noi_cop"]
        filas.append({
            "ano": a["ano"],
            "gpi_cop": a["gpi_cop"],
            "egi_cop": a["egi_cop"],
            "administracion_cop": a["administracion_cop"],
            "gastos_cop": a["gastos_cop"],
            "noi_cop": a["noi_cop"],
            "flujo_inversionista_cop": a["noi_cop"],
            "acumulado_cop": acum,
        })
    filas[-1]["flujo_inversionista_cop"] += res["salida_cop"]
    filas[-1]["acumulado_cop"] += res["salida_cop"]
    filas.append({
        "ano": "TOTAL",
        "gpi_cop": sum(a["gpi_cop"] for a in res["anos"]),
        "egi_cop": sum(a["egi_cop"] for a in res["anos"]),
        "administracion_cop": sum(a["administracion_cop"] for a in res["anos"]),
        "gastos_cop": sum(a["gastos_cop"] for a in res["anos"]),
        "noi_cop": sum(a["noi_cop"] for a in res["anos"]),
        "flujo_inversionista_cop": res["sum_noi_cop"] + res["salida_cop"],
        "acumulado_cop": res["sum_noi_cop"] + res["salida_cop"] - res["inversion_total_cop"],
    })
    with open(ruta, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=list(filas[0].keys()), delimiter=";")
        w.writeheader()
        w.writerows(filas)


# ----------------------------------------------------------------------------
# Informe HTML (estetica: Fathom Information Design)
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
h3{font-size:14px;font-weight:700;margin:18px 0 8px;}
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
tr.grupo td{background:var(--celda);font-weight:700;font-size:12px;letter-spacing:.08em;
text-transform:uppercase;color:var(--navy);border-bottom:2px solid var(--tinta);}
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
.kpi-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin:12px 0;}
@media(max-width:720px){.kpi-grid{grid-template-columns:1fr;}}
.kpi-card{border:1px solid var(--linea);padding:14px 16px;background:#fff;}
.kpi-card .k{font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--gris);}
.kpi-card .v{font-size:22px;font-weight:700;font-variant-numeric:tabular-nums;margin-top:4px;}
.kpi-card .d{font-size:12px;color:var(--gris);margin-top:2px;}
.barra-tir{display:flex;align-items:center;gap:10px;margin:6px 0;}
.barra-tir .lab{width:150px;font-size:12px;color:var(--gris);text-align:right;flex-shrink:0;}
.barra-tir .pista{flex:1;background:var(--celda);height:16px;position:relative;}
.barra-tir .pista .fill{height:100%;background:var(--navy);}
.barra-tir .pista .umbral{position:absolute;top:-3px;bottom:-3px;width:2px;background:var(--rojo);}
.barra-tir .val{width:64px;font-size:12.5px;font-weight:600;font-variant-numeric:tabular-nums;}
"""


def _svg_tornado(sens: dict) -> str:
    """Tornado de sensibilidad: impacto +-10% sobre el VPN (promedio, COP)."""
    filas = sens["ranking"]
    max_imp = max([f["impacto_vpn_promedio_cop"] for f in filas] + [1.0])
    w = 460
    h = 30
    altura = len(filas) * h + 20
    partes = []
    partes.append(f'<text x="0" y="12" font-size="11" fill="#6B6B66" letter-spacing="1.5">'
                  f'IMPACTO EN VPN (COP) ANTE VARIACION +-10% — PROMEDIO TODAS LAS COMBINACIONES</text>')
    y = 30
    for fila in filas:
        imp = fila["impacto_vpn_promedio_cop"]
        lw = (imp / max_imp) * w
        color = "#1F3A5F"
        if fila["variable"] in ("tasa_descuento_pct",):
            color = "#9A7B2D"
        partes.append(f'<rect x="{w / 2 - lw / 2:.1f}" y="{y}" width="{lw:.1f}" height="14" '
                      f'fill="{color}" opacity="0.55"/>')
        partes.append(f'<text x="{w / 2 + 8}" y="{y + 11}" font-size="11.5" fill="#1C1C1A" '
                      f'font-variant-numeric="tabular-nums">{_fmt_m(imp)} M</text>')
        partes.append(f'<text x="{w / 2 + 62}" y="{y + 11}" font-size="11.5" fill="#1C1C1A">'
                      f'{_h(fila["etiqueta"])}</text>')
        y += h
    partes.append(f'<line x1="{w / 2}" y1="20" x2="{w / 2}" y2="{y}" stroke="#1C1C1A" stroke-width="1"/>')
    return (f'<svg class="tornado" viewBox="0 0 {w + 280} {altura}" '
            f'xmlns="http://www.w3.org/2000/svg">{"".join(partes)}</svg>')


def _barras_tir(resultados: list, reglas: dict) -> str:
    """Barras de TIR y cap rate de entrada con umbral."""
    umbral_tir = reglas["tir_minima_pct"]
    umbral_cap = reglas["cap_rate_entrada_min_pct"]
    max_v = max([(r["TIR_pct"] or 0.0) for r in resultados] +
                [r["cap_rate_entrada_pct"] for r in resultados] + [12.0]) * 1.2
    partes = []
    for kpi, umbral, color in (("TIR_pct", umbral_tir, "#1F3A5F"),
                               ("cap_rate_entrada_pct", umbral_cap, "#3E6B4F")):
        partes.append(f'<h3 style="margin-top:10px;">{kpi.replace("_pct", "")} (%)</h3>')
        for r in sorted(resultados, key=lambda x: (x["TIR_pct"] or -99.0) if kpi == "TIR_pct" else x["cap_rate_entrada_pct"]):
            v = r[kpi] or 0.0
            pct_w = min(100.0, v / max_v * 100.0)
            etiqueta = f"{r['estrategia_nombre'].split(' — ')[0]} · {r['producto'].split(' — ')[0]}"
            partes.append(
                f'<div class="barra-tir"><span class="lab">{_h(etiqueta)}</span>'
                f'<div class="pista"><div class="fill" style="width:{pct_w:.1f}%"></div>'
                f'<div class="umbral" style="left:{min(100.0, umbral / max_v * 100.0):.1f}%"></div></div>'
                f'<span class="val">{v:.1f}%</span></div>')
        partes.append(f'<p class="leyenda">Umbral: {umbral:.0f}% (linea roja).</p>')
    return "".join(partes)


def generar_informe_html(params: dict, resultados: list, alertas_por_combo: dict,
                         sens: dict, recomendacion: dict, ruta: str) -> None:
    meta = params["meta"]
    gfa = params["gfa_max_m2"]
    lote = params["lote"]
    reglas = params["reglas_renta"]
    renta = params["renta"]
    cl_total = costo_lote_total(lote)

    cls_v = "viable" if recomendacion["estado"] == "VIABLE" else "no-viable"
    veredicto_html = (f'<div class="veredicto {cls_v}">'
                      f'<span class="tag">Recomendacion: {recomendacion["estado"]}</span>'
                      f'<p>{_h(recomendacion["veredicto_textual"])}</p></div>')

    # --- Tabla comparativa por estrategia x escenario ---
    filas_tabla = []
    for estr_id in ("CP", "LP"):
        grupo = next(r for r in resultados if r["estrategia"] == estr_id)
        filas_tabla.append(
            f'<tr class="grupo"><td colspan="12">{_h(grupo["estrategia_nombre"])}</td></tr>')
        for r in [x for x in resultados if x["estrategia"] == estr_id]:
            criticas = [a for a in alertas_por_combo[f"{r['estrategia']}_{r['escenario_id']}"]
                        if a["nivel"] == "critica"]
            estado = '<span class="estado bad">NO VIABLE</span>' if criticas else \
                     '<span class="estado ok">VIABLE</span>'
            tir = f"{r['TIR_pct']:.1f}%" if r["TIR_pct"] is not None else "—"
            filas_tabla.append(f"""<tr>
<td><b>{_h(r['producto'])}</b><br><span class="mini">{r['num_unidades']} unid. de {r['unidad_m2']:.0f} m2</span></td>
<td class="num">{r['area_arrendable_m2']:.0f}</td>
<td class="num">{_fmt_cop(r['canon_m2_mes'])}</td>
<td class="num">{r['ocupacion_pct']:.0f}%</td>
<td class="num">{_fmt_m(r['gpi_1_cop'])}</td>
<td class="num">{_fmt_m(r['noi_1_cop'])}</td>
<td class="num">{_fmt_m(r['inversion_total_cop'])}</td>
<td class="num">{r['cap_rate_entrada_pct']:.1f}%</td>
<td class="num">{tir}</td>
<td class="num">{_fmt_m(r['VPN_cop'])}</td>
<td class="num">{r['payback_descontado_anios'] if r['payback_descontado_anios'] is not None else '—'}</td>
<td>{estado}</td></tr>""")
    tabla = f"""<div class="tabla-scroll"><table>
<tr><th>Producto</th><th class="num">Area arr.<br>(m2)</th><th class="num">Canon<br>($/m2/mes)</th>
<th class="num">Ocup.</th><th class="num">GPI a1<br>(M$)</th><th class="num">NOI a1<br>(M$)</th>
<th class="num">Inversion<br>(M$)</th><th class="num">Cap rate<br>entrada</th><th class="num">TIR</th>
<th class="num">VPN (M$)</th><th class="num">Payback<br>desc. (a)</th><th>Estado</th></tr>
{''.join(filas_tabla)}</table></div>
<p class="fuente">Cifras en millones de COP. GPI = ingreso bruto potencial; NOI = ingreso neto operativo;
cap rate de entrada = NOI a1 / inversion; TIR y VPN con horizonte de {renta['horizonte_anios']:.0f} anos
y valor de salida capitalizado al {renta['cap_rate_salida_pct']:.1f}%.</p>"""

    # --- Alertas ---
    alertas_html = ""
    for r in resultados:
        items = "".join(
            f'<li class="{a["nivel"]}"><b>{a["kpi"]}</b>{_h(a["texto"])}</li>'
            for a in alertas_por_combo[f"{r['estrategia']}_{r['escenario_id']}"])
        alertas_html += (f'<h3>{_h(r["estrategia_nombre"])} · {_h(r["producto"])}</h3>'
                         f'<ul class="alertas">{items}</ul>')

    # --- Sensibilidad ---
    filas_sens = ""
    for f in sens["ranking"]:
        filas_sens += (f'<tr><td class="num">{f["puesto"]}</td><td><b>{_h(f["etiqueta"])}</b></td>'
                       f'<td class="num">{_fmt_m(f["impacto_vpn_promedio_cop"])}</td>'
                       f'<td class="num">{f["rango_plausible_x"]:.2f}x</td>'
                       f'<td class="num">{_fmt_m(f["riesgo_esperado"])}</td>'
                       f'<td>{_h(f["prioridad_fetch"])}</td></tr>')
    tabla_sens = f"""<div class="tabla-scroll"><table>
<tr><th class="num">#</th><th>Variable</th><th class="num">Impacto +-10% en VPN<br>(M$, promedio)</th>
<th class="num">Rango plausible</th><th class="num">Riesgo esperado<br>(M$)</th>
<th>Prioridad de fetch de datos</th></tr>{filas_sens}</table></div>
<div class="nota">{_h(sens['nota_metodologica'])}<br><br>
<b>Lectura:</b> el canon y la ocupacion son las variables de mayor impacto sobre el VPN porque
escalan directamente el ingreso; el costo duro domina la inversion; el cap rate de salida define
el valor residual del activo. El incremento del canon (IPC) es la proteccion contra la inflacion
y la palanca estructural del modelo de renta.</div>"""

    # --- Suelo soportable ---
    filas_suelo = ""
    for r in sorted(resultados, key=lambda x: x["suelo_soportable_cop"], reverse=True):
        est = ('<span class="estado ok">cubre CL</span>' if r["suelo_soportable_cop"] >= cl_total
               else '<span class="estado bad">no cubre CL</span>')
        filas_suelo += f"""<tr>
<td>{_h(r['estrategia_nombre'].split(' — ')[0])}</td>
<td><b>{_h(r['producto'])}</b></td>
<td class="num">{_fmt_m(r['suelo_soportable_cop'])}</td>
<td class="num">{r['CL_inversion_pct']:.1f}%</td>
<td>{est}</td></tr>"""
    suelo_html = f"""<div class="tabla-scroll"><table>
<tr><th>Estrategia</th><th>Producto</th><th class="num">CL soportable<br>(M$)</th>
<th class="num">CL / inversion</th><th>Vs. CL pedido ({_fmt_m(cl_total)} M)</th></tr>
{filas_suelo}</table></div>
<div class="nota"><b>Lectura:</b> el CL soportable es el maximo que el proyecto de renta puede pagar
por el suelo dejando VPN >= 0 a la tasa de descuento exigida ({reglas['tasa_descuento_pct']:.0f}%).
Si el precio pedido del lote lo supera, la diferencia es la brecha de negociacion (o la razon para
arrendar el lote / buscar otro esquema de suelo).</div>"""

    # --- Referencia venta (F2) ---
    ref_html = ""
    ref = params.get("referencia_venta")
    if ref and ref.get("escenarios"):
        filas_ref = ""
        for esc_id, det in ref["escenarios"].items():
            filas_ref += f"""<tr>
<td><b>{_h(det.get('nombre', esc_id))}</b></td>
<td class="num">{det.get('ROI_venta_pct', '—')}%</td>
<td class="num">{det.get('MUB_venta_pct', '—')}%</td>
<td class="num">{det.get('CL_IT_pct', '—')}%</td>
<td class="num">{det.get('estado', '—')}</td></tr>"""
        ref_html = f"""<h2>4. Comparacion con la alternativa de venta (F2)</h2>
<p class="mini">{_h(ref.get('nota', ''))}</p>
<div class="tabla-scroll"><table>
<tr><th>Escenario</th><th class="num">ROI venta<br>(F2)</th><th class="num">MUB venta</th>
<th class="num">CL/IT venta</th><th>Estado venta</th></tr>{filas_ref}</table></div>
<div class="nota"><b>Lectura:</b> la tabla reproduce los KPIs del modelo de venta
(F2_Modelo_Financiero) para el mismo lote. Compare el ROI de venta contra la TIR de renta:
la renta transforma un flujo unico (2 anos) en un flujo perpetuo (10 anos + salida) con riesgo
operativo, y su atractivo depende de la tasa exigida y del precio del suelo.</div>"""

    # --- Flujo de caja del mejor caso ---
    mejor = recomendacion["recomendado"]
    flujo_html = ""
    if mejor:
        filas_fc = ""
        acum = -mejor["inversion_total_cop"]
        for a in mejor["anos"]:
            acum += a["noi_cop"]
            filas_fc += f"""<tr>
<td class="num">{a['ano']}</td>
<td class="num">{_fmt_m(a['gpi_cop'])}</td>
<td class="num">{_fmt_m(a['egi_cop'])}</td>
<td class="num">{_fmt_m(a['administracion_cop'])}</td>
<td class="num">{_fmt_m(a['gastos_cop'])}</td>
<td class="num">{_fmt_m(a['noi_cop'])}</td>
<td class="num">{_fmt_m(acum)}</td></tr>"""
        filas_fc += f"""<tr class="ultimo"><td colspan="5"><b>Valor de salida (a{mejor['horizonte_anios']})</b></td>
<td class="num"><b>{_fmt_m(mejor['salida_cop'])}</b></td>
<td class="num"><b>{_fmt_m(acum + mejor['salida_cop'])}</b></td></tr>"""
        flujo_html = f"""<h2>7. Flujo de caja anual — mejor combinacion ({_h(mejor['estrategia_nombre'])} · {_h(mejor['producto'])})</h2>
<p class="mini">Inversion inicial {_fmt_m(mejor['inversion_total_cop'])} M (lote
{_fmt_m(mejor['costo_lote_cop'])} M + construccion {_fmt_m(mejor['costo_duro_cop'])} M + blandos
{_fmt_m(mejor['costo_blando_cop'])} M + leasing {_fmt_m(mejor['marketing_leasing_cop'])} M
+ mobiliario {_fmt_m(mejor['mobiliario_cop'])} M). Cifras en millones de COP.</p>
<div class="tabla-scroll"><table>
<tr><th class="num">Ano</th><th class="num">GPI</th><th class="num">EGI</th><th class="num">Administracion</th>
<th class="num">Gastos + capex</th><th class="num">NOI</th><th class="num">Acumulado</th></tr>
{filas_fc}</table></div>"""

    # --- KPI cards ---
    cards = ""
    if mejor:
        tir_c = f"{mejor['TIR_pct']:.1f}%" if mejor["TIR_pct"] is not None else "—"
        cards = f"""<div class="kpi-grid">
<div class="kpi-card"><div class="k">TIR (con salida)</div><div class="v">{tir_c}</div>
<div class="d">minimo exigido {reglas['tir_minima_pct']:.0f}%</div></div>
<div class="kpi-card"><div class="k">Cap rate entrada</div><div class="v">{mejor['cap_rate_entrada_pct']:.1f}%</div>
<div class="d">NOI a1 / inversion</div></div>
<div class="kpi-card"><div class="k">VPN</div><div class="v">${_fmt_m(mejor['VPN_cop'])} M</div>
<div class="d">@ {reglas['tasa_descuento_pct']:.0f}% anual</div></div>
<div class="kpi-card"><div class="k">Inversion total</div><div class="v">${_fmt_m(mejor['inversion_total_cop'])} M</div>
<div class="d">{_h(mejor['estrategia_nombre'].split(' — ')[0])} · {mejor['num_unidades']} unid.</div></div>
</div>"""

    # --- Supuestos y fuentes ---
    filas_fuentes = ""
    for esc_id, esc in params["escenarios"].items():
        cps = esc["canon_m2_mes"].get("CP", "—")
        lps = esc["canon_m2_mes"].get("LP", "—")
        filas_fuentes += f"""<tr>
<td><b>{_h(esc['nombre'])}</b></td>
<td class="num">{_fmt_cop(lps)}</td>
<td class="num">{_fmt_cop(cps)}</td>
<td class="num">{_fmt_cop(esc['costo_construccion_m2'])}</td>
<td>{_h(esc.get('fuente_canon', ''))}<br>
<a href="{_h(esc.get('fuente_canon_url', '#'))}">{_h(esc.get('fuente_canon_url', ''))}</a></td>
<td>{_h(esc.get('fuente_costo', ''))}</td></tr>"""
    fuentes_html = f"""<div class="tabla-scroll"><table>
<tr><th>Escenario</th><th class="num">Canon LP<br>($/m2/mes)</th><th class="num">Canon CP<br>($/m2/mes)</th>
<th class="num">Costo duro<br>($/m2)</th><th>Fuente canon (consultada {_h(meta.get('fecha_ejecucion', ''))})</th>
<th>Fuente costo</th></tr>{filas_fuentes}</table></div>
<p class="fuente">Suelo: {_h(lote.get('fuente', ''))} — {_h(lote.get('fuente_url', ''))}.
Costos blandos {params['financiero']['costos_blandos_pct']:.0f}% del costo duro; leasing
{params['financiero']['marketing_leasing_pct']:.0f}% del GPI a1; mobiliario CP
{_fmt_cop(params['estrategias']['CP']['mobiliario_cop_m2'])}/m2; incremento de canon
{renta['incremento_canon_pct']:.1f}%/ano (IPC 2026 5,56% DANE) y de gastos
{renta['incremento_gastos_pct']:.1f}%/ano.</p>"""

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Renta (Build-to-Rent) Fase 2 — {_h(meta.get('chip', ''))}</title>
<style>{_CSS}</style>
</head>
<body>
<div class="wrap">
<header>
<div class="kicker">Modelo Financiero Inmobiliario — Construir para arrendar (Fase 2)</div>
<h1>Build-to-Rent del lote: {_h(meta.get('chip', 'caso de referencia'))}</h1>
<div class="sub">Ampliacion del F2 (que recomendaba evaluar arriendo cuando CL/IT > 30%): el proyecto
se construye y se mantiene como activo generador de renta, con dos estrategias — corto plazo temporal
amoblado (CP) y largo plazo tradicional (LP) — para cada escenario de producto, a
{renta['horizonte_anios']:.0f} anos con valor de salida.</div>
<div class="meta">
<span><b>GFA maximo (Fase 1):</b> {gfa:.0f} m2</span>
<span><b>Lote:</b> {lote['area_m2']:.0f} m2 · CL {_fmt_cop(cl_total)} COP</span>
<span><b>Estrategias:</b> CP (temporal amoblado) y LP (tradicional)</span>
<span><b>Tasa exigida:</b> {reglas['tasa_descuento_pct']:.0f}% · <b>TIR minima:</b> {reglas['tir_minima_pct']:.0f}%</span>
<span><b>Fecha:</b> {_h(meta.get('fecha_ejecucion', ''))}</span>
<span><b>Moneda:</b> COP</span>
</div>
</header>

{veredicto_html}
{cards}

<h2>1. Resumen ejecutivo</h2>
{veredicto_html}

<h2>2. Comparativo de estrategias y productos (KPIs)</h2>
{tabla}

<h2>3. TIR y cap rate frente a umbrales</h2>
{_barras_tir(resultados, reglas)}

{ref_html}

<h2>5. Analisis de sensibilidad +-10%</h2>
<div class="grid-sens">
<div>{tabla_sens}</div>
<div>{_svg_tornado(sens)}</div>
</div>

<h2>6. Suelo soportable por combinacion</h2>
{suelo_html}

{flujo_html}

<h2>8. Alertas de viabilidad por combinacion</h2>
{alertas_html}

<h2>9. Supuestos, fuentes y trazabilidad</h2>
{fuentes_html}
<div class="nota"><b>Alcance:</b> inversion 100% propia (sin deuda; el apalancamiento y su efecto
sobre el ROE se reservan para Fase 3); ocupacion promedio anual constante desde el ano 1 (sin rampa
de leasing); la envolvente normativa (GFA) es restriccion de entrada de Fase 1; no se emite concepto
legal, urbanistico, tributario o de uso de suelo. El impuesto predial, seguros, mantenimiento y
corretaje se agrupan en los gastos operativos (% del EGI); la administracion de propiedad horizontal
se modela aparte (COP/m2/mes).</div>

<h2>10. Como actualizar el modelo</h2>
<div class="nota">Edite <b>parametros_entrada.json</b> (GFA, lote, cánones por escenario y estrategia,
ocupacion, gastos, reglas, horizonte o cap rate de salida) y vuelva a ejecutar:
<code>python F2_RENTA_MOTOR_v01.py</code>. El script recalcula KPIs, alertas, sensibilidad,
recomendacion e informe sin tocar el codigo. Para el lote real use
<code>--parametros parametros_AAA0127AZPA_renta.json</code>.</div>

<footer>Generado por F2_RENTA_MOTOR_v01.py — Fase 2, Build-to-Rent (prefactibilidad).
Datos de mercado consultados el {_h(meta.get('fecha_ejecucion', ''))}; fuentes en la seccion 8.
Este documento es una herramienta de decision preliminar; requiere validacion de comparables de
cánones en radio 5 km y revision especializada antes de decisiones de inversion.</footer>
</div>
</body>
</html>"""

    with open(ruta, "w", encoding="utf-8") as f:
        f.write(html)


# ----------------------------------------------------------------------------
# Flujo principal
# ----------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Motor Build-to-Rent — Fase 2 (2 estrategias x 3 escenarios, flujo "
                    "descontado 10 anos, KPIs de renta, sensibilidad +-10% e informe HTML).")
    parser.add_argument("--parametros", default="parametros_entrada.json",
                        help="Ruta al JSON de parametros (default: parametros_entrada.json)")
    parser.add_argument("--chip", default=None,
                        help="Identificador CHIP del predio (opcional, sobreescribe meta.chip)")
    parser.add_argument("--gfa", type=float, default=None,
                        help="GFA maximo en m2 (sobreescribe gfa_max_m2)")
    parser.add_argument("--costo-lote", type=float, default=None,
                        help="Costo total del lote COP (sobreescribe lote.costo_lote_total_cop)")
    parser.add_argument("--estrategia", choices=["CP", "LP", "todas"], default="todas",
                        help="Estrategia a evaluar (default: todas)")
    parser.add_argument("--outdir", default=None,
                        help="Carpeta de salida (default: resultados/)")
    parser.add_argument("--sin-informe", action="store_true",
                        help="No generar el informe HTML")
    args = parser.parse_args()

    params = cargar_parametros(args.parametros)
    meta = params["meta"]
    gfa = args.gfa if args.gfa is not None else params["gfa_max_m2"]
    lote = params["lote"]
    if args.costo_lote is not None:
        lote = dict(lote)
        lote["costo_lote_total_cop"] = args.costo_lote
    cl = costo_lote_total(lote)
    fin = params["financiero"]
    renta = params["renta"]
    reglas = params["reglas_renta"]
    escenarios = params["escenarios"]
    estrategias = {k: v for k, v in params["estrategias"].items()
                   if args.estrategia == "todas" or k == args.estrategia}

    # Etiquetar escenarios
    for esc_id, esc in escenarios.items():
        esc["id"] = esc_id

    # 1) Calcular combinaciones
    resultados = []
    for estr_id, estr in estrategias.items():
        for esc_id, esc in escenarios.items():
            res = run_combinacion(gfa, cl, esc, estr_id, estr, fin, renta, reglas)
            resultados.append(res)

    # 2) Alertas
    alertas_por_combo = {}
    for res in resultados:
        alertas_por_combo[f"{res['estrategia']}_{res['escenario_id']}"] = \
            evaluar_alertas(res, reglas)

    # 3) Sensibilidad
    sens = analizar_sensibilidad(gfa, cl, escenarios, estrategias, fin, renta, reglas,
                                 params["sensibilidad"]["variacion_pct"])

    # 4) Recomendacion
    recomendacion = recomendar(resultados, alertas_por_combo, reglas)

    # 5) Salidas
    outdir = args.outdir or "resultados"
    os.makedirs(outdir, exist_ok=True)
    base = os.path.join(outdir, "")
    ruta_json = base + "resultados_completos.json"
    ruta_csv_comp = base + "comparativo_renta.csv"
    ruta_csv_sens = base + "sensibilidad.csv"
    ruta_html = base + "informe_F2_renta.html"

    salida_json = {
        "meta": meta,
        "gfa_max_m2": gfa,
        "costo_lote_cop": cl,
        "parametros_usados": {
            "financiero": fin,
            "renta": renta,
            "reglas_renta": reglas,
            "sensibilidad": params["sensibilidad"],
            "escenarios": {k: {kk: vv for kk, vv in v.items() if kk != "id"}
                           for k, v in escenarios.items()},
            "estrategias": {k: v for k, v in estrategias.items()},
        },
        "resultados": [{k: v for k, v in r.items() if k not in ("flujos", "anos")}
                       for r in resultados],
        "alertas": alertas_por_combo,
        "sensibilidad": sens,
        "recomendacion": {k: v for k, v in recomendacion.items() if k != "recomendado"}
                          | ({"recomendado": {k: v for k, v in recomendacion["recomendado"].items()
                                              if k not in ("flujos", "anos")}}
                             if recomendacion["recomendado"] else {}),
    }
    with open(ruta_json, "w", encoding="utf-8") as f:
        json.dump(salida_json, f, ensure_ascii=False, indent=2)

    exportar_csv_comparativo(resultados, ruta_csv_comp)
    exportar_csv_sensibilidad(sens, ruta_csv_sens)

    ruta_csv_flujo = None
    mejor = recomendacion["recomendado"]
    if mejor:
        ruta_csv_flujo = base + f"flujo_caja_{mejor['estrategia']}_{mejor['escenario_id']}.csv"
        exportar_csv_flujo(mejor, ruta_csv_flujo)

    if not args.sin_informe:
        generar_informe_html(params, resultados, alertas_por_combo, sens,
                             recomendacion, ruta_html)

    # 6) Consola
    print("=" * 84)
    print("ANALISIS BUILD-TO-RENT — FASE 2")
    print(f"CHIP: {meta.get('chip', 'sin asignar')} | GFA maximo: {gfa:.2f} m2 | "
          f"Costo lote: {_fmt_cop(cl)} COP")
    print(f"Fecha de datos: {meta.get('fecha_ejecucion', 'n/d')} | Moneda: COP | "
          f"Tasa exigida: {reglas['tasa_descuento_pct']:.0f}%")
    print("=" * 84)
    cab = (f"{'Estrategia':<34}{'NGA':>7}{'Area':>7}{'Canon':>10}{'Ocup':>6}"
           f"{'Inv M$':>10}{'CapRate':>8}{'TIR%':>8}{'VPN M$':>10}{'PB a':>6}  Estado")
    print(cab)
    print("-" * 84)
    for r in resultados:
        criticas = [a for a in alertas_por_combo[f"{r['estrategia']}_{r['escenario_id']}"]
                    if a["nivel"] == "critica"]
        estado = "NO VIABLE" if criticas else "VIABLE"
        tir = f"{r['TIR_pct']:.1f}" if r["TIR_pct"] is not None else "n/d"
        pb = f"{r['payback_descontado_anios']:.1f}" if r["payback_descontado_anios"] is not None else "—"
        print(f"{r['estrategia_nombre'].split(' — ')[0] + ' · ' + r['producto']:<34}"
              f"{r['nga_m2']:>7.0f}{r['area_arrendable_m2']:>7.0f}"
              f"{_fmt_cop(r['canon_m2_mes']):>10}{r['ocupacion_pct']:>5.0f}%"
              f"{_fmt_m(r['inversion_total_cop']):>10}"
              f"{r['cap_rate_entrada_pct']:>7.1f}%{tir:>8}"
              f"{_fmt_m(r['VPN_cop']):>10}{pb:>6}  {estado}")
    print("-" * 84)
    print("SUELO SOPORTABLE (maximo CL con VPN >= 0):")
    for r in sorted(resultados, key=lambda x: x["suelo_soportable_cop"], reverse=True):
        marca = "OK" if r["suelo_soportable_cop"] >= cl else "brecha"
        print(f"  {r['estrategia_nombre'].split(' — ')[0]:<8} {r['producto']:<18} "
              f"{_fmt_m(r['suelo_soportable_cop']):>10} M  ({marca})")
    print("-" * 84)
    print("SENSIBILIDAD +-10% (impacto en VPN, M$ promedio):")
    for f in sens["ranking"]:
        print(f"  #{f['puesto']} {f['etiqueta']:<42} {_fmt_m(f['impacto_vpn_promedio_cop']):>9} M"
              f"  riesgo {_fmt_m(f['riesgo_esperado']):>9} M")
    print("-" * 84)
    print("RECOMENDACION:")
    print(f"  [{recomendacion['estado']}] {recomendacion['veredicto_textual']}")
    print("-" * 84)
    print("Archivos generados:")
    print(f"  JSON : {os.path.abspath(ruta_json)}")
    print(f"  CSV  : {os.path.abspath(ruta_csv_comp)}")
    print(f"  CSV  : {os.path.abspath(ruta_csv_sens)}")
    if ruta_csv_flujo:
        print(f"  CSV  : {os.path.abspath(ruta_csv_flujo)}")
    if not args.sin_informe:
        print(f"  HTML : {os.path.abspath(ruta_html)}")
    print("=" * 84)
    return 0


if __name__ == "__main__":
    sys.exit(main())
