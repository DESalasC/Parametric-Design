# T_Grasshopper_Kernel_Undo_Actions_GH_RemoveObjectAction

﻿ GH\_RemoveObjectAction Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Undo.Actions](../html/N_Grasshopper_Kernel_Undo_Actions.htm "Grasshopper.Kernel.Undo.Actions")

[GH\_RemoveObjectAction Class](../html/T_Grasshopper_Kernel_Undo_Actions_GH_RemoveObjectAction.htm "GH_RemoveObjectAction Class")

[GH\_RemoveObjectAction Constructor](../html/M_Grasshopper_Kernel_Undo_Actions_GH_RemoveObjectAction__ctor.htm "GH_RemoveObjectAction Constructor ")

[GH\_RemoveObjectAction Properties](../html/Properties_T_Grasshopper_Kernel_Undo_Actions_GH_RemoveObjectAction.htm "GH_RemoveObjectAction Properties")

[GH\_RemoveObjectAction Methods](../html/Methods_T_Grasshopper_Kernel_Undo_Actions_GH_RemoveObjectAction.htm "GH_RemoveObjectAction Methods")

[GH\_RemoveObjectAction Fields](../html/Fields_T_Grasshopper_Kernel_Undo_Actions_GH_RemoveObjectAction.htm "GH_RemoveObjectAction Fields")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_RemoveObjectAction Class |

Records a single object removal.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST22FC4904\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [Grasshopper.Kernel.UndoAddLanguageSpecificTextSet("LST22FC4904\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_UndoAction](T_Grasshopper_Kernel_Undo_GH_UndoAction.htm)  
    [Grasshopper.Kernel.UndoAddLanguageSpecificTextSet("LST22FC4904\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_ArchivedUndoAction](T_Grasshopper_Kernel_Undo_GH_ArchivedUndoAction.htm)  
      Grasshopper.Kernel.Undo.ActionsAddLanguageSpecificTextSet("LST22FC4904\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_RemoveObjectAction

**Namespace:**
 [Grasshopper.Kernel.Undo.Actions](N_Grasshopper_Kernel_Undo_Actions.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_RemoveObjectAction : GH_ArchivedUndoAction
```

```
Public Class GH_RemoveObjectAction
	Inherits GH_ArchivedUndoAction
```

AddLanguageTabSet("ID1EBCA");

The GH\_RemoveObjectAction type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_RemoveObjectAction](M_Grasshopper_Kernel_Undo_Actions_GH_RemoveObjectAction__ctor.htm) | Initializes a new instance of the GH\_RemoveObjectAction class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [ExpiresDisplay](P_Grasshopper_Kernel_Undo_GH_UndoAction_ExpiresDisplay.htm) | Override this property if you want the Rhino viewport display to refresh upon undo completion. (Inherited from [GH\_UndoAction](T_Grasshopper_Kernel_Undo_GH_UndoAction.htm).) |
| Public property | [ExpiresSolution](P_Grasshopper_Kernel_Undo_Actions_GH_RemoveObjectAction_ExpiresSolution.htm) | (Overrides [GH\_UndoActionAddLanguageSpecificTextSet("LST22FC4904\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");ExpiresSolution](P_Grasshopper_Kernel_Undo_GH_UndoAction_ExpiresSolution.htm).) |
| Public property | [State](P_Grasshopper_Kernel_Undo_GH_UndoAction_State.htm) | (Inherited from [GH\_UndoAction](T_Grasshopper_Kernel_Undo_GH_UndoAction.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Protected method | [Deserialize](M_Grasshopper_Kernel_Undo_GH_ArchivedUndoAction_Deserialize.htm) | Deserializes the obj from the local archive. (Inherited from [GH\_ArchivedUndoAction](T_Grasshopper_Kernel_Undo_GH_ArchivedUndoAction.htm).) |
| Protected method | [Internal\_Redo](M_Grasshopper_Kernel_Undo_Actions_GH_RemoveObjectAction_Internal_Redo.htm) | (Overrides [GH\_UndoActionAddLanguageSpecificTextSet("LST22FC4904\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");Internal\_Redo(GH\_Document)](M_Grasshopper_Kernel_Undo_GH_UndoAction_Internal_Redo.htm).) |
| Protected method | [Internal\_Undo](M_Grasshopper_Kernel_Undo_Actions_GH_RemoveObjectAction_Internal_Undo.htm) | (Overrides [GH\_UndoActionAddLanguageSpecificTextSet("LST22FC4904\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");Internal\_Undo(GH\_Document)](M_Grasshopper_Kernel_Undo_GH_UndoAction_Internal_Undo.htm).) |
| Public method | [Read](M_Grasshopper_Kernel_Undo_GH_ArchivedUndoAction_Read.htm) | (Inherited from [GH\_ArchivedUndoAction](T_Grasshopper_Kernel_Undo_GH_ArchivedUndoAction.htm).) |
| Public method | [Redo](M_Grasshopper_Kernel_Undo_GH_UndoAction_Redo.htm) | (Inherited from [GH\_UndoAction](T_Grasshopper_Kernel_Undo_GH_UndoAction.htm).) |
| Protected method | [Serialize](M_Grasshopper_Kernel_Undo_GH_ArchivedUndoAction_Serialize.htm) | Serializes the obj into the local archive. (Inherited from [GH\_ArchivedUndoAction](T_Grasshopper_Kernel_Undo_GH_ArchivedUndoAction.htm).) |
| Protected method | [SerializeToByteArray](M_Grasshopper_Kernel_Undo_GH_ArchivedUndoAction_SerializeToByteArray.htm) | Serializes the obj into the local archive. (Inherited from [GH\_ArchivedUndoAction](T_Grasshopper_Kernel_Undo_GH_ArchivedUndoAction.htm).) |
| Public method | [Undo](M_Grasshopper_Kernel_Undo_GH_UndoAction_Undo.htm) | (Inherited from [GH\_UndoAction](T_Grasshopper_Kernel_Undo_GH_UndoAction.htm).) |
| Public method | [Write](M_Grasshopper_Kernel_Undo_GH_ArchivedUndoAction_Write.htm) | (Inherited from [GH\_ArchivedUndoAction](T_Grasshopper_Kernel_Undo_GH_ArchivedUndoAction.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Fields

|  | Name | Description |
| --- | --- | --- |
| Protected field | [m\_data](F_Grasshopper_Kernel_Undo_GH_ArchivedUndoAction_m_data.htm) | Internal data storage for serialized archives. (Inherited from [GH\_ArchivedUndoAction](T_Grasshopper_Kernel_Undo_GH_ArchivedUndoAction.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Undo.Actions Namespace](N_Grasshopper_Kernel_Undo_Actions.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)