# ADR-004: Postergar integración de RHINO-MCP y ROBO-HOPPER

**Fecha:** 2026-08-01
**Estado:** Aceptado

## Contexto

Durante el setup del proyecto, se identificaron dos herramientas modernas que podrían mejorar la integración entre Claude Code y Grasshopper:

1. **RHINO-MCP** (easehee/rhino-mcp) - puente Rhino 8 ↔ Claude Desktop vía MCP
2. **ROBO-HOPPER** (Simone Peluffo) - agente que construye definiciones GH en vivo

Ambas herramientas prometen productividad drástica al permitir que Claude cree y modifique definiciones Grasshopper directamente en el canvas.

## Análisis

### Argumentos a favor de integrar ahora

- Productividad drástica (Claude construye GH en vivo)
- Iteración visual inmediata
- Debug en tiempo real del canvas
- Estado del arte en integración LLM-CAD
- Gratuitas (open source / freeware)

### Argumentos en contra (huecos detectados)

1. **Bloqueador técnico:** ROBO-HOPPER requiere Claude Desktop o suscripción directa a Claude/Gemini/ChatGPT. El proyecto usa Claude Code (CLI) vía FCC con GLM-5.2. No compatible directamente.

2. **Beta inestable:** ROBO-HOPPER se describe como "work-in-progress beta, it keeps progressing each day". Riesgo de rework si cambia la API.

3. **Infraestructura base incompleta:** Rhino 8, Archicad y Tapir NO están instalados todavía. Instalar MCPs sobre infraestructura no validada es construir sobre arena.

4. **Trabajo existente:** 15 scripts GHPython migrados (F1-F4, ~7,747 líneas). Pasar a ROBO-HOPPER invalidaría ese trabajo o requeriría migración compleja.

5. **Complejidad cognitiva:** Stack actual ya tiene 10+ componentes. Agregar MCPs = 12+. Dificulta debugging cuando algo falle.

6. **Resuelven problema que no existe aún:** Los MCPs aceleran iteración visual, pero el problema actual es tener pipeline funcional end-to-end. Primero que funcione, luego optimizar.

7. **MCPs no son estándar:** Son implementaciones específicas de terceros. Si se abandonan, todo lo construido sobre ellas se pierde.

## Decisión

**Postergar la integración de RHINO-MCP y ROBO-HOPPER.** No instalar ahora.

### Plan por fases

#### FASE A — Pipeline funcional SIN MCPs (ahora)
1. Instalar Rhino 8 + Archicad + Tapir
2. Validar FCC + Claude Code + GLM-5.2 end-to-end
3. Adaptar scripts F1 a JSONs estructurados
4. Crear F5_MAPEO_TAPIR_v01.py con elementos nativos
5. Probar pipeline completo con lote real

#### FASE B — Evaluación con datos (después)
1. Una vez pipeline funcione, identificar cuellos de botella
2. ¿Dónde duele? ¿Iteración visual? ¿Debug? ¿Comunicación GH-Archicad?
3. Si el dolor justifica el riesgo: evaluar MCPs
4. Si no: mantener stack actual

#### FASE C — MCPs como aditivos (futuro)
- Solo si FASE B identifica valor claro
- Instalar sobre infraestructura validada
- No romper pipeline existente
- MCPs se vuelven opcionales, no requeridos

## Consecuencias

### Positivas
- Stack más simple y predecible
- 15 scripts migrados se mantienen vigentes
- Menor superficie de ataque para debugging
- Pipeline se valida primero, optimización después
- No dependencia de betas inestables

### Negativas
- Pierde productividad potencial de iteración visual
- Claude no puede manipular canvas GH directamente (por ahora)
- Iteración requiere: escribir .py → cargar en GH → probar (más lento)

### Neutrales
- Los MCPs quedan como opción futura, no se descartan
- Si en 3-6 meses ROBO-HOPPER madura, se reevalúa
- El pipeline base no depende de MCPs

## Decisión sobre GDL

Confirmado durante el análisis: **NO usar GDL (Geometric Description Language)** para elementos BIM.

### Justificación
- GDL es lenguaje de script para objetos de librería, no elementos BIM nativos
- Limitaciones de edición: objetos GDL son "cajas negras"
- No se integran con listados BIM nativos
- Requieren programación para modificar
- Adecuado para muebles/equipos, NO para muros/losas/estructura

### Implementación
F5_MAPEO_TAPIR_v01.py debe crear SOLO elementos nativos:
- AC_Slab (placas)
- AC_Wall (muros)
- AC_Column (columnas)
- AC_Beam (vigas)
- AC_Zone (zonas)
- AC_Roof (cubiertas)
- Set_UserText (propiedades POT/NSR-10)

Prohibidos: AC_Morph, GDL objects, exports DWG/DXF sin inteligencia BIM.

## Referencias

- [[adr-001-uso-tapir]] - Decisión original de Tapir
- [[adr-003-elementos-bim-nativos-vs-morphs]] - Elementos nativos
- Pipeline general: docs/arquitectura/pipeline-general.md
