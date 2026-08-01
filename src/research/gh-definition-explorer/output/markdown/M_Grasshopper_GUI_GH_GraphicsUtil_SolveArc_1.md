# M_Grasshopper_GUI_GH_GraphicsUtil_SolveArc_1

﻿ GH\_GraphicsUtil.SolveArc Method (Double, Double, Double, Double, Double, Double, RectangleF, Single, Single)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH\_GraphicsUtil Class](../html/T_Grasshopper_GUI_GH_GraphicsUtil.htm "GH_GraphicsUtil Class")

[GH\_GraphicsUtil Methods](../html/Methods_T_Grasshopper_GUI_GH_GraphicsUtil.htm "GH_GraphicsUtil Methods")

[SolveArc Method](../html/Overload_Grasshopper_GUI_GH_GraphicsUtil_SolveArc.htm "SolveArc Method ")

[SolveArc Method (Point3d, Point3d, Vector3d, RectangleF, Single, Single)](../html/M_Grasshopper_GUI_GH_GraphicsUtil_SolveArc.htm "SolveArc Method (Point3d, Point3d, Vector3d, RectangleF, Single, Single)")

[SolveArc Method (PointF, PointF, SizeF, RectangleF, Single, Single)](../html/M_Grasshopper_GUI_GH_GraphicsUtil_SolveArc_2.htm "SolveArc Method (PointF, PointF, SizeF, RectangleF, Single, Single)")

[SolveArc Method (Double, Double, Double, Double, Double, Double, RectangleF, Single, Single)](../html/M_Grasshopper_GUI_GH_GraphicsUtil_SolveArc_1.htm "SolveArc Method (Double, Double, Double, Double, Double, Double, RectangleF, Single, Single)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_GraphicsUtilAddLanguageSpecificTextSet("LSTA61CD5BD\_0?cpp=::|nu=.");SolveArc Method (Double, Double, Double, Double, Double, Double, RectangleFAddLanguageSpecificTextSet("LSTA61CD5BD\_1?cpp=%");, SingleAddLanguageSpecificTextSet("LSTA61CD5BD\_2?cpp=%");, SingleAddLanguageSpecificTextSet("LSTA61CD5BD\_3?cpp=%");) |

Create a GDI circular arc definition from start-point, end-point and tangent direction.

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static bool SolveArc(
	double p0X,
	double p0Y,
	double p1X,
	double p1Y,
	double dx,
	double dy,
	ref RectangleF box,
	ref float angle,
	ref float sweep
)
```

```
Public Shared Function SolveArc ( 
	p0X As Double,
	p0Y As Double,
	p1X As Double,
	p1Y As Double,
	dx As Double,
	dy As Double,
	ByRef box As RectangleF,
	ByRef angle As Single,
	ByRef sweep As Single
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

p0X
:   Type: [SystemAddLanguageSpecificTextSet("LSTA61CD5BD\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");Double](https://docs.microsoft.com/dotnet/api/system.double)

p0Y
:   Type: [SystemAddLanguageSpecificTextSet("LSTA61CD5BD\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");Double](https://docs.microsoft.com/dotnet/api/system.double)

p1X
:   Type: [SystemAddLanguageSpecificTextSet("LSTA61CD5BD\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");Double](https://docs.microsoft.com/dotnet/api/system.double)

p1Y
:   Type: [SystemAddLanguageSpecificTextSet("LSTA61CD5BD\_7?cs=.|vb=.|cpp=::|nu=.|fs=.");Double](https://docs.microsoft.com/dotnet/api/system.double)

dx
:   Type: [SystemAddLanguageSpecificTextSet("LSTA61CD5BD\_8?cs=.|vb=.|cpp=::|nu=.|fs=.");Double](https://docs.microsoft.com/dotnet/api/system.double)

dy
:   Type: [SystemAddLanguageSpecificTextSet("LSTA61CD5BD\_9?cs=.|vb=.|cpp=::|nu=.|fs=.");Double](https://docs.microsoft.com/dotnet/api/system.double)

box
:   Type: [System.DrawingAddLanguageSpecificTextSet("LSTA61CD5BD\_10?cs=.|vb=.|cpp=::|nu=.|fs=.");RectangleF](https://docs.microsoft.com/dotnet/api/system.drawing.rectanglef)AddLanguageSpecificTextSet("LSTA61CD5BD\_11?cpp=%");

angle
:   Type: [SystemAddLanguageSpecificTextSet("LSTA61CD5BD\_12?cs=.|vb=.|cpp=::|nu=.|fs=.");Single](https://docs.microsoft.com/dotnet/api/system.single)AddLanguageSpecificTextSet("LSTA61CD5BD\_13?cpp=%");

sweep
:   Type: [SystemAddLanguageSpecificTextSet("LSTA61CD5BD\_14?cs=.|vb=.|cpp=::|nu=.|fs=.");Single](https://docs.microsoft.com/dotnet/api/system.single)AddLanguageSpecificTextSet("LSTA61CD5BD\_15?cpp=%");

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_GraphicsUtil Class](T_Grasshopper_GUI_GH_GraphicsUtil.htm)

[SolveArc Overload](Overload_Grasshopper_GUI_GH_GraphicsUtil_SolveArc.htm)

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)