# M_Grasshopper_Kernel_GH_ZuiAction_SetupTooltip

﻿ GH\_ZuiAction.SetupTooltip Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_ZuiAction Class](../html/T_Grasshopper_Kernel_GH_ZuiAction.htm "GH_ZuiAction Class")

[GH\_ZuiAction Methods](../html/Methods_T_Grasshopper_Kernel_GH_ZuiAction.htm "GH_ZuiAction Methods")

[IsTooltipRegion Method](../html/M_Grasshopper_Kernel_GH_ZuiAction_IsTooltipRegion.htm "IsTooltipRegion Method ")

[Perform Method](../html/M_Grasshopper_Kernel_GH_ZuiAction_Perform.htm "Perform Method ")

[SetupTooltip Method](../html/M_Grasshopper_Kernel_GH_ZuiAction_SetupTooltip.htm "SetupTooltip Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ZuiActionAddLanguageSpecificTextSet("LST8803E372\_0?cpp=::|nu=.");SetupTooltip Method |

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public abstract void SetupTooltip(
	PointF canvasPoint,
	GH_TooltipDisplayEventArgs e
)
```

```
Public MustOverride Sub SetupTooltip ( 
	canvasPoint As PointF,
	e As GH_TooltipDisplayEventArgs
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

canvasPoint
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST8803E372\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");PointF](https://docs.microsoft.com/dotnet/api/system.drawing.pointf)

e
:   Type: [Grasshopper.GUIAddLanguageSpecificTextSet("LST8803E372\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_TooltipDisplayEventArgs](T_Grasshopper_GUI_GH_TooltipDisplayEventArgs.htm)

#### Implements

[IGH\_TooltipAwareObjectAddLanguageSpecificTextSet("LST8803E372\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");SetupTooltip(PointF, GH\_TooltipDisplayEventArgs)](M_Grasshopper_GUI_Canvas_IGH_TooltipAwareObject_SetupTooltip.htm)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_ZuiAction Class](T_Grasshopper_Kernel_GH_ZuiAction.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)