# Properties_T_Grasshopper_GUI_GH_TooltipDisplayEventArgs

﻿ GH\_TooltipDisplayEventArgs Properties

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
| GH\_TooltipDisplayEventArgs Properties |

The [GH\_TooltipDisplayEventArgs](T_Grasshopper_GUI_GH_TooltipDisplayEventArgs.htm) type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Control](P_Grasshopper_GUI_GH_TooltipDisplayEventArgs_Control.htm) | Gets the control for whom the tooltip is about to be displayed. |
| Public property | [Description](P_Grasshopper_GUI_GH_TooltipDisplayEventArgs_Description.htm) | Gets or sets the description of the tooltip. This field is optional. |
| Public property | [Diagram](P_Grasshopper_GUI_GH_TooltipDisplayEventArgs_Diagram.htm) | Gets or sets the image that is displayed in the details section of the tooltip. This field is optional, but when it is defined, the Description property is ignored. |
| Public property | [Icon](P_Grasshopper_GUI_GH_TooltipDisplayEventArgs_Icon.htm) | Gets or sets the icon that is displayed in the upper left hand corner of the tooltip. This field is optional. |
| Public property | [Point](P_Grasshopper_GUI_GH_TooltipDisplayEventArgs_Point.htm) | Gets the point in control coordinates for the tooltip locus. |
| Public property | [Region](P_Grasshopper_GUI_GH_TooltipDisplayEventArgs_Region.htm) | Gets or sets the active region (in control coordinates) for this tooltip. Once a tooltip is shown inside the region, the tooltip will 'stick' to the mouse for as long as the mouse remains within this region. By default the region is set to Rectangle.Empty, which indicates that region tracking is not used for this tooltip. |
| Public property | [Text](P_Grasshopper_GUI_GH_TooltipDisplayEventArgs_Text.htm) | Gets or sets the text of the tooltip. If you do not set the Text property, you must set the Title property or the tooltip will not be shown. |
| Public property | [Title](P_Grasshopper_GUI_GH_TooltipDisplayEventArgs_Title.htm) | Gets or sets the title of the tooltip. If you do not set the Title property, you must set the Text property or the tooltip will not be shown. |
| Public property | [Valid](P_Grasshopper_GUI_GH_TooltipDisplayEventArgs_Valid.htm) | Gets whether there is currently enough data to display a tooltip. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_TooltipDisplayEventArgs Class](T_Grasshopper_GUI_GH_TooltipDisplayEventArgs.htm)

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)