# M_Grasshopper_GUI_GH_SamplingSphere_SampleSphere

﻿ GH\_SamplingSphere.SampleSphere Method (Sphere)

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
| GH\_SamplingSphereAddLanguageSpecificTextSet("LST2EF6F1B8\_0?cpp=::|nu=.");SampleSphere Method (Sphere) |

Sample the UV locations of a sphere. The sphere should be centered on the world origin.

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public Point2d[,] SampleSphere(
	Sphere sphere
)
```

```
Public Function SampleSphere ( 
	sphere As Sphere
) As Point2d(,)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

sphere
:   Type: Sphere  
    Sphere to sample.

#### Return Value

Type: AddLanguageSpecificTextSet("LST2EF6F1B8\_1?cpp=array&lt;");Point2dAddLanguageSpecificTextSet("LST2EF6F1B8\_2?cpp=,2&gt;|vb=(,)|nu=[,]");  
A two-dimensional array of Sphere UV locations, one for each sample point.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_SamplingSphere Class](T_Grasshopper_GUI_GH_SamplingSphere.htm)

[SampleSphere Overload](Overload_Grasshopper_GUI_GH_SamplingSphere_SampleSphere.htm)

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)