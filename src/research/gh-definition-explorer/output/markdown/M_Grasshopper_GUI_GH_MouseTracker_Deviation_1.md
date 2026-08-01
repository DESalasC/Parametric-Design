# M_Grasshopper_GUI_GH_MouseTracker_Deviation_1

﻿ GH\_MouseTracker.Deviation Method (DateTime, DateTime)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH\_MouseTracker Class](../html/T_Grasshopper_GUI_GH_MouseTracker.htm "GH_MouseTracker Class")

[GH\_MouseTracker Methods](../html/Methods_T_Grasshopper_GUI_GH_MouseTracker.htm "GH_MouseTracker Methods")

[Deviation Method](../html/Overload_Grasshopper_GUI_GH_MouseTracker_Deviation.htm "Deviation Method ")

[Deviation Method](../html/M_Grasshopper_GUI_GH_MouseTracker_Deviation.htm "Deviation Method ")

[Deviation Method (DateTime, DateTime)](../html/M_Grasshopper_GUI_GH_MouseTracker_Deviation_1.htm "Deviation Method (DateTime, DateTime)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_MouseTrackerAddLanguageSpecificTextSet("LST510832C\_0?cpp=::|nu=.");Deviation Method (DateTime, DateTime) |

Gets the maximum deviation of the recorded mouse path.
The maximum deviation is the furthest distance the mouse has been
from the first point in the history span. It does **not** measure
the largest deviation between any two points in the time span, only
the first and any subsequent point.

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public double Deviation(
	DateTime t0,
	DateTime t1
)
```

```
Public Function Deviation ( 
	t0 As DateTime,
	t1 As DateTime
) As Double
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

t0
:   Type: [SystemAddLanguageSpecificTextSet("LST510832C\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");DateTime](https://docs.microsoft.com/dotnet/api/system.datetime)  
    Represents the earliest time to include.

t1
:   Type: [SystemAddLanguageSpecificTextSet("LST510832C\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");DateTime](https://docs.microsoft.com/dotnet/api/system.datetime)  
    Represents the latest time to include.

#### Return Value

Type: [Double](https://docs.microsoft.com/dotnet/api/system.double)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_MouseTracker Class](T_Grasshopper_GUI_GH_MouseTracker.htm)

[Deviation Overload](Overload_Grasshopper_GUI_GH_MouseTracker_Deviation.htm)

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)