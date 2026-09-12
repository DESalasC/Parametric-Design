# M_Grasshopper_GUI_GH_GraphicsUtil_AppendArc

﻿ GH\_GraphicsUtil.AppendArc Method (Point3d, Point3d, Vector3d, GraphicsPath)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH\_GraphicsUtil Class](../html/T_Grasshopper_GUI_GH_GraphicsUtil.htm "GH_GraphicsUtil Class")

[GH\_GraphicsUtil Methods](../html/Methods_T_Grasshopper_GUI_GH_GraphicsUtil.htm "GH_GraphicsUtil Methods")

[AppendArc Method](../html/Overload_Grasshopper_GUI_GH_GraphicsUtil_AppendArc.htm "AppendArc Method ")

[AppendArc Method (Point3d, Point3d, Vector3d, GraphicsPath)](../html/M_Grasshopper_GUI_GH_GraphicsUtil_AppendArc.htm "AppendArc Method (Point3d, Point3d, Vector3d, GraphicsPath)")

[AppendArc Method (PointF, PointF, SizeF, GraphicsPath)](../html/M_Grasshopper_GUI_GH_GraphicsUtil_AppendArc_1.htm "AppendArc Method (PointF, PointF, SizeF, GraphicsPath)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_GraphicsUtilAddLanguageSpecificTextSet("LSTE7FC5409\_0?cpp=::|nu=.");AppendArc Method (Point3d, Point3d, Vector3d, GraphicsPath) |

Append an arc segment to a GraphicsPath. If the arc cannot be solved,
a linear segment is appended instead.

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static void AppendArc(
	Point3d p0,
	Point3d p1,
	Vector3d dir,
	GraphicsPath path
)
```

```
Public Shared Sub AppendArc ( 
	p0 As Point3d,
	p1 As Point3d,
	dir As Vector3d,
	path As GraphicsPath
)
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

path
:   Type: [System.Drawing.Drawing2DAddLanguageSpecificTextSet("LSTE7FC5409\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GraphicsPath](https://docs.microsoft.com/dotnet/api/system.drawing.drawing2d.graphicspath)  
    Path to append to.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_GraphicsUtil Class](T_Grasshopper_GUI_GH_GraphicsUtil.htm)

[AppendArc Overload](Overload_Grasshopper_GUI_GH_GraphicsUtil_AppendArc.htm)

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)