# T_Grasshopper_GUI_IGH_FileDropTarget

﻿ IGH\_FileDropTarget Interface

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[IGH\_FileDropTarget Interface](../html/T_Grasshopper_GUI_IGH_FileDropTarget.htm "IGH_FileDropTarget Interface")

[IGH\_FileDropTarget Methods](../html/Methods_T_Grasshopper_GUI_IGH_FileDropTarget.htm "IGH_FileDropTarget Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_FileDropTarget Interface |

Implement this interface in your IGH\_DocumentObject if you want to participate in Drag+Drop events.

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public interface IGH_FileDropTarget
```

```
Public Interface IGH_FileDropTarget
```

AddLanguageTabSet("ID0EBCA");

The IGH\_FileDropTarget type exposes the following members.

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [AcceptableFile](M_Grasshopper_GUI_IGH_FileDropTarget_AcceptableFile.htm) | Gets a value indicating whether or not the path can be handled by the local object. |
| Public method | [HandleDrop](M_Grasshopper_GUI_IGH_FileDropTarget_HandleDrop.htm) | Handle a file drop. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)