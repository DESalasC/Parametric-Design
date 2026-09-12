# P_Grasshopper_GUI_GH_MouseTracker_MaximumDuration

﻿ GH\_MouseTracker.MaximumDuration Property 

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
| GH\_MouseTrackerAddLanguageSpecificTextSet("LSTB5363BC7\_0?cpp=::|nu=.");MaximumDuration Property |

Gets or sets the maximum allowed duration of the entire record. When new frames are recorded,
old frames that are more distant than MaximumDuration will be dropped. The default duration is
10 seconds.

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public TimeSpan MaximumDuration { get; set; }
```

```
Public Property MaximumDuration As TimeSpan
	Get
	Set
```

AddLanguageTabSet("ID0EBCA");

#### Property Value

Type: [TimeSpan](https://docs.microsoft.com/dotnet/api/system.timespan)  

[Missing <value> documentation for "P:Grasshopper.GUI.GH\_MouseTracker.MaximumDuration"]

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_MouseTracker Class](T_Grasshopper_GUI_GH_MouseTracker.htm)

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)