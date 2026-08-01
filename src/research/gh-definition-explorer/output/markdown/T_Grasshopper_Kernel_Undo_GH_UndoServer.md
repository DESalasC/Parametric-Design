# T_Grasshopper_Kernel_Undo_GH_UndoServer

﻿ GH\_UndoServer Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Undo](../html/N_Grasshopper_Kernel_Undo.htm "Grasshopper.Kernel.Undo")

[GH\_UndoServer Class](../html/T_Grasshopper_Kernel_Undo_GH_UndoServer.htm "GH_UndoServer Class")

[GH\_UndoServer Constructor](../html/M_Grasshopper_Kernel_Undo_GH_UndoServer__ctor.htm "GH_UndoServer Constructor ")

[GH\_UndoServer Properties](../html/Properties_T_Grasshopper_Kernel_Undo_GH_UndoServer.htm "GH_UndoServer Properties")

[GH\_UndoServer Methods](../html/Methods_T_Grasshopper_Kernel_Undo_GH_UndoServer.htm "GH_UndoServer Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_UndoServer Class |

Provides access to a documents undo data.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST25976CEB\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.Kernel.UndoAddLanguageSpecificTextSet("LST25976CEB\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_UndoServer

**Namespace:**
 [Grasshopper.Kernel.Undo](N_Grasshopper_Kernel_Undo.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_UndoServer : IGH_DebugDescription
```

```
Public Class GH_UndoServer
	Implements IGH_DebugDescription
```

AddLanguageTabSet("ID1EBCA");

The GH\_UndoServer type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_UndoServer](M_Grasshopper_Kernel_Undo_GH_UndoServer__ctor.htm) | Initializes a new instance of the GH\_UndoServer class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [FirstRedoName](P_Grasshopper_Kernel_Undo_GH_UndoServer_FirstRedoName.htm) | Gets the name of the last item in the redo stack (the first item to be redone). |
| Public property | [FirstUndoName](P_Grasshopper_Kernel_Undo_GH_UndoServer_FirstUndoName.htm) | Gets the name of the last item in the undo stack (the first item to be undone). |
| Public property | [MaxRecords](P_Grasshopper_Kernel_Undo_GH_UndoServer_MaxRecords.htm) | Gets or sets the maximum number of undo records that can be stored. |
| Public property | [RedoCount](P_Grasshopper_Kernel_Undo_GH_UndoServer_RedoCount.htm) | Number of redo records currently in the stack. |
| Public property | [RedoGuids](P_Grasshopper_Kernel_Undo_GH_UndoServer_RedoGuids.htm) | Gets a sorted list of all the redo Guids in this server. |
| Public property | [RedoNames](P_Grasshopper_Kernel_Undo_GH_UndoServer_RedoNames.htm) | Gets a sorted list of all the redo Guids in this server. |
| Public property | [UndoCount](P_Grasshopper_Kernel_Undo_GH_UndoServer_UndoCount.htm) | Number of undo records currently in the stack. |
| Public property | [UndoGuids](P_Grasshopper_Kernel_Undo_GH_UndoServer_UndoGuids.htm) | Gets a sorted list of all the undo Guids in this server. |
| Public property | [UndoNames](P_Grasshopper_Kernel_Undo_GH_UndoServer_UndoNames.htm) | Gets a sorted list of all the undo Guids in this server. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [AppendToDebugLog](M_Grasshopper_Kernel_Undo_GH_UndoServer_AppendToDebugLog.htm) |  |
| Public method | [Clear](M_Grasshopper_Kernel_Undo_GH_UndoServer_Clear.htm) | Clear both undo and redo lists. |
| Public method | [ClearRedo](M_Grasshopper_Kernel_Undo_GH_UndoServer_ClearRedo.htm) | Clear the undo list. |
| Public method | [ClearUndo](M_Grasshopper_Kernel_Undo_GH_UndoServer_ClearUndo.htm) | Clear the redo list. |
| Public method | [MergeRecords](M_Grasshopper_Kernel_Undo_GH_UndoServer_MergeRecords.htm) | Attempt to merge the N most recent records into one. The name of the merged record will be identical to the name of the oldest record. |
| Public method | [PerformRedo](M_Grasshopper_Kernel_Undo_GH_UndoServer_PerformRedo.htm) | Performs a single Redo step if possible and migrates the record onto the undo stack. This function may throw all kinds of exceptions, if you're calling it from a UI thread, use a Try..Catch block to prevent crashes. |
| Public method | [PerformUndo](M_Grasshopper_Kernel_Undo_GH_UndoServer_PerformUndo.htm) | Performs a single Undo step when possible and migrates the record onto the redo stack. This function may throw all kinds of exceptions, if you're calling it from a UI thread, use a Try..Catch block to prevent crashes. |
| Public method | [PushUndoRecord(GH\_UndoRecord)](M_Grasshopper_Kernel_Undo_GH_UndoServer_PushUndoRecord.htm) | Add a new undo record to the undo stack, this function clears the Redo stack. |
| Public method | [PushUndoRecord(String, GH\_UndoAction)](M_Grasshopper_Kernel_Undo_GH_UndoServer_PushUndoRecord_1.htm) | Add a new undo record to the undo stack, this function clears the Redo stack. |
| Public method | [RemoveRecord](M_Grasshopper_Kernel_Undo_GH_UndoServer_RemoveRecord.htm) | Remove the record with the specified ID from the undo or redo stack. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Undo Namespace](N_Grasshopper_Kernel_Undo.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)