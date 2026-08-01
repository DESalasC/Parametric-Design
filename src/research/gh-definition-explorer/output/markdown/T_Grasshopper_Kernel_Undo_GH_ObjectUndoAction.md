# T_Grasshopper_Kernel_Undo_GH_ObjectUndoAction

﻿ GH\_ObjectUndoAction Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Undo](../html/N_Grasshopper_Kernel_Undo.htm "Grasshopper.Kernel.Undo")

[GH\_ObjectUndoAction Class](../html/T_Grasshopper_Kernel_Undo_GH_ObjectUndoAction.htm "GH_ObjectUndoAction Class")

[GH\_ObjectUndoAction Constructor](../html/M_Grasshopper_Kernel_Undo_GH_ObjectUndoAction__ctor.htm "GH_ObjectUndoAction Constructor ")

[GH\_ObjectUndoAction Properties](../html/Properties_T_Grasshopper_Kernel_Undo_GH_ObjectUndoAction.htm "GH_ObjectUndoAction Properties")

[GH\_ObjectUndoAction Methods](../html/Methods_T_Grasshopper_Kernel_Undo_GH_ObjectUndoAction.htm "GH_ObjectUndoAction Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ObjectUndoAction Class |

Utility base class for undo actions that operate on a single IGH\_DocumentObject.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST60D4F573\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [Grasshopper.Kernel.UndoAddLanguageSpecificTextSet("LST60D4F573\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_UndoAction](T_Grasshopper_Kernel_Undo_GH_UndoAction.htm)  
    Grasshopper.Kernel.UndoAddLanguageSpecificTextSet("LST60D4F573\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_ObjectUndoAction  
      [More...](#fullInheritance)

**Namespace:**
 [Grasshopper.Kernel.Undo](N_Grasshopper_Kernel_Undo.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public abstract class GH_ObjectUndoAction : GH_UndoAction
```

```
Public MustInherit Class GH_ObjectUndoAction
	Inherits GH_UndoAction
```

AddLanguageTabSet("ID1EBCA");

The GH\_ObjectUndoAction type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Protected method | [GH\_ObjectUndoAction](M_Grasshopper_Kernel_Undo_GH_ObjectUndoAction__ctor.htm) | Initializes a new instance of the GH\_ObjectUndoAction class |

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
| Protected method | [Internal\_Redo](M_Grasshopper_Kernel_Undo_GH_ObjectUndoAction_Internal_Redo.htm) | (Overrides [GH\_UndoActionAddLanguageSpecificTextSet("LST60D4F573\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Internal\_Redo(GH\_Document)](M_Grasshopper_Kernel_Undo_GH_UndoAction_Internal_Redo.htm).) |
| Protected method | [Internal\_Undo](M_Grasshopper_Kernel_Undo_GH_ObjectUndoAction_Internal_Undo.htm) | (Overrides [GH\_UndoActionAddLanguageSpecificTextSet("LST60D4F573\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");Internal\_Undo(GH\_Document)](M_Grasshopper_Kernel_Undo_GH_UndoAction_Internal_Undo.htm).) |
| Protected method | [Object\_Redo](M_Grasshopper_Kernel_Undo_GH_ObjectUndoAction_Object_Redo.htm) |  |
| Protected method | [Object\_Undo](M_Grasshopper_Kernel_Undo_GH_ObjectUndoAction_Object_Undo.htm) |  |
| Public method | [Read](M_Grasshopper_Kernel_Undo_GH_UndoAction_Read.htm) | (Inherited from [GH\_UndoAction](T_Grasshopper_Kernel_Undo_GH_UndoAction.htm).) |
| Public method | [Redo](M_Grasshopper_Kernel_Undo_GH_UndoAction_Redo.htm) | (Inherited from [GH\_UndoAction](T_Grasshopper_Kernel_Undo_GH_UndoAction.htm).) |
| Public method | [Undo](M_Grasshopper_Kernel_Undo_GH_UndoAction_Undo.htm) | (Inherited from [GH\_UndoAction](T_Grasshopper_Kernel_Undo_GH_UndoAction.htm).) |
| Public method | [Write](M_Grasshopper_Kernel_Undo_GH_UndoAction_Write.htm) | (Inherited from [GH\_UndoAction](T_Grasshopper_Kernel_Undo_GH_UndoAction.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Undo Namespace](N_Grasshopper_Kernel_Undo.htm)

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST60D4F573\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [Grasshopper.Kernel.UndoAddLanguageSpecificTextSet("LST60D4F573\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_UndoAction](T_Grasshopper_Kernel_Undo_GH_UndoAction.htm)  
    Grasshopper.Kernel.UndoAddLanguageSpecificTextSet("LST60D4F573\_7?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_ObjectUndoAction  
      [Grasshopper.Kernel.Undo.ActionsAddLanguageSpecificTextSet("LST60D4F573\_8?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_DataMatchingAction](T_Grasshopper_Kernel_Undo_Actions_GH_DataMatchingAction.htm)  
      [Grasshopper.Kernel.Undo.ActionsAddLanguageSpecificTextSet("LST60D4F573\_9?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_DataModificationAction](T_Grasshopper_Kernel_Undo_Actions_GH_DataModificationAction.htm)  
      [Grasshopper.Kernel.Undo.ActionsAddLanguageSpecificTextSet("LST60D4F573\_10?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_HiddenAction](T_Grasshopper_Kernel_Undo_Actions_GH_HiddenAction.htm)  
      [Grasshopper.Kernel.Undo.ActionsAddLanguageSpecificTextSet("LST60D4F573\_11?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_IconDisplayAction](T_Grasshopper_Kernel_Undo_Actions_GH_IconDisplayAction.htm)  
      [Grasshopper.Kernel.Undo.ActionsAddLanguageSpecificTextSet("LST60D4F573\_12?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_IconOverrideAction](T_Grasshopper_Kernel_Undo_Actions_GH_IconOverrideAction.htm)  
      [Grasshopper.Kernel.Undo.ActionsAddLanguageSpecificTextSet("LST60D4F573\_13?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_LayoutAction](T_Grasshopper_Kernel_Undo_Actions_GH_LayoutAction.htm)  
      [Grasshopper.Kernel.Undo.ActionsAddLanguageSpecificTextSet("LST60D4F573\_14?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_LockedAction](T_Grasshopper_Kernel_Undo_Actions_GH_LockedAction.htm)  
      [Grasshopper.Kernel.Undo.ActionsAddLanguageSpecificTextSet("LST60D4F573\_15?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_NickNameAction](T_Grasshopper_Kernel_Undo_Actions_GH_NickNameAction.htm)  
      [Grasshopper.Kernel.Undo.ActionsAddLanguageSpecificTextSet("LST60D4F573\_16?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_PersistentDataActionAddLanguageSpecificTextSet("LST60D4F573\_17?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST60D4F573\_18?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Undo_Actions_GH_PersistentDataAction_1.htm)  
      [Grasshopper.Kernel.Undo.ActionsAddLanguageSpecificTextSet("LST60D4F573\_19?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_PivotAction](T_Grasshopper_Kernel_Undo_Actions_GH_PivotAction.htm)  
      [Grasshopper.Kernel.Undo.ActionsAddLanguageSpecificTextSet("LST60D4F573\_20?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_WireDisplayAction](T_Grasshopper_Kernel_Undo_Actions_GH_WireDisplayAction.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)