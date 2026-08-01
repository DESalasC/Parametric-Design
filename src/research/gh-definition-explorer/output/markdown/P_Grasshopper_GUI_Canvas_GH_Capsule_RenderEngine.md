# P_Grasshopper_GUI_Canvas_GH_Capsule_RenderEngine

﻿ GH\_Capsule.RenderEngine Property 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI.Canvas](../html/N_Grasshopper_GUI_Canvas.htm "Grasshopper.GUI.Canvas")

[GH\_Capsule Class](../html/T_Grasshopper_GUI_Canvas_GH_Capsule.htm "GH_Capsule Class")

[GH\_Capsule Properties](../html/Properties_T_Grasshopper_GUI_Canvas_GH_Capsule.htm "GH_Capsule Properties")

[Box Property](../html/P_Grasshopper_GUI_Canvas_GH_Capsule_Box.htm "Box Property ")

[Box\_Content Property](../html/P_Grasshopper_GUI_Canvas_GH_Capsule_Box_Content.htm "Box_Content Property ")

[Font Property](../html/P_Grasshopper_GUI_Canvas_GH_Capsule_Font.htm "Font Property ")

[Highlight Property](../html/P_Grasshopper_GUI_Canvas_GH_Capsule_Highlight.htm "Highlight Property ")

[HighlightShape Property](../html/P_Grasshopper_GUI_Canvas_GH_Capsule_HighlightShape.htm "HighlightShape Property ")

[InputGrips Property](../html/P_Grasshopper_GUI_Canvas_GH_Capsule_InputGrips.htm "InputGrips Property ")

[JaggedLeft Property](../html/P_Grasshopper_GUI_Canvas_GH_Capsule_JaggedLeft.htm "JaggedLeft Property ")

[JaggedRight Property](../html/P_Grasshopper_GUI_Canvas_GH_Capsule_JaggedRight.htm "JaggedRight Property ")

[MaxRadius Property](../html/P_Grasshopper_GUI_Canvas_GH_Capsule_MaxRadius.htm "MaxRadius Property ")

[OutlineShape Property](../html/P_Grasshopper_GUI_Canvas_GH_Capsule_OutlineShape.htm "OutlineShape Property ")

[OutputGrips Property](../html/P_Grasshopper_GUI_Canvas_GH_Capsule_OutputGrips.htm "OutputGrips Property ")

[Palette Property](../html/P_Grasshopper_GUI_Canvas_GH_Capsule_Palette.htm "Palette Property ")

[Radius Property](../html/P_Grasshopper_GUI_Canvas_GH_Capsule_Radius.htm "Radius Property ")

[RenderEngine Property](../html/P_Grasshopper_GUI_Canvas_GH_Capsule_RenderEngine.htm "RenderEngine Property ")

[Text Property](../html/P_Grasshopper_GUI_Canvas_GH_Capsule_Text.htm "Text Property ")

[TextOrientation Property](../html/P_Grasshopper_GUI_Canvas_GH_Capsule_TextOrientation.htm "TextOrientation Property ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_CapsuleAddLanguageSpecificTextSet("LST163B3D00\_0?cpp=::|nu=.");RenderEngine Property |

Gets the RenderEngine associated with this capsule.
You typically don't need to go this far, just use
one of the Render() overloads on GH\_Capsule directly.

**Namespace:**
 [Grasshopper.GUI.Canvas](N_Grasshopper_GUI_Canvas.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public GH_CapsuleRenderEngine RenderEngine { get; }
```

```
Public ReadOnly Property RenderEngine As GH_CapsuleRenderEngine
	Get
```

AddLanguageTabSet("ID0EBCA");

#### Property Value

Type: [GH\_CapsuleRenderEngine](T_Grasshopper_GUI_Canvas_GH_CapsuleRenderEngine.htm)  

[Missing <value> documentation for "P:Grasshopper.GUI.Canvas.GH\_Capsule.RenderEngine"]

![](../icons/SectionExpanded.png)Remarks

Do not store pointers to the RenderEngine, always call this property anew.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Capsule Class](T_Grasshopper_GUI_Canvas_GH_Capsule.htm)

[Grasshopper.GUI.Canvas Namespace](N_Grasshopper_GUI_Canvas.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)