# -*- coding: utf-8 -*-
"""
================================================================================
actualizar_casos_renta.py — Utilidad: prepara JSONs de renta de los casos
================================================================================
1) Crea parametros_AAA0039KRMR_renta.json (caso C, UPZ Muzu) con escenario
   D_MIXTO (USO-MULTIPLE, override de usuario) y referencia_venta.
2) Anade D_MIXTO y actualiza referencia_venta en los JSONs de renta de
   AAA0127AZPA y AAA0030JKOE, leyendo los resultados de venta regenerados.

USO:
  python actualizar_casos_renta.py

Requiere los resultados de venta ya corridos:
  ../F2_Modelo_Financiero/resultados/resultados_AAA0127AZPA_gfa1053_cl550.json
  ../F2_Modelo_Financiero/resultados/resultados_AAA0030JKOE.json
  ../F2_Modelo_Financiero/resultados/resultados_AAA0039KRMR.json
================================================================================
"""

import io
import json
import os
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
VENTA = os.path.join(BASE, "..", "..", "src", "fase-2-demanda", "F2_Modelo_Financiero", "resultados")
RENTA = os.path.join(BASE, "..", "..", "src", "fase-2-demanda", "F2_Modelo_Renta")

# Escenarios de sensibilidad salud/oficinas (mismo modulo que los anade a venta)
sys.path.insert(0, BASE)
from agregar_sensibilidad_salud_oficinas import CASOS as CASOS_SENS
from agregar_sensibilidad_salud_oficinas import _mix_salud, _mix_oficinas  # noqa: E402


SENS_KEY = ("D_MIXTO_SALUD", "D_MIXTO_OFICINAS")


def anadir_sensibilidad(data, chip):
    c = CASOS_SENS[chip]
    for key, fn in zip(SENS_KEY, (_mix_salud, _mix_oficinas)):
        if key not in data["escenarios"]:
            data["escenarios"][key] = fn(c, "renta")
    return data


def resumen_venta(path_resultados, nota):
    with io.open(path_resultados, "r", encoding="utf-8") as f:
        paquete = json.load(f)
    escs = {}
    for r in paquete["escenarios"]:
        escs[r["escenario_id"]] = {
            "nombre": r["producto"],
            "ROI_venta_pct": r["ROI_pct"],
            "MUB_venta_pct": r["MUB_pct"],
            "CL_IT_pct": r["CL_IT_pct"],
            "estado": r.get("estado", "NO VIABLE"),
        }
    return {"nota": nota, "escenarios": escs}


D_MIXTO_RENTA = {
    "A": {
        "nombre": "D - Mixto (override usuario)",
        "nota": "USO-MULTIPLE: override de usuario fuera de reglamentacion. Mix 20% local comercial + 80% vivienda estandar (Prado Veraniego). Cánones LP: vivienda validada $30.000/m2/mes; local supuesto $45.000. CP = x1,7.",
        "override_uso": True,
        "mix_usos": [
            {"uso": "Local comercial", "pct_gfa": 0.20, "unidad_m2": 50.0, "eficiencia_nga": 0.85,
             "costo_construccion_m2": 3600000, "canon_m2_mes": {"CP": 76500, "LP": 45000},
             "fuente": "Local Prado Veraniego LP $45.000/m2/mes (supuesto de ejercicio)."},
            {"uso": "Vivienda estandar", "pct_gfa": 0.80, "unidad_m2": 65.0, "eficiencia_nga": 0.78,
             "costo_construccion_m2": 3000000, "canon_m2_mes": {"CP": 51000, "LP": 30000},
             "fuente": "Canon validado 2026-08-13: LP $30.000/m2/mes."},
        ],
        "fuente_canon": "Supuestos de ejercicio 2026-08-14 (mix uso multiple).",
        "fuente_costo": "Supuestos de ejercicio 2026-08-14 (local $3,6 M/m2, vivienda $3,0 M/m2).",
    },
    "B": {
        "nombre": "D - Mixto (override usuario)",
        "nota": "USO-MULTIPLE: override de usuario fuera de reglamentacion. Mix 30% local comercial turistico + 70% vivienda estandar (La Candelaria, sobrecosto restauracion). Canones ajustados a comparables 2026-08-14.",
        "override_uso": True,
        "mix_usos": [
            {"uso": "Local comercial turistico", "pct_gfa": 0.30, "unidad_m2": 40.0, "eficiencia_nga": 0.85,
             "costo_construccion_m2": 4500000, "canon_m2_mes": {"CP": 70000, "LP": 42000},
             "fuente": "Local centro historico LP $42.000/m2/mes (supuesto de ejercicio)."},
            {"uso": "Vivienda estandar", "pct_gfa": 0.70, "unidad_m2": 55.0, "eficiencia_nga": 0.75,
             "costo_construccion_m2": 4000000, "canon_m2_mes": {"CP": 74800, "LP": 44000},
             "fuente": "Vivienda centro historico LP $44.000/m2/mes (apartaestudios turisticos 2026-08-14)."},
        ],
        "fuente_canon": "Comparables 2026-08-14 + supuestos (mix uso multiple).",
        "fuente_costo": "Supuestos de ejercicio 2026-08-14 (local restauracion $4,5 M/m2, vivienda $4,0 M/m2).",
    },
    "C": {
        "nombre": "D - Mixto (override usuario)",
        "nota": "USO-MULTIPLE: override de usuario fuera de reglamentacion. Mix 35% local comercial + 65% vivienda VIS (Muzu/Puente Aranda). Canones validados 2026-08-14.",
        "override_uso": True,
        "mix_usos": [
            {"uso": "Local comercial", "pct_gfa": 0.35, "unidad_m2": 60.0, "eficiencia_nga": 0.85,
             "costo_construccion_m2": 3200000, "canon_m2_mes": {"CP": 85000, "LP": 50000},
             "fuente": "Local Muzu LP $50.000/m2/mes (supuesto sobre media zona 2026-08-14)."},
            {"uso": "Vivienda VIS", "pct_gfa": 0.65, "unidad_m2": 55.0, "eficiencia_nga": 0.80,
             "costo_construccion_m2": 2600000, "canon_m2_mes": {"CP": 51000, "LP": 30000},
             "fuente": "Vivienda VIS Muzu LP $30.000/m2/mes (Properati jul-2026)."},
        ],
        "fuente_canon": "Comparables 2026-08-14 (Properati Puente Aranda $36.066/m2/mes; VIS -15%).",
        "fuente_costo": "Supuestos de ejercicio 2026-08-14 (local $3,2 M/m2, vivienda $2,6 M/m2).",
    },
}


