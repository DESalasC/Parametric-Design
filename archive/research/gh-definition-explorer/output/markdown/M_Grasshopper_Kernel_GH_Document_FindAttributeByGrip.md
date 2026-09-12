# M_Grasshopper_Kernel_GH_Document_FindAttributeByGrip

﻿ GH\_Document.FindAttributeByGrip Method (PointF, Boolean, Boolean, Boolean, Int32)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_Document Class](../html/T_Grasshopper_Kernel_GH_Document.htm "GH_Document Class")

[GH\_Document Methods](../html/Methods_T_Grasshopper_Kernel_GH_Document.htm "GH_Document Methods")

[FindAttributeByGrip Method](../html/Overload_Grasshopper_Kernel_GH_Document_FindAttributeByGrip.htm "FindAttributeByGrip Method ")

[FindAttributeByGrip Method (PointF, Boolean, Int32)](../html/M_Grasshopper_Kernel_GH_Document_FindAttributeByGrip_1.htm "FindAttributeByGrip Method (PointF, Boolean, Int32)")

[FindAttributeByGrip Method (PointF, Boolean, Boolean, Boolean, Int32)](../html/M_Grasshopper_Kernel_GH_Document_FindAttributeByGrip.htm "FindAttributeByGrip Method (PointF, Boolean, Boolean, Boolean, Int32)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_DocumentAddLanguageSpecificTextSet("LSTCF19213D\_0?cpp=::|nu=.");FindAttributeByGrip Method (PointF, Boolean, Boolean, Boolean, Int32) |

Search for attributes that contain grips near the search locus

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public IGH_Attributes FindAttributeByGrip(
	PointF pt,
	bool bLimitToOutside,
	bool bIncludeInputs,
	bool bIncludeOutputs,
	int SearchRadius = 12
)
```

```
Public Function FindAttributeByGrip ( 
	pt As PointF,
	bLimitToOutside As Boolean,
	bIncludeInputs As Boolean,
	bIncludeOutputs As Boolean,
	Optional SearchRadius As Integer = 12
) As IGH_Attributes
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

pt
:   Type: [System.DrawingAddLanguageSpecificTextSet("LSTCF19213D\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");PointF](https://docs.microsoft.com/dotnet/api/system.drawing.pointf)  
    Pixel for search start

bLimitToOutside
:   Type: [SystemAddLanguageSpecificTextSet("LSTCF19213D\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
    If true, grips are ignored if the pt is on the 'inside' side.

bIncludeInputs
:   Type: [SystemAddLanguageSpecificTextSet("LSTCF19213D\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)

bIncludeOutputs
:   Type: [SystemAddLanguageSpecificTextSet("LSTCF19213D\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)

SearchRadius (Optional)
:   Type: [SystemAddLanguageSpecificTextSet("LSTCF19213D\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Radius of search

#### Return Value

Type: [IGH\_Attributes](T_Grasshopper_Kernel_IGH_Attributes.htm)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Document Class](T_Grasshopper_Kernel_GH_Document.htm)

[FindAttributeByGrip Overload](Overload_Grasshopper_Kernel_GH_Document_FindAttributeByGrip.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)