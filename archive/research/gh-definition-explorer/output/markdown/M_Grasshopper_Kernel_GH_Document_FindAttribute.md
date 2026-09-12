# M_Grasshopper_Kernel_GH_Document_FindAttribute

﻿ GH\_Document.FindAttribute Method (PointF, Boolean)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_Document Class](../html/T_Grasshopper_Kernel_GH_Document.htm "GH_Document Class")

[GH\_Document Methods](../html/Methods_T_Grasshopper_Kernel_GH_Document.htm "GH_Document Methods")

[FindAttribute Method](../html/Overload_Grasshopper_Kernel_GH_Document_FindAttribute.htm "FindAttribute Method ")

[FindAttribute Method (Guid)](../html/M_Grasshopper_Kernel_GH_Document_FindAttribute_1.htm "FindAttribute Method (Guid)")

[FindAttribute Method (PointF, Boolean)](../html/M_Grasshopper_Kernel_GH_Document_FindAttribute.htm "FindAttribute Method (PointF, Boolean)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_DocumentAddLanguageSpecificTextSet("LSTD8F39D02\_0?cpp=::|nu=.");FindAttribute Method (PointF, Boolean) |

Search for attributes that contain a certain point.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public IGH_Attributes FindAttribute(
	PointF pt,
	bool topLevelOnly
)
```

```
Public Function FindAttribute ( 
	pt As PointF,
	topLevelOnly As Boolean
) As IGH_Attributes
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

pt
:   Type: [System.DrawingAddLanguageSpecificTextSet("LSTD8F39D02\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");PointF](https://docs.microsoft.com/dotnet/api/system.drawing.pointf)  
    The point in Canvas coordinates

topLevelOnly
:   Type: [SystemAddLanguageSpecificTextSet("LSTD8F39D02\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
    If true, child attributes will be skipped.

#### Return Value

Type: [IGH\_Attributes](T_Grasshopper_Kernel_IGH_Attributes.htm)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Document Class](T_Grasshopper_Kernel_GH_Document.htm)

[FindAttribute Overload](Overload_Grasshopper_Kernel_GH_Document_FindAttribute.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)