def crear_caso_C():
    path = os.path.join(RENTA, "parametros_AAA0039KRMR_renta.json")
    data = {
        "meta": {
            "modelo": "F2_RENTA_MOTOR_v03",
            "version": "1.0",
            "fase": "Prefactibilidad (Fase 2) - Modelo Build-to-Rent (BTR)",
            "ciudad": "Bogota D.C., Colombia",
            "moneda": "COP",
            "fecha_ejecucion": "2026-08-14",
            "chip": "AAA0039KRMR-MUZU",
            "horizonte_anios": 10,
            "origen_datos": "Lote real AAA0039KRMR (UPZ MUZU - Puente Aranda; area 356,96 m2; tratamiento Consolidacion). GFA de ejercicio 1.100 m2 (IC 3,08; rango '1' de la GDB inconsistente con altura maxima 26,6 m segun ADR-005 -> revision F1).",
            "nota_general": "Caso de estudio 2026-08-14 (ejercicio). Incluye D_MIXTO (USO-MULTIPLE, override de usuario fuera de reglamentacion) y escenarios de sensibilidad salud/oficinas. Canones VIS/Estandar validados 2026-08-14 (Properati); el resto supuestos de ejercicio documentados."
        },
        "gfa_max_m2": 1100.0,
        "lote": {
            "area_m2": 356.96,
            "precio_suelo_m2": 1961000.0,
            "impuestos_escritura_pct": 0.0,
            "costo_lote_total_cop": 700000000.0,
            "fuente": "CL $700.000.000 COP = supuesto de ejercicio (~$1,96 M/m2 de suelo, Muzu/Puente Aranda 2026).",
            "fuente_url": "D:\\Work\\PROJECTS\\DiseñoParametrico\\data\\pot-cache\\AAA0039KRMR-contexto.json"
        },
        "financiero": {"costos_blandos_pct": 15.0, "marketing_leasing_pct": 2.0},
        "renta": {"horizonte_anios": 10, "incremento_canon_pct": 5.5,
                  "incremento_gastos_pct": 6.5, "cap_rate_salida_pct": 6.2},
        "reglas_renta": {"tasa_descuento_pct": 10.0, "tir_minima_pct": 10.0,
                         "cap_rate_entrada_min_pct": 5.0, "payback_max_anios": 8.0,
                         "cl_inversion_precaucion_pct": 25.0, "cl_inversion_inviable_pct": 30.0},
        "sensibilidad": {"variacion_pct": 10.0},
        "estrategias": {
            "CP": {"nombre": "Corto plazo - temporal amoblado", "ocupacion_pct": 75.0,
                   "administracion_m2_mes": 8000.0, "gastos_operativos_pct_egi": 25.0,
                   "capex_pct_egi": 3.0, "mobiliario_cop_m2": 500000.0,
                   "nota": "Base del modelo (75%)."},
            "LP": {"nombre": "Largo plazo - arriendo tradicional", "ocupacion_pct": 95.0,
                   "administracion_m2_mes": 6000.0, "gastos_operativos_pct_egi": 12.0,
                   "capex_pct_egi": 1.0, "mobiliario_cop_m2": 0.0,
                   "nota": "Base del modelo (95%)."},
        },
        "escenarios": {
            "A_VIS": {"nombre": "A - VIS / VIP", "unidad_m2": 55.0, "eficiencia_nga": 0.8,
                      "costo_construccion_m2": 2600000.0,
                      "canon_m2_mes": {"CP": 51000.0, "LP": 30000.0},
                      "fuente_canon": "Validado 2026-08-14: Properati jul-2026 Puente Aranda $36.066/m2/mes; VIS ~ -15% -> $30.000 LP. CP = x1,7.",
                      "fuente_canon_url": "https://www.properati.com.co/s/puente-aranda-bogota-d-c/apartamento/arriendo",
                      "fuente_costo": "Konstruing: $2,6 M/m2 (supuesto de ejercicio).",
                      "fuente_costo_url": "https://konstruing.com.co/blog/cuanto-cuesta-construir-casa-bogota-2026.html",
                      "nota": "Canon validado con comparable 2026-08-14 (antes $18.000 LP)."},
            "B_ESTANDAR": {"nombre": "B - Estandar", "unidad_m2": 70.0, "eficiencia_nga": 0.75,
                           "costo_construccion_m2": 3000000.0,
                           "canon_m2_mes": {"CP": 61200.0, "LP": 36000.0},
                           "fuente_canon": "Validado 2026-08-14: Properati jul-2026 Puente Aranda $36.066/m2/mes. CP = x1,7.",
                           "fuente_canon_url": "https://www.properati.com.co/s/puente-aranda-bogota-d-c/apartamento/arriendo",
                           "fuente_costo": "Konstruing: $3,0 M/m2 (supuesto de ejercicio).",
                           "fuente_costo_url": "https://konstruing.com.co/blog/cuanto-cuesta-construir-casa-bogota-2026.html",
                           "nota": "Canon validado con comparable 2026-08-14 (antes $22.000 LP)."},
            "C_LUJO": {"nombre": "C - Lujo / Alto nivel", "unidad_m2": 120.0, "eficiencia_nga": 0.7,
                       "costo_construccion_m2": 3800000.0,
                       "canon_m2_mes": {"CP": 76500.0, "LP": 45000.0},
                       "fuente_canon": "Premium +25% sobre media Properati jul-2026 ($45.000 LP; antes $32.000). CP = x1,7.",
                       "fuente_canon_url": "https://www.properati.com.co/s/puente-aranda-bogota-d-c/apartamento/arriendo",
                       "fuente_costo": "Konstruing premium: $3,8 M/m2 (supuesto de ejercicio).",
                       "fuente_costo_url": "https://konstruing.com.co/blog/cuanto-cuesta-construir-casa-bogota-2026.html",
                       "nota": "Ajustado 2026-08-14 al comparable de zona."},
            "D_MIXTO": dict(D_MIXTO_RENTA["C"]),
        },
    }
    ref_path = os.path.join(VENTA, "resultados_AAA0039KRMR.json")
    data["referencia_venta"] = resumen_venta(
        ref_path,
        "KPIs del modelo de venta F2 (corrida 2026-08-14 con precios validados): ningun escenario viable (CL $700 M alto para GFA 1.100 m2; mejor D_MIXTO ROI -7,1%). La renta es la alternativa a explorar (LP x D_MIXTO / D_MIXTO_SALUD viables).")
    with io.open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print("OK creado:", path)


