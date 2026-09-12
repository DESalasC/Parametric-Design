# T_Grasshopper_Kernel_Undo_Actions_GH_LockedAction

﻿ GH\_LockedAction Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Undo.Actions](../html/N_Grasshopper_Kernel_Undo_Actions.htm "Grasshopper.Kernel.Undo.Actions")

[GH\_LockedAction Class](../html/T_Grasshopper_Kernel_Undo_Actions_GH_LockedAction.htm "GH_LockedAction Class")

[GH\_LockedAction Constructor](../html/M_Grasshopper_Kernel_Undo_Actions_GH_LockedAction__ctor.htm "GH_LockedAction Constructor ")

[GH\_LockedAction Properties](../html/Properties_T_Grasshopper_Kernel_Undo_Actions_GH_LockedAction.htm "GH_LockedAction Properties")

[GH\_LockedAction Methods](../html/Methods_T_Grasshopper_Kernel_Undo_Actions_GH_LockedAction.htm "GH_LockedAction Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_LockedAction Class |

Records a single object Enabled event.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST5CA8A366\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [Grasshopper.Kernel.UndoAddLanguageSpecificTextSet("LST5CA8A366\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_UndoAction](T_Grasshopper_Kernel_Undo_GH_UndoAction.htm)  
    [Grasshopper.Kernel.UndoAddLanguageSpecificTextSet("LST5CA8A366\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_ObjectUndoAction](T_Grasshopper_Kernel_Undo_GH_ObjectUndoAction.htm)  
      Grasshopper.Kernel.Undo.ActionsAddLanguageSpecificTextSet("LST5CA8A366\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_LockedAction

**Namespace:**
 [Grasshopper.Kernel.Undo.Actions](N_Grasshopper_Kernel_Undo_Actions.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_LockedAction : GH_ObjectUndoAction
```

```
Public Class GH_LockedAction
	Inherits GH_ObjectUndoAction
```

AddLanguageTabSet("ID1EBCA");

The GH\_LockedAction type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_LockedAction](M_Grasshopper_Kernel_Undo_Actions_GH_LockedAction__ctor.htm) | Initializes a new instance of the GH\_LockedAction class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [ExpiresDisplay](P_Grasshopper_Kernel_Undo_GH_UndoAction_ExpiresDisplay.htm) | Override this property if you want the Rhino viewport display to refresh upon undo completion. (Inherited from [GH\_UndoAction](T_Grasshopper_Kernel_Undo_GH_UndoAction.htm).) |
| Public property | [ExpiresSolution](P_Grasshopper_Kernel_Undo_Actions_GH_LockedAction_ExpiresSolution.htm) | (Overrides [GH\_UndoActionAddLanguageSpecificTextSet("LST5CA8A366\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");ExpiresSolution](P_Grasshopper_Kernel_Undo_GH_UndoAction_ExpiresSolution.htm).) |
| Public property | [State](P_Grasshopper_Kernel_Undo_GH_UndoAction_State.htm) | (Inherited from [GH\_UndoAction](T_Grasshopper_Kernel_Undo_GH_UndoAction.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Protected method | [Internal\_Redo](M_Grasshopper_Kernel_Undo_GH_ObjectUndoAction_Internal_Redo.htm) | (Inherited from [GH\_ObjectUndoAction](T_Grasshopper_Kernel_Undo_GH_ObjectUndoAction.htm).) |
| Protected method | [Internal\_Undo](M_Grasshopper_Kernel_Undo_GH_ObjectUndoAction_Internal_Undo.htm) | (Inherited from [GH\_ObjectUndoAction](T_Grasshopper_Kernel_Undo_GH_ObjectUndoAction.htm).) |
| Protected method | [Object\_Redo](M_Grasshopper_Kernel_Undo_Actions_GH_LockedAction_Object_Redo.htm) | (Overrides [GH\_ObjectUndoActionAddLanguageSpecificTextSet("LST5CA8A366\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");Object\_Redo(GH\_Document, IGH\_DocumentObject)](M_Grasshopper_Kernel_Undo_GH_ObjectUndoAction_Object_Redo.htm).) |
| Protected method | [Object\_Undo](M_Grasshopper_Kernel_Undo_Actions_GH_LockedAction_Object_Undo.htm) | (Overrides [GH\_ObjectUndoActionAddLanguageSpecificTextSet("LST5CA8A366\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");Object\_Undo(GH\_Document, IGH\_DocumentObject)](M_Grasshopper_Kernel_Undo_GH_ObjectUndoAction_Object_Undo.htm).) |
| Public method | [Read](M_Grasshopper_Kernel_Undo_GH_UndoAction_Read.htm) | (Inherited from [GH\_UndoAction](T_Grasshopper_Kernel_Undo_GH_UndoAction.htm).) |
| Public method | [Redo](M_Grasshopper_Kernel_Undo_GH_UndoAction_Redo.htm) | (Inherited from [GH\_UndoAction](T_Grasshopper_Kernel_Undo_GH_UndoAction.htm).) |
| Public method | [Undo](M_Grasshopper_Kernel_Undo_GH_UndoAction_Undo.htm) | (Inherited from [GH\_UndoAction](T_Grasshopper_Kernel_Undo_GH_UndoAction.htm).) |
| Public method | [Write](M_Grasshopper_Kernel_Undo_GH_UndoAction_Write.htm) | (Inherited from [GH\_UndoAction](T_Grasshopper_Kernel_Undo_GH_UndoAction.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Undo.Actions Namespace](N_Grasshopper_Kernel_Undo_Actions.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)