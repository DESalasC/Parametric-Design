# M_Grasshopper_Kernel_Undo_IGH_UndoAction_Redo

﻿ IGH\_UndoAction.Redo Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Undo](../html/N_Grasshopper_Kernel_Undo.htm "Grasshopper.Kernel.Undo")

[IGH\_UndoAction Interface](../html/T_Grasshopper_Kernel_Undo_IGH_UndoAction.htm "IGH_UndoAction Interface")

[IGH\_UndoAction Methods](../html/Methods_T_Grasshopper_Kernel_Undo_IGH_UndoAction.htm "IGH_UndoAction Methods")

[Redo Method](../html/M_Grasshopper_Kernel_Undo_IGH_UndoAction_Redo.htm "Redo Method ")

[Undo Method](../html/M_Grasshopper_Kernel_Undo_IGH_UndoAction_Undo.htm "Undo Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_UndoActionAddLanguageSpecificTextSet("LSTFF69166D\_0?cpp=::|nu=.");Redo Method |

Redo the action stored in this record.

**Namespace:**
 [Grasshopper.Kernel.Undo](N_Grasshopper_Kernel_Undo.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
void Redo(
	GH_Document doc
)
```

```
Sub Redo ( 
	doc As GH_Document
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

doc
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LSTFF69166D\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Document](T_Grasshopper_Kernel_GH_Document.htm)  
    The target document.

![](../icons/SectionExpanded.png)Exceptions

| Exception | Condition |
| --- | --- |
| [GH\_UndoException](T_Grasshopper_Kernel_Undo_GH_UndoException.htm) | Thrown when the State flag conflicts with a redo action. |

![](../icons/SectionExpanded.png)See Also

#### Reference

[IGH\_UndoAction Interface](T_Grasshopper_Kernel_Undo_IGH_UndoAction.htm)

[Grasshopper.Kernel.Undo Namespace](N_Grasshopper_Kernel_Undo.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)