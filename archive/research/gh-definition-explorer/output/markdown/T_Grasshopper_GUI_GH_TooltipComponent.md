# T_Grasshopper_GUI_GH_TooltipComponent

﻿ GH\_TooltipComponent Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH\_TooltipComponent Class](../html/T_Grasshopper_GUI_GH_TooltipComponent.htm "GH_TooltipComponent Class")

[GH\_TooltipComponent Constructor](../html/M_Grasshopper_GUI_GH_TooltipComponent__ctor.htm "GH_TooltipComponent Constructor ")

[GH\_TooltipComponent Properties](../html/Properties_T_Grasshopper_GUI_GH_TooltipComponent.htm "GH_TooltipComponent Properties")

[GH\_TooltipComponent Methods](../html/Methods_T_Grasshopper_GUI_GH_TooltipComponent.htm "GH_TooltipComponent Methods")

[GH\_TooltipComponent Events](../html/Events_T_Grasshopper_GUI_GH_TooltipComponent.htm "GH_TooltipComponent Events")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_TooltipComponent Class |

This component provides Grasshopper tooltip functionality through a winforms Component.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LSTD6971485\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [SystemAddLanguageSpecificTextSet("LSTD6971485\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");MarshalByRefObject](https://docs.microsoft.com/dotnet/api/system.marshalbyrefobject)  
    [System.ComponentModelAddLanguageSpecificTextSet("LSTD6971485\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Component](https://docs.microsoft.com/dotnet/api/system.componentmodel.component)  
      Grasshopper.GUIAddLanguageSpecificTextSet("LSTD6971485\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_TooltipComponent

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public sealed class GH_TooltipComponent : Component
```

```
Public NotInheritable Class GH_TooltipComponent
	Inherits Component
```

AddLanguageTabSet("ID1EBCA");

The GH\_TooltipComponent type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_TooltipComponent](M_Grasshopper_GUI_GH_TooltipComponent__ctor.htm) | Initializes a new instance of the GH\_TooltipComponent class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Delay](P_Grasshopper_GUI_GH_TooltipComponent_Delay.htm) | Gets or sets the delay (in milliseconds) for this tooltip to appear. |
| Public property | [Enabled](P_Grasshopper_GUI_GH_TooltipComponent_Enabled.htm) | Gets or sets the Enabled flag. |
| Public property | [Tag](P_Grasshopper_GUI_GH_TooltipComponent_Tag.htm) | Provides an easy way to store information on this Tooltip. |
| Public property | [Target](P_Grasshopper_GUI_GH_TooltipComponent_Target.htm) | Gets or sets the control this tooltip is tied to. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [Hide](M_Grasshopper_GUI_GH_TooltipComponent_Hide.htm) |  |
| Public method | [IsTag](M_Grasshopper_GUI_GH_TooltipComponent_IsTag.htm) | Test whether the current Tooltip tag matches the object. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Events

|  | Name | Description |
| --- | --- | --- |
| Public event | [PopulateTooltip](E_Grasshopper_GUI_GH_TooltipComponent_PopulateTooltip.htm) | This event is raised just prior to the tooltip display. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)