# M_Grasshopper_GUI_GH_Tooltip_AssignTooltipFields

﻿ GH\_Tooltip.AssignTooltipFields Method 

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
| GH\_TooltipAddLanguageSpecificTextSet("LSTF2C3F1DE\_0?cpp=::|nu=.");AssignTooltipFields Method |

Set all fields of the Tooltip. You'll still need to call Show() to display the tooltip.

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static void AssignTooltipFields(
	string title = null,
	string text = null,
	string description = null,
	Image icon = null,
	Image diagram = null
)
```

```
Public Shared Sub AssignTooltipFields ( 
	Optional title As String = Nothing,
	Optional text As String = Nothing,
	Optional description As String = Nothing,
	Optional icon As Image = Nothing,
	Optional diagram As Image = Nothing
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

title (Optional)
:   Type: [SystemAddLanguageSpecificTextSet("LSTF2C3F1DE\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    The Title text on the tooltip

text (Optional)
:   Type: [SystemAddLanguageSpecificTextSet("LSTF2C3F1DE\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    The text content of the tooltip

description (Optional)
:   Type: [SystemAddLanguageSpecificTextSet("LSTF2C3F1DE\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    The block text to be displayed in the sunken area of the tooltip.

icon (Optional)
:   Type: [System.DrawingAddLanguageSpecificTextSet("LSTF2C3F1DE\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");Image](https://docs.microsoft.com/dotnet/api/system.drawing.image)  
    The Icon to be displayed next to the Title.

diagram (Optional)
:   Type: [System.DrawingAddLanguageSpecificTextSet("LSTF2C3F1DE\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");Image](https://docs.microsoft.com/dotnet/api/system.drawing.image)  
    The image to be displayed in the sunken area.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Tooltip Class](T_Grasshopper_GUI_GH_Tooltip.htm)

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)