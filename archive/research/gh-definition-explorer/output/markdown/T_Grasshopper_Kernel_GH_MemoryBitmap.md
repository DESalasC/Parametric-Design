# T_Grasshopper_Kernel_GH_MemoryBitmap

﻿ GH\_MemoryBitmap Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_MemoryBitmap Class](../html/T_Grasshopper_Kernel_GH_MemoryBitmap.htm "GH_MemoryBitmap Class")

[GH\_MemoryBitmap Constructor](../html/Overload_Grasshopper_Kernel_GH_MemoryBitmap__ctor.htm "GH_MemoryBitmap Constructor ")

[GH\_MemoryBitmap Properties](../html/Properties_T_Grasshopper_Kernel_GH_MemoryBitmap.htm "GH_MemoryBitmap Properties")

[GH\_MemoryBitmap Methods](../html/Methods_T_Grasshopper_Kernel_GH_MemoryBitmap.htm "GH_MemoryBitmap Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_MemoryBitmap Class |

Utility class for ultra-fast bitmap sampling and filters.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST7C9A90DC\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.KernelAddLanguageSpecificTextSet("LST7C9A90DC\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_MemoryBitmap

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public sealed class GH_MemoryBitmap
```

```
Public NotInheritable Class GH_MemoryBitmap
```

AddLanguageTabSet("ID1EBCA");

The GH\_MemoryBitmap type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_MemoryBitmap(Bitmap)](M_Grasshopper_Kernel_GH_MemoryBitmap__ctor.htm) | Default constructor. |
| Public method | [GH\_MemoryBitmap(Bitmap, WrapMode)](M_Grasshopper_Kernel_GH_MemoryBitmap__ctor_1.htm) | Constructor with Wrap mode override. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [HasAlphaChannel](P_Grasshopper_Kernel_GH_MemoryBitmap_HasAlphaChannel.htm) | Gets a value indicating whether or not the local image has an alpha channel defined. |
| Public property | [Height](P_Grasshopper_Kernel_GH_MemoryBitmap_Height.htm) | Gets the height (in pixels) of the local image. |
| Public property | [SizeOf](P_Grasshopper_Kernel_GH_MemoryBitmap_SizeOf.htm) | Gets the size (in bytes) of the local image. |
| Public property | [Width](P_Grasshopper_Kernel_GH_MemoryBitmap_Width.htm) | Gets the width (in pixels) of the local image. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [A](M_Grasshopper_Kernel_GH_MemoryBitmap_A.htm) | Gets the alpha channel value at the given pixel coordinates. |
| Public method | [B](M_Grasshopper_Kernel_GH_MemoryBitmap_B.htm) | Gets the blue channel value at the given pixel coordinates. |
| Public method | [Colour(Int32, Int32)](M_Grasshopper_Kernel_GH_MemoryBitmap_Colour.htm) | Gets the colour at the given pixel coordinates. |
| Public method | [Colour(Int32, Int32, Color)](M_Grasshopper_Kernel_GH_MemoryBitmap_Colour_1.htm) | Sets the colour at the given pixel coordinates. |
| Public method | [CopyChannel](M_Grasshopper_Kernel_GH_MemoryBitmap_CopyChannel.htm) | Copy the contents of one channel into another. |
| Public method | [Filter\_AlphaEdges](M_Grasshopper_Kernel_GH_MemoryBitmap_Filter_AlphaEdges.htm) | Set the alpha component on all edges to a specific value. |
| Public method | [Filter\_BlurAddLanguageSpecificTextSet("LST7C9A90DC\_2?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_GH_MemoryBitmap_Filter_Blur.htm) | Blur the image in both directions. |
| Public method | [Filter\_Blur(Int32)](M_Grasshopper_Kernel_GH_MemoryBitmap_Filter_Blur_1.htm) | Blur the image N times in both directions. |
| Public method | [Filter\_Blur(Int32, Int32)](M_Grasshopper_Kernel_GH_MemoryBitmap_Filter_Blur_2.htm) | Blur the image in both directions. |
| Public method | [Filter\_Blur(Int32, Int32, Int32)](M_Grasshopper_Kernel_GH_MemoryBitmap_Filter_Blur_3.htm) | Blur the image N times in both directions. |
| Public method | [Filter\_BlurAlpha](M_Grasshopper_Kernel_GH_MemoryBitmap_Filter_BlurAlpha.htm) | Blur the alpha channel of the image N times in both directions. |
| Public method | [Filter\_Contrast](M_Grasshopper_Kernel_GH_MemoryBitmap_Filter_Contrast.htm) | Adjust the contrast of a specific channel. |
| Public method | [Filter\_DitherPattern](M_Grasshopper_Kernel_GH_MemoryBitmap_Filter_DitherPattern.htm) | Create a checkerboard dither pattern. |
| Public method | [Filter\_DropShadow](M_Grasshopper_Kernel_GH_MemoryBitmap_Filter_DropShadow.htm) | Add a drop-shadow to the image. Image is not grown, so if you want the drop shadow to extend beyond the image boundaries, you have to add padding to the image first. |
| Public method | [Filter\_Dullify](M_Grasshopper_Kernel_GH_MemoryBitmap_Filter_Dullify.htm) | Reduces contrast based on opacity. This filter pulls all colours towards dull grey, without wrecking drop-shadows. |
| Public method | [Filter\_Equalize](M_Grasshopper_Kernel_GH_MemoryBitmap_Filter_Equalize.htm) | Set all the values in a specific channel to a specific value. |
| Public method | [Filter\_GreyScaleAddLanguageSpecificTextSet("LST7C9A90DC\_3?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_GH_MemoryBitmap_Filter_GreyScale.htm) | Convert the image to a greyscale shadow of its former self. |
| Public method | [Filter\_GreyScale(Double)](M_Grasshopper_Kernel_GH_MemoryBitmap_Filter_GreyScale_1.htm) | Convert the image to a greyscale shadow of its former self. |
| Public method | [Filter\_HueScale](M_Grasshopper_Kernel_GH_MemoryBitmap_Filter_HueScale.htm) | Convert the image to a greyscale representation of the hues. |
| Public method | [Filter\_Invert](M_Grasshopper_Kernel_GH_MemoryBitmap_Filter_Invert.htm) | Invert all values in a specific channel. |
| Public method | [Filter\_LumScale](M_Grasshopper_Kernel_GH_MemoryBitmap_Filter_LumScale.htm) | Convert the image to a greyscale representation of the luminance. |
| Public method | [Filter\_Multiply(GH\_BitmapChannel, Double)](M_Grasshopper_Kernel_GH_MemoryBitmap_Filter_Multiply.htm) | Multiply all values in a specific channel with a specific factor. |
| Public method | [Filter\_Multiply(GH\_BitmapChannel, Double, Byte)](M_Grasshopper_Kernel_GH_MemoryBitmap_Filter_Multiply_1.htm) | Multiply all values in a specific channel with a specific factor, using a custom scaling center anchor. |
| Public method | [Filter\_SatScale](M_Grasshopper_Kernel_GH_MemoryBitmap_Filter_SatScale.htm) | Convert the image to a greyscale representation of the saturation. |
| Public method | [Filter\_Shift](M_Grasshopper_Kernel_GH_MemoryBitmap_Filter_Shift.htm) | Shift all values in a specific channel with a specific amount. |
| Public method | [Filter\_SpectrumScale](M_Grasshopper_Kernel_GH_MemoryBitmap_Filter_SpectrumScale.htm) | Convert the image to a spectral representation of the hues. |
| Public method | [Filter\_Tint](M_Grasshopper_Kernel_GH_MemoryBitmap_Filter_Tint.htm) | Colorize the image using Hue and Saturation from a base colour. |
| Public method | [G](M_Grasshopper_Kernel_GH_MemoryBitmap_G.htm) | Gets the greeb channel value at the given pixel coordinates. |
| Public method | [OpaqueArea](M_Grasshopper_Kernel_GH_MemoryBitmap_OpaqueArea.htm) | Find the opaque area of a bitmap. The opaque area is the rectangle that contains pixels with a colour that is not fully transparent. |
| Public methodStatic member | [PadBitmap](M_Grasshopper_Kernel_GH_MemoryBitmap_PadBitmap.htm) | Add padding edges around a bitmap. |
| Public method | [R](M_Grasshopper_Kernel_GH_MemoryBitmap_R.htm) | Gets the red channel value at the given pixel coordinates. |
| Public method | [Release](M_Grasshopper_Kernel_GH_MemoryBitmap_Release.htm) | Release the locked bits. You **must** call this function when you are done with this GH\_MemoryBitmap instance. |
| Public method | [Sample(Double, Double, ColorAddLanguageSpecificTextSet("LST7C9A90DC\_4?cpp=%");)](M_Grasshopper_Kernel_GH_MemoryBitmap_Sample.htm) | Top level sampling function for interpolated sampling. |
| Public method | [Sample(Int32, Int32, ColorAddLanguageSpecificTextSet("LST7C9A90DC\_5?cpp=%");)](M_Grasshopper_Kernel_GH_MemoryBitmap_Sample_1.htm) | Top level sampling function. |
| Public methodStatic member | [ShrinkBitmap](M_Grasshopper_Kernel_GH_MemoryBitmap_ShrinkBitmap.htm) | Shrink an image by removing all outer columns and rows that contain only fully transparent pixels. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)