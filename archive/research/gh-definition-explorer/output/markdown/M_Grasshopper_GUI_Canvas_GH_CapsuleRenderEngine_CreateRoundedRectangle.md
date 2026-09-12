# M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_CreateRoundedRectangle

﻿ GH\_CapsuleRenderEngine.CreateRoundedRectangle Method (Rectangle, Int32)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI.Canvas](../html/N_Grasshopper_GUI_Canvas.htm "Grasshopper.GUI.Canvas")

[GH\_CapsuleRenderEngine Class](../html/T_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine.htm "GH_CapsuleRenderEngine Class")

[GH\_CapsuleRenderEngine Methods](../html/Methods_T_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine.htm "GH_CapsuleRenderEngine Methods")

[CreateRoundedRectangle Method](../html/Overload_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_CreateRoundedRectangle.htm "CreateRoundedRectangle Method ")

[CreateRoundedRectangle Method (Rectangle, Int32)](../html/M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_CreateRoundedRectangle.htm "CreateRoundedRectangle Method (Rectangle, Int32)")

[CreateRoundedRectangle Method (RectangleF, Single)](../html/M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_CreateRoundedRectangle_2.htm "CreateRoundedRectangle Method (RectangleF, Single)")

[CreateRoundedRectangle Method (Rectangle, Int32, Int32, Int32, Int32)](../html/M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_CreateRoundedRectangle_1.htm "CreateRoundedRectangle Method (Rectangle, Int32, Int32, Int32, Int32)")

[CreateRoundedRectangle Method (RectangleF, Single, Single, Single, Single)](../html/M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_CreateRoundedRectangle_3.htm "CreateRoundedRectangle Method (RectangleF, Single, Single, Single, Single)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_CapsuleRenderEngineAddLanguageSpecificTextSet("LSTFE62847B\_0?cpp=::|nu=.");CreateRoundedRectangle Method (Rectangle, Int32) |

Static (Shared in VB) method for creating rectangles with rounded corners.

**Namespace:**
 [Grasshopper.GUI.Canvas](N_Grasshopper_GUI_Canvas.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static GraphicsPath CreateRoundedRectangle(
	Rectangle rec,
	int radius
)
```

```
Public Shared Function CreateRoundedRectangle ( 
	rec As Rectangle,
	radius As Integer
) As GraphicsPath
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

rec
:   Type: [System.DrawingAddLanguageSpecificTextSet("LSTFE62847B\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Rectangle](https://docs.microsoft.com/dotnet/api/system.drawing.rectangle)  
    Rectangle to fillet. Rectangles smaller than 3 pixels wide/high will be grown.

radius
:   Type: [SystemAddLanguageSpecificTextSet("LSTFE62847B\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Radius of corner fillets.

#### Return Value

Type: [GraphicsPath](https://docs.microsoft.com/dotnet/api/system.drawing.drawing2d.graphicspath)  
Graphics path that describes the rounded rectangle.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_CapsuleRenderEngine Class](T_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine.htm)

[CreateRoundedRectangle Overload](Overload_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_CreateRoundedRectangle.htm)

[Grasshopper.GUI.Canvas Namespace](N_Grasshopper_GUI_Canvas.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)