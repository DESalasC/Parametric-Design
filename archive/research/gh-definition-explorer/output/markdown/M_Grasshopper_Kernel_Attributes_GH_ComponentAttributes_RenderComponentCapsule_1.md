# M_Grasshopper_Kernel_Attributes_GH_ComponentAttributes_RenderComponentCapsule_1

﻿ GH\_ComponentAttributes.RenderComponentCapsule Method (GH\_Canvas, Graphics, Boolean, Boolean, Boolean, Boolean, Boolean, Boolean)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Attributes](../html/N_Grasshopper_Kernel_Attributes.htm "Grasshopper.Kernel.Attributes")

[GH\_ComponentAttributes Class](../html/T_Grasshopper_Kernel_Attributes_GH_ComponentAttributes.htm "GH_ComponentAttributes Class")

[GH\_ComponentAttributes Methods](../html/Methods_T_Grasshopper_Kernel_Attributes_GH_ComponentAttributes.htm "GH_ComponentAttributes Methods")

[RenderComponentCapsule Method](../html/Overload_Grasshopper_Kernel_Attributes_GH_ComponentAttributes_RenderComponentCapsule.htm "RenderComponentCapsule Method ")

[RenderComponentCapsule Method (GH\_Canvas, Graphics)](../html/M_Grasshopper_Kernel_Attributes_GH_ComponentAttributes_RenderComponentCapsule.htm "RenderComponentCapsule Method (GH_Canvas, Graphics)")

[RenderComponentCapsule Method (GH\_Canvas, Graphics, Boolean, Boolean, Boolean, Boolean, Boolean, Boolean)](../html/M_Grasshopper_Kernel_Attributes_GH_ComponentAttributes_RenderComponentCapsule_1.htm "RenderComponentCapsule Method (GH_Canvas, Graphics, Boolean, Boolean, Boolean, Boolean, Boolean, Boolean)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ComponentAttributesAddLanguageSpecificTextSet("LSTE4B57EDE\_0?cpp=::|nu=.");RenderComponentCapsule Method (GH\_Canvas, Graphics, Boolean, Boolean, Boolean, Boolean, Boolean, Boolean) |

Utility function, draws the component capsule including all specified elements.

**Namespace:**
 [Grasshopper.Kernel.Attributes](N_Grasshopper_Kernel_Attributes.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
protected void RenderComponentCapsule(
	GH_Canvas canvas,
	Graphics graphics,
	bool drawComponentBaseBox,
	bool drawComponentNameBox,
	bool drawJaggedEdges,
	bool drawParameterGrips,
	bool drawParameterNames,
	bool drawZuiElements
)
```

```
Protected Sub RenderComponentCapsule ( 
	canvas As GH_Canvas,
	graphics As Graphics,
	drawComponentBaseBox As Boolean,
	drawComponentNameBox As Boolean,
	drawJaggedEdges As Boolean,
	drawParameterGrips As Boolean,
	drawParameterNames As Boolean,
	drawZuiElements As Boolean
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

canvas
:   Type: [Grasshopper.GUI.CanvasAddLanguageSpecificTextSet("LSTE4B57EDE\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Canvas](T_Grasshopper_GUI_Canvas_GH_Canvas.htm)  
    Canvas to draw into.

graphics
:   Type: [System.DrawingAddLanguageSpecificTextSet("LSTE4B57EDE\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Graphics](https://docs.microsoft.com/dotnet/api/system.drawing.graphics)  
    Graphics object to draw with.

drawComponentBaseBox
:   Type: [SystemAddLanguageSpecificTextSet("LSTE4B57EDE\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
    If true, will draw the component background box.

drawComponentNameBox
:   Type: [SystemAddLanguageSpecificTextSet("LSTE4B57EDE\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
    If true, will draw component nickname/icon element.

drawJaggedEdges
:   Type: [SystemAddLanguageSpecificTextSet("LSTE4B57EDE\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
    If true, parameterless sides will have jagged edges drawn on them.

drawParameterGrips
:   Type: [SystemAddLanguageSpecificTextSet("LSTE4B57EDE\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
    If true, will draw parameter grips.

drawParameterNames
:   Type: [SystemAddLanguageSpecificTextSet("LSTE4B57EDE\_7?cs=.|vb=.|cpp=::|nu=.|fs=.");Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
    If true, will draw parameter nicknames.

drawZuiElements
:   Type: [SystemAddLanguageSpecificTextSet("LSTE4B57EDE\_8?cs=.|vb=.|cpp=::|nu=.|fs=.");Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
    If true, will draw ZUI variable parameter interface.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_ComponentAttributes Class](T_Grasshopper_Kernel_Attributes_GH_ComponentAttributes.htm)

[RenderComponentCapsule Overload](Overload_Grasshopper_Kernel_Attributes_GH_ComponentAttributes_RenderComponentCapsule.htm)

[Grasshopper.Kernel.Attributes Namespace](N_Grasshopper_Kernel_Attributes.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)