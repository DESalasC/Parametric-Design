# T_Grasshopper_GUI_GH_DragInfo

﻿ GH\_DragInfo Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH\_DragInfo Class](../html/T_Grasshopper_GUI_GH_DragInfo.htm "GH_DragInfo Class")

[GH\_DragInfo Constructor](../html/M_Grasshopper_GUI_GH_DragInfo__ctor.htm "GH_DragInfo Constructor ")

[GH\_DragInfo Properties](../html/Properties_T_Grasshopper_GUI_GH_DragInfo.htm "GH_DragInfo Properties")

[GH\_DragInfo Methods](../html/Methods_T_Grasshopper_GUI_GH_DragInfo.htm "GH_DragInfo Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_DragInfo Class |

Contains data used for UI drag operations.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST11DA2361\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.GUIAddLanguageSpecificTextSet("LST11DA2361\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_DragInfo

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_DragInfo
```

```
Public Class GH_DragInfo
```

AddLanguageTabSet("ID1EBCA");

The GH\_DragInfo type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_DragInfo](M_Grasshopper_GUI_GH_DragInfo__ctor.htm) | Create a new DragInfo instance. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Box\_Drag](P_Grasshopper_GUI_GH_DragInfo_Box_Drag.htm) | Gets the dimensions of the box as a result of the dragging op. |
| Public property | [Box\_Start](P_Grasshopper_GUI_GH_DragInfo_Box_Start.htm) | Gets the dimensions of the drag box prior to dragging. |
| Public property | [Constraint](P_Grasshopper_GUI_GH_DragInfo_Constraint.htm) | Gets or sets the directional constraint for the drag operation. |
| Public property | [Point\_Drag](P_Grasshopper_GUI_GH_DragInfo_Point_Drag.htm) | Gets the cursor location at the current moment. |
| Public property | [Point\_Start](P_Grasshopper_GUI_GH_DragInfo_Point_Start.htm) | Gets the cursor location at the start of the drag. |
| Public property | [Region](P_Grasshopper_GUI_GH_DragInfo_Region.htm) | Gets or sets the drag limits. If the region is Rectangle.Empty then the region is ignored. For valid results the Region should be larger than the dimensions of the drag box. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [Drag](M_Grasshopper_GUI_GH_DragInfo_Drag.htm) | Call this method to adjust the drag data. Results will be automatically constrained and limited. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)