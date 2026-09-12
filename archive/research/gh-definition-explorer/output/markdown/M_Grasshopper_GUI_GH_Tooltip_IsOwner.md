# M_Grasshopper_GUI_GH_Tooltip_IsOwner

﻿ GH\_Tooltip.IsOwner Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH\_Tooltip Class](../html/T_Grasshopper_GUI_GH_Tooltip.htm "GH_Tooltip Class")

[GH\_Tooltip Methods](../html/Methods_T_Grasshopper_GUI_GH_Tooltip.htm "GH_Tooltip Methods")

[Adjust Method](../html/M_Grasshopper_GUI_GH_Tooltip_Adjust.htm "Adjust Method ")

[AssignTooltipFields Method](../html/M_Grasshopper_GUI_GH_Tooltip_AssignTooltipFields.htm "AssignTooltipFields Method ")

[Clear Method](../html/M_Grasshopper_GUI_GH_Tooltip_Clear.htm "Clear Method ")

[IsOwner Method](../html/M_Grasshopper_GUI_GH_Tooltip_IsOwner.htm "IsOwner Method ")

[IsTag Method](../html/M_Grasshopper_GUI_GH_Tooltip_IsTag.htm "IsTag Method ")

[Layout Method](../html/M_Grasshopper_GUI_GH_Tooltip_Layout.htm "Layout Method ")

[Show Method](../html/M_Grasshopper_GUI_GH_Tooltip_Show.htm "Show Method ")

[TooltipDetailedInformation Method](../html/M_Grasshopper_GUI_GH_Tooltip_TooltipDetailedInformation.htm "TooltipDetailedInformation Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_TooltipAddLanguageSpecificTextSet("LST8FF02686\_0?cpp=::|nu=.");IsOwner Method |

Returns true if the test control matches the internal Owner control.
Use this method to make sure you actually own this tooltip prior to clearing it.

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static bool IsOwner(
	Control test
)
```

```
Public Shared Function IsOwner ( 
	test As Control
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

test
:   Type: [System.Windows.FormsAddLanguageSpecificTextSet("LST8FF02686\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Control](https://docs.microsoft.com/dotnet/api/system.windows.forms.control)

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)

![](../icons/SectionExpanded.png)Remarks

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Tooltip Class](T_Grasshopper_GUI_GH_Tooltip.htm)

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)