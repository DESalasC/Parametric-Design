# M_Grasshopper_GUI_Canvas_GH_Canvas_ShowComponentSearchBox_1

﻿ GH\_Canvas.ShowComponentSearchBox Method (Point)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI.Canvas](../html/N_Grasshopper_GUI_Canvas.htm "Grasshopper.GUI.Canvas")

[GH\_Canvas Class](../html/T_Grasshopper_GUI_Canvas_GH_Canvas.htm "GH_Canvas Class")

[GH\_Canvas Methods](../html/Methods_T_Grasshopper_GUI_Canvas_GH_Canvas.htm "GH_Canvas Methods")

[ShowComponentSearchBox Method](../html/Overload_Grasshopper_GUI_Canvas_GH_Canvas_ShowComponentSearchBox.htm "ShowComponentSearchBox Method ")

[ShowComponentSearchBox Method](../html/M_Grasshopper_GUI_Canvas_GH_Canvas_ShowComponentSearchBox.htm "ShowComponentSearchBox Method ")

[ShowComponentSearchBox Method (Point)](../html/M_Grasshopper_GUI_Canvas_GH_Canvas_ShowComponentSearchBox_1.htm "ShowComponentSearchBox Method (Point)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_CanvasAddLanguageSpecificTextSet("LSTC8027AFF\_0?cpp=::|nu=.");ShowComponentSearchBox Method (Point) |

Display the component Search dialog at the given coordinate.
The dialog cannot be shown if ModifiersEnabled=False.

**Namespace:**
 [Grasshopper.GUI.Canvas](N_Grasshopper_GUI_Canvas.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public bool ShowComponentSearchBox(
	Point at
)
```

```
Public Function ShowComponentSearchBox ( 
	at As Point
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

at
:   Type: [System.DrawingAddLanguageSpecificTextSet("LSTC8027AFF\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Point](https://docs.microsoft.com/dotnet/api/system.drawing.point)  
    Location (in screen space) for the center of the search box.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True on success, false on failure.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Canvas Class](T_Grasshopper_GUI_Canvas_GH_Canvas.htm)

[ShowComponentSearchBox Overload](Overload_Grasshopper_GUI_Canvas_GH_Canvas_ShowComponentSearchBox.htm)

[Grasshopper.GUI.Canvas Namespace](N_Grasshopper_GUI_Canvas.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)