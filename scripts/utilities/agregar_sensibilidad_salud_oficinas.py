# -*- coding: utf-8 -*-
"""Añade escenarios de sensibilidad D_MIXTO_SALUD y D_MIXTO_OFICINAS a los JSONs de
parámetros de los 3 casos (venta y renta). Idempotente: no duplica si ya existen.

Fuentes de la sensibilidad (consultadas 2026-08-14):
- Consultorios Bogotá: FincaRaíz promedio $5,14 M/mes en 37 m2 (~$139k/m2/mes);
  MercadoLibre $3,5 M en 35 m2 (~$100k), Chicó $3,3 M en 24 m2 (~$137k);
  Ciencuadras Marly $1,55 M en 25 m2 (~$62k); SaludTools frecuente $1,8-3,2 M
  (~$45-80k/m2/mes en 30-40 m2). Zona no-prime (Suba/Muzu): $55.000/m2/mes LP.
  Candelaria (central/turistica): $60.000.
- Oficinas Bogotá: clase A $82.683/m2/mes (Q3-2025, RentOfficeToday); prime
  $88.300 con vacancia <1% (ValoraAnalitik 2026); no-prime: $38.000 (referencia).
- Precios de venta derivados del canon (cap rate implicito 7,5-8,5%), etiquetados
  como supuestos: consultorio $6,5-7,5 M/m2; oficina $5,5-6,0 M/m2.
- Costo consultorio = estandar x1,10 (instalaciones medicas: gases, redes).
- CP = LP para salud/oficinas: el temporal amoblado no aplica a estos usos.
"""
import io
import json
import os

BASE = os.path.join(os.path.dirname(__file__), "..", "..")
FIN = os.path.normpath(os.path.join(BASE, "src", "fase-2-demanda", "F2_Modelo_Financiero"))
REN = os.path.normpath(os.path.join(BASE, "src", "fase-2-demanda", "F2_Modelo_Renta"))

# Parámetros por caso: vivienda del D_MIXTO base (uso, pct, precio, canon LP, costo)
CASOS = {
    "AAA0127AZPA": {  # El Prado, Suba — vivienda ESTANDAR (como el D_MIXTO base del caso)
        "vivienda": {"uso": "Vivienda estandar", "unidad_m2": 65.0, "eficiencia_nga": 0.78,
                     "precio_venta_m2": 6800000, "canon_lp": 30000,
                     "costo_construccion_m2": 3000000},
        "consultorio": {"precio_venta_m2": 6500000, "canon_lp": 55000},
        "oficina": {"precio_venta_m2": 5500000, "canon_lp": 38000},
    },
    "AAA0030JKOE": {  # Candelaria — vivienda estandar (centro historico)
        "vivienda": {"uso": "Vivienda estandar", "unidad_m2": 70.0, "eficiencia_nga": 0.75,
                     "precio_venta_m2": 7500000, "canon_lp": 44000,
                     "costo_construccion_m2": 3000000},
        "consultorio": {"precio_venta_m2": 7500000, "canon_lp": 60000},
        "oficina": {"precio_venta_m2": 6000000, "canon_lp": 38000},
    },
    "AAA0039KRMR": {  # Muzu — vivienda VIS
        "vivienda": {"uso": "Vivienda VIS", "unidad_m2": 55.0, "eficiencia_nga": 0.80,
                     "precio_venta_m2": 4300000, "canon_lp": 30000,
                     "costo_construccion_m2": 2600000},
        "consultorio": {"precio_venta_m2": 6500000, "canon_lp": 55000},
        "oficina": {"precio_venta_m2": 5500000, "canon_lp": 38000},
    },
}

NOTA = ("SENSIBILIDAD 2026-08-14: sin comparable directo en la UPZ; rango ciudad: "
        "consultorios $45-140k/m2/mes (FincaRaiz, MercadoLibre, Ciencuadras, SaludTools) y "
        "oficinas clase A $82,7k / prime $88,3k (RentOfficeToday, ValoraAnalitik Q3-2025); "
        "se usa valor no-prime. Precio de venta derivado del canon (cap rate implicito "
        "7,5-8,5%). Costo consultorio = estandar x1,10 (instalaciones medicas). "
        "CP = LP: el temporal amoblado no aplica a salud/oficinas.")


