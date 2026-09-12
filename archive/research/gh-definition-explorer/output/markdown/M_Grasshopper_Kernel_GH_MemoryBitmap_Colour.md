# M_Grasshopper_Kernel_GH_MemoryBitmap_Colour

﻿ GH\_MemoryBitmap.Colour Method (Int32, Int32)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_MemoryBitmap Class](../html/T_Grasshopper_Kernel_GH_MemoryBitmap.htm "GH_MemoryBitmap Class")

[GH\_MemoryBitmap Methods](../html/Methods_T_Grasshopper_Kernel_GH_MemoryBitmap.htm "GH_MemoryBitmap Methods")

[Colour Method](../html/Overload_Grasshopper_Kernel_GH_MemoryBitmap_Colour.htm "Colour Method ")

[Colour Method (Int32, Int32)](../html/M_Grasshopper_Kernel_GH_MemoryBitmap_Colour.htm "Colour Method (Int32, Int32)")

[Colour Method (Int32, Int32, Color)](../html/M_Grasshopper_Kernel_GH_MemoryBitmap_Colour_1.htm "Colour Method (Int32, Int32, Color)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_MemoryBitmapAddLanguageSpecificTextSet("LSTCC314A9B\_0?cpp=::|nu=.");Colour Method (Int32, Int32) |

Gets the colour at the given pixel coordinates.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public Color Colour(
	int x,
	int y
)
```

```
Public Function Colour ( 
	x As Integer,
	y As Integer
) As Color
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

x
:   Type: [SystemAddLanguageSpecificTextSet("LSTCC314A9B\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    X coordinate (column) of pixel. Must be on image interior.

y
:   Type: [SystemAddLanguageSpecificTextSet("LSTCC314A9B\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Y coordinate (column) of pixel. Must be on image interior.

#### Return Value

Type: [Color](https://docs.microsoft.com/dotnet/api/system.drawing.color)  
Colour at given pixel.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_MemoryBitmap Class](T_Grasshopper_Kernel_GH_MemoryBitmap.htm)

[Colour Overload](Overload_Grasshopper_Kernel_GH_MemoryBitmap_Colour.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)