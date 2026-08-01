# M_Grasshopper_Kernel_Attributes_GH_ComponentAttributes_InvalidateCanvas

﻿ GH\_ComponentAttributes.InvalidateCanvas Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Attributes](../html/N_Grasshopper_Kernel_Attributes.htm "Grasshopper.Kernel.Attributes")

[GH\_ComponentAttributes Class](../html/T_Grasshopper_Kernel_Attributes_GH_ComponentAttributes.htm "GH_ComponentAttributes Class")

[GH\_ComponentAttributes Methods](../html/Methods_T_Grasshopper_Kernel_Attributes_GH_ComponentAttributes.htm "GH_ComponentAttributes Methods")

[AppendToAttributeTree Method](../html/M_Grasshopper_Kernel_Attributes_GH_ComponentAttributes_AppendToAttributeTree.htm "AppendToAttributeTree Method ")

[ExpireLayout Method](../html/M_Grasshopper_Kernel_Attributes_GH_ComponentAttributes_ExpireLayout.htm "ExpireLayout Method ")

[InvalidateCanvas Method](../html/M_Grasshopper_Kernel_Attributes_GH_ComponentAttributes_InvalidateCanvas.htm "InvalidateCanvas Method ")

[IsPickRegion Method](../html/Overload_Grasshopper_Kernel_Attributes_GH_ComponentAttributes_IsPickRegion.htm "IsPickRegion Method ")

[Layout Method](../html/M_Grasshopper_Kernel_Attributes_GH_ComponentAttributes_Layout.htm "Layout Method ")

[LayoutBounds Method](../html/M_Grasshopper_Kernel_Attributes_GH_ComponentAttributes_LayoutBounds.htm "LayoutBounds Method ")

[LayoutComponentBox Method](../html/M_Grasshopper_Kernel_Attributes_GH_ComponentAttributes_LayoutComponentBox.htm "LayoutComponentBox Method ")

[LayoutInputParams Method](../html/M_Grasshopper_Kernel_Attributes_GH_ComponentAttributes_LayoutInputParams.htm "LayoutInputParams Method ")

[LayoutOutputParams Method](../html/M_Grasshopper_Kernel_Attributes_GH_ComponentAttributes_LayoutOutputParams.htm "LayoutOutputParams Method ")

[Render Method](../html/M_Grasshopper_Kernel_Attributes_GH_ComponentAttributes_Render.htm "Render Method ")

[RenderComponentCapsule Method](../html/Overload_Grasshopper_Kernel_Attributes_GH_ComponentAttributes_RenderComponentCapsule.htm "RenderComponentCapsule Method ")

[RenderComponentParameters Method](../html/M_Grasshopper_Kernel_Attributes_GH_ComponentAttributes_RenderComponentParameters.htm "RenderComponentParameters Method ")

[RenderVariableParameterUI Method](../html/M_Grasshopper_Kernel_Attributes_GH_ComponentAttributes_RenderVariableParameterUI.htm "RenderVariableParameterUI Method ")

[RespondToMouseDown Method](../html/M_Grasshopper_Kernel_Attributes_GH_ComponentAttributes_RespondToMouseDown.htm "RespondToMouseDown Method ")

[SetupTooltip Method](../html/M_Grasshopper_Kernel_Attributes_GH_ComponentAttributes_SetupTooltip.htm "SetupTooltip Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ComponentAttributesAddLanguageSpecificTextSet("LST5782C59C\_0?cpp=::|nu=.");InvalidateCanvas Method |

The canvas must be invalidated when the mouse is near enough and
this component has variable parameters.

**Namespace:**
 [Grasshopper.Kernel.Attributes](N_Grasshopper_Kernel_Attributes.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public override bool InvalidateCanvas(
	GH_Canvas canvas,
	GH_CanvasMouseEvent e
)
```

```
Public Overrides Function InvalidateCanvas ( 
	canvas As GH_Canvas,
	e As GH_CanvasMouseEvent
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

canvas
:   Type: [Grasshopper.GUI.CanvasAddLanguageSpecificTextSet("LST5782C59C\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Canvas](T_Grasshopper_GUI_Canvas_GH_Canvas.htm)

e
:   Type: [Grasshopper.GUIAddLanguageSpecificTextSet("LST5782C59C\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_CanvasMouseEvent](T_Grasshopper_GUI_GH_CanvasMouseEvent.htm)

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_ComponentAttributes Class](T_Grasshopper_Kernel_Attributes_GH_ComponentAttributes.htm)

[Grasshopper.Kernel.Attributes Namespace](N_Grasshopper_Kernel_Attributes.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)