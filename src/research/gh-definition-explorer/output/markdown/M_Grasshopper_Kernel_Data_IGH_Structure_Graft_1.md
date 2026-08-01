# M_Grasshopper_Kernel_Data_IGH_Structure_Graft_1

﻿ IGH\_Structure.Graft Method (GH\_GraftMode, GH\_Path)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Data](../html/N_Grasshopper_Kernel_Data.htm "Grasshopper.Kernel.Data")

[IGH\_Structure Interface](../html/T_Grasshopper_Kernel_Data_IGH_Structure.htm "IGH_Structure Interface")

[IGH\_Structure Methods](../html/Methods_T_Grasshopper_Kernel_Data_IGH_Structure.htm "IGH_Structure Methods")

[Graft Method](../html/Overload_Grasshopper_Kernel_Data_IGH_Structure_Graft.htm "Graft Method ")

[Graft Method (GH\_GraftMode)](../html/M_Grasshopper_Kernel_Data_IGH_Structure_Graft.htm "Graft Method (GH_GraftMode)")

[Graft Method (GH\_GraftMode, GH\_Path)](../html/M_Grasshopper_Kernel_Data_IGH_Structure_Graft_1.htm "Graft Method (GH_GraftMode, GH_Path)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_StructureAddLanguageSpecificTextSet("LST812B2BD4\_0?cpp=::|nu=.");Graft Method (GH\_GraftMode, GH\_Path) |

Grafts a specific path by reallocating all data into child paths.
If a grafted path coincides with an existing path,
the data item in question will be appended to the existing path.

**Namespace:**
 [Grasshopper.Kernel.Data](N_Grasshopper_Kernel_Data.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
void Graft(
	GH_GraftMode mode,
	GH_Path path
)
```

```
Sub Graft ( 
	mode As GH_GraftMode,
	path As GH_Path
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

mode
:   Type: [Grasshopper.Kernel.DataAddLanguageSpecificTextSet("LST812B2BD4\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_GraftMode](T_Grasshopper_Kernel_Data_GH_GraftMode.htm)  
    Graft mode.

path
:   Type: [Grasshopper.Kernel.DataAddLanguageSpecificTextSet("LST812B2BD4\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Path](T_Grasshopper_Kernel_Data_GH_Path.htm)  
    Path to graft

![](../icons/SectionExpanded.png)See Also

#### Reference

[IGH\_Structure Interface](T_Grasshopper_Kernel_Data_IGH_Structure.htm)

[Graft Overload](Overload_Grasshopper_Kernel_Data_IGH_Structure_Graft.htm)

[Grasshopper.Kernel.Data Namespace](N_Grasshopper_Kernel_Data.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)