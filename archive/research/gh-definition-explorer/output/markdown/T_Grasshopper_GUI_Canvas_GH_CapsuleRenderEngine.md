# T_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine

﻿ GH\_CapsuleRenderEngine Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI.Canvas](../html/N_Grasshopper_GUI_Canvas.htm "Grasshopper.GUI.Canvas")

[GH\_CapsuleRenderEngine Class](../html/T_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine.htm "GH_CapsuleRenderEngine Class")

[GH\_CapsuleRenderEngine Methods](../html/Methods_T_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine.htm "GH_CapsuleRenderEngine Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_CapsuleRenderEngine Class |

Provides basic Render methods for capsule display.
You typically don't need this class, just use the Render()
overloads on GH\_Capsule directly.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST3A0C0487\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.GUI.CanvasAddLanguageSpecificTextSet("LST3A0C0487\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_CapsuleRenderEngine

**Namespace:**
 [Grasshopper.GUI.Canvas](N_Grasshopper_GUI_Canvas.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_CapsuleRenderEngine
```

```
Public Class GH_CapsuleRenderEngine
```

AddLanguageTabSet("ID1EBCA");

The GH\_CapsuleRenderEngine type exposes the following members.

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public methodStatic member | [CreateHighlightBar(Rectangle, Int32, Int32)](M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_CreateHighlightBar.htm) | Static (Shared in VB) method for creating Grasshopper Capsule highlight fills. |
| Public methodStatic member | [CreateHighlightBar(Rectangle, Int32, Int32, Int32)](M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_CreateHighlightBar_2.htm) | Static (Shared in VB) method for creating Grasshopper Capsule highlight fills. |
| Public methodStatic member | [CreateHighlightBar(Rectangle, Int32, Int32, Boolean, Boolean)](M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_CreateHighlightBar_1.htm) | Static (Shared in VB) method for creating Grasshopper Capsule highlight fills. |
| Public methodStatic member | [CreateHighlightBar(Rectangle, Int32, Int32, Int32, Boolean, Boolean)](M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_CreateHighlightBar_3.htm) | Static (Shared in VB) method for creating Grasshopper Capsule highlight fills. |
| Public methodStatic member | [CreateJaggedRectangle](M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_CreateJaggedRectangle.htm) | Static (Shared in VB) method for creating rectangles with rounded corners. |
| Public methodStatic member | [CreateRoundedRectangle(Rectangle, Int32)](M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_CreateRoundedRectangle.htm) | Static (Shared in VB) method for creating rectangles with rounded corners. |
| Public methodStatic member | [CreateRoundedRectangle(RectangleF, Single)](M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_CreateRoundedRectangle_2.htm) | Static (Shared in VB) method for creating rectangles with rounded corners. |
| Public methodStatic member | [CreateRoundedRectangle(Rectangle, Int32, Int32, Int32, Int32)](M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_CreateRoundedRectangle_1.htm) | Static (Shared in VB) method for creating rectangles with rounded corners. |
| Public methodStatic member | [CreateRoundedRectangle(RectangleF, Single, Single, Single, Single)](M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_CreateRoundedRectangle_3.htm) | Static (Shared in VB) method for creating rectangles with rounded corners. |
| Public methodStatic member | [GetImpliedPalette](M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_GetImpliedPalette.htm) | Static (Shared in VB) method for solving which palette is the default given a specific object's properties. Default palettes are either GH\_Palette.Normal, GH\_Palette.Warning or GH\_Palette.Error depending on the objects' runtime message level. |
| Public methodStatic member | [GetImpliedStyle(GH\_Palette, IGH\_Attributes)](M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_GetImpliedStyle.htm) | Static (Shared in VB) method for solving which palette style is implied by the properties. |
| Public methodStatic member | [GetImpliedStyle(GH\_Palette, Boolean, Boolean, Boolean)](M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_GetImpliedStyle_1.htm) | Static (Shared in VB) method for solving which palette style is implied by the properties. |
| Public method | [RenderAlphaFill](M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_RenderAlphaFill.htm) | Render a standard transparancy background hatch. This is only needed when the capsule background colour is not fully opaque. This is usually the second stage in a capsule rendering, right after the Grips are drawn. |
| Public method | [RenderBackground](M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_RenderBackground.htm) | Render a default capsule background fill. This is usually the third stage in a capsule rendering. |
| Public method | [RenderBackground\_Alternative](M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_RenderBackground_Alternative.htm) | Render a custom capsule background fill. This is usually the third stage in a capsule rendering. |
| Public method | [RenderBoundaryDots](M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_RenderBoundaryDots.htm) | Render a collection of boundary dots along the top edge of the capsule. |
| Public method | [RenderGrips](M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_RenderGrips.htm) | Render all the grips associates with the capsule. Grips are not drawn if the zoom level is less than 50%. This is usually the first stage in a Capsule rendering. |
| Public method | [RenderGrips\_Alternative](M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_RenderGrips_Alternative.htm) | Render all the grips associates with the capsule as semi-circles. This is needed if the capsule background is not fully opaque. Grips are not drawn if the zoom level is less than 50%. This is usually the first stage in a Capsule rendering. |
| Public method | [RenderHighlight](M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_RenderHighlight.htm) | Render a highlight bar. This is highly zoom-dependant. Highlight rendering is usually the fourth stage in a Capsule Rendering, after the background but prior to the edges. |
| Public method | [RenderIcon(Graphics, Image, Int32, Int32)](M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_RenderIcon_1.htm) | Render an image icon centered into the box. If the content box has been defined the icon will be centered there, otherwise the outline box will be used. |
| Public method | [RenderIcon(Graphics, Image, RectangleF, Int32, Int32)](M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_RenderIcon.htm) | Render an image icon centered into the box. If the content box has been defined the icon will be centered there, otherwise the outline box will be used. |
| Public methodStatic member | [RenderInputGrip](M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_RenderInputGrip.htm) | Static (Shared in VB) method to render a default input grip. |
| Public method | [RenderMessage](M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_RenderMessage.htm) | Render a text message underneath the capsule. |
| Public method | [RenderOutlines](M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_RenderOutlines.htm) | Render default capsule outlines. If the zoom factor is less than 50% the inner outline is not drawn. This is usually the fifth stage in a Capsule rendering. |
| Public methodStatic member | [RenderOutputGrip](M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_RenderOutputGrip.htm) | Static (Shared in VB) method to render a default output grip. |
| Public method | [RenderText](M_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine_RenderText.htm) | Render the capsule text. This is usually the sixth and final stage in a capsule rendering. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI.Canvas Namespace](N_Grasshopper_GUI_Canvas.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)