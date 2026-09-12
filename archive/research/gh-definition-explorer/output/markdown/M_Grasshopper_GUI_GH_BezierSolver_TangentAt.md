# M_Grasshopper_GUI_GH_BezierSolver_TangentAt

﻿ GH\_BezierSolver.TangentAt Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH\_BezierSolver Class](../html/T_Grasshopper_GUI_GH_BezierSolver.htm "GH_BezierSolver Class")

[GH\_BezierSolver Methods](../html/Methods_T_Grasshopper_GUI_GH_BezierSolver.htm "GH_BezierSolver Methods")

[AngleAt Method](../html/M_Grasshopper_GUI_GH_BezierSolver_AngleAt.htm "AngleAt Method ")

[PointAt Method](../html/M_Grasshopper_GUI_GH_BezierSolver_PointAt.htm "PointAt Method ")

[TangentAt Method](../html/M_Grasshopper_GUI_GH_BezierSolver_TangentAt.htm "TangentAt Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_BezierSolverAddLanguageSpecificTextSet("LST64060E7A\_0?cpp=::|nu=.");TangentAt Method |

Evaluate the tangent vector of a Bezier span.

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static SizeF TangentAt(
	ref PointF P0,
	ref PointF P1,
	ref PointF P2,
	ref PointF P3,
	float t
)
```

```
Public Shared Function TangentAt ( 
	ByRef P0 As PointF,
	ByRef P1 As PointF,
	ByRef P2 As PointF,
	ByRef P3 As PointF,
	t As Single
) As SizeF
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

P0
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST64060E7A\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");PointF](https://docs.microsoft.com/dotnet/api/system.drawing.pointf)AddLanguageSpecificTextSet("LST64060E7A\_2?cpp=%");  
    Start point of bezier.

P1
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST64060E7A\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");PointF](https://docs.microsoft.com/dotnet/api/system.drawing.pointf)AddLanguageSpecificTextSet("LST64060E7A\_4?cpp=%");  
    Point for start tangent.

P2
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST64060E7A\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");PointF](https://docs.microsoft.com/dotnet/api/system.drawing.pointf)AddLanguageSpecificTextSet("LST64060E7A\_6?cpp=%");  
    Point for end tangent.

P3
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST64060E7A\_7?cs=.|vb=.|cpp=::|nu=.|fs=.");PointF](https://docs.microsoft.com/dotnet/api/system.drawing.pointf)AddLanguageSpecificTextSet("LST64060E7A\_8?cpp=%");  
    End point of bezier.

t
:   Type: [SystemAddLanguageSpecificTextSet("LST64060E7A\_9?cs=.|vb=.|cpp=::|nu=.|fs=.");Single](https://docs.microsoft.com/dotnet/api/system.single)  
    Unit parameter.

#### Return Value

Type: [SizeF](https://docs.microsoft.com/dotnet/api/system.drawing.sizef)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_BezierSolver Class](T_Grasshopper_GUI_GH_BezierSolver.htm)

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)