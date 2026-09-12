# M_Grasshopper_GUI_Gradient_GH_Gradient_NearestGrip_2

﻿ GH\_Gradient.NearestGrip Method (RectangleF, PointF, Double)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI.Gradient](../html/N_Grasshopper_GUI_Gradient.htm "Grasshopper.GUI.Gradient")

[GH\_Gradient Class](../html/T_Grasshopper_GUI_Gradient_GH_Gradient.htm "GH_Gradient Class")

[GH\_Gradient Methods](../html/Methods_T_Grasshopper_GUI_Gradient_GH_Gradient.htm "GH_Gradient Methods")

[NearestGrip Method](../html/Overload_Grasshopper_GUI_Gradient_GH_Gradient_NearestGrip.htm "NearestGrip Method ")

[NearestGrip Method (Double)](../html/M_Grasshopper_GUI_Gradient_GH_Gradient_NearestGrip.htm "NearestGrip Method (Double)")

[NearestGrip Method (Double, GH\_GripSide)](../html/M_Grasshopper_GUI_Gradient_GH_Gradient_NearestGrip_1.htm "NearestGrip Method (Double, GH_GripSide)")

[NearestGrip Method (RectangleF, PointF, Double)](../html/M_Grasshopper_GUI_Gradient_GH_Gradient_NearestGrip_2.htm "NearestGrip Method (RectangleF, PointF, Double)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_GradientAddLanguageSpecificTextSet("LST2B945721\_0?cpp=::|nu=.");NearestGrip Method (RectangleF, PointF, Double) |

Find the nearest grip in screen coordinates.

**Namespace:**
 [Grasshopper.GUI.Gradient](N_Grasshopper_GUI_Gradient.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public int NearestGrip(
	RectangleF dest,
	PointF pt,
	double maxRadius
)
```

```
Public Function NearestGrip ( 
	dest As RectangleF,
	pt As PointF,
	maxRadius As Double
) As Integer
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

dest
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST2B945721\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");RectangleF](https://docs.microsoft.com/dotnet/api/system.drawing.rectanglef)  
    Retangle that contains the entire gradient.

pt
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST2B945721\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");PointF](https://docs.microsoft.com/dotnet/api/system.drawing.pointf)  
    Point to search from.

maxRadius
:   Type: [SystemAddLanguageSpecificTextSet("LST2B945721\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Double](https://docs.microsoft.com/dotnet/api/system.double)  
    Maximum distance between point and grip.

#### Return Value

Type: [Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
The grip closest to the point.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Gradient Class](T_Grasshopper_GUI_Gradient_GH_Gradient.htm)

[NearestGrip Overload](Overload_Grasshopper_GUI_Gradient_GH_Gradient_NearestGrip.htm)

[Grasshopper.GUI.Gradient Namespace](N_Grasshopper_GUI_Gradient.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)