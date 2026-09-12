# GhIoIndexGenerator

`GhIoIndexGenerator` es una herramienta de consola (.NET) que genera un índice en Markdown de los tipos públicos definidos en `GH_IO.dll`.  
El índice resultante (`GH_IO-index.md`) se usa como mapa textual de la biblioteca GH_IO dentro del sistema de documentación (`GhDefinitionExplorer` + bóveda de Obsidian).[web:233][web:247][web:250]

---

## Propósito

- Enumerar automáticamente clases, estructuras, interfaces y enumeraciones de GH_IO.dll usando Reflection.[web:286][web:288]
- Agrupar los tipos por namespace (`GH_IO`, `GH_IO.Serialization`, `GH_IO.Types`, `GH_IO.UserInterface`, etc.).[web:233][web:247][web:250][web:282]
- Generar un archivo Markdown que sirve como referencia global y checklist de notas de clase “pendientes” o ya existentes.

Este índice complementa las notas manuales como:

- `GH_Archive.md`
- `GH_Chunk.md`
- `GH_Message.md`
- `gh_io-serialization.md`
- `gh_io-types.md`

---

## Funcionamiento

El programa realiza los siguientes pasos:

1. Carga `GH_IO.dll` desde la instalación de Rhino / Grasshopper usando `Assembly.LoadFrom`.[web:286][web:305][web:306]
2. Obtiene todos los tipos públicos con `GetTypes()`.[web:286][web:288]
3. Agrupa los tipos por namespace.
4. Para cada tipo, determina su categoría (class, struct, interface, enum).
5. Genera un archivo Markdown con secciones por namespace y líneas por tipo:

   ```markdown
   ## GH_IO.Serialization

   - Class `GH_Archive` – nota esperada: [[GH_Archive]]
   - Class `GH_Chunk` – nota esperada: [[GH_Chunk]]
   - Class `GH_Message` – nota esperada: [[GH_Message]]
   - Interface `GH_IChunk` – pendiente de nota
   - Interface `GH_IReader` – pendiente de nota
   - Interface `GH_IWriter` – pendiente de nota
   - Struct `ID` – pendiente de nota
   - Enum `GH_Message_Type` – pendiente de nota
   ```

6. Escribe el resultado en la ruta configurada para la documentación, por ejemplo:

   ```text
   C:\Users\Dario Salas\proyectos\DiseñoParametrico_sistema\GhDefinitionExplorer\output\markdown\GH_IO-index.md
   ```

---

## Configuración

La ruta de `GH_IO.dll` se configura en `Program.cs`:

```csharp
var ghIoPath = @"C:\Program Files\Rhino 8\Plug-ins\Grasshopper\GH_IO.dll";
```

Si se quiere generar el índice contra otra versión (por ejemplo la del paquete NuGet `grasshopper`), se puede cambiar a:

```csharp
var ghIoPath = @"C:\Users\Dario Salas\.nuget\packages\grasshopper\7.38.24338.17001\lib\net48\GH_IO.dll";
```

Asegúrate de que el archivo exista; de lo contrario, el programa mostrará:

```text
[ERROR] No se encontró GH_IO.dll en: <ruta>
```

---

## Uso

### Compilar

Desde la carpeta del proyecto:

```bash
dotnet build
```

Esto compila `GhIoIndexGenerator` y genera `bin\Debug\net10.0\GhIoIndexGenerator.dll`.

### Ejecutar

Para generar o refrescar el índice:

```bash
dotnet run
```

Si todo está correctamente configurado, verás:

```text
[OK] Índice GH_IO generado en: C:\Users\Dario Salas\proyectos\DiseñoParametrico_sistema\GhDefinitionExplorer\output\markdown\GH_IO-index.md
```

---

## Integración con el proyecto principal

Este proyecto se integra con `GhDefinitionExplorer` y la bóveda de documentación de la siguiente forma:

- `GhDefinitionExplorer` genera documentación Markdown a partir de definiciones de Grasshopper (archivos .gh / .ghx).
- `GhIoIndexGenerator` genera el índice `GH_IO-index.md` a partir de `GH_IO.dll`.
- La carpeta `output/markdown` (o la carpeta sincronizada con Obsidian) contiene:
  - notas generadas por tu herramienta,
  - notas manuales (por ejemplo `GH_Archive.md`),
  - el índice `GH_IO-index.md`.

Opcionalmente, se puede añadir un paso al pipeline de build (script o target de MSBuild) que ejecute `GhIoIndexGenerator` después de compilar el proyecto principal.[web:307][web:316]

---

## Convención de notas

El índice usa una convención simple para marcar notas esperadas:

- Para algunos tipos clave (por ejemplo, `GH_Archive`, `GH_Chunk`, `GH_Message`), el índice muestra:

  ```markdown
  nota esperada: [[GH_Archive]]
  ```

- Para el resto, muestra:

  ```markdown
  pendiente de nota
  ```

Cuando se crea una nueva nota de clase en la bóveda, se puede:

- cambiar la convención de nombre de archivo si hace falta,
- actualizar la función `GetNoteHint` en `Program.cs` para que el índice apunte directamente a `[[NombreDeNota]]`.

---

## Desarrollo futuro

Posibles extensiones de `GhIoIndexGenerator`:

- Detectar automáticamente qué notas existen ya en la carpeta de documentación y marcar los tipos correspondientes como “documentados”.
- Generar índices por otros ensamblados relacionados (por ejemplo, `Grasshopper.dll`).
- Añadir filtros para ignorar tipos internos o que no sean relevantes para el sistema.

Por ahora, su rol principal es mantener sincronizado el mapa textual de GH_IO con el SDK real, facilitando el trabajo de documentación y diseño paramétrico.[web:233][web:247][web:250]