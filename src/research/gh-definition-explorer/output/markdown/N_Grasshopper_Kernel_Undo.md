# N_Grasshopper_Kernel_Undo

﻿ Grasshopper.Kernel.Undo Namespace

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Undo](../html/N_Grasshopper_Kernel_Undo.htm "Grasshopper.Kernel.Undo")

[GH\_ArchivedUndoAction Class](../html/T_Grasshopper_Kernel_Undo_GH_ArchivedUndoAction.htm "GH_ArchivedUndoAction Class")

[GH\_ObjectUndoAction Class](../html/T_Grasshopper_Kernel_Undo_GH_ObjectUndoAction.htm "GH_ObjectUndoAction Class")

[GH\_UndoAction Class](../html/T_Grasshopper_Kernel_Undo_GH_UndoAction.htm "GH_UndoAction Class")

[GH\_UndoException Class](../html/T_Grasshopper_Kernel_Undo_GH_UndoException.htm "GH_UndoException Class")

[GH\_UndoRecord Class](../html/T_Grasshopper_Kernel_Undo_GH_UndoRecord.htm "GH_UndoRecord Class")

[GH\_UndoServer Class](../html/T_Grasshopper_Kernel_Undo_GH_UndoServer.htm "GH_UndoServer Class")

[GH\_UndoState Enumeration](../html/T_Grasshopper_Kernel_Undo_GH_UndoState.htm "GH_UndoState Enumeration")

[IGH\_UndoAction Interface](../html/T_Grasshopper_Kernel_Undo_IGH_UndoAction.htm "IGH_UndoAction Interface")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| Grasshopper.Kernel.Undo Namespace |

Namespace that contains all the types and methods to do with the recording and re-instating GHX undo/redo data.

![](../icons/SectionExpanded.png)Classes

|  | Class | Description |
| --- | --- | --- |
| Public class | [GH\_ArchivedUndoAction](T_Grasshopper_Kernel_Undo_GH_ArchivedUndoAction.htm) | Base class implementation for undo actions that require (de)serialization of data. |
| Public class | [GH\_ObjectUndoAction](T_Grasshopper_Kernel_Undo_GH_ObjectUndoAction.htm) | Utility base class for undo actions that operate on a single IGH\_DocumentObject. |
| Public class | [GH\_UndoAction](T_Grasshopper_Kernel_Undo_GH_UndoAction.htm) | Base class implementation for undo actions. |
| Public class | [GH\_UndoException](T_Grasshopper_Kernel_Undo_GH_UndoException.htm) | Exception associated with undo events |
| Public class | [GH\_UndoRecord](T_Grasshopper_Kernel_Undo_GH_UndoRecord.htm) | Represents a single undo/redo record. A single record may contain any number of undo actions. |
| Public class | [GH\_UndoServer](T_Grasshopper_Kernel_Undo_GH_UndoServer.htm) | Provides access to a documents undo data. |

![](../icons/SectionExpanded.png)Interfaces

|  | Interface | Description |
| --- | --- | --- |
| Public interface | [IGH\_UndoAction](T_Grasshopper_Kernel_Undo_IGH_UndoAction.htm) | Base interface for all undo/redo actions |

![](../icons/SectionExpanded.png)Enumerations

|  | Enumeration | Description |
| --- | --- | --- |
| Public enumeration | [GH\_UndoState](T_Grasshopper_Kernel_Undo_GH_UndoState.htm) | State enumeration for undo records. |

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)