#!/usr/bin/env python3
# ==============================================================================
# extract-decreto-555-relevante.py
# ------------------------------------------------------------------------------
# Extrae las partes relevantes del Decreto 555/2021 para el pipeline paramétrico
# y genera:
#   1. docs/normativa/pot-bogota/decreto-555-extractos.md
#   2. data/pot-bogota/retiros-estructurados.json
#   3. data/pot-bogota/edificabilidad-estructurada.json
#   4. data/pot-bogota/tratamientos-estructurados.json
#
# Uso:
#   python scripts/utilities/extract-decreto-555-relevante.py --input /home/z/my-project/upload/decreto555.md
# ==============================================================================

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import click

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent


def extraer_seccion(texto: str, patron_busqueda: str, lineas_despues: int = 80) -> str:
    """Extrae una sección del decreto a partir de un patrón regex."""
    lineas = texto.split("\n")
    patron = re.compile(patron_busqueda)
    for i, linea in enumerate(lineas):
        if patron.search(linea):
            inicio = max(0, i - 2)
            fin = min(len(lineas), i + lineas_despues)
            return "\n".join(lineas[inicio:fin])
    return ""


def limpiar_texto(texto: str) -> str:
    """Limpia el texto (elimina líneas vacías excesivas, normaliza espacios)."""
    # Eliminar referencias URL
    texto = re.sub(r"https?://[^\s]+", "", texto)
    # Colapsar espacios múltiples
    texto = re.sub(r" {2,}", " ", texto)
    # Eliminar líneas vacías consecutivas
    texto = re.sub(r"\n{3,}", "\n\n", texto)
    return texto.strip()


