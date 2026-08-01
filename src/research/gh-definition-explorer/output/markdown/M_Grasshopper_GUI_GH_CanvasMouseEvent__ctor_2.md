# M_Grasshopper_GUI_GH_CanvasMouseEvent__ctor_2

﻿ GH\_CanvasMouseEvent Constructor (Point, PointF, MouseButtons, Int32, Int32)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH\_CanvasMouseEvent Class](../html/T_Grasshopper_GUI_GH_CanvasMouseEvent.htm "GH_CanvasMouseEvent Class")

[GH\_CanvasMouseEvent Constructor](../html/Overload_Grasshopper_GUI_GH_CanvasMouseEvent__ctor.htm "GH_CanvasMouseEvent Constructor ")

[GH\_CanvasMouseEvent Constructor](../html/M_Grasshopper_GUI_GH_CanvasMouseEvent__ctor.htm "GH_CanvasMouseEvent Constructor ")

[GH\_CanvasMouseEvent Constructor (GH\_Viewport, MouseEventArgs)](../html/M_Grasshopper_GUI_GH_CanvasMouseEvent__ctor_1.htm "GH_CanvasMouseEvent Constructor (GH_Viewport, MouseEventArgs)")

[GH\_CanvasMouseEvent Constructor (Point, PointF, MouseButtons, Int32, Int32)](../html/M_Grasshopper_GUI_GH_CanvasMouseEvent__ctor_2.htm "GH_CanvasMouseEvent Constructor (Point, PointF, MouseButtons, Int32, Int32)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_CanvasMouseEvent Constructor (Point, PointF, MouseButtons, Int32, Int32) |

Constructor.

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public GH_CanvasMouseEvent(
	Point pt_control,
	PointF pt_canvas,
	MouseButtons mButton,
	int iClicks = 0,
	int iDelta = 0
)
```

```
Public Sub New ( 
	pt_control As Point,
	pt_canvas As PointF,
	mButton As MouseButtons,
	Optional iClicks As Integer = 0,
	Optional iDelta As Integer = 0
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

pt\_control
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST770F4DEB\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Point](https://docs.microsoft.com/dotnet/api/system.drawing.point)  
    Cursor location in control pixel coordinates.

pt\_canvas
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST770F4DEB\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");PointF](https://docs.microsoft.com/dotnet/api/system.drawing.pointf)  
    Cursor location in canvas unit coordinates.

mButton
:   Type: [System.Windows.FormsAddLanguageSpecificTextSet("LST770F4DEB\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");MouseButtons](https://docs.microsoft.com/dotnet/api/system.windows.forms.mousebuttons)  
    Currently pressed mouse buttons.

iClicks (Optional)
:   Type: [SystemAddLanguageSpecificTextSet("LST770F4DEB\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Number of times the buttons were pressed and released.

iDelta (Optional)
:   Type: [SystemAddLanguageSpecificTextSet("LST770F4DEB\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    A signed count of the number of detents the mouse wheel has rotated.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_CanvasMouseEvent Class](T_Grasshopper_GUI_GH_CanvasMouseEvent.htm)

[GH\_CanvasMouseEvent Overload](Overload_Grasshopper_GUI_GH_CanvasMouseEvent__ctor.htm)

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)