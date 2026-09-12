# Methods_T_Grasshopper_Kernel_GH_Component

﻿ GH\_Component Methods

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_Component Class](../html/T_Grasshopper_Kernel_GH_Component.htm "GH_Component Class")

[GH\_Component Methods](../html/Methods_T_Grasshopper_Kernel_GH_Component.htm "GH_Component Methods")

[AddedToDocument Method](../html/M_Grasshopper_Kernel_GH_Component_AddedToDocument.htm "AddedToDocument Method ")

[AfterSolveInstance Method](../html/M_Grasshopper_Kernel_GH_Component_AfterSolveInstance.htm "AfterSolveInstance Method ")

[AppendAdditionalComponentMenuItems Method](../html/M_Grasshopper_Kernel_GH_Component_AppendAdditionalComponentMenuItems.htm "AppendAdditionalComponentMenuItems Method ")

[AppendAdditionalMenuItems Method](../html/M_Grasshopper_Kernel_GH_Component_AppendAdditionalMenuItems.htm "AppendAdditionalMenuItems Method ")

[AssignInitCodeToInputParameter Method](../html/M_Grasshopper_Kernel_GH_Component_AssignInitCodeToInputParameter.htm "AssignInitCodeToInputParameter Method ")

[BakeGeometry Method](../html/Overload_Grasshopper_Kernel_GH_Component_BakeGeometry.htm "BakeGeometry Method ")

[BeforeSolveInstance Method](../html/M_Grasshopper_Kernel_GH_Component_BeforeSolveInstance.htm "BeforeSolveInstance Method ")

[ClearData Method](../html/M_Grasshopper_Kernel_GH_Component_ClearData.htm "ClearData Method ")

[ClearRuntimeMessages Method](../html/M_Grasshopper_Kernel_GH_Component_ClearRuntimeMessages.htm "ClearRuntimeMessages Method ")

[CollectData Method](../html/M_Grasshopper_Kernel_GH_Component_CollectData.htm "CollectData Method ")

[ComputeData Method](../html/M_Grasshopper_Kernel_GH_Component_ComputeData.htm "ComputeData Method ")

[CreateAttributes Method](../html/M_Grasshopper_Kernel_GH_Component_CreateAttributes.htm "CreateAttributes Method ")

[DependsOn Method](../html/M_Grasshopper_Kernel_GH_Component_DependsOn.htm "DependsOn Method ")

[DocumentAngleTolerance Method](../html/M_Grasshopper_Kernel_GH_Component_DocumentAngleTolerance.htm "DocumentAngleTolerance Method ")

[DocumentContextChanged Method](../html/M_Grasshopper_Kernel_GH_Component_DocumentContextChanged.htm "DocumentContextChanged Method ")

[DocumentTolerance Method](../html/M_Grasshopper_Kernel_GH_Component_DocumentTolerance.htm "DocumentTolerance Method ")

[DrawViewportMeshes Method](../html/M_Grasshopper_Kernel_GH_Component_DrawViewportMeshes.htm "DrawViewportMeshes Method ")

[DrawViewportWires Method](../html/M_Grasshopper_Kernel_GH_Component_DrawViewportWires.htm "DrawViewportWires Method ")

[ExpireDownStreamObjects Method](../html/M_Grasshopper_Kernel_GH_Component_ExpireDownStreamObjects.htm "ExpireDownStreamObjects Method ")

[GenerateDefaultHTML Method](../html/M_Grasshopper_Kernel_GH_Component_GenerateDefaultHTML.htm "GenerateDefaultHTML Method ")

[GenerateParameterHelp Method](../html/Overload_Grasshopper_Kernel_GH_Component_GenerateParameterHelp.htm "GenerateParameterHelp Method ")

[HtmlHelp\_Source Method](../html/M_Grasshopper_Kernel_GH_Component_HtmlHelp_Source.htm "HtmlHelp_Source Method ")

[IsolateObject Method](../html/M_Grasshopper_Kernel_GH_Component_IsolateObject.htm "IsolateObject Method ")

[MovedBetweenDocuments Method](../html/M_Grasshopper_Kernel_GH_Component_MovedBetweenDocuments.htm "MovedBetweenDocuments Method ")

[PostConstructor Method](../html/M_Grasshopper_Kernel_GH_Component_PostConstructor.htm "PostConstructor Method ")

[Read Method](../html/M_Grasshopper_Kernel_GH_Component_Read.htm "Read Method ")

