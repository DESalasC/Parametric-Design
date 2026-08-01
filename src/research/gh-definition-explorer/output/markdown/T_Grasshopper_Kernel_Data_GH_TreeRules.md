# T_Grasshopper_Kernel_Data_GH_TreeRules

﻿ GH\_TreeRules Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Data](../html/N_Grasshopper_Kernel_Data.htm "Grasshopper.Kernel.Data")

[GH\_TreeRules Class](../html/T_Grasshopper_Kernel_Data_GH_TreeRules.htm "GH_TreeRules Class")

[GH\_TreeRules Constructor](../html/M_Grasshopper_Kernel_Data_GH_TreeRules__ctor.htm "GH_TreeRules Constructor ")

[GH\_TreeRules Properties](../html/Properties_T_Grasshopper_Kernel_Data_GH_TreeRules.htm "GH_TreeRules Properties")

[GH\_TreeRules Methods](../html/Methods_T_Grasshopper_Kernel_Data_GH_TreeRules.htm "GH_TreeRules Methods")

[GH\_TreeRules Fields](../html/Fields_T_Grasshopper_Kernel_Data_GH_TreeRules.htm "GH_TreeRules Fields")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_TreeRules Class |

Represents an entire data tree rule set.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LSTC6B75788\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.Kernel.DataAddLanguageSpecificTextSet("LSTC6B75788\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_TreeRules

**Namespace:**
 [Grasshopper.Kernel.Data](N_Grasshopper_Kernel_Data.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public sealed class GH_TreeRules
```

```
Public NotInheritable Class GH_TreeRules
```

AddLanguageTabSet("ID1EBCA");

The GH\_TreeRules type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_TreeRules](M_Grasshopper_Kernel_Data_GH_TreeRules__ctor.htm) | Constructs a new rule set for testing data trees. Unless you know exactly what you are doing, use the FromString() static method instead. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [HasItemRule](P_Grasshopper_Kernel_Data_GH_TreeRules_HasItemRule.htm) | Gets whether this rule set has a defined index rule. |
| Public property | [HasPathRules](P_Grasshopper_Kernel_Data_GH_TreeRules_HasPathRules.htm) | Gets whether this rule set has any path rules. |
| Public property | [PathRuleCount](P_Grasshopper_Kernel_Data_GH_TreeRules_PathRuleCount.htm) | Gets the number of defined path rules. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [Apply(GH\_Path)](M_Grasshopper_Kernel_Data_GH_TreeRules_Apply.htm) | Apply all the local rules to a path. |
| Public method | [Apply(GH\_Path, Int32)](M_Grasshopper_Kernel_Data_GH_TreeRules_Apply_1.htm) | Apply all the local rules to a path+index combination. |
| Public methodStatic member | [FromString](M_Grasshopper_Kernel_Data_GH_TreeRules_FromString.htm) | Attempt to parse a Pattern string. |
| Public method | [ToString](M_Grasshopper_Kernel_Data_GH_TreeRules_ToString.htm) | (Overrides [ObjectAddLanguageSpecificTextSet("LSTC6B75788\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");ToStringAddLanguageSpecificTextSet("LSTC6B75788\_3?cs=()|vb=|cpp=()|nu=()|fs=()");](https://docs.microsoft.com/dotnet/api/system.object.tostring#system-object-tostring).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Fields

|  | Name | Description |
| --- | --- | --- |
| Public fieldStatic member | [AllowedChars](F_Grasshopper_Kernel_Data_GH_TreeRules_AllowedChars.htm) |  |
| Public fieldStatic member | [AndOperator](F_Grasshopper_Kernel_Data_GH_TreeRules_AndOperator.htm) |  |
| Public fieldStatic member | [AnyNumbersSymbol](F_Grasshopper_Kernel_Data_GH_TreeRules_AnyNumbersSymbol.htm) |  |
| Public fieldStatic member | [AnyNumberSymbol](F_Grasshopper_Kernel_Data_GH_TreeRules_AnyNumberSymbol.htm) |  |
| Public fieldStatic member | [ItemBrackets](F_Grasshopper_Kernel_Data_GH_TreeRules_ItemBrackets.htm) |  |
| Public fieldStatic member | [ItemCloseBracket](F_Grasshopper_Kernel_Data_GH_TreeRules_ItemCloseBracket.htm) |  |
| Public fieldStatic member | [ItemOpenBracket](F_Grasshopper_Kernel_Data_GH_TreeRules_ItemOpenBracket.htm) |  |
| Public fieldStatic member | [NotOperator](F_Grasshopper_Kernel_Data_GH_TreeRules_NotOperator.htm) |  |
| Public fieldStatic member | [OrOperator](F_Grasshopper_Kernel_Data_GH_TreeRules_OrOperator.htm) |  |
| Public fieldStatic member | [PathBrackets](F_Grasshopper_Kernel_Data_GH_TreeRules_PathBrackets.htm) |  |
| Public fieldStatic member | [PathCloseBracket](F_Grasshopper_Kernel_Data_GH_TreeRules_PathCloseBracket.htm) |  |
| Public fieldStatic member | [PathOpenBracket](F_Grasshopper_Kernel_Data_GH_TreeRules_PathOpenBracket.htm) |  |
| Public fieldStatic member | [PathSeparator](F_Grasshopper_Kernel_Data_GH_TreeRules_PathSeparator.htm) |  |
| Public fieldStatic member | [RangeSymbol](F_Grasshopper_Kernel_Data_GH_TreeRules_RangeSymbol.htm) |  |
| Public fieldStatic member | [RuleBrackets](F_Grasshopper_Kernel_Data_GH_TreeRules_RuleBrackets.htm) |  |
| Public fieldStatic member | [RuleCloseBracket](F_Grasshopper_Kernel_Data_GH_TreeRules_RuleCloseBracket.htm) |  |
| Public fieldStatic member | [RuleOpenBracket](F_Grasshopper_Kernel_Data_GH_TreeRules_RuleOpenBracket.htm) |  |
| Public fieldStatic member | [Separator](F_Grasshopper_Kernel_Data_GH_TreeRules_Separator.htm) |  |
| Public fieldStatic member | [SequenceCode](F_Grasshopper_Kernel_Data_GH_TreeRules_SequenceCode.htm) |  |
| Public fieldStatic member | [SequenceSymbol](F_Grasshopper_Kernel_Data_GH_TreeRules_SequenceSymbol.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Data Namespace](N_Grasshopper_Kernel_Data.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)