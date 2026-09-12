# M_Grasshopper_Kernel_GH_GHXHarvester_HarvestBoundingBoxes_2

﻿ GH\_GHXHarvester.HarvestBoundingBoxes Method (String)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_GHXHarvester Class](../html/T_Grasshopper_Kernel_GH_GHXHarvester.htm "GH_GHXHarvester Class")

[GH\_GHXHarvester Methods](../html/Methods_T_Grasshopper_Kernel_GH_GHXHarvester.htm "GH_GHXHarvester Methods")

[HarvestBoundingBoxes Method](../html/Overload_Grasshopper_Kernel_GH_GHXHarvester_HarvestBoundingBoxes.htm "HarvestBoundingBoxes Method ")

[HarvestBoundingBoxes Method (GH\_Archive)](../html/M_Grasshopper_Kernel_GH_GHXHarvester_HarvestBoundingBoxes.htm "HarvestBoundingBoxes Method (GH_Archive)")

[HarvestBoundingBoxes Method (GH\_IReader)](../html/M_Grasshopper_Kernel_GH_GHXHarvester_HarvestBoundingBoxes_1.htm "HarvestBoundingBoxes Method (GH_IReader)")

[HarvestBoundingBoxes Method (String)](../html/M_Grasshopper_Kernel_GH_GHXHarvester_HarvestBoundingBoxes_2.htm "HarvestBoundingBoxes Method (String)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_GHXHarvesterAddLanguageSpecificTextSet("LST1B77CE91\_0?cpp=::|nu=.");HarvestBoundingBoxes Method (String) |

Harvest all attribute bounding boxes from a GHX/GH archive.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static List<RectangleF> HarvestBoundingBoxes(
	string file
)
```

```
Public Shared Function HarvestBoundingBoxes ( 
	file As String
) As List(Of RectangleF)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

file
:   Type: [SystemAddLanguageSpecificTextSet("LST1B77CE91\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    File to parse.

#### Return Value

Type: [List](https://docs.microsoft.com/dotnet/api/system.collections.generic.list-1)AddLanguageSpecificTextSet("LST1B77CE91\_2?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");[RectangleF](https://docs.microsoft.com/dotnet/api/system.drawing.rectanglef)AddLanguageSpecificTextSet("LST1B77CE91\_3?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
A list of all attribute bounding boxes or null on failure.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_GHXHarvester Class](T_Grasshopper_Kernel_GH_GHXHarvester.htm)

[HarvestBoundingBoxes Overload](Overload_Grasshopper_Kernel_GH_GHXHarvester_HarvestBoundingBoxes.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)