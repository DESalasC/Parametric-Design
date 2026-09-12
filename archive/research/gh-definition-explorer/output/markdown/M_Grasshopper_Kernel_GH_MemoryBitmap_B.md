# M_Grasshopper_Kernel_GH_MemoryBitmap_B

﻿ GH\_MemoryBitmap.B Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_MemoryBitmap Class](../html/T_Grasshopper_Kernel_GH_MemoryBitmap.htm "GH_MemoryBitmap Class")

[GH\_MemoryBitmap Methods](../html/Methods_T_Grasshopper_Kernel_GH_MemoryBitmap.htm "GH_MemoryBitmap Methods")

[A Method](../html/M_Grasshopper_Kernel_GH_MemoryBitmap_A.htm "A Method ")

[B Method](../html/M_Grasshopper_Kernel_GH_MemoryBitmap_B.htm "B Method ")

[Colour Method](../html/Overload_Grasshopper_Kernel_GH_MemoryBitmap_Colour.htm "Colour Method ")

[CopyChannel Method](../html/M_Grasshopper_Kernel_GH_MemoryBitmap_CopyChannel.htm "CopyChannel Method ")

[Filter\_AlphaEdges Method](../html/M_Grasshopper_Kernel_GH_MemoryBitmap_Filter_AlphaEdges.htm "Filter_AlphaEdges Method ")

[Filter\_Blur Method](../html/Overload_Grasshopper_Kernel_GH_MemoryBitmap_Filter_Blur.htm "Filter_Blur Method ")

[Filter\_BlurAlpha Method](../html/M_Grasshopper_Kernel_GH_MemoryBitmap_Filter_BlurAlpha.htm "Filter_BlurAlpha Method ")

[Filter\_Contrast Method](../html/M_Grasshopper_Kernel_GH_MemoryBitmap_Filter_Contrast.htm "Filter_Contrast Method ")

[Filter\_DitherPattern Method](../html/M_Grasshopper_Kernel_GH_MemoryBitmap_Filter_DitherPattern.htm "Filter_DitherPattern Method ")

[Filter\_DropShadow Method](../html/M_Grasshopper_Kernel_GH_MemoryBitmap_Filter_DropShadow.htm "Filter_DropShadow Method ")

[Filter\_Dullify Method](../html/M_Grasshopper_Kernel_GH_MemoryBitmap_Filter_Dullify.htm "Filter_Dullify Method ")

[Filter\_Equalize Method](../html/M_Grasshopper_Kernel_GH_MemoryBitmap_Filter_Equalize.htm "Filter_Equalize Method ")

[Filter\_GreyScale Method](../html/Overload_Grasshopper_Kernel_GH_MemoryBitmap_Filter_GreyScale.htm "Filter_GreyScale Method ")

[Filter\_HueScale Method](../html/M_Grasshopper_Kernel_GH_MemoryBitmap_Filter_HueScale.htm "Filter_HueScale Method ")

[Filter\_Invert Method](../html/M_Grasshopper_Kernel_GH_MemoryBitmap_Filter_Invert.htm "Filter_Invert Method ")

[Filter\_LumScale Method](../html/M_Grasshopper_Kernel_GH_MemoryBitmap_Filter_LumScale.htm "Filter_LumScale Method ")

[Filter\_Multiply Method](../html/Overload_Grasshopper_Kernel_GH_MemoryBitmap_Filter_Multiply.htm "Filter_Multiply Method ")

[Filter\_SatScale Method](../html/M_Grasshopper_Kernel_GH_MemoryBitmap_Filter_SatScale.htm "Filter_SatScale Method ")

[Filter\_Shift Method](../html/M_Grasshopper_Kernel_GH_MemoryBitmap_Filter_Shift.htm "Filter_Shift Method ")

[Filter\_SpectrumScale Method](../html/M_Grasshopper_Kernel_GH_MemoryBitmap_Filter_SpectrumScale.htm "Filter_SpectrumScale Method ")

[Filter\_Tint Method](../html/M_Grasshopper_Kernel_GH_MemoryBitmap_Filter_Tint.htm "Filter_Tint Method ")

[G Method](../html/M_Grasshopper_Kernel_GH_MemoryBitmap_G.htm "G Method ")

[OpaqueArea Method](../html/M_Grasshopper_Kernel_GH_MemoryBitmap_OpaqueArea.htm "OpaqueArea Method ")

[PadBitmap Method](../html/M_Grasshopper_Kernel_GH_MemoryBitmap_PadBitmap.htm "PadBitmap Method ")

[R Method](../html/M_Grasshopper_Kernel_GH_MemoryBitmap_R.htm "R Method ")

[Release Method](../html/M_Grasshopper_Kernel_GH_MemoryBitmap_Release.htm "Release Method ")

[Sample Method](../html/Overload_Grasshopper_Kernel_GH_MemoryBitmap_Sample.htm "Sample Method ")

[ShrinkBitmap Method](../html/M_Grasshopper_Kernel_GH_MemoryBitmap_ShrinkBitmap.htm "ShrinkBitmap Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_MemoryBitmapAddLanguageSpecificTextSet("LST39B6B68A\_0?cpp=::|nu=.");B Method |

Gets the blue channel value at the given pixel coordinates.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public byte B(
	int x,
	int y
)
```

```
Public Function B ( 
	x As Integer,
	y As Integer
) As Byte
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

x
:   Type: [SystemAddLanguageSpecificTextSet("LST39B6B68A\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    X coordinate (column) of pixel. Must be on image interior.

y
:   Type: [SystemAddLanguageSpecificTextSet("LST39B6B68A\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Y coordinate (column) of pixel. Must be on image interior.

#### Return Value

Type: [Byte](https://docs.microsoft.com/dotnet/api/system.byte)  
Value of Blue channel at given pixel.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_MemoryBitmap Class](T_Grasshopper_Kernel_GH_MemoryBitmap.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)