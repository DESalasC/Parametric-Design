# T_Grasshopper_GUI_GH_Tooltip

﻿ GH\_Tooltip Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH\_Tooltip Class](../html/T_Grasshopper_GUI_GH_Tooltip.htm "GH_Tooltip Class")

[GH\_Tooltip Properties](../html/Properties_T_Grasshopper_GUI_GH_Tooltip.htm "GH_Tooltip Properties")

[GH\_Tooltip Methods](../html/Methods_T_Grasshopper_GUI_GH_Tooltip.htm "GH_Tooltip Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_Tooltip Class |

Implements a custom Tooltip class with advanced functionality.
All methods and fields are Shared. There can never be more than one GH\_Tooltip.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST151081C\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.GUIAddLanguageSpecificTextSet("LST151081C\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Tooltip

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public sealed class GH_Tooltip
```

```
Public NotInheritable Class GH_Tooltip
```

AddLanguageTabSet("ID1EBCA");

The GH\_Tooltip type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public propertyStatic member | [Tag](P_Grasshopper_GUI_GH_Tooltip_Tag.htm) | Gets or sets the tag object for the tooltip |
| Public propertyStatic member | [TooltipForm](P_Grasshopper_GUI_GH_Tooltip_TooltipForm.htm) | Gets the internal instance of GH\_TooltipForm. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public methodStatic member | [Adjust](M_Grasshopper_GUI_GH_Tooltip_Adjust.htm) | Repositions the tooltip to match with new cursor positions. |
| Public methodStatic member | [AssignTooltipFields](M_Grasshopper_GUI_GH_Tooltip_AssignTooltipFields.htm) | Set all fields of the Tooltip. You'll still need to call Show() to display the tooltip. |
| Public methodStatic member | [Clear](M_Grasshopper_GUI_GH_Tooltip_Clear.htm) | Hides the tooltip and clears all references and caches. |
| Public methodStatic member | [IsOwner](M_Grasshopper_GUI_GH_Tooltip_IsOwner.htm) | Returns true if the test control matches the internal Owner control. Use this method to make sure you actually own this tooltip prior to clearing it. |
| Public methodStatic member | [IsTag](M_Grasshopper_GUI_GH_Tooltip_IsTag.htm) | Returns True if the test object matches the internal Tag object |
| Public methodStatic member | [Layout](M_Grasshopper_GUI_GH_Tooltip_Layout.htm) | Layout the tooltip fields. Layout happens automatically if you use the AssigTooltipField method, if however you poke values directly in the tooltip form you must place a call to Layout() before showing the tooltip. |
| Public methodStatic member | [Show](M_Grasshopper_GUI_GH_Tooltip_Show.htm) | Display the tooltip on screen. |
| Public methodStatic member | [TooltipDetailedInformation](M_Grasshopper_GUI_GH_Tooltip_TooltipDetailedInformation.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)