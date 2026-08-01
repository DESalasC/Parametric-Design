# M_Grasshopper_GUI_Canvas_GH_NamedView__ctor_4

﻿ GH\_NamedView Constructor (String, PointF, Single, GH\_NamedViewType)

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
| GH\_NamedView Constructor (String, PointF, Single, GH\_NamedViewType) |

Create a new named view.

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
	string view_name,
	PointF view_point,
	float view_zoom = 1f,
	GH_NamedViewType view_type = GH_NamedViewType.target
)
```

```
Public Sub New ( 
	view_name As String,
	view_point As PointF,
	Optional view_zoom As Single = 1F,
	Optional view_type As GH_NamedViewType = GH_NamedViewType.target
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

view\_name
:   Type: [SystemAddLanguageSpecificTextSet("LST97A16760\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of view.

view\_point
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST97A16760\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");PointF](https://docs.microsoft.com/dotnet/api/system.drawing.pointf)  
    Anchor point of named view.

view\_zoom (Optional)
:   Type: [SystemAddLanguageSpecificTextSet("LST97A16760\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Single](https://docs.microsoft.com/dotnet/api/system.single)  
    Zoom factor of named view.

view\_type (Optional)
:   Type: [Grasshopper.GUI.CanvasAddLanguageSpecificTextSet("LST97A16760\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_NamedViewType](T_Grasshopper_GUI_Canvas_GH_NamedViewType.htm)  
    The type of named view.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_NamedView Class](T_Grasshopper_GUI_Canvas_GH_NamedView.htm)

[GH\_NamedView Overload](Overload_Grasshopper_GUI_Canvas_GH_NamedView__ctor.htm)

[Grasshopper.GUI.Canvas Namespace](N_Grasshopper_GUI_Canvas.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)