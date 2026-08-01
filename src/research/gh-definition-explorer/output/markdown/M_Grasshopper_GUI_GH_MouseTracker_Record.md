# M_Grasshopper_GUI_GH_MouseTracker_Record

﻿ GH\_MouseTracker.Record Method (Point)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH\_MouseTracker Class](../html/T_Grasshopper_GUI_GH_MouseTracker.htm "GH_MouseTracker Class")

[GH\_MouseTracker Methods](../html/Methods_T_Grasshopper_GUI_GH_MouseTracker.htm "GH_MouseTracker Methods")

[Record Method](../html/Overload_Grasshopper_GUI_GH_MouseTracker_Record.htm "Record Method ")

[Record Method (Point)](../html/M_Grasshopper_GUI_GH_MouseTracker_Record.htm "Record Method (Point)")

[Record Method (Point, Object)](../html/M_Grasshopper_GUI_GH_MouseTracker_Record_1.htm "Record Method (Point, Object)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_MouseTrackerAddLanguageSpecificTextSet("LST6358E74A\_0?cpp=::|nu=.");Record Method (Point) |

Record a new mouse event frame. If this frame is closer than [Accuracy]ms to the previously recorded frame, it is not included.

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public void Record(
	Point position
)
```

```
Public Sub Record ( 
	position As Point
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

position
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST6358E74A\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Point](https://docs.microsoft.com/dotnet/api/system.drawing.point)  
    Location of new frame.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_MouseTracker Class](T_Grasshopper_GUI_GH_MouseTracker.htm)

[Record Overload](Overload_Grasshopper_GUI_GH_MouseTracker_Record.htm)

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)