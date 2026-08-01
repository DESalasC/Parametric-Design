# M_Grasshopper_GUI_Canvas_GH_Border_CreateBorders

﻿ GH\_Border.CreateBorders Method (RectangleF, Int32)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI.Canvas](../html/N_Grasshopper_GUI_Canvas.htm "Grasshopper.GUI.Canvas")

[GH\_Border Class](../html/T_Grasshopper_GUI_Canvas_GH_Border.htm "GH_Border Class")

[GH\_Border Methods](../html/Methods_T_Grasshopper_GUI_Canvas_GH_Border.htm "GH_Border Methods")

[CreateBorders Method](../html/Overload_Grasshopper_GUI_Canvas_GH_Border_CreateBorders.htm "CreateBorders Method ")

[CreateBorders Method (RectangleF, Int32)](../html/M_Grasshopper_GUI_Canvas_GH_Border_CreateBorders.htm "CreateBorders Method (RectangleF, Int32)")

[CreateBorders Method (RectangleF, Padding)](../html/M_Grasshopper_GUI_Canvas_GH_Border_CreateBorders_3.htm "CreateBorders Method (RectangleF, Padding)")

[CreateBorders Method (RectangleF, Int32, Int32)](../html/M_Grasshopper_GUI_Canvas_GH_Border_CreateBorders_1.htm "CreateBorders Method (RectangleF, Int32, Int32)")

[CreateBorders Method (RectangleF, Int32, Int32, Int32, Int32)](../html/M_Grasshopper_GUI_Canvas_GH_Border_CreateBorders_2.htm "CreateBorders Method (RectangleF, Int32, Int32, Int32, Int32)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_BorderAddLanguageSpecificTextSet("LST3CEB64C8\_0?cpp=::|nu=.");CreateBorders Method (RectangleF, Int32) |

Static (Shared) method for creating a set of borders.

**Namespace:**
 [Grasshopper.GUI.Canvas](N_Grasshopper_GUI_Canvas.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static List<GH_Border> CreateBorders(
	RectangleF box,
	int borderSize
)
```

```
Public Shared Function CreateBorders ( 
	box As RectangleF,
	borderSize As Integer
) As List(Of GH_Border)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

box
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST3CEB64C8\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");RectangleF](https://docs.microsoft.com/dotnet/api/system.drawing.rectanglef)  
    Box for border creation.

borderSize
:   Type: [SystemAddLanguageSpecificTextSet("LST3CEB64C8\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    The width of all borders.

#### Return Value

Type: [List](https://docs.microsoft.com/dotnet/api/system.collections.generic.list-1)AddLanguageSpecificTextSet("LST3CEB64C8\_3?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");[GH\_Border](T_Grasshopper_GUI_Canvas_GH_Border.htm)AddLanguageSpecificTextSet("LST3CEB64C8\_4?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
A list of borders.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Border Class](T_Grasshopper_GUI_Canvas_GH_Border.htm)

[CreateBorders Overload](Overload_Grasshopper_GUI_Canvas_GH_Border_CreateBorders.htm)

[Grasshopper.GUI.Canvas Namespace](N_Grasshopper_GUI_Canvas.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)