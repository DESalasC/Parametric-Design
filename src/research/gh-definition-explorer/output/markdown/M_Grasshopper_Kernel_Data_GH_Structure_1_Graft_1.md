# M_Grasshopper_Kernel_Data_GH_Structure_1_Graft_1

﻿ GH\_Structure(T).Graft Method (GH\_GraftMode, GH\_Path)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Data](../html/N_Grasshopper_Kernel_Data.htm "Grasshopper.Kernel.Data")

[GH\_Structure(T) Class](../html/T_Grasshopper_Kernel_Data_GH_Structure_1.htm "GH_Structure(T) Class")

[GH\_Structure(T) Methods](../html/Methods_T_Grasshopper_Kernel_Data_GH_Structure_1.htm "GH_Structure(T) Methods")

[Graft Method](../html/Overload_Grasshopper_Kernel_Data_GH_Structure_1_Graft.htm "Graft Method ")

[Graft Method (GH\_GraftMode)](../html/M_Grasshopper_Kernel_Data_GH_Structure_1_Graft.htm "Graft Method (GH_GraftMode)")

[Graft Method (GH\_GraftMode, GH\_Path)](../html/M_Grasshopper_Kernel_Data_GH_Structure_1_Graft_1.htm "Graft Method (GH_GraftMode, GH_Path)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_StructureAddLanguageSpecificTextSet("LSTBF0D6273\_0?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTBF0D6273\_1?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");AddLanguageSpecificTextSet("LSTBF0D6273\_2?cpp=::|nu=.");Graft Method (GH\_GraftMode, GH\_Path) |

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
public void Graft(
	GH_GraftMode mode,
	GH_Path path
)
```

```
Public Sub Graft ( 
	mode As GH_GraftMode,
	path As GH_Path
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

mode
:   Type: [Grasshopper.Kernel.DataAddLanguageSpecificTextSet("LSTBF0D6273\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_GraftMode](T_Grasshopper_Kernel_Data_GH_GraftMode.htm)  
    Graft mode.

path
:   Type: [Grasshopper.Kernel.DataAddLanguageSpecificTextSet("LSTBF0D6273\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Path](T_Grasshopper_Kernel_Data_GH_Path.htm)  
    Path to graft

#### Implements

[IGH\_StructureAddLanguageSpecificTextSet("LSTBF0D6273\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");Graft(GH\_GraftMode, GH\_Path)](M_Grasshopper_Kernel_Data_IGH_Structure_Graft_1.htm)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_StructureAddLanguageSpecificTextSet("LSTBF0D6273\_6?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTBF0D6273\_7?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;"); Class](T_Grasshopper_Kernel_Data_GH_Structure_1.htm)

[Graft Overload](Overload_Grasshopper_Kernel_Data_GH_Structure_1_Graft.htm)

[Grasshopper.Kernel.Data Namespace](N_Grasshopper_Kernel_Data.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)