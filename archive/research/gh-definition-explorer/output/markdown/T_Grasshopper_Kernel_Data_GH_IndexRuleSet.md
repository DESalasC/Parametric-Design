# T_Grasshopper_Kernel_Data_GH_IndexRuleSet

﻿ GH\_IndexRuleSet Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Data](../html/N_Grasshopper_Kernel_Data.htm "Grasshopper.Kernel.Data")

[GH\_IndexRuleSet Class](../html/T_Grasshopper_Kernel_Data_GH_IndexRuleSet.htm "GH_IndexRuleSet Class")

[GH\_IndexRuleSet Constructor](../html/M_Grasshopper_Kernel_Data_GH_IndexRuleSet__ctor.htm "GH_IndexRuleSet Constructor ")

[GH\_IndexRuleSet Properties](../html/Properties_T_Grasshopper_Kernel_Data_GH_IndexRuleSet.htm "GH_IndexRuleSet Properties")

[GH\_IndexRuleSet Methods](../html/Methods_T_Grasshopper_Kernel_Data_GH_IndexRuleSet.htm "GH_IndexRuleSet Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_IndexRuleSet Class |

A collection of index rules.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST24E48904\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.Kernel.DataAddLanguageSpecificTextSet("LST24E48904\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_IndexRuleSet

**Namespace:**
 [Grasshopper.Kernel.Data](N_Grasshopper_Kernel_Data.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_IndexRuleSet
```

```
Public Class GH_IndexRuleSet
```

AddLanguageTabSet("ID1EBCA");

The GH\_IndexRuleSet type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_IndexRuleSet](M_Grasshopper_Kernel_Data_GH_IndexRuleSet__ctor.htm) | Blank constructor. Creates an empty collection of rules. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Count](P_Grasshopper_Kernel_Data_GH_IndexRuleSet_Count.htm) | Gets the number of rules defined in this collection. |
| Public property | [Rule](P_Grasshopper_Kernel_Data_GH_IndexRuleSet_Rule.htm) | Gets the rule at the specified index. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [AddAnyDigitRule](M_Grasshopper_Kernel_Data_GH_IndexRuleSet_AddAnyDigitRule.htm) | Append a rule for any single digit. |
| Public method | [AddAnyDigitsRule](M_Grasshopper_Kernel_Data_GH_IndexRuleSet_AddAnyDigitsRule.htm) | Append a rule for any amount of digits. |
| Public method | [AddDigitPatternRule(AddLanguageSpecificTextSet("LST24E48904\_2?cpp=array&lt;");Int32AddLanguageSpecificTextSet("LST24E48904\_3?cpp=&gt;|cs=[]|vb=()|nu=[]|fs=[]");)](M_Grasshopper_Kernel_Data_GH_IndexRuleSet_AddDigitPatternRule_2.htm) | Append a rule for filtering digit patterns. |
| Public method | [AddDigitPatternRule(Int32, Int32)](M_Grasshopper_Kernel_Data_GH_IndexRuleSet_AddDigitPatternRule.htm) | Append a rule for filtering digit patterns. This pattern does not have an upper bound. |
| Public method | [AddDigitPatternRule(Int32, Int32, Int32)](M_Grasshopper_Kernel_Data_GH_IndexRuleSet_AddDigitPatternRule_1.htm) | Append a rule for filtering digit patterns. |
| Public method | [AddDigitRule](M_Grasshopper_Kernel_Data_GH_IndexRuleSet_AddDigitRule.htm) | Append a single digit rule. |
| Public method | [AddRangePatternRule](M_Grasshopper_Kernel_Data_GH_IndexRuleSet_AddRangePatternRule.htm) | Append a rule for filtering range patterns. |
| Public method | [AddRangeRule](M_Grasshopper_Kernel_Data_GH_IndexRuleSet_AddRangeRule.htm) | Append a single range rule. |
| Public method | [Evaluate](M_Grasshopper_Kernel_Data_GH_IndexRuleSet_Evaluate.htm) | Evaluate the index given the local rules. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Data Namespace](N_Grasshopper_Kernel_Data.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)