# Methods_T_Grasshopper_Kernel_IGH_DocumentObject

﻿ IGH\_DocumentObject Methods

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH\_DocumentObject Interface](../html/T_Grasshopper_Kernel_IGH_DocumentObject.htm "IGH_DocumentObject Interface")

[IGH\_DocumentObject Methods](../html/Methods_T_Grasshopper_Kernel_IGH_DocumentObject.htm "IGH_DocumentObject Methods")

[AddedToDocument Method](../html/M_Grasshopper_Kernel_IGH_DocumentObject_AddedToDocument.htm "AddedToDocument Method ")

[AppendMenuItems Method](../html/M_Grasshopper_Kernel_IGH_DocumentObject_AppendMenuItems.htm "AppendMenuItems Method ")

[CreateAttributes Method](../html/M_Grasshopper_Kernel_IGH_DocumentObject_CreateAttributes.htm "CreateAttributes Method ")

[DocumentContextChanged Method](../html/M_Grasshopper_Kernel_IGH_DocumentObject_DocumentContextChanged.htm "DocumentContextChanged Method ")

[ExpirePreview Method](../html/M_Grasshopper_Kernel_IGH_DocumentObject_ExpirePreview.htm "ExpirePreview Method ")

[ExpireSolution Method](../html/M_Grasshopper_Kernel_IGH_DocumentObject_ExpireSolution.htm "ExpireSolution Method ")

[IsolateObject Method](../html/M_Grasshopper_Kernel_IGH_DocumentObject_IsolateObject.htm "IsolateObject Method ")

[MovedBetweenDocuments Method](../html/M_Grasshopper_Kernel_IGH_DocumentObject_MovedBetweenDocuments.htm "MovedBetweenDocuments Method ")

[OnAttributesChanged Method](../html/M_Grasshopper_Kernel_IGH_DocumentObject_OnAttributesChanged.htm "OnAttributesChanged Method ")

[OnDisplayExpired Method](../html/M_Grasshopper_Kernel_IGH_DocumentObject_OnDisplayExpired.htm "OnDisplayExpired Method ")

[OnObjectChanged Method](../html/Overload_Grasshopper_Kernel_IGH_DocumentObject_OnObjectChanged.htm "OnObjectChanged Method ")

[OnPingDocument Method](../html/M_Grasshopper_Kernel_IGH_DocumentObject_OnPingDocument.htm "OnPingDocument Method ")

[OnPreviewExpired Method](../html/M_Grasshopper_Kernel_IGH_DocumentObject_OnPreviewExpired.htm "OnPreviewExpired Method ")

[OnSolutionExpired Method](../html/M_Grasshopper_Kernel_IGH_DocumentObject_OnSolutionExpired.htm "OnSolutionExpired Method ")

[RecordUndoEvent Method](../html/Overload_Grasshopper_Kernel_IGH_DocumentObject_RecordUndoEvent.htm "RecordUndoEvent Method ")

[RemovedFromDocument Method](../html/M_Grasshopper_Kernel_IGH_DocumentObject_RemovedFromDocument.htm "RemovedFromDocument Method ")

