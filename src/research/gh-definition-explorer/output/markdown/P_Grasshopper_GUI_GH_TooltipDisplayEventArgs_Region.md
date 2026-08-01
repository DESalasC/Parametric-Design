# P_Grasshopper_GUI_GH_TooltipDisplayEventArgs_Region

﻿ GH\_TooltipDisplayEventArgs.Region Property 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH\_TooltipDisplayEventArgs Class](../html/T_Grasshopper_GUI_GH_TooltipDisplayEventArgs.htm "GH_TooltipDisplayEventArgs Class")

[GH\_TooltipDisplayEventArgs Properties](../html/Properties_T_Grasshopper_GUI_GH_TooltipDisplayEventArgs.htm "GH_TooltipDisplayEventArgs Properties")

[Control Property](../html/P_Grasshopper_GUI_GH_TooltipDisplayEventArgs_Control.htm "Control Property ")

[Description Property](../html/P_Grasshopper_GUI_GH_TooltipDisplayEventArgs_Description.htm "Description Property ")

[Diagram Property](../html/P_Grasshopper_GUI_GH_TooltipDisplayEventArgs_Diagram.htm "Diagram Property ")

[Icon Property](../html/P_Grasshopper_GUI_GH_TooltipDisplayEventArgs_Icon.htm "Icon Property ")

[Point Property](../html/P_Grasshopper_GUI_GH_TooltipDisplayEventArgs_Point.htm "Point Property ")

[Region Property](../html/P_Grasshopper_GUI_GH_TooltipDisplayEventArgs_Region.htm "Region Property ")

[Text Property](../html/P_Grasshopper_GUI_GH_TooltipDisplayEventArgs_Text.htm "Text Property ")

[Title Property](../html/P_Grasshopper_GUI_GH_TooltipDisplayEventArgs_Title.htm "Title Property ")

[Valid Property](../html/P_Grasshopper_GUI_GH_TooltipDisplayEventArgs_Valid.htm "Valid Property ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_TooltipDisplayEventArgsAddLanguageSpecificTextSet("LST8BFAB119\_0?cpp=::|nu=.");Region Property |

Gets or sets the active region (in control coordinates) for this tooltip.
Once a tooltip is shown inside the region, the tooltip will 'stick' to the mouse
for as long as the mouse remains within this region. By default the region is
set to Rectangle.Empty, which indicates that region tracking is not used for this
tooltip.

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public Rectangle Region { get; set; }
```

```
Public Property Region As Rectangle
	Get
	Set
```

AddLanguageTabSet("ID0EBCA");

#### Property Value

Type: [Rectangle](https://docs.microsoft.com/dotnet/api/system.drawing.rectangle)  

[Missing <value> documentation for "P:Grasshopper.GUI.GH\_TooltipDisplayEventArgs.Region"]

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_TooltipDisplayEventArgs Class](T_Grasshopper_GUI_GH_TooltipDisplayEventArgs.htm)

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)