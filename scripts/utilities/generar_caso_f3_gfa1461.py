# -*- coding: utf-8 -*-
"""generar_caso_f3_gfa1461.py — JSON de resultados F2 del caso A (AAA0127AZPA) a la escala
de la envolvente Fase 1 v06 (GFA 1.461,1 m²) con la hipótesis de CL $800 M (2026-08-16).

Combina dos fuentes:
  - Escenarios A/B/C: corrida REAL del motor v03 con --costo-lote 800.000.000
    (F2_Modelo_Financiero/resultados_AAA0127AZPA_gfa1461_cl800/resultados_completos.json).
  - Escenarios mixtos D_MIXTO* (override USO-MULTIPLE del usuario): escalados desde
    resultados_AAA0127AZPA_gfa1053_cl550.json — mismos % de uso y eficiencias del
    componente original; gfa_i = pct_gfa x GFA nuevo; unidades enteras; KPIs con
    la estructura del pipeline (CB 15% CD, CMV 4% IT).

Salida: F2_Modelo_Financiero/resultados/resultados_AAA0127AZPA_gfa1461_cl800.json
(consumido por F3_DISTRIBUCION_v01.py, caso A).

USO:  python scripts/utilities/generar_caso_f3_gfa1461.py
"""
import io
import json
import os

BASE = os.path.join(os.path.dirname(__file__), "..", "..")
FIN = os.path.normpath(os.path.join(BASE, "src", "fase-2-demanda", "F2_Modelo_Financiero"))
GFA_NUEVO = 1461.0972          # envolvente Fase 1 v06 (gfa-gh.json, 2026-08-16)
CL_NUEVO = 800_000_000.0       # hipotesis del usuario 2026-08-16 (para avanzar el modelado)
FUENTE_MIXTOS = os.path.join(FIN, "resultados", "resultados_AAA0127AZPA_gfa1053_cl550.json")
FUENTE_V03 = os.path.join(FIN, "resultados_AAA0127AZPA_gfa1461_cl800", "resultados_completos.json")
SALIDA = os.path.join(FIN, "resultados", "resultados_AAA0127AZPA_gfa1461_cl800.json")

BLANDOS_PCT = 0.15
MKT_PCT = 0.04

NOTA = ("Caso A (El Prado) a la escala de la envolvente Fase 1 v06: GFA 1.461,1 m2 "
        "(6 pisos, ocupacion 243,5 m2, antejardin 5,0 m) y CL $800 M (hipotesis del "
        "usuario 2026-08-16 para avanzar; el lote se pedia en $1.200 M). Escenarios "
        "A/B/C de la corrida real del motor v03 (mercado 2026); mixtos D_MIXTO* "
        "escalados desde el caso gfa1053_cl550 (mismos % de uso del override USO-MULTIPLE).")


def escalar_componente(c, pct_sum):
    """Escala un componente del mix_usos_detalle al GFA nuevo manteniendo eficiencia,
    unidad tipica, precio y costo del componente original."""
    pct = c.get("pct_gfa", 0.0)
    gfa_i = round(pct * GFA_NUEVO, 2)
    gfa_o = c.get("gfa_i", 0.0) or 0.0
    nga_o = c.get("nga_i", 0.0) or 0.0
    efic = (nga_o / gfa_o) if gfa_o > 0 else 0.8
    nga_i = round(gfa_i * efic, 2)
    vend_o = c.get("area_vendible_m2", 0.0) or 0.0
    n_o = c.get("num_unidades", 0) or 0
    if n_o > 0 and nga_o > 0:
        unidad = round(vend_o / n_o, 1)
        vendible = round(nga_i * (vend_o / nga_o), 1)
        n_nuevo = int(round(vendible / unidad)) if unidad else 0
        vendible = round(n_nuevo * unidad, 1)
    else:
        unidad, vendible, n_nuevo = 0.0, 0.0, 0
    precio = c.get("precio_venta_m2", 0.0) or 0.0
    costo = c.get("costo_construccion_m2", 0.0) or 0.0
    return {
        "uso": c["uso"], "pct_gfa": pct, "gfa_i": gfa_i, "nga_i": nga_i,
        "num_unidades": n_nuevo, "area_vendible_m2": vendible,
        "precio_venta_m2": precio, "costo_construccion_m2": costo,
        "ingresos_cop": round(vendible * precio, 2),
    }


