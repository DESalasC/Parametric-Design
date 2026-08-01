#!/usr/bin/env python3
"""
Etapa 1: Conversión mínima HTML → Markdown para Grasshopper API Docs
====================================================================

Objetivo:
    - Recorrer todos los archivos .htm/.html del repositorio clonado.
    - Convertirlos a Markdown manteniendo la estructura de carpetas.
    - Preparar la salida para uso en Obsidian, NotebookLM, Graphify.

Mejoras:
    - Conteo previo de archivos HTML.
    - Parámetros de línea de comando para source/output.
    - Límite opcional de archivos procesados (MAX_FILES) para pruebas.
    - Hook para manejo futuro de imágenes.
    - Encabezado # título al inicio de cada archivo Markdown.
"""

import os
import argparse
from pathlib import Path

from markdownify import markdownify as md  # HTML → Markdown [web:56]


# ============================================================================
# CONFIGURACIÓN POR DEFECTO (puedes sobreescribir vía argumentos)
# ============================================================================

DEFAULT_SOURCE_ROOT = r"C:\Users\Dario Salas\proyectos\DiseñoParametrico_sistema\GhDefinitionExplorer\grasshopper-api-docs"
DEFAULT_OUTPUT_ROOT = r"C:\Users\Dario Salas\proyectos\DiseñoParametrico_sistema\GhDefinitionExplorer\output\markdown"
HTML_SUBPATH = r"api\grasshopper\html"

HTML_EXTENSIONS = {".htm", ".html"}

# Para pruebas puedes limitar el número de archivos procesados:
# None = sin límite, procesa todos
MAX_FILES = None  # por ejemplo, 500 para pruebas rápidas


# ============================================================================
# PARÁMETROS DE LÍNEA DE COMANDO
# ============================================================================

def parse_args():
    parser = argparse.ArgumentParser(
        description="Etapa 1: Convertir Grasshopper API HTML → Markdown"
    )
    parser.add_argument(
        "--source",
        type=str,
        default=DEFAULT_SOURCE_ROOT,
        help=f"Ruta raíz del repo clonado (por defecto: {DEFAULT_SOURCE_ROOT})",
    )
    parser.add_argument(
        "--output",
        type=str,
        default=DEFAULT_OUTPUT_ROOT,
        help=f"Ruta raíz de salida Markdown (por defecto: {DEFAULT_OUTPUT_ROOT})",
    )
    parser.add_argument(
        "--max-files",
        type=int,
        default=None,
        help="Número máximo de archivos a procesar (None = todos).",
    )
    return parser.parse_args()


# ============================================================================
# FUNCIONES AUXILIARES
# ============================================================================

def ensure_dir_exists(path: Path):
    """Crea el directorio y todos los padres si no existen (mkdir -p)."""
    path.mkdir(parents=True, exist_ok=True)


def get_output_path(source_file: Path, source_root: Path, output_root: Path) -> Path:
    """
    Calcula la ruta de destino manteniendo la estructura relativa.

    Ejemplo:
        source_root\\subdir\\file.htm  ->  output_root\\subdir\\file.md
    """
    try:
        relative_path = source_file.relative_to(source_root)
    except ValueError:
        # Si no se puede hacer relativo (caso raro), usar solo el nombre
        relative_path = Path(source_file.name)

    return output_root / relative_path


def process_images_in_html(html_content: str, source_file: Path, output_root: Path) -> str:
    """
    Hook para manejo de imágenes.

    Versión Etapa 1:
        - No modifica el contenido.
    Etapas futuras:
        - Detectar <img src="...">.
        - Copiar imágenes a output_root/_assets.
        - Actualizar rutas en el HTML/Markdown.
    """
    return html_content


def convert_html_to_markdown(html_content: str) -> str:
    """
    Convierte contenido HTML a Markdown usando markdownify.

    Convenciones:
        - Encabezados estilo ATX (#, ##, etc.) [web:56][web:62]
        - Listas con guiones.
        - Elimina <script> y <style>.
    """
    return md(
        html_content,
        heading_style="ATX",        # Encabezados con # en lugar de subrayado [web:62]
        bullets="-",                # Usar - para listas
        strip=["script", "style"],  # Eliminar scripts y estilos
    )


# ============================================================================
# FUNCIÓN PRINCIPAL
# ============================================================================

