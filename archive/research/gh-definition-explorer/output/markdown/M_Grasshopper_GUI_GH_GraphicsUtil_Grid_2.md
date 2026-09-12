# M_Grasshopper_GUI_GH_GraphicsUtil_Grid_2

﻿ GH\_GraphicsUtil.Grid Method (Graphics, RectangleF, Int32, Int32, Color, Color)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH\_GraphicsUtil Class](../html/T_Grasshopper_GUI_GH_GraphicsUtil.htm "GH_GraphicsUtil Class")

[GH\_GraphicsUtil Methods](../html/Methods_T_Grasshopper_GUI_GH_GraphicsUtil.htm "GH_GraphicsUtil Methods")

[Grid Method](../html/Overload_Grasshopper_GUI_GH_GraphicsUtil_Grid.htm "Grid Method ")

[Grid Method (Graphics, RectangleF, Int32)](../html/M_Grasshopper_GUI_GH_GraphicsUtil_Grid.htm "Grid Method (Graphics, RectangleF, Int32)")

[Grid Method (Graphics, RectangleF, Int32, Int32)](../html/M_Grasshopper_GUI_GH_GraphicsUtil_Grid_1.htm "Grid Method (Graphics, RectangleF, Int32, Int32)")

[Grid Method (Graphics, RectangleF, Int32, Int32, Color, Color)](../html/M_Grasshopper_GUI_GH_GraphicsUtil_Grid_2.htm "Grid Method (Graphics, RectangleF, Int32, Int32, Color, Color)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_GraphicsUtilAddLanguageSpecificTextSet("LSTDEF8BEC6\_0?cpp=::|nu=.");Grid Method (Graphics, RectangleF, Int32, Int32, Color, Color) |

Draw a grid.

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static void Grid(
	Graphics g,
	RectangleF rec,
	int densityX,
	int densityY,
	Color colorBg,
	Color colorWire
)
```

```
Public Shared Sub Grid ( 
	g As Graphics,
	rec As RectangleF,
	densityX As Integer,
	densityY As Integer,
	colorBg As Color,
	colorWire As Color
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

g
:   Type: [System.DrawingAddLanguageSpecificTextSet("LSTDEF8BEC6\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Graphics](https://docs.microsoft.com/dotnet/api/system.drawing.graphics)  
    Graphics object to draw with.

rec
:   Type: [System.DrawingAddLanguageSpecificTextSet("LSTDEF8BEC6\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");RectangleF](https://docs.microsoft.com/dotnet/api/system.drawing.rectanglef)  
    Grid rectangle.

densityX
:   Type: [SystemAddLanguageSpecificTextSet("LSTDEF8BEC6\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Density in x direction.

densityY
:   Type: [SystemAddLanguageSpecificTextSet("LSTDEF8BEC6\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Density in y direction.

colorBg
:   Type: [System.DrawingAddLanguageSpecificTextSet("LSTDEF8BEC6\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");Color](https://docs.microsoft.com/dotnet/api/system.drawing.color)  
    Background colour override, the default is 30/255 white.

colorWire
:   Type: [System.DrawingAddLanguageSpecificTextSet("LSTDEF8BEC6\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");Color](https://docs.microsoft.com/dotnet/api/system.drawing.color)  
    Grid line colour override, the default is 40/255 black.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_GraphicsUtil Class](T_Grasshopper_GUI_GH_GraphicsUtil.htm)

[Grid Overload](Overload_Grasshopper_GUI_GH_GraphicsUtil_Grid.htm)

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)