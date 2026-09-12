# T_Grasshopper_Kernel_Undo_GH_UndoRecord

﻿ GH\_UndoRecord Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Undo](../html/N_Grasshopper_Kernel_Undo.htm "Grasshopper.Kernel.Undo")

[GH\_UndoRecord Class](../html/T_Grasshopper_Kernel_Undo_GH_UndoRecord.htm "GH_UndoRecord Class")

[GH\_UndoRecord Constructor](../html/Overload_Grasshopper_Kernel_Undo_GH_UndoRecord__ctor.htm "GH_UndoRecord Constructor ")

[GH\_UndoRecord Properties](../html/Properties_T_Grasshopper_Kernel_Undo_GH_UndoRecord.htm "GH_UndoRecord Properties")

[GH\_UndoRecord Methods](../html/Methods_T_Grasshopper_Kernel_Undo_GH_UndoRecord.htm "GH_UndoRecord Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_UndoRecord Class |

Represents a single undo/redo record. A single record may contain any number of undo actions.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST81A4CD7E\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.Kernel.UndoAddLanguageSpecificTextSet("LST81A4CD7E\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_UndoRecord

**Namespace:**
 [Grasshopper.Kernel.Undo](N_Grasshopper_Kernel_Undo.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_UndoRecord
```

```
Public Class GH_UndoRecord
```

AddLanguageTabSet("ID1EBCA");

The GH\_UndoRecord type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_UndoRecordAddLanguageSpecificTextSet("LST81A4CD7E\_2?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Undo_GH_UndoRecord__ctor.htm) | Initializes a new instance of the GH\_UndoRecord class |
| Public method | [GH\_UndoRecord(String)](M_Grasshopper_Kernel_Undo_GH_UndoRecord__ctor_1.htm) | Initializes a new instance of the GH\_UndoRecord class |
| Public method | [GH\_UndoRecord(String, IGH\_UndoAction)](M_Grasshopper_Kernel_Undo_GH_UndoRecord__ctor_2.htm) | Initializes a new instance of the GH\_UndoRecord class |
| Public method | [GH\_UndoRecord(String, AddLanguageSpecificTextSet("LST81A4CD7E\_3?cpp=array&lt;");IGH\_UndoActionAddLanguageSpecificTextSet("LST81A4CD7E\_4?cpp=&gt;|cs=[]|vb=()|nu=[]|fs=[]");)](M_Grasshopper_Kernel_Undo_GH_UndoRecord__ctor_3.htm) | Initializes a new instance of the GH\_UndoRecord class |
| Public method | [GH\_UndoRecord(String, IEnumerableAddLanguageSpecificTextSet("LST81A4CD7E\_5?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");IGH\_UndoActionAddLanguageSpecificTextSet("LST81A4CD7E\_6?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");)](M_Grasshopper_Kernel_Undo_GH_UndoRecord__ctor_4.htm) | Initializes a new instance of the GH\_UndoRecord class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [ActionCount](P_Grasshopper_Kernel_Undo_GH_UndoRecord_ActionCount.htm) | Gets the number of actions stored in this record. |
| Public property | [Actions](P_Grasshopper_Kernel_Undo_GH_UndoRecord_Actions.htm) | Gets or sets the actions inside this record. |
| Public property | [ExpiresDisplay](P_Grasshopper_Kernel_Undo_GH_UndoRecord_ExpiresDisplay.htm) | Gets the display expiration flag for this event. If True, the Rhino viewports will be redrawn once the entire undo record has been completed. If ExpiresSolution is set to true, ExpriresDisplay is implied. |
| Public property | [ExpiresSolution](P_Grasshopper_Kernel_Undo_GH_UndoRecord_ExpiresSolution.htm) | Gets the solution expiration flag for this event. If True, the solution needs to be recalculated once the entire undo record has been completed. |
| Public property | [Guid](P_Grasshopper_Kernel_Undo_GH_UndoRecord_Guid.htm) | Gets the ID of this undo item. Every undo record has a unique ID. |
| Public property | [Name](P_Grasshopper_Kernel_Undo_GH_UndoRecord_Name.htm) | Gets or sets the name of the undo record (as displayed in the menu) |
| Public property | [State](P_Grasshopper_Kernel_Undo_GH_UndoRecord_State.htm) | Gets the undo state of this record. The state dictates which action are legal. |
| Public property | [Time](P_Grasshopper_Kernel_Undo_GH_UndoRecord_Time.htm) | Gets the time at which this record was created. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [AddAction](M_Grasshopper_Kernel_Undo_GH_UndoRecord_AddAction.htm) | Append an undo action to this record. You should only do this prior to calling undo for the first time. |
| Public method | [Redo](M_Grasshopper_Kernel_Undo_GH_UndoRecord_Redo.htm) |  |
| Public method | [Undo](M_Grasshopper_Kernel_Undo_GH_UndoRecord_Undo.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Undo Namespace](N_Grasshopper_Kernel_Undo.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)