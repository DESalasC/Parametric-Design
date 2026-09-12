# M_Grasshopper_Kernel_Data_GH_Lexer_EvaluatePath

﻿ GH\_Lexer.EvaluatePath Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Data](../html/N_Grasshopper_Kernel_Data.htm "Grasshopper.Kernel.Data")

[GH\_Lexer Class](../html/T_Grasshopper_Kernel_Data_GH_Lexer.htm "GH_Lexer Class")

[GH\_Lexer Methods](../html/Methods_T_Grasshopper_Kernel_Data_GH_Lexer.htm "GH_Lexer Methods")

[EvaluatePath Method](../html/M_Grasshopper_Kernel_Data_GH_Lexer_EvaluatePath.htm "EvaluatePath Method ")

[PerformLexicalReplace Method](../html/Overload_Grasshopper_Kernel_Data_GH_Lexer_PerformLexicalReplace.htm "PerformLexicalReplace Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_LexerAddLanguageSpecificTextSet("LST15ED948C\_0?cpp=::|nu=.");EvaluatePath Method |

Evaluate the variables in this mask with the provided expression solver.

**Namespace:**
 [Grasshopper.Kernel.Data](N_Grasshopper_Kernel_Data.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public bool EvaluatePath(
	GH_ExpressionParser evaluator,
	ref GH_Path path,
	ref int index
)
```

```
Public Function EvaluatePath ( 
	evaluator As GH_ExpressionParser,
	ByRef path As GH_Path,
	ByRef index As Integer
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

evaluator
:   Type: [Grasshopper.Kernel.ExpressionsAddLanguageSpecificTextSet("LST15ED948C\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_ExpressionParser](T_Grasshopper_Kernel_Expressions_GH_ExpressionParser.htm)  
    Evaluator to use. Must have all variables properly set up.

path
:   Type: [Grasshopper.Kernel.DataAddLanguageSpecificTextSet("LST15ED948C\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Path](T_Grasshopper_Kernel_Data_GH_Path.htm)AddLanguageSpecificTextSet("LST15ED948C\_3?cpp=%");  
    Path result.

index
:   Type: [SystemAddLanguageSpecificTextSet("LST15ED948C\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)AddLanguageSpecificTextSet("LST15ED948C\_5?cpp=%");  
    Index result. If the lexer contains no item representation then
    the index remains unmolested.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True on success, false on failure.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Lexer Class](T_Grasshopper_Kernel_Data_GH_Lexer.htm)

[Grasshopper.Kernel.Data Namespace](N_Grasshopper_Kernel_Data.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)