# -*- coding: utf-8 -*-
"""
generar_casos_pipeline.py — Genera los JSON de entrada del pipeline (data/fase-2-demanda)
para los casos de estudio del ejercicio 2026-08-14 (AAA0127AZPA GFA 1053, AAA0030JKOE
La Candelaria, AAA0039KRMR Muzu). El lote 002407033006 (Venecia-sur) fue EXCLUIDO del
ejercicio por decision del usuario (2026-08-14).

Formato identico al consumido por F2_DEMANDA_MOTOR_v01.py (pipeline) y por el motor
financiero mejorado. Formulas del pipeline: NGA = GFA x eficiencia; unidades enteras;
IT = area_vendible x precio; CD = GFA x costo; CB = 15% CD; CMV = 4% IT.

USO:  python scripts/utilities/generar_casos_pipeline.py
"""
import json
import os

CASOS = [
    {
        "chip": "AAA0127AZPA",
        "archivo": "AAA0127AZPA-prefactibilidad-gfa1053-cl550.json",
        "gfa": 1053.0,
        "costo_lote": 550_000_000.0,
        "nota": "Caso de estudio 2026-08-14: GFA 1053 m2 y CL $550 M (ejercicio del usuario). "
                "Precios validados con comparables Prado Veraniego (2026-08-13).",
        "escenarios": [
            {"producto": "VIS", "unidad": 55.0, "eficiencia": 0.8,
             "precio": 4_727_444, "costo": 2_300_000},
            {"producto": "Estandar", "unidad": 85.0, "eficiencia": 0.75,
             "precio": 6_800_000, "costo": 3_000_000},
            {"producto": "Lujo", "unidad": 150.0, "eficiencia": 0.7,
             "precio": 9_500_000, "costo": 4_300_000},
        ],
    },
    {
        "chip": "AAA0030JKOE",
        "archivo": "AAA0030JKOE-prefactibilidad.json",
        "gfa": 3312.575,  # 946,45 m2 x IO 0,7 x 5 pisos (Decreto 492/07, norma-manual)
        "costo_lote": 1_420_000_000.0,
        "nota": "Caso de estudio 2026-08-14: lote real La Candelaria (UPZ 94), GFA normativo "
                "= 946,45 m2 x 0,7 x 5 pisos = 3.312,6 m2. CL supuesto de ejercicio $1.420 M "
                "(~$1,5 M/m2, suelo centro historico). Precios/costos con sobrecosto de "
                "restauracion (supuestos de ejercicio documentados).",
        "escenarios": [
            {"producto": "VIS", "unidad": 55.0, "eficiencia": 0.8,
             "precio": 4_727_444, "costo": 2_600_000},
            {"producto": "Estandar", "unidad": 85.0, "eficiencia": 0.75,
             "precio": 7_500_000, "costo": 3_400_000},
            {"producto": "Lujo", "unidad": 150.0, "eficiencia": 0.7,
             "precio": 10_500_000, "costo": 4_800_000},
        ],
    },
    {
        "chip": "AAA0039KRMR",
        "archivo": "AAA0039KRMR-prefactibilidad.json",
        "gfa": 1100.0,  # 356,96 m2 x IC 3,08 (altura max GDB 26,6 m; rango '1' inconsistente -> supuesto ejercicio)
        "costo_lote": 700_000_000.0,
        "nota": "Caso de estudio 2026-08-14: lote real AAA0039KRMR (UPZ Muzu, Puente Aranda; "
                "356,96 m2; Consolidacion). GFA 1.100 m2 (supuesto de ejercicio). CL $700 M "
                "(~$1,96 M/m2, supuesto de ejercicio). Zona de actividad multiple; precios/"
                "canones de zona (supuestos de ejercicio documentados).",
        "escenarios": [
            {"producto": "VIS", "unidad": 55.0, "eficiencia": 0.8,
             "precio": 4_300_000, "costo": 2_600_000},
            {"producto": "Estandar", "unidad": 70.0, "eficiencia": 0.75,
             "precio": 5_800_000, "costo": 3_000_000},
            {"producto": "Lujo", "unidad": 120.0, "eficiencia": 0.7,
             "precio": 7_200_000, "costo": 3_800_000},
        ],
    },
]


def main() -> int:
    out_dir = os.path.join(os.path.dirname(__file__), "..", "..", "data", "fase-2-demanda")
    out_dir = os.path.normpath(out_dir)
    for caso in CASOS:
        escs = []
        for s in caso["escenarios"]:
            nga = caso["gfa"] * s["eficiencia"]
            unidades = int(nga // s["unidad"])
            area = unidades * s["unidad"]
            it = area * s["precio"]
            cd = caso["gfa"] * s["costo"]
            cb = cd * 0.15
            cmv = it * 0.04
            ctd = caso["costo_lote"] + cd + cb + cmv
            ub = it - ctd
            escs.append({
                "producto": s["producto"],
                "gfa_m2": round(caso["gfa"], 2),
                "nga_m2": round(nga, 2),
                "num_unidades": unidades,
                "tamano_unidad_m2": s["unidad"],
                "ingresos_totales_cop": round(it, 2),
                "costo_lote_cop": caso["costo_lote"],
                "costo_duro_cop": round(cd, 2),
                "costo_blando_cop": round(cb, 2),
                "costo_mkt_cop": round(cmv, 2),
                "costo_total_cop": round(ctd, 2),
                "utilidad_bruta_cop": round(ub, 2),
                "KPIs": {
                    "MUB_pct": round(ub / it * 100, 2) if it else 0.0,
                    "ROI_pct": round(ub / ctd * 100, 2) if ctd else 0.0,
                    "Lote_sobre_Ventas_pct": round(caso["costo_lote"] / it * 100, 2) if it else 0.0,
                },
            })
        doc = {
            "chip": caso["chip"],
            "gfa_maximo_evaluado": caso["gfa"],
            "costo_lote_input": caso["costo_lote"],
            "nota": caso["nota"],
            "escenarios": escs,
        }
        ruta = os.path.join(out_dir, caso["archivo"])
        with open(ruta, "w", encoding="utf-8") as f:
            json.dump(doc, f, ensure_ascii=False, indent=4)
        print(f"OK {caso['archivo']} ({len(escs)} escenarios)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
