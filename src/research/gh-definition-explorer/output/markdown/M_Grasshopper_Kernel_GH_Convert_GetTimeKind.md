# M_Grasshopper_Kernel_GH_Convert_GetTimeKind

﻿ GH\_Convert.GetTimeKind Method (DateTime)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_Convert Class](../html/T_Grasshopper_Kernel_GH_Convert.htm "GH_Convert Class")

[GH\_Convert Methods](../html/Methods_T_Grasshopper_Kernel_GH_Convert.htm "GH_Convert Methods")

[GetTimeKind Method](../html/Overload_Grasshopper_Kernel_GH_Convert_GetTimeKind.htm "GetTimeKind Method ")

[GetTimeKind Method (DateTime)](../html/M_Grasshopper_Kernel_GH_Convert_GetTimeKind.htm "GetTimeKind Method (DateTime)")

[GetTimeKind Method (DateTime, DateTime)](../html/M_Grasshopper_Kernel_GH_Convert_GetTimeKind_1.htm "GetTimeKind Method (DateTime, DateTime)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ConvertAddLanguageSpecificTextSet("LSTB168FB88\_0?cpp=::|nu=.");GetTimeKind Method (DateTime) |

Gets the kind of time implied by a System.DateTime value.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static GH_TimeKind GetTimeKind(
	DateTime time
)
```

```
Public Shared Function GetTimeKind ( 
	time As DateTime
) As GH_TimeKind
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

time
:   Type: [SystemAddLanguageSpecificTextSet("LSTB168FB88\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");DateTime](https://docs.microsoft.com/dotnet/api/system.datetime)  
    Time to evaluate.

#### Return Value

Type: [GH\_TimeKind](T_Grasshopper_Kernel_GH_TimeKind.htm)  
GH\_TimeKind.PureTime, GH\_TimeKind.PureDate or GH\_TimeKind.DateAndTime.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Convert Class](T_Grasshopper_Kernel_GH_Convert.htm)

[GetTimeKind Overload](Overload_Grasshopper_Kernel_GH_Convert_GetTimeKind.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)