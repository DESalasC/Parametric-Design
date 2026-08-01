# M_Grasshopper_GUI_Canvas_IGH_TooltipAwareObject_SetupTooltip

﻿ IGH\_TooltipAwareObject.SetupTooltip Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI.Canvas](../html/N_Grasshopper_GUI_Canvas.htm "Grasshopper.GUI.Canvas")

[IGH\_TooltipAwareObject Interface](../html/T_Grasshopper_GUI_Canvas_IGH_TooltipAwareObject.htm "IGH_TooltipAwareObject Interface")

[IGH\_TooltipAwareObject Methods](../html/Methods_T_Grasshopper_GUI_Canvas_IGH_TooltipAwareObject.htm "IGH_TooltipAwareObject Methods")

[IsTooltipRegion Method](../html/M_Grasshopper_GUI_Canvas_IGH_TooltipAwareObject_IsTooltipRegion.htm "IsTooltipRegion Method ")

[SetupTooltip Method](../html/M_Grasshopper_GUI_Canvas_IGH_TooltipAwareObject_SetupTooltip.htm "SetupTooltip Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_TooltipAwareObjectAddLanguageSpecificTextSet("LST6289B253\_0?cpp=::|nu=.");SetupTooltip Method |

This function is called when a tooltip it about to be displayed.

**Namespace:**
 [Grasshopper.GUI.Canvas](N_Grasshopper_GUI_Canvas.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
void SetupTooltip(
	PointF canvasPoint,
	GH_TooltipDisplayEventArgs e
)
```

```
Sub SetupTooltip ( 
	canvasPoint As PointF,
	e As GH_TooltipDisplayEventArgs
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

canvasPoint
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST6289B253\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");PointF](https://docs.microsoft.com/dotnet/api/system.drawing.pointf)  
    The pixel coordinate on the canvas of the cursor.

e
:   Type: [Grasshopper.GUIAddLanguageSpecificTextSet("LST6289B253\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_TooltipDisplayEventArgs](T_Grasshopper_GUI_GH_TooltipDisplayEventArgs.htm)  
    Tooltip display arguments.

![](../icons/SectionExpanded.png)See Also

#### Reference

[IGH\_TooltipAwareObject Interface](T_Grasshopper_GUI_Canvas_IGH_TooltipAwareObject.htm)

[Grasshopper.GUI.Canvas Namespace](N_Grasshopper_GUI_Canvas.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)