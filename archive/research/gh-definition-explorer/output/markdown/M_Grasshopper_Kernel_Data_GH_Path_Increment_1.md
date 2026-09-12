# M_Grasshopper_Kernel_Data_GH_Path_Increment_1

﻿ GH\_Path.Increment Method (Int32, Int32)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Data](../html/N_Grasshopper_Kernel_Data.htm "Grasshopper.Kernel.Data")

[GH\_Path Class](../html/T_Grasshopper_Kernel_Data_GH_Path.htm "GH_Path Class")

[GH\_Path Methods](../html/Methods_T_Grasshopper_Kernel_Data_GH_Path.htm "GH_Path Methods")

[Increment Method](../html/Overload_Grasshopper_Kernel_Data_GH_Path_Increment.htm "Increment Method ")

[Increment Method (Int32)](../html/M_Grasshopper_Kernel_Data_GH_Path_Increment.htm "Increment Method (Int32)")

[Increment Method (Int32, Int32)](../html/M_Grasshopper_Kernel_Data_GH_Path_Increment_1.htm "Increment Method (Int32, Int32)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_PathAddLanguageSpecificTextSet("LST8095330A\_0?cpp=::|nu=.");Increment Method (Int32, Int32) |

Increment a specific index in this path by one.

**Namespace:**
 [Grasshopper.Kernel.Data](N_Grasshopper_Kernel_Data.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public GH_Path Increment(
	int index,
	int offset
)
```

```
Public Function Increment ( 
	index As Integer,
	offset As Integer
) As GH_Path
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

index
:   Type: [SystemAddLanguageSpecificTextSet("LST8095330A\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Index to increment. Valis indices are (-Length+1) to (Length-1).

offset
:   Type: [SystemAddLanguageSpecificTextSet("LST8095330A\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Amount to increment.

#### Return Value

Type: [GH\_Path](T_Grasshopper_Kernel_Data_GH_Path.htm)  
A new path with incremented index.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Path Class](T_Grasshopper_Kernel_Data_GH_Path.htm)

[Increment Overload](Overload_Grasshopper_Kernel_Data_GH_Path_Increment.htm)

[Grasshopper.Kernel.Data Namespace](N_Grasshopper_Kernel_Data.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)