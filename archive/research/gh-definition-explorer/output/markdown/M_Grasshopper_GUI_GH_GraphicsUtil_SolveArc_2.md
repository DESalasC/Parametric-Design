# M_Grasshopper_GUI_GH_GraphicsUtil_SolveArc_2

﻿ GH\_GraphicsUtil.SolveArc Method (PointF, PointF, SizeF, RectangleF, Single, Single)

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
| GH\_GraphicsUtilAddLanguageSpecificTextSet("LST9AFC24F6\_0?cpp=::|nu=.");SolveArc Method (PointF, PointF, SizeF, RectangleFAddLanguageSpecificTextSet("LST9AFC24F6\_1?cpp=%");, SingleAddLanguageSpecificTextSet("LST9AFC24F6\_2?cpp=%");, SingleAddLanguageSpecificTextSet("LST9AFC24F6\_3?cpp=%");) |

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
	PointF p0,
	PointF p1,
	SizeF dir,
	ref RectangleF box,
	ref float angle,
	ref float sweep
)
```

```
Public Shared Function SolveArc ( 
	p0 As PointF,
	p1 As PointF,
	dir As SizeF,
	ByRef box As RectangleF,
	ByRef angle As Single,
	ByRef sweep As Single
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

p0
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST9AFC24F6\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");PointF](https://docs.microsoft.com/dotnet/api/system.drawing.pointf)  
    Start point of arc.

p1
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST9AFC24F6\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");PointF](https://docs.microsoft.com/dotnet/api/system.drawing.pointf)  
    End point of arc.

dir
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST9AFC24F6\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");SizeF](https://docs.microsoft.com/dotnet/api/system.drawing.sizef)  
    Tangent direction at start of arc.

box
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST9AFC24F6\_7?cs=.|vb=.|cpp=::|nu=.|fs=.");RectangleF](https://docs.microsoft.com/dotnet/api/system.drawing.rectanglef)AddLanguageSpecificTextSet("LST9AFC24F6\_8?cpp=%");  
    Bounding box of arc (out)

angle
:   Type: [SystemAddLanguageSpecificTextSet("LST9AFC24F6\_9?cs=.|vb=.|cpp=::|nu=.|fs=.");Single](https://docs.microsoft.com/dotnet/api/system.single)AddLanguageSpecificTextSet("LST9AFC24F6\_10?cpp=%");  
    Start angle of arc (out)

sweep
:   Type: [SystemAddLanguageSpecificTextSet("LST9AFC24F6\_11?cs=.|vb=.|cpp=::|nu=.|fs=.");Single](https://docs.microsoft.com/dotnet/api/system.single)AddLanguageSpecificTextSet("LST9AFC24F6\_12?cpp=%");  
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