[RegisterInputParams Method](../html/M_Grasshopper_Kernel_GH_Component_RegisterInputParams.htm "RegisterInputParams Method ")

[RegisterOutputParams Method](../html/M_Grasshopper_Kernel_GH_Component_RegisterOutputParams.htm "RegisterOutputParams Method ")

[RegisterRemoteIDs Method](../html/M_Grasshopper_Kernel_GH_Component_RegisterRemoteIDs.htm "RegisterRemoteIDs Method ")

[RemovedFromDocument Method](../html/M_Grasshopper_Kernel_GH_Component_RemovedFromDocument.htm "RemovedFromDocument Method ")

[RuntimeMessages Method](../html/M_Grasshopper_Kernel_GH_Component_RuntimeMessages.htm "RuntimeMessages Method ")

[SolveInstance Method](../html/M_Grasshopper_Kernel_GH_Component_SolveInstance.htm "SolveInstance Method ")

[Write Method](../html/M_Grasshopper_Kernel_GH_Component_Write.htm "Write Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_Component Methods |

The [GH\_Component](T_Grasshopper_Kernel_GH_Component.htm) type exposes the following members.

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [AddedToDocument](M_Grasshopper_Kernel_GH_Component_AddedToDocument.htm) | Overrides the AddedToDocument method and delegates the call to all parameters. (Overrides [GH\_DocumentObjectAddLanguageSpecificTextSet("LSTD04B890A\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");AddedToDocument(GH\_Document)](M_Grasshopper_Kernel_GH_DocumentObject_AddedToDocument.htm).) |
| Public method | [AddRuntimeMessage](M_Grasshopper_Kernel_GH_ActiveObject_AddRuntimeMessage.htm) | Add a new message to this object. Valid message type flags are Warning and Error. If the Message string is empty or zero-length no message is added. (Inherited from [GH\_ActiveObject](T_Grasshopper_Kernel_GH_ActiveObject.htm).) |
| Protected method | [AfterSolveInstance](M_Grasshopper_Kernel_GH_Component_AfterSolveInstance.htm) | Override this method if you want to be called after the last call to SolveInstance. |
| Protected method | [AppendAdditionalComponentMenuItems](M_Grasshopper_Kernel_GH_Component_AppendAdditionalComponentMenuItems.htm) | Override this function if you want to insert some custom menu items in your derived Component class. Items will be added between List Matching items and parameter menus. |
| Public method | [AppendAdditionalMenuItems](M_Grasshopper_Kernel_GH_Component_AppendAdditionalMenuItems.htm) | Adds typical component type items to the context menu: 1. Data comparison types 2. Custom (overridden) items 3. Nested input parameter context menu items 4. Nested output parameter context menu items (Overrides [GH\_ActiveObjectAddLanguageSpecificTextSet("LSTD04B890A\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");AppendAdditionalMenuItems(ToolStripDropDown)](M_Grasshopper_Kernel_GH_ActiveObject_AppendAdditionalMenuItems.htm).) |
| Public method | [AppendMenuItems](M_Grasshopper_Kernel_GH_ActiveObject_AppendMenuItems.htm) | This function is called when a context menu is about to be displayed. Override it to set custom items. GH\_ActiveObject will already populate the menu with default items, if you merely wish to insert object-specific menu item, consider overriding AppendAdditionalMenuItems instead. (Inherited from [GH\_ActiveObject](T_Grasshopper_Kernel_GH_ActiveObject.htm).) |
| Protected method | [AssignInitCodeToInputParameter](M_Grasshopper_Kernel_GH_Component_AssignInitCodeToInputParameter.htm) | Utility function for parsing and assigning init codes. This only works for standard parameter types. |
| Public method | [BakeGeometry(RhinoDoc, ListAddLanguageSpecificTextSet("LSTD04B890A\_2?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");GuidAddLanguageSpecificTextSet("LSTD04B890A\_3?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");)](M_Grasshopper_Kernel_GH_Component_BakeGeometry_1.htm) |  |
| Public method | [BakeGeometry(RhinoDoc, ObjectAttributes, ListAddLanguageSpecificTextSet("LSTD04B890A\_4?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");GuidAddLanguageSpecificTextSet("LSTD04B890A\_5?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");)](M_Grasshopper_Kernel_GH_Component_BakeGeometry.htm) |  |
| Protected method | [BeforeSolveInstance](M_Grasshopper_Kernel_GH_Component_BeforeSolveInstance.htm) | Override this method if you want to be called before the first call to SolveInstance. |
| Public method | [ClearData](M_Grasshopper_Kernel_GH_Component_ClearData.htm) | Clear the data inside this component and all output parameters. (Overrides [GH\_ActiveObjectAddLanguageSpecificTextSet("LSTD04B890A\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");ClearDataAddLanguageSpecificTextSet("LSTD04B890A\_7?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_GH_ActiveObject_ClearData.htm).) |
| Public method | [ClearRuntimeMessages](M_Grasshopper_Kernel_GH_Component_ClearRuntimeMessages.htm) | Clears all runtime messages in me and my parameters (Overrides [GH\_ActiveObjectAddLanguageSpecificTextSet("LSTD04B890A\_8?cs=.|vb=.|cpp=::|nu=.|fs=.");ClearRuntimeMessagesAddLanguageSpecificTextSet("LSTD04B890A\_9?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_GH_ActiveObject_ClearRuntimeMessages.htm).) |
| Public method | [CollectData](M_Grasshopper_Kernel_GH_Component_CollectData.htm) | Calls CollectData on all input parameters and makes sure the Component and all associated parameters are left in a valid state. (Overrides [GH\_ActiveObjectAddLanguageSpecificTextSet("LSTD04B890A\_10?cs=.|vb=.|cpp=::|nu=.|fs=.");CollectDataAddLanguageSpecificTextSet("LSTD04B890A\_11?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_GH_ActiveObject_CollectData.htm).) |
| Public method | [ComputeData](M_Grasshopper_Kernel_GH_Component_ComputeData.htm) | Compute all data and fill out all output parameters. (Overrides [GH\_ActiveObjectAddLanguageSpecificTextSet("LSTD04B890A\_12?cs=.|vb=.|cpp=::|nu=.|fs=.");ComputeDataAddLanguageSpecificTextSet("LSTD04B890A\_13?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_GH_ActiveObject_ComputeData.htm).) |
| Public method | [CopyFrom](M_Grasshopper_Kernel_GH_InstanceDescription_CopyFrom.htm) | Copy all fields (except the instance ID) from another instance description. (Inherited from [GH\_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).) |
| Public method | [CreateAttributes](M_Grasshopper_Kernel_GH_Component_CreateAttributes.htm) | Create new attributes. (Overrides [GH\_DocumentObjectAddLanguageSpecificTextSet("LSTD04B890A\_14?cs=.|vb=.|cpp=::|nu=.|fs=.");CreateAttributesAddLanguageSpecificTextSet("LSTD04B890A\_15?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_GH_DocumentObject_CreateAttributes.htm).) |
| Public method | [DependsOn](M_Grasshopper_Kernel_GH_Component_DependsOn.htm) | Returns True is any one of my input parameters depends on the source. (Overrides [GH\_ActiveObjectAddLanguageSpecificTextSet("LSTD04B890A\_16?cs=.|vb=.|cpp=::|nu=.|fs=.");DependsOn(IGH\_ActiveObject)](M_Grasshopper_Kernel_GH_ActiveObject_DependsOn.htm).) |
| Protected method | [DestroyIconCache](M_Grasshopper_Kernel_GH_DocumentObject_DestroyIconCache.htm) | Call this method to erase the existing icon cache. You must call this if you want to change the display icon of an object. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Protected methodStatic member | [DocumentAngleTolerance](M_Grasshopper_Kernel_GH_Component_DocumentAngleTolerance.htm) | Gets the Angle tolerance (in radians) for the currently active Rhino document. |
| Public method | [DocumentContextChanged](M_Grasshopper_Kernel_GH_Component_DocumentContextChanged.htm) | Overrides the DocumentContextChanged method and delegates the call to all parameters. (Overrides [GH\_DocumentObjectAddLanguageSpecificTextSet("LSTD04B890A\_17?cs=.|vb=.|cpp=::|nu=.|fs=.");DocumentContextChanged(GH\_Document, GH\_DocumentContext)](M_Grasshopper_Kernel_GH_DocumentObject_DocumentContextChanged.htm).) |
| Protected methodStatic member | [DocumentTolerance](M_Grasshopper_Kernel_GH_Component_DocumentTolerance.htm) | Gets the Absolute tolerance for the currently active Rhino document. |
| Public method | [DrawViewportMeshes](M_Grasshopper_Kernel_GH_Component_DrawViewportMeshes.htm) | Draw preview meshes for this component and all associated parameters. |
| Public method | [DrawViewportWires](M_Grasshopper_Kernel_GH_Component_DrawViewportWires.htm) | Draw preview wires for this component and all associated parameters. |
| Protected method | [ExpireDownStreamObjects](M_Grasshopper_Kernel_GH_Component_ExpireDownStreamObjects.htm) | Expire all objects that depend on any of the output parameters. (Overrides [GH\_ActiveObjectAddLanguageSpecificTextSet("LSTD04B890A\_18?cs=.|vb=.|cpp=::|nu=.|fs=.");ExpireDownStreamObjectsAddLanguageSpecificTextSet("LSTD04B890A\_19?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_GH_ActiveObject_ExpireDownStreamObjects.htm).) |
| Public method | [ExpirePreview](M_Grasshopper_Kernel_GH_DocumentObject_ExpirePreview.htm) | Call this function when you suspect that the preview has expired for this object. This will cause the display cache to be eradicated. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Public method | [ExpireSolution](M_Grasshopper_Kernel_GH_ActiveObject_ExpireSolution.htm) | Informs the document that owns this object that the solution has expired. The current object will be set to BLANK as a result. This method is recursive, it will also expire any and all objects which depend on this object. If you want a less destructive expiration, consider using ClearData(). If this object is already Blank, you should consider not expiring it. (Inherited from [GH\_ActiveObject](T_Grasshopper_Kernel_GH_ActiveObject.htm).) |
| Protected method | [GenerateDefaultHTML](M_Grasshopper_Kernel_GH_Component_GenerateDefaultHTML.htm) | Creates the default component help topic, including all parameter lists. |
| Protected method | [GenerateParameterHelpAddLanguageSpecificTextSet("LSTD04B890A\_20?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_GH_Component_GenerateParameterHelp.htm) | Create an HTML string that lists names and descriptions for input and output parameters. |
| Protected method | [GenerateParameterHelp(IGH\_Param)](M_Grasshopper_Kernel_GH_Component_GenerateParameterHelp_1.htm) | Generate HTML string for a single parameter. |
| Protected method | [GetValue(String, Boolean)](M_Grasshopper_Kernel_GH_DocumentObject_GetValue.htm) | Get a boolean value from the component value table. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Protected method | [GetValue(String, Double)](M_Grasshopper_Kernel_GH_DocumentObject_GetValue_1.htm) | Get a double value from the component value table. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Protected method | [GetValue(String, Color)](M_Grasshopper_Kernel_GH_DocumentObject_GetValue_2.htm) | Get a color value from the component value table. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Protected method | [GetValue(String, Int32)](M_Grasshopper_Kernel_GH_DocumentObject_GetValue_3.htm) | Get an integer value from the component value table. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Protected method | [GetValue(String, String)](M_Grasshopper_Kernel_GH_DocumentObject_GetValue_4.htm) | Get a string value from the component value table. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Protected method | [HtmlHelp\_Source](M_Grasshopper_Kernel_GH_Component_HtmlHelp_Source.htm) | Return a String which contains HTML formatted source for the help topic. If you want to pass a URL that points to a remote page, then prefix the URL with a GOTO: tag, like so: GOTO:http://www.YourWebAddressHere.com (Overrides [GH\_DocumentObjectAddLanguageSpecificTextSet("LSTD04B890A\_21?cs=.|vb=.|cpp=::|nu=.|fs=.");HtmlHelp\_SourceAddLanguageSpecificTextSet("LSTD04B890A\_22?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_GH_DocumentObject_HtmlHelp_Source.htm).) |
| Public method | [IsolateObject](M_Grasshopper_Kernel_GH_Component_IsolateObject.htm) | Sever the connections of all input and output parameters. (Overrides [GH\_DocumentObjectAddLanguageSpecificTextSet("LSTD04B890A\_23?cs=.|vb=.|cpp=::|nu=.|fs=.");IsolateObjectAddLanguageSpecificTextSet("LSTD04B890A\_24?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_GH_DocumentObject_IsolateObject.htm).) |
| Protected method | [Menu\_AppendBakeItem](M_Grasshopper_Kernel_GH_ActiveObject_Menu_AppendBakeItem.htm) | Append the default Bake menu item. (Inherited from [GH\_ActiveObject](T_Grasshopper_Kernel_GH_ActiveObject.htm).) |
| Protected method | [Menu\_AppendEnableItem](M_Grasshopper_Kernel_GH_ActiveObject_Menu_AppendEnableItem.htm) | Append the default Enable/Disable menu item. (Inherited from [GH\_ActiveObject](T_Grasshopper_Kernel_GH_ActiveObject.htm).) |
| Protected method | [Menu\_AppendObjectHelp](M_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendObjectHelp.htm) | Appends the default object Help menu item. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Protected method | [Menu\_AppendObjectName](M_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendObjectName.htm) | Appends the old-fashioned object name menu item. If you also want the Display mode toggle then use Menu\_AppendObjectNameEx() (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Protected method | [Menu\_AppendObjectNameEx](M_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendObjectNameEx.htm) | Appends the default object name + display mode menu item. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Protected method | [Menu\_AppendPreviewItem](M_Grasshopper_Kernel_GH_ActiveObject_Menu_AppendPreviewItem.htm) | Append the default Show/Hide preview menu item. (Inherited from [GH\_ActiveObject](T_Grasshopper_Kernel_GH_ActiveObject.htm).) |
| Protected method | [Menu\_AppendPublish](M_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendPublish.htm) | Appends the default item for publishing to RCP. This menu will only appear if the current class implement IRcpAwareObject (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Protected method | [Menu\_AppendRuntimeMessages](M_Grasshopper_Kernel_GH_ActiveObject_Menu_AppendRuntimeMessages.htm) | Append the default warnings and errors menu items. (Inherited from [GH\_ActiveObject](T_Grasshopper_Kernel_GH_ActiveObject.htm).) |
| Public method | [MovedBetweenDocuments](M_Grasshopper_Kernel_GH_Component_MovedBetweenDocuments.htm) | Overrides the MovedBetweenDocuments method and delegates the call to all parameters. (Overrides [GH\_DocumentObjectAddLanguageSpecificTextSet("LSTD04B890A\_25?cs=.|vb=.|cpp=::|nu=.|fs=.");MovedBetweenDocuments(GH\_Document, GH\_Document)](M_Grasshopper_Kernel_GH_DocumentObject_MovedBetweenDocuments.htm).) |
| Public method | [NewInstanceGuidAddLanguageSpecificTextSet("LSTD04B890A\_26?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_GH_InstanceDescription_NewInstanceGuid.htm) | Generate a new random instance GUID (Inherited from [GH\_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).) |
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
| Protected method | [PostConstructor](M_Grasshopper_Kernel_GH_Component_PostConstructor.htm) | The PostConstructor is called from within each constructor. DO NOT OVERRIDE THIS unless you know what you are doing. |
| Public method | [Read](M_Grasshopper_Kernel_GH_Component_Read.htm) | Read all required data for deserialization from an IO archive. (Overrides [GH\_ActiveObjectAddLanguageSpecificTextSet("LSTD04B890A\_27?cs=.|vb=.|cpp=::|nu=.|fs=.");Read(GH\_IReader)](M_Grasshopper_Kernel_GH_ActiveObject_Read.htm).) |
| Public method | [ReadFull](M_Grasshopper_Kernel_GH_InstanceDescription_ReadFull.htm) | GH\_InstanceDescription does not by default serialize all fields. Use this function to read *all* fields from the archive. This method is compatible with the default Write()/Read() operations. (Inherited from [GH\_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).) |
| Public method | [RecordUndoEvent(GH\_UndoRecord)](M_Grasshopper_Kernel_GH_DocumentObject_RecordUndoEvent.htm) | Record an entire undo record. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Public method | [RecordUndoEvent(String)](M_Grasshopper_Kernel_GH_DocumentObject_RecordUndoEvent_1.htm) | Record a generic object change undo event. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Public method | [RecordUndoEvent(String, IGH\_UndoAction)](M_Grasshopper_Kernel_GH_DocumentObject_RecordUndoEvent_2.htm) | Record a specific object change undo event. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Protected method | [RegisterInputParams](M_Grasshopper_Kernel_GH_Component_RegisterInputParams.htm) | Declare all your input parameters here. |
| Protected method | [RegisterOutputParams](M_Grasshopper_Kernel_GH_Component_RegisterOutputParams.htm) | Declare all your output parameters here. |
| Public method | [RegisterRemoteIDs](M_Grasshopper_Kernel_GH_Component_RegisterRemoteIDs.htm) | Registers all my input parameters with the UUID\_LookUpTable (Overrides [GH\_ActiveObjectAddLanguageSpecificTextSet("LSTD04B890A\_28?cs=.|vb=.|cpp=::|nu=.|fs=.");RegisterRemoteIDs(GH\_GuidTable)](M_Grasshopper_Kernel_GH_ActiveObject_RegisterRemoteIDs.htm).) |
| Public method | [RemovedFromDocument](M_Grasshopper_Kernel_GH_Component_RemovedFromDocument.htm) | Overrides the RemovedFromDocument method and delegates the call to all parameters. (Overrides [GH\_DocumentObjectAddLanguageSpecificTextSet("LSTD04B890A\_29?cs=.|vb=.|cpp=::|nu=.|fs=.");RemovedFromDocument(GH\_Document)](M_Grasshopper_Kernel_GH_DocumentObject_RemovedFromDocument.htm).) |
| Public method | [RuntimeMessages](M_Grasshopper_Kernel_GH_Component_RuntimeMessages.htm) | Gets the list of cached runtime messages that were recorded during solver-time processes. For components, the set of runtime messages also includes input and output parameters. (Overrides [GH\_ActiveObjectAddLanguageSpecificTextSet("LSTD04B890A\_30?cs=.|vb=.|cpp=::|nu=.|fs=.");RuntimeMessages(GH\_RuntimeMessageLevel)](M_Grasshopper_Kernel_GH_ActiveObject_RuntimeMessages.htm).) |
| Public method | [SDKCompliancy](M_Grasshopper_Kernel_GH_ActiveObject_SDKCompliancy.htm) | Test whether this object is compliant with a given Rhino version. (Inherited from [GH\_ActiveObject](T_Grasshopper_Kernel_GH_ActiveObject.htm).) |
| Public method | [SetIconOverride](M_Grasshopper_Kernel_GH_DocumentObject_SetIconOverride.htm) | Set a new custom icon override for this object. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Protected method | [SetValue(String, Boolean)](M_Grasshopper_Kernel_GH_DocumentObject_SetValue.htm) | Set a named value. This value will be serialized with the component. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Protected method | [SetValue(String, Double)](M_Grasshopper_Kernel_GH_DocumentObject_SetValue_1.htm) | Set a named value. This value will be serialized with the component. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Protected method | [SetValue(String, Color)](M_Grasshopper_Kernel_GH_DocumentObject_SetValue_2.htm) | Set a named value. This value will be serialized with the component. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Protected method | [SetValue(String, Int32)](M_Grasshopper_Kernel_GH_DocumentObject_SetValue_3.htm) | Set a named value. This value will be serialized with the component. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Protected method | [SetValue(String, String)](M_Grasshopper_Kernel_GH_DocumentObject_SetValue_4.htm) | Set a named value. This value will be serialized with the component. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Protected method | [SolveInstance](M_Grasshopper_Kernel_GH_Component_SolveInstance.htm) | This function will be called (successively) from within the ComputeData method of this component. |
| Public method | [TriggerAutoSaveAddLanguageSpecificTextSet("LSTD04B890A\_31?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_GH_DocumentObject_TriggerAutoSave.htm) | Triggers the AutoSave function on the owner document with the object\_changed flag. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Public method | [TriggerAutoSave(GH\_AutoSaveTrigger)](M_Grasshopper_Kernel_GH_DocumentObject_TriggerAutoSave_1.htm) | Triggers the AutoSave function on the owner document with a custom flag. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Public method | [TriggerAutoSave(Guid)](M_Grasshopper_Kernel_GH_DocumentObject_TriggerAutoSave_3.htm) | Triggers the AutoSave function on the owner document with the object\_changed flag. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Public method | [TriggerAutoSave(GH\_AutoSaveTrigger, Guid)](M_Grasshopper_Kernel_GH_DocumentObject_TriggerAutoSave_2.htm) | Triggers the AutoSave function on the owner document with a custom flag. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Protected method | [ValuesChanged](M_Grasshopper_Kernel_GH_DocumentObject_ValuesChanged.htm) | Override this method if you want to respond to changes to the value table. The base implementation is empty, so you don't have to call it. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Public method | [Write](M_Grasshopper_Kernel_GH_Component_Write.htm) | Write all required data for deserialization to an IO archive. (Overrides [GH\_ActiveObjectAddLanguageSpecificTextSet("LSTD04B890A\_32?cs=.|vb=.|cpp=::|nu=.|fs=.");Write(GH\_IWriter)](M_Grasshopper_Kernel_GH_ActiveObject_Write.htm).) |
| Public method | [WriteFull](M_Grasshopper_Kernel_GH_InstanceDescription_WriteFull.htm) | GH\_InstanceDescription does not by default serialize all fields. Use this function to write *all* fields to the archive. This method is compatible with the default Write()/Read() operations. (Inherited from [GH\_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Component Class](T_Grasshopper_Kernel_GH_Component.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)