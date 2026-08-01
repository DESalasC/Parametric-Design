# GhDefinitionExplorer — Claude Code Configuration

Este proyecto se centra en explorar y documentar definiciones de Grasshopper (`.gh` / `.ghx`) usando `GH_IO.dll` y la documentación técnica local de Grasshopper.

## 1. Alcance del proyecto

- Leer archivos `.gh` y `.ghx` usando `GH_IO.dll`.
- Volcar su estructura (chunks/items) a logs legibles.
- Diseñar un modelo intermedio (`definition.json`) sin hacer suposiciones sobre el formato.
- Usar la documentación local de Grasshopper como fuente de verdad técnica.

## 2. Rutas importantes

- Código del explorador:
  - `GhDefinitionExplorer/Program.cs`
  - `GhDefinitionExplorer/GhDefinitionExplorer.csproj`
- Documentación técnica de Grasshopper:
  - `GhDefinitionExplorer/output/markdown/GH_IO/`
    - `GH/index.md`
    - `Serialization/index.md`
    - `Types/index.md`
    - `UserInterfase/index.md`
    - `VersionNumber/index.md`
- Salidas esperadas:
  - Logs de exploración: `docs/knowledge-base/ghx-samples/logs/`
  - Futuros JSON de definición: `docs/knowledge-base/ghx-samples/exports/`

## 3. Reglas específicas para GH_IO y el explorador

1. **Antes de tocar código de GH_IO**:
   - leer `output/markdown/GH_IO/GH/index.md`
   - leer `output/markdown/GH_IO/Serialization/index.md`
2. **No inventar API**:
   - no crear métodos, propiedades o clases que no aparezcan en la documentación local.
   - si falta claridad, buscar primero en los índices y luego pedir ayuda.
3. **Formato de archivos Grasshopper**:
   - no modificar directamente el XML de `.ghx` sin pasar por `GH_IO.dll` o métodos documentados.
   - tratar `.gh` y `.ghx` como formatos controlados por `GH_IO.Serialization`, no como texto libre.
4. **Logs y salidas**:
   - los logs de exploración van en `docs/knowledge-base/ghx-samples/logs/` con nombre `test_XX_*.log`.
   - no escribir logs ni JSON en la raíz del proyecto.

## 4. Cómo trabajar con Program.cs y el .csproj

- **Siempre** leer `GhDefinitionExplorer.csproj` antes de cambiar referencias.
- Mantener la referencia a `GH_IO.dll` apuntando a la ruta correcta de Rhino/Grasshopper.
- No mezclar lógica de exploración con lógica de exportación; mantener funciones claras y pequeñas.
- Antes de cambios grandes, revisar:
  - `docs/Pipeline.md`
  - `docs/ARQUITECTURA.md`

## 5. Relación con Ruflo y el CLAUDE.md global

- Ruflo gestiona memoria y coordinación a nivel sistema.
- Este archivo define reglas locales de este subproyecto.
- En caso de conflicto:
  - seguir las reglas de **seguridad y memoria** de Ruflo,
  - pero respetar las reglas técnicas específicas de GH_IO indicadas aquí.

## 6. Estilo de cambios y validación

- Preferir cambios pequeños y verificables:
  - ajustar un método a la vez,
  - compilar y revisar errores de compilación como señal de desajuste de API.
- Tras cualquier cambio en el explorador:
  - compilar (`dotnet build`) desde `GhDefinitionExplorer`.
  - probar al menos un archivo `.gh` sencillo (`test_01_single_slider.gh`) y generar un log.
- Documentar hallazgos importantes sobre estructura de `.gh` / `.ghx` en:
  - `docs/Pipeline.md` (flujo),
  - o notas de `docs/knowledge-base/ghx-samples/notes/`.

## 7. Uso con Obsidian y Graphify

- Las notas de `output/markdown/GH_IO/` son parte del vault de Obsidian.
- Graphify puede leer estas notas y generar un grafo:
  - usar `/graphify GH_IO` o `/graphify Serialization` 