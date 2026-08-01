# M_Grasshopper_Kernel_GH_Convert_CreatePureTime

﻿ GH\_Convert.CreatePureTime Method (DateTime)

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
| GH\_ConvertAddLanguageSpecificTextSet("LST42C1D57E\_0?cpp=::|nu=.");CreatePureTime Method (DateTime) |

Convert a datetime structure into a pure time, i.e. remove the date portion.
As per convention, this means setting the year, month and day to 1.

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
	DateTime date
)
```

```
Public Shared Function CreatePureTime ( 
	date As DateTime
) As DateTime
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

date
:   Type: [SystemAddLanguageSpecificTextSet("LST42C1D57E\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");DateTime](https://docs.microsoft.com/dotnet/api/system.datetime)

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