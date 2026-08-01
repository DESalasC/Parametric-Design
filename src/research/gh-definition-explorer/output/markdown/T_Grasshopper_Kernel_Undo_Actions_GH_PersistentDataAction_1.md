# T_Grasshopper_Kernel_Undo_Actions_GH_PersistentDataAction_1

﻿ GH\_PersistentDataAction(T) Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Undo.Actions](../html/N_Grasshopper_Kernel_Undo_Actions.htm "Grasshopper.Kernel.Undo.Actions")

[GH\_PersistentDataAction(T) Class](../html/T_Grasshopper_Kernel_Undo_Actions_GH_PersistentDataAction_1.htm "GH_PersistentDataAction(T) Class")

[GH\_PersistentDataAction(T) Constructor](../html/M_Grasshopper_Kernel_Undo_Actions_GH_PersistentDataAction_1__ctor.htm "GH_PersistentDataAction(T) Constructor ")

[GH\_PersistentDataAction(T) Properties](../html/Properties_T_Grasshopper_Kernel_Undo_Actions_GH_PersistentDataAction_1.htm "GH_PersistentDataAction(T) Properties")

[GH\_PersistentDataAction(T) Methods](../html/Methods_T_Grasshopper_Kernel_Undo_Actions_GH_PersistentDataAction_1.htm "GH_PersistentDataAction(T) Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_PersistentDataActionAddLanguageSpecificTextSet("LSTC87B0A59\_0?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTC87B0A59\_1?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)"); Class |

Records the changes in the persistent data of a parameter.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LSTC87B0A59\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [Grasshopper.Kernel.UndoAddLanguageSpecificTextSet("LSTC87B0A59\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_UndoAction](T_Grasshopper_Kernel_Undo_GH_UndoAction.htm)  
    [Grasshopper.Kernel.UndoAddLanguageSpecificTextSet("LSTC87B0A59\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_ObjectUndoAction](T_Grasshopper_Kernel_Undo_GH_ObjectUndoAction.htm)  
      Grasshopper.Kernel.Undo.ActionsAddLanguageSpecificTextSet("LSTC87B0A59\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_PersistentDataActionAddLanguageSpecificTextSet("LSTC87B0A59\_6?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTC87B0A59\_7?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");

**Namespace:**
 [Grasshopper.Kernel.Undo.Actions](N_Grasshopper_Kernel_Undo_Actions.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_PersistentDataAction<T> : GH_ObjectUndoAction
where T : class, IGH_Goo
```

```
Public Class GH_PersistentDataAction(Of T As {Class, IGH_Goo})
	Inherits GH_ObjectUndoAction
```

AddLanguageTabSet("ID1EBCA");

#### Type Parameters

T

The GH\_PersistentDataActionAddLanguageSpecificTextSet("LSTC87B0A59\_8?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTC87B0A59\_9?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;"); type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_PersistentDataActionAddLanguageSpecificTextSet("LSTC87B0A59\_10?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTC87B0A59\_11?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](M_Grasshopper_Kernel_Undo_Actions_GH_PersistentDataAction_1__ctor.htm) | Initializes a new instance of the GH\_PersistentDataActionAddLanguageSpecificTextSet("LSTC87B0A59\_12?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTC87B0A59\_13?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;"); class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [ExpiresDisplay](P_Grasshopper_Kernel_Undo_GH_UndoAction_ExpiresDisplay.htm) | Override this property if you want the Rhino viewport display to refresh upon undo completion. (Inherited from [GH\_UndoAction](T_Grasshopper_Kernel_Undo_GH_UndoAction.htm).) |
| Public property | [ExpiresSolution](P_Grasshopper_Kernel_Undo_Actions_GH_PersistentDataAction_1_ExpiresSolution.htm) | (Overrides [GH\_UndoActionAddLanguageSpecificTextSet("LSTC87B0A59\_14?cs=.|vb=.|cpp=::|nu=.|fs=.");ExpiresSolution](P_Grasshopper_Kernel_Undo_GH_UndoAction_ExpiresSolution.htm).) |
| Public property | [State](P_Grasshopper_Kernel_Undo_GH_UndoAction_State.htm) | (Inherited from [GH\_UndoAction](T_Grasshopper_Kernel_Undo_GH_UndoAction.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Protected method | [Internal\_Redo](M_Grasshopper_Kernel_Undo_GH_ObjectUndoAction_Internal_Redo.htm) | (Inherited from [GH\_ObjectUndoAction](T_Grasshopper_Kernel_Undo_GH_ObjectUndoAction.htm).) |
| Protected method | [Internal\_Undo](M_Grasshopper_Kernel_Undo_GH_ObjectUndoAction_Internal_Undo.htm) | (Inherited from [GH\_ObjectUndoAction](T_Grasshopper_Kernel_Undo_GH_ObjectUndoAction.htm).) |
| Protected method | [Object\_Redo](M_Grasshopper_Kernel_Undo_Actions_GH_PersistentDataAction_1_Object_Redo.htm) | (Overrides [GH\_ObjectUndoActionAddLanguageSpecificTextSet("LSTC87B0A59\_15?cs=.|vb=.|cpp=::|nu=.|fs=.");Object\_Redo(GH\_Document, IGH\_DocumentObject)](M_Grasshopper_Kernel_Undo_GH_ObjectUndoAction_Object_Redo.htm).) |
| Protected method | [Object\_Undo](M_Grasshopper_Kernel_Undo_Actions_GH_PersistentDataAction_1_Object_Undo.htm) | (Overrides [GH\_ObjectUndoActionAddLanguageSpecificTextSet("LSTC87B0A59\_16?cs=.|vb=.|cpp=::|nu=.|fs=.");Object\_Undo(GH\_Document, IGH\_DocumentObject)](M_Grasshopper_Kernel_Undo_GH_ObjectUndoAction_Object_Undo.htm).) |
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