def escalar_mixto(esc, cl):
    """Reconstruye un escenario D_MIXTO* escalado con KPIs estilo pipeline."""
    comps = [escalar_componente(c, GFA_NUEVO) for c in (esc.get("mix_usos_detalle") or [])]
    it = sum(c["ingresos_cop"] for c in comps)
    cd = sum(c["gfa_i"] * c["costo_construccion_m2"] for c in comps)
    cb = BLANDOS_PCT * cd
    cmv = MKT_PCT * it
    ct = cl + cd + cb + cmv
    ub = it - ct
    nuevo = json.loads(json.dumps(esc))  # copia profunda (conserva notas/fuentes)
    nuevo["gfa_m2"] = round(GFA_NUEVO, 2)
    nuevo["nga_m2"] = round(sum(c["nga_i"] for c in comps), 2)
    nuevo["num_unidades"] = sum(c["num_unidades"] for c in comps)
    nuevo["area_vendible_m2"] = round(sum(c["area_vendible_m2"] for c in comps), 2)
    nuevo["ingresos_totales_cop"] = round(it, 2)
    nuevo["costo_lote_cop"] = cl
    nuevo["costo_duro_cop"] = round(cd, 2)
    nuevo["costo_blando_cop"] = round(cb, 2)
    nuevo["costo_mkt_cop"] = round(cmv, 2)
    nuevo["costo_total_cop"] = round(ct, 2)
    nuevo["utilidad_bruta_cop"] = round(ub, 2)
    nuevo["mix_usos_detalle"] = comps
    nuevo["KPIs"] = {
        "MUB_pct": round(100.0 * ub / it, 2) if it else 0.0,
        "ROI_pct": round(100.0 * ub / ct, 2) if ct else 0.0,
        "Lote_sobre_Ventas_pct": round(100.0 * cl / it, 2) if it else 0.0,
    }
    nuevo["nota"] = NOTA
    return nuevo


def main() -> int:
    with io.open(FUENTE_MIXTOS, encoding="utf-8") as f:
        base = json.load(f)
    with io.open(FUENTE_V03, encoding="utf-8") as f:
        v03 = json.load(f)

    escenarios = []
    for esc in v03["escenarios"]:            # A/B/C reales de la corrida CL800
        escenarios.append(esc)
    for esc in base["escenarios"]:           # D_MIXTO* escalados
        if esc["escenario_id"].startswith("D_MIXTO"):
            escenarios.append(escalar_mixto(esc, CL_NUEVO))

    paquete = json.loads(json.dumps(base))
    paquete["meta"]["gfa_fuente"] = "grasshopper-f1 (gfa-gh.json, envolvente v06)"
    paquete["meta"]["origen_datos"] = NOTA
    paquete["meta"]["fecha_ejecucion"] = "2026-08-16"
    paquete["gfa_max_m2"] = round(GFA_NUEVO, 2)
    paquete["lote"]["costo_lote_total_cop"] = CL_NUEVO
    paquete["costo_lote_total_cop"] = CL_NUEVO
    paquete["escenarios"] = escenarios
    paquete["recomendacion"] = v03["recomendacion"]
    paquete["alertas"] = v03["alertas"]
    paquete["sensibilidad"] = v03["sensibilidad"]
    paquete["aporte_suelo_analisis"] = v03.get("aporte_suelo_analisis")
    paquete["arriendo_analisis"] = v03.get("arriendo_analisis")
    paquete["flujo_caja"] = v03.get("flujo_caja")
    paquete["generado_por"] = "generar_caso_f3_gfa1461.py (2026-08-16)"

    with io.open(SALIDA, "w", encoding="utf-8") as f:
        json.dump(paquete, f, ensure_ascii=False, indent=2)
    print("OK ->", SALIDA)
    print("escenarios:", ", ".join(e["escenario_id"] for e in escenarios))
    for e in escenarios:
        if e["escenario_id"].startswith("D_MIXTO"):
            k = e["KPIs"]
            print(f"  {e['escenario_id']:22s} unid {e['num_unidades']:3d} | "
                  f"MUB {k['MUB_pct']:6.2f}% | ROI {k['ROI_pct']:6.2f}% | "
                  f"CL/IT {k['Lote_sobre_Ventas_pct']:5.2f}%")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
