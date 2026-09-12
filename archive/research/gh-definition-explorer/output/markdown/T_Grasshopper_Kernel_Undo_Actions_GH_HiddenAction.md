# T_Grasshopper_Kernel_Undo_Actions_GH_HiddenAction

﻿ GH\_HiddenAction Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Undo.Actions](../html/N_Grasshopper_Kernel_Undo_Actions.htm "Grasshopper.Kernel.Undo.Actions")

[GH\_HiddenAction Class](../html/T_Grasshopper_Kernel_Undo_Actions_GH_HiddenAction.htm "GH_HiddenAction Class")

[GH\_HiddenAction Constructor](../html/M_Grasshopper_Kernel_Undo_Actions_GH_HiddenAction__ctor.htm "GH_HiddenAction Constructor ")

[GH\_HiddenAction Properties](../html/Properties_T_Grasshopper_Kernel_Undo_Actions_GH_HiddenAction.htm "GH_HiddenAction Properties")

[GH\_HiddenAction Methods](../html/Methods_T_Grasshopper_Kernel_Undo_Actions_GH_HiddenAction.htm "GH_HiddenAction Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_HiddenAction Class |

Records a single object Preview event.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST696A4075\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [Grasshopper.Kernel.UndoAddLanguageSpecificTextSet("LST696A4075\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_UndoAction](T_Grasshopper_Kernel_Undo_GH_UndoAction.htm)  
    [Grasshopper.Kernel.UndoAddLanguageSpecificTextSet("LST696A4075\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_ObjectUndoAction](T_Grasshopper_Kernel_Undo_GH_ObjectUndoAction.htm)  
      Grasshopper.Kernel.Undo.ActionsAddLanguageSpecificTextSet("LST696A4075\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_HiddenAction

**Namespace:**
 [Grasshopper.Kernel.Undo.Actions](N_Grasshopper_Kernel_Undo_Actions.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_HiddenAction : GH_ObjectUndoAction
```

```
Public Class GH_HiddenAction
	Inherits GH_ObjectUndoAction
```

AddLanguageTabSet("ID1EBCA");

The GH\_HiddenAction type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_HiddenAction](M_Grasshopper_Kernel_Undo_Actions_GH_HiddenAction__ctor.htm) | Initializes a new instance of the GH\_HiddenAction class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [ExpiresDisplay](P_Grasshopper_Kernel_Undo_Actions_GH_HiddenAction_ExpiresDisplay.htm) | (Overrides [GH\_UndoActionAddLanguageSpecificTextSet("LST696A4075\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");ExpiresDisplay](P_Grasshopper_Kernel_Undo_GH_UndoAction_ExpiresDisplay.htm).) |
| Public property | [ExpiresSolution](P_Grasshopper_Kernel_Undo_GH_UndoAction_ExpiresSolution.htm) | Override this property if you want the Grasshopper solution to refresh upon undo completion. (Inherited from [GH\_UndoAction](T_Grasshopper_Kernel_Undo_GH_UndoAction.htm).) |
| Public property | [State](P_Grasshopper_Kernel_Undo_GH_UndoAction_State.htm) | (Inherited from [GH\_UndoAction](T_Grasshopper_Kernel_Undo_GH_UndoAction.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Protected method | [Internal\_Redo](M_Grasshopper_Kernel_Undo_GH_ObjectUndoAction_Internal_Redo.htm) | (Inherited from [GH\_ObjectUndoAction](T_Grasshopper_Kernel_Undo_GH_ObjectUndoAction.htm).) |
| Protected method | [Internal\_Undo](M_Grasshopper_Kernel_Undo_GH_ObjectUndoAction_Internal_Undo.htm) | (Inherited from [GH\_ObjectUndoAction](T_Grasshopper_Kernel_Undo_GH_ObjectUndoAction.htm).) |
| Protected method | [Object\_Redo](M_Grasshopper_Kernel_Undo_Actions_GH_HiddenAction_Object_Redo.htm) | (Overrides [GH\_ObjectUndoActionAddLanguageSpecificTextSet("LST696A4075\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");Object\_Redo(GH\_Document, IGH\_DocumentObject)](M_Grasshopper_Kernel_Undo_GH_ObjectUndoAction_Object_Redo.htm).) |
| Protected method | [Object\_Undo](M_Grasshopper_Kernel_Undo_Actions_GH_HiddenAction_Object_Undo.htm) | (Overrides [GH\_ObjectUndoActionAddLanguageSpecificTextSet("LST696A4075\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");Object\_Undo(GH\_Document, IGH\_DocumentObject)](M_Grasshopper_Kernel_Undo_GH_ObjectUndoAction_Object_Undo.htm).) |
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