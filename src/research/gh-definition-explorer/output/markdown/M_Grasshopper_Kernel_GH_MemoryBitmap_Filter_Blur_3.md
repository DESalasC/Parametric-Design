# M_Grasshopper_Kernel_GH_MemoryBitmap_Filter_Blur_3

﻿ GH\_MemoryBitmap.Filter\_Blur Method (Int32, Int32, Int32)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_MemoryBitmap Class](../html/T_Grasshopper_Kernel_GH_MemoryBitmap.htm "GH_MemoryBitmap Class")

[GH\_MemoryBitmap Methods](../html/Methods_T_Grasshopper_Kernel_GH_MemoryBitmap.htm "GH_MemoryBitmap Methods")

[Filter\_Blur Method](../html/Overload_Grasshopper_Kernel_GH_MemoryBitmap_Filter_Blur.htm "Filter_Blur Method ")

[Filter\_Blur Method](../html/M_Grasshopper_Kernel_GH_MemoryBitmap_Filter_Blur.htm "Filter_Blur Method ")

[Filter\_Blur Method (Int32)](../html/M_Grasshopper_Kernel_GH_MemoryBitmap_Filter_Blur_1.htm "Filter_Blur Method (Int32)")

[Filter\_Blur Method (Int32, Int32)](../html/M_Grasshopper_Kernel_GH_MemoryBitmap_Filter_Blur_2.htm "Filter_Blur Method (Int32, Int32)")

[Filter\_Blur Method (Int32, Int32, Int32)](../html/M_Grasshopper_Kernel_GH_MemoryBitmap_Filter_Blur_3.htm "Filter_Blur Method (Int32, Int32, Int32)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_MemoryBitmapAddLanguageSpecificTextSet("LSTB32957A4\_0?cpp=::|nu=.");Filter\_Blur Method (Int32, Int32, Int32) |

Blur the image N times in both directions.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public void Filter_Blur(
	int N,
	int interior_weight,
	int exterior_weight
)
```

```
Public Sub Filter_Blur ( 
	N As Integer,
	interior_weight As Integer,
	exterior_weight As Integer
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

N
:   Type: [SystemAddLanguageSpecificTextSet("LSTB32957A4\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Number of times to perform the blurring operation.

interior\_weight
:   Type: [SystemAddLanguageSpecificTextSet("LSTB32957A4\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Weighting factor for pixels at the center of the convolution matrix.

exterior\_weight
:   Type: [SystemAddLanguageSpecificTextSet("LSTB32957A4\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Weighting factor for pixels at the edges of the convolution matrix.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_MemoryBitmap Class](T_Grasshopper_Kernel_GH_MemoryBitmap.htm)

[Filter\_Blur Overload](Overload_Grasshopper_Kernel_GH_MemoryBitmap_Filter_Blur.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)