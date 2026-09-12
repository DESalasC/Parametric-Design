# T_Grasshopper_GUI_GH_MouseTracker

﻿ GH\_MouseTracker Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH\_MouseTracker Class](../html/T_Grasshopper_GUI_GH_MouseTracker.htm "GH_MouseTracker Class")

[GH\_MouseTracker Constructor](../html/Overload_Grasshopper_GUI_GH_MouseTracker__ctor.htm "GH_MouseTracker Constructor ")

[GH\_MouseTracker Properties](../html/Properties_T_Grasshopper_GUI_GH_MouseTracker.htm "GH_MouseTracker Properties")

[GH\_MouseTracker Methods](../html/Methods_T_Grasshopper_GUI_GH_MouseTracker.htm "GH_MouseTracker Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_MouseTracker Class |

Record mouse-movements over time.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST829A55C9\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.GUIAddLanguageSpecificTextSet("LST829A55C9\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_MouseTracker

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_MouseTracker
```

```
Public Class GH_MouseTracker
```

AddLanguageTabSet("ID1EBCA");

The GH\_MouseTracker type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_MouseTrackerAddLanguageSpecificTextSet("LST829A55C9\_2?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_GUI_GH_MouseTracker__ctor.htm) | Create a new mouse tracker. |
| Public method | [GH\_MouseTracker(Point)](M_Grasshopper_GUI_GH_MouseTracker__ctor_1.htm) | Create a new mouse tracker. |
| Public method | [GH\_MouseTracker(Point, Object)](M_Grasshopper_GUI_GH_MouseTracker__ctor_2.htm) | Create a new mouse tracker. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Duration](P_Grasshopper_GUI_GH_MouseTracker_Duration.htm) | Gets the timespan that has passed between the oldest and youngest recorded frames. This is **not** the same as the time that has passed since recording began. |
| Public property | [Frame](P_Grasshopper_GUI_GH_MouseTracker_Frame.htm) | Gets the position (in control coordinates) of the frame at the given index. |
| Public property | [FrameCount](P_Grasshopper_GUI_GH_MouseTracker_FrameCount.htm) | Gets the number of recorded frames. |
| Public property | [MaximumDuration](P_Grasshopper_GUI_GH_MouseTracker_MaximumDuration.htm) | Gets or sets the maximum allowed duration of the entire record. When new frames are recorded, old frames that are more distant than MaximumDuration will be dropped. The default duration is 10 seconds. |
| Public property | [MaximumFrameCount](P_Grasshopper_GUI_GH_MouseTracker_MaximumFrameCount.htm) | Gets or sets the maximum number of frames to keep in history. If more frames are added, the oldest ones will be dropped. The default is 16,384 frames. |
| Public property | [NewestFrame](P_Grasshopper_GUI_GH_MouseTracker_NewestFrame.htm) | Gets the most recent frame in recorded history. |
| Public property | [OldestFrame](P_Grasshopper_GUI_GH_MouseTracker_OldestFrame.htm) | Gets the oldest frame in recorded history. |
| Public property | [TemporalAccuracy](P_Grasshopper_GUI_GH_MouseTracker_TemporalAccuracy.htm) | Gets or sets the maximum temporal accuracy. Frames that are closer together than the accuracy will not be recorded. The default accuracy equals 5ms. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [DeviationAddLanguageSpecificTextSet("LST829A55C9\_3?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_GUI_GH_MouseTracker_Deviation.htm) | Gets the maximum deviation of the recorded mouse path. The maximum deviation is the furthest distance the mouse has been from the first point in the history record. |
| Public method | [Deviation(DateTime, DateTime)](M_Grasshopper_GUI_GH_MouseTracker_Deviation_1.htm) | Gets the maximum deviation of the recorded mouse path. The maximum deviation is the furthest distance the mouse has been from the first point in the history span. It does **not** measure the largest deviation between any two points in the time span, only the first and any subsequent point. |
| Public method | [DropFrames(DateTime)](M_Grasshopper_GUI_GH_MouseTracker_DropFrames.htm) | Drop all frames older than a given limit. |
| Public method | [DropFrames(Double)](M_Grasshopper_GUI_GH_MouseTracker_DropFrames_1.htm) | Find the youngest frame that deviates too much from the current locus and drop it and everything preceding it. |
| Public method | [DropFrames(Double, Point)](M_Grasshopper_GUI_GH_MouseTracker_DropFrames_2.htm) | Find the youngest frame that deviates too much from the given locus and drop it and everything preceding it. |
| Public method | [LastFrameWithinDeviation](M_Grasshopper_GUI_GH_MouseTracker_LastFrameWithinDeviation.htm) | Starting from the youngest frame, finds the oldest frame that is still within a maximum deviation of the youngest frame. |
| Public method | [Record(Point)](M_Grasshopper_GUI_GH_MouseTracker_Record.htm) | Record a new mouse event frame. If this frame is closer than [Accuracy]ms to the previously recorded frame, it is not included. |
| Public method | [Record(Point, Object)](M_Grasshopper_GUI_GH_MouseTracker_Record_1.htm) | Record a new mouse event frame. If this frame is closer than [Accuracy]ms to the previously recorded frame, it is not included. |
| Public method | [ToString](M_Grasshopper_GUI_GH_MouseTracker_ToString.htm) | (Overrides [ObjectAddLanguageSpecificTextSet("LST829A55C9\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");ToStringAddLanguageSpecificTextSet("LST829A55C9\_5?cs=()|vb=|cpp=()|nu=()|fs=()");](https://docs.microsoft.com/dotnet/api/system.object.tostring#system-object-tostring).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)