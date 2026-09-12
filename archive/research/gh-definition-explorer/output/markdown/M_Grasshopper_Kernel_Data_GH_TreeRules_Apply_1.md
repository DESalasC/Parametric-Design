# M_Grasshopper_Kernel_Data_GH_TreeRules_Apply_1

﻿ GH\_TreeRules.Apply Method (GH\_Path, Int32)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Data](../html/N_Grasshopper_Kernel_Data.htm "Grasshopper.Kernel.Data")

[GH\_TreeRules Class](../html/T_Grasshopper_Kernel_Data_GH_TreeRules.htm "GH_TreeRules Class")

[GH\_TreeRules Methods](../html/Methods_T_Grasshopper_Kernel_Data_GH_TreeRules.htm "GH_TreeRules Methods")

[Apply Method](../html/Overload_Grasshopper_Kernel_Data_GH_TreeRules_Apply.htm "Apply Method ")

[Apply Method (GH\_Path)](../html/M_Grasshopper_Kernel_Data_GH_TreeRules_Apply.htm "Apply Method (GH_Path)")

[Apply Method (GH\_Path, Int32)](../html/M_Grasshopper_Kernel_Data_GH_TreeRules_Apply_1.htm "Apply Method (GH_Path, Int32)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_TreeRulesAddLanguageSpecificTextSet("LST80CB4DC0\_0?cpp=::|nu=.");Apply Method (GH\_Path, Int32) |

Apply all the local rules to a path+index combination.

**Namespace:**
 [Grasshopper.Kernel.Data](N_Grasshopper_Kernel_Data.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public bool Apply(
	GH_Path path,
	int index
)
```

```
Public Function Apply ( 
	path As GH_Path,
	index As Integer
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

path
:   Type: [Grasshopper.Kernel.DataAddLanguageSpecificTextSet("LST80CB4DC0\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Path](T_Grasshopper_Kernel_Data_GH_Path.htm)  
    Path to test.

index
:   Type: [SystemAddLanguageSpecificTextSet("LST80CB4DC0\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Index to test.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True if path+index pass all the rule tests.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_TreeRules Class](T_Grasshopper_Kernel_Data_GH_TreeRules.htm)

[Apply Overload](Overload_Grasshopper_Kernel_Data_GH_TreeRules_Apply.htm)

[Grasshopper.Kernel.Data Namespace](N_Grasshopper_Kernel_Data.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)