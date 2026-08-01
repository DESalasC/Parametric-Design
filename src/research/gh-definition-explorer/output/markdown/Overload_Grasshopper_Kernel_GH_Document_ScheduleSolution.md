# Overload_Grasshopper_Kernel_GH_Document_ScheduleSolution

﻿ GH\_Document.ScheduleSolution Method 

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
| GH\_DocumentAddLanguageSpecificTextSet("LSTF463B4B1\_0?cpp=::|nu=.");ScheduleSolution Method |

![](../icons/SectionExpanded.png)Overload List

|  | Name | Description |
| --- | --- | --- |
| Public method | [ScheduleSolution(Int32)](M_Grasshopper_Kernel_GH_Document_ScheduleSolution.htm) | Schedule a new solution after a specified time interval. The schedule is erased if another solution is triggered before the schedule is executed. Tight schedules override loose schedules. If this method is called *during* a solution, the schedule will be started after the current solution completes. |
| Public method | [ScheduleSolution(Int32, GH\_DocumentAddLanguageSpecificTextSet("LSTF463B4B1\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_ScheduleDelegate)](M_Grasshopper_Kernel_GH_Document_ScheduleSolution_1.htm) | Schedule a new solution after a specified time interval. The schedule is erased if another solution is triggered before the schedule is executed. Tight schedules override loose schedules. If this method is called *during* a solution, the schedule will be started after the current solution completes. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Document Class](T_Grasshopper_Kernel_GH_Document.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)