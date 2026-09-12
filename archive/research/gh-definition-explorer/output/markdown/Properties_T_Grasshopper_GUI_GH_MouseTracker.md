# Properties_T_Grasshopper_GUI_GH_MouseTracker

﻿ GH\_MouseTracker Properties

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH\_MouseTracker Class](../html/T_Grasshopper_GUI_GH_MouseTracker.htm "GH_MouseTracker Class")

[GH\_MouseTracker Properties](../html/Properties_T_Grasshopper_GUI_GH_MouseTracker.htm "GH_MouseTracker Properties")

[Duration Property](../html/P_Grasshopper_GUI_GH_MouseTracker_Duration.htm "Duration Property ")

[Frame Property](../html/P_Grasshopper_GUI_GH_MouseTracker_Frame.htm "Frame Property ")

[FrameCount Property](../html/P_Grasshopper_GUI_GH_MouseTracker_FrameCount.htm "FrameCount Property ")

[MaximumDuration Property](../html/P_Grasshopper_GUI_GH_MouseTracker_MaximumDuration.htm "MaximumDuration Property ")

[MaximumFrameCount Property](../html/P_Grasshopper_GUI_GH_MouseTracker_MaximumFrameCount.htm "MaximumFrameCount Property ")

[NewestFrame Property](../html/P_Grasshopper_GUI_GH_MouseTracker_NewestFrame.htm "NewestFrame Property ")

[OldestFrame Property](../html/P_Grasshopper_GUI_GH_MouseTracker_OldestFrame.htm "OldestFrame Property ")

[TemporalAccuracy Property](../html/P_Grasshopper_GUI_GH_MouseTracker_TemporalAccuracy.htm "TemporalAccuracy Property ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_MouseTracker Properties |

The [GH\_MouseTracker](T_Grasshopper_GUI_GH_MouseTracker.htm) type exposes the following members.

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

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_MouseTracker Class](T_Grasshopper_GUI_GH_MouseTracker.htm)

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)