@click.command()
@click.option("--input", "-i", required=True, type=click.Path(exists=True))
@click.option("--output-dir", default=str(PROJECT_ROOT / "docs" / "normativa" / "pot-bogota"))
@click.option("--data-dir", default=str(PROJECT_ROOT / "data" / "pot-bogota"))
def main(input: str, output_dir: str, data_dir: str) -> None:
    """Extrae partes relevantes del Decreto 555/2021."""

    input_path = Path(input)
    output_path = Path(output_dir)
    data_path = Path(data_dir)

    output_path.mkdir(parents=True, exist_ok=True)
    data_path.mkdir(parents=True, exist_ok=True)

    click.echo(f"[INFO] Leyendo: {input_path}")
    texto = input_path.read_text(encoding="utf-8")
    click.echo(f"[INFO] Total líneas: {len(texto.splitlines())}")

    # =====================================================================
    # 1. Extraer secciones relevantes
    # =====================================================================
    click.echo("")
    click.echo("[1] Extrayendo secciones relevantes...")

    secciones = {
        "art_256_normas_comunes": {
            "titulo": "Artículo 256. Normas urbanísticas comunes a los tratamientos",
            "busqueda": r"Art[íi]culo\s*256\s*\.?\s*Normas",
            "lineas": 50,
        },
        "art_257_edificabilidad_maxima": {
            "titulo": "Artículo 257. Edificabilidad máxima permitida en los tratamientos",
            "busqueda": r"Art[íi]culo\s*257\s*\.?\s*Edificabilidad",
            "lineas": 30,
        },
        "art_258_antejardin": {
            "titulo": "Artículo 258. Dimensión del antejardín",
            "busqueda": r"Art[íi]culo\s*258\s*\.?\s*Dimensi[óo]n",
            "lineas": 40,
        },
        "art_259_retrocesos": {
            "titulo": "Artículo 259. Retrocesos existentes sobre espacio público",
            "busqueda": r"Art[íi]culo\s*259\s*\.?\s*Retrocesos",
            "lineas": 30,
        },
        "art_260_altura_maxima": {
            "titulo": "Artículo 260. Altura máxima de las edificaciones",
            "busqueda": r"Art[íi]culo\s*260\s*\.?\s*Altura",
            "lineas": 40,
        },
        "art_261_manzanas": {
            "titulo": "Artículo 261. Condiciones para configuración de manzanas",
            "busqueda": r"Art[íi]culo\s*261\s*\.?\s*Condiciones",
            "lineas": 60,
        },
        "art_281_edificabilidad_desarrollo": {
            "titulo": "Artículo 281. Edificabilidad y altura máxima en tratamiento de desarrollo",
            "busqueda": r"Art[íi]culo\s*281\s*\.?\s*Edificabilidad",
            "lineas": 120,
        },
        "art_282_lineamientos_4C_4D": {
            "titulo": "Artículo 282. Lineamientos para proyectos en rangos 4C y 4D",
            "busqueda": r"Art[íi]culo\s*282\s*\.?\s*Lineamientos",
            "lineas": 40,
        },
        "art_283_predios_aislados": {
            "titulo": "Artículo 283. Predios urbanizables no urbanizados aislados",
            "busqueda": r"Art[íi]culo\s*283\s*\.?\s*Normas",
            "lineas": 50,
        },
        "art_301_renovacion_urbana": {
            "titulo": "Artículo 301. Tratamiento de renovación urbana",
            "busqueda": r"Art[íi]culo\s*301\s*\.?\s*Tratamiento\s+de\s+renovaci[óo]n",
            "lineas": 50,
        },
        "art_304_indice_renovacion": {
            "titulo": "Artículo 304. Índice de construcción efectivo en renovación",
            "busqueda": r"Art[íi]culo\s*304\s*\.?\s*Reglas",
            "lineas": 40,
        },
        "art_310_consolidacion": {
            "titulo": "Artículo 310. Normas de edificabilidad en tratamiento de consolidación",
            "busqueda": r"Art[íi]culo\s*310\s*\.?\s*Normas\s+de\s+edificabilidad",
            "lineas": 80,
        },
        "art_311_copropiedad": {
            "titulo": "Artículo 311. Normas para conjuntos en copropiedad",
            "busqueda": r"Art[íi]culo\s*311\s*\.?\s*Normas\s+aplicables",
            "lineas": 60,
        },
        "art_339_bordes_urbanos": {
            "titulo": "Artículo 339. Bordes Urbanos",
            "busqueda": r"Art[íi]culo\s*339\s*\.?\s*Bordes",
            "lineas": 30,
        },
        "art_340_subdivisiones": {
            "titulo": "Artículo 340. Subdivisiones (área y frente mínimos por altura)",
            "busqueda": r"Art[íi]culo\s*340\s*\.?\s*Subdivisiones",
            "lineas": 60,
        },
        "art_343_conservacion": {
            "titulo": "Artículo 343. Tratamiento urbanístico de conservación",
            "busqueda": r"Art[íi]culo\s*343\s*\.?\s*Tratamiento\s+urban[íi]stico\s+de\s+conservaci[óo]n",
            "lineas": 50,
        },
    }

    extractos = {}
    for key, config in secciones.items():
        click.echo(f"  - {config['titulo']}")
        extracto = extraer_seccion(texto, config["busqueda"], config["lineas"])
        if extracto:
            extractos[key] = {
                "titulo": config["titulo"],
                "contenido": limpiar_texto(extracto),
            }
        else:
            click.echo(f"    [WARN] No encontrado", err=True)

    # =====================================================================
    # 2. Generar Markdown consolidado
    # =====================================================================
    click.echo("")
    click.echo("[2] Generando Markdown consolidado...")

    md_content = """---
fecha: 2026-08-01
tipo: referencia
fase: transversal
estado: activo
tags: [pot, decreto-555, bogota, normativa, extractos]
---

# Decreto 555/2021 - Extractos Relevantes para Pipeline Paramétrico

**Fuente:** Decreto 555 del 29 de diciembre de 2021 - POT Bogotá
**Propósito:** Documentación normativa estructurada para alimentar `CONFIGURAR_LADOS_v04.py` y `MOTOR_DEMANDA.py`.

## Índice de artículos relevantes

"""

    for key, data in extractos.items():
        md_content += f"- [[#{data['titulo']}|{data['titulo']}]]\n"

    md_content += "\n---\n\n"

    for key, data in extractos.items():
        md_content += f"## {data['titulo']}\n\n"
        md_content += f"```\n{data['contenido']}\n```\n\n"
        md_content += "---\n\n"

    md_content += """## Referencias cruzadas

- [[03-retiros-obligatorios]]
- [[04-edificabilidad-y-ocupacion]]
- [[05-alturas-maximas]]
- [[12-anexo-tablas-retiros]]

## Notas de implementación

### Para CONFIGURAR_LADOS_v04.py
Los retiros se derivan del **tratamiento urbanístico** + **tipología edificatoria** + **área del lote**.
Ver `data/pot-bogota/retiros-estructurados.json` para los valores estructurados.

### Para MOTOR_DEMANDA.py
La edificabilidad máxima se deriva del **rango** asignado al predio.
Ver `data/pot-bogota/edificabilidad-estructurada.json` para los valores estructurados.

### Para VOLUMEN_v04.py
La altura máxima ya se obtiene del .gdb (capa `Area_elevacion_maxima`).
Validar contra los rangos de edificabilidad para asegurar consistencia.
"""

    md_file = output_path / "decreto-555-extractos.md"
    md_file.write_text(md_content, encoding="utf-8")
    click.echo(f"  [OK] {md_file}")

    # =====================================================================
    # 3. Generar JSON estructurado de retiros
    # =====================================================================
    click.echo("")
    click.echo("[3] Generando retiros-estructurados.json...")

    retiros = {
        "_metadata": {
            "fuente": "Decreto 555 del 29 de diciembre de 2021",
            "fecha_extraccion": "2026-08-01",
            "descripcion": "Retiros y aislamientos obligatorios por tratamiento y tipología",
        },
        "tratamientos": {
            "desarrollo": {
                "tipologia_aislada": {
                    "descripcion": "Predios en zonas con tipología edificatoria aislada",
                    "frente_mayor_16m_fondo_mayor_13_5m": {
                        "altura_max_pisos": 6,
                        "aislamiento_posterior_m": 3.0,
                        "aislamiento_lateral_m": "variable según relación 2:1 con perfil vial",
                    },
                    "frente_10_5_a_16m_fondo_mayor_8m": {
                        "altura_max_pisos": 3,
                        "aislamiento_posterior_m": 3.0,
                        "nota": "Si solo cumple una condición, máximo 2 pisos",
                    },
                    "frente_menor_10_5m": {
                        "altura_max_pisos": 3,
                        "aislamiento_posterior_m": 3.0,
                        "nota": "Pueden parearse por un costado",
                    },
                },
                "tipologia_continua": {
                    "descripcion": "Predios en zonas con tipología edificatoria continua",
                    "norma": "Aplican normas de la manzana donde se encuentren",
                    "aislamiento_lateral_m": "no exigido (tipología continua)",
                },
            },
            "consolidacion": {
                "tipologia_continua": {
                    "aislamiento_lateral_m": "no exigido",
                    "nota": "Salvo lo indicado en parágrafos especiales (VIS/VIP)",
                },
                "tipologia_aislada": {
                    "frente_minimo_m": 24,
                    "area_minima_m2": 1200,
                    "nota": "Para alturas superiores debe colindar con vía >= 22m",
                },
            },
            "renovacion_urbana": {
                "descripcion": "Modalidad de revitalización",
                "indice_construccion_efectivo_max_directo": 5.0,
                "indice_construccion_efectivo_max_con_cesion_esquina": 6.0,
                "indice_construccion_efectivo_max_manzana_completa": 7.0,
                "indice_construccion_efectivo_max_con_plan_parcial": "superior a 7.0",
            },
            "conservacion": {
                "descripcion": "Bienes de Interés Cultural",
                "norma": "Según ficha de valoración y nivel de intervención (1-4)",
                "nota": "Restringido, requiere concepto del Consejo Distrital de Patrimonio Cultural",
            },
            "mejoramiento_integral": {
                "descripcion": "Asentamientos informales en proceso de legalización",
                "norma": "Según Plan Vecinos y regularización",
            },
        },
        "rurales": {
            "centros_poblados": {
                "altura_max_pisos": 2,
                "antejardin_m": "no exigido (excepto si vecinos lo tienen)",
                "voladizos_m": 0.60,
                "sotanos": "no permitidos",
            },
            "vivienda_campestre_guaymaral": {
                "altura_max_pisos": 2,
                "frente_minimo_m": 10,
                "IO_max_vivienda": 0.10,
                "IO_max_otros": 0.20,
                "IC_max_vivienda": 0.20,
                "IC_max_otros": 0.40,
            },
            "vivienda_rural_dispersa": {
                "altura_max_pisos": 2,
                "retiro_frontal_via_m": 5.0,
                "voladizos_m": 0.60,
                "sotanos": "no permitidos",
            },
            "nodos_equipamiento_rural": {
                "altura_max_pisos": 2,
                "excepcion_nariño_pisos": 4,
                "antejardin_m": 5.0,
                "IO_max": 0.29,
                "IC_max": 1.3,
                "frente_minimo_m": 10,
                "area_minima_ha": 1,
            },
        },
        "subdivisiones_prediales": {
            "descripcion": "Área y frente mínimos para subdivisiones según altura objetivo",
            "tabla": {
                "3_pisos": {"area_min_m2": 53, "frente_min_m": 4.5},
                "5_pisos": {"area_min_m2": 144, "frente_min_m": 12},
                "8_pisos": {"area_min_m2": 216, "frente_min_m": 18},
                "12_pisos": {"area_min_m2": 360, "frente_min_m": 30},
            },
            "nota": "Predios existentes con 53 m² y frente < 4.5m pueden alcanzar máximo 3 pisos",
        },
        "antejardines": {
            "descripcion": "Dimensión mínima entre paramento de construcción y lindero frontal",
            "fuente_cartografica": "Mapa CU-5.5 'Dimensionamiento de Antejardines'",
            "default_si_no_determinado": "Dimensión mínima según Manual de Normas Comunes",
            "centros_poblados_rurales": "No se exige, excepto si edificaciones vecinas lo tienen",
            "nodos_equipamiento_rural": "Mínimo 5 m sobre vía",
        },
        "notas_importantes": [
            "Los valores específicos por UPZ se definen en mapas CU-5.4.2 a CU-5.4.33",
            "El antejardín se actualiza mediante resoluciones de la Secretaría Distrital de Planeación",
            "Verificar siempre condiciones especiales: VIS, VIP, Bordes Urbanos, Áreas de Actividad",
            "La relación 2:1 entre altura de edificación y ancho de perfil vial es determinante",
            "Cuando la altura máxima sea más de 2 veces el ancho del perfil vial, se exige retroceso progresivo",
        ],
    }

    retiros_file = data_path / "retiros-estructurados.json"
    retiros_file.write_text(json.dumps(retiros, ensure_ascii=False, indent=2), encoding="utf-8")
    click.echo(f"  [OK] {retiros_file}")

    # =====================================================================
    # 4. Generar JSON estructurado de edificabilidad
    # =====================================================================
    click.echo("")
    click.echo("[4] Generando edificabilidad-estructurada.json...")

    edificabilidad = {
        "_metadata": {
            "fuente": "Decreto 555 del 29 de diciembre de 2021",
            "fecha_extraccion": "2026-08-01",
            "descripcion": "Rangos de edificabilidad por tratamiento",
        },
        "tratamiento_desarrollo": {
            "descripcion": "Rangos de edificabilidad para tratamiento de desarrollo",
            "fuente_cartografica": "Mapas CU-5.4.2 a CU-5.4.33 'Edificabilidad máxima'",
            "rangos": {
                "RANGO_1": {
                    "IC_max_con_VIS_VIP": 2.82,
                    "IC_max_sin_VIS_VIP": 2.25,
                    "IO_max_ANU": 0.28,
                    "altura_max_pisos": 3,
                },
                "RANGO_2": {
                    "IC_max_con_VIS_VIP": 2.57,
                    "IC_max_sin_VIS_VIP": 2.00,
                    "IO_max_ANU": 0.28,
                    "altura_max_pisos": 8,
                },
                "RANGO_3": {
                    "IC_max_con_VIS_VIP": 2.32,
                    "IC_max_sin_VIS_VIP": 1.75,
                    "IO_max_ANU": 0.15,
                    "nota_altura": "Según normas volumétricas del tratamiento",
                },
                "RANGO_4A": {
                    "IC_max_con_VIS_VIP": 1.75,
                    "IC_max_sin_VIS_VIP": 1.20,
                    "IO_max_ANU": 0.15,
                    "nota_altura": "Según normas comunes a los tratamientos",
                },
                "RANGO_4B": {
                    "IC_max_con_VIS_VIP": 1.75,
                    "IC_max_sin_VIS_VIP": 1.20,
                    "IO_max_ANU": 0.15,
                },
                "RANGO_4C": {
                    "IC_max_con_VIS_VIP": 1.20,
                    "IC_max_sin_VIS_VIP": 0.90,
                    "IO_max_ANU": 0.10,
                    "nota": "Lineamientos especiales según Artículo 282",
                },
                "RANGO_4D": {
                    "IC_max_con_VIS_VIP": 0.90,
                    "IC_max_sin_VIS_VIP": 0.90,
                    "IO_max_ANU": 0.10,
                    "nota": "Lineamientos especiales según Artículo 282",
                },
            },
            "definiciones": {
                "IC": "Índice de Construcción = Área Construida / Área Neta Urbanizable",
                "IO": "Índice de Ocupación = Área Ocupada / Área Neta Urbanizable",
                "ANU": "Área Neta Urbanizable",
                "VIS": "Vivienda de Interés Social",
                "VIP": "Vivienda de Interés Prioritario",
            },
        },
        "tratamiento_consolidacion": {
            "descripcion": "Edificabilidad según normas volumétricas",
            "IO_IC": "resultantes de la aplicación de las normas volumétricas",
            "altura_pisos": "Definida en mapas CU-5.4.2 a CU-5.4.33 por UPL",
            "excepcion_proximidad": {
                "condicion": "Predios en área de actividad de proximidad con ámbito >= 1 manzana",
                "altura_max_pisos": "2 veces el permitido en mapas, sin superar 12 pisos",
            },
            "excepcion_VIS_VIP": {
                "condicion": "Áreas receptoras de VIS/VIP con >= 70% VIS o >= 50% VIP",
                "altura_max_pisos": "Según mapas, indistintamente del área",
                "aislamiento_lateral": "Desde altura base del sector en tipología continua",
            },
            "urbanizacion_san_jose_bavaria": {
                "densidad_max_viv_por_lote": 4,
                "IC_max_predial": 0.30,
                "IO_max_predial": "según licencia original",
            },
        },
        "tratamiento_renovacion_urbana": {
            "descripcion": "Modalidad de revitalización",
            "IC_efectivo_max_licencia_directa": 5.0,
            "IC_efectivo_max_con_cesion_esquina": 6.0,
            "IC_efectivo_max_manzana_completa": 7.0,
            "IC_efectivo_max_con_plan_parcial": "superior a 7.0 (requiere plan parcial)",
            "area_minima_plan_parcial_ha": 3.0,
            "mezcla_usos_residencial_min": "8% del área de construcción base",
        },
        "tratamiento_conservacion": {
            "descripcion": "Bienes de Interés Cultural - regulación especial",
            "norma": "Según ficha de valoración, nivel 1-4",
            "requiere_concepto": "Consejo Distrital de Patrimonio Cultural",
        },
        "equipamientos": {
            "existentes": "Mantienen condiciones de edificabilidad y volumetría existentes",
            "nuevos": "Según sector donde se localicen",
            "en_parques": "Optimización del suelo, sin IO/IC específico",
            "dotacionales_estudio": "Definidos en estudios urbanísticos para dotacionales",
        },
        "rurales": {
            "vivienda_campestre_guaymaral": {
                "IO_max_vivienda": 0.10,
                "IO_max_otros_usos": 0.20,
                "IC_max_vivienda": 0.20,
                "IC_max_otros": 0.40,
                "altura_max_pisos": 2,
                "frente_min_m": 10,
            },
            "nodos_equipamiento_rural": {
                "IO_max": 0.29,
                "IC_max": 1.3,
                "altura_max_pisos": 2,
                "excepcion_los_nariño_pisos": 4,
                "frente_min_m": 10,
                "area_min_ha": 1,
            },
        },
        "notas_importantes": [
            "IC = Índice de Construcción, IO = Índice de Ocupación",
            "Los rangos 4C y 4D tienen lineamientos especiales (Artículo 282)",
            "La edificabilidad adicional por VIS/VIP está sujeta a cumplimiento de obligaciones",
            "Alturas máximas por UPZ en mapas CU-5.4.2 a CU-5.4.33",
            "La edificabilidad efectiva puede diferir de la máxima según obligaciones urbanísticas",
        ],
    }

    edif_file = data_path / "edificabilidad-estructurada.json"
    edif_file.write_text(json.dumps(edificabilidad, ensure_ascii=False, indent=2), encoding="utf-8")
    click.echo(f"  [OK] {edif_file}")

    # =====================================================================
    # 5. Generar JSON estructurado de tratamientos
    # =====================================================================
    click.echo("")
    click.echo("[5] Generando tratamientos-estructurados.json...")

    tratamientos = {
        "_metadata": {
            "fuente": "Decreto 555 del 29 de diciembre de 2021",
            "fecha_extraccion": "2026-08-01",
        },
        "tratamientos": {
            "conservacion": {
                "nombre": "Conservación",
                "objetivo": "Preservar Bienes de Interés Cultural",
                "ambito": "BIC grupo urbano y arquitectónico en suelo urbano o expansión",
                "modalidades": ["Conservación integral", "Conservación tipológica"],
                "niveles_intervencion": {
                    "1": "Conservación integral (máxima restricción)",
                    "2": "Conservación tipológica",
                    "3": "Adoptado en PEMP",
                    "4": "Inmuebles sin valores / lotes sin edificar",
                },
                "requiere": "Concepto del Consejo Distrital de Patrimonio Cultural",
            },
            "consolidacion": {
                "nombre": "Consolidación",
                "objetivo": "Afianzar patrones de uso y edificabilidad",
                "ambito": "Sectores urbanos consolidados",
                "incluye": [
                    "Áreas urbanizadas con licencia vigente",
                    "Planes parciales ejecutados",
                    "Predios ex-Mejoramiento Integral con déficit superado",
                    "Predios dotacionales/industriales/comerciales en consolidación",
                ],
                "tipologias": ["Continua", "Aislada"],
                "normas_volumetricas": "Según mapas CU-5.4.2 a CU-5.4.33",
            },
            "renovacion_urbana": {
                "nombre": "Renovación Urbana",
                "objetivo": "Transformar o recuperar sectores deteriorados",
                "modalidad": "Revitalización",
                "ambito": "Mapa CU-5.1 'Tratamientos urbanísticos'",
                "incluye": [
                    "Bienes fiscales",
                    "Predios en consolidación que cumplan condiciones especiales",
                    "Clubes y centros recreo-deportivos en reordenamiento",
                    "Proyectos de renovación para movilidad sostenible",
                ],
                "exige_plan_parcial_si_IC_mayor_a": 7.0,
                "area_minima_plan_parcial_ha": 3.0,
            },
            "desarrollo": {
                "nombre": "Desarrollo",
                "objetivo": "Urbanizar suelo de expansión",
                "ambito": "Suelo urbano de expansión",
                "rangos_edificabilidad": ["1", "2", "3", "4A", "4B", "4C", "4D"],
                "exige_plan_parcial": True,
                "obligaciones_urbanisticas": ["cesión suelo", "construcción redes", "VIS/VIP"],
            },
            "mejoramiento_integral": {
                "nombre": "Mejoramiento Integral",
                "objetivo": "Regularizar asentamientos informales",
                "ambito": "Barrios de origen informal en proceso de legalización",
                "instrumento": "Plan Vecinos (Decreto 563 de 2023)",
                "excepcion_bordes_urbanos": "Áreas de Ocupación Pública Prioritaria",
            },
        },
        "mapas_referencia": {
            "tratamientos": "CU-5.1 'Tratamientos urbanísticos'",
            "edificabilidad": "CU-5.4.2 a CU-5.4.33 (por UPL)",
            "antejardines": "CU-5.5 'Dimensionamiento de Antejardines'",
            "areas_actividad": "CU-5.3 'Áreas de Actividad'",
        },
        "manuales_referencia": [
            "Manual de Normas Comunes a los Tratamientos Urbanísticos (Decreto 603 de 2022)",
            "Manual de Normas Urbanísticas para el Tratamiento de Conservación",
        ],
    }

    trat_file = data_path / "tratamientos-estructurados.json"
    trat_file.write_text(json.dumps(tratamientos, ensure_ascii=False, indent=2), encoding="utf-8")
    click.echo(f"  [OK] {trat_file}")

    # =====================================================================
    # 6. Resumen
    # =====================================================================
    click.echo("")
    click.echo("=" * 60)
    click.echo("  EXTRACCIÓN COMPLETADA")
    click.echo("=" * 60)
    click.echo("")
    click.echo("Archivos generados:")
    click.echo(f"  [MD]  {md_file}")
    click.echo(f"  [JSON] {retiros_file}")
    click.echo(f"  [JSON] {edif_file}")
    click.echo(f"  [JSON] {trat_file}")
    click.echo("")
    click.echo("Próximos pasos:")
    click.echo("  1. Revisar el Markdown y ajustar si es necesario")
    click.echo("  2. Integrar retiros-estructurados.json en CONFIGURAR_LADOS_v04.py")
    click.echo("  3. Integrar edificabilidad-estructurada.json en MOTOR_DEMANDA.py")
    click.echo("  4. Commitear en Git")
    click.echo("")


if __name__ == "__main__":
    main()
