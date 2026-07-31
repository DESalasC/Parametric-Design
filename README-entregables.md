# Entregables — DiseñoParametrico Setup v2

**Fecha:** 2026-08-01
**Para:** Dario Salas
**Hardware target:** i5-12600K, 64 GB RAM, RTX 4070 Ti 12 GB, Win 11 Pro 25H2

---

## Archivos generados

| # | Archivo | Tamaño aprox | Qué hacer con él |
|---|---------|--------------|------------------|
| 1 | `analisis-reformulacion-v2.md` | 15 KB | Guardar en `D:\WORK\NOTES\obsidian-vault\10-arquitectura\` como nota de entrada |
| 2 | `init-project.ps1` | 19 KB | Copiar a `D:\WORK\scripts\` y ejecutar una sola vez |
| 3 | `setup-env.ps1` | 8 KB | Copiar a `D:\WORK\scripts\` y ejecutar una sola vez |
| 4 | `setup-obsidian.ps1` | 13 KB | Copiar a `D:\WORK\scripts\` y ejecutar una sola vez |
| 5 | `gpkg-to-cache.py` | 15 KB | Copiar a `D:\WORK\PROJECTS\DiseñoParametrico\scripts\utilities\` |
| 6 | `validate-neighbors.py` | 14 KB | Copiar a `D:\WORK\PROJECTS\DiseñoParametrico\scripts\utilities\` |
| 7 | `start-compute.ps1` | 5 KB | Copiar a `D:\WORK\PROJECTS\DiseñoParametrico\scripts\rhino-compute\` |
| 8 | `stop-compute.ps1` | 2 KB | Copiar a `D:\WORK\PROJECTS\DiseñoParametrico\scripts\rhino-compute\` |
| 9 | `health-check.ps1` | 6 KB | Copiar a `D:\WORK\PROJECTS\DiseñoParametrico\scripts\rhino-compute\` |
| 10 | `CLAUDE-global.md` | 5 KB | Renombrar a `CLAUDE.md` y guardar en `D:\WORK\` |
| 11 | `CLAUDE-proyecto.md` | 8 KB | Renombrar a `CLAUDE.md` y guardar en `D:\WORK\PROJECTS\DiseñoParametrico\` (lo genera `init-project.ps1`, este es backup) |
| 12 | `CLAUDE-vault.md` | 5 KB | Lo copia automáticamente `setup-obsidian.ps1` al vault |

---

## Orden de ejecución recomendado

### Paso 1 — Preparar scripts base (5 min)

```powershell
# Crear carpeta de scripts si no existe
New-Item -ItemType Directory -Path "D:\WORK\scripts" -Force

# Copiar setup-env.ps1 e init-project.ps1 a D:\WORK\scripts\
# (manualmente desde donde los descargaste)
```

### Paso 2 — Configurar variables de entorno (2 min)

```powershell
# Abrir PowerShell 7 como Work
powershell -ExecutionPolicy Bypass -File "D:\WORK\scripts\setup-env.ps1"

# REINICIAR PowerShell después (importante para que carguen las variables)
exit
```

### Paso 3 — Crear estructura del proyecto (3 min)

```powershell
# En nueva sesión de PowerShell
powershell -ExecutionPolicy Bypass -File "D:\WORK\scripts\init-project.ps1"
```

Esto creará:
- `D:\WORK\PROJECTS\DiseñoParametrico\` con toda la estructura
- Plantillas: `.gitignore`, `CLAUDE.md`, `README.md`, `pyproject.toml`
- Config: `config/field-whitelist.json`, `.vscode/settings.json`, `.vscode/tasks.json`
- Documentación inicial: `docs/arquitectura/pipeline-general.md`, `adr-001-uso-tapir.md`
- Git inicializado con primer commit

### Paso 4 — Copiar scripts utilitarios (5 min)

```powershell
# Scripts de Rhino.Compute
Copy-Item .\start-compute.ps1 "D:\WORK\PROJECTS\DiseñoParametrico\scripts\rhino-compute\"
Copy-Item .\stop-compute.ps1 "D:\WORK\PROJECTS\DiseñoParametrico\scripts\rhino-compute\"
Copy-Item .\health-check.ps1 "D:\WORK\PROJECTS\DiseñoParametrico\scripts\rhino-compute\"

# Scripts Python de utilidades
Copy-Item .\gpkg-to-cache.py "D:\WORK\PROJECTS\DiseñoParametrico\scripts\utilities\"
Copy-Item .\validate-neighbors.py "D:\WORK\PROJECTS\DiseñoParametrico\scripts\utilities\"

