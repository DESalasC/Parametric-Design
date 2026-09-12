# M_Grasshopper_GUI_GH_GraphicsUtil_RenderBalloonTag

﻿ GH\_GraphicsUtil.RenderBalloonTag Method (Graphics, String, Font, Color, Color, PointF, Boolean)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH\_GraphicsUtil Class](../html/T_Grasshopper_GUI_GH_GraphicsUtil.htm "GH_GraphicsUtil Class")

[GH\_GraphicsUtil Methods](../html/Methods_T_Grasshopper_GUI_GH_GraphicsUtil.htm "GH_GraphicsUtil Methods")

[RenderBalloonTag Method](../html/Overload_Grasshopper_GUI_GH_GraphicsUtil_RenderBalloonTag.htm "RenderBalloonTag Method ")

[RenderBalloonTag Method (Graphics, String, PointF, RectangleF)](../html/M_Grasshopper_GUI_GH_GraphicsUtil_RenderBalloonTag_3.htm "RenderBalloonTag Method (Graphics, String, PointF, RectangleF)")

[RenderBalloonTag Method (Graphics, String, Font, PointF, RectangleF)](../html/M_Grasshopper_GUI_GH_GraphicsUtil_RenderBalloonTag_2.htm "RenderBalloonTag Method (Graphics, String, Font, PointF, RectangleF)")

[RenderBalloonTag Method (Graphics, String, Font, Color, Color, PointF, Boolean)](../html/M_Grasshopper_GUI_GH_GraphicsUtil_RenderBalloonTag.htm "RenderBalloonTag Method (Graphics, String, Font, Color, Color, PointF, Boolean)")

[RenderBalloonTag Method (Graphics, String, Font, Color, Color, PointF, RectangleF)](../html/M_Grasshopper_GUI_GH_GraphicsUtil_RenderBalloonTag_1.htm "RenderBalloonTag Method (Graphics, String, Font, Color, Color, PointF, RectangleF)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_GraphicsUtilAddLanguageSpecificTextSet("LSTF211E797\_0?cpp=::|nu=.");RenderBalloonTag Method (Graphics, String, Font, Color, Color, PointF, Boolean) |

Draw a balloon tag in a container.

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static void RenderBalloonTag(
	Graphics g,
	string text,
	Font font,
	Color backColor,
	Color foreColor,
	PointF tip,
	bool upright
)
```

```
Public Shared Sub RenderBalloonTag ( 
	g As Graphics,
	text As String,
	font As Font,
	backColor As Color,
	foreColor As Color,
	tip As PointF,
	upright As Boolean
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

g
:   Type: [System.DrawingAddLanguageSpecificTextSet("LSTF211E797\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Graphics](https://docs.microsoft.com/dotnet/api/system.drawing.graphics)  
    Graphics object to draw with.

text
:   Type: [SystemAddLanguageSpecificTextSet("LSTF211E797\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Text of tag.

font
:   Type: [System.DrawingAddLanguageSpecificTextSet("LSTF211E797\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Font](https://docs.microsoft.com/dotnet/api/system.drawing.font)  
    Font of tag.

backColor
:   Type: [System.DrawingAddLanguageSpecificTextSet("LSTF211E797\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");Color](https://docs.microsoft.com/dotnet/api/system.drawing.color)  
    Background colour of balloon.

foreColor
:   Type: [System.DrawingAddLanguageSpecificTextSet("LSTF211E797\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");Color](https://docs.microsoft.com/dotnet/api/system.drawing.color)  
    Foreground colour of balloon edge and text.

tip
:   Type: [System.DrawingAddLanguageSpecificTextSet("LSTF211E797\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");PointF](https://docs.microsoft.com/dotnet/api/system.drawing.pointf)  
    Tip of balloon.

upright
:   Type: [SystemAddLanguageSpecificTextSet("LSTF211E797\_7?cs=.|vb=.|cpp=::|nu=.|fs=.");Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
    If true, the balloon will be above the tip point.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_GraphicsUtil Class](T_Grasshopper_GUI_GH_GraphicsUtil.htm)

[RenderBalloonTag Overload](Overload_Grasshopper_GUI_GH_GraphicsUtil_RenderBalloonTag.htm)

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)