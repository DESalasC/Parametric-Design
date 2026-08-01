# M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_RenderIcon

﻿ GH\_CapsuleRenderEngine.RenderIcon Method (Graphics, Image, RectangleF, Int32, Int32)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI.Canvas](../html/N_Grasshopper_GUI_Canvas.htm "Grasshopper.GUI.Canvas")

[GH\_CapsuleRenderEngine Class](../html/T_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine.htm "GH_CapsuleRenderEngine Class")

[GH\_CapsuleRenderEngine Methods](../html/Methods_T_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine.htm "GH_CapsuleRenderEngine Methods")

[RenderIcon Method](../html/Overload_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_RenderIcon.htm "RenderIcon Method ")

[RenderIcon Method (Graphics, Image, Int32, Int32)](../html/M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_RenderIcon_1.htm "RenderIcon Method (Graphics, Image, Int32, Int32)")

[RenderIcon Method (Graphics, Image, RectangleF, Int32, Int32)](../html/M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_RenderIcon.htm "RenderIcon Method (Graphics, Image, RectangleF, Int32, Int32)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_CapsuleRenderEngineAddLanguageSpecificTextSet("LSTDC3718FB\_0?cpp=::|nu=.");RenderIcon Method (Graphics, Image, RectangleF, Int32, Int32) |

Render an image icon centered into the box. If the content box has been defined the icon
will be centered there, otherwise the outline box will be used.

**Namespace:**
 [Grasshopper.GUI.Canvas](N_Grasshopper_GUI_Canvas.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public void RenderIcon(
	Graphics G,
	Image icon,
	RectangleF box,
	int offsetX = 0,
	int offsetY = 0
)
```

```
Public Sub RenderIcon ( 
	G As Graphics,
	icon As Image,
	box As RectangleF,
	Optional offsetX As Integer = 0,
	Optional offsetY As Integer = 0
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

G
:   Type: [System.DrawingAddLanguageSpecificTextSet("LSTDC3718FB\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Graphics](https://docs.microsoft.com/dotnet/api/system.drawing.graphics)  
    Graphics surface to draw onto.

icon
:   Type: [System.DrawingAddLanguageSpecificTextSet("LSTDC3718FB\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Image](https://docs.microsoft.com/dotnet/api/system.drawing.image)  
    Icon to draw.

box
:   Type: [System.DrawingAddLanguageSpecificTextSet("LSTDC3718FB\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");RectangleF](https://docs.microsoft.com/dotnet/api/system.drawing.rectanglef)  
    Box override.

offsetX (Optional)
:   Type: [SystemAddLanguageSpecificTextSet("LSTDC3718FB\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Additional x-offset (in original pixel units).

offsetY (Optional)
:   Type: [SystemAddLanguageSpecificTextSet("LSTDC3718FB\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Additional y-offset (in original pixel units).

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_CapsuleRenderEngine Class](T_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine.htm)

[RenderIcon Overload](Overload_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_RenderIcon.htm)

[Grasshopper.GUI.Canvas Namespace](N_Grasshopper_GUI_Canvas.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)