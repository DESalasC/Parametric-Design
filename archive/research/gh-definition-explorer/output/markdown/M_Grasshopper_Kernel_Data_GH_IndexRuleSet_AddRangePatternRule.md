# M_Grasshopper_Kernel_Data_GH_IndexRuleSet_AddRangePatternRule

﻿ GH\_IndexRuleSet.AddRangePatternRule Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Data](../html/N_Grasshopper_Kernel_Data.htm "Grasshopper.Kernel.Data")

[GH\_IndexRuleSet Class](../html/T_Grasshopper_Kernel_Data_GH_IndexRuleSet.htm "GH_IndexRuleSet Class")

[GH\_IndexRuleSet Methods](../html/Methods_T_Grasshopper_Kernel_Data_GH_IndexRuleSet.htm "GH_IndexRuleSet Methods")

[AddAnyDigitRule Method](../html/M_Grasshopper_Kernel_Data_GH_IndexRuleSet_AddAnyDigitRule.htm "AddAnyDigitRule Method ")

[AddAnyDigitsRule Method](../html/M_Grasshopper_Kernel_Data_GH_IndexRuleSet_AddAnyDigitsRule.htm "AddAnyDigitsRule Method ")

[AddDigitPatternRule Method](../html/Overload_Grasshopper_Kernel_Data_GH_IndexRuleSet_AddDigitPatternRule.htm "AddDigitPatternRule Method ")

[AddDigitRule Method](../html/M_Grasshopper_Kernel_Data_GH_IndexRuleSet_AddDigitRule.htm "AddDigitRule Method ")

[AddRangePatternRule Method](../html/M_Grasshopper_Kernel_Data_GH_IndexRuleSet_AddRangePatternRule.htm "AddRangePatternRule Method ")

[AddRangeRule Method](../html/M_Grasshopper_Kernel_Data_GH_IndexRuleSet_AddRangeRule.htm "AddRangeRule Method ")

[Evaluate Method](../html/M_Grasshopper_Kernel_Data_GH_IndexRuleSet_Evaluate.htm "Evaluate Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_IndexRuleSetAddLanguageSpecificTextSet("LSTDCF227ED\_0?cpp=::|nu=.");AddRangePatternRule Method |

Append a rule for filtering range patterns.

**Namespace:**
 [Grasshopper.Kernel.Data](N_Grasshopper_Kernel_Data.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public void AddRangePatternRule(
	GH_IndexRange[] pattern
)
```

```
Public Sub AddRangePatternRule ( 
	pattern As GH_IndexRange()
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

pattern
:   Type: AddLanguageSpecificTextSet("LSTDCF227ED\_1?cpp=array&lt;");[Grasshopper.Kernel.DataAddLanguageSpecificTextSet("LSTDCF227ED\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_IndexRange](T_Grasshopper_Kernel_Data_GH_IndexRange.htm)AddLanguageSpecificTextSet("LSTDCF227ED\_3?cpp=&gt;|vb=()|nu=[]");  
    Complete pattern. A complete pattern consists of at least three ranges,
    the first one signifying the pattern lower bound, the last one signifying the patters upper bound
    (use GH\_IndexRange.MaxValue is you do not want to enforce an upper bound), and at least one range in between
    defining the pattern growth.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_IndexRuleSet Class](T_Grasshopper_Kernel_Data_GH_IndexRuleSet.htm)

[Grasshopper.Kernel.Data Namespace](N_Grasshopper_Kernel_Data.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)