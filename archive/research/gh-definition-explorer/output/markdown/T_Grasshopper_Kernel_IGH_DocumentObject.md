# T_Grasshopper_Kernel_IGH_DocumentObject

﻿ IGH\_DocumentObject Interface

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH\_DocumentObject Interface](../html/T_Grasshopper_Kernel_IGH_DocumentObject.htm "IGH_DocumentObject Interface")

[IGH\_DocumentObject Properties](../html/Properties_T_Grasshopper_Kernel_IGH_DocumentObject.htm "IGH_DocumentObject Properties")

[IGH\_DocumentObject Methods](../html/Methods_T_Grasshopper_Kernel_IGH_DocumentObject.htm "IGH_DocumentObject Methods")

[IGH\_DocumentObject Events](../html/Events_T_Grasshopper_Kernel_IGH_DocumentObject.htm "IGH_DocumentObject Events")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_DocumentObject Interface |

Base interface for objects that want to play on the Canvas.
Do not implement this interface from scratch. Either inherit from
GH\_DocumentObject or one of the other partially finished types such as
GH\_ActiveObject, GH\_Param(Of T) or GH\_Component.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public interface IGH_DocumentObject : IGH_InstanceDescription
```

```
Public Interface IGH_DocumentObject
	Inherits IGH_InstanceDescription
