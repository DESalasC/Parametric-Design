# T_Grasshopper_Kernel_Undo_GH_ArchivedUndoAction

﻿ GH\_ArchivedUndoAction Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Undo](../html/N_Grasshopper_Kernel_Undo.htm "Grasshopper.Kernel.Undo")

[GH\_ArchivedUndoAction Class](../html/T_Grasshopper_Kernel_Undo_GH_ArchivedUndoAction.htm "GH_ArchivedUndoAction Class")

[GH\_ArchivedUndoAction Constructor](../html/M_Grasshopper_Kernel_Undo_GH_ArchivedUndoAction__ctor.htm "GH_ArchivedUndoAction Constructor ")

[GH\_ArchivedUndoAction Properties](../html/Properties_T_Grasshopper_Kernel_Undo_GH_ArchivedUndoAction.htm "GH_ArchivedUndoAction Properties")

[GH\_ArchivedUndoAction Methods](../html/Methods_T_Grasshopper_Kernel_Undo_GH_ArchivedUndoAction.htm "GH_ArchivedUndoAction Methods")

[GH\_ArchivedUndoAction Fields](../html/Fields_T_Grasshopper_Kernel_Undo_GH_ArchivedUndoAction.htm "GH_ArchivedUndoAction Fields")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ArchivedUndoAction Class |

Base class implementation for undo actions that require (de)serialization of data.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST41AA775\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [Grasshopper.Kernel.UndoAddLanguageSpecificTextSet("LST41AA775\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_UndoAction](T_Grasshopper_Kernel_Undo_GH_UndoAction.htm)  
    Grasshopper.Kernel.UndoAddLanguageSpecificTextSet("LST41AA775\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_ArchivedUndoAction  
      [Grasshopper.Kernel.Undo.ActionsAddLanguageSpecificTextSet("LST41AA775\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_AddStateAction](T_Grasshopper_Kernel_Undo_Actions_GH_AddStateAction.htm)  
      [Grasshopper.Kernel.Undo.ActionsAddLanguageSpecificTextSet("LST41AA775\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_GenericObjectAction](T_Grasshopper_Kernel_Undo_Actions_GH_GenericObjectAction.htm)  
      [Grasshopper.Kernel.Undo.ActionsAddLanguageSpecificTextSet("LST41AA775\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_RemoveObjectAction](T_Grasshopper_Kernel_Undo_Actions_GH_RemoveObjectAction.htm)  
      [Grasshopper.Kernel.Undo.ActionsAddLanguageSpecificTextSet("LST41AA775\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_RemoveStateAction](T_Grasshopper_Kernel_Undo_Actions_GH_RemoveStateAction.htm)

**Namespace:**
 [Grasshopper.Kernel.Undo](N_Grasshopper_Kernel_Undo.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public abstract class GH_ArchivedUndoAction : GH_UndoAction
```

```
Public MustInherit Class GH_ArchivedUndoAction
	Inherits GH_UndoAction
```

AddLanguageTabSet("ID1EBCA");

The GH\_ArchivedUndoAction type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Protected method | [GH\_ArchivedUndoAction](M_Grasshopper_Kernel_Undo_GH_ArchivedUndoAction__ctor.htm) | Initializes a new instance of the GH\_ArchivedUndoAction class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [ExpiresDisplay](P_Grasshopper_Kernel_Undo_GH_UndoAction_ExpiresDisplay.htm) | Override this property if you want the Rhino viewport display to refresh upon undo completion. (Inherited from [GH\_UndoAction](T_Grasshopper_Kernel_Undo_GH_UndoAction.htm).) |
| Public property | [ExpiresSolution](P_Grasshopper_Kernel_Undo_GH_UndoAction_ExpiresSolution.htm) | Override this property if you want the Grasshopper solution to refresh upon undo completion. (Inherited from [GH\_UndoAction](T_Grasshopper_Kernel_Undo_GH_UndoAction.htm).) |
| Public property | [State](P_Grasshopper_Kernel_Undo_GH_UndoAction_State.htm) | (Inherited from [GH\_UndoAction](T_Grasshopper_Kernel_Undo_GH_UndoAction.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Protected method | [Deserialize](M_Grasshopper_Kernel_Undo_GH_ArchivedUndoAction_Deserialize.htm) | Deserializes the obj from the local archive. |
| Protected method | [Internal\_Redo](M_Grasshopper_Kernel_Undo_GH_UndoAction_Internal_Redo.htm) | (Inherited from [GH\_UndoAction](T_Grasshopper_Kernel_Undo_GH_UndoAction.htm).) |
| Protected method | [Internal\_Undo](M_Grasshopper_Kernel_Undo_GH_UndoAction_Internal_Undo.htm) | (Inherited from [GH\_UndoAction](T_Grasshopper_Kernel_Undo_GH_UndoAction.htm).) |
| Public method | [Read](M_Grasshopper_Kernel_Undo_GH_ArchivedUndoAction_Read.htm) | (Overrides [GH\_UndoActionAddLanguageSpecificTextSet("LST41AA775\_7?cs=.|vb=.|cpp=::|nu=.|fs=.");Read(GH\_IReader)](M_Grasshopper_Kernel_Undo_GH_UndoAction_Read.htm).) |
| Public method | [Redo](M_Grasshopper_Kernel_Undo_GH_UndoAction_Redo.htm) | (Inherited from [GH\_UndoAction](T_Grasshopper_Kernel_Undo_GH_UndoAction.htm).) |
| Protected method | [Serialize](M_Grasshopper_Kernel_Undo_GH_ArchivedUndoAction_Serialize.htm) | Serializes the obj into the local archive. |
| Protected method | [SerializeToByteArray](M_Grasshopper_Kernel_Undo_GH_ArchivedUndoAction_SerializeToByteArray.htm) | Serializes the obj into the local archive. |
| Public method | [Undo](M_Grasshopper_Kernel_Undo_GH_UndoAction_Undo.htm) | (Inherited from [GH\_UndoAction](T_Grasshopper_Kernel_Undo_GH_UndoAction.htm).) |
| Public method | [Write](M_Grasshopper_Kernel_Undo_GH_ArchivedUndoAction_Write.htm) | (Overrides [GH\_UndoActionAddLanguageSpecificTextSet("LST41AA775\_8?cs=.|vb=.|cpp=::|nu=.|fs=.");Write(GH\_IWriter)](M_Grasshopper_Kernel_Undo_GH_UndoAction_Write.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Fields

|  | Name | Description |
| --- | --- | --- |
| Protected field | [m\_data](F_Grasshopper_Kernel_Undo_GH_ArchivedUndoAction_m_data.htm) | Internal data storage for serialized archives. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Undo Namespace](N_Grasshopper_Kernel_Undo.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)