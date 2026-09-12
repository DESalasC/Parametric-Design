# P_Grasshopper_Kernel_Undo_GH_UndoRecord_ExpiresDisplay

﻿ GH\_UndoRecord.ExpiresDisplay Property 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Undo](../html/N_Grasshopper_Kernel_Undo.htm "Grasshopper.Kernel.Undo")

[GH\_UndoRecord Class](../html/T_Grasshopper_Kernel_Undo_GH_UndoRecord.htm "GH_UndoRecord Class")

[GH\_UndoRecord Properties](../html/Properties_T_Grasshopper_Kernel_Undo_GH_UndoRecord.htm "GH_UndoRecord Properties")

[ActionCount Property](../html/P_Grasshopper_Kernel_Undo_GH_UndoRecord_ActionCount.htm "ActionCount Property ")

[Actions Property](../html/P_Grasshopper_Kernel_Undo_GH_UndoRecord_Actions.htm "Actions Property ")

[ExpiresDisplay Property](../html/P_Grasshopper_Kernel_Undo_GH_UndoRecord_ExpiresDisplay.htm "ExpiresDisplay Property ")

[ExpiresSolution Property](../html/P_Grasshopper_Kernel_Undo_GH_UndoRecord_ExpiresSolution.htm "ExpiresSolution Property ")

[Guid Property](../html/P_Grasshopper_Kernel_Undo_GH_UndoRecord_Guid.htm "Guid Property ")

[Name Property](../html/P_Grasshopper_Kernel_Undo_GH_UndoRecord_Name.htm "Name Property ")

[State Property](../html/P_Grasshopper_Kernel_Undo_GH_UndoRecord_State.htm "State Property ")

[Time Property](../html/P_Grasshopper_Kernel_Undo_GH_UndoRecord_Time.htm "Time Property ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_UndoRecordAddLanguageSpecificTextSet("LSTE16BBF98\_0?cpp=::|nu=.");ExpiresDisplay Property |

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
public bool ExpiresDisplay { get; }
```

```
Public ReadOnly Property ExpiresDisplay As Boolean
	Get
```

AddLanguageTabSet("ID0EBCA");

#### Property Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  

[Missing <value> documentation for "P:Grasshopper.Kernel.Undo.GH\_UndoRecord.ExpiresDisplay"]

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_UndoRecord Class](T_Grasshopper_Kernel_Undo_GH_UndoRecord.htm)

[Grasshopper.Kernel.Undo Namespace](N_Grasshopper_Kernel_Undo.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)