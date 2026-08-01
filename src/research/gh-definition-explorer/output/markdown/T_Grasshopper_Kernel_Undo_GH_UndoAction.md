# T_Grasshopper_Kernel_Undo_GH_UndoAction

﻿ GH\_UndoAction Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Undo](../html/N_Grasshopper_Kernel_Undo.htm "Grasshopper.Kernel.Undo")

[GH\_UndoAction Class](../html/T_Grasshopper_Kernel_Undo_GH_UndoAction.htm "GH_UndoAction Class")

[GH\_UndoAction Constructor](../html/M_Grasshopper_Kernel_Undo_GH_UndoAction__ctor.htm "GH_UndoAction Constructor ")

[GH\_UndoAction Properties](../html/Properties_T_Grasshopper_Kernel_Undo_GH_UndoAction.htm "GH_UndoAction Properties")

[GH\_UndoAction Methods](../html/Methods_T_Grasshopper_Kernel_Undo_GH_UndoAction.htm "GH_UndoAction Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_UndoAction Class |

Base class implementation for undo actions.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LSTFB929914\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.Kernel.UndoAddLanguageSpecificTextSet("LSTFB929914\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_UndoAction  
    [Grasshopper.Kernel.Undo.ActionsAddLanguageSpecificTextSet("LSTFB929914\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_AddObjectAction](T_Grasshopper_Kernel_Undo_Actions_GH_AddObjectAction.htm)  
    [Grasshopper.Kernel.Undo.ActionsAddLanguageSpecificTextSet("LSTFB929914\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_WireAction](T_Grasshopper_Kernel_Undo_Actions_GH_WireAction.htm)  
    [Grasshopper.Kernel.UndoAddLanguageSpecificTextSet("LSTFB929914\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_ArchivedUndoAction](T_Grasshopper_Kernel_Undo_GH_ArchivedUndoAction.htm)  
    [Grasshopper.Kernel.UndoAddLanguageSpecificTextSet("LSTFB929914\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_ObjectUndoAction](T_Grasshopper_Kernel_Undo_GH_ObjectUndoAction.htm)

**Namespace:**
 [Grasshopper.Kernel.Undo](N_Grasshopper_Kernel_Undo.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public abstract class GH_UndoAction : IGH_UndoAction
```

```
Public MustInherit Class GH_UndoAction
	Implements IGH_UndoAction
```

AddLanguageTabSet("ID1EBCA");

The GH\_UndoAction type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Protected method | [GH\_UndoAction](M_Grasshopper_Kernel_Undo_GH_UndoAction__ctor.htm) | Initializes a new instance of the GH\_UndoAction class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [ExpiresDisplay](P_Grasshopper_Kernel_Undo_GH_UndoAction_ExpiresDisplay.htm) | Override this property if you want the Rhino viewport display to refresh upon undo completion. |
| Public property | [ExpiresSolution](P_Grasshopper_Kernel_Undo_GH_UndoAction_ExpiresSolution.htm) | Override this property if you want the Grasshopper solution to refresh upon undo completion. |
| Public property | [State](P_Grasshopper_Kernel_Undo_GH_UndoAction_State.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Protected method | [Internal\_Redo](M_Grasshopper_Kernel_Undo_GH_UndoAction_Internal_Redo.htm) |  |
| Protected method | [Internal\_Undo](M_Grasshopper_Kernel_Undo_GH_UndoAction_Internal_Undo.htm) |  |
| Public method | [Read](M_Grasshopper_Kernel_Undo_GH_UndoAction_Read.htm) |  |
| Public method | [Redo](M_Grasshopper_Kernel_Undo_GH_UndoAction_Redo.htm) |  |
| Public method | [Undo](M_Grasshopper_Kernel_Undo_GH_UndoAction_Undo.htm) |  |
| Public method | [Write](M_Grasshopper_Kernel_Undo_GH_UndoAction_Write.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Undo Namespace](N_Grasshopper_Kernel_Undo.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)