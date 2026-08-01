# M_Grasshopper_Kernel_Data_GH_TreeRules__ctor

﻿ GH\_TreeRules Constructor 

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
| GH\_TreeRules Constructor |

Constructs a new rule set for testing data trees.
Unless you know exactly what you are doing, use the FromString() static method instead.

**Namespace:**
 [Grasshopper.Kernel.Data](N_Grasshopper_Kernel_Data.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public GH_TreeRules(
	IEnumerable<IGH_Rule> pathRules,
	IGH_Rule indexRule
)
```

```
Public Sub New ( 
	pathRules As IEnumerable(Of IGH_Rule),
	indexRule As IGH_Rule
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

pathRules
:   Type: [System.Collections.GenericAddLanguageSpecificTextSet("LSTF3011AAC\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");IEnumerable](https://docs.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)AddLanguageSpecificTextSet("LSTF3011AAC\_1?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");[IGH\_Rule](T_Grasshopper_Kernel_Data_IGH_Rule.htm)AddLanguageSpecificTextSet("LSTF3011AAC\_2?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
    A collection of path rules.

indexRule
:   Type: [Grasshopper.Kernel.DataAddLanguageSpecificTextSet("LSTF3011AAC\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");IGH\_Rule](T_Grasshopper_Kernel_Data_IGH_Rule.htm)  
    Optional index rule (may be null).

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_TreeRules Class](T_Grasshopper_Kernel_Data_GH_TreeRules.htm)

[Grasshopper.Kernel.Data Namespace](N_Grasshopper_Kernel_Data.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)