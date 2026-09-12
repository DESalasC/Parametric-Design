# M_Grasshopper_GUI_GH_GeometricFont_DrawPath

﻿ GH\_GeometricFont.DrawPath Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH\_GeometricFont Class](../html/T_Grasshopper_GUI_GH_GeometricFont.htm "GH_GeometricFont Class")

[GH\_GeometricFont Methods](../html/Methods_T_Grasshopper_GUI_GH_GeometricFont.htm "GH_GeometricFont Methods")

[Draw0 Method](../html/M_Grasshopper_GUI_GH_GeometricFont_Draw0.htm "Draw0 Method ")

[Draw1 Method](../html/M_Grasshopper_GUI_GH_GeometricFont_Draw1.htm "Draw1 Method ")

[Draw2 Method](../html/M_Grasshopper_GUI_GH_GeometricFont_Draw2.htm "Draw2 Method ")

[Draw3 Method](../html/M_Grasshopper_GUI_GH_GeometricFont_Draw3.htm "Draw3 Method ")

[Draw4 Method](../html/M_Grasshopper_GUI_GH_GeometricFont_Draw4.htm "Draw4 Method ")

[Draw5 Method](../html/M_Grasshopper_GUI_GH_GeometricFont_Draw5.htm "Draw5 Method ")

[Draw6 Method](../html/M_Grasshopper_GUI_GH_GeometricFont_Draw6.htm "Draw6 Method ")

[Draw7 Method](../html/M_Grasshopper_GUI_GH_GeometricFont_Draw7.htm "Draw7 Method ")

[Draw8 Method](../html/M_Grasshopper_GUI_GH_GeometricFont_Draw8.htm "Draw8 Method ")

[Draw9 Method](../html/M_Grasshopper_GUI_GH_GeometricFont_Draw9.htm "Draw9 Method ")

[DrawBracketClose Method](../html/M_Grasshopper_GUI_GH_GeometricFont_DrawBracketClose.htm "DrawBracketClose Method ")

[DrawBracketOpen Method](../html/M_Grasshopper_GUI_GH_GeometricFont_DrawBracketOpen.htm "DrawBracketOpen Method ")

[DrawDash Method](../html/M_Grasshopper_GUI_GH_GeometricFont_DrawDash.htm "DrawDash Method ")

[DrawNumber Method](../html/Overload_Grasshopper_GUI_GH_GeometricFont_DrawNumber.htm "DrawNumber Method ")

[DrawPath Method](../html/M_Grasshopper_GUI_GH_GeometricFont_DrawPath.htm "DrawPath Method ")

[DrawSemiColon Method](../html/M_Grasshopper_GUI_GH_GeometricFont_DrawSemiColon.htm "DrawSemiColon Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_GeometricFontAddLanguageSpecificTextSet("LSTF008E6EE\_0?cpp=::|nu=.");DrawPath Method |

Draw an entire path string at a specific location.

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static void DrawPath(
	Graphics graphics,
	GH_Path path,
	Color colour,
	PointF position
)
```

```
Public Shared Sub DrawPath ( 
	graphics As Graphics,
	path As GH_Path,
	colour As Color,
	position As PointF
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

graphics
:   Type: [System.DrawingAddLanguageSpecificTextSet("LSTF008E6EE\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Graphics](https://docs.microsoft.com/dotnet/api/system.drawing.graphics)  
    Graphics object to draw with.

path
:   Type: [Grasshopper.Kernel.DataAddLanguageSpecificTextSet("LSTF008E6EE\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Path](T_Grasshopper_Kernel_Data_GH_Path.htm)  
    Path to draw.

colour
:   Type: [System.DrawingAddLanguageSpecificTextSet("LSTF008E6EE\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Color](https://docs.microsoft.com/dotnet/api/system.drawing.color)  
    Colour of path.

position
:   Type: [System.DrawingAddLanguageSpecificTextSet("LSTF008E6EE\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");PointF](https://docs.microsoft.com/dotnet/api/system.drawing.pointf)  
    Location of opening bracket.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_GeometricFont Class](T_Grasshopper_GUI_GH_GeometricFont.htm)

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)