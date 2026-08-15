# -*- coding: utf-8 -*-
"""
================================================================================
verificacion_independiente.py — Verificador independiente del modelo F2 Renta
Proyecto: DiseñoParametrico — Fase 2 (Build-to-Rent)
================================================================================

Recalcula con formulas escritas a mano (equivalente a una hoja de calculo
independiente) todos los KPIs del motor F2_RENTA_MOTOR_v03.py y los contrasta
contra el JSON de resultados generado por el motor.

Diferencias deliberadas respecto al motor (independencia metodologica):
  - TIR: el motor usa biseccion; este verificador usa Newton-Raphson.
  - VPN/NOI: formulas literales reescritas (misma matematica, distinto codigo).
  - Payback: recalculo directo con acumulados.

USO:
  python verificacion_independiente.py                       # usa resultados/ y parametros_entrada.json
  python verificacion_independiente.py --parametros parametros_AAA0127AZPA_renta.json --resultados resultados_AAA0127AZPA_renta

SALIDA: PASS si todas las comparaciones cumplen tolerancia; FAIL en caso contrario.
================================================================================
"""

import argparse
import json
import math
import os
import sys

TOL_MONTO = 0.005   # 0,5% relativo para montos
TOL_TIR = 0.1       # 0,1 puntos porcentuales para TIR


def _costo_lote(lote: dict) -> float:
    if lote.get("costo_lote_total_cop"):
        return float(lote["costo_lote_total_cop"])
    return lote["area_m2"] * lote["precio_suelo_m2"] * (1 + lote.get("impuestos_escritura_pct", 4.0) / 100.0)


def _vp(flujos: list, tasa: float) -> float:
    return sum(f / (1 + tasa) ** i for i, f in enumerate(flujos))


def _tir_newton(flujos: list, semilla: float = 0.10) -> float:
    """TIR por Newton-Raphson sobre la derivada del VPN."""
    t = semilla
    for _ in range(100):
        v = 0.0
        dv = 0.0
        for i, f in enumerate(flujos):
            den = (1 + t) ** i
            v += f / den
            if i > 0:
                dv += -i * f / ((1 + t) ** (i + 1))
        if abs(v) < 1e-10:
            return t
        if abs(dv) < 1e-12:
            break
        t_new = t - v / dv
        if abs(t_new - t) < 1e-10:
            return t_new
        t = t_new
    return t


