# Methods_T_Grasshopper_Kernel_GH_ActiveObject

﻿ GH\_ActiveObject Methods

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_ActiveObject Class](../html/T_Grasshopper_Kernel_GH_ActiveObject.htm "GH_ActiveObject Class")

[GH\_ActiveObject Methods](../html/Methods_T_Grasshopper_Kernel_GH_ActiveObject.htm "GH_ActiveObject Methods")

[AddRuntimeMessage Method](../html/M_Grasshopper_Kernel_GH_ActiveObject_AddRuntimeMessage.htm "AddRuntimeMessage Method ")

[AppendAdditionalMenuItems Method](../html/M_Grasshopper_Kernel_GH_ActiveObject_AppendAdditionalMenuItems.htm "AppendAdditionalMenuItems Method ")

[AppendMenuItems Method](../html/M_Grasshopper_Kernel_GH_ActiveObject_AppendMenuItems.htm "AppendMenuItems Method ")

[ClearData Method](../html/M_Grasshopper_Kernel_GH_ActiveObject_ClearData.htm "ClearData Method ")

[ClearRuntimeMessages Method](../html/M_Grasshopper_Kernel_GH_ActiveObject_ClearRuntimeMessages.htm "ClearRuntimeMessages Method ")

[CollectData Method](../html/M_Grasshopper_Kernel_GH_ActiveObject_CollectData.htm "CollectData Method ")

[ComputeData Method](../html/M_Grasshopper_Kernel_GH_ActiveObject_ComputeData.htm "ComputeData Method ")

[DependsOn Method](../html/M_Grasshopper_Kernel_GH_ActiveObject_DependsOn.htm "DependsOn Method ")

[ExpireDownStreamObjects Method](../html/M_Grasshopper_Kernel_GH_ActiveObject_ExpireDownStreamObjects.htm "ExpireDownStreamObjects Method ")

[ExpireSolution Method](../html/M_Grasshopper_Kernel_GH_ActiveObject_ExpireSolution.htm "ExpireSolution Method ")

[Menu\_AppendBakeItem Method](../html/M_Grasshopper_Kernel_GH_ActiveObject_Menu_AppendBakeItem.htm "Menu_AppendBakeItem Method ")

[Menu\_AppendEnableItem Method](../html/M_Grasshopper_Kernel_GH_ActiveObject_Menu_AppendEnableItem.htm "Menu_AppendEnableItem Method ")

[Menu\_AppendPreviewItem Method](../html/M_Grasshopper_Kernel_GH_ActiveObject_Menu_AppendPreviewItem.htm "Menu_AppendPreviewItem Method ")

[Menu\_AppendRuntimeMessages Method](../html/M_Grasshopper_Kernel_GH_ActiveObject_Menu_AppendRuntimeMessages.htm "Menu_AppendRuntimeMessages Method ")

[Read Method](../html/M_Grasshopper_Kernel_GH_ActiveObject_Read.htm "Read Method ")

[RegisterRemoteIDs Method](../html/M_Grasshopper_Kernel_GH_ActiveObject_RegisterRemoteIDs.htm "RegisterRemoteIDs Method ")

[RuntimeMessages Method](../html/M_Grasshopper_Kernel_GH_ActiveObject_RuntimeMessages.htm "RuntimeMessages Method ")

[SDKCompliancy Method](../html/M_Grasshopper_Kernel_GH_ActiveObject_SDKCompliancy.htm "SDKCompliancy Method ")

