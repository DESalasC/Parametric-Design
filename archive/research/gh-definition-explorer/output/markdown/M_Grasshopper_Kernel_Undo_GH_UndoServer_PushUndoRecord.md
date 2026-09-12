# M_Grasshopper_Kernel_Undo_GH_UndoServer_PushUndoRecord

﻿ GH\_UndoServer.PushUndoRecord Method (GH\_UndoRecord)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Undo](../html/N_Grasshopper_Kernel_Undo.htm "Grasshopper.Kernel.Undo")

[GH\_UndoServer Class](../html/T_Grasshopper_Kernel_Undo_GH_UndoServer.htm "GH_UndoServer Class")

[GH\_UndoServer Methods](../html/Methods_T_Grasshopper_Kernel_Undo_GH_UndoServer.htm "GH_UndoServer Methods")

[PushUndoRecord Method](../html/Overload_Grasshopper_Kernel_Undo_GH_UndoServer_PushUndoRecord.htm "PushUndoRecord Method ")

[PushUndoRecord Method (GH\_UndoRecord)](../html/M_Grasshopper_Kernel_Undo_GH_UndoServer_PushUndoRecord.htm "PushUndoRecord Method (GH_UndoRecord)")

[PushUndoRecord Method (String, GH\_UndoAction)](../html/M_Grasshopper_Kernel_Undo_GH_UndoServer_PushUndoRecord_1.htm "PushUndoRecord Method (String, GH_UndoAction)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_UndoServerAddLanguageSpecificTextSet("LST9AA3D26F\_0?cpp=::|nu=.");PushUndoRecord Method (GH\_UndoRecord) |

Add a new undo record to the undo stack, this function clears the Redo stack.

**Namespace:**
 [Grasshopper.Kernel.Undo](N_Grasshopper_Kernel_Undo.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public void PushUndoRecord(
	GH_UndoRecord record
)
```

```
Public Sub PushUndoRecord ( 
	record As GH_UndoRecord
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

record
:   Type: [Grasshopper.Kernel.UndoAddLanguageSpecificTextSet("LST9AA3D26F\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_UndoRecord](T_Grasshopper_Kernel_Undo_GH_UndoRecord.htm)  
    Record to add.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_UndoServer Class](T_Grasshopper_Kernel_Undo_GH_UndoServer.htm)

[PushUndoRecord Overload](Overload_Grasshopper_Kernel_Undo_GH_UndoServer_PushUndoRecord.htm)

[Grasshopper.Kernel.Undo Namespace](N_Grasshopper_Kernel_Undo.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)