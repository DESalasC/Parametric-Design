# M_Grasshopper_Kernel_GH_MemoryBitmap_Filter_Multiply_1

﻿ GH\_MemoryBitmap.Filter\_Multiply Method (GH\_BitmapChannel, Double, Byte)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_MemoryBitmap Class](../html/T_Grasshopper_Kernel_GH_MemoryBitmap.htm "GH_MemoryBitmap Class")

[GH\_MemoryBitmap Methods](../html/Methods_T_Grasshopper_Kernel_GH_MemoryBitmap.htm "GH_MemoryBitmap Methods")

[Filter\_Multiply Method](../html/Overload_Grasshopper_Kernel_GH_MemoryBitmap_Filter_Multiply.htm "Filter_Multiply Method ")

[Filter\_Multiply Method (GH\_BitmapChannel, Double)](../html/M_Grasshopper_Kernel_GH_MemoryBitmap_Filter_Multiply.htm "Filter_Multiply Method (GH_BitmapChannel, Double)")

[Filter\_Multiply Method (GH\_BitmapChannel, Double, Byte)](../html/M_Grasshopper_Kernel_GH_MemoryBitmap_Filter_Multiply_1.htm "Filter_Multiply Method (GH_BitmapChannel, Double, Byte)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_MemoryBitmapAddLanguageSpecificTextSet("LST208F6432\_0?cpp=::|nu=.");Filter\_Multiply Method (GH\_BitmapChannel, Double, Byte) |

Multiply all values in a specific channel with a specific factor,
using a custom scaling center anchor.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public void Filter_Multiply(
	GH_BitmapChannel channel,
	double factor,
	byte anchor
)
```

```
Public Sub Filter_Multiply ( 
	channel As GH_BitmapChannel,
	factor As Double,
	anchor As Byte
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

channel
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LST208F6432\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_BitmapChannel](T_Grasshopper_Kernel_GH_BitmapChannel.htm)  
    Channel(s) to multiply.

factor
:   Type: [SystemAddLanguageSpecificTextSet("LST208F6432\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Double](https://docs.microsoft.com/dotnet/api/system.double)  
    Multiplication factor.

anchor
:   Type: [SystemAddLanguageSpecificTextSet("LST208F6432\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Byte](https://docs.microsoft.com/dotnet/api/system.byte)  
    Byte value to scale from.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_MemoryBitmap Class](T_Grasshopper_Kernel_GH_MemoryBitmap.htm)

[Filter\_Multiply Overload](Overload_Grasshopper_Kernel_GH_MemoryBitmap_Filter_Multiply.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)