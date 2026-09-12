# M_Grasshopper_Kernel_Data_IGH_Structure_ReplacePath

﻿ IGH\_Structure.ReplacePath Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Data](../html/N_Grasshopper_Kernel_Data.htm "Grasshopper.Kernel.Data")

[IGH\_Structure Interface](../html/T_Grasshopper_Kernel_Data_IGH_Structure.htm "IGH_Structure Interface")

[IGH\_Structure Methods](../html/Methods_T_Grasshopper_Kernel_Data_IGH_Structure.htm "IGH_Structure Methods")

[AllData Method](../html/M_Grasshopper_Kernel_Data_IGH_Structure_AllData.htm "AllData Method ")

[Clear Method](../html/M_Grasshopper_Kernel_Data_IGH_Structure_Clear.htm "Clear Method ")

[ClearData Method](../html/M_Grasshopper_Kernel_Data_IGH_Structure_ClearData.htm "ClearData Method ")

[DataDescription Method](../html/M_Grasshopper_Kernel_Data_IGH_Structure_DataDescription.htm "DataDescription Method ")

[EnsureCapacity Method](../html/M_Grasshopper_Kernel_Data_IGH_Structure_EnsureCapacity.htm "EnsureCapacity Method ")

[ExpandPath Method](../html/M_Grasshopper_Kernel_Data_IGH_Structure_ExpandPath.htm "ExpandPath Method ")

[Flatten Method](../html/M_Grasshopper_Kernel_Data_IGH_Structure_Flatten.htm "Flatten Method ")

[Graft Method](../html/Overload_Grasshopper_Kernel_Data_IGH_Structure_Graft.htm "Graft Method ")

[LongestPathIndex Method](../html/M_Grasshopper_Kernel_Data_IGH_Structure_LongestPathIndex.htm "LongestPathIndex Method ")

[PathExists Method](../html/M_Grasshopper_Kernel_Data_IGH_Structure_PathExists.htm "PathExists Method ")

[PathIndex Method](../html/M_Grasshopper_Kernel_Data_IGH_Structure_PathIndex.htm "PathIndex Method ")

[RemovePath Method](../html/M_Grasshopper_Kernel_Data_IGH_Structure_RemovePath.htm "RemovePath Method ")

[ReplacePath Method](../html/M_Grasshopper_Kernel_Data_IGH_Structure_ReplacePath.htm "ReplacePath Method ")

[ShortestPathIndex Method](../html/M_Grasshopper_Kernel_Data_IGH_Structure_ShortestPathIndex.htm "ShortestPathIndex Method ")

[Simplify Method](../html/M_Grasshopper_Kernel_Data_IGH_Structure_Simplify.htm "Simplify Method ")

[TrimExcess Method](../html/M_Grasshopper_Kernel_Data_IGH_Structure_TrimExcess.htm "TrimExcess Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_StructureAddLanguageSpecificTextSet("LST105A266C\_0?cpp=::|nu=.");ReplacePath Method |

Replace an existing path with a different one.
If the operation is successfull, then the 'find' path
will be deleted. If the 'replace' path is already defined,
the items in 'find' will be appended to the existing path.

**Namespace:**
 [Grasshopper.Kernel.Data](N_Grasshopper_Kernel_Data.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
void ReplacePath(
	GH_Path find,
	GH_Path replace
)
```

```
Sub ReplacePath ( 
	find As GH_Path,
	replace As GH_Path
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

find
:   Type: [Grasshopper.Kernel.DataAddLanguageSpecificTextSet("LST105A266C\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Path](T_Grasshopper_Kernel_Data_GH_Path.htm)  
    The path to search for.

replace
:   Type: [Grasshopper.Kernel.DataAddLanguageSpecificTextSet("LST105A266C\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Path](T_Grasshopper_Kernel_Data_GH_Path.htm)  
    The new path.

![](../icons/SectionExpanded.png)See Also

#### Reference

[IGH\_Structure Interface](T_Grasshopper_Kernel_Data_IGH_Structure.htm)

[Grasshopper.Kernel.Data Namespace](N_Grasshopper_Kernel_Data.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)