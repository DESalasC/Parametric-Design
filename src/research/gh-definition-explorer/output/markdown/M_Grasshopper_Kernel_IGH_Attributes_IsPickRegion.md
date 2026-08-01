# M_Grasshopper_Kernel_IGH_Attributes_IsPickRegion

﻿ IGH\_Attributes.IsPickRegion Method (PointF)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH\_Attributes Interface](../html/T_Grasshopper_Kernel_IGH_Attributes.htm "IGH_Attributes Interface")

[IGH\_Attributes Methods](../html/Methods_T_Grasshopper_Kernel_IGH_Attributes.htm "IGH_Attributes Methods")

[IsPickRegion Method](../html/Overload_Grasshopper_Kernel_IGH_Attributes_IsPickRegion.htm "IsPickRegion Method ")

[IsPickRegion Method (PointF)](../html/M_Grasshopper_Kernel_IGH_Attributes_IsPickRegion.htm "IsPickRegion Method (PointF)")

[IsPickRegion Method (RectangleF, GH\_PickBox)](../html/M_Grasshopper_Kernel_IGH_Attributes_IsPickRegion_1.htm "IsPickRegion Method (RectangleF, GH_PickBox)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_AttributesAddLanguageSpecificTextSet("LST5AD2CB0F\_0?cpp=::|nu=.");IsPickRegion Method (PointF) |

Determines whether a point is within the pickable region for this object.
By default, any point inside the Bounds is treated as pickable.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
bool IsPickRegion(
	PointF point
)
```

```
Function IsPickRegion ( 
	point As PointF
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

point
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST5AD2CB0F\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");PointF](https://docs.microsoft.com/dotnet/api/system.drawing.pointf)  
    Point location to test.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)

![](../icons/SectionExpanded.png)See Also

#### Reference

[IGH\_Attributes Interface](T_Grasshopper_Kernel_IGH_Attributes.htm)

[IsPickRegion Overload](Overload_Grasshopper_Kernel_IGH_Attributes_IsPickRegion.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)