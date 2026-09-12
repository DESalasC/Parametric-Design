# M_Grasshopper_Kernel_GH_Document_RelevantObjectAtPoint_1

﻿ GH\_Document.RelevantObjectAtPoint Method (PointF, GH\_RelevantObjectFilter)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_Document Class](../html/T_Grasshopper_Kernel_GH_Document.htm "GH_Document Class")

[GH\_Document Methods](../html/Methods_T_Grasshopper_Kernel_GH_Document.htm "GH_Document Methods")

[RelevantObjectAtPoint Method](../html/Overload_Grasshopper_Kernel_GH_Document_RelevantObjectAtPoint.htm "RelevantObjectAtPoint Method ")

[RelevantObjectAtPoint Method (PointF)](../html/M_Grasshopper_Kernel_GH_Document_RelevantObjectAtPoint.htm "RelevantObjectAtPoint Method (PointF)")

[RelevantObjectAtPoint Method (PointF, GH\_RelevantObjectFilter)](../html/M_Grasshopper_Kernel_GH_Document_RelevantObjectAtPoint_1.htm "RelevantObjectAtPoint Method (PointF, GH_RelevantObjectFilter)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_DocumentAddLanguageSpecificTextSet("LST27207D5B\_0?cpp=::|nu=.");RelevantObjectAtPoint Method (PointF, GH\_RelevantObjectFilter) |

Find the most relevant object at a given canvas location.
The most relevant object might be a regular Object (Component or Parameter),
it might be an attribute grip, an attribute balloon, a wire or a group.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public GH_RelevantObjectData RelevantObjectAtPoint(
	PointF pt,
	GH_RelevantObjectFilter searchFilter
)
```

```
Public Function RelevantObjectAtPoint ( 
	pt As PointF,
	searchFilter As GH_RelevantObjectFilter
) As GH_RelevantObjectData
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

pt
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST27207D5B\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");PointF](https://docs.microsoft.com/dotnet/api/system.drawing.pointf)  
    The point to test.

searchFilter
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LST27207D5B\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_RelevantObjectFilter](T_Grasshopper_Kernel_GH_RelevantObjectFilter.htm)

#### Return Value

Type: [GH\_RelevantObjectData](T_Grasshopper_Kernel_GH_RelevantObjectData.htm)  
Information about the most relevant object or Null if no
relevant object could be found at the given point.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Document Class](T_Grasshopper_Kernel_GH_Document.htm)

[RelevantObjectAtPoint Overload](Overload_Grasshopper_Kernel_GH_Document_RelevantObjectAtPoint.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)