# M_Grasshopper_Kernel_GH_Convert_CreatePureTime_1

﻿ GH\_Convert.CreatePureTime Method (Int32, Int32, Int32)

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
| GH\_ConvertAddLanguageSpecificTextSet("LST9720331\_0?cpp=::|nu=.");CreatePureTime Method (Int32, Int32, Int32) |

Create a pure time instance. If the total number of hours, minutes and seconds exceeds a full year
then it is not possible to create a pure time and the largest possible pure time will be returned instead.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static DateTime CreatePureTime(
	int hours,
	int minutes,
	int seconds
)
```

```
Public Shared Function CreatePureTime ( 
	hours As Integer,
	minutes As Integer,
	seconds As Integer
) As DateTime
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

hours
:   Type: [SystemAddLanguageSpecificTextSet("LST9720331\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)

minutes
:   Type: [SystemAddLanguageSpecificTextSet("LST9720331\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)

seconds
:   Type: [SystemAddLanguageSpecificTextSet("LST9720331\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)

#### Return Value

Type: [DateTime](https://docs.microsoft.com/dotnet/api/system.datetime)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Convert Class](T_Grasshopper_Kernel_GH_Convert.htm)

[CreatePureTime Overload](Overload_Grasshopper_Kernel_GH_Convert_CreatePureTime.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)