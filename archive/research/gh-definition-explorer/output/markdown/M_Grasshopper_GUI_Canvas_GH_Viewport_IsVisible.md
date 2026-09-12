# M_Grasshopper_GUI_Canvas_GH_Viewport_IsVisible

﻿ GH\_Viewport.IsVisible Method (PointF, Single)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI.Canvas](../html/N_Grasshopper_GUI_Canvas.htm "Grasshopper.GUI.Canvas")

[GH\_Viewport Class](../html/T_Grasshopper_GUI_Canvas_GH_Viewport.htm "GH_Viewport Class")

[GH\_Viewport Methods](../html/Methods_T_Grasshopper_GUI_Canvas_GH_Viewport.htm "GH_Viewport Methods")

[IsVisible Method](../html/Overload_Grasshopper_GUI_Canvas_GH_Viewport_IsVisible.htm "IsVisible Method ")

[IsVisible Method (PointF, Single)](../html/M_Grasshopper_GUI_Canvas_GH_Viewport_IsVisible.htm "IsVisible Method (PointF, Single)")

[IsVisible Method (RectangleF, Single)](../html/M_Grasshopper_GUI_Canvas_GH_Viewport_IsVisible_1.htm "IsVisible Method (RectangleF, Single)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ViewportAddLanguageSpecificTextSet("LST3B8BBD1F\_0?cpp=::|nu=.");IsVisible Method (PointFAddLanguageSpecificTextSet("LST3B8BBD1F\_1?cpp=%");, Single) |

Test visibility of a point.

**Namespace:**
 [Grasshopper.GUI.Canvas](N_Grasshopper_GUI_Canvas.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public bool IsVisible(
	ref PointF pt,
	float margin = 0f
)
```

```
Public Function IsVisible ( 
	ByRef pt As PointF,
	Optional margin As Single = 0F
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

pt
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST3B8BBD1F\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");PointF](https://docs.microsoft.com/dotnet/api/system.drawing.pointf)AddLanguageSpecificTextSet("LST3B8BBD1F\_3?cpp=%");  
    Point in canvas coordinates.

margin (Optional)
:   Type: [SystemAddLanguageSpecificTextSet("LST3B8BBD1F\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");Single](https://docs.microsoft.com/dotnet/api/system.single)  
    Fuzzy area around point to test.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True if the point is visible in the control upon projection.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Viewport Class](T_Grasshopper_GUI_Canvas_GH_Viewport.htm)

[IsVisible Overload](Overload_Grasshopper_GUI_Canvas_GH_Viewport_IsVisible.htm)

[Grasshopper.GUI.Canvas Namespace](N_Grasshopper_GUI_Canvas.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)