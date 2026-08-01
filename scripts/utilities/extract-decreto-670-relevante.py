#!/usr/bin/env python3
# ==============================================================================
# extract-decreto-670-relevante.py
# ------------------------------------------------------------------------------
# Extrae las partes relevantes del Decreto 670 de 2025 (Decreto Único Distrital
# de Ordenamiento Territorial de Bogotá D.C.).
#
# El Decreto 670 es una COMPILACIÓN que:
#   - Recopila Decretos 555/2021, 088/2017, 582/2023, 603/2022, 563/2023,
#     523/2010, 550/2025, 466/2024, 099/2024, 122/2023, 203/2022, etc.
#   - Reenumera artículos (1-1400+)
#   - Mantiene vigentes las normas compiladas (ultraactividad)
#   - Añade nuevas disposiciones: incentivos, fichas C/UNE, actuaciones estratégicas
#
# Este script genera:
#   1. docs/normativa/pot-bogota/decreto-670-extractos.md
#   2. data/pot-bogota/decreto-670-estructura.json (índice navegable)
#   3. data/pot-bogota/incentivos-670.json (incentivos urbanísticos)
#   4. data/pot-bogota/actuaciones-estrategicas-670.json
#
# Uso:
#   python scripts/utilities/extract-decreto-670-relevante.py --input <ruta_a_decreto_670.md>
# ==============================================================================

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import click

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent


def extraer_seccion(texto: str, patron: str, lineas_despues: int = 80) -> str:
    """Extrae una sección del decreto usando regex."""
    lineas = texto.split("\n")
    patron_re = re.compile(patron)
    for i, linea in enumerate(lineas):
        if patron_re.search(linea):
            inicio = max(0, i - 2)
            fin = min(len(lineas), i + lineas_despues)
            return "\n".join(lineas[inicio:fin])
    return ""


def limpiar_texto(texto: str) -> str:
    """Limpia el texto."""
    texto = re.sub(r"https?://[^\s]+", "", texto)
    texto = re.sub(r" {2,}", " ", texto)
    texto = re.sub(r"\n{3,}", "\n\n", texto)
    return texto.strip()


def buscar_articulos_por_tema(texto: str, palabras_clave: list[str]) -> list[dict]:
    """Busca artículos que contengan palabras clave."""
    lineas = texto.split("\n")
    resultados = []
    patron_articulo = re.compile(r"Art[íi]culo\s+(\d+)\s*\.?\s*(.+?)$")

    for i, linea in enumerate(lineas):
        match = patron_articulo.search(linea)
        if match:
            numero = match.group(1)
            titulo = match.group(2).strip()
            contenido_completo = "\n".join(lineas[i:min(i + 30, len(lineas))])

            for palabra in palabras_clave:
                if palabra.lower() in contenido_completo.lower():
                    resultados.append({
                        "numero": numero,
                        "titulo": titulo,
                        "linea_inicio": i + 1,
                        "palabra_clave": palabra,
                        "extracto": limpiar_texto(contenido_completo[:1000]),
                    })
                    break

    return resultados


