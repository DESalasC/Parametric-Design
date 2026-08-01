# T_Grasshopper_Kernel_Undo_IGH_UndoAction

﻿ IGH\_UndoAction Interface

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Undo](../html/N_Grasshopper_Kernel_Undo.htm "Grasshopper.Kernel.Undo")

[IGH\_UndoAction Interface](../html/T_Grasshopper_Kernel_Undo_IGH_UndoAction.htm "IGH_UndoAction Interface")

[IGH\_UndoAction Properties](../html/Properties_T_Grasshopper_Kernel_Undo_IGH_UndoAction.htm "IGH_UndoAction Properties")

[IGH\_UndoAction Methods](../html/Methods_T_Grasshopper_Kernel_Undo_IGH_UndoAction.htm "IGH_UndoAction Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_UndoAction Interface |

Base interface for all undo/redo actions

**Namespace:**
 [Grasshopper.Kernel.Undo](N_Grasshopper_Kernel_Undo.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public interface IGH_UndoAction : GH_ISerializable
```

```
Public Interface IGH_UndoAction
	Inherits GH_ISerializable
```

AddLanguageTabSet("ID0EBCA");

The IGH\_UndoAction type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [ExpiresDisplay](P_Grasshopper_Kernel_Undo_IGH_UndoAction_ExpiresDisplay.htm) | Gets the display expiration flag for this event. If True, the Rhino viewports will be redrawn once the entire undo record has been completed. If ExpiresSolution is set to true, ExpriresDisplay is implied. |
| Public property | [ExpiresSolution](P_Grasshopper_Kernel_Undo_IGH_UndoAction_ExpiresSolution.htm) | Gets the solution expiration flag for this event. If True, the solution needs to be recalculated once the entire undo record has been completed. |
| Public property | [State](P_Grasshopper_Kernel_Undo_IGH_UndoAction_State.htm) | Gets the current state of the undo action. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [Read](M_GH_IO_GH_ISerializable_Read.htm) | This method is called whenever the instance is required to deserialize itself. (Inherited from [GH\_ISerializable](T_GH_IO_GH_ISerializable.htm).) |
| Public method | [Redo](M_Grasshopper_Kernel_Undo_IGH_UndoAction_Redo.htm) | Redo the action stored in this record. |
| Public method | [Undo](M_Grasshopper_Kernel_Undo_IGH_UndoAction_Undo.htm) | Undo the action stored in this record. |
| Public method | [Write](M_GH_IO_GH_ISerializable_Write.htm) | This method is called whenever the instance is required to serialize itself. (Inherited from [GH\_ISerializable](T_GH_IO_GH_ISerializable.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Undo Namespace](N_Grasshopper_Kernel_Undo.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)