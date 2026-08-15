# -*- coding: utf-8 -*-
"""
================================================================================
verificacion_independiente.py — Verificacion cruzada del modelo F2
================================================================================
Recalcula los KPIs de los 3 escenarios con formulas escritas a mano (independientes
del motor) y los contrasta contra resultados_completos.json generado por
F2_DEMANDA_MOTOR_v03.py. Funciona como la "hoja de calculo independiente" del
plan de verificacion: si todo PASS, el motor esta correcto.

USO:
  python verificacion_independiente.py [ruta_parametros] [ruta_resultados]

SALIDA:
  PASS/FAIL por escenario y por KPI, con diferencia relativa.
================================================================================
"""

import json
import os
import sys

TOL = 1e-6  # tolerancia relativa


def _cargar(ruta):
    with open(ruta, "r", encoding="utf-8") as f:
        return json.load(f)


def verificar(params_path, results_path):
    params = _cargar(params_path)
    paquete = _cargar(results_path)

    gfa = params["gfa_max_m2"]
    lote = params["lote"]
    fin = params["financiero"]
    if lote.get("costo_lote_total_cop"):
        cl = float(lote["costo_lote_total_cop"])
    else:
        cl = lote["area_m2"] * lote["precio_suelo_m2"] * (1 + lote["impuestos_escritura_pct"] / 100.0)

    ok_total = True
    print("=" * 70)
    print("VERIFICACION INDEPENDIENTE — F2 DEMANDA MOTOR")
    print(f"GFA={gfa} m2 | CL={cl:,.0f} COP | tolerancia relativa {TOL}")
    print("=" * 70)

    for esc_id, esc in params["escenarios"].items():
        # --- Recalculo manual (mismas reglas: unidades enteras floor) ---
        if esc.get("mix_usos"):
            nga = 0.0
            unidades = 0
            area_vendible = 0.0
            ingresos = 0.0
            costo_duro = 0.0
            abs_pond = 0.0
            for m in esc["mix_usos"]:
                gfa_i = gfa * m["pct_gfa"]
                nga_i = gfa_i * m["eficiencia_nga"]
                unid = int(nga_i // m["unidad_m2"])
                area_i = unid * m["unidad_m2"]
                nga += nga_i
                unidades += unid
                area_vendible += area_i
                ingresos += area_i * m["precio_venta_m2"]
                costo_duro += gfa_i * m["costo_construccion_m2"]
                abs_pond += unid / max(m.get("absorcion_unid_mes", 2.0), 0.1)
            absorcion = unidades / abs_pond if abs_pond > 0 else 0.0
        else:
            nga = gfa * esc["eficiencia_nga"]
            unidades = int(nga // esc["unidad_m2"])
            area_vendible = unidades * esc["unidad_m2"]
            ingresos = area_vendible * esc["precio_venta_m2"]
            costo_duro = gfa * esc["costo_construccion_m2"]
            absorcion = esc["absorcion_unid_mes"]

        costo_blando = costo_duro * fin["costos_blandos_pct"] / 100.0
        costo_mkt = ingresos * fin["marketing_ventas_pct"] / 100.0
        costo_total = cl + costo_duro + costo_blando + costo_mkt
        utilidad = ingresos - costo_total

        mub = utilidad / ingresos * 100.0 if ingresos else 0.0
        roi = utilidad / costo_total * 100.0 if costo_total else 0.0
        cl_it = cl / ingresos * 100.0 if ingresos else 0.0
        meses = unidades / absorcion if absorcion else float("inf")

        esperado = {
            "nga_m2": nga, "num_unidades": unidades, "area_vendible_m2": area_vendible,
            "ingresos_totales_cop": ingresos, "costo_duro_cop": costo_duro,
            "costo_blando_cop": costo_blando, "costo_mkt_cop": costo_mkt,
            "costo_total_cop": costo_total, "utilidad_bruta_cop": utilidad,
            "MUB_pct": mub, "ROI_pct": roi, "CL_IT_pct": cl_it,
            "meses_venta_estimados": meses,
        }

        motor = next(r for r in paquete["escenarios"] if r["escenario_id"] == esc_id)
        print(f"\nEscenario: {motor['producto']}")
        fallas = []
        for campo, val_esp in esperado.items():
            val_motor = motor[campo]
            # El motor redondea a 2 decimales al guardar (1 en meses_venta);
            # comparar contra el mismo redondeo para evitar falsos FAIL por precision.
            dec = 1 if campo == "meses_venta_estimados" else 2
            val_esp_red = round(val_esp, dec)
            dif = abs(val_esp_red - val_motor) / max(abs(val_esp_red), 1e-9)
            marca = "PASS" if dif <= TOL else "FAIL"
            if marca == "FAIL":
                fallas.append(campo)
            print(f"  [{marca}] {campo:<24} manual={val_esp_red:>16,.2f}  motor={val_motor:>16,.2f}  "
                  f"diff={dif:.2e}")

        # Verificacion adicional: CL en el paquete
        if "costo_lote_total_cop" in paquete:
            dif_cl = abs(round(cl, 2) - paquete["costo_lote_total_cop"]) / max(abs(round(cl, 2)), 1e-9)
            marca = "PASS" if dif_cl <= TOL else "FAIL"
            if marca == "FAIL":
                fallas.append("costo_lote_total")
            print(f"  [{marca}] {'costo_lote_total_cop':<24} manual={round(cl, 2):>16,.2f}  "
                  f"motor={paquete['costo_lote_total_cop']:>16,.2f}  diff={dif_cl:.2e}")

        if fallas:
            ok_total = False
            print(f"  >>> ESCENARIO CON FALLAS: {fallas}")

    # Verificacion de consistencia de alertas: caso base debe tener al menos una
    # alerta critica si el KPI viola una regla.
    reglas = params["reglas_decision"]
    print("\nVerificacion de alertas (reglas de decision):")
    for r in paquete["escenarios"]:
        alertas = paquete["alertas"].get(r["escenario_id"], [])
        criticas = [a for a in alertas if a["nivel"] == "critica"]
        viola = (r["MUB_pct"] < reglas["mub_riesgo_pct"] or
                 r["ROI_pct"] < reglas["roi_minimo_pct"] or
                 r["CL_IT_pct"] > reglas["cl_it_inviable_pct"])
        if viola and not criticas:
            ok_total = False
            print(f"  [FAIL] {r['producto']}: viola reglas pero no tiene alerta critica")
        elif not viola and criticas:
            ok_total = False
            print(f"  [FAIL] {r['producto']}: tiene alerta critica sin violar reglas")
        else:
            print(f"  [PASS] {r['producto']}: alertas criticas={len(criticas)} consistentes")

    print("\n" + "=" * 70)
    print("RESULTADO GLOBAL:", "PASS" if ok_total else "FAIL")
    print("=" * 70)
    return 0 if ok_total else 1


if __name__ == "__main__":
    base = os.path.dirname(os.path.abspath(__file__))
    params_path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(base, "parametros_entrada.json")
    results_path = sys.argv[2] if len(sys.argv) > 2 else os.path.join(base, "resultados", "resultados_completos.json")
    sys.exit(verificar(params_path, results_path))
