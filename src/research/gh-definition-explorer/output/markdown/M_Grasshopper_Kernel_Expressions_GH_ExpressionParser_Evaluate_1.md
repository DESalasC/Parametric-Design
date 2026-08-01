# M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Evaluate_1

﻿ GH\_ExpressionParser.Evaluate Method (Queue(GH\_ParserSymbol))

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Expressions](../html/N_Grasshopper_Kernel_Expressions.htm "Grasshopper.Kernel.Expressions")

[GH\_ExpressionParser Class](../html/T_Grasshopper_Kernel_Expressions_GH_ExpressionParser.htm "GH_ExpressionParser Class")

[GH\_ExpressionParser Methods](../html/Methods_T_Grasshopper_Kernel_Expressions_GH_ExpressionParser.htm "GH_ExpressionParser Methods")

[Evaluate Method](../html/Overload_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Evaluate.htm "Evaluate Method ")

[Evaluate Method](../html/M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Evaluate.htm "Evaluate Method ")

[Evaluate Method (Queue(GH\_ParserSymbol))](../html/M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Evaluate_1.htm "Evaluate Method (Queue(GH_ParserSymbol))")

[Evaluate Method (String)](../html/M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Evaluate_2.htm "Evaluate Method (String)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ExpressionParserAddLanguageSpecificTextSet("LST177A9781\_0?cpp=::|nu=.");Evaluate Method (QueueAddLanguageSpecificTextSet("LST177A9781\_1?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");GH\_ParserSymbolAddLanguageSpecificTextSet("LST177A9781\_2?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");) |

Evaluate the expression queue without overriding any local caches.
You can obtain an expression queue by calling CachedSymbols()

**Namespace:**
 [Grasshopper.Kernel.Expressions](N_Grasshopper_Kernel_Expressions.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public GH_Variant Evaluate(
	Queue<GH_ParserSymbol> qHint
)
```

```
Public Function Evaluate ( 
	qHint As Queue(Of GH_ParserSymbol)
) As GH_Variant
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

qHint
:   Type: [System.Collections.GenericAddLanguageSpecificTextSet("LST177A9781\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Queue](https://docs.microsoft.com/dotnet/api/system.collections.generic.queue-1)AddLanguageSpecificTextSet("LST177A9781\_4?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");[GH\_ParserSymbol](T_Grasshopper_Kernel_Expressions_GH_ParserSymbol.htm)AddLanguageSpecificTextSet("LST177A9781\_5?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");

#### Return Value

Type: [GH\_Variant](T_Grasshopper_Kernel_Expressions_GH_Variant.htm)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_ExpressionParser Class](T_Grasshopper_Kernel_Expressions_GH_ExpressionParser.htm)

[Evaluate Overload](Overload_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Evaluate.htm)

[Grasshopper.Kernel.Expressions Namespace](N_Grasshopper_Kernel_Expressions.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)