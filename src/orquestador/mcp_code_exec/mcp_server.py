# -*- coding: utf-8 -*-
"""
mcp_server.py — Servidor MCP de code execution para filtrar contexto50.json
Protocolo: JSON-RPC 2.0 sobre stdio (MCP). Stdlib de Python 3.12.
================================================================================

Propósito
---------
Exponer herramientas MCP para consultar y filtrar de forma segura los archivos
contexto50.json (data/pot-cache/<CHIP>-contexto50.json) con las volumetrías de
vecinos en radio 50 m (marco canvas, MAGNA-SIRGAS origen Bogotá).

Herramientas:
  1. filtrar_edificios   -> filtra edificios por chip y filtros (altura, pisos,
                            area, z_base) con paginación.
  2. ejecutar_codigo     -> ejecuta Python de usuario en sandbox aislado
                            (subprocess, solo lectura de pot-cache, sin red,
                            timeout, builtins restringidos).

Esquema de entrada (filtrar_edificios):
  {
    "chip": "string",                      // requerido: CHIP del predio
    "filtros": {                           // opcional
      "altura_min_m": number,
      "altura_max_m": number,
      "pisos_min": int,
      "pisos_max": int,
      "area_min_m2": number,
      "area_max_m2": number,
      "z_base_min_m": number,
      "z_base_max_m": number
    },
    "limite": int,                         // opcional, default 200, max 2000
    "incluir_geometria": bool              // opcional, default true
  }

Esquema de salida:
  {
    "ok": bool,
    "chip": string,
    "metadata": {chip, esquema, radio_m, conteo, ...},
    "edificios": [ {...campos del edificio...} ],
    "total_en_archivo": int,
    "filtrados": int,
    "filtros_aplicados": {...}
  }

Sandbox (ejecutar_codigo):
  - Subprocess aislado (python -I), datos inyectados por stdin (JSON).
  - Lectura solo de data/pot-cache/ (nunca escritura fuera de temp).
  - Sin red (no se inyecta urllib/socket/requests).
  - Timeout (default 30 s, max 120 s).
  - Builtins restringidos.

Integración:
  - Transporte principal: stdio (MCP estándar).
  - Puede envolverse en HTTP/SSE para el orquestador (puerto 8900) vía subprocess.
  - fcc-server (8787) puede proxyear a este proceso stdin/stdout.

Uso:
  python src/orquestador/mcp_code_exec/mcp_server.py
================================================================================
"""
