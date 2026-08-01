# M_Grasshopper_GUI_Canvas_GH_NamedView__ctor_2

﻿ GH\_NamedView Constructor (GH\_Viewport, Rectangle, PointF)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI.Canvas](../html/N_Grasshopper_GUI_Canvas.htm "Grasshopper.GUI.Canvas")

[GH\_NamedView Class](../html/T_Grasshopper_GUI_Canvas_GH_NamedView.htm "GH_NamedView Class")

[GH\_NamedView Constructor](../html/Overload_Grasshopper_GUI_Canvas_GH_NamedView__ctor.htm "GH_NamedView Constructor ")

[GH\_NamedView Constructor](../html/M_Grasshopper_GUI_Canvas_GH_NamedView__ctor.htm "GH_NamedView Constructor ")

[GH\_NamedView Constructor (Rectangle, RectangleF)](../html/M_Grasshopper_GUI_Canvas_GH_NamedView__ctor_3.htm "GH_NamedView Constructor (Rectangle, RectangleF)")

[GH\_NamedView Constructor (GH\_Viewport, Point, PointF)](../html/M_Grasshopper_GUI_Canvas_GH_NamedView__ctor_1.htm "GH_NamedView Constructor (GH_Viewport, Point, PointF)")

[GH\_NamedView Constructor (GH\_Viewport, Rectangle, PointF)](../html/M_Grasshopper_GUI_Canvas_GH_NamedView__ctor_2.htm "GH_NamedView Constructor (GH_Viewport, Rectangle, PointF)")

[GH\_NamedView Constructor (String, PointF, Single, GH\_NamedViewType)](../html/M_Grasshopper_GUI_Canvas_GH_NamedView__ctor_4.htm "GH_NamedView Constructor (String, PointF, Single, GH_NamedViewType)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_NamedView Constructor (GH\_Viewport, Rectangle, PointF) |

Create a new view useful for point inclusion transitions.

**Namespace:**
 [Grasshopper.GUI.Canvas](N_Grasshopper_GUI_Canvas.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public GH_NamedView(
	GH_Viewport view,
	Rectangle region,
	PointF target
)
```

```
Public Sub New ( 
	view As GH_Viewport,
	region As Rectangle,
	target As PointF
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

view
:   Type: [Grasshopper.GUI.CanvasAddLanguageSpecificTextSet("LST9B78B731\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Viewport](T_Grasshopper_GUI_Canvas_GH_Viewport.htm)  
    Viewport this transition is supposed to work in.

region
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST9B78B731\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Rectangle](https://docs.microsoft.com/dotnet/api/system.drawing.rectangle)  
    Region into which the target is supposed to be visible in control coordinates.
    For example, the contents of the viewport.

target
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST9B78B731\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");PointF](https://docs.microsoft.com/dotnet/api/system.drawing.pointf)  
    Point to ensure.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_NamedView Class](T_Grasshopper_GUI_Canvas_GH_NamedView.htm)

[GH\_NamedView Overload](Overload_Grasshopper_GUI_Canvas_GH_NamedView__ctor.htm)

[Grasshopper.GUI.Canvas Namespace](N_Grasshopper_GUI_Canvas.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)