# Commit de los scripts
cd D:\WORK\PROJECTS\DiseñoParametrico
git add -A
git commit -m "feat: add setup scripts (compute, gpkg, neighbors)"
```

### Paso 5 — Configurar CLAUDE.md jerárquico (2 min)

```powershell
# CLAUDE.md global en D:\WORK\
Copy-Item .\CLAUDE-global.md "D:\WORK\CLAUDE.md" -Force

# CLAUDE.md del proyecto (ya creado por init-project.ps1, sobrescribir con plantilla completa)
Copy-Item .\CLAUDE-proyecto.md "D:\WORK\PROJECTS\DiseñoParametrico\CLAUDE.md" -Force

# CLAUDE.md del vault Obsidian — lo copia automáticamente setup-obsidian.ps1
```

### Paso 6 — Instalar Obsidian y crear el vault (5 min)

```powershell
# Ejecutar el script dedicado (instala Obsidian + crea vault + Git)
powershell -ExecutionPolicy Bypass -File "D:\WORK\scripts\setup-obsidian.ps1"
```

**Después de que termine el script, abrir Obsidian manualmente:**
1. Busca "Obsidian" en el menú Inicio de Windows.
2. Al abrir, **NO** selecciones "Create new vault".
3. Selecciona **"Open folder as vault"**.
4. Navega a `D:\WORK\NOTES\obsidian-vault` y selecciona esa carpeta.
5. Click en **"Link"** o **"Open"**.

**Plugins recomendados (instalar dentro de Obsidian):**
- Settings (engranaje abajo izquierda) → Community plugins → Turn on community plugins
- Browse → buscar e instalar:
  - **Obsidian Git** (auto-commit del vault cada 30 min)
  - **Templater** (plantillas para notas nuevas)
  - **Dataview** (consultas tipo SQL sobre notas)
  - **Graph Analysis** (análisis del grafo de conocimiento)
  - **Admonition** (bloques visuales: warning, tip, info)

**Configurar Obsidian Git:**
- Settings → Obsidian Git
- Auto backup interval: `30` (minutos)
- Commit message: `vault: auto-update {{date}}`
- Pull on startup: ON

### Paso 7 — Crear entorno Python (5 min)

```powershell
cd D:\WORK\PROJECTS\DiseñoParametrico

# Crear venv
python -m venv .venv

# Activar
.\.venv\Scripts\Activate.ps1

# Instalar dependencias
pip install -e .[dev]
pip install pyogrio shapely click rich pyproj
pip install rhino3dm  # para validate-neighbors.py
```

### Paso 8 — Verificar todo (2 min)

```powershell
# Health check completo
powershell -ExecutionPolicy Bypass -File "D:\WORK\PROJECTS\DiseñoParametrico\scripts\rhino-compute\health-check.ps1"
```

Debe mostrar:
- [OK] Variables de entorno
- [OK] Rutas críticas
- [OK] Comandos disponibles
- [SKIP] o [FAIL] en servicios que aún no estén corriendo (normal en este punto)

### Paso 9 — Descargar modelos Ollama (10-30 min)

✅ **Ya completado por el usuario.** Modelos descargados:

| Modelo | Tamaño | Uso recomendado |
|--------|--------|-----------------|
| `qwen2.5-coder:14b` | 9.0 GB | **Primario** (default Claude Code) |
| `qwen2.5-coder:latest` | 4.7 GB | Alternativa más liviana para código |
| `qwen2.5:32b` | 19 GB | Razonamiento profundo (solo si compute apagado) |
| `qwen2.5:7b` | 4.7 GB | **Cuando Rhino.Compute esté activo** (libera VRAM) |
| `mistral:latest` | 4.4 GB | Fallback conversacional |
| `codellama:latest` | 3.8 GB | Alternativa para código |
| `llama3.2:3b` | 2.0 GB | **Emergencia** (VRAM casi llena) |

**Verificar:**
```powershell
ollama list
# Debe mostrar los 7 modelos arriba
```

### Paso 10 — Probar POT (5 min)

```powershell
cd D:\WORK\PROJECTS\DiseñoParametrico

# Listar capas del .gpkg
python scripts\utilities\gpkg-to-cache.py --list-layers

# Inspeccionar campos de la capa principal (reemplazar <layer> con el nombre real)
python scripts\utilities\gpkg-to-cache.py --show-fields <layer_name> --limit 1

