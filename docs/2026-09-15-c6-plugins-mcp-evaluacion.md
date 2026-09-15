---
fecha: 2026-09-15
tipo: evaluación
alcance: C6 — plugins/MCP/skills a instalar
estado: propuesta
tags: [infra, plugins, mcp, hostinger, c6, openclaw, claude-code]
---

# C6 — Evaluación de plugins/MCP/skills a instalar (lección Hostinger)

## Contexto

En el incidente previo se habilitó el plugin **`hostinger@claude-plugins-official`**
y quedó desactivado (`false`) junto con otros de cero uso. La lección: **no
habilitar plugins/MCP con dependencias externas o de pago sin verificar su
utilidad real y su huella (procesos, red, cuentas)**. Objetivo de C6: definir
**qué conviene instalar** y **con qué criterio**, para no repetir el caso
Hostinger.

## Estado actual observado (2026-09-15)

**Claude Code (`D:\Users\Work\.claude\settings.json`)**
- `model`: `sonnet[1m]` · `language`: Español · `permissions.defaultMode`: auto.
- Habilitados: `superpowers`, `playwright`, `mattpocock-skills`,
  `huggingface-skills`, `nowledge-mem`.
- Deshabilitados: `code-review`, `skill-creator`, `code-simplifier`, `github`,
  `claude-md-management`, `nvidia-skills`, **`hostinger`**.

**MCP de OpenClaw/AutoClaw (`workspace/config/mcporter.json`)**
- `autoclaw-productivity` (streamablehttp 19681/mcp) — núcleo, mantener.
- `autoclaw-github` (19681/github/mcp) — mantener.

**MCP sueltos (`D:\Work\.claude\mcp.json`)**
- `playwright`, `sentry`, `context7`. ⚠️ **el archivo tiene una API key de
  Context7 en claro** (`CONTEXT7_API_KEY`): mover a variable de entorno y rotar.

## Criterios de admisión (aplicar antes de instalar cualquiera)

1. **Utilidad demostrada**: resolver un caso real del proyecto (no “por tenerlo”).
2. **Huella local**: preferir local/offline; evitar servicios que exijan cuenta,
   suscripción o proxy externo (causa raíz del caso Hostinger).
3. **Reversibilidad**: instalable y desinstalable con un toggle; sin escritura en
   rutas fuera del proyecto/perfil.
4. **Datos**: sin secretos en claro; credenciales por variable de entorno.
5. **Licencia/red**: revisar qué endpoint externo consume y con qué frecuencia.
6. **Un servicio por necesidad**: no duplicar (p. ej. dos navegadores MCP).

## Recomendación por candidato

| Candidato | Veredicto | Motivo |
|---|---|---|
| `autoclaw-productivity` / `autoclaw-github` | **Mantener** | Núcleo local (127.0.0.1:19681), uso diario. |
| `playwright` (browser MCP) | **Mantener, con reserva** | Útil, pero el flujo web preferente es `autoglm-browser-agent`; evitar duplicar navegadores. |
| `context7` | **Condicional** | Útil para docs de librerías; **rotar la API key y moverla a env**. |
| `sentry` | **Evaluar** | Solo si se instrumenta un servicio propio; hoy sin caso real. |
| `nowledge-mem` | **Mantener** | Ya integrado (ADR-014). |
| `huggingface-skills` / `nvidia-skills` | **Deshabilitar por defecto** | Sin uso verificado; NVIDIA requiere cuenta/endpoint externo. |
| `hostinger` | **NO habilitar** | Proveedor externo de pago; causa del incidente. |
| `superpowers`, `mattpocock-skills` | **Mantener** | Locales, uso confirmado en el flujo Claude Code. |
| `code-review`, `skill-creator`, `code-simplifier`, `github`, `claude-md-management` | **Off / on-demand** | Activar solo cuando se use el flujo correspondiente; `github` reactivar si se hace flujo de PRs desde CLI. |
| Agentes permanentes (filesystem MCP, `data-loader`, `neighbors-validator`, `design-guardian`, `doc-sync`) | **Diferido** | Nada permanente hasta cerrar C4/C5; evaluar con los mismos 6 criterios. |

## Regla durable propuesta

> Antes de habilitar un plugin/MCP: **justificar con un caso real**, verificar
> que **no dependa de un servicio externo de pago** y que sea **reversible por
> toggle**. Sin eso, queda **off por defecto**.

## Pendientes C6

1. Rotar y parametrizar la API key de Context7 (`D:\Work\.claude\mcp.json`).
2. Decidir `sentry` y `playwright` (¿uno solo de navegador?).
3. Re-evaluar agentes permanentes tras cerrar C4/C5.
