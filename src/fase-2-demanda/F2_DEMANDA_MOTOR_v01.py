"""
================================================================================
F2_DEMANDA_MOTOR_v01.py — Estudio de Prefactibilidad Inmobiliaria
Proyecto: DiseñoParametrico / Fase 2
Python 3.12 Standalone (NO Grasshopper)
================================================================================

OBJETIVO:
  Evaluar 3 escenarios de desarrollo (VIS, Estándar, Lujo) basados en el GFA
  máximo de la Fase 1 y determinar el producto más rentable.

USO:
  python src/fase-2-demanda/F2_DEMANDA_MOTOR_v01.py --chip AAA0127AZPA --gfa 632.695061 --costo-lote 1200000000

SALIDA:
  Guarda un JSON en data/fase-2-demanda/<CHIP>-prefactibilidad.json
================================================================================
"""

import argparse
import json
import os
from typing import Dict, Any, List

# --- Datos de Mercado Referencia (Bogotá - COP) ---
# En el futuro, estos valores serán sobrescritos por el fetch de MetroCuadrado/Habi
MARKET_DATA: Dict[str, Dict[str, float]] = {
    "VIS": {
        "ntg_ratio": 0.80,
        "avg_unit_size_m2": 55.0,
        "construccion_m2": 2600000,
        "venta_m2": 4500000
    },
    "Estandar": {
        "ntg_ratio": 0.75,
        "avg_unit_size_m2": 85.0,
        "construccion_m2": 3500000,
        "venta_m2": 6500000
    },
    "Lujo": {
        "ntg_ratio": 0.70,
        "avg_unit_size_m2": 150.0,
        "construccion_m2": 5000000,
        "venta_m2": 9500000
    }
}

# --- Parámetros Financieros Base ---
COSTOS_BLANDOS_PCT = 0.15  # 15% del costo duro
COSTOS_MKT_PCT = 0.04      # 4% de los ingresos totales


def run_scenario(scenario_name: str, gfa_max: float, costo_lote: float, market: Dict[str, float]) -> Dict[str, Any]:
    """Calcula los KPIs para un escenario específico."""
    
    nga = gfa_max * market["ntg_ratio"]
    num_unidades = int(nga / market["avg_unit_size_m2"])
    area_vendible_real = num_unidades * market["avg_unit_size_m2"]
    
    ingresos_totales = area_vendible_real * market["venta_m2"]
    costo_duro = gfa_max * market["construccion_m2"]
    costo_blando = costo_duro * COSTOS_BLANDOS_PCT
    costo_mkt = ingresos_totales * COSTOS_MKT_PCT
    costo_total = costo_lote + costo_duro + costo_blando + costo_mkt
    
    utilidad_bruta = ingresos_totales - costo_total
    mub = (utilidad_bruta / ingresos_totales) * 100 if ingresos_totales > 0 else 0
    roi = (utilidad_bruta / costo_total) * 100 if costo_total > 0 else 0
    cl_sobre_ventas = (costo_lote / ingresos_totales) * 100 if ingresos_totales > 0 else 0
    
    return {
        "producto": scenario_name,
        "gfa_m2": round(gfa_max, 2),
        "nga_m2": round(nga, 2),
        "num_unidades": num_unidades,
        "tamano_unidad_m2": market["avg_unit_size_m2"],
        "ingresos_totales_cop": round(ingresos_totales, 2),
        "costo_lote_cop": round(costo_lote, 2),
        "costo_duro_cop": round(costo_duro, 2),
        "costo_blando_cop": round(costo_blando, 2),
        "costo_mkt_cop": round(costo_mkt, 2),
        "costo_total_cop": round(costo_total, 2),
        "utilidad_bruta_cop": round(utilidad_bruta, 2),
        "KPIs": {
            "MUB_pct": round(mub, 2),
            "ROI_pct": round(roi, 2),
            "Lote_sobre_Ventas_pct": round(cl_sobre_ventas, 2)
        }
    }

def evaluate(gfa_max: float, costo_lote: float, chip: str) -> Dict[str, Any]:
    """Evalúa todos los escenarios y selecciona el mejor por ROI."""
    escenarios: List[Dict[str, Any]] = []
    
    for name, data in MARKET_DATA.items():
        escenarios.append(run_scenario(name, gfa_max, costo_lote, data))
    
    # Ordenar por ROI descendente
    escenarios_sorted = sorted(escenarios, key=lambda x: x["KPIs"]["ROI_pct"], reverse=True)
    recomendado = escenarios_sorted[0]
    
    return {
        "chip": chip,
        "gfa_maximo_evaluado": gfa_max,
        "costo_lote_input": costo_lote,
        "escenarios": escenarios_sorted,
        "recomendacion": {
            "producto": recomendado["producto"],
            "roi_esperado": recomendado["KPIs"]["ROI_pct"],
            "num_unidades_sugeridas": recomendado["num_unidades"],
            "tamano_unidad_sugerida": recomendado["tamano_unidad_m2"]
        }
    }

def main():
    parser = argparse.ArgumentParser(description="Motor de Demanda Inmobiliaria")
    parser.add_argument("--chip", type=str, required=True, help="CHIP del predio")
    parser.add_argument("--gfa", type=float, required=True, help="GFA máximo calculado en Fase 1 (m2)")
    parser.add_argument("--costo-lote", type=float, required=True, help="Costo total de adquisición del lote (COP)")
    
    args = parser.parse_args()
    
    resultado = evaluate(args.gfa, args.costo_lote, args.chip)
    
    # Guardar JSON
    output_dir = "data/fase-2-demanda"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "{}-prefactibilidad.json".format(args.chip))
    
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(resultado, f, indent=4, ensure_ascii=False)
    
    # Imprimir resumen en consola
    print("\n" + "="*50)
    print("ANÁLISIS DE PREFACTIBILIDAD — CHIP: {}".format(args.chip))
    print("="*50)
    print("GFA Máximo: {:.1f} m2 | Costo Lote: ${:,.0f} COP\n".format(args.gfa, args.costo_lote))
    
    print("{:<10} {:<10} {:<15} {:<15} {:<10}".format(
        "Producto", "Unidades", "Ingresos (M)", "Utilidad (M)", "ROI %"
    ))
    print("-" * 60)
    for esc in resultado["escenarios"]:
        print("{:<10} {:<10} {:<15.1f} {:<15.1f} {:<10.2f}".format(
            esc["producto"],
            esc["num_unidades"],
            esc["ingresos_totales_cop"] / 1e6,
            esc["utilidad_bruta_cop"] / 1e6,
            esc["KPIs"]["ROI_pct"]
        ))
        
    print("\n>>> RECOMENDACIÓN: Desarrollar producto '{}' ({} unidades de {} m2) con ROI esperado de {}%".format(
        resultado["recomendacion"]["producto"],
        resultado["recomendacion"]["num_unidades_sugeridas"],
        resultado["recomendacion"]["tamano_unidad_sugerida"],
        resultado["recomendacion"]["roi_esperado"]
    ))
    print("JSON guardado en: {}\n".format(output_path))

if __name__ == "__main__":
    main()
    