[TriggerAutoSave Method](../html/Overload_Grasshopper_Kernel_IGH_DocumentObject_TriggerAutoSave.htm "TriggerAutoSave Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_DocumentObject Methods |

The [IGH\_DocumentObject](T_Grasshopper_Kernel_IGH_DocumentObject.htm) type exposes the following members.

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [AddedToDocument](M_Grasshopper_Kernel_IGH_DocumentObject_AddedToDocument.htm) | This method will be called when an object is added to a document. |
| Public method | [AppendMenuItems](M_Grasshopper_Kernel_IGH_DocumentObject_AppendMenuItems.htm) | This function is called when a context menu is about to be displayed. Override it to set custom items. |
| Public method | [CreateAttributes](M_Grasshopper_Kernel_IGH_DocumentObject_CreateAttributes.htm) | Create new default attributes for this object. You should only call this function when the Attributes() field is null. |
| Public method | [DocumentContextChanged](M_Grasshopper_Kernel_IGH_DocumentObject_DocumentContextChanged.htm) | This method will be called when the document that owns this object moves into a different context. |
| Public method | [ExpirePreview](M_Grasshopper_Kernel_IGH_DocumentObject_ExpirePreview.htm) | Call this function when you suspect that the preview has expired for this object. This will cause the display cache to be eradicated. |
| Public method | [ExpireSolution](M_Grasshopper_Kernel_IGH_DocumentObject_ExpireSolution.htm) | Call this function whenever you do something which expires the current solution. This will make sure all caches are erased, all downstream objects are expired and that the event is raised. The default implementation merely places a call to OnSolutionExpired(), override this function in derived classes to make sure you clear local data caches and expire downstream objects. |
| Public method | [IsolateObject](M_Grasshopper_Kernel_IGH_DocumentObject_IsolateObject.htm) | Destroy all connections to other objects. |
| Public method | [MovedBetweenDocuments](M_Grasshopper_Kernel_IGH_DocumentObject_MovedBetweenDocuments.htm) | This method will be called when an object is moved from one document to another. |
| Public method | [NewInstanceGuidAddLanguageSpecificTextSet("LSTB4124516\_0?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_IGH_InstanceDescription_NewInstanceGuid.htm) | Generate a new random instance GUID (Inherited from [IGH\_InstanceDescription](T_Grasshopper_Kernel_IGH_InstanceDescription.htm).) |
| Public method | [NewInstanceGuid(Guid)](M_Grasshopper_Kernel_IGH_InstanceDescription_NewInstanceGuid_1.htm) | Set the instance ID to be a specific GUID. This is very dangerous, only use this function if you're 6"4' and called David. (Inherited from [IGH\_InstanceDescription](T_Grasshopper_Kernel_IGH_InstanceDescription.htm).) |
| Public method | [OnAttributesChanged](M_Grasshopper_Kernel_IGH_DocumentObject_OnAttributesChanged.htm) | Raises the AttributesChanged event on the toplevel object. |
| Public method | [OnDisplayExpired](M_Grasshopper_Kernel_IGH_DocumentObject_OnDisplayExpired.htm) | Raises the DisplayExpired event on the toplevel object. |
| Public method | [OnObjectChanged(GH\_ObjectChangedEventArgs)](M_Grasshopper_Kernel_IGH_DocumentObject_OnObjectChanged.htm) | Raises the ObjectChanged event on the current (!not the top level!) object. |
| Public method | [OnObjectChanged(GH\_ObjectEventType)](M_Grasshopper_Kernel_IGH_DocumentObject_OnObjectChanged_1.htm) | Raises the ObjectChanged event on the current (!not the top level!) object. |
| Public method | [OnObjectChanged(String)](M_Grasshopper_Kernel_IGH_DocumentObject_OnObjectChanged_3.htm) | Raises the ObjectChanged event on the current (!not the top level!) object. |
| Public method | [OnObjectChanged(GH\_ObjectEventType, Object)](M_Grasshopper_Kernel_IGH_DocumentObject_OnObjectChanged_2.htm) | Raises the ObjectChanged event on the current (!not the top level!) object. |
| Public method | [OnObjectChanged(String, Object)](M_Grasshopper_Kernel_IGH_DocumentObject_OnObjectChanged_4.htm) | Raises the ObjectChanged event on the current (!not the top level!) object. |
| Public method | [OnPingDocument](M_Grasshopper_Kernel_IGH_DocumentObject_OnPingDocument.htm) | Raise the PingDocument Event on the toplevel object and try to find the document which owns this object. |
| Public method | [OnPreviewExpired](M_Grasshopper_Kernel_IGH_DocumentObject_OnPreviewExpired.htm) | Raises the PreviewExpired event on the toplevel object. |
| Public method | [OnSolutionExpired](M_Grasshopper_Kernel_IGH_DocumentObject_OnSolutionExpired.htm) | Raises the SolutionExpired event on the toplevel object. |
| Public method | [RecordUndoEvent(GH\_UndoRecord)](M_Grasshopper_Kernel_IGH_DocumentObject_RecordUndoEvent.htm) | Record an entire undo record. |
| Public method | [RecordUndoEvent(String)](M_Grasshopper_Kernel_IGH_DocumentObject_RecordUndoEvent_1.htm) | Record a generic object change undo event. |
| Public method | [RecordUndoEvent(String, IGH\_UndoAction)](M_Grasshopper_Kernel_IGH_DocumentObject_RecordUndoEvent_2.htm) | Record a specific object change undo event. |
| Public method | [RemovedFromDocument](M_Grasshopper_Kernel_IGH_DocumentObject_RemovedFromDocument.htm) | This method will be called when an object is removed from a document. |
| Public method | [TriggerAutoSaveAddLanguageSpecificTextSet("LSTB4124516\_1?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_IGH_DocumentObject_TriggerAutoSave.htm) | Triggers the AutoSave function on the owner document with the object\_changed flag. |
| Public method | [TriggerAutoSave(GH\_AutoSaveTrigger)](M_Grasshopper_Kernel_IGH_DocumentObject_TriggerAutoSave_1.htm) | Triggers the AutoSave function on the owner document with a custom flag. |
| Public method | [TriggerAutoSave(Guid)](M_Grasshopper_Kernel_IGH_DocumentObject_TriggerAutoSave_3.htm) | Triggers the AutoSave function on the owner document with the object\_changed flag. |
| Public method | [TriggerAutoSave(GH\_AutoSaveTrigger, Guid)](M_Grasshopper_Kernel_IGH_DocumentObject_TriggerAutoSave_2.htm) | Triggers the AutoSave function on the owner document with a custom flag. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[IGH\_DocumentObject Interface](T_Grasshopper_Kernel_IGH_DocumentObject.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)