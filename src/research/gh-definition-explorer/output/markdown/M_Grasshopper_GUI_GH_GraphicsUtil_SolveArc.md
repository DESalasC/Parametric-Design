# M_Grasshopper_GUI_GH_GraphicsUtil_SolveArc

﻿ GH\_GraphicsUtil.SolveArc Method (Point3d, Point3d, Vector3d, RectangleF, Single, Single)

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
| GH\_GraphicsUtilAddLanguageSpecificTextSet("LSTF0367DBA\_0?cpp=::|nu=.");SolveArc Method (Point3d, Point3d, Vector3d, RectangleFAddLanguageSpecificTextSet("LSTF0367DBA\_1?cpp=%");, SingleAddLanguageSpecificTextSet("LSTF0367DBA\_2?cpp=%");, SingleAddLanguageSpecificTextSet("LSTF0367DBA\_3?cpp=%");) |

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
	Point3d p0,
	Point3d p1,
	Vector3d dir,
	ref RectangleF box,
	ref float angle,
	ref float sweep
)
```

```
Public Shared Function SolveArc ( 
	p0 As Point3d,
	p1 As Point3d,
	dir As Vector3d,
	ByRef box As RectangleF,
	ByRef angle As Single,
	ByRef sweep As Single
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

p0
:   Type: Point3d  
    Start point of arc.

p1
:   Type: Point3d  
    End point of arc.

dir
:   Type: Vector3d  
    Tangent direction at start of arc.

box
:   Type: [System.DrawingAddLanguageSpecificTextSet("LSTF0367DBA\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");RectangleF](https://docs.microsoft.com/dotnet/api/system.drawing.rectanglef)AddLanguageSpecificTextSet("LSTF0367DBA\_5?cpp=%");  
    Bounding box of arc (out)

angle
:   Type: [SystemAddLanguageSpecificTextSet("LSTF0367DBA\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");Single](https://docs.microsoft.com/dotnet/api/system.single)AddLanguageSpecificTextSet("LSTF0367DBA\_7?cpp=%");  
    Start angle of arc (out)

sweep
:   Type: [SystemAddLanguageSpecificTextSet("LSTF0367DBA\_8?cs=.|vb=.|cpp=::|nu=.|fs=.");Single](https://docs.microsoft.com/dotnet/api/system.single)AddLanguageSpecificTextSet("LSTF0367DBA\_9?cpp=%");  
    Sweep angle of arc (out)

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True on success, false on failure.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_GraphicsUtil Class](T_Grasshopper_GUI_GH_GraphicsUtil.htm)

[SolveArc Overload](Overload_Grasshopper_GUI_GH_GraphicsUtil_SolveArc.htm)

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)