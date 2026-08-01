# M_Grasshopper_GUI_GH_GraphicsUtil_RenderHighlightBox_2

﻿ GH\_GraphicsUtil.RenderHighlightBox Method (Graphics, Rectangle, Int32, Color, Color)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH\_GraphicsUtil Class](../html/T_Grasshopper_GUI_GH_GraphicsUtil.htm "GH_GraphicsUtil Class")

[GH\_GraphicsUtil Methods](../html/Methods_T_Grasshopper_GUI_GH_GraphicsUtil.htm "GH_GraphicsUtil Methods")

[RenderHighlightBox Method](../html/Overload_Grasshopper_GUI_GH_GraphicsUtil_RenderHighlightBox.htm "RenderHighlightBox Method ")

[RenderHighlightBox Method (Graphics, Rectangle, Int32)](../html/M_Grasshopper_GUI_GH_GraphicsUtil_RenderHighlightBox.htm "RenderHighlightBox Method (Graphics, Rectangle, Int32)")

[RenderHighlightBox Method (Graphics, Rectangle, Int32, Boolean, Boolean)](../html/M_Grasshopper_GUI_GH_GraphicsUtil_RenderHighlightBox_1.htm "RenderHighlightBox Method (Graphics, Rectangle, Int32, Boolean, Boolean)")

[RenderHighlightBox Method (Graphics, Rectangle, Int32, Color, Color)](../html/M_Grasshopper_GUI_GH_GraphicsUtil_RenderHighlightBox_2.htm "RenderHighlightBox Method (Graphics, Rectangle, Int32, Color, Color)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_GraphicsUtilAddLanguageSpecificTextSet("LST3DF4BD59\_0?cpp=::|nu=.");RenderHighlightBox Method (Graphics, Rectangle, Int32, Color, Color) |

Render a typical blueish highlight rectangle

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static void RenderHighlightBox(
	Graphics g,
	Rectangle box,
	int cornerRadius,
	Color fill,
	Color edge
)
```

```
Public Shared Sub RenderHighlightBox ( 
	g As Graphics,
	box As Rectangle,
	cornerRadius As Integer,
	fill As Color,
	edge As Color
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

g
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST3DF4BD59\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Graphics](https://docs.microsoft.com/dotnet/api/system.drawing.graphics)  
    Graphics object to render with.

box
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST3DF4BD59\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Rectangle](https://docs.microsoft.com/dotnet/api/system.drawing.rectangle)  
    Dimensions of selection box.

cornerRadius
:   Type: [SystemAddLanguageSpecificTextSet("LST3DF4BD59\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Radius (in pixels) of box corners, use zero or less to render crisp rectangles.

fill
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST3DF4BD59\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");Color](https://docs.microsoft.com/dotnet/api/system.drawing.color)  
    Fill colour

edge
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST3DF4BD59\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");Color](https://docs.microsoft.com/dotnet/api/system.drawing.color)  
    Edge colour

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_GraphicsUtil Class](T_Grasshopper_GUI_GH_GraphicsUtil.htm)

[RenderHighlightBox Overload](Overload_Grasshopper_GUI_GH_GraphicsUtil_RenderHighlightBox.htm)

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)