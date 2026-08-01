# T_Grasshopper_Kernel_Expressions_GH_ExpressionSyntaxWriter

﻿ GH\_ExpressionSyntaxWriter Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Expressions](../html/N_Grasshopper_Kernel_Expressions.htm "Grasshopper.Kernel.Expressions")

[GH\_ExpressionSyntaxWriter Class](../html/T_Grasshopper_Kernel_Expressions_GH_ExpressionSyntaxWriter.htm "GH_ExpressionSyntaxWriter Class")

[GH\_ExpressionSyntaxWriter Methods](../html/Methods_T_Grasshopper_Kernel_Expressions_GH_ExpressionSyntaxWriter.htm "GH_ExpressionSyntaxWriter Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ExpressionSyntaxWriter Class |

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LSTCDC56AC9\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.Kernel.ExpressionsAddLanguageSpecificTextSet("LSTCDC56AC9\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_ExpressionSyntaxWriter

**Namespace:**
 [Grasshopper.Kernel.Expressions](N_Grasshopper_Kernel_Expressions.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public sealed class GH_ExpressionSyntaxWriter
```

```
Public NotInheritable Class GH_ExpressionSyntaxWriter
```

AddLanguageTabSet("ID1EBCA");

The GH\_ExpressionSyntaxWriter type exposes the following members.

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public methodStatic member | [RewriteAll](M_Grasshopper_Kernel_Expressions_GH_ExpressionSyntaxWriter_RewriteAll.htm) | Apply all syntax rulesets to the expression. |
| Public methodStatic member | [RewriteForEvaluator(GH\_CodeString)](M_Grasshopper_Kernel_Expressions_GH_ExpressionSyntaxWriter_RewriteForEvaluator.htm) | Rewrite the expression so that all temporary keywords and symbols are replaced by evaluator-specific chars. The expression will become less readable, do not let the user see the result of this function. You need to rewrite the expression with this function if you intend to feed it into the Evaluator. |
| Public methodStatic member | [RewriteForEvaluator(String)](M_Grasshopper_Kernel_Expressions_GH_ExpressionSyntaxWriter_RewriteForEvaluator_1.htm) | Rewrite the expression so that all temporary keywords and symbols are replaced by evaluator-specific chars. The expression will become less readable, do not let the user see the result of this function. You need to rewrite the expression with this function if you intend to feed it into the Evaluator. |
| Public methodStatic member | [RewriteForGraphicInterface(GH\_CodeString)](M_Grasshopper_Kernel_Expressions_GH_ExpressionSyntaxWriter_RewriteForGraphicInterface.htm) | Rewrite the expression so that tags are replaced by the complex characters that make up the esoteric operators, functions and constants. The expression should become more readable for humans. |
| Public methodStatic member | [RewriteForGraphicInterface(String)](M_Grasshopper_Kernel_Expressions_GH_ExpressionSyntaxWriter_RewriteForGraphicInterface_1.htm) | Rewrite the expression so that tags are replaced by the complex characters that make up the esoteric operators, functions and constants. The expression should become more readable |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Expressions Namespace](N_Grasshopper_Kernel_Expressions.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)