@click.command()
@click.option("--input", "-i", required=True, type=click.Path(exists=True))
@click.option("--output-dir", default=str(PROJECT_ROOT / "docs" / "normativa" / "pot-bogota"))
@click.option("--data-dir", default=str(PROJECT_ROOT / "data" / "pot-bogota"))
def main(input: str, output_dir: str, data_dir: str) -> None:
    """Extrae partes relevantes del Decreto 670 de 2025."""

    input_path = Path(input)
    output_path = Path(output_dir)
    data_path = Path(data_dir)

    output_path.mkdir(parents=True, exist_ok=True)
    data_path.mkdir(parents=True, exist_ok=True)

    click.echo(f"[INFO] Leyendo: {input_path}")
    texto = input_path.read_text(encoding="utf-8")
    click.echo(f"[INFO] Total líneas: {len(texto.splitlines())}")

    # =====================================================================
    # 1. Extraer índice general del decreto
    # =====================================================================
    click.echo("")
    click.echo("[1] Extrayendo estructura general del Decreto 670...")

    estructura = {
        "_metadata": {
            "fuente": "Decreto 670 de 2025 - Decreto Único Distrital de Ordenamiento Territorial de Bogotá D.C.",
            "fecha_expedicion": "27/12/2025",
            "fecha_entrada_vigencia": "28/12/2025",
            "registro_distrital": "8485 del 27 de diciembre del 2025",
            "tipo": "Decreto Único Distrital - Compilación",
            "descripcion": "Compila y racionaliza la reglamentación del POT (Decreto 555/2021) y decretos reglamentarios relacionados. Mantiene vigencia ultraactiva de las normas compiladas.",
        },
        "decretos_compilados": [
            {"decreto": "555/2021", "descripcion": "POT Bogotá - revisión general", "es_principal": True},
            {"decreto": "088/2017", "descripcion": "Unidad de Planeamiento Zonal Lagos de Torca"},
            {"decreto": "122/2023", "descripcion": "Vivienda colectiva y soluciones habitacionales con servicios"},
            {"decreto": "203/2022", "descripcion": "Servicios especiales en espacio público"},
            {"decreto": "523/2010", "descripcion": "Microzonificación sísmica de Bogotá"},
            {"decreto": "550/2025", "descripcion": "Actuación Estratégica Zona Industrial de Bogotá (ZIBo)"},
            {"decreto": "563/2023", "descripcion": "Reglamentación de planes parciales de renovación urbana"},
            {"decreto": "582/2023", "descripcion": "Incentivos urbanísticos por ecourbanismo"},
            {"decreto": "603/2022", "descripcion": "Primera actualización del Manual de Normas Comunes"},
            {"decreto": "466/2024", "descripcion": "Actualización Manual de Normas Comunes (Anexo 5)"},
            {"decreto": "099/2024", "descripcion": "Normas de construcción y habitabilidad vivienda"},
        ],
        "libros": [
            {"libro": 1, "titulo": "Microzonificación sísmica de Bogotá D.C.", "linea_inicio": 200},
            {"libro": 2, "titulo": "Gestión del riesgo de desastres y cambio climático", "linea_inicio": 844},
            {"libro": 3, "titulo": "Actuaciones urbanísticas en suelo rural y centros poblados", "linea_inicio": 2055},
            {"libro": 4, "titulo": "Acciones urbanísticas en suelo urbano", "linea_inicio": 8278},
            {"libro": 5, "titulo": "Planes, programas, proyectos y estrategias territoriales", "linea_inicio": 10526},
            {"libro": 6, "titulo": "Disposiciones finales", "linea_inicio": 44986},
        ],
        "relacion_con_555": {
            "descripcion": "El Decreto 670/2025 NO deroga ni reemplaza el Decreto 555/2021. Lo compila y mantiene vigente.",
            "efectos_juridicos": "Las normas compiladas mantienen efectos jurídicos ultraactivos",
            "regimen_transicion": "Licencias radicadas antes del 25/12/2024 se rigen por normas anteriores",
            "referencias_555_en_670": "El 670 cita constantemente artículos del 555 (ej: 'Artículo 286 del Decreto 555 de 2021')",
        },
    }

    # =====================================================================
    # 2. Buscar artículos relevantes para el pipeline paramétrico
    # =====================================================================
    click.echo("[2] Buscando artículos relevantes...")

    # Búsqueda por temas
    temas_busqueda = {
        "retiros_aislamientos": ["aislamiento", "retiro", "retroceso", "antejardín"],
        "edificabilidad": ["edificabilidad", "índice de construcción", "índice de ocupación", "IC máximo", "IO máximo"],
        "tratamientos": ["tratamiento urbanístico", "tratamiento de desarrollo", "tratamiento de consolidación"],
        "incentivos": ["incentivo", "Factor ECOS", "ecourbanismo"],
        "actuaciones_estrategicas": ["Actuación Estratégica", "ZIBo", "Lagos de Torca", "Distrito Aeroportuario"],
        "alturas": ["altura máxima", "alturas permitidas", "número de pisos"],
        "usos": ["uso principal", "uso complementario", "uso residencial", "área de actividad"],
        "cesiones": ["cesión obligatoria", "cesión en suelo", "espacio público"],
        "fichas_CUNE": ["C/UNE", "Fichas de edificabilidad", "Urbanizados No Edificados"],
    }

    articulos_por_tema = {}
    for tema, palabras in temas_busqueda.items():
        click.echo(f"  - Tema: {tema}")
        arts = buscar_articulos_por_tema(texto, palabras)
        # Limitar a los 15 más relevantes por tema
        articulos_por_tema[tema] = arts[:15]
        click.echo(f"    Encontrados: {len(arts)} (mostrando primeros 15)")

    # =====================================================================
    # 3. Extraer secciones específicas clave
    # =====================================================================
    click.echo("")
    click.echo("[3] Extrayendo secciones clave...")

    secciones_clave = {
        "objeto_y_ambito": {
            "titulo": "Artículo 1. Objeto y ámbito de aplicación",
            "patron": r"Art[íi]culo\s*\.\s*1\s*\.\s*Objeto\s+y\s+ámbito",
            "lineas": 40,
        },
        "incentivos_urbanisticos": {
            "titulo": "Incentivos Urbanísticos (general)",
            "patron": r"INCENTIVOS\s+URBANÍSTICOS",
            "lineas": 60,
        },
        "incentivo_tipo_1": {
            "titulo": "Incentivo Tipo 1: Disminución mezcla de usos",
            "patron": r"Tipo\s*1:\s*Disminución\s+del\s+Porcentaje",
            "lineas": 50,
        },
        "incentivo_tipo_3": {
            "titulo": "Incentivo Tipo 3: Disminución aislamiento lateral",
            "patron": r"Tipo\s*3:\s*Disminución\s+exigencia\s+de\s+aislamiento",
            "lineas": 30,
        },
        "fichas_cune": {
            "titulo": "Fichas de Edificabilidad para C/UNE",
            "patron": r"Art[íi]culo\s*239\s*\.\s*Objeto\s*\.\s*Adoptar\s+las\s+fichas\s+de\s+edificabilidad",
            "lineas": 60,
        },
        "actuacion_zibo": {
            "titulo": "Actuación Estratégica Zona Industrial de Bogotá (ZIBo)",
            "patron": r"Art[íi]culo\s*724\s*\.",
            "lineas": 80,
        },
        "manzanas_cuidado": {
            "titulo": "Manzanas del Cuidado",
            "patron": r"manzana\s+del\s+cuidado|Manzana\s+del\s+Cuidado",
            "lineas": 40,
        },
        "regimen_transicion": {
            "titulo": "Régimen de Transición",
            "patron": r"R[ée]gimen\s+de\s+[Tt]ransici[óo]n",
            "lineas": 30,
        },
        "vivienda_colectiva": {
            "titulo": "Vivienda Colectiva y Soluciones Habitacionales",
            "patron": r"Art[íi]culo\s*221\s*\.\s*Objeto\s+y\s+ámbito",
            "lineas": 50,
        },
        "tratamiento_desarrollo_670": {
            "titulo": "Tratamiento de Desarrollo (en 670)",
            "patron": r"SUBSECCIÓN\s*1\s*\n\s*TRATAMIENTO\s+DE\s+DESARROLLO",
            "lineas": 60,
        },
        "tratamiento_consolidacion_670": {
            "titulo": "Tratamiento de Consolidación (en 670)",
            "patron": r"SUBSECCIÓN\s*3\s*\n\s*TRATAMIENTO\s+DE\s+CONSOLIDACI[ÓO]N",
            "lineas": 80,
        },
    }

    extractos = {}
    for key, config in secciones_clave.items():
        click.echo(f"  - {config['titulo']}")
        extracto = extraer_seccion(texto, config["patron"], config["lineas"])
        if extracto:
            extractos[key] = {
                "titulo": config["titulo"],
                "contenido": limpiar_texto(extracto),
            }
        else:
            click.echo(f"    [WARN] No encontrado")

    # =====================================================================
    # 4. Generar Markdown consolidado
    # =====================================================================
    click.echo("")
    click.echo("[4] Generando Markdown consolidado...")

    md_content = f"""---
fecha: 2026-08-01
tipo: referencia
fase: transversal
estado: activo
tags: [pot, decreto-670, decreto-unico, bogota, normativa, compilacion]
---

# Decreto 670 de 2025 - Extractos Relevantes

**Tipo:** Decreto Único Distrital de Ordenamiento Territorial de Bogotá D.C.
**Fecha de expedición:** 27/12/2025
**Fecha de entrada en vigencia:** 28/12/2025
**Registro Distrital:** 8485 del 27 de diciembre del 2025

## ⚠️ Relación con el Decreto 555/2021

{estructura["relacion_con_555"]["descripcion"]}

- **Efectos jurídicos:** {estructura["relacion_con_555"]["efectos_juridicos"]}
- **Régimen de transición:** {estructura["relacion_con_555"]["regimen_transicion"]}
- **Referencias:** {estructura["relacion_con_555"]["referencias_555_en_670"]}

## Decretos compilados en el 670

| Decreto | Descripción | Principal |
|---------|-------------|-----------|
"""
    for dec in estructura["decretos_compilados"]:
        principal = "✅" if dec.get("es_principal") else ""
        md_content += f"| {dec['decreto']} | {dec['descripcion']} | {principal} |\n"

    md_content += """
## Estructura del Decreto 670 (6 libros)

"""
    for libro in estructura["libros"]:
        md_content += f"- **LIBRO {libro['libro']}:** {libro['titulo']}\n"

    md_content += "\n---\n\n## Secciones clave extraídas\n\n"

    for key, data in extractos.items():
        md_content += f"## {data['titulo']}\n\n"
        md_content += f"```\n{data['contenido']}\n```\n\n---\n\n"

    md_content += "## Artículos por tema\n\n"

    for tema, arts in articulos_por_tema.items():
        if arts:
            md_content += f"### {tema.replace('_', ' ').title()}\n\n"
            md_content += "| Artículo | Título | Palabra clave |\n"
            md_content += "|----------|--------|---------------|\n"
            for art in arts[:10]:
                titulo_corto = art["titulo"][:60] + "..." if len(art["titulo"]) > 60 else art["titulo"]
                md_content += f"| {art['numero']} | {titulo_corto} | {art['palabra_clave']} |\n"
            md_content += "\n"

    md_content += """## Referencias cruzadas

- [[decreto-555-extractos]] - Extractos del Decreto 555/2021 (POT base)
- [[03-retiros-obligatorios]] - Retiros estructurados
- [[04-edificabilidad-y-ocupacion]] - Edificabilidad estructurada
- [[05-alturas-maximas]] - Alturas máximas

## Notas de implementación

### Para el pipeline paramétrico
1. **El 555 sigue siendo la fuente principal** de normativa POT.
2. **El 670 añade precisiones** y actualizaciones (especialmente Anexo 5 Manual de Normas Comunes).
3. **Aplicar overrides del 670** cuando existan discrepancias con el 555.
4. **Verificar fecha de radicación** de licencias para régimen de transición.

### Incentivos urbanísticos (NUEVO en 670)
3 tipos de incentivos para proyectos con ecourbanismo:
- **Tipo 1:** Reducción mezcla de usos (8% → 3%) en Desarrollo y Renovación Urbana
- **Tipo 2:** Aumento área estacionamientos (Factor ECOS, +3%)
- **Tipo 3:** Disminución aislamiento lateral (15.70m en vez de 11.40m en Renovación)

### Fichas C/UNE (actualizadas en 670)
Las fichas de edificabilidad para predios Urbanizados No Edificados (C/UNE) se adoptan mediante el Artículo 239 del Decreto 670.
"""

    md_file = output_path / "decreto-670-extractos.md"
    md_file.write_text(md_content, encoding="utf-8")
    click.echo(f"  [OK] {md_file}")

    # =====================================================================
    # 5. Generar JSON con incentivos
    # =====================================================================
    click.echo("")
    click.echo("[5] Generando incentivos-670.json...")

    incentivos = {
        "_metadata": {
            "fuente": "Decreto 670 de 2025 - Libro 4, Parte 4 (Incentivos Urbanísticos)",
            "fecha_extraccion": "2026-08-01",
            "descripcion": "Incentivos urbanísticos por ecourbanismo y construcción sostenible",
            "decreto_origen": "582 de 2023 (compilado en 670)",
        },
        "tipos_incentivo": {
            "tipo_1_mezcla_usos": {
                "descripcion": "Disminución del Porcentaje de Condiciones de Mezcla de Usos",
                "reduccion": "de 8% a 3% del área construida a otros usos",
                "tratamientos_aplicables": ["Desarrollo", "Renovación Urbana"],
                "articulo_555_referencia": "Artículos 300 y 305 del Decreto 555/2021",
                "condiciones": [
                    "Predios en tratamiento de desarrollo con plan parcial que exija 8% a comercio y servicios",
                    "Predios en licencia con área > 2 hectáreas netas urbanizables",
                    "Predios en renovación urbana con englobe de manzana o plan parcial",
                ],
            },
            "tipo_2_estacionamientos": {
                "descripcion": "Aumento de área para Estacionamientos",
                "incremento": "+3% adicional al porcentaje opcional (Factor ECOS)",
                "base_legal": "Artículos 389 y 390 del Decreto 555/2021",
                "calculo": "sobre el área construida",
                "segun_area_actividad": True,
            },
            "tipo_3_aislamiento_lateral": {
                "descripcion": "Disminución exigencia de aislamiento lateral",
                "cambio_altura_inicio": "de 11.40m a 15.70m (en Renovación Urbana)",
                "no_incrementa_IC": True,
                "tratamientos_aplicables": ["Renovación Urbana", "Mejoramiento Integral"],
                "excepcion_mejoramiento": "Edificaciones ≥ 3 pisos sin edificación colindante mayor a 3 pisos pueden iniciar aislamiento desde el 4to piso",
            },
        },
        "aplicacion_por_tratamiento_area": {
            "desarrollo": {
                "estructurante_receptora_VIS": ["Tipo 1"],
                "estructurante_receptora_actividades_economicas": ["Tipo 2"],
                "proximidad_generadora_soportes_urbanos": ["Tipo 2"],
                "proximidad_receptora_soportes_urbanos": ["Tipo 2"],
                "grandes_servicios_metropolitanos": ["Tipo 2"],
            },
            "renovacion_urbana": {
                "todas_las_areas_actividad": ["Tipo 1", "Tipo 3"],
            },
            "mejoramiento_integral": {
                "aplica_tipo_3": True,
            },
        },
        "acceso_al_incentivo": {
            "regla_general": "El promotor puede acceder a SÓLO UNO de los tipos de incentivos",
            "segun_uso_y_tipo": "VIS/VIP y No VIS/VIP tienen acceso diferenciado",
            "manual_referencia": "Manual de Ecourbanismo y Construcción Sostenible",
        },
        "notas_importantes": [
            "Los incentivos requieren implementar medidas de ecourbanismo del Título II del Libro 4",
            "Aplicar siempre cumplimiento de fachadas activas (Artículo 243 del 555/2021)",
            "Para C/UNE en consolidación, aplicar fichas de edificabilidad adoptadas (Art. 239 del 670)",
        ],
    }

    incentivos_file = data_path / "incentivos-670.json"
    incentivos_file.write_text(json.dumps(incentivos, ensure_ascii=False, indent=2), encoding="utf-8")
    click.echo(f"  [OK] {incentivos_file}")

    # =====================================================================
    # 6. Generar JSON con actuaciones estratégicas
    # =====================================================================
    click.echo("")
    click.echo("[6] Generando actuaciones-estrategicas-670.json...")

    actuaciones = {
        "_metadata": {
            "fuente": "Decreto 670 de 2025 - Libro 5",
            "fecha_extraccion": "2026-08-01",
        },
        "actuaciones_estrategicas": {
            "ZIBo": {
                "nombre": "Actuación Estratégica Zona Industrial de Bogotá",
                "decreto_origen": "550 de 2025",
                "articulo_670": "Artículo 724+",
                "objetivo": "Consolidar Anillo de Innovación y Conocimiento (AICB) + CTIB",
                "linea_documento": 21549,
                "componentes": ["Planos", "Documento Técnico de Soporte", "Anexos ambientales"],
            },
            "Lagos_Torca": {
                "nombre": "Ciudad Lagos de Torca",
                "decreto_origen": "088 de 2017",
                "articulo_670": "Artículo 1093+",
                "tratamientos": ["Desarrollo", "Consolidación (3 modalidades)", "Conservación", "Renovación Urbana"],
                "linea_documento": 34690,
            },
            "Distrito_Aeroportuario_Engativa": {
                "nombre": "Actuación Estratégica Distrito Aeroportuario Engativá",
                "articulo_670": "Referenciado en Libro 5",
            },
            "Manzanas_Cuidado": {
                "nombre": "Manzanas del Cuidado",
                "descripcion": "Sistema Distrital del Cuidado",
                "indice_construccion_min": 0.8,
            },
        },
    }

    actuaciones_file = data_path / "actuaciones-estrategicas-670.json"
    actuaciones_file.write_text(json.dumps(actuaciones, ensure_ascii=False, indent=2), encoding="utf-8")
    click.echo(f"  [OK] {actuaciones_file}")

    # =====================================================================
    # 7. Generar JSON con estructura del decreto
    # =====================================================================
    click.echo("")
    click.echo("[7] Generando decreto-670-estructura.json...")

    estructura["articulos_por_tema"] = {}
    for tema, arts in articulos_por_tema.items():
        estructura["articulos_por_tema"][tema] = [
            {
                "numero": art["numero"],
                "titulo": art["titulo"],
                "linea": art["linea_inicio"],
                "palabra_clave": art["palabra_clave"],
            }
            for art in arts[:10]
        ]

    estructura["secciones_extraidas"] = {k: v["titulo"] for k, v in extractos.items()}

    estructura_file = data_path / "decreto-670-estructura.json"
    estructura_file.write_text(json.dumps(estructura, ensure_ascii=False, indent=2), encoding="utf-8")
    click.echo(f"  [OK] {estructura_file}")

    # =====================================================================
    # 8. Resumen
    # =====================================================================
    click.echo("")
    click.echo("=" * 60)
    click.echo("  EXTRACCIÓN DECRETO 670 COMPLETADA")
    click.echo("=" * 60)
    click.echo("")
    click.echo("Archivos generados:")
    click.echo(f"  [MD]   {md_file}")
    click.echo(f"  [JSON] {incentivos_file}")
    click.echo(f"  [JSON] {actuaciones_file}")
    click.echo(f"  [JSON] {estructura_file}")
    click.echo("")
    click.echo("PRÓXIMOS PASOS:")
    click.echo("  1. Integrar incentivos-670.json en MOTOR_DEMANDA.py (para opciones de mezcla de usos)")
    click.echo("  2. Integrar actuaciones-estrategicas-670.json en CONTEXTO_v09.py (zonas especiales)")
    click.echo("  3. En gpkg-to-cache-v4.py, agregar lectura de incentivos cuando el tratamiento aplique")
    click.echo("  4. Commitear:")
    click.echo('     git add -A && git commit -m "feat: integración Decreto 670/2025 (compilación POT)"')
    click.echo("")


if __name__ == "__main__":
    main()