def actualizar_A_B():
    pares = [
        ("parametros_AAA0127AZPA_renta_gfa1053_cl550.json", "resultados_AAA0127AZPA_gfa1053_cl550.json", "A",
         "KPIs del modelo de venta F2 (corrida 2026-08-14 con D_MIXTO): B estandar 18,5% NO viable; D_MIXTO VIABLE (ROI 26,6%). La renta sigue siendo la recomendacion (LP x A, TIR 11,1%)."),
        ("parametros_AAA0030JKOE_renta.json", "resultados_AAA0030JKOE.json", "B",
         "KPIs del modelo de venta F2 (corrida 2026-08-14 con D_MIXTO): B estandar VIABLE (ROI 22,3%); D_MIXTO NO viable (ROI -8,6% por sobrecosto restauracion)."),
    ]
    for fname, res_name, key, nota in pares:
        path = os.path.join(RENTA, fname)
        with io.open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        data["escenarios"]["D_MIXTO"] = D_MIXTO_RENTA[key]
        data["referencia_venta"] = resumen_venta(os.path.join(VENTA, res_name), nota)
        with io.open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print("OK actualizado:", fname)


if __name__ == "__main__":
    crear_caso_C()
    actualizar_A_B()
    # Escenarios de sensibilidad salud/oficinas (idempotente)
    for fname, chip in [
        ("parametros_AAA0127AZPA_renta_gfa1053_cl550.json", "AAA0127AZPA"),
        ("parametros_AAA0030JKOE_renta.json", "AAA0030JKOE"),
        ("parametros_AAA0039KRMR_renta.json", "AAA0039KRMR"),
    ]:
        path = os.path.join(RENTA, fname)
        with io.open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        data = anadir_sensibilidad(data, chip)
        with io.open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print("OK sensibilidad:", fname)
