# MCP Validators (CLI tools, not MCP servers)

> **Importante:** estos scripts **no son servidores MCP**. No implementan el
> protocolo stdio/JSON-RPC, así que **no deben declararse** bajo `mcpServers`
> en `.mcp.json`. Si se declaran ahí, Claude Code intenta arrancarlos como
> servidores, falla el handshake y no cargan (además ensucian los logs).

## Qué son

Herramientas de **lint/validación** de un archivo de configuración MCP
(estilo `.mcp.json`). Validan el *contenido* de la config; no exponen tools.

Comprueban, por cada entrada de servidor:

1. Campos obligatorios: `command` (string), `args` (lista de strings).
2. Resolución del comando: rutas absolutas/relativas se verifican contra el
   disco; nombres simples se resuelven en `PATH` (`shutil.which`).
3. Flags CLI peligrosos dentro de `args` (`--plugin-url`, `--load-config`,
   `--no-*-mcp-servers`, `--debug...true`).
4. Variables de `env`: sintaxis de clave válida, valor string no vacío, y
   aviso si la clave parece contener credenciales.
5. Detección de overrides de admin/política en claves de `env`.

## Uso

```bash
# Validación básica
python scripts/mcp-validator.py .mcp.json

# Generar reporte JSON
python scripts/mcp-validator.py .mcp.json -o report.json

# Modo estricto (los warnings cuentan como fallo)
python scripts/mcp-validator.py .mcp.json --strict
```

Los wrappers bash mantienen la interfaz antigua y delegan en el validador de
Python (única fuente de verdad):

```bash
./scripts/mcp-validate.sh --init .mcp.json
./scripts/mcp-validate-cli.sh --validate .mcp.json
```

Códigos de salida: `0` = sin errores, `1` = hay errores, `2` = config ilegible.

## Si algún día quieres un servidor MCP real

Los validators no deben volver a `mcpServers`. Si de verdad quieres exponer la
validación como *tool* MCP, hay que implementar un servidor que hable JSON-RPC
sobre stdio (p. ej. con el SDK `@modelcontextprotocol/sdk` o `mcp` de Python) y
declararlo aparte, con su `command`/`args` apuntando a ese servidor real.
