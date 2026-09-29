# DiseñoParametrico — Environment Setup Guide

## Quick Start (5 minutes)

### 1. Activate Python Environment
```powershell
cd D:\WORK\PROJECTS\DiseñoParametrico
.\.venv\Scripts\Activate.ps1
```

If `.venv` doesn't exist, create it first (siempre con Python 3.12 — los wheels del stack son `cp312`):
```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2. Install Dependencies
```powershell
pip install -e .[dev]
pip install pyogrio shapely click rich pyproj rhino3dm
```

### 3. Verify Installation
```powershell
pytest src/fase-1-contexto/tests/ -v
python scripts/utilities/gpkg-to-cache.py --list-layers
```

---

## Complete Setup (Detailed)

### Prerequisites
- **Python 3.12** (external, not IronPython)
- **Windows 11** (Pro or Enterprise)
- **Git** (for version control)
- **Rhino 8** + **Grasshopper** + **ArchiCAD** (for BIM operations)
- **Ollama** (for local IA models)

### Step 1: Repository Clone/Sync
```powershell
# If you have not cloned the repo yet
git clone <repo-url> D:\WORK\PROJECTS\DiseñoParametrico
cd D:\WORK\PROJECTS\DiseñoParametrico

# Keep up to date
git pull origin main
```

### Step 2: Python Virtual Environment

#### Create venv (first time only)
```powershell
cd D:\WORK\PROJECTS\DiseñoParametrico
py -3.12 -m venv .venv   # SIEMPRE 3.12 (nunca 3.11/3.13): los wheels del stack son cp312
```

> Si el venv quedó creado/apuntado con otra versión (síntomas: `No module named
> numpy._core...` o `No module named shapely.lib`), re-apuntar **sin reinstalar**:
> `py -3.12 -m venv --upgrade .venv` (ver lecciones 2026-09-27 / 2026-09-28).

#### Activate venv
```powershell
# PowerShell
.\.venv\Scripts\Activate.ps1

# If execution policy blocks it, run:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser -Force
.\.venv\Scripts\Activate.ps1
```

#### Verify Python 3.12
```powershell
python --version  # Should show Python 3.12.x
```

### Step 3: Install Project Dependencies

```powershell
# Install project + dev dependencies
pip install -e .[dev]

# Install spatial dependencies (required for POT/GIS workflows)
pip install pyogrio shapely click rich pyproj rtree

# Install BIM/3D tools
pip install rhino3dm ifcopenshell

# For PDF processing (optional, used in some utilities)
pip install pdf2image pymupdf pytesseract
```

### Step 4: Set Environment Variables

Create/update environment variables for the session:

#### Option A: PowerShell Profile (Permanent)
Add to your PowerShell profile (`$PROFILE`):
```powershell
$env:DISENO_PARAMETRICO_ROOT = "D:\WORK\PROJECTS\DiseñoParametrico"
$env:POT_GPKG_PATH = "D:\Users\Dario Salas\proyectos\DesParametrico\2-Entradas\Datos_Sitio_GDB\bd_uaecd.gpkg"
$env:OLLAMA_MODELS = "D:\Users\Work\.ollama\models\"
```

#### Option B: Session-Only (Temporary)
```powershell
$env:DISENO_PARAMETRICO_ROOT = "D:\WORK\PROJECTS\DiseñoParametrico"
$env:POT_GPKG_PATH = "D:\Users\Dario Salas\proyectos\DesParametrico\2-Entradas\Datos_Sitio_GDB\bd_uaecd.gpkg"
$env:OLLAMA_MODELS = "D:\Users\Work\.ollama\models\"
```

### Step 5: Verify Core Functionality

#### Test Python Scripts
```powershell
# List POT layers
python scripts/utilities/gpkg-to-cache.py --list-layers

# Show POT fields (limit 1)
python scripts/utilities/gpkg-to-cache.py --show-fields Area_elevacion_maxima --limit 1
```

#### Run Tests
```powershell
# Run all tests
pytest tests/ -v

# Run only Fase 1 tests
pytest src/fase-1-contexto/tests/ -v

# Run with coverage
pytest tests/ --cov=src --cov-report=term-missing
```

#### Verify Linting
```powershell
# Check code quality
ruff check src/ --extend-select=I,N,B,UP

# Type checking
mypy src/
```

### Step 6: Configure Rhino/Grasshopper Services

#### Start Rhino.Compute (Headless)
```powershell
# Start Rhino Compute on port 6001
powershell $env:DISENO_PARAMETRICO_ROOT\scripts\rhino-compute\start-compute.ps1

# Health check
powershell $env:DISENO_PARAMETRICO_ROOT\scripts\rhino-compute\health-check.ps1

# Stop when done
powershell $env:DISENO_PARAMETRICO_ROOT\scripts\rhino-compute\stop-compute.ps1
```

#### Configure Local Ollama Models
```powershell
# Check installed models
ollama list

# Pull primary model if missing
ollama pull qwen2.5-coder:14b

