# M_Grasshopper_GUI_GH_SamplingSphere_SampleSphere_1

﻿ GH\_SamplingSphere.SampleSphere Method (Sphere, GH\_MemoryBitmap)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH\_SamplingSphere Class](../html/T_Grasshopper_GUI_GH_SamplingSphere.htm "GH_SamplingSphere Class")

[GH\_SamplingSphere Methods](../html/Methods_T_Grasshopper_GUI_GH_SamplingSphere.htm "GH_SamplingSphere Methods")

[SampleSphere Method](../html/Overload_Grasshopper_GUI_GH_SamplingSphere_SampleSphere.htm "SampleSphere Method ")

[SampleSphere Method (Sphere)](../html/M_Grasshopper_GUI_GH_SamplingSphere_SampleSphere.htm "SampleSphere Method (Sphere)")

[SampleSphere Method (Sphere, GH\_MemoryBitmap)](../html/M_Grasshopper_GUI_GH_SamplingSphere_SampleSphere_1.htm "SampleSphere Method (Sphere, GH_MemoryBitmap)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_SamplingSphereAddLanguageSpecificTextSet("LSTA2482310\_0?cpp=::|nu=.");SampleSphere Method (Sphere, GH\_MemoryBitmap) |

Sample a sphere with a UV texture and return a bitmap of sampled values.

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public Bitmap SampleSphere(
	Sphere sphere,
	GH_MemoryBitmap texture
)
```

```
Public Function SampleSphere ( 
	sphere As Sphere,
	texture As GH_MemoryBitmap
) As Bitmap
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

sphere
:   Type: Sphere  
    Sphere to sample, it should be centered on the world origin.

texture
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LSTA2482310\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_MemoryBitmap](T_Grasshopper_Kernel_GH_MemoryBitmap.htm)  
    Texture to sample, the texture will not be modified.

#### Return Value

Type: [Bitmap](https://docs.microsoft.com/dotnet/api/system.drawing.bitmap)  
A bitmap of Size x Size pixels.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_SamplingSphere Class](T_Grasshopper_GUI_GH_SamplingSphere.htm)

[SampleSphere Overload](Overload_Grasshopper_GUI_GH_SamplingSphere_SampleSphere.htm)

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)