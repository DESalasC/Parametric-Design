# M_Grasshopper_GUI_GH_GDI_Util_FilletPolyline

﻿ GH\_GDI\_Util.FilletPolyline Method (Point[], Int32)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH\_GDI\_Util Class](../html/T_Grasshopper_GUI_GH_GDI_Util.htm "GH_GDI_Util Class")

[GH\_GDI\_Util Methods](../html/Methods_T_Grasshopper_GUI_GH_GDI_Util.htm "GH_GDI_Util Methods")

[FilletPolyline Method](../html/Overload_Grasshopper_GUI_GH_GDI_Util_FilletPolyline.htm "FilletPolyline Method ")

[FilletPolyline Method (Point[], Int32)](../html/M_Grasshopper_GUI_GH_GDI_Util_FilletPolyline.htm "FilletPolyline Method (Point[], Int32)")

[FilletPolyline Method (PointF[], Single)](../html/M_Grasshopper_GUI_GH_GDI_Util_FilletPolyline_1.htm "FilletPolyline Method (PointF[], Single)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_GDI\_UtilAddLanguageSpecificTextSet("LSTA2C34D6F\_0?cpp=::|nu=.");FilletPolyline Method (AddLanguageSpecificTextSet("LSTA2C34D6F\_1?cpp=array&lt;");PointAddLanguageSpecificTextSet("LSTA2C34D6F\_2?cpp=&gt;|vb=()|nu=[]");, Int32) |

Fillet all the corners of a freeform outline.

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static GraphicsPath FilletPolyline(
	Point[] corners,
	int radius
)
```

```
Public Shared Function FilletPolyline ( 
	corners As Point(),
	radius As Integer
) As GraphicsPath
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

corners
:   Type: AddLanguageSpecificTextSet("LSTA2C34D6F\_3?cpp=array&lt;");[System.DrawingAddLanguageSpecificTextSet("LSTA2C34D6F\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");Point](https://docs.microsoft.com/dotnet/api/system.drawing.point)AddLanguageSpecificTextSet("LSTA2C34D6F\_5?cpp=&gt;|vb=()|nu=[]");  
    A list of corner points.

radius
:   Type: [SystemAddLanguageSpecificTextSet("LSTA2C34D6F\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Fillet to apply to all corners.

#### Return Value

Type: [GraphicsPath](https://docs.microsoft.com/dotnet/api/system.drawing.drawing2d.graphicspath)  
A graphics path describing the filleted shape, or Nothing on failure.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_GDI\_Util Class](T_Grasshopper_GUI_GH_GDI_Util.htm)

[FilletPolyline Overload](Overload_Grasshopper_GUI_GH_GDI_Util_FilletPolyline.htm)

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)