# Pull lightweight fallback
ollama pull qwen2.5:7b
ollama pull llama3.2:3b
```

---

## VS Code Configuration

### 1. Open Workspace
```powershell
code D:\WORK\PROJECTS\DiseñoParametrico\workspace.code-workspace
```

### 2. Install Extensions (Recommended)
- **Python** (ms-python.python)
- **Pylance** (ms-python.vscode-pylance)
- **Ruff** (charliermarsh.ruff)
- **Grasshopper** (mcneel.grasshopper)
- **Thunder Client** (rangav.vscode-thunder-client) — for testing APIs

### 3. Python Interpreter
VS Code should auto-detect `.venv`. To manually set:
1. `Ctrl+Shift+P` → "Python: Select Interpreter"
2. Choose `.\.venv\Scripts\python.exe`

---

## Project Structure Overview

```
DiseñoParametrico/
├── .venv/                    # Python virtual environment (do NOT commit)
├── .vscode/                  # VS Code workspace settings
├── config/                   # Configuration files (field-whitelist.json)
├── data/                     # Data sources
│   ├── pot-cache/            # Cached POT JSON by CHIP
│   ├── fase-2-demanda/       # GFA input for phase 2
│   ├── lotes-ejemplo/        # Example lots
│   └── ...
├── gh-definitions/           # Grasshopper definitions (.ghx)
│   └── F1_Contexto_Base-Editado_v02  # Master workflow
├── scripts/                  # Standalone Python scripts
│   ├── rhino-compute/        # Rhino Compute management
│   └── utilities/            # gpkg-to-cache, validate-neighbors, etc.
├── src/                      # Main source code by phase
│   ├── fase-1-contexto/      # Context + normative (POT, retiros, patios)
│   ├── fase-2-demanda/       # Demand + financial models
│   ├── fase-3-masa/          # Mass generation
│   ├── fase-4-ambiental/     # Environmental analysis (Ladybug)
│   └── fase-5-bim/           # BIM injection (ArchiCAD API)
├── tests/                    # Test fixtures and test_*.py
├── logs/                     # Execution logs
├── CLAUDE.md                 # Rules and conventions (READ FIRST)
├── README.md                 # Project overview
├── pyproject.toml            # Project metadata + dependencies
├── requirements.txt          # Pinned versions (pip freeze output)
└── workspace.code-workspace  # VS Code workspace config
```

---

## Common Workflows

### Workflow 1: Add a New Lot to Cache
```powershell
# 1. Ensure GeoJSON with lot boundaries exists
$geojson = "D:\path\to\lot-chapinero.json"

# 2. Run fetch script (creates data/pot-cache/<CHIP>-contexto.json)
python scripts/utilities/gpkg-to-cache.py --lot $geojson

# 3. Use in Grasshopper via F1_ETAPA1_CONTEXTO component
```

### Workflow 2: Validate Neighbor Morphs
```powershell
# 1. Export neighbors from Rhino as 3DM
# 2. Validate with script
python scripts/utilities/validate-neighbors.py --input data\neighbors\vecinos.3dm

# 3. Check logs for warnings (missing AlturaTotal, invalid geometry, etc.)
```

### Workflow 3: Run Fase 1 → Fase 2 Pipeline
```powershell
# 1. Ensure GHX is open in Grasshopper with F1 definition
# 2. Phase 1 exports to: data/fase-2-demanda/<CHIP>-gfa-gh.json
# 3. Run Phase 2 motor
python src/fase-2-demanda/F2_DEMANDA_MOTOR_v03.py --chip <CHIP>
# or with custom GFA
python src/fase-2-demanda/F2_DEMANDA_MOTOR_v03.py --chip <CHIP> --gfa data/fase-2-demanda/<CHIP>-gfa-gh.json
```

### Workflow 4: Code Quality Checks
```powershell
# Linting
ruff check src/ --extend-select=I,N,B,UP

# Type checking
mypy src/

# Format (auto-fix)
ruff format src/

# Full CI simulation
pytest tests/ --cov=src && ruff check src/ && mypy src/
```

---

## Troubleshooting

### Issue: `ModuleNotFoundError: No module named 'fiona'`
**Solution:**
```powershell
pip install fiona pyogrio geopandas
```

### Issue: `.venv\Scripts\Activate.ps1` cannot be loaded
**Solution:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser -Force
.\.venv\Scripts\Activate.ps1
```

### Issue: Rhino.Compute not responding (port 6001)
**Solution:**
```powershell
# Stop any existing process
Stop-Process -Name compute.geometry.exe -Force

# Start fresh
powershell scripts\rhino-compute\start-compute.ps1

# Check health
powershell scripts\rhino-compute\health-check.ps1
```

### Issue: Ollama VRAM exhaustion
**Solution:**
```powershell
# Switch to lightweight model
ollama pull qwen2.5:7b
# Update Ollama model selection in your scripts
```

### Issue: GHPython component says "Can not determine language"
**Solution:**
- **DO NOT use the "Python 3 Script" component** (Rhino 8 bug, seals component)
- Use the classic **"Script"** component + select **IronPython 2.7**
- Ensure no shebang (`#! /usr/bin/env python3`) at script start

---

## Key Configuration Files

### [CLAUDE.md](./CLAUDE.md)
**READ FIRST.** Contains:
- Naming conventions
- GHPython rules (IronPython 2.7 only)
- Pipeline phases and versions
- Normative references (Decreto 555/2021, NSR-10)

### [pyproject.toml](./pyproject.toml)
- Project metadata + dependencies (Python 3.12+)
- Optional dependencies: `[dev]`, `[bim]`
- Pytest, ruff, mypy configuration

### [.editorconfig](./.editorconfig)
- IDE-agnostic formatting rules (line length, indentation)
- Apply in VS Code via "EditorConfig for VS Code" extension

### [workspace.code-workspace](./workspace.code-workspace)
- VS Code workspace settings
- Extensions recommendations
- Python interpreter path

---

## Next Steps

1. ✅ **Activate venv** → `.\.venv\Scripts\Activate.ps1`
2. ✅ **Install dependencies** → `pip install -e .[dev]`
3. ✅ **Read CLAUDE.md** → Understand the rules
4. ✅ **Run tests** → `pytest tests/ -v`
5. 🚀 **Start working** → Choose a phase and begin

For questions, refer to [CLAUDE.md](./CLAUDE.md) or the vault at `D:\WORK\NOTES\obsidian-vault\`.

---

**Last Updated:** 2026-09-01  
**Python:** 3.12  
**Status:** Ready for development
