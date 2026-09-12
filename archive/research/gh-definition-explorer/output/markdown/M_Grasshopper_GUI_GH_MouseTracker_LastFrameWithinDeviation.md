# M_Grasshopper_GUI_GH_MouseTracker_LastFrameWithinDeviation

﻿ GH\_MouseTracker.LastFrameWithinDeviation Method 

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
| GH\_MouseTrackerAddLanguageSpecificTextSet("LSTF5A6F392\_0?cpp=::|nu=.");LastFrameWithinDeviation Method |

Starting from the youngest frame, finds the oldest frame that is still
within a maximum deviation of the youngest frame.

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public int LastFrameWithinDeviation(
	double deviation
)
```

```
Public Function LastFrameWithinDeviation ( 
	deviation As Double
) As Integer
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

deviation
:   Type: [SystemAddLanguageSpecificTextSet("LSTF5A6F392\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Double](https://docs.microsoft.com/dotnet/api/system.double)  
    Maximum allowed deviation.

#### Return Value

Type: [Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
The index of the oldest frame with a distance less than the
deviation from the youngest frame, or -1 if no such frame could be found.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_MouseTracker Class](T_Grasshopper_GUI_GH_MouseTracker.htm)

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)