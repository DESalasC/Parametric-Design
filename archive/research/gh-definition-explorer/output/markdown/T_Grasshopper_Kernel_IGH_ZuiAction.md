# T_Grasshopper_Kernel_IGH_ZuiAction

﻿ IGH\_ZuiAction Interface

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH\_ZuiAction Interface](../html/T_Grasshopper_Kernel_IGH_ZuiAction.htm "IGH_ZuiAction Interface")

[IGH\_ZuiAction Properties](../html/Properties_T_Grasshopper_Kernel_IGH_ZuiAction.htm "IGH_ZuiAction Properties")

[IGH\_ZuiAction Methods](../html/Methods_T_Grasshopper_Kernel_IGH_ZuiAction.htm "IGH_ZuiAction Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_ZuiAction Interface |

Represents a single action which is only visible on screen above a certain zoom level.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public interface IGH_ZuiAction : IGH_TooltipAwareObject
```

```
Public Interface IGH_ZuiAction
	Inherits IGH_TooltipAwareObject
```

AddLanguageTabSet("ID0EBCA");

The IGH\_ZuiAction type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Name](P_Grasshopper_Kernel_IGH_ZuiAction_Name.htm) | Gets the display name for this action. Keep it short and sweet. |
| Public property | [TooltipEnabled](P_Grasshopper_GUI_Canvas_IGH_TooltipAwareObject_TooltipEnabled.htm) | Gets the tooltip enabled value. If False, no further tooltip functions will be called. (Inherited from [IGH\_TooltipAwareObject](T_Grasshopper_GUI_Canvas_IGH_TooltipAwareObject.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [IsTooltipRegion](M_Grasshopper_GUI_Canvas_IGH_TooltipAwareObject_IsTooltipRegion.htm) | Determine whether the specified pixel should result in a tooltip when the cursor hovers over it. (Inherited from [IGH\_TooltipAwareObject](T_Grasshopper_GUI_Canvas_IGH_TooltipAwareObject.htm).) |
| Public method | [Perform](M_Grasshopper_Kernel_IGH_ZuiAction_Perform.htm) | This method will be called when the action needs to be performed. |
| Public method | [SetupTooltip](M_Grasshopper_GUI_Canvas_IGH_TooltipAwareObject_SetupTooltip.htm) | This function is called when a tooltip it about to be displayed. (Inherited from [IGH\_TooltipAwareObject](T_Grasshopper_GUI_Canvas_IGH_TooltipAwareObject.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)