# N_Grasshopper_Kernel_Undo_Actions

﻿ Grasshopper.Kernel.Undo.Actions Namespace

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Undo.Actions](../html/N_Grasshopper_Kernel_Undo_Actions.htm "Grasshopper.Kernel.Undo.Actions")

[GH\_AddObjectAction Class](../html/T_Grasshopper_Kernel_Undo_Actions_GH_AddObjectAction.htm "GH_AddObjectAction Class")

[GH\_AddStateAction Class](../html/T_Grasshopper_Kernel_Undo_Actions_GH_AddStateAction.htm "GH_AddStateAction Class")

[GH\_DataMatchingAction Class](../html/T_Grasshopper_Kernel_Undo_Actions_GH_DataMatchingAction.htm "GH_DataMatchingAction Class")

[GH\_DataModificationAction Class](../html/T_Grasshopper_Kernel_Undo_Actions_GH_DataModificationAction.htm "GH_DataModificationAction Class")

[GH\_GenericObjectAction Class](../html/T_Grasshopper_Kernel_Undo_Actions_GH_GenericObjectAction.htm "GH_GenericObjectAction Class")

[GH\_HiddenAction Class](../html/T_Grasshopper_Kernel_Undo_Actions_GH_HiddenAction.htm "GH_HiddenAction Class")

[GH\_IconDisplayAction Class](../html/T_Grasshopper_Kernel_Undo_Actions_GH_IconDisplayAction.htm "GH_IconDisplayAction Class")

[GH\_IconOverrideAction Class](../html/T_Grasshopper_Kernel_Undo_Actions_GH_IconOverrideAction.htm "GH_IconOverrideAction Class")

[GH\_LayoutAction Class](../html/T_Grasshopper_Kernel_Undo_Actions_GH_LayoutAction.htm "GH_LayoutAction Class")

[GH\_LockedAction Class](../html/T_Grasshopper_Kernel_Undo_Actions_GH_LockedAction.htm "GH_LockedAction Class")

[GH\_NickNameAction Class](../html/T_Grasshopper_Kernel_Undo_Actions_GH_NickNameAction.htm "GH_NickNameAction Class")

[GH\_PersistentDataAction(T) Class](../html/T_Grasshopper_Kernel_Undo_Actions_GH_PersistentDataAction_1.htm "GH_PersistentDataAction(T) Class")

[GH\_PivotAction Class](../html/T_Grasshopper_Kernel_Undo_Actions_GH_PivotAction.htm "GH_PivotAction Class")

[GH\_RemoveObjectAction Class](../html/T_Grasshopper_Kernel_Undo_Actions_GH_RemoveObjectAction.htm "GH_RemoveObjectAction Class")

[GH\_RemoveStateAction Class](../html/T_Grasshopper_Kernel_Undo_Actions_GH_RemoveStateAction.htm "GH_RemoveStateAction Class")

[GH\_WireAction Class](../html/T_Grasshopper_Kernel_Undo_Actions_GH_WireAction.htm "GH_WireAction Class")

[GH\_WireDisplayAction Class](../html/T_Grasshopper_Kernel_Undo_Actions_GH_WireDisplayAction.htm "GH_WireDisplayAction Class")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| Grasshopper.Kernel.Undo.Actions Namespace |

Contains a set of predefined undo/redo actions to make certain undo records simpler.

![](../icons/SectionExpanded.png)Classes

|  | Class | Description |
| --- | --- | --- |
| Public class | [GH\_AddObjectAction](T_Grasshopper_Kernel_Undo_Actions_GH_AddObjectAction.htm) | Records a single object addition. |
| Public class | [GH\_AddStateAction](T_Grasshopper_Kernel_Undo_Actions_GH_AddStateAction.htm) | Record the addition of a single solution state to a document. |
| Public class | [GH\_DataMatchingAction](T_Grasshopper_Kernel_Undo_Actions_GH_DataMatchingAction.htm) | Records a single Component DataComparison event. |
| Public class | [GH\_DataModificationAction](T_Grasshopper_Kernel_Undo_Actions_GH_DataModificationAction.htm) | Records a single Parameter DataModification event. |
| Public class | [GH\_GenericObjectAction](T_Grasshopper_Kernel_Undo_Actions_GH_GenericObjectAction.htm) | Records a single object change. Object changes are undone/redone by (de)serializing the objects. Object changes also keep track of all wires feeding into and coming out of the object. |
| Public class | [GH\_HiddenAction](T_Grasshopper_Kernel_Undo_Actions_GH_HiddenAction.htm) | Records a single object Preview event. |
| Public class | [GH\_IconDisplayAction](T_Grasshopper_Kernel_Undo_Actions_GH_IconDisplayAction.htm) | Records a single icon display mode event. |
| Public class | [GH\_IconOverrideAction](T_Grasshopper_Kernel_Undo_Actions_GH_IconOverrideAction.htm) | Records a single icon override event. |
| Public class | [GH\_LayoutAction](T_Grasshopper_Kernel_Undo_Actions_GH_LayoutAction.htm) | Records a single object layout event. Useful for tracking object resizes. |
| Public class | [GH\_LockedAction](T_Grasshopper_Kernel_Undo_Actions_GH_LockedAction.htm) | Records a single object Enabled event. |
| Public class | [GH\_NickNameAction](T_Grasshopper_Kernel_Undo_Actions_GH_NickNameAction.htm) | Records a single object NickName and IconDisplayMode event. |
| Public class | [GH\_PersistentDataActionAddLanguageSpecificTextSet("LST1A68F0AD\_0?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST1A68F0AD\_1?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Undo_Actions_GH_PersistentDataAction_1.htm) | Records the changes in the persistent data of a parameter. |
| Public class | [GH\_PivotAction](T_Grasshopper_Kernel_Undo_Actions_GH_PivotAction.htm) | Records a single object pivot event. Useful for tracking object movement. |
| Public class | [GH\_RemoveObjectAction](T_Grasshopper_Kernel_Undo_Actions_GH_RemoveObjectAction.htm) | Records a single object removal. |
| Public class | [GH\_RemoveStateAction](T_Grasshopper_Kernel_Undo_Actions_GH_RemoveStateAction.htm) | Record the removal of a single solution state from a document. |
| Public class | [GH\_WireAction](T_Grasshopper_Kernel_Undo_Actions_GH_WireAction.htm) | Records any change to the input wires of a given parameter. |
| Public class | [GH\_WireDisplayAction](T_Grasshopper_Kernel_Undo_Actions_GH_WireDisplayAction.htm) | Records a single wire display mode event. |

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)