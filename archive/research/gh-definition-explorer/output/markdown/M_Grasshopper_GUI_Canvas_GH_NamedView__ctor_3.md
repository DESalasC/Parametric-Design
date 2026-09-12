# M_Grasshopper_GUI_Canvas_GH_NamedView__ctor_3

﻿ GH\_NamedView Constructor (Rectangle, RectangleF)

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
| GH\_NamedView Constructor (Rectangle, RectangleF) |

Create a new view useful for box-fit transitions.

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
	Rectangle view_box,
	RectangleF target_box
)
```

```
Public Sub New ( 
	view_box As Rectangle,
	target_box As RectangleF
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

view\_box
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST357AAEF6\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Rectangle](https://docs.microsoft.com/dotnet/api/system.drawing.rectangle)  
    The dimensions of the area into which we want to display something in control coordinates. For example, the Visible area in a Viewport.

target\_box
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST357AAEF6\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");RectangleF](https://docs.microsoft.com/dotnet/api/system.drawing.rectanglef)  
    The dimensions of the area we want to display in viewport coordinates. For example, the bounding box of some objects.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_NamedView Class](T_Grasshopper_GUI_Canvas_GH_NamedView.htm)

[GH\_NamedView Overload](Overload_Grasshopper_GUI_Canvas_GH_NamedView__ctor.htm)

[Grasshopper.GUI.Canvas Namespace](N_Grasshopper_GUI_Canvas.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)