def _mix_salud(c, modo):
    viv = c["vivienda"]
    cons = c["consultorio"]
    comps = [
        {"uso": "Consultorios (salud)", "pct_gfa": 0.25, "unidad_m2": 40.0,
         "eficiencia_nga": 0.75,
         "costo_construccion_m2": round(viv["costo_construccion_m2"] * 1.10, -5),
         "fuente": "Consultorios: canon no-prime $55-60k/m2/mes (rango ciudad 2026, ver nota)."},
        {"uso": viv["uso"], "pct_gfa": 0.75, "unidad_m2": viv["unidad_m2"],
         "eficiencia_nga": viv["eficiencia_nga"],
         "costo_construccion_m2": viv["costo_construccion_m2"],
         "fuente": "Vivienda del caso (canon/precio validado 2026-08-14)."},
    ]
    if modo == "venta":
        comps[0]["precio_venta_m2"] = cons["precio_venta_m2"]
        comps[0]["absorcion_unid_mes"] = 1.0
        comps[1]["precio_venta_m2"] = viv["precio_venta_m2"]
        comps[1]["absorcion_unid_mes"] = 2.5
        return {
            "nombre": "D - Mixto Salud (sensibilidad)",
            "nivel_acabados": "Mixto",
            "nota": "USO-MULTIPLE + componente de salud (override fuera de reglamentacion). " + NOTA,
            "override_uso": True, "sensibilidad": "salud/oficinas",
            "mix_usos": comps,
            "fuente_precio": "Precios de sensibilidad 2026-08-14 (consultorio derivado del canon; vivienda del caso).",
            "fuente_costo": "Costo consultorio = estandar x1,10 (instalaciones medicas); vivienda del caso.",
        }
    comps[0]["canon_m2_mes"] = {"CP": cons["canon_lp"], "LP": cons["canon_lp"]}
    comps[1]["canon_m2_mes"] = {"CP": round(viv["canon_lp"] * 1.7), "LP": viv["canon_lp"]}
    return {
        "nombre": "D - Mixto Salud (sensibilidad)",
        "nota": "USO-MULTIPLE + componente de salud (override fuera de reglamentacion). " + NOTA,
        "override_uso": True, "sensibilidad": "salud/oficinas",
        "mix_usos": comps,
        "fuente_canon": "Canones de sensibilidad 2026-08-14 (consultorio rango ciudad; vivienda del caso).",
        "fuente_costo": "Costo consultorio = estandar x1,10 (instalaciones medicas); vivienda del caso.",
    }


def _mix_oficinas(c, modo):
    viv = c["vivienda"]
    ofi = c["oficina"]
    comps = [
        {"uso": "Oficinas (servicios)", "pct_gfa": 0.25, "unidad_m2": 60.0,
         "eficiencia_nga": 0.80,
         "costo_construccion_m2": viv["costo_construccion_m2"],
         "fuente": "Oficinas: canon no-prime $38.000/m2/mes (clase A $82,7k, ver nota)."},
        {"uso": viv["uso"], "pct_gfa": 0.75, "unidad_m2": viv["unidad_m2"],
         "eficiencia_nga": viv["eficiencia_nga"],
         "costo_construccion_m2": viv["costo_construccion_m2"],
         "fuente": "Vivienda del caso (canon/precio validado 2026-08-14)."},
    ]
    if modo == "venta":
        comps[0]["precio_venta_m2"] = ofi["precio_venta_m2"]
        comps[0]["absorcion_unid_mes"] = 0.5
        comps[1]["precio_venta_m2"] = viv["precio_venta_m2"]
        comps[1]["absorcion_unid_mes"] = 2.5
        return {
            "nombre": "D - Mixto Oficinas (sensibilidad)",
            "nivel_acabados": "Mixto",
            "nota": "USO-MULTIPLE + componente de oficinas (override fuera de reglamentacion). " + NOTA,
            "override_uso": True, "sensibilidad": "salud/oficinas",
            "mix_usos": comps,
            "fuente_precio": "Precios de sensibilidad 2026-08-14 (oficina derivado del canon; vivienda del caso).",
            "fuente_costo": "Costo de vivienda del caso (oficina sin sobrecosto).",
        }
    comps[0]["canon_m2_mes"] = {"CP": ofi["canon_lp"], "LP": ofi["canon_lp"]}
    comps[1]["canon_m2_mes"] = {"CP": round(viv["canon_lp"] * 1.7), "LP": viv["canon_lp"]}
    return {
        "nombre": "D - Mixto Oficinas (sensibilidad)",
        "nota": "USO-MULTIPLE + componente de oficinas (override fuera de reglamentacion). " + NOTA,
        "override_uso": True, "sensibilidad": "salud/oficinas",
        "mix_usos": comps,
        "fuente_canon": "Canones de sensibilidad 2026-08-14 (oficina no-prime; vivienda del caso).",
        "fuente_costo": "Costo de vivienda del caso (oficina sin sobrecosto).",
    }


