# T_Grasshopper_GUI_GH_CanvasMouseEvent

﻿ GH\_CanvasMouseEvent Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH\_CanvasMouseEvent Class](../html/T_Grasshopper_GUI_GH_CanvasMouseEvent.htm "GH_CanvasMouseEvent Class")

[GH\_CanvasMouseEvent Constructor](../html/Overload_Grasshopper_GUI_GH_CanvasMouseEvent__ctor.htm "GH_CanvasMouseEvent Constructor ")

[GH\_CanvasMouseEvent Properties](../html/Properties_T_Grasshopper_GUI_GH_CanvasMouseEvent.htm "GH_CanvasMouseEvent Properties")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_CanvasMouseEvent Class |

Class used in Canvas UI events.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST16301929\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [SystemAddLanguageSpecificTextSet("LST16301929\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");EventArgs](https://docs.microsoft.com/dotnet/api/system.eventargs)  
    Grasshopper.GUIAddLanguageSpecificTextSet("LST16301929\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_CanvasMouseEvent

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_CanvasMouseEvent : EventArgs
```

```
Public Class GH_CanvasMouseEvent
	Inherits EventArgs
```

AddLanguageTabSet("ID1EBCA");

The GH\_CanvasMouseEvent type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_CanvasMouseEventAddLanguageSpecificTextSet("LST16301929\_3?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_GUI_GH_CanvasMouseEvent__ctor.htm) | Blank constructor. |
| Public method | [GH\_CanvasMouseEvent(GH\_Viewport, MouseEventArgs)](M_Grasshopper_GUI_GH_CanvasMouseEvent__ctor_1.htm) | Constructor. |
| Public method | [GH\_CanvasMouseEvent(Point, PointF, MouseButtons, Int32, Int32)](M_Grasshopper_GUI_GH_CanvasMouseEvent__ctor_2.htm) | Constructor. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Button](P_Grasshopper_GUI_GH_CanvasMouseEvent_Button.htm) | Gets which mouse button was pressed. |
| Public property | [CanvasLocation](P_Grasshopper_GUI_GH_CanvasMouseEvent_CanvasLocation.htm) | Gets the location of the cursor in canvas unit coordinates. |
| Public property | [CanvasX](P_Grasshopper_GUI_GH_CanvasMouseEvent_CanvasX.htm) | Gets the x-coordinate of the cursor location in canvas unit coordinates. |
| Public property | [CanvasY](P_Grasshopper_GUI_GH_CanvasMouseEvent_CanvasY.htm) | Gets the y-coordinate of the cursor location in canvas unit coordinates. |
| Public property | [Clicks](P_Grasshopper_GUI_GH_CanvasMouseEvent_Clicks.htm) | Gets the number of times the mouse button was pressed and released. |
| Public property | [ControlLocation](P_Grasshopper_GUI_GH_CanvasMouseEvent_ControlLocation.htm) | Gets the location of the cursor in control pixel coordinates. |
| Public property | [ControlX](P_Grasshopper_GUI_GH_CanvasMouseEvent_ControlX.htm) | Gets the x-coordinate of the cursor location in control pixel coordinates. |
| Public property | [ControlY](P_Grasshopper_GUI_GH_CanvasMouseEvent_ControlY.htm) | Gets the y-coordinate of the cursor location in control pixel coordinates. |
| Public property | [Delta](P_Grasshopper_GUI_GH_CanvasMouseEvent_Delta.htm) | Gets a signed count of the number of detents the mouse wheel has rotated. A detent is one notch of the mouse wheel. |
| Public property | [WinFormsEventArgs](P_Grasshopper_GUI_GH_CanvasMouseEvent_WinFormsEventArgs.htm) | Downcast this data into a Windows.Forms.MouseEventArgs instance. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)