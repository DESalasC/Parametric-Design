Fase 3: Motor Normativo y Prisma Edificable

Objetivo: Aplicar automáticamente la normativa POT (Retiros, Alturas, IC, IO) sobre la geometría del lote para generar el volumen máximo edificable.
Problema Resuelto

    Lectura de Normativa: Se intentó leer el JSON general del Decreto 555, pero descubrimos que los valores exactos de Altura y UPZ están en la geodatabase espacial del POT. El script ahora lee la altura real (11.4m) directamente del contexto.json.
    Cálculo de IO e IC: Se corrigió la matemática para calcular el Índice de Ocupación (Área huella / Área lote) y el Índice de Construcción (Área total construida / Área lote) como factores decimales.
    Error de GUID en GH: Si la entrada lote_curve recibe un GUID, AreaMassProperties.Compute falla. Se debe configurar el Type Hint de la entrada a Curve.

Scripts Producidos

    src/fase-1-contexto/F1_NORMATIVA_APLICAR_v04.py: Genera el prisma edificable.

Lógica del Script

    Lee altura_maxima_m del JSON del lote.
    Aplica Curve.Offset hacia adentro con los retiros (frontal, lateral, posterior).
    Valida que el offset no haya expandido la curva.
    Extruye la huella resultante usando Extrusion.Create con la altura real.
    Calcula y devuelve IO, IC y el mensaje de log.

Siguiente Paso (Pendiente)

Implementar la lógica espacial para lotes de esquina: detectar vértices donde dos vías se cruzan y restar un cubo de 3x3m (patio de aislamiento) del prisma edificable, además de diferenciar retiros laterales si colindan con zona verde.