def _mix_institucional(c, modo):
    """D_MIXTO_INSTITUCIONAL: 30% GFA institucional salud (laboratorio/IPS) + 70% vivienda VIS.
    Solo aplica al caso A (clúster de salud real de El Prado/Prado Veraniego, verificado
    2026-08-14 con capa oficial de IPS y comparables FincaRaíz del barrio $61,5-88k/m2/mes)."""
    viv = c["vivienda"]
    comp = {"uso": "Institucional salud (laboratorio/IPS)", "pct_gfa": 0.30,
            "unidad_m2": 300.0, "eficiencia_nga": 0.75,
            "costo_construccion_m2": round(viv["costo_construccion_m2"] * 1.15, -5),
            "fuente": "Canon LP $60.000/m2/mes: comparables consultorios Prado Veraniego "
                      "$61,5-88k/m2/mes (FincaRaiz 2026-08-14), descuento ~20% por escala "
                      "(areas >= 300 m2, contratos largos). Costo x1,15 (instalaciones de laboratorio)."}
    comp2 = {"uso": viv["uso"], "pct_gfa": 0.70, "unidad_m2": viv["unidad_m2"],
             "eficiencia_nga": viv["eficiencia_nga"],
             "costo_construccion_m2": viv["costo_construccion_m2"],
             "fuente": "Vivienda del caso (canon/precio validado 2026-08-14)."}
    if modo == "venta":
        comp["precio_venta_m2"] = 7000000
        comp["absorcion_unid_mes"] = 0.25
        comp2["precio_venta_m2"] = viv["precio_venta_m2"]
        comp2["absorcion_unid_mes"] = 2.5
        return {"nombre": "D - Mixto Institucional Salud (sensibilidad)",
                "nivel_acabados": "Mixto",
                "nota": "USO-MULTIPLE + institucional salud (laboratorio/IPS). Mercado real del "
                        "barrio: 2 IPS < 200 m y 8 < 500 m (capa oficial Datos Abiertos Bogota "
                        "2026-08-14), 5+ hogares geriatricos < 200 m (levantamiento del usuario). "
                        "Precio de venta derivado del canon (cap rate implicito ~10%).",
                "override_uso": True, "sensibilidad": "salud-institucional",
                "mix_usos": [comp, comp2],
                "fuente_precio": "Institucional salud $7,0 M/m2 derivado del canon 60.000x12/0,10; vivienda del caso.",
                "fuente_costo": "Institucional = estandar x1,15 (instalaciones de laboratorio)."}
    comp["canon_m2_mes"] = {"CP": 60000, "LP": 60000}
    comp2["canon_m2_mes"] = {"CP": round(viv["canon_lp"] * 1.7), "LP": viv["canon_lp"]}
    return {"nombre": "D - Mixto Institucional Salud (sensibilidad)",
            "nota": "USO-MULTIPLE + institucional salud (laboratorio/IPS). Mercado real del barrio "
                    "(ver escenario de venta). CP = LP: el temporal amoblado no aplica a salud.",
            "override_uso": True, "sensibilidad": "salud-institucional",
            "mix_usos": [comp, comp2],
            "fuente_canon": "Comparables consultorios Prado Veraniego $61,5-88k/m2/mes (FincaRaiz 2026-08-14); institucional $60k LP.",
            "fuente_costo": "Institucional = estandar x1,15 (instalaciones de laboratorio)."}


