# M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_GetImpliedPalette

﻿ GH\_CapsuleRenderEngine.GetImpliedPalette Method 

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
| GH\_CapsuleRenderEngineAddLanguageSpecificTextSet("LST93BD62F7\_0?cpp=::|nu=.");GetImpliedPalette Method |

Static (Shared in VB) method for solving which palette is the default given a specific object's properties.
Default palettes are either GH\_Palette.Normal, GH\_Palette.Warning or GH\_Palette.Error depending on the objects' runtime message level.

**Namespace:**
 [Grasshopper.GUI.Canvas](N_Grasshopper_GUI_Canvas.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static GH_Palette GetImpliedPalette(
	IGH_ActiveObject obj
)
```

```
Public Shared Function GetImpliedPalette ( 
	obj As IGH_ActiveObject
) As GH_Palette
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

obj
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LST93BD62F7\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");IGH\_ActiveObject](T_Grasshopper_Kernel_IGH_ActiveObject.htm)  
    Object to evaluate.

#### Return Value

Type: [GH\_Palette](T_Grasshopper_GUI_Canvas_GH_Palette.htm)  
The default palette.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_CapsuleRenderEngine Class](T_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine.htm)

[Grasshopper.GUI.Canvas Namespace](N_Grasshopper_GUI_Canvas.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)