#!/usr/bin/env python3
# ==============================================================================
# extract-nsr-10-relevante.py
# ------------------------------------------------------------------------------
# Extrae las partes relevantes del Reglamento Colombiano de Construcción
# Sismo Resistente NSR-10 para el pipeline paramétrico.
#
# Genera:
#   1. docs/normativa/nsr-10/nsr-10-extractos.md
#   2. data/nsr-10/separaciones-sismicas.json
#   3. data/nsr-10/grupos-uso-coef-importancia.json
#   4. data/nsr-10/amenaza-sismica-bogota.json
#
# Uso:
#   python scripts/utilities/extract-nsr-10-relevante.py --input <ruta_a_Reglamentacion_NSR.md>
# ==============================================================================

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import click

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent


def extraer_seccion(texto: str, patron: str, lineas_despues: int = 80) -> str:
    """Extrae una sección del NSR usando regex."""
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


@click.command()
@click.option("--input", "-i", required=True, type=click.Path(exists=True))
@click.option("--output-dir", default=str(PROJECT_ROOT / "docs" / "normativa" / "nsr-10"))
@click.option("--data-dir", default=str(PROJECT_ROOT / "data" / "nsr-10"))
def main(input: str, output_dir: str, data_dir: str) -> None:
    """Extrae partes relevantes del NSR-10."""

    input_path = Path(input)
    output_path = Path(output_dir)
    data_path = Path(data_dir)

    output_path.mkdir(parents=True, exist_ok=True)
    data_path.mkdir(parents=True, exist_ok=True)

    click.echo(f"[INFO] Leyendo: {input_path}")
    texto = input_path.read_text(encoding="utf-8")
    click.echo(f"[INFO] Total líneas: {len(texto.splitlines())}")

    # =====================================================================
    # 1. Extraer secciones clave del NSR-10
    # =====================================================================
    click.echo("")
    click.echo("[1] Extrayendo secciones relevantes del NSR-10...")

    secciones = {
        "a_1_2_objeto": {
            "titulo": "A.1.2 - Objeto y organización del Reglamento",
            "patron": r"A\.1\.2\.2\s*—\s*OBJETO",
            "lineas": 30,
        },
        "a_2_2_movimientos_sismicos": {
            "titulo": "A.2.2 - Movimientos sísmicos de diseño (Aa, Av)",
            "patron": r"A\.2\.2\s*—\s*MOVIMIENTOS\s+S[ÍI]SMICOS\s+DE\s+DISE[ÑN]O",
            "lineas": 50,
        },
        "a_2_3_zonas_amenaza": {
            "titulo": "A.2.3 - Zonas de Amenaza Sísmica (Baja, Intermedia, Alta)",
            "patron": r"A\.2\.3\s*—\s*ZONAS\s+DE\s+AMENAZA\s+S[ÍI]SMICA",
            "lineas": 60,
        },
        "a_2_4_efectos_locales": {
            "titulo": "A.2.4 - Efectos locales (perfiles de suelo)",
            "patron": r"A\.2\.4\s*—\s*EFECTOS\s+LOCALES",
            "lineas": 80,
        },
        "a_2_5_coef_importancia": {
            "titulo": "A.2.5 - Coeficiente de Importancia (Grupos de Uso I-IV)",
            "patron": r"A\.2\.5\s*—\s*COEFICIENTE\s+DE\s+IMPORTANCIA",
            "lineas": 100,
        },
        "a_2_5_1_grupos_uso": {
            "titulo": "A.2.5.1 - Grupos de Uso (I, II, III, IV)",
            "patron": r"A\.2\.5\.1\s*—\s*GRUPOS\s+DE\s+USO",
            "lineas": 80,
        },
        "a_2_6_espectro": {
            "titulo": "A.2.6 - Espectro de diseño",
            "patron": r"A\.2\.6\s*—\s*ESPECTROS\s+DE\s+DISE[ÑN]O",
            "lineas": 60,
        },
        "a_6_5_separacion_sismica": {
            "titulo": "A.6.5 - Separación entre estructuras adyacentes (CRÍTICO)",
            "patron": r"A\.6\.5\s*—\s*SEPARACI[ÓO]N\s+ENTRE\s+ESTRUCTURAS\s+ADYACENTES",
            "lineas": 250,
        },
        "a_2_3_2_ciudades": {
            "titulo": "Tabla A.2.3-2 - Valores Aa y Av para ciudades capitales",
            "patron": r"Tabla\s*A\.2\.3-2",
            "lineas": 100,
        },
    }

    extractos = {}
    for key, config in secciones.items():
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
    # 2. Generar JSON de separaciones sísmicas (CRÍTICO para ANALISIS_VECINOS.py)
    # =====================================================================
    click.echo("")
    click.echo("[2] Generando separaciones-sismicas.json...")

    separaciones = {
        "_metadata": {
            "fuente": "NSR-10 - Título A, Sección A.6.5",
            "fecha_extraccion": "2026-08-01",
            "descripcion": "Separación sísmica mínima entre edificaciones colindantes",
            "aplica_para": "ANALISIS_VECINOS.py - cálculo de separaciones NSR-10",
        },
        "alcance": {
            "aplica": [
                "Edificaciones nuevas con licencia posterior a NSR-10 (2010)",
                "Solo en Zonas de Amenaza Sísmica Intermedia y Alta",
                "Edificaciones > 2 pisos aéreos en colindancia",
            ],
            "no_aplica": [
                "Zona de Amenaza Sísmica Baja (Aa y Av <= 0.10)",
                "Edificaciones de Reconocimiento (legalización)",
                "Edificaciones <= 2 pisos aéreos en colindancia",
                "Rehabilitación sísmica (ver A.10.7)",
            ],
            "excepcion_zona_via_publica": "Cuando el paramento colinda con vía pública o zona verde pública NO se requiere separación sísmica (sí se requieren retrocesos urbanísticos)",
        },
        "tabla_separacion_minima": {
            "descripcion": "Tabla A.6.5-1 - Separación sísmica mínima en cubierta",
            "casos": {
                "1_y_2_pisos_aereos": {
                    "existe_vecina_no_separo": "no requiere",
                    "coinciden_losas_vecina": "no requiere",
                    "no_coinciden_losas_vecina": "no requiere",
                    "no_existe_vecina": "no requiere",
                },
                "3_pisos_aereos": {
                    "existe_vecina_no_separo": "no requiere",
                    "coinciden_losas_vecina": "no requiere",
                    "no_coinciden_losas_vecina": "1% de hn (altura nueva en colindancia)",
                    "no_existe_vecina": "no requiere",
                },
                "mas_de_3_pisos_aereos": {
                    "existe_vecina_no_separo": "n/a",
                    "coinciden_losas_vecina": "2% de hn",
                    "no_coinciden_losas_vecina": "3% de hn",
                    "no_existe_vecina": "1% de hn",
                },
            },
            "nota_1": "Para pisos diferentes a cubierta, multiplicar coeficiente por la altura del piso en particular",
            "nota_2": "Cuando terreno inclinado o alturas de piso diferentes, usar el que conduzca a MAYOR separación",
        },
        "formulas_calculo": {
            "separacion_piso_i": "s_i = coeficiente_tabla × h_i",
            "donde": {
                "s_i": "separación sísmica en el piso i (metros)",
                "coeficiente_tabla": "1%, 2% o 3% según caso (0.01, 0.02, 0.03)",
                "h_i": "altura sobre el nivel del terreno del piso i (metros)",
                "h_n": "altura total de la edificación nueva en la colindancia (metros)",
            },
            "ejemplo": {
                "caso": "Edificación nueva de 5 pisos (h_n=15m), sin edificación vecina, junto a paramento privado",
                "coeficiente": 0.01,
                "separacion_cubierta": "0.01 × 15 = 0.15 m",
                "separacion_piso_3": "0.01 × 9 = 0.09 m (si h_3=9m)",
            },
        },
        "definiciones_clave": {
            "altura_piso": "Distancia vertical entre dos losas consecutivas",
            "altura_edificacion_colindancia": "h_n - altura de la edificación nueva medida en la colindancia",
            "cerramiento": "Muro divisorio entre dos predios, sin edificación",
            "coincidencia_losas_entrepiso": "Cuando las losas de la edificación nueva y vecina están al mismo nivel en la colindancia",
            "numero_pisos_aereos": "Número de pisos sobre el nivel del terreno",
            "separacion_sismica_colindancia": "Distancia horizontal entre la edificación nueva y el paramento del lote",
        },
        "recomendaciones_adicionales": {
            "precauciones": [
                "Evitar depósito de materiales extraños en la separación sísmica",
                "Colocar protección de humedad para agua lluvia",
                "Indicar paramento y separación en planos arquitectónicos",
            ],
            "casos_especiales": [
                "Edificaciones de refuerzo/rehabilitación: ingeniero debe estudiar interacción con vecinas (A.10.1.7)",
                "Terrenos inclinados: usar altura que conduzca a mayor separación",
                "Diferentes alturas de piso o número de pisos: tomar el peor caso",
            ],
        },
        "relacion_con_pot_bogota": {
            "pot_retiro_urbano": "El POT exige retiros urbanísticos (3.0m por defecto en consolidación)",
            "nsr_separacion_sismica": "El NSR exige separación sísmica adicional si la edificación vecina no se ha separado",
            "aplicacion_conjunta": "Tomar el MAYOR valor entre retiro urbanístico y separación sísmica",
            "ejemplo": "Si POT exige retiro frontal 3.0m y NSR exige separación sísmica 0.45m → usar 3.0m (mayor)",
        },
    }

    sep_file = data_path / "separaciones-sismicas.json"
    sep_file.write_text(json.dumps(separaciones, ensure_ascii=False, indent=2), encoding="utf-8")
    click.echo(f"  [OK] {sep_file}")

    # =====================================================================
    # 3. Generar JSON de grupos de uso y coeficientes
    # =====================================================================
    click.echo("")
    click.echo("[3] Generando grupos-uso-coef-importancia.json...")

    grupos_uso = {
        "_metadata": {
            "fuente": "NSR-10 - Sección A.2.5",
            "fecha_extraccion": "2026-08-01",
            "descripcion": "Grupos de uso y coeficientes de importancia para diseño sísmico",
        },
        "grupos": {
            "IV": {
                "nombre": "Edificaciones indispensables",
                "coeficiente_importancia_I": 1.50,
                "descripcion": "Atención a la comunidad que debe funcionar durante y después de un sismo",
                "incluye": [
                    "Hospitales, clínicas y centros de salud con cirugía, UCI, neonatos, urgencias",
                    "Aeropuertos, estaciones ferroviarias y de transporte masivo",
                    "Centrales telefónicas, telecomunicación, radiodifusión",
                    "Refugios para emergencias, centrales de aeronavegación",
                    "Centrales de operación de líneas vitales (energía, agua, combustibles)",
                    "Edificaciones con agentes explosivos, tóxicos, dañinos",
                    "Plantas de generación eléctrica de emergencia",
                    "Tanques y sistemas contra incendio",
                ],
            },
            "III": {
                "nombre": "Edificaciones de atención a la comunidad",
                "coeficiente_importancia_I": 1.25,
                "descripcion": "Indispensables después de un temblor para atender emergencia y preservar salud",
                "incluye": [
                    "Estaciones de bomberos, defensa civil, policía, cuarteles",
                    "Garajes de vehículos de emergencia",
                    "Estructuras y equipos de centros de atención de emergencias",
                    "Guarderías, escuelas, colegios, universidades",
                    "Edificaciones del Grupo II con seguridad adicional",
                    "Designadas por administración municipal/distrital/nacional",
                ],
            },
            "II": {
                "nombre": "Estructuras de ocupación especial",
                "coeficiente_importancia_I": 1.10,
                "descripcion": "Ocupación especial o concentración de personas",
                "incluye": [
                    "Edificaciones con > 200 personas en un mismo salón",
                    "Graderías al aire libre con > 2000 personas",
                    "Almacenes y centros comerciales con > 500 m² por piso",
                    "Hospitales, clínicas y centros de salud no cubiertos en Grupo IV",
                    "Edificaciones donde trabajan o residan > 3000 personas",
                    "Edificios gubernamentales",
                ],
            },
            "I": {
                "nombre": "Estructuras de ocupación normal",
                "coeficiente_importancia_I": 1.00,
                "descripcion": "Todas las edificaciones no incluidas en Grupos II, III y IV",
                "incluye": [
                    "Vivienda unifamiliar y multifamiliar normal",
                    "Oficinas sin concentración masiva de personas",
                    "Comercio pequeño (< 500 m² por piso)",
                    "Bodegas sin alto riesgo",
                ],
            },
        },
        "tabla_valores_I": {
            "IV": 1.50,
            "III": 1.25,
            "II": 1.10,
            "I": 1.00,
        },
        "notas": [
            "El coeficiente I modifica el espectro de diseño - mayor I = mayores fuerzas sísmicas",
            "Grupos II, III, IV consideran valores con probabilidad menor de excedencia (no 10% en 50 años)",
            "Grupo I: probabilidad 10% en 50 años (referencia base)",
            "Casas de 1-2 pisos del Grupo I pueden usar método simplificado (Título E)",
        ],
    }

    grupos_file = data_path / "grupos-uso-coef-importancia.json"
    grupos_file.write_text(json.dumps(grupos_uso, ensure_ascii=False, indent=2), encoding="utf-8")
    click.echo(f"  [OK] {grupos_file}")

    # =====================================================================
    # 4. Generar JSON de amenaza sísmica Bogotá
    # =====================================================================
    click.echo("")
    click.echo("[4] Generando amenaza-sismica-bogota.json...")

    amenaza = {
        "_metadata": {
            "fuente": "NSR-10 - Tabla A.2.3-2 (ciudades capitales) + A.2.3 (zonas)",
            "fecha_extraccion": "2026-08-01",
            "descripcion": "Valores de amenaza sísmica para Bogotá D.C.",
        },
        "bogota_dc": {
            "Aa_aceleracion_pico_efectiva": 0.15,
            "Av_velocidad_pico_efectiva": 0.20,
            "zona_amenaza": "INTERMEDIA (Av > 0.10 y <= 0.20)",
            "fuente_tabla": "Tabla A.2.3-2 del NSR-10",
        },
        "zonas_amenaza_sismica": {
            "Baja": {
                "criterio": "Aa y Av menores o iguales a 0.10",
                "implicaciones": [
                    "No se requieren consideraciones de separación sísmica entre edificaciones vecinas (A.6.5.2.1.a)",
                    "Diseño sísmico menos exigente",
                    "Casas de 1-2 pisos pueden usar método simplificado (Título E)",
                ],
            },
            "Intermedia": {
                "criterio": "Aa o Av mayores de 0.10 y ninguno excede 0.20",
                "implicaciones": [
                    "SÍ aplican requisitos de separación sísmica (A.6.5)",
                    "Diseño sísmico estándar",
                    "Bogotá está en esta zona",
                ],
            },
            "Alta": {
                "criterio": "Aa o Av mayores que 0.20",
                "implicaciones": [
                    "SÍ aplican requisitos de separación sísmica (A.6.5)",
                    "Diseño sísmico más exigente",
                    "Estudios geotécnicos más detallados",
                ],
            },
        },
        "regiones_sismicas": {
            "descripcion": "Tabla A.2.2-1 - Valores por región (1-10)",
            "tabla": {
                "region_1": {"Aa": 0.05, "Av": 0.05},
                "region_2": {"Aa": 0.10, "Av": 0.10},
                "region_3": {"Aa": 0.15, "Av": 0.15},
                "region_4": {"Aa": 0.20, "Av": 0.20},
                "region_5": {"Aa": 0.25, "Av": 0.25},
                "region_6": {"Aa": 0.30, "Av": 0.30},
                "region_7": {"Aa": 0.35, "Av": 0.35},
                "region_8": {"Aa": 0.40, "Av": 0.40},
                "region_9": {"Aa": 0.45, "Av": 0.45},
                "region_10": {"Aa": 0.50, "Av": 0.50},
            },
        },
        "microzonificacion_bogota": {
            "descripcion": "Bogotá tiene microzonificación sísmica propia (Decreto 523/2010, compilado en 670/2025)",
            "fuente": "Decreto 670 de 2025 - Libro 1, Título 1",
            "importancia": "Estudio detallado que reemplaza valores genéricos del NSR-10 para Bogotá",
            "aplicacion": "Para proyectos en Bogotá se debe usar la microzonificación oficial, no solo los valores Aa/Av del NSR-10",
        },
        "implicaciones_para_pipeline": {
            "bogota_aplica_separacion_sismica": True,
            "bogota_zona_amenaza": "Intermedia",
            "edificaciones_3_pisos_requieren_separacion": True,
            "edificaciones_mas_3_pisos_requieren_separacion": True,
            "casas_1_2_pisos_no_requieren": True,
            "parametro_para_analisis_vecinos": "Si lote en Bogotá y proyecto > 2 pisos: aplicar A.6.5",
        },
    }

    amenaza_file = data_path / "amenaza-sismica-bogota.json"
    amenaza_file.write_text(json.dumps(amenaza, ensure_ascii=False, indent=2), encoding="utf-8")
    click.echo(f"  [OK] {amenaza_file}")

    # =====================================================================
    # 5. Generar Markdown consolidado
    # =====================================================================
    click.echo("")
    click.echo("[5] Generando Markdown consolidado...")

    md_content = """---
fecha: 2026-08-01
tipo: referencia
fase: transversal
estado: activo
tags: [nsr-10, sismo-resistente, bogota, normativa, separacion-sismica]
---

# NSR-10 - Extractos Relevantes para Pipeline Paramétrico

**Fuente:** Reglamento Colombiano de Construcción Sismo Resistente NSR-10
**Fecha de expedición:** 26 de marzo de 2010 (Diario Oficial 47.663)
**Entidad:** Ministerio de Ambiente, Vivienda y Desarrollo Territorial

## Estructura del NSR-10

El reglamento está organizado en 11 títulos:

| Título | Tema | Relevancia para pipeline |
|--------|------|---------------------------|
| **A** | Requisitos generales de diseño y construcción sismo resistente | ⭐⭐⭐ CRÍTICO |
| B | Cargas | ⭐⭐ |
| C | Concreto estructural | ⭐ |
| D | Mampostería estructural | ⭐ |
| E | Casas de uno y dos pisos | ⭐⭐ |
| F | Estructuras metálicas | ⭐ |
| G | Estructuras de madera y guadua | ⭐ |
| H | Estudios geotécnicos | ⭐⭐ |
| I | Supervisión técnica | ⭐ |
| J | Requisitos de protección contra incendios | ⭐⭐ |
| K | Requisitos complementarios | ⭐ |

## Bogotá D.C. - Valores NSR-10

| Parámetro | Valor | Fuente |
|-----------|-------|--------|
| **Aa** (aceleración pico efectiva) | **0.15** | Tabla A.2.3-2 |
| **Av** (velocidad pico efectiva) | **0.20** | Tabla A.2.3-2 |
| **Zona de amenaza sísmica** | **Intermedia** | A.2.3.2 |
| **Microzonificación** | Sí (Decreto 523/2010, compilado en 670/2025) | A.2.1.2.1 |

## Aplicabilidad para el pipeline

### En Bogotá D.C. SÍ aplican:
- ✅ Requisitos de separación sísmica entre edificaciones vecinas (A.6.5)
- ✅ Para edificaciones > 2 pisos aéreos en colindancia
- ✅ Microzonificación sísmica propia (más detallada que NSR-10 genérico)

### En Bogotá D.C. NO aplican (excepciones):
- ❌ Casas de 1-2 pisos (no requieren separación sísmica)
- ❌ Edificaciones con paramento colindante con vía pública o zona verde pública
- ❌ Edificaciones de Reconocimiento (legalización)

## Para ANALISIS_VECINOS.py

La función principal del NSR-10 en el pipeline es el cálculo de **separaciones sísmicas**
entre la edificación nueva y los vecinos. Esto se suma a los retiros urbanísticos del POT.

### Regla de aplicación
```
separación_final = MÁXIMO(retiro_urbano_POT, separación_sísmica_NSR)
```

### Tabla A.6.5-1 (resumen)

| Pisos aéreos en colindancia | Vecina no se separó | Losas coinciden | Losas no coinciden | Sin vecina |
|------------------------------|---------------------|-----------------|--------------------|-------------|
| 1-2 pisos | no requiere | no requiere | no requiere | no requiere |
| 3 pisos | no requiere | no requiere | **1% de hn** | no requiere |
| >3 pisos | n/a | **2% de hn** | **3% de hn** | **1% de hn** |

Donde `hn` = altura de la edificación nueva en la colindancia.

## Extractos completos

"""

    for key, data in extractos.items():
        md_content += f"## {data['titulo']}\n\n"
        md_content += f"```\n{data['contenido']}\n```\n\n---\n\n"

    md_content += """## Referencias cruzadas

- [[decreto-555-extractos]] - POT Bogotá
- [[decreto-670-extractos]] - Compilación POT
- [[03-retiros-obligatorios]] - Retiros POT
- [[04-edificabilidad-y-ocupacion]] - Edificabilidad POT

## JSONs estructurados generados

- `data/nsr-10/separaciones-sismicas.json` - Tabla A.6.5-1 estructurada
- `data/nsr-10/grupos-uso-coef-importancia.json` - Grupos I-IV con coeficientes
- `data/nsr-10/amenaza-sismica-bogota.json` - Valores Aa/Av para Bogotá

## Notas de implementación

### Para CONTEXTO_v09.py
- Cargar `amenaza-sismica-bogota.json` para verificar si aplican separaciones
- Bogotá está en Zona Intermedia → SÍ aplican requisitos A.6.5

### Para ANALISIS_VECINOS.py
- Cargar `separaciones-sismicas.json` para tabla A.6.5-1
- Calcular separación según número de pisos del proyecto (parámetro de entrada)
- Comparar con retiros urbanísticos del POT (tomar el mayor)

### Para VOLUMEN_v04.py
- Considerar coeficiente de importancia según grupo de uso
- Edificaciones residenciales normales: Grupo I, I=1.00
- Si el proyecto incluye >200 personas en un salón: Grupo II, I=1.10
"""

    md_file = output_path / "nsr-10-extractos.md"
    md_file.write_text(md_content, encoding="utf-8")
    click.echo(f"  [OK] {md_file}")

    # =====================================================================
    # 6. Resumen
    # =====================================================================
    click.echo("")
    click.echo("=" * 60)
    click.echo("  EXTRACCIÓN NSR-10 COMPLETADA")
    click.echo("=" * 60)
    click.echo("")
    click.echo("Archivos generados:")
    click.echo(f"  [MD]   {md_file}")
    click.echo(f"  [JSON] {sep_file}")
    click.echo(f"  [JSON] {grupos_file}")
    click.echo(f"  [JSON] {amenaza_file}")
    click.echo("")
    click.echo("PRÓXIMOS PASOS:")
    click.echo("  1. Integrar separaciones-sismicas.json en ANALISIS_VECINOS.py")
    click.echo("  2. Integrar amenaza-sismica-bogota.json en CONTEXTO_v09.py")
    click.echo("  3. Cargar grupos-uso-coef-importancia.json en VOLUMEN_v04.py")
    click.echo("  4. Commitear:")
    click.echo('     git add -A && git commit -m "feat: integración NSR-10 + separaciones sísmicas + Bogotá amenaza intermedia"')
    click.echo("")


if __name__ == "__main__":
    main()