# Generar caché para lote de ejemplo
python scripts\utilities\gpkg-to-cache.py --lot data\lotes-ejemplo\lote-chapinero.json --verbose
```

---

## Verificación final

Después de completar todos los pasos, deberías tener:

- [ ] `D:\WORK\` con estructura completa
- [ ] `D:\WORK\PROJECTS\DiseñoParametrico\` inicializado con Git
- [ ] Variables de entorno configuradas (verificar con `echo $env:OLLAMA_MODELS`)
- [ ] Modelos Ollama descargados (verificar con `ollama list`)
- [ ] Python venv activo con dependencias instaladas
- [ ] `health-check.ps1` muestra mayormente OK
- [ ] `gpkg-to-cache.py --list-layers` lee el `.gpkg` correctamente

---

## Próximos pasos (después del setup)

### Semana 2
1. Instalar Obsidian y apuntar a `D:\WORK\NOTES\obsidian-vault\`.
2. Migrar notas existentes al vault (por etapas).
3. Migrar scripts GHPython (`CONTEXTO_v09.py`, etc.) a `src\fase-1-contexto\`.
4. Copiar `.gh` y `.ghx` a `gh-definitions\`.

### Semana 3
1. Instalar Rhino 8 + Archicad + Tapir.
2. Probar conexión Tapir bidireccional.
3. Ejecutar `start-compute.ps1` y probar Hops desde Grasshopper.

### Semana 4
1. Configurar fcc-server (clonar repo + `.env`).
2. Instalar Claude Code (`npm install -g @anthropic-ai/claude-code`).
3. Verificar Claude Code lee el vault y responde correctamente.

### Semana 5+
1. Reforzar Fase 1 con tests y fixtures.
2. Empezar Fase 2: `MOTOR_DEMANDA.py`.

---

## Solución de problemas

### Error: "Ollama no responde después de setup-env.ps1"
```powershell
# Reiniciar servicio
Restart-Service Ollama

# Verificar
ollama list
```

### Error: "compute.rhino3d.exe no encontrado"
- Verificar que Rhino 8 esté instalado en `C:\Program Files\Rhino 8\`.
- Si está en otra ruta, editar `start-compute.ps1` y agregar la ruta al array `$computePaths`.

### Error: "No se puede leer el .gpkg"
- Verificar que `pyogrio` esté instalado: `pip install pyogrio`.
- Verificar ruta del `.gpkg` en `setup-env.ps1` (variable `POT_GPKG_PATH`).
- Si el `.gpkg` tiene otra capa, ejecutar `gpkg-to-cache.py --list-layers` para ver el nombre exacto.

### Error: "validate-neighbors.py falla con ImportError: rhino3dm"
```powershell
pip install rhino3dm
```

### Error: "Claude Code no se conecta a fcc-server"
- Verificar que fcc-server esté corriendo: `curl http://127.0.0.1:8787/v1/models`.
- Verificar variable: `echo $env:ANTHROPIC_BASE_URL` (debe mostrar `http://127.0.0.1:8787`).
- Si fcc-server no está instalado todavía, eso es normal — se hace en la semana 4.

---

## Notas importantes

1. **No ejecutes `init-project.ps1` dos veces**: si necesitas recrear, borra `D:\WORK\PROJECTS\DiseñoParametrico\` primero.

2. **El `.gpkg` no se mueve**: queda en `D:\Users\Dario Salas\proyectos\DesParametrico\2-Entradas\Datos_Sitio_GDB\`. El script lo referencia por variable de entorno `POT_GPKG_PATH`.

3. **Los modelos Ollama sí se mueven a D:**: con `OLLAMA_MODELS=D:\Work\AI\ollama\models`, las descargas nuevas van allí. Los modelos ya descargados pueden requerir re-descarga si estaban en `C:\Users\Work\.ollama\models\`.

4. **CLAUDE.md jerárquico**: hay 3 archivos `CLAUDE.md` (global, proyecto, vault). No mezclarlos. Claude Code usa el más cercano al directorio de trabajo.

5. **Git desde el día 1**: tanto el proyecto como el vault están en Git. Commitear al final de cada sesión.

---

## Contacto y soporte

Este documento fue generado por el asistente IA. Si encuentras errores o necesitas ajustes:
- Anotar en `D:\WORK\NOTES\obsidian-vault\50-lecciones\` como post-mortem.
- Ajustar los scripts en `D:\WORK\scripts\` y volver a ejecutar.
