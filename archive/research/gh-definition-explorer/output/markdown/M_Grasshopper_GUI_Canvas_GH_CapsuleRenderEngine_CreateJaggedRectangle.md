# M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_CreateJaggedRectangle

﻿ GH\_CapsuleRenderEngine.CreateJaggedRectangle Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI.Canvas](../html/N_Grasshopper_GUI_Canvas.htm "Grasshopper.GUI.Canvas")

[GH\_CapsuleRenderEngine Class](../html/T_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine.htm "GH_CapsuleRenderEngine Class")

[GH\_CapsuleRenderEngine Methods](../html/Methods_T_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine.htm "GH_CapsuleRenderEngine Methods")

[CreateHighlightBar Method](../html/Overload_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_CreateHighlightBar.htm "CreateHighlightBar Method ")

[CreateJaggedRectangle Method](../html/M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_CreateJaggedRectangle.htm "CreateJaggedRectangle Method ")

[CreateRoundedRectangle Method](../html/Overload_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_CreateRoundedRectangle.htm "CreateRoundedRectangle Method ")

[GetImpliedPalette Method](../html/M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_GetImpliedPalette.htm "GetImpliedPalette Method ")

[GetImpliedStyle Method](../html/Overload_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_GetImpliedStyle.htm "GetImpliedStyle Method ")

[RenderAlphaFill Method](../html/M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_RenderAlphaFill.htm "RenderAlphaFill Method ")

[RenderBackground Method](../html/M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_RenderBackground.htm "RenderBackground Method ")

[RenderBackground\_Alternative Method](../html/M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_RenderBackground_Alternative.htm "RenderBackground_Alternative Method ")

[RenderBoundaryDots Method](../html/M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_RenderBoundaryDots.htm "RenderBoundaryDots Method ")

[RenderGrips Method](../html/M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_RenderGrips.htm "RenderGrips Method ")

[RenderGrips\_Alternative Method](../html/M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_RenderGrips_Alternative.htm "RenderGrips_Alternative Method ")

[RenderHighlight Method](../html/M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_RenderHighlight.htm "RenderHighlight Method ")

[RenderIcon Method](../html/Overload_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_RenderIcon.htm "RenderIcon Method ")

[RenderInputGrip Method](../html/M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_RenderInputGrip.htm "RenderInputGrip Method ")

[RenderMessage Method](../html/M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_RenderMessage.htm "RenderMessage Method ")

[RenderOutlines Method](../html/M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_RenderOutlines.htm "RenderOutlines Method ")

[RenderOutputGrip Method](../html/M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_RenderOutputGrip.htm "RenderOutputGrip Method ")

[RenderText Method](../html/M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_RenderText.htm "RenderText Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_CapsuleRenderEngineAddLanguageSpecificTextSet("LST33658166\_0?cpp=::|nu=.");CreateJaggedRectangle Method |

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
public static GraphicsPath CreateJaggedRectangle(
	RectangleF rec,
	float R0,
	float R1,
	float R2,
	float R3,
	bool jaggedLeft,
	bool jaggedRight
)
```

```
Public Shared Function CreateJaggedRectangle ( 
	rec As RectangleF,
	R0 As Single,
	R1 As Single,
	R2 As Single,
	R3 As Single,
	jaggedLeft As Boolean,
	jaggedRight As Boolean
) As GraphicsPath
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

rec
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST33658166\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");RectangleF](https://docs.microsoft.com/dotnet/api/system.drawing.rectanglef)  
    Rectangle to fillet. Rectangles smaller than 3 pixels wide/high will be grown.

R0
:   Type: [SystemAddLanguageSpecificTextSet("LST33658166\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Single](https://docs.microsoft.com/dotnet/api/system.single)  
    Radius of upper left corner. Zero or negative values omit fillets.

R1
:   Type: [SystemAddLanguageSpecificTextSet("LST33658166\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Single](https://docs.microsoft.com/dotnet/api/system.single)  
    Radius of upper right corner. Zero or negative values omit fillets.

R2
:   Type: [SystemAddLanguageSpecificTextSet("LST33658166\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");Single](https://docs.microsoft.com/dotnet/api/system.single)  
    Radius of lower right corner. Zero or negative values omit fillets.

R3
:   Type: [SystemAddLanguageSpecificTextSet("LST33658166\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");Single](https://docs.microsoft.com/dotnet/api/system.single)  
    Radius of lower left corner. Zero or negative values omit fillets.

jaggedLeft
:   Type: [SystemAddLanguageSpecificTextSet("LST33658166\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
    If true, the left edge of the rectangle will be jagged and R0 and R3 will be ignored.

jaggedRight
:   Type: [SystemAddLanguageSpecificTextSet("LST33658166\_7?cs=.|vb=.|cpp=::|nu=.|fs=.");Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
    If true, the right edge of the rectangle will be jagged and R1 and R2 will be ignored.

#### Return Value

Type: [GraphicsPath](https://docs.microsoft.com/dotnet/api/system.drawing.drawing2d.graphicspath)  
Graphics path that describes the rounded rectangle.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_CapsuleRenderEngine Class](T_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine.htm)

[Grasshopper.GUI.Canvas Namespace](N_Grasshopper_GUI_Canvas.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)