def _mix_geriatrico(c, modo):
    """D_MIXTO_GERIATRICO: 30% GFA hogar geriatrico (operador) + 70% vivienda VIS.
    Canon derivado de la capacidad de pago del operador: 25-30 cupos x $2,5-4 M/mes
    (hogaresgerontologicos.com / MayorVida 2026) = $62-120 M/mes; ~25% a canon sobre
    400-500 m2 -> $35-60k/m2/mes; se usa $40.000 LP."""
    viv = c["vivienda"]
    comp = {"uso": "Hogar geriatrico (operador)", "pct_gfa": 0.30,
            "unidad_m2": 400.0, "eficiencia_nga": 0.80,
            "costo_construccion_m2": round(viv["costo_construccion_m2"] * 1.05, -5),
            "fuente": "Canon LP $40.000/m2/mes derivado de capacidad de pago (25-30 cupos x "
                      "$2,5-4 M/mes, hogaresgerontologicos.com/MayorVida 2026). 5+ hogares en "
                      "< 200 m (levantamiento del usuario 2026-08-14)."}
    comp2 = {"uso": viv["uso"], "pct_gfa": 0.70, "unidad_m2": viv["unidad_m2"],
             "eficiencia_nga": viv["eficiencia_nga"],
             "costo_construccion_m2": viv["costo_construccion_m2"],
             "fuente": "Vivienda del caso (canon/precio validado 2026-08-14)."}
    if modo == "venta":
        comp["precio_venta_m2"] = 5500000
        comp["absorcion_unid_mes"] = 0.25
        comp2["precio_venta_m2"] = viv["precio_venta_m2"]
        comp2["absorcion_unid_mes"] = 2.5
        return {"nombre": "D - Mixto Geriatrico (sensibilidad)",
                "nivel_acabados": "Mixto",
                "nota": "USO-MULTIPLE + hogar geriatrico (operador arrienda el espacio). "
                        "Demanda respaldada: Suba concentra 13% de los adultos mayores de Bogota "
                        "(Alcaldia) e indice de envejecimiento de la ciudad 72/100 (proyecciones).",
                "override_uso": True, "sensibilidad": "salud-institucional",
                "mix_usos": [comp, comp2],
                "fuente_precio": "Geriátrico $5,5 M/m2 (derivado del canon con cap rate ~8,7%); vivienda del caso.",
                "fuente_costo": "Geriátrico = estandar x1,05 (adecuaciones basicas; el operador equipa)."}
    comp["canon_m2_mes"] = {"CP": 40000, "LP": 40000}
    comp2["canon_m2_mes"] = {"CP": round(viv["canon_lp"] * 1.7), "LP": viv["canon_lp"]}
    return {"nombre": "D - Mixto Geriatrico (sensibilidad)",
            "nota": "USO-MULTIPLE + hogar geriatrico (operador). Demanda respaldada por "
                    "envejecimiento (ver escenario de venta). CP = LP.",
            "override_uso": True, "sensibilidad": "salud-institucional",
            "mix_usos": [comp, comp2],
            "fuente_canon": "Canon derivado de capacidad de pago del operador (2026-08-14).",
            "fuente_costo": "Geriátrico = estandar x1,05 (adecuaciones basicas)."}


def main():
    n = 0
    for chip, c in CASOS.items():
        for modo, carpeta in (("venta", FIN), ("renta", REN)):
            if chip == "AAA0127AZPA":
                nombre = {"venta": "parametros_AAA0127AZPA_venta_gfa1053_cl550.json",
                          "renta": "parametros_AAA0127AZPA_renta_gfa1053_cl550.json"}[modo]
            else:
                nombre = {"venta": f"parametros_{chip}_venta.json",
                          "renta": f"parametros_{chip}_renta.json"}[modo]
            ruta = os.path.join(carpeta, nombre)
            d = json.load(io.open(ruta, encoding="utf-8"))
            for key, fn in (("D_MIXTO_SALUD", _mix_salud), ("D_MIXTO_OFICINAS", _mix_oficinas)):
                if key in d["escenarios"]:
                    continue
                d["escenarios"][key] = fn(c, modo)
                n += 1
            # Escenarios de salud institucional: solo caso A (cluster de salud real verificado)
            if chip == "AAA0127AZPA":
                for key, fn in (("D_MIXTO_INSTITUCIONAL", _mix_institucional),
                                ("D_MIXTO_GERIATRICO", _mix_geriatrico)):
                    if key in d["escenarios"]:
                        continue
                    d["escenarios"][key] = fn(c, modo)
                    n += 1
            io.open(ruta, "w", encoding="utf-8").write(
                json.dumps(d, ensure_ascii=False, indent=2))
            print("OK", nombre)
    print("Escenarios anadidos:", n)


if __name__ == "__main__":
    main()
