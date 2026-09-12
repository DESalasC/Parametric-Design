# M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_CreateHighlightBar_2

﻿ GH\_CapsuleRenderEngine.CreateHighlightBar Method (Rectangle, Int32, Int32, Int32)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI.Canvas](../html/N_Grasshopper_GUI_Canvas.htm "Grasshopper.GUI.Canvas")

[GH\_CapsuleRenderEngine Class](../html/T_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine.htm "GH_CapsuleRenderEngine Class")

[GH\_CapsuleRenderEngine Methods](../html/Methods_T_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine.htm "GH_CapsuleRenderEngine Methods")

[CreateHighlightBar Method](../html/Overload_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_CreateHighlightBar.htm "CreateHighlightBar Method ")

[CreateHighlightBar Method (Rectangle, Int32, Int32)](../html/M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_CreateHighlightBar.htm "CreateHighlightBar Method (Rectangle, Int32, Int32)")

[CreateHighlightBar Method (Rectangle, Int32, Int32, Int32)](../html/M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_CreateHighlightBar_2.htm "CreateHighlightBar Method (Rectangle, Int32, Int32, Int32)")

[CreateHighlightBar Method (Rectangle, Int32, Int32, Boolean, Boolean)](../html/M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_CreateHighlightBar_1.htm "CreateHighlightBar Method (Rectangle, Int32, Int32, Boolean, Boolean)")

[CreateHighlightBar Method (Rectangle, Int32, Int32, Int32, Boolean, Boolean)](../html/M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_CreateHighlightBar_3.htm "CreateHighlightBar Method (Rectangle, Int32, Int32, Int32, Boolean, Boolean)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_CapsuleRenderEngineAddLanguageSpecificTextSet("LST31011839\_0?cpp=::|nu=.");CreateHighlightBar Method (Rectangle, Int32, Int32, Int32) |

Static (Shared in VB) method for creating Grasshopper Capsule highlight fills.

**Namespace:**
 [Grasshopper.GUI.Canvas](N_Grasshopper_GUI_Canvas.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static GraphicsPath CreateHighlightBar(
	Rectangle rec,
	int R0,
	int R1,
	int size
)
```

```
Public Shared Function CreateHighlightBar ( 
	rec As Rectangle,
	R0 As Integer,
	R1 As Integer,
	size As Integer
) As GraphicsPath
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

rec
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST31011839\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Rectangle](https://docs.microsoft.com/dotnet/api/system.drawing.rectangle)  
    Rectangle for entire fill.

R0
:   Type: [SystemAddLanguageSpecificTextSet("LST31011839\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Radius of upper left corner.

R1
:   Type: [SystemAddLanguageSpecificTextSet("LST31011839\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Radius of upper right corner.

size
:   Type: [SystemAddLanguageSpecificTextSet("LST31011839\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Highlight fill height.

#### Return Value

Type: [GraphicsPath](https://docs.microsoft.com/dotnet/api/system.drawing.drawing2d.graphicspath)  
Graphics path that describes the highlight fill shape.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_CapsuleRenderEngine Class](T_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine.htm)

[CreateHighlightBar Overload](Overload_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_CreateHighlightBar.htm)

[Grasshopper.GUI.Canvas Namespace](N_Grasshopper_GUI_Canvas.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)