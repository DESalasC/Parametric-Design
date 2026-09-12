# Methods_T_Grasshopper_GUI_GH_MouseTracker

﻿ GH\_MouseTracker Methods

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH\_MouseTracker Class](../html/T_Grasshopper_GUI_GH_MouseTracker.htm "GH_MouseTracker Class")

[GH\_MouseTracker Methods](../html/Methods_T_Grasshopper_GUI_GH_MouseTracker.htm "GH_MouseTracker Methods")

[Deviation Method](../html/Overload_Grasshopper_GUI_GH_MouseTracker_Deviation.htm "Deviation Method ")

[DropFrames Method](../html/Overload_Grasshopper_GUI_GH_MouseTracker_DropFrames.htm "DropFrames Method ")

[LastFrameWithinDeviation Method](../html/M_Grasshopper_GUI_GH_MouseTracker_LastFrameWithinDeviation.htm "LastFrameWithinDeviation Method ")

[Record Method](../html/Overload_Grasshopper_GUI_GH_MouseTracker_Record.htm "Record Method ")

[ToString Method](../html/M_Grasshopper_GUI_GH_MouseTracker_ToString.htm "ToString Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_MouseTracker Methods |

The [GH\_MouseTracker](T_Grasshopper_GUI_GH_MouseTracker.htm) type exposes the following members.

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [DeviationAddLanguageSpecificTextSet("LST4A59075D\_0?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_GUI_GH_MouseTracker_Deviation.htm) | Gets the maximum deviation of the recorded mouse path. The maximum deviation is the furthest distance the mouse has been from the first point in the history record. |
| Public method | [Deviation(DateTime, DateTime)](M_Grasshopper_GUI_GH_MouseTracker_Deviation_1.htm) | Gets the maximum deviation of the recorded mouse path. The maximum deviation is the furthest distance the mouse has been from the first point in the history span. It does **not** measure the largest deviation between any two points in the time span, only the first and any subsequent point. |
| Public method | [DropFrames(DateTime)](M_Grasshopper_GUI_GH_MouseTracker_DropFrames.htm) | Drop all frames older than a given limit. |
| Public method | [DropFrames(Double)](M_Grasshopper_GUI_GH_MouseTracker_DropFrames_1.htm) | Find the youngest frame that deviates too much from the current locus and drop it and everything preceding it. |
| Public method | [DropFrames(Double, Point)](M_Grasshopper_GUI_GH_MouseTracker_DropFrames_2.htm) | Find the youngest frame that deviates too much from the given locus and drop it and everything preceding it. |
| Public method | [LastFrameWithinDeviation](M_Grasshopper_GUI_GH_MouseTracker_LastFrameWithinDeviation.htm) | Starting from the youngest frame, finds the oldest frame that is still within a maximum deviation of the youngest frame. |
| Public method | [Record(Point)](M_Grasshopper_GUI_GH_MouseTracker_Record.htm) | Record a new mouse event frame. If this frame is closer than [Accuracy]ms to the previously recorded frame, it is not included. |
| Public method | [Record(Point, Object)](M_Grasshopper_GUI_GH_MouseTracker_Record_1.htm) | Record a new mouse event frame. If this frame is closer than [Accuracy]ms to the previously recorded frame, it is not included. |
| Public method | [ToString](M_Grasshopper_GUI_GH_MouseTracker_ToString.htm) | (Overrides [ObjectAddLanguageSpecificTextSet("LST4A59075D\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");ToStringAddLanguageSpecificTextSet("LST4A59075D\_2?cs=()|vb=|cpp=()|nu=()|fs=()");](https://docs.microsoft.com/dotnet/api/system.object.tostring#system-object-tostring).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_MouseTracker Class](T_Grasshopper_GUI_GH_MouseTracker.htm)

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)