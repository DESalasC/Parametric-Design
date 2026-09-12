# M_Grasshopper_Kernel_Data_GH_IndexRuleSet_AddDigitPatternRule_2

﻿ GH\_IndexRuleSet.AddDigitPatternRule Method (Int32[])

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Data](../html/N_Grasshopper_Kernel_Data.htm "Grasshopper.Kernel.Data")

[GH\_IndexRuleSet Class](../html/T_Grasshopper_Kernel_Data_GH_IndexRuleSet.htm "GH_IndexRuleSet Class")

[GH\_IndexRuleSet Methods](../html/Methods_T_Grasshopper_Kernel_Data_GH_IndexRuleSet.htm "GH_IndexRuleSet Methods")

[AddDigitPatternRule Method](../html/Overload_Grasshopper_Kernel_Data_GH_IndexRuleSet_AddDigitPatternRule.htm "AddDigitPatternRule Method ")

[AddDigitPatternRule Method (Int32[])](../html/M_Grasshopper_Kernel_Data_GH_IndexRuleSet_AddDigitPatternRule_2.htm "AddDigitPatternRule Method (Int32[])")

[AddDigitPatternRule Method (Int32, Int32)](../html/M_Grasshopper_Kernel_Data_GH_IndexRuleSet_AddDigitPatternRule.htm "AddDigitPatternRule Method (Int32, Int32)")

[AddDigitPatternRule Method (Int32, Int32, Int32)](../html/M_Grasshopper_Kernel_Data_GH_IndexRuleSet_AddDigitPatternRule_1.htm "AddDigitPatternRule Method (Int32, Int32, Int32)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_IndexRuleSetAddLanguageSpecificTextSet("LST4ABB6474\_0?cpp=::|nu=.");AddDigitPatternRule Method (AddLanguageSpecificTextSet("LST4ABB6474\_1?cpp=array&lt;");Int32AddLanguageSpecificTextSet("LST4ABB6474\_2?cpp=&gt;|vb=()|nu=[]");) |

Append a rule for filtering digit patterns.

**Namespace:**
 [Grasshopper.Kernel.Data](N_Grasshopper_Kernel_Data.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public void AddDigitPatternRule(
	int[] pattern
)
```

```
Public Sub AddDigitPatternRule ( 
	pattern As Integer()
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

pattern
:   Type: AddLanguageSpecificTextSet("LST4ABB6474\_3?cpp=array&lt;");[SystemAddLanguageSpecificTextSet("LST4ABB6474\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)AddLanguageSpecificTextSet("LST4ABB6474\_5?cpp=&gt;|vb=()|nu=[]");  
    Complete pattern. A complete pattern consists of at least three integers,
    the first one signifying the pattern lower bound, the last one signifying the patters upper bound
    (use Int32.MaxValue is you do not want to enforce an upper bound), and at least one integer in between
    defining the pattern growth.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_IndexRuleSet Class](T_Grasshopper_Kernel_Data_GH_IndexRuleSet.htm)

[AddDigitPatternRule Overload](Overload_Grasshopper_Kernel_Data_GH_IndexRuleSet_AddDigitPatternRule.htm)

[Grasshopper.Kernel.Data Namespace](N_Grasshopper_Kernel_Data.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)