def main():
    args = parse_args()

    source_root = Path(args.source)
    output_root = Path(args.output)
    max_files = args.max_files if args.max_files is not None else MAX_FILES

    print("=" * 70)
    print("ETAPA 1: Conversión HTML → Markdown")
    print("=" * 70)

    # Construir ruta a la carpeta HTML dentro del repo
    source_path = source_root / HTML_SUBPATH

    # Verificar que existe la carpeta fuente
    if not source_path.exists():
        print(f"\n[ERROR] No se encuentra la carpeta fuente:")
        print(f"  {source_path}")
        print(f"\nVerifica que:")
        print(f"  - La ruta raíz del repo (--source) es correcta.")
        print(f"  - El subpath HTML_SUBPATH coincide con la estructura del repo.")
        return

    print(f"\n[OK] Carpeta fuente encontrada: {source_path}")

    # Crear carpeta de salida
    ensure_dir_exists(output_root)
    print(f"[OK] Carpeta de salida: {output_root}")

    # Conteo previo de archivos HTML
    pre_count = sum(
        1
        for root, dirs, files in os.walk(source_path)
        for filename in files
        if Path(filename).suffix.lower() in HTML_EXTENSIONS
    )
    print(f"\n[INFO] Archivos HTML/HTM detectados: {pre_count}")
    if pre_count == 0:
        print("[ADVERTENCIA] No se encontraron archivos HTML/HTM. Revisa la estructura.")
        return

    # Contadores
    total_archivos = 0
    archivos_procesados = 0
    errores = 0
    converted_files = []

    print(f"\n{'─' * 70}")
    print("Iniciando recorrido y conversión...")
    print(f"{'─' * 70}\n")

    # Recorrer todos los archivos
    for root, dirs, files in os.walk(source_path):
        for filename in files:
            ext = Path(filename).suffix.lower()
            if ext in HTML_EXTENSIONS:
                total_archivos += 1

                archivo_origen = Path(root) / filename
                archivo_destino_relativo = get_output_path(
                    archivo_origen, source_path, output_root
                )
                archivo_destino = archivo_destino_relativo.with_suffix(".md")

                try:
                    ensure_dir_exists(archivo_destino.parent)

                    # Leer HTML
                    with open(archivo_origen, "r", encoding="utf-8", errors="ignore") as f:
                        html_content = f.read()

                    # Hook para imágenes (Etapa 1: no hace nada)
                    html_content = process_images_in_html(html_content, archivo_origen, output_root)

                    # Convertir a Markdown
                    md_content = convert_html_to_markdown(html_content)

                    # Encabezado simple con título basado en nombre de archivo
                    title = archivo_origen.stem
                    md_content = f"# {title}\n\n" + md_content

                    # Escribir Markdown
                    with open(archivo_destino, "w", encoding="utf-8") as f:
                        f.write(md_content)

                    archivos_procesados += 1
                    converted_files.append(archivo_destino_relativo.with_suffix(".md"))

                    # Progreso
                    if archivos_procesados % 100 == 0:
                        print(f"  Procesados {archivos_procesados} archivos...")

                    # Límite opcional de archivos (para pruebas)
                    if max_files is not None and archivos_procesados >= max_files:
                        print(f"\n[INFO] Se alcanzó el límite MAX_FILES={max_files}.")
                        break

                except Exception as e:
                    errores += 1
                    print(f"  [ERROR] No se pudo procesar {archivo_origen}: {str(e)[:80]}")

        if max_files is not None and archivos_procesados >= max_files:
            break

    # ============================================================================
    # RESUMEN FINAL
    # ============================================================================

    print(f"\n{'=' * 70}")
    print("RESUMEN DE LA CONVERSIÓN")
    print(f"{'=' * 70}")
    print(f"  Archivos HTML/HTM encontrados (previo): {pre_count}")
    print(f"  Archivos HTML/HTM recorridos:          {total_archivos}")
    print(f"  Archivos Markdown generados:           {archivos_procesados}")
    print(f"  Errores durante el proceso:            {errores}")
    print(f"{'=' * 70}")

    if archivos_procesados > 0:
        print(f"\n[ÉXITO] Conversión completada.")
        print(f"  Los archivos están en: {output_root}")
        print("  Obsidian puede abrir esta carpeta como vault de referencia. [web:11]")
        if max_files is not None:
            print(f"  Nota: solo se procesaron los primeros {archivos_procesados} archivos "
                  f"(MAX_FILES={max_files}).")
    else:
        print(f"\n[ADVERTENCIA] No se procesaron archivos.")
        print(f"  Verifica que la ruta sea correcta:")
        print(f"  {source_path}")
        print(f"  Y que contenga archivos .htm o .html.")


# ============================================================================
# PUNTO DE ENTRADA
# ============================================================================

if __name__ == "__main__":
    main()