# Overload_Grasshopper_Kernel_GH_Convert_CreatePureTime

﻿ GH\_Convert.CreatePureTime Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_Convert Class](../html/T_Grasshopper_Kernel_GH_Convert.htm "GH_Convert Class")

[GH\_Convert Methods](../html/Methods_T_Grasshopper_Kernel_GH_Convert.htm "GH_Convert Methods")

[CreatePureTime Method](../html/Overload_Grasshopper_Kernel_GH_Convert_CreatePureTime.htm "CreatePureTime Method ")

[CreatePureTime Method (DateTime)](../html/M_Grasshopper_Kernel_GH_Convert_CreatePureTime.htm "CreatePureTime Method (DateTime)")

[CreatePureTime Method (Int32, Int32, Int32)](../html/M_Grasshopper_Kernel_GH_Convert_CreatePureTime_1.htm "CreatePureTime Method (Int32, Int32, Int32)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ConvertAddLanguageSpecificTextSet("LST778DCC6\_0?cpp=::|nu=.");CreatePureTime Method |

![](../icons/SectionExpanded.png)Overload List

|  | Name | Description |
| --- | --- | --- |
| Public methodStatic member | [CreatePureTime(DateTime)](M_Grasshopper_Kernel_GH_Convert_CreatePureTime.htm) | Convert a datetime structure into a pure time, i.e. remove the date portion. As per convention, this means setting the year, month and day to 1. |
| Public methodStatic member | [CreatePureTime(Int32, Int32, Int32)](M_Grasshopper_Kernel_GH_Convert_CreatePureTime_1.htm) | Create a pure time instance. If the total number of hours, minutes and seconds exceeds a full year then it is not possible to create a pure time and the largest possible pure time will be returned instead. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Convert Class](T_Grasshopper_Kernel_GH_Convert.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)