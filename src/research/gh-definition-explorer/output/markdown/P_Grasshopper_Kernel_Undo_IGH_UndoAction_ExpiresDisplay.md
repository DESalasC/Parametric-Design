# P_Grasshopper_Kernel_Undo_IGH_UndoAction_ExpiresDisplay

﻿ IGH\_UndoAction.ExpiresDisplay Property 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Undo](../html/N_Grasshopper_Kernel_Undo.htm "Grasshopper.Kernel.Undo")

[IGH\_UndoAction Interface](../html/T_Grasshopper_Kernel_Undo_IGH_UndoAction.htm "IGH_UndoAction Interface")

[IGH\_UndoAction Properties](../html/Properties_T_Grasshopper_Kernel_Undo_IGH_UndoAction.htm "IGH_UndoAction Properties")

[ExpiresDisplay Property](../html/P_Grasshopper_Kernel_Undo_IGH_UndoAction_ExpiresDisplay.htm "ExpiresDisplay Property ")

[ExpiresSolution Property](../html/P_Grasshopper_Kernel_Undo_IGH_UndoAction_ExpiresSolution.htm "ExpiresSolution Property ")

[State Property](../html/P_Grasshopper_Kernel_Undo_IGH_UndoAction_State.htm "State Property ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_UndoActionAddLanguageSpecificTextSet("LSTBCDFEC55\_0?cpp=::|nu=.");ExpiresDisplay Property |

Gets the display expiration flag for this event. If True, the Rhino viewports will be redrawn
once the entire undo record has been completed.
If ExpiresSolution is set to true, ExpriresDisplay is implied.

**Namespace:**
 [Grasshopper.Kernel.Undo](N_Grasshopper_Kernel_Undo.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
bool ExpiresDisplay { get; }
```

```
ReadOnly Property ExpiresDisplay As Boolean
	Get
```

AddLanguageTabSet("ID0EBCA");

#### Property Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  

[Missing <value> documentation for "P:Grasshopper.Kernel.Undo.IGH\_UndoAction.ExpiresDisplay"]

![](../icons/SectionExpanded.png)See Also

#### Reference

[IGH\_UndoAction Interface](T_Grasshopper_Kernel_Undo_IGH_UndoAction.htm)

[Grasshopper.Kernel.Undo Namespace](N_Grasshopper_Kernel_Undo.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)