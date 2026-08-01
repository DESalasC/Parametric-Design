# M_Grasshopper_Kernel_Undo_GH_UndoServer_MergeRecords

﻿ GH\_UndoServer.MergeRecords Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Undo](../html/N_Grasshopper_Kernel_Undo.htm "Grasshopper.Kernel.Undo")

[GH\_UndoServer Class](../html/T_Grasshopper_Kernel_Undo_GH_UndoServer.htm "GH_UndoServer Class")

[GH\_UndoServer Methods](../html/Methods_T_Grasshopper_Kernel_Undo_GH_UndoServer.htm "GH_UndoServer Methods")

[AppendToDebugLog Method](../html/M_Grasshopper_Kernel_Undo_GH_UndoServer_AppendToDebugLog.htm "AppendToDebugLog Method ")

[Clear Method](../html/M_Grasshopper_Kernel_Undo_GH_UndoServer_Clear.htm "Clear Method ")

[ClearRedo Method](../html/M_Grasshopper_Kernel_Undo_GH_UndoServer_ClearRedo.htm "ClearRedo Method ")

[ClearUndo Method](../html/M_Grasshopper_Kernel_Undo_GH_UndoServer_ClearUndo.htm "ClearUndo Method ")

[MergeRecords Method](../html/M_Grasshopper_Kernel_Undo_GH_UndoServer_MergeRecords.htm "MergeRecords Method ")

[PerformRedo Method](../html/M_Grasshopper_Kernel_Undo_GH_UndoServer_PerformRedo.htm "PerformRedo Method ")

[PerformUndo Method](../html/M_Grasshopper_Kernel_Undo_GH_UndoServer_PerformUndo.htm "PerformUndo Method ")

[PushUndoRecord Method](../html/Overload_Grasshopper_Kernel_Undo_GH_UndoServer_PushUndoRecord.htm "PushUndoRecord Method ")

[RemoveRecord Method](../html/M_Grasshopper_Kernel_Undo_GH_UndoServer_RemoveRecord.htm "RemoveRecord Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_UndoServerAddLanguageSpecificTextSet("LSTFA8F4D32\_0?cpp=::|nu=.");MergeRecords Method |

Attempt to merge the N most recent records into one.
The name of the merged record will be identical to the
name of the oldest record.

**Namespace:**
 [Grasshopper.Kernel.Undo](N_Grasshopper_Kernel_Undo.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public bool MergeRecords(
	int count
)
```

```
Public Function MergeRecords ( 
	count As Integer
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

count
:   Type: [SystemAddLanguageSpecificTextSet("LSTFA8F4D32\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Number of most recent records to merge.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True if merge was successful.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_UndoServer Class](T_Grasshopper_Kernel_Undo_GH_UndoServer.htm)

[Grasshopper.Kernel.Undo Namespace](N_Grasshopper_Kernel_Undo.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)