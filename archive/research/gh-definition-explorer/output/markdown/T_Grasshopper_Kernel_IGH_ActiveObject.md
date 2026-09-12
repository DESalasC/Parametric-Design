# T_Grasshopper_Kernel_IGH_ActiveObject

﻿ IGH\_ActiveObject Interface

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH\_ActiveObject Interface](../html/T_Grasshopper_Kernel_IGH_ActiveObject.htm "IGH_ActiveObject Interface")

[IGH\_ActiveObject Properties](../html/Properties_T_Grasshopper_Kernel_IGH_ActiveObject.htm "IGH_ActiveObject Properties")

[IGH\_ActiveObject Methods](../html/Methods_T_Grasshopper_Kernel_IGH_ActiveObject.htm "IGH_ActiveObject Methods")

[IGH\_ActiveObject Events](../html/Events_T_Grasshopper_Kernel_IGH_ActiveObject.htm "IGH_ActiveObject Events")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_ActiveObject Interface |

Base interface for all objects on the canvas that participate in solutions

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public interface IGH_ActiveObject : IGH_DocumentObject
```

```
Public Interface IGH_ActiveObject
	Inherits IGH_DocumentObject
```

AddLanguageTabSet("ID0EBCA");

The IGH\_ActiveObject type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Attributes](P_Grasshopper_Kernel_IGH_DocumentObject_Attributes.htm) | Gets or sets the attributes that are associated with this object. Only set custom attributes if you know what you are doing. (Inherited from [IGH\_DocumentObject](T_Grasshopper_Kernel_IGH_DocumentObject.htm).) |
| Public property | [ComponentGuid](P_Grasshopper_Kernel_IGH_DocumentObject_ComponentGuid.htm) | Returns a consistent ID for this object type. Every object must supply a unique and unchanging ID that is used to identify objects of the same type. (Inherited from [IGH\_DocumentObject](T_Grasshopper_Kernel_IGH_DocumentObject.htm).) |
| Public property | [Exposure](P_Grasshopper_Kernel_IGH_DocumentObject_Exposure.htm) | Gets the exposure of this object in the Graphical User Interface. (Inherited from [IGH\_DocumentObject](T_Grasshopper_Kernel_IGH_DocumentObject.htm).) |
| Public property | [Icon\_24x24](P_Grasshopper_Kernel_IGH_DocumentObject_Icon_24x24.htm) | The icon associated with this object. (Inherited from [IGH\_DocumentObject](T_Grasshopper_Kernel_IGH_DocumentObject.htm).) |
| Public property | [Icon\_24x24\_Locked](P_Grasshopper_Kernel_IGH_DocumentObject_Icon_24x24_Locked.htm) | The greyscale icon of this object. (Inherited from [IGH\_DocumentObject](T_Grasshopper_Kernel_IGH_DocumentObject.htm).) |
| Public property | [IconDisplayMode](P_Grasshopper_Kernel_IGH_DocumentObject_IconDisplayMode.htm) | Gets the current display mode of the object. (Inherited from [IGH\_DocumentObject](T_Grasshopper_Kernel_IGH_DocumentObject.htm).) |
| Public property | [IsDataProvider](P_Grasshopper_Kernel_IGH_ActiveObject_IsDataProvider.htm) | Gets whether or not this object is capable of emitting data. |
| Public property | [Locked](P_Grasshopper_Kernel_IGH_ActiveObject_Locked.htm) | Gets or sets the locked flag of this object. Locked objects are ignored during solutions. |
| Public property | [MutableNickName](P_Grasshopper_Kernel_IGH_ActiveObject_MutableNickName.htm) | Gets or sets a value that enables Nick name changes through the menu. The default is TRUE. |
| Public property | [Obsolete](P_Grasshopper_Kernel_IGH_DocumentObject_Obsolete.htm) | Gets whether this object is Obsolete. (Inherited from [IGH\_DocumentObject](T_Grasshopper_Kernel_IGH_DocumentObject.htm).) |
| Public property | [Phase](P_Grasshopper_Kernel_IGH_ActiveObject_Phase.htm) | Gets the solution phase in which this object is currently stuck. |
| Public property | [ProcessorTime](P_Grasshopper_Kernel_IGH_ActiveObject_ProcessorTime.htm) | Gets the most recent measured processor time. |
| Public property | [RuntimeMessageLevel](P_Grasshopper_Kernel_IGH_ActiveObject_RuntimeMessageLevel.htm) | Gets the worst-case level of all messages. I.e. if only warnings have been recorded, the level will be ::warning. If even a single error exists, the level will be ::error. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [AddedToDocument](M_Grasshopper_Kernel_IGH_DocumentObject_AddedToDocument.htm) | This method will be called when an object is added to a document. (Inherited from [IGH\_DocumentObject](T_Grasshopper_Kernel_IGH_DocumentObject.htm).) |
| Public method | [AddRuntimeMessage](M_Grasshopper_Kernel_IGH_ActiveObject_AddRuntimeMessage.htm) | Add a new message to this object. Valid message type flags are Warning and Error. If the Message string is empty or zero-length no message is added. |
| Public method | [AppendMenuItems](M_Grasshopper_Kernel_IGH_DocumentObject_AppendMenuItems.htm) | This function is called when a context menu is about to be displayed. Override it to set custom items. (Inherited from [IGH\_DocumentObject](T_Grasshopper_Kernel_IGH_DocumentObject.htm).) |
| Public method | [ClearData](M_Grasshopper_Kernel_IGH_ActiveObject_ClearData.htm) | This function is called whenever the object needs to clear all solution data. This usually amounts to wiping volatile caches and messages. This function will not affect any other objects, but it will set the Phase flag to Blank |
| Public method | [ClearRuntimeMessages](M_Grasshopper_Kernel_IGH_ActiveObject_ClearRuntimeMessages.htm) | Clear all message lists. |
| Public method | [CollectData](M_Grasshopper_Kernel_IGH_ActiveObject_CollectData.htm) | This function is called whenever the object is required to collect all data. Either from Persistent records, from source params or whatever. This step is only performed if the phase flag is Blank or Failed. Upon completion, the phase flag will be set to Collected |
| Public method | [ComputeData](M_Grasshopper_Kernel_IGH_ActiveObject_ComputeData.htm) | This function is called whenever the object is required to generate new data. This step is only performed by some objects and only when the Phase flag is Collected. Upon completion, the Phase will be Computed. If this object throws exceptions, it is the responsibility of the caller to set the Phase flag to Failed. |
| Public method | [CreateAttributes](M_Grasshopper_Kernel_IGH_DocumentObject_CreateAttributes.htm) | Create new default attributes for this object. You should only call this function when the Attributes() field is null. (Inherited from [IGH\_DocumentObject](T_Grasshopper_Kernel_IGH_DocumentObject.htm).) |
| Public method | [DependsOn](M_Grasshopper_Kernel_IGH_ActiveObject_DependsOn.htm) | Solve the inheritance relationship between this object and a potential parental object. |
| Public method | [DocumentContextChanged](M_Grasshopper_Kernel_IGH_DocumentObject_DocumentContextChanged.htm) | This method will be called when the document that owns this object moves into a different context. (Inherited from [IGH\_DocumentObject](T_Grasshopper_Kernel_IGH_DocumentObject.htm).) |
| Public method | [ExpirePreview](M_Grasshopper_Kernel_IGH_DocumentObject_ExpirePreview.htm) | Call this function when you suspect that the preview has expired for this object. This will cause the display cache to be eradicated. (Inherited from [IGH\_DocumentObject](T_Grasshopper_Kernel_IGH_DocumentObject.htm).) |
| Public method | [ExpireSolution](M_Grasshopper_Kernel_IGH_DocumentObject_ExpireSolution.htm) | Call this function whenever you do something which expires the current solution. This will make sure all caches are erased, all downstream objects are expired and that the event is raised. The default implementation merely places a call to OnSolutionExpired(), override this function in derived classes to make sure you clear local data caches and expire downstream objects. (Inherited from [IGH\_DocumentObject](T_Grasshopper_Kernel_IGH_DocumentObject.htm).) |
| Public method | [IsolateObject](M_Grasshopper_Kernel_IGH_DocumentObject_IsolateObject.htm) | Destroy all connections to other objects. (Inherited from [IGH\_DocumentObject](T_Grasshopper_Kernel_IGH_DocumentObject.htm).) |
| Public method | [MovedBetweenDocuments](M_Grasshopper_Kernel_IGH_DocumentObject_MovedBetweenDocuments.htm) | This method will be called when an object is moved from one document to another. (Inherited from [IGH\_DocumentObject](T_Grasshopper_Kernel_IGH_DocumentObject.htm).) |
| Public method | [OnAttributesChanged](M_Grasshopper_Kernel_IGH_DocumentObject_OnAttributesChanged.htm) | Raises the AttributesChanged event on the toplevel object. (Inherited from [IGH\_DocumentObject](T_Grasshopper_Kernel_IGH_DocumentObject.htm).) |
| Public method | [OnDisplayExpired](M_Grasshopper_Kernel_IGH_DocumentObject_OnDisplayExpired.htm) | Raises the DisplayExpired event on the toplevel object. (Inherited from [IGH\_DocumentObject](T_Grasshopper_Kernel_IGH_DocumentObject.htm).) |
| Public method | [OnObjectChanged(GH\_ObjectChangedEventArgs)](M_Grasshopper_Kernel_IGH_DocumentObject_OnObjectChanged.htm) | Raises the ObjectChanged event on the current (!not the top level!) object. (Inherited from [IGH\_DocumentObject](T_Grasshopper_Kernel_IGH_DocumentObject.htm).) |
| Public method | [OnObjectChanged(GH\_ObjectEventType)](M_Grasshopper_Kernel_IGH_DocumentObject_OnObjectChanged_1.htm) | Raises the ObjectChanged event on the current (!not the top level!) object. (Inherited from [IGH\_DocumentObject](T_Grasshopper_Kernel_IGH_DocumentObject.htm).) |
| Public method | [OnObjectChanged(String)](M_Grasshopper_Kernel_IGH_DocumentObject_OnObjectChanged_3.htm) | Raises the ObjectChanged event on the current (!not the top level!) object. (Inherited from [IGH\_DocumentObject](T_Grasshopper_Kernel_IGH_DocumentObject.htm).) |
| Public method | [OnObjectChanged(GH\_ObjectEventType, Object)](M_Grasshopper_Kernel_IGH_DocumentObject_OnObjectChanged_2.htm) | Raises the ObjectChanged event on the current (!not the top level!) object. (Inherited from [IGH\_DocumentObject](T_Grasshopper_Kernel_IGH_DocumentObject.htm).) |
| Public method | [OnObjectChanged(String, Object)](M_Grasshopper_Kernel_IGH_DocumentObject_OnObjectChanged_4.htm) | Raises the ObjectChanged event on the current (!not the top level!) object. (Inherited from [IGH\_DocumentObject](T_Grasshopper_Kernel_IGH_DocumentObject.htm).) |
| Public method | [OnPingDocument](M_Grasshopper_Kernel_IGH_DocumentObject_OnPingDocument.htm) | Raise the PingDocument Event on the toplevel object and try to find the document which owns this object. (Inherited from [IGH\_DocumentObject](T_Grasshopper_Kernel_IGH_DocumentObject.htm).) |
| Public method | [OnPreviewExpired](M_Grasshopper_Kernel_IGH_DocumentObject_OnPreviewExpired.htm) | Raises the PreviewExpired event on the toplevel object. (Inherited from [IGH\_DocumentObject](T_Grasshopper_Kernel_IGH_DocumentObject.htm).) |
| Public method | [OnSolutionExpired](M_Grasshopper_Kernel_IGH_DocumentObject_OnSolutionExpired.htm) | Raises the SolutionExpired event on the toplevel object. (Inherited from [IGH\_DocumentObject](T_Grasshopper_Kernel_IGH_DocumentObject.htm).) |
| Public method | [RecordUndoEvent(GH\_UndoRecord)](M_Grasshopper_Kernel_IGH_DocumentObject_RecordUndoEvent.htm) | Record an entire undo record. (Inherited from [IGH\_DocumentObject](T_Grasshopper_Kernel_IGH_DocumentObject.htm).) |
| Public method | [RecordUndoEvent(String)](M_Grasshopper_Kernel_IGH_DocumentObject_RecordUndoEvent_1.htm) | Record a generic object change undo event. (Inherited from [IGH\_DocumentObject](T_Grasshopper_Kernel_IGH_DocumentObject.htm).) |
| Public method | [RecordUndoEvent(String, IGH\_UndoAction)](M_Grasshopper_Kernel_IGH_DocumentObject_RecordUndoEvent_2.htm) | Record a specific object change undo event. (Inherited from [IGH\_DocumentObject](T_Grasshopper_Kernel_IGH_DocumentObject.htm).) |
| Public method | [RegisterRemoteIDs](M_Grasshopper_Kernel_IGH_ActiveObject_RegisterRemoteIDs.htm) | If this object depends on Rhino Objects, you must register the UUIDs of those objects. Failure to do so will result in faulty event handling. |
| Public method | [RemovedFromDocument](M_Grasshopper_Kernel_IGH_DocumentObject_RemovedFromDocument.htm) | This method will be called when an object is removed from a document. (Inherited from [IGH\_DocumentObject](T_Grasshopper_Kernel_IGH_DocumentObject.htm).) |
| Public method | [RuntimeMessages](M_Grasshopper_Kernel_IGH_ActiveObject_RuntimeMessages.htm) | Gets the list of cached runtime messages that were recorded during solver-time processes. |
| Public method | [SDKCompliancy](M_Grasshopper_Kernel_IGH_ActiveObject_SDKCompliancy.htm) | Test whether this object is compliant with a given Rhino version. |
| Public method | [TriggerAutoSaveAddLanguageSpecificTextSet("LST11FEBCBC\_0?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_IGH_DocumentObject_TriggerAutoSave.htm) | Triggers the AutoSave function on the owner document with the object\_changed flag. (Inherited from [IGH\_DocumentObject](T_Grasshopper_Kernel_IGH_DocumentObject.htm).) |
| Public method | [TriggerAutoSave(GH\_AutoSaveTrigger)](M_Grasshopper_Kernel_IGH_DocumentObject_TriggerAutoSave_1.htm) | Triggers the AutoSave function on the owner document with a custom flag. (Inherited from [IGH\_DocumentObject](T_Grasshopper_Kernel_IGH_DocumentObject.htm).) |
| Public method | [TriggerAutoSave(Guid)](M_Grasshopper_Kernel_IGH_DocumentObject_TriggerAutoSave_3.htm) | Triggers the AutoSave function on the owner document with the object\_changed flag. (Inherited from [IGH\_DocumentObject](T_Grasshopper_Kernel_IGH_DocumentObject.htm).) |
| Public method | [TriggerAutoSave(GH\_AutoSaveTrigger, Guid)](M_Grasshopper_Kernel_IGH_DocumentObject_TriggerAutoSave_2.htm) | Triggers the AutoSave function on the owner document with a custom flag. (Inherited from [IGH\_DocumentObject](T_Grasshopper_Kernel_IGH_DocumentObject.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Events

|  | Name | Description |
| --- | --- | --- |
| Public event | [AttributesChanged](E_Grasshopper_Kernel_IGH_DocumentObject_AttributesChanged.htm) | Raised whenever the number or kind of attributes changes. This event is handled by GH\_Documents who subsequently wipe their attribute caches. (Inherited from [IGH\_DocumentObject](T_Grasshopper_Kernel_IGH_DocumentObject.htm).) |
| Public event | [DisplayExpired](E_Grasshopper_Kernel_IGH_DocumentObject_DisplayExpired.htm) | Raised whenever the display (on the Canvas) of a certain object becomes invalid. (Inherited from [IGH\_DocumentObject](T_Grasshopper_Kernel_IGH_DocumentObject.htm).) |
| Public event | [ObjectChanged](E_Grasshopper_Kernel_IGH_DocumentObject_ObjectChanged.htm) | Raised whenever some property of the object changes that would affect remote instances. (Inherited from [IGH\_DocumentObject](T_Grasshopper_Kernel_IGH_DocumentObject.htm).) |
| Public event | [PingDocument](E_Grasshopper_Kernel_IGH_DocumentObject_PingDocument.htm) | Raised whenever an object needs to know which GH\_Document it belongs to. (Inherited from [IGH\_DocumentObject](T_Grasshopper_Kernel_IGH_DocumentObject.htm).) |
| Public event | [PreviewExpired](E_Grasshopper_Kernel_IGH_DocumentObject_PreviewExpired.htm) | Raised whenever the display (in the Rhino viewports) of a certain object becomes invalid. (Inherited from [IGH\_DocumentObject](T_Grasshopper_Kernel_IGH_DocumentObject.htm).) |
| Public event | [SolutionExpired](E_Grasshopper_Kernel_IGH_DocumentObject_SolutionExpired.htm) | Raised whenever the solution of a certain object becomes invalid. (Inherited from [IGH\_DocumentObject](T_Grasshopper_Kernel_IGH_DocumentObject.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)