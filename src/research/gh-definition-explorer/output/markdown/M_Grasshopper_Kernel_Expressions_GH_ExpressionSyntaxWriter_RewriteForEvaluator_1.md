# M_Grasshopper_Kernel_Expressions_GH_ExpressionSyntaxWriter_RewriteForEvaluator_1

﻿ GH\_ExpressionSyntaxWriter.RewriteForEvaluator Method (String)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Expressions](../html/N_Grasshopper_Kernel_Expressions.htm "Grasshopper.Kernel.Expressions")

[GH\_ExpressionSyntaxWriter Class](../html/T_Grasshopper_Kernel_Expressions_GH_ExpressionSyntaxWriter.htm "GH_ExpressionSyntaxWriter Class")

[GH\_ExpressionSyntaxWriter Methods](../html/Methods_T_Grasshopper_Kernel_Expressions_GH_ExpressionSyntaxWriter.htm "GH_ExpressionSyntaxWriter Methods")

[RewriteForEvaluator Method](../html/Overload_Grasshopper_Kernel_Expressions_GH_ExpressionSyntaxWriter_RewriteForEvaluator.htm "RewriteForEvaluator Method ")

[RewriteForEvaluator Method (GH\_CodeString)](../html/M_Grasshopper_Kernel_Expressions_GH_ExpressionSyntaxWriter_RewriteForEvaluator.htm "RewriteForEvaluator Method (GH_CodeString)")

[RewriteForEvaluator Method (String)](../html/M_Grasshopper_Kernel_Expressions_GH_ExpressionSyntaxWriter_RewriteForEvaluator_1.htm "RewriteForEvaluator Method (String)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ExpressionSyntaxWriterAddLanguageSpecificTextSet("LST883501B5\_0?cpp=::|nu=.");RewriteForEvaluator Method (String) |

Rewrite the expression so that all temporary keywords and symbols are replaced by evaluator-specific chars.
The expression will become less readable, do not let the user see the result of this function.
You need to rewrite the expression with this function if you intend to feed it into the Evaluator.

**Namespace:**
 [Grasshopper.Kernel.Expressions](N_Grasshopper_Kernel_Expressions.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static string RewriteForEvaluator(
	string Expression
)
```

```
Public Shared Function RewriteForEvaluator ( 
	Expression As String
) As String
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

Expression
:   Type: [SystemAddLanguageSpecificTextSet("LST883501B5\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)

#### Return Value

Type: [String](https://docs.microsoft.com/dotnet/api/system.string)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_ExpressionSyntaxWriter Class](T_Grasshopper_Kernel_Expressions_GH_ExpressionSyntaxWriter.htm)

[RewriteForEvaluator Overload](Overload_Grasshopper_Kernel_Expressions_GH_ExpressionSyntaxWriter_RewriteForEvaluator.htm)

[Grasshopper.Kernel.Expressions Namespace](N_Grasshopper_Kernel_Expressions.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)