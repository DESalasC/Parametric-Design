# M_Grasshopper_Kernel_Undo_GH_UndoRecord_AddAction

﻿ GH\_UndoRecord.AddAction Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Undo](../html/N_Grasshopper_Kernel_Undo.htm "Grasshopper.Kernel.Undo")

[GH\_UndoRecord Class](../html/T_Grasshopper_Kernel_Undo_GH_UndoRecord.htm "GH_UndoRecord Class")

[GH\_UndoRecord Methods](../html/Methods_T_Grasshopper_Kernel_Undo_GH_UndoRecord.htm "GH_UndoRecord Methods")

[AddAction Method](../html/M_Grasshopper_Kernel_Undo_GH_UndoRecord_AddAction.htm "AddAction Method ")

[Redo Method](../html/M_Grasshopper_Kernel_Undo_GH_UndoRecord_Redo.htm "Redo Method ")

[Undo Method](../html/M_Grasshopper_Kernel_Undo_GH_UndoRecord_Undo.htm "Undo Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_UndoRecordAddLanguageSpecificTextSet("LSTC079CE01\_0?cpp=::|nu=.");AddAction Method |

Append an undo action to this record. You should only do this prior to calling undo for the first time.

**Namespace:**
 [Grasshopper.Kernel.Undo](N_Grasshopper_Kernel_Undo.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public void AddAction(
	IGH_UndoAction action
)
```

```
Public Sub AddAction ( 
	action As IGH_UndoAction
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

action
:   Type: [Grasshopper.Kernel.UndoAddLanguageSpecificTextSet("LSTC079CE01\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");IGH\_UndoAction](T_Grasshopper_Kernel_Undo_IGH_UndoAction.htm)  
    Action to append.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_UndoRecord Class](T_Grasshopper_Kernel_Undo_GH_UndoRecord.htm)

[Grasshopper.Kernel.Undo Namespace](N_Grasshopper_Kernel_Undo.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)