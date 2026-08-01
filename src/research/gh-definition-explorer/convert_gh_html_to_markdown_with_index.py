#!/usr/bin/env python3
"""
Etapa 1+2: Conversión HTML → Markdown + índices por namespace
==============================================================

Objetivo:
    - Recorrer todos los archivos .htm/.html del repo Grasshopper API Docs.
    - Convertirlos a Markdown manteniendo la estructura de carpetas.
    - Detectar namespaces por heurística basada en nombre de archivo.
    - Crear index.md por namespace con lista de clases y enlaces.
    - Crear index.md maestro en la raíz.

La heurística de namespaces está inspirada en la convención de nombres del repo:
    - N_GH_IO_Serialization.htm                  -> GH_IO.Serialization
    - N_Grasshopper_Kernel.htm                  -> Grasshopper.Kernel
    - T_GH_IO_Serialization_GH_Archive.htm       -> GH_IO.Serialization
    - T_GH_IO_Types_GH_BoundingBox.htm           -> GH_IO.Types
    - T_GH_IO_UserInterface_GH_ArchiveMessageViewer.htm -> GH_IO.UserInterface
    - T_Grasshopper_Kernel_GH_Document.htm       -> Grasshopper.Kernel
"""

import os
import argparse
from pathlib import Path
from typing import Dict, List, Tuple

from markdownify import markdownify as md  # HTML → Markdown [web:56]


# ============================================================================
# CONFIGURACIÓN POR DEFECTO
# ============================================================================

DEFAULT_SOURCE_ROOT = r"C:\Users\Dario Salas\proyectos\DiseñoParametrico_sistema\GhDefinitionExplorer\grasshopper-api-docs"
DEFAULT_OUTPUT_ROOT = r"C:\Users\Dario Salas\proyectos\DiseñoParametrico_sistema\GhDefinitionExplorer\output\markdown"
HTML_SUBPATH = r"api\grasshopper\html"

HTML_EXTENSIONS = {".htm", ".html"}

# Límite opcional de archivos (None = todos)
MAX_FILES = None

# Índices en memoria
namespaces_index: Dict[str, List[Tuple[str, Path]]] = {}  # ns -> [(class_name, md_rel)]
all_classes_index: List[Tuple[str, str, Path]] = []       # (ns, class_name, md_rel)


# ============================================================================
# PARÁMETROS DE LÍNEA DE COMANDO
# ============================================================================

def parse_args():
    parser = argparse.ArgumentParser(
        description="Etapa 1+2: Convertir Grasshopper API HTML → Markdown + índices por namespace"
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
    """Crea el directorio y todos los padres si no existen."""
    path.mkdir(parents=True, exist_ok=True)


def get_output_path(source_file: Path, source_root: Path, output_root: Path) -> Path:
    """
    Calcula la ruta de destino manteniendo la estructura relativa.
    """
    try:
        relative_path = source_file.relative_to(source_root)
    except ValueError:
        relative_path = Path(source_file.name)
    return output_root / relative_path


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
        heading_style="ATX",
        bullets="-",
        strip=["script", "style"],
    )


def infer_namespace_from_filename(fname: str) -> str:
    """
    Heurística basada en la convención de nombres de grasshopper-api-docs.

    Ejemplos:
    - N_GH_IO_Serialization.htm                  -> GH_IO.Serialization
    - N_Grasshopper_Kernel.htm                  -> Grasshopper.Kernel
    - T_GH_IO_Serialization_GH_Archive.htm       -> GH_IO.Serialization
    - T_GH_IO_Types_GH_BoundingBox.htm           -> GH_IO.Types
    - T_GH_IO_UserInterface_GH_ArchiveMessageViewer.htm -> GH_IO.UserInterface
    - T_Grasshopper_Kernel_GH_Document.htm       -> Grasshopper.Kernel
    """
    stem = Path(fname).stem
    parts = stem.split("_")

    if not parts:
        return ""

    prefix = parts[0]

    # N_* archivos de namespace
    if prefix == "N" and len(parts) >= 2:
        # N_Grasshopper_Kernel -> Grasshopper.Kernel
        # N_GH_IO_Serialization -> GH_IO.Serialization
        ns = ".".join(parts[1:])
        return ns

    # T_* archivos de tipo (clase)
    if prefix == "T" and len(parts) >= 3:
        # GH_IO.*
        if parts[1] == "GH" and parts[2] == "IO":
            if len(parts) >= 4:
                sub = parts[3]
                ns = f"GH_IO.{sub}"
                return ns
            else:
                return "GH_IO"

        # Grasshopper.*
        if parts[1] == "Grasshopper":
            if len(parts) >= 3:
                ns_parts = parts[1:-1]
                ns = ".".join(ns_parts)
                return ns
            else:
                return "Grasshopper"

        # fallback genérico
        return parts[1]

    # M_* archivos de métodos (similar lógica)
    if prefix == "M" and len(parts) >= 3:
        if parts[1] == "GH" and parts[2] == "IO":
            if len(parts) >= 4:
                sub = parts[3]
                ns = f"GH_IO.{sub}"
                return ns
            else:
                return "GH_IO"

        if parts[1] == "Grasshopper":
            if len(parts) >= 3:
                ns_parts = parts[1:-2]
                ns = ".".join(ns_parts) if ns_parts else "Grasshopper"
                return ns
            else:
                return "Grasshopper"

        return parts[1]

    return ""


