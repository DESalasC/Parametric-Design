# T_Grasshopper_Kernel_Expressions_GH_ExpressionParser

﻿ GH\_ExpressionParser Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Expressions](../html/N_Grasshopper_Kernel_Expressions.htm "Grasshopper.Kernel.Expressions")

[GH\_ExpressionParser Class](../html/T_Grasshopper_Kernel_Expressions_GH_ExpressionParser.htm "GH_ExpressionParser Class")

[GH\_ExpressionParser Constructor](../html/Overload_Grasshopper_Kernel_Expressions_GH_ExpressionParser__ctor.htm "GH_ExpressionParser Constructor ")

[GH\_ExpressionParser Properties](../html/Properties_T_Grasshopper_Kernel_Expressions_GH_ExpressionParser.htm "GH_ExpressionParser Properties")

[GH\_ExpressionParser Methods](../html/Methods_T_Grasshopper_Kernel_Expressions_GH_ExpressionParser.htm "GH_ExpressionParser Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ExpressionParser Class |

Provides a run-time evaluator for Grasshopper expressions.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST7DB513AF\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.Kernel.ExpressionsAddLanguageSpecificTextSet("LST7DB513AF\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_ExpressionParser

**Namespace:**
 [Grasshopper.Kernel.Expressions](N_Grasshopper_Kernel_Expressions.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_ExpressionParser
```

```
Public Class GH_ExpressionParser
```

AddLanguageTabSet("ID1EBCA");

The GH\_ExpressionParser type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_ExpressionParserAddLanguageSpecificTextSet("LST7DB513AF\_2?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser__ctor.htm) | Initializes a new instance of the GH\_ExpressionParser class |
| Public method | [GH\_ExpressionParser(Boolean)](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser__ctor_1.htm) | Initializes a new instance of the GH\_ExpressionParser class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [ThrowExceptions](P_Grasshopper_Kernel_Expressions_GH_ExpressionParser_ThrowExceptions.htm) |  |
| Public property | [Variables](P_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Variables.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [AddVariable(String, Complex)](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_AddVariable.htm) |  |
| Public method | [AddVariable(String, Plane)](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_AddVariable_1.htm) |  |
| Public method | [AddVariable(String, Point3d)](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_AddVariable_2.htm) |  |
| Public method | [AddVariable(String, Vector3d)](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_AddVariable_3.htm) |  |
| Public method | [AddVariable(String, Boolean)](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_AddVariable_4.htm) |  |
| Public method | [AddVariable(String, Double)](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_AddVariable_5.htm) |  |
| Public method | [AddVariable(String, Int32)](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_AddVariable_6.htm) |  |
| Public method | [AddVariable(String, String)](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_AddVariable_7.htm) |  |
| Public method | [AddVariableEx(String, GH\_Variant)](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_AddVariableEx.htm) |  |
| Public method | [AddVariableEx(String, IGH\_Goo)](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_AddVariableEx_1.htm) |  |
| Public methodStatic member | [BalancedCharTest](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_BalancedCharTest.htm) | Test a string for balanced open and close chars. You can use this function to see if brackets or parenthesis have been properly used. |
| Public method | [CachedSymbols](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_CachedSymbols.htm) | Retrieve a copy of the Queue of cached symbols. You can use the cached symbols as an uber-optimization to speed up successive calls to Evaluate() with an identical expression string |
| Public method | [CacheSymbols](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_CacheSymbols.htm) | Create a Symbols array from the expression. Use this method if you intend to evaluate the same expression multiple times. At this point, the expression has to be in correct syntax format. Use the GH\_ExpressionSyntaxWriter.RewriteAll() method to make sure. |
| Public method | [ClearSymbols](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_ClearSymbols.htm) | Destroy the Symbols cache. |
| Public method | [ClearVariables](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_ClearVariables.htm) | Destroy the variable cache. |
| Public method | [DisplayFunctionList](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_DisplayFunctionList.htm) |  |
| Public method | [EvaluateAddLanguageSpecificTextSet("LST7DB513AF\_3?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Evaluate.htm) | Evaluate the expression currently loaded in the Symbols cache using the currently loaded variables. |
| Public method | [Evaluate(QueueAddLanguageSpecificTextSet("LST7DB513AF\_4?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");GH\_ParserSymbolAddLanguageSpecificTextSet("LST7DB513AF\_5?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");)](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Evaluate_1.htm) | Evaluate the expression queue without overriding any local caches. You can obtain an expression queue by calling CachedSymbols() |
| Public method | [Evaluate(String)](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Evaluate_2.htm) | Store a new expression in the Symbols cache and evaluate it using the current variables |
| Public methodStatic member | [IsValidVariableName](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_IsValidVariableName.htm) | Tests whether a string is a valid variable name for expressions. Valid names must contain at least one character, must start with an alphabetic character, and only contain alphanumeric chars and underscores. |
| Protected method | [Op\_BinaryAddition](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Op_BinaryAddition.htm) |  |
| Protected method | [Op\_BinaryAmpersand](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Op_BinaryAmpersand.htm) |  |
| Protected method | [Op\_BinaryAND](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Op_BinaryAND.htm) |  |
| Protected method | [Op\_BinaryAngle](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Op_BinaryAngle.htm) |  |
| Protected method | [Op\_BinaryCircumflex](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Op_BinaryCircumflex.htm) |  |
| Protected method | [Op\_BinaryCrossProduct](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Op_BinaryCrossProduct.htm) |  |
| Protected method | [Op\_BinaryDistance](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Op_BinaryDistance.htm) |  |
| Protected method | [Op\_BinaryDivision](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Op_BinaryDivision.htm) |  |
| Protected method | [Op\_BinaryEquality](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Op_BinaryEquality.htm) |  |
| Protected method | [Op\_BinaryIntegerDivision](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Op_BinaryIntegerDivision.htm) |  |
| Protected method | [Op\_BinaryLargerThan](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Op_BinaryLargerThan.htm) |  |
| Protected method | [Op\_BinaryLargerThanOrEqual](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Op_BinaryLargerThanOrEqual.htm) |  |
| Protected method | [Op\_BinaryModulus](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Op_BinaryModulus.htm) |  |
| Protected method | [Op\_BinaryMultiplication](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Op_BinaryMultiplication.htm) |  |
| Protected method | [Op\_BinaryNearEquality](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Op_BinaryNearEquality.htm) |  |
| Protected method | [Op\_BinaryOR](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Op_BinaryOR.htm) |  |
| Protected method | [Op\_BinaryPull](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Op_BinaryPull.htm) |  |
| Protected method | [Op\_BinaryPush](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Op_BinaryPush.htm) |  |
| Protected method | [Op\_BinarySmallerThan](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Op_BinarySmallerThan.htm) |  |
| Protected method | [Op\_BinarySmallerThanOrEqual](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Op_BinarySmallerThanOrEqual.htm) |  |
| Protected method | [Op\_BinarySubtraction](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Op_BinarySubtraction.htm) |  |
| Protected method | [Op\_BinaryXOR](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Op_BinaryXOR.htm) |  |
| Protected method | [Op\_UnaryBang](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Op_UnaryBang.htm) |  |
| Protected method | [Op\_UnaryCube](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Op_UnaryCube.htm) |  |
| Protected method | [Op\_UnaryDeg2Rad](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Op_UnaryDeg2Rad.htm) |  |
| Protected method | [Op\_UnaryImaginary](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Op_UnaryImaginary.htm) |  |
| Protected method | [Op\_UnaryMinus](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Op_UnaryMinus.htm) |  |
| Protected method | [Op\_UnaryNOT](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Op_UnaryNOT.htm) |  |
| Protected method | [Op\_UnaryOComponent](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Op_UnaryOComponent.htm) |  |
| Protected method | [Op\_UnaryPlus](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Op_UnaryPlus.htm) |  |
| Protected method | [Op\_UnarySquare](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Op_UnarySquare.htm) |  |
| Protected method | [Op\_UnaryXComponent](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Op_UnaryXComponent.htm) |  |
| Protected method | [Op\_UnaryYComponent](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Op_UnaryYComponent.htm) |  |
| Protected method | [Op\_UnaryZComponent](M_Grasshopper_Kernel_Expressions_GH_ExpressionParser_Op_UnaryZComponent.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Expressions Namespace](N_Grasshopper_Kernel_Expressions.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)