[Write Method](../html/M_Grasshopper_Kernel_GH_ActiveObject_Write.htm "Write Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ActiveObject Methods |

The [GH\_ActiveObject](T_Grasshopper_Kernel_GH_ActiveObject.htm) type exposes the following members.

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [AddedToDocument](M_Grasshopper_Kernel_GH_DocumentObject_AddedToDocument.htm) | This method will be called when an object is added to a document. Override this method if you want to handle such events. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Public method | [AddRuntimeMessage](M_Grasshopper_Kernel_GH_ActiveObject_AddRuntimeMessage.htm) | Add a new message to this object. Valid message type flags are Warning and Error. If the Message string is empty or zero-length no message is added. |
| Public method | [AppendAdditionalMenuItems](M_Grasshopper_Kernel_GH_ActiveObject_AppendAdditionalMenuItems.htm) | Override this function if you want to add additional items to the object context menu. Default items already included in the menu toolstrip are: 1. Name  2. Preview  3. Warnings  4. Errors  5. [additional items will be inserted here]  6. Help |
| Public method | [AppendMenuItems](M_Grasshopper_Kernel_GH_ActiveObject_AppendMenuItems.htm) | This function is called when a context menu is about to be displayed. Override it to set custom items. GH\_ActiveObject will already populate the menu with default items, if you merely wish to insert object-specific menu item, consider overriding AppendAdditionalMenuItems instead. (Overrides [GH\_DocumentObjectAddLanguageSpecificTextSet("LST89EE971D\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");AppendMenuItems(ToolStripDropDown)](M_Grasshopper_Kernel_GH_DocumentObject_AppendMenuItems.htm).) |
| Public method | [ClearData](M_Grasshopper_Kernel_GH_ActiveObject_ClearData.htm) | This function is called whenever the object needs to clear all solution data. Override this function if you need to perform custom clensing. |
| Public method | [ClearRuntimeMessages](M_Grasshopper_Kernel_GH_ActiveObject_ClearRuntimeMessages.htm) | Destroy all warning and error lists |
| Public method | [CollectData](M_Grasshopper_Kernel_GH_ActiveObject_CollectData.htm) | This function is called whenever the object is required to collect all data. Either from Persistent records, from source params or whatever. |
| Public method | [ComputeData](M_Grasshopper_Kernel_GH_ActiveObject_ComputeData.htm) | This function is called whenever the object is required to generate new data. |
| Public method | [CopyFrom](M_Grasshopper_Kernel_GH_InstanceDescription_CopyFrom.htm) | Copy all fields (except the instance ID) from another instance description. (Inherited from [GH\_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).) |
| Public method | [CreateAttributes](M_Grasshopper_Kernel_GH_DocumentObject_CreateAttributes.htm) | This function creates the stand-alone attributes for this object. If you wish to supply your own Attributes, you must override this function. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Public method | [DependsOn](M_Grasshopper_Kernel_GH_ActiveObject_DependsOn.htm) | Returns a boolean indicating whether or not the current object somehow inherits from the PotenialSource object |
| Protected method | [DestroyIconCache](M_Grasshopper_Kernel_GH_DocumentObject_DestroyIconCache.htm) | Call this method to erase the existing icon cache. You must call this if you want to change the display icon of an object. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Public method | [DocumentContextChanged](M_Grasshopper_Kernel_GH_DocumentObject_DocumentContextChanged.htm) | This method will be called when the document that owns this object moves into a different context. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Protected method | [ExpireDownStreamObjects](M_Grasshopper_Kernel_GH_ActiveObject_ExpireDownStreamObjects.htm) | This function is called whenever the solution for this object expires. Override this function if objects depend on you. |
| Public method | [ExpirePreview](M_Grasshopper_Kernel_GH_DocumentObject_ExpirePreview.htm) | Call this function when you suspect that the preview has expired for this object. This will cause the display cache to be eradicated. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Public method | [ExpireSolution](M_Grasshopper_Kernel_GH_ActiveObject_ExpireSolution.htm) | Informs the document that owns this object that the solution has expired. The current object will be set to BLANK as a result. This method is recursive, it will also expire any and all objects which depend on this object. If you want a less destructive expiration, consider using ClearData(). If this object is already Blank, you should consider not expiring it. (Overrides [GH\_DocumentObjectAddLanguageSpecificTextSet("LST89EE971D\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");ExpireSolution(Boolean)](M_Grasshopper_Kernel_GH_DocumentObject_ExpireSolution.htm).) |
| Protected method | [GetValue(String, Boolean)](M_Grasshopper_Kernel_GH_DocumentObject_GetValue.htm) | Get a boolean value from the component value table. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Protected method | [GetValue(String, Double)](M_Grasshopper_Kernel_GH_DocumentObject_GetValue_1.htm) | Get a double value from the component value table. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Protected method | [GetValue(String, Color)](M_Grasshopper_Kernel_GH_DocumentObject_GetValue_2.htm) | Get a color value from the component value table. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Protected method | [GetValue(String, Int32)](M_Grasshopper_Kernel_GH_DocumentObject_GetValue_3.htm) | Get an integer value from the component value table. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Protected method | [GetValue(String, String)](M_Grasshopper_Kernel_GH_DocumentObject_GetValue_4.htm) | Get a string value from the component value table. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Protected method | [HtmlHelp\_Source](M_Grasshopper_Kernel_GH_DocumentObject_HtmlHelp_Source.htm) | Return a String which contains HTML formatted source for the help topic. If you want to pass a URL that points to a remote page, then prefix the URL with a GOTO: tag, like so: GOTO:http://www.YourWebAddressHere.com (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Public method | [IsolateObject](M_Grasshopper_Kernel_GH_DocumentObject_IsolateObject.htm) | Destroy all connections to other objects. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Protected method | [Menu\_AppendBakeItem](M_Grasshopper_Kernel_GH_ActiveObject_Menu_AppendBakeItem.htm) | Append the default Bake menu item. |
| Protected method | [Menu\_AppendEnableItem](M_Grasshopper_Kernel_GH_ActiveObject_Menu_AppendEnableItem.htm) | Append the default Enable/Disable menu item. |
| Protected method | [Menu\_AppendObjectHelp](M_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendObjectHelp.htm) | Appends the default object Help menu item. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Protected method | [Menu\_AppendObjectName](M_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendObjectName.htm) | Appends the old-fashioned object name menu item. If you also want the Display mode toggle then use Menu\_AppendObjectNameEx() (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Protected method | [Menu\_AppendObjectNameEx](M_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendObjectNameEx.htm) | Appends the default object name + display mode menu item. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Protected method | [Menu\_AppendPreviewItem](M_Grasshopper_Kernel_GH_ActiveObject_Menu_AppendPreviewItem.htm) | Append the default Show/Hide preview menu item. |
| Protected method | [Menu\_AppendPublish](M_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendPublish.htm) | Appends the default item for publishing to RCP. This menu will only appear if the current class implement IRcpAwareObject (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Protected method | [Menu\_AppendRuntimeMessages](M_Grasshopper_Kernel_GH_ActiveObject_Menu_AppendRuntimeMessages.htm) | Append the default warnings and errors menu items. |
| Public method | [MovedBetweenDocuments](M_Grasshopper_Kernel_GH_DocumentObject_MovedBetweenDocuments.htm) | This method will be called when an object is moved from one document to another. Override this method if you want to handle such events. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Public method | [NewInstanceGuidAddLanguageSpecificTextSet("LST89EE971D\_2?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_GH_InstanceDescription_NewInstanceGuid.htm) | Generate a new random instance GUID (Inherited from [GH\_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).) |
| Public method | [NewInstanceGuid(Guid)](M_Grasshopper_Kernel_GH_InstanceDescription_NewInstanceGuid_1.htm) | Set the instance ID to be a specific GUID. This is very dangerous, only use this function if you're 6"4' and your first name is David. (Inherited from [GH\_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).) |
| Public method | [OnAttributesChanged](M_Grasshopper_Kernel_GH_DocumentObject_OnAttributesChanged.htm) | Raises the AttributesChanged event on the toplevel object. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Public method | [OnDisplayExpired](M_Grasshopper_Kernel_GH_DocumentObject_OnDisplayExpired.htm) | Raises the DisplayExpired event on the toplevel object. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Public method | [OnObjectChanged(GH\_ObjectChangedEventArgs)](M_Grasshopper_Kernel_GH_DocumentObject_OnObjectChanged.htm) | (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Public method | [OnObjectChanged(GH\_ObjectEventType)](M_Grasshopper_Kernel_GH_DocumentObject_OnObjectChanged_1.htm) | (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Public method | [OnObjectChanged(String)](M_Grasshopper_Kernel_GH_DocumentObject_OnObjectChanged_3.htm) | (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Public method | [OnObjectChanged(GH\_ObjectEventType, Object)](M_Grasshopper_Kernel_GH_DocumentObject_OnObjectChanged_2.htm) | (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Public method | [OnObjectChanged(String, Object)](M_Grasshopper_Kernel_GH_DocumentObject_OnObjectChanged_4.htm) | (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Public method | [OnPingDocument](M_Grasshopper_Kernel_GH_DocumentObject_OnPingDocument.htm) | Raise the PingDocument Event on the toplevel object and try to find the document which owns this object. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Public method | [OnPreviewExpired](M_Grasshopper_Kernel_GH_DocumentObject_OnPreviewExpired.htm) | Raises the PreviewExpired event on the toplevel object. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Public method | [OnSolutionExpired](M_Grasshopper_Kernel_GH_DocumentObject_OnSolutionExpired.htm) | Raises the SolutionExpired event on the toplevel object. You probably want to call ExpireSolution() instead of this method directly. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Public method | [Read](M_Grasshopper_Kernel_GH_ActiveObject_Read.htm) | (Overrides [GH\_DocumentObjectAddLanguageSpecificTextSet("LST89EE971D\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Read(GH\_IReader)](M_Grasshopper_Kernel_GH_DocumentObject_Read.htm).) |
| Public method | [ReadFull](M_Grasshopper_Kernel_GH_InstanceDescription_ReadFull.htm) | GH\_InstanceDescription does not by default serialize all fields. Use this function to read *all* fields from the archive. This method is compatible with the default Write()/Read() operations. (Inherited from [GH\_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).) |
| Public method | [RecordUndoEvent(GH\_UndoRecord)](M_Grasshopper_Kernel_GH_DocumentObject_RecordUndoEvent.htm) | Record an entire undo record. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Public method | [RecordUndoEvent(String)](M_Grasshopper_Kernel_GH_DocumentObject_RecordUndoEvent_1.htm) | Record a generic object change undo event. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Public method | [RecordUndoEvent(String, IGH\_UndoAction)](M_Grasshopper_Kernel_GH_DocumentObject_RecordUndoEvent_2.htm) | Record a specific object change undo event. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Public method | [RegisterRemoteIDs](M_Grasshopper_Kernel_GH_ActiveObject_RegisterRemoteIDs.htm) | Override this function if you want object changes in the Rhino document to trigger a new solution. |
| Public method | [RemovedFromDocument](M_Grasshopper_Kernel_GH_DocumentObject_RemovedFromDocument.htm) | This method will be called when an object is removed from a document. Override this method if you want to handle such events. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Public method | [RuntimeMessages](M_Grasshopper_Kernel_GH_ActiveObject_RuntimeMessages.htm) | Gets the list of cached runtime messages that were recorded during solver-time processes. |
| Public method | [SDKCompliancy](M_Grasshopper_Kernel_GH_ActiveObject_SDKCompliancy.htm) | Test whether this object is compliant with a given Rhino version. |
| Public method | [SetIconOverride](M_Grasshopper_Kernel_GH_DocumentObject_SetIconOverride.htm) | Set a new custom icon override for this object. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Protected method | [SetValue(String, Boolean)](M_Grasshopper_Kernel_GH_DocumentObject_SetValue.htm) | Set a named value. This value will be serialized with the component. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Protected method | [SetValue(String, Double)](M_Grasshopper_Kernel_GH_DocumentObject_SetValue_1.htm) | Set a named value. This value will be serialized with the component. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Protected method | [SetValue(String, Color)](M_Grasshopper_Kernel_GH_DocumentObject_SetValue_2.htm) | Set a named value. This value will be serialized with the component. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Protected method | [SetValue(String, Int32)](M_Grasshopper_Kernel_GH_DocumentObject_SetValue_3.htm) | Set a named value. This value will be serialized with the component. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Protected method | [SetValue(String, String)](M_Grasshopper_Kernel_GH_DocumentObject_SetValue_4.htm) | Set a named value. This value will be serialized with the component. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Public method | [TriggerAutoSaveAddLanguageSpecificTextSet("LST89EE971D\_4?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_GH_DocumentObject_TriggerAutoSave.htm) | Triggers the AutoSave function on the owner document with the object\_changed flag. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Public method | [TriggerAutoSave(GH\_AutoSaveTrigger)](M_Grasshopper_Kernel_GH_DocumentObject_TriggerAutoSave_1.htm) | Triggers the AutoSave function on the owner document with a custom flag. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Public method | [TriggerAutoSave(Guid)](M_Grasshopper_Kernel_GH_DocumentObject_TriggerAutoSave_3.htm) | Triggers the AutoSave function on the owner document with the object\_changed flag. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Public method | [TriggerAutoSave(GH\_AutoSaveTrigger, Guid)](M_Grasshopper_Kernel_GH_DocumentObject_TriggerAutoSave_2.htm) | Triggers the AutoSave function on the owner document with a custom flag. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Protected method | [ValuesChanged](M_Grasshopper_Kernel_GH_DocumentObject_ValuesChanged.htm) | Override this method if you want to respond to changes to the value table. The base implementation is empty, so you don't have to call it. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Public method | [Write](M_Grasshopper_Kernel_GH_ActiveObject_Write.htm) | (Overrides [GH\_DocumentObjectAddLanguageSpecificTextSet("LST89EE971D\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");Write(GH\_IWriter)](M_Grasshopper_Kernel_GH_DocumentObject_Write.htm).) |
| Public method | [WriteFull](M_Grasshopper_Kernel_GH_InstanceDescription_WriteFull.htm) | GH\_InstanceDescription does not by default serialize all fields. Use this function to write *all* fields to the archive. This method is compatible with the default Write()/Read() operations. (Inherited from [GH\_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_ActiveObject Class](T_Grasshopper_Kernel_GH_ActiveObject.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)