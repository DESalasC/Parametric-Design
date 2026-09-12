# M_Grasshopper_Kernel_GH_StateTag_RenderTagPolygonIcon

﻿ GH\_StateTag.RenderTagPolygonIcon Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_StateTag Class](../html/T_Grasshopper_Kernel_GH_StateTag.htm "GH_StateTag Class")

[GH\_StateTag Methods](../html/Methods_T_Grasshopper_Kernel_GH_StateTag.htm "GH_StateTag Methods")

[Render Method](../html/M_Grasshopper_Kernel_GH_StateTag_Render.htm "Render Method ")

[RenderFreeformIcon Method](../html/M_Grasshopper_Kernel_GH_StateTag_RenderFreeformIcon.htm "RenderFreeformIcon Method ")

[RenderTagBlankIcon Method](../html/Overload_Grasshopper_Kernel_GH_StateTag_RenderTagBlankIcon.htm "RenderTagBlankIcon Method ")

[RenderTagPolygonIcon Method](../html/M_Grasshopper_Kernel_GH_StateTag_RenderTagPolygonIcon.htm "RenderTagPolygonIcon Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_StateTagAddLanguageSpecificTextSet("LST404D7E1\_0?cpp=::|nu=.");RenderTagPolygonIcon Method |

Render a filled polygon with default shading.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
protected void RenderTagPolygonIcon(
	Graphics graphics,
	PointF[] polygon
)
```

```
Protected Sub RenderTagPolygonIcon ( 
	graphics As Graphics,
	polygon As PointF()
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

graphics
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST404D7E1\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Graphics](https://docs.microsoft.com/dotnet/api/system.drawing.graphics)  
    Graphics object to draw with.

polygon
:   Type: AddLanguageSpecificTextSet("LST404D7E1\_2?cpp=array&lt;");[System.DrawingAddLanguageSpecificTextSet("LST404D7E1\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");PointF](https://docs.microsoft.com/dotnet/api/system.drawing.pointf)AddLanguageSpecificTextSet("LST404D7E1\_4?cpp=&gt;|vb=()|nu=[]");  
    Polygon corners.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_StateTag Class](T_Grasshopper_Kernel_GH_StateTag.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)