# T_Grasshopper_GUI_GH_TrackerFrame

﻿ GH\_TrackerFrame Structure

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH\_TrackerFrame Structure](../html/T_Grasshopper_GUI_GH_TrackerFrame.htm "GH_TrackerFrame Structure")

[GH\_TrackerFrame Constructor](../html/M_Grasshopper_GUI_GH_TrackerFrame__ctor.htm "GH_TrackerFrame Constructor ")

[GH\_TrackerFrame Fields](../html/Fields_T_Grasshopper_GUI_GH_TrackerFrame.htm "GH_TrackerFrame Fields")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_TrackerFrame Structure |

Represents a single frame in a mouse-tracker history.
A frame represents all relevant mouse and keyboard data at a given time.

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public struct GH_TrackerFrame
```

```
Public Structure GH_TrackerFrame
```

AddLanguageTabSet("ID0EBCA");

The GH\_TrackerFrame type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_TrackerFrame](M_Grasshopper_GUI_GH_TrackerFrame__ctor.htm) | Initializes a new instance of the GH\_TrackerFrame class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Fields

|  | Name | Description |
| --- | --- | --- |
| Public field | [Buttons](F_Grasshopper_GUI_GH_TrackerFrame_Buttons.htm) | The state of the mouse buttons of the frame. |
| Public field | [Keys](F_Grasshopper_GUI_GH_TrackerFrame_Keys.htm) | The state of the modifier keys (Contro, Shift and Alt) of the frame. |
| Public field | [PositionControl](F_Grasshopper_GUI_GH_TrackerFrame_PositionControl.htm) | The position (in control coordinates) of the frame. |
| Public field | [PositionScreen](F_Grasshopper_GUI_GH_TrackerFrame_PositionScreen.htm) | The position (in screen coordinates) of the frame. |
| Public field | [Tag](F_Grasshopper_GUI_GH_TrackerFrame_Tag.htm) | Optional Tag object (to be supplied by user). |
| Public field | [Time](F_Grasshopper_GUI_GH_TrackerFrame_Time.htm) | The time at which this frame was recorded. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)