def calcular_manual(params: dict) -> dict:
    """Recalculo independiente: devuelve KPIs por combinacion."""
    gfa = params["gfa_max_m2"]
    cl = _costo_lote(params["lote"])
    fin = params["financiero"]
    renta = params["renta"]
    reglas = params["reglas_renta"]
    h = int(renta["horizonte_anios"])
    inc_c = renta["incremento_canon_pct"] / 100.0
    inc_g = renta["incremento_gastos_pct"] / 100.0
    cap_sal = renta["cap_rate_salida_pct"] / 100.0
    tasa = reglas["tasa_descuento_pct"] / 100.0

    salida = {}
    for esc_id, esc in params["escenarios"].items():
        if esc.get("mix_usos"):
            comps = []
            for m in esc["mix_usos"]:
                gfa_i = gfa * m["pct_gfa"]
                nga_i = gfa_i * m["eficiencia_nga"]
                unid = int(nga_i // m["unidad_m2"])
                area_i = unid * m["unidad_m2"]
                comps.append({"area": area_i, "canon": m["canon_m2_mes"],
                              "costo": m["costo_construccion_m2"], "gfa_i": gfa_i,
                              "unidades": unid})
            area_mix = sum(c["area"] for c in comps)
            cd_mix = sum(c["gfa_i"] * c["costo"] for c in comps)
            esc_mix_flag = True
        else:
            esc_eff = esc
            cd_mix = None
            esc_mix_flag = False
            area_mix = None
        for estr_id, estr in params["estrategias"].items():
            if esc_mix_flag:
                canon = (sum(c["area"] * c["canon"][estr_id] for c in comps) / area_mix
                         if area_mix else 0.0)
                cd = cd_mix
            else:
                canon = esc_eff["canon_m2_mes"][estr_id]
                cd = gfa * esc_eff["costo_construccion_m2"]
            if area_mix is None:
                nga = gfa * esc_eff["eficiencia_nga"]
                unidades = int(nga // esc_eff["unidad_m2"])
                area_mix = unidades * esc_eff["unidad_m2"]
            ocup = estr["ocupacion_pct"] / 100.0
            adm_m2 = estr["administracion_m2_mes"]
            gastos_pct = (estr["gastos_operativos_pct_egi"] + estr["capex_pct_egi"]) / 100.0

            # Inversion
            cb = cd * fin["costos_blandos_pct"] / 100.0
            gpi_1 = area_mix * canon * 12.0
            mkt = gpi_1 * fin["marketing_leasing_pct"] / 100.0
            mob = area_mix * float(estr.get("mobiliario_cop_m2", 0.0))
            inv = cl + cd + cb + mkt + mob

            # Flujo anual
            nois = []
            for t in range(1, h + 1):
                gpi = area_mix * canon * 12.0 * (1 + inc_c) ** (t - 1)
                egi = gpi * ocup
                adm = area_mix * adm_m2 * 12.0 * (1 + inc_g) ** (t - 1)
                gastos = egi * gastos_pct
                nois.append(egi - adm - gastos)
            salida_activo = nois[-1] * (1 + inc_c) / cap_sal

            flujos = [-inv] + nois
            flujos[-1] += salida_activo

            vpn = _vp(flujos, tasa)
            tir = _tir_newton(flujos)
            vp_ing = _vp([0.0] + nois, tasa) + salida_activo / (1 + tasa) ** h
            suelo = max(0.0, vp_ing - (inv - cl))

            # Payback descontado
            acum = -inv
            pb_d = None
            for i, f in enumerate(flujos):
                if i == 0:
                    continue
                prev = acum
                acum += f / (1 + tasa) ** i
                if prev < 0 <= acum and pb_d is None:
                    pb_d = (i - 1) + (-prev) / (acum - prev)

            # Breakeven de ocupacion
            adm_1 = area_mix * adm_m2 * 12.0
            be = adm_1 / (gpi_1 * (1 - gastos_pct)) if gpi_1 * (1 - gastos_pct) > 0 else float("inf")

            salida[f"{estr_id}_{esc_id}"] = {
                "inversion": inv, "noi_1": nois[0], "gpi_1": gpi_1,
                "cap_rate": nois[0] / inv * 100.0,
                "tir": tir * 100.0, "vpn": vpn,
                "suelo_soportable": suelo, "pb_d": pb_d,
                "ocup_be": min(1.0, be) * 100.0,
                "cl_inv": cl / inv * 100.0,
                "multiplico": (sum(nois) + salida_activo) / inv,
            }
    return salida


def comparar(parametros_path: str, resultados_path: str) -> tuple:
    with open(parametros_path, "r", encoding="utf-8") as f:
        params = json.load(f)
    with open(resultados_path, "r", encoding="utf-8") as f:
        res = json.load(f)

    manual = calcular_manual(params)
    errores = []
    checks = 0

    for combo, m in manual.items():
        r = next((x for x in res["resultados"]
                  if f"{x['estrategia']}_{x['escenario_id']}" == combo), None)
        if r is None:
            errores.append(f"{combo}: sin resultado en el JSON del motor")
            continue
        parejas = [
            ("inversion_total_cop", m["inversion"]),
            ("noi_1_cop", m["noi_1"]),
            ("gpi_1_cop", m["gpi_1"]),
            ("VPN_cop", m["vpn"]),
            ("suelo_soportable_cop", m["suelo_soportable"]),
        ]
        for campo, val in parejas:
            checks += 1
            tol = max(abs(val) * TOL_MONTO, 1.0)
            if abs(r[campo] - val) > tol:
                errores.append(f"{combo}.{campo}: motor {r[campo]:.2f} vs manual {val:.2f}")
        checks += 1
        if abs(r["cap_rate_entrada_pct"] - m["cap_rate"]) > TOL_TIR:
            errores.append(f"{combo}.cap_rate: motor {r['cap_rate_entrada_pct']:.2f} vs manual {m['cap_rate']:.2f}")
        checks += 1
        if r["TIR_pct"] is not None and abs(r["TIR_pct"] - m["tir"]) > TOL_TIR:
            errores.append(f"{combo}.TIR: motor {r['TIR_pct']:.2f} vs manual {m['tir']:.2f}")
        checks += 1
        if r["CL_inversion_pct"] is not None and abs(r["CL_inversion_pct"] - m["cl_inv"]) > TOL_TIR:
            errores.append(f"{combo}.CL_inv: motor {r['CL_inversion_pct']:.2f} vs manual {m['cl_inv']:.2f}")
        checks += 1
        if r["multiplico_x"] is not None and abs(r["multiplico_x"] - m["multiplico"]) > TOL_TIR:
            errores.append(f"{combo}.multiplico: motor {r['multiplico_x']:.3f} vs manual {m['multiplico']:.3f}")
        if r["payback_descontado_anios"] is not None and m["pb_d"] is not None:
            checks += 1
            if abs(r["payback_descontado_anios"] - m["pb_d"]) > 0.2:
                errores.append(f"{combo}.pb_d: motor {r['payback_descontado_anios']:.2f} vs manual {m['pb_d']:.2f}")
        checks += 1
        if abs(r["ocupacion_breakeven_pct"] - m["ocup_be"]) > 0.5:
            errores.append(f"{combo}.ocup_be: motor {r['ocupacion_breakeven_pct']:.2f} vs manual {m['ocup_be']:.2f}")

    return checks, errores


def main() -> int:
    parser = argparse.ArgumentParser(description="Verificador independiente F2 Renta")
    parser.add_argument("--parametros", default="parametros_entrada.json")
    parser.add_argument("--resultados", default="resultados/resultados_completos.json")
    args = parser.parse_args()

    checks, errores = comparar(args.parametros, args.resultados)
    print("=" * 70)
    print("VERIFICACION INDEPENDIENTE — F2_RENTA_MOTOR_v03")
    print(f"  Parametros : {args.parametros}")
    print(f"  Resultados : {args.resultados}")
    print(f"  Chequeos   : {checks}")
    if errores:
        print(f"  ERRORES    : {len(errores)}")
        for e in errores[:20]:
            print(f"    - {e}")
        print("RESULTADO: FAIL")
        print("=" * 70)
        return 1
    print("  RESULTADO: PASS (todas las comparaciones dentro de tolerancia)")
    print("=" * 70)
    return 0


if __name__ == "__main__":
    sys.exit(main())
