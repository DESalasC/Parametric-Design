# M_Grasshopper_Kernel_GH_Document_ScheduleSolution_1

﻿ GH\_Document.ScheduleSolution Method (Int32, GH\_Document.GH\_ScheduleDelegate)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_Document Class](../html/T_Grasshopper_Kernel_GH_Document.htm "GH_Document Class")

[GH\_Document Methods](../html/Methods_T_Grasshopper_Kernel_GH_Document.htm "GH_Document Methods")

[ScheduleSolution Method](../html/Overload_Grasshopper_Kernel_GH_Document_ScheduleSolution.htm "ScheduleSolution Method ")

[ScheduleSolution Method (Int32)](../html/M_Grasshopper_Kernel_GH_Document_ScheduleSolution.htm "ScheduleSolution Method (Int32)")

[ScheduleSolution Method (Int32, GH\_Document.GH\_ScheduleDelegate)](../html/M_Grasshopper_Kernel_GH_Document_ScheduleSolution_1.htm "ScheduleSolution Method (Int32, GH_Document.GH_ScheduleDelegate)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_DocumentAddLanguageSpecificTextSet("LST1FF74EE0\_0?cpp=::|nu=.");ScheduleSolution Method (Int32, GH\_DocumentAddLanguageSpecificTextSet("LST1FF74EE0\_1?cpp=::|nu=.");GH\_ScheduleDelegate) |

Schedule a new solution after a specified time interval. The schedule is erased if another solution
is triggered before the schedule is executed. Tight schedules override loose schedules.
If this method is called *during* a solution, the schedule will be started
after the current solution completes.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public void ScheduleSolution(
	int delay,
	GH_DocumentAddLanguageSpecificTextSet("LST1FF74EE0_2?cs=.|vb=.|cpp=::|nu=.|fs=.");GH_ScheduleDelegate callback
)
```

```
Public Sub ScheduleSolution ( 
	delay As Integer,
	callback As GH_DocumentAddLanguageSpecificTextSet("LST1FF74EE0_3?cs=.|vb=.|cpp=::|nu=.|fs=.");GH_ScheduleDelegate
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

delay
:   Type: [SystemAddLanguageSpecificTextSet("LST1FF74EE0\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    The delay (in milliseconds) between the completion of this solution
    and the start of the scheduled solution. If the delay is 1ms or more, a timer will be used
    to trigger a new solution sometime in the future. If a delay of 0ms is used, then the
    next solution will run recursively within the current solution. You should not use a delay of
    zero milliseconds too often as it will cause the Rhino process to run out of stack-space.
    The SolutionDepth property can be used to see how deeply recursive the solution currently is.

callback
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LST1FF74EE0\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_DocumentAddLanguageSpecificTextSet("LST1FF74EE0\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_ScheduleDelegate](T_Grasshopper_Kernel_GH_Document_GH_ScheduleDelegate.htm)  
    If not null, the callback will be called *before* the scheduled solution
    is triggered.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Document Class](T_Grasshopper_Kernel_GH_Document.htm)

[ScheduleSolution Overload](Overload_Grasshopper_Kernel_GH_Document_ScheduleSolution.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)