```

AddLanguageTabSet("ID0EBCA");

The IGH\_DocumentObject type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Attributes](P_Grasshopper_Kernel_IGH_DocumentObject_Attributes.htm) | Gets or sets the attributes that are associated with this object. Only set custom attributes if you know what you are doing. |
| Public property | [Category](P_Grasshopper_Kernel_IGH_InstanceDescription_Category.htm) | Gets or sets the Category in which this object belongs. If HasCategory() returns false, this field has no meaning. (Inherited from [IGH\_InstanceDescription](T_Grasshopper_Kernel_IGH_InstanceDescription.htm).) |
| Public property | [ComponentGuid](P_Grasshopper_Kernel_IGH_DocumentObject_ComponentGuid.htm) | Returns a consistent ID for this object type. Every object must supply a unique and unchanging ID that is used to identify objects of the same type. |
| Public property | [Description](P_Grasshopper_Kernel_IGH_InstanceDescription_Description.htm) | Gets or sets the description of the object. This field typically remains fixed during the lifetime of an object. (Inherited from [IGH\_InstanceDescription](T_Grasshopper_Kernel_IGH_InstanceDescription.htm).) |
| Public property | [Exposure](P_Grasshopper_Kernel_IGH_DocumentObject_Exposure.htm) | Gets the exposure of this object in the Graphical User Interface. |
| Public property | [HasCategory](P_Grasshopper_Kernel_IGH_InstanceDescription_HasCategory.htm) | Gets whether or not the Category field has been set. (Inherited from [IGH\_InstanceDescription](T_Grasshopper_Kernel_IGH_InstanceDescription.htm).) |
| Public property | [HasSubCategory](P_Grasshopper_Kernel_IGH_InstanceDescription_HasSubCategory.htm) | Gets whether or not the SubCategory field has been set. (Inherited from [IGH\_InstanceDescription](T_Grasshopper_Kernel_IGH_InstanceDescription.htm).) |
| Public property | [Icon\_24x24](P_Grasshopper_Kernel_IGH_DocumentObject_Icon_24x24.htm) | The icon associated with this object. |
| Public property | [Icon\_24x24\_Locked](P_Grasshopper_Kernel_IGH_DocumentObject_Icon_24x24_Locked.htm) | The greyscale icon of this object. |
| Public property | [IconDisplayMode](P_Grasshopper_Kernel_IGH_DocumentObject_IconDisplayMode.htm) | Gets the current display mode of the object. |
| Public property | [InstanceDescription](P_Grasshopper_Kernel_IGH_InstanceDescription_InstanceDescription.htm) | Gets a description of the current state of the object. This field is usually the same as the Description() field, but it might be variable when overridden. (Inherited from [IGH\_InstanceDescription](T_Grasshopper_Kernel_IGH_InstanceDescription.htm).) |
| Public property | [InstanceGuid](P_Grasshopper_Kernel_IGH_InstanceDescription_InstanceGuid.htm) | Gets the ID of this runtime instance. (Inherited from [IGH\_InstanceDescription](T_Grasshopper_Kernel_IGH_InstanceDescription.htm).) |
| Public property | [Keywords](P_Grasshopper_Kernel_IGH_InstanceDescription_Keywords.htm) | Gets a list of additional keywords that describe the object. Typically this list is empty but you can override this property to aid in object searches. (Inherited from [IGH\_InstanceDescription](T_Grasshopper_Kernel_IGH_InstanceDescription.htm).) |
| Public property | [Name](P_Grasshopper_Kernel_IGH_InstanceDescription_Name.htm) | Gets or sets the name of the object. This field typically remains fixed during the lifetime of an object. (Inherited from [IGH\_InstanceDescription](T_Grasshopper_Kernel_IGH_InstanceDescription.htm).) |
| Public property | [NickName](P_Grasshopper_Kernel_IGH_InstanceDescription_NickName.htm) | Gets or sets the nickname of the object. This field can be changed by the user. (Inherited from [IGH\_InstanceDescription](T_Grasshopper_Kernel_IGH_InstanceDescription.htm).) |
| Public property | [Obsolete](P_Grasshopper_Kernel_IGH_DocumentObject_Obsolete.htm) | Gets whether this object is Obsolete. |
| Public property | [SubCategory](P_Grasshopper_Kernel_IGH_InstanceDescription_SubCategory.htm) | Gets or sets the SubCategory in which this object belongs. If HasSubCategory() returns false, this field has no meaning. (Inherited from [IGH\_InstanceDescription](T_Grasshopper_Kernel_IGH_InstanceDescription.htm).) |

[Top](#PageHeader)

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
| Public method | [NewInstanceGuidAddLanguageSpecificTextSet("LST865562BC\_0?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_IGH_InstanceDescription_NewInstanceGuid.htm) | Generate a new random instance GUID (Inherited from [IGH\_InstanceDescription](T_Grasshopper_Kernel_IGH_InstanceDescription.htm).) |
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
| Public method | [TriggerAutoSaveAddLanguageSpecificTextSet("LST865562BC\_1?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_IGH_DocumentObject_TriggerAutoSave.htm) | Triggers the AutoSave function on the owner document with the object\_changed flag. |
| Public method | [TriggerAutoSave(GH\_AutoSaveTrigger)](M_Grasshopper_Kernel_IGH_DocumentObject_TriggerAutoSave_1.htm) | Triggers the AutoSave function on the owner document with a custom flag. |
| Public method | [TriggerAutoSave(Guid)](M_Grasshopper_Kernel_IGH_DocumentObject_TriggerAutoSave_3.htm) | Triggers the AutoSave function on the owner document with the object\_changed flag. |
| Public method | [TriggerAutoSave(GH\_AutoSaveTrigger, Guid)](M_Grasshopper_Kernel_IGH_DocumentObject_TriggerAutoSave_2.htm) | Triggers the AutoSave function on the owner document with a custom flag. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Events

|  | Name | Description |
| --- | --- | --- |
| Public event | [AttributesChanged](E_Grasshopper_Kernel_IGH_DocumentObject_AttributesChanged.htm) | Raised whenever the number or kind of attributes changes. This event is handled by GH\_Documents who subsequently wipe their attribute caches. |
| Public event | [DisplayExpired](E_Grasshopper_Kernel_IGH_DocumentObject_DisplayExpired.htm) | Raised whenever the display (on the Canvas) of a certain object becomes invalid. |
| Public event | [ObjectChanged](E_Grasshopper_Kernel_IGH_DocumentObject_ObjectChanged.htm) | Raised whenever some property of the object changes that would affect remote instances. |
| Public event | [PingDocument](E_Grasshopper_Kernel_IGH_DocumentObject_PingDocument.htm) | Raised whenever an object needs to know which GH\_Document it belongs to. |
| Public event | [PreviewExpired](E_Grasshopper_Kernel_IGH_DocumentObject_PreviewExpired.htm) | Raised whenever the display (in the Rhino viewports) of a certain object becomes invalid. |
| Public event | [SolutionExpired](E_Grasshopper_Kernel_IGH_DocumentObject_SolutionExpired.htm) | Raised whenever the solution of a certain object becomes invalid. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)