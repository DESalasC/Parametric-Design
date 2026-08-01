# M_Grasshopper_Kernel_GH_MemoryBitmap_Sample_1

﻿ GH\_MemoryBitmap.Sample Method (Int32, Int32, Color)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_MemoryBitmap Class](../html/T_Grasshopper_Kernel_GH_MemoryBitmap.htm "GH_MemoryBitmap Class")

[GH\_MemoryBitmap Methods](../html/Methods_T_Grasshopper_Kernel_GH_MemoryBitmap.htm "GH_MemoryBitmap Methods")

[Sample Method](../html/Overload_Grasshopper_Kernel_GH_MemoryBitmap_Sample.htm "Sample Method ")

[Sample Method (Double, Double, Color)](../html/M_Grasshopper_Kernel_GH_MemoryBitmap_Sample.htm "Sample Method (Double, Double, Color)")

[Sample Method (Int32, Int32, Color)](../html/M_Grasshopper_Kernel_GH_MemoryBitmap_Sample_1.htm "Sample Method (Int32, Int32, Color)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_MemoryBitmapAddLanguageSpecificTextSet("LST84B5FD0D\_0?cpp=::|nu=.");Sample Method (Int32, Int32, ColorAddLanguageSpecificTextSet("LST84B5FD0D\_1?cpp=%");) |

Top level sampling function.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public bool Sample(
	int x,
	int y,
	ref Color col
)
```

```
Public Function Sample ( 
	x As Integer,
	y As Integer,
	ByRef col As Color
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

x
:   Type: [SystemAddLanguageSpecificTextSet("LST84B5FD0D\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Unmapped x pixel coordinate.

y
:   Type: [SystemAddLanguageSpecificTextSet("LST84B5FD0D\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Unmapped y pixel coordinate.

col
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST84B5FD0D\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");Color](https://docs.microsoft.com/dotnet/api/system.drawing.color)AddLanguageSpecificTextSet("LST84B5FD0D\_5?cpp=%");  
    Colour output.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True on success, false if pixels could not be sampled.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_MemoryBitmap Class](T_Grasshopper_Kernel_GH_MemoryBitmap.htm)

[Sample Overload](Overload_Grasshopper_Kernel_GH_MemoryBitmap_Sample.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)