def register_class_for_index(namespace: str, class_name: str, md_rel: Path):
    """
    Registra una clase para los índices de namespace y maestro.
    """
    namespaces_index.setdefault(namespace, []).append((class_name, md_rel))
    all_classes_index.append((namespace, class_name, md_rel))


def build_namespace_index_files(output_root: Path):
    """
    Crea index.md por namespace con enlaces a sus clases.
    """
    for ns, entries in namespaces_index.items():
        ns_dir = output_root / ns.replace(".", "/")
        ensure_dir_exists(ns_dir)
        index_path = ns_dir / "index.md"

        lines = [f"# Namespace {ns}\n", "## Clases\n"]

        for class_name, md_rel in sorted(entries, key=lambda e: e[0].lower()):
            rel_link = os.path.relpath(output_root / md_rel, ns_dir)
            lines.append(f"- [{class_name}]({rel_link})")

        index_path.write_text("\n".join(lines), encoding="utf-8")
        print(f"[INDEX] Namespace index creado: {index_path}")


def build_master_index(output_root: Path):
    """
    Crea índice maestro con enlaces a namespaces y clases.
    """
    master_path = output_root / "index.md"
    lines = ["# Índice maestro Grasshopper SDK\n"]

    lines.append("## Por namespace\n")
    for ns in sorted(namespaces_index.keys()):
        ns_index_rel = ns.replace(".", "/") + "/index.md"
        lines.append(f"- [{ns}]({ns_index_rel})")

    lines.append("\n## Todas las clases\n")
    for ns, class_name, md_rel in sorted(all_classes_index, key=lambda e: (e[0].lower(), e[1].lower())):
        rel_link = os.path.relpath(output_root / md_rel, output_root)
        lines.append(f"- **{ns}**: [{class_name}]({rel_link})")

    master_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"[INDEX] Índice maestro creado: {master_path}")


# ============================================================================
# FUNCIÓN PRINCIPAL
# ============================================================================

def main():
    args = parse_args()

    source_root = Path(args.source)
    output_root = Path(args.output)
    max_files = args.max_files if args.max_files is not None else MAX_FILES

    print("=" * 70)
    print("ETAPA 1+2: Conversión HTML → Markdown + índices por namespace")
    print("=" * 70)

    source_path = source_root / HTML_SUBPATH

    if not source_path.exists():
        print(f"\n[ERROR] No se encuentra la carpeta fuente:")
        print(f"  {source_path}")
        return

    print(f"\n[OK] Carpeta fuente encontrada: {source_path}")

    ensure_dir_exists(output_root)
    print(f"[OK] Carpeta de salida: {output_root}")

    # Conteo previo
    pre_count = sum(
        1
        for root, dirs, files in os.walk(source_path)
        for filename in files
        if Path(filename).suffix.lower() in HTML_EXTENSIONS
    )
    print(f"\n[INFO] Archivos HTML/HTM detectados: {pre_count}")

    if pre_count == 0:
        print("[ADVERTENCIA] No se encontraron archivos HTML/HTM.")
        return

    total_archivos = 0
    archivos_procesados = 0
    errores = 0

    print(f"\n{'─' * 70}")
    print("Iniciando recorrido y conversión...")
    print(f"{'─' * 70}\n")

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

                    with open(archivo_origen, "r", encoding="utf-8", errors="ignore") as f:
                        html_content = f.read()

                    md_content = convert_html_to_markdown(html_content)

                    # Encabezado simple: nombre de archivo sin extensión
                    title = archivo_origen.stem
                    md_content = f"# {title}\n\n" + md_content

                    with open(archivo_destino, "w", encoding="utf-8") as f:
                        f.write(md_content)

                    archivos_procesados += 1

                    # Detectar namespace y registrar clase si aplica
                    ns = infer_namespace_from_filename(filename)
                    if ns and archivo_origen.name.startswith("T_"):
                        # md_rel es la ruta relativa desde output_root
                        md_rel = archivo_destino_relativo.with_suffix(".md").relative_to(output_root)
                        register_class_for_index(ns, title, md_rel)

                    if archivos_procesados % 100 == 0:
                        print(f"  Procesados {archivos_procesados} archivos...")

                    if max_files is not None and archivos_procesados >= max_files:
                        print(f"\n[INFO] Se alcanzó el límite MAX_FILES={max_files}.")
                        break

                except Exception as e:
                    errores += 1
                    print(f"  [ERROR] No se pudo procesar {archivo_origen}: {str(e)[:80]}")

        if max_files is not None and archivos_procesados >= max_files:
            break

    # Crear índices por namespace y maestro
    print(f"\n[INFO] Creando índices por namespace y maestro...")
    build_namespace_index_files(output_root)
    build_master_index(output_root)

    # Resumen
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
        print(f"  La carpeta de salida es: {output_root}")
        print("  - index.md (maestro) referencia todos los namespaces y clases.")
        print("  - Cada namespace tiene su propio index.md en subcarpetas como GH_IO/Serialization/index.md.")
        print("  Obsidian puede abrir esta carpeta como vault de referencia. [web:11]")
    else:
        print(f"\n[ADVERTENCIA] No se procesaron archivos.")
        print(f"  Verifica que la ruta sea correcta y que haya .htm/.html en: {source_path}")


if __name__ == "__main__":
    main()