# T_Grasshopper_Kernel_GH_Document

﻿ GH\_Document Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_Document Class](../html/T_Grasshopper_Kernel_GH_Document.htm "GH_Document Class")

[GH\_Document Constructor](../html/M_Grasshopper_Kernel_GH_Document__ctor.htm "GH_Document Constructor ")

[GH\_Document Properties](../html/Properties_T_Grasshopper_Kernel_GH_Document.htm "GH_Document Properties")

[GH\_Document Methods](../html/Methods_T_Grasshopper_Kernel_GH_Document.htm "GH_Document Methods")

[GH\_Document Events](../html/Events_T_Grasshopper_Kernel_GH_Document.htm "GH_Document Events")

[GH\_Document Fields](../html/Fields_T_Grasshopper_Kernel_GH_Document.htm "GH_Document Fields")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_Document Class |

Represents a single Grasshopper document.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST30C267B0\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.KernelAddLanguageSpecificTextSet("LST30C267B0\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Document

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public sealed class GH_Document : GH_ISerializable, 
	IDisposable, IComparable<GH_Document>, IGH_DebugDescription
```

```
Public NotInheritable Class GH_Document
	Implements GH_ISerializable, IDisposable, IComparable(Of GH_Document), 
	IGH_DebugDescription
```

AddLanguageTabSet("ID1EBCA");

The GH\_Document type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_Document](M_Grasshopper_Kernel_GH_Document__ctor.htm) | Constructor for GH\_Document. Makes sure all important members are initialized. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [AbortRequested](P_Grasshopper_Kernel_GH_Document_AbortRequested.htm) | Gets the abortrequested flag state. |
| Public property | [ActiveDoc](P_Grasshopper_Kernel_GH_Document_ActiveDoc.htm) | Gets or sets a value indicating that this document was last active in a multi-doc aware Rhino. |
| Public property | [AttributeCount](P_Grasshopper_Kernel_GH_Document_AttributeCount.htm) | Returns the total number of attributes in the document. Both Normal and Hidden ones |
| Public property | [Attributes](P_Grasshopper_Kernel_GH_Document_Attributes.htm) | Returns a list of all the attributes in this document. This includes attributes for nested objects such as input or output parameters. |
| Public property | [Author](P_Grasshopper_Kernel_GH_Document_Author.htm) | Gets the author details associated with this document. |
| Public property | [ConstantServer](P_Grasshopper_Kernel_GH_Document_ConstantServer.htm) | Gets the dictionary of constants defined in this document. |
| Public property | [ContainsCustomPreviewObjects](P_Grasshopper_Kernel_GH_Document_ContainsCustomPreviewObjects.htm) | Gets whether this document contains \*any\* custom preview objects. |
| Public property | [Context](P_Grasshopper_Kernel_GH_Document_Context.htm) | Gets or sets the context for this document. Note that the context is not a state so much as an action. Therefore it is not particularly useful to read the context after the fact, rather, context is mostly intended to be a setter, not a getter. When you set the context, all top-level document objects will be informed and the ContextChanged event will be raised. |
| Public propertyStatic member | [DefaultPreviewColour](P_Grasshopper_Kernel_GH_Document_DefaultPreviewColour.htm) | Gets or sets the default preview colour for normal objects. |
| Public propertyStatic member | [DefaultSelectedPreviewColour](P_Grasshopper_Kernel_GH_Document_DefaultSelectedPreviewColour.htm) | Gets or sets the default preview colour for normal objects. |
| Public property | [DisplayName](P_Grasshopper_Kernel_GH_Document_DisplayName.htm) | Gets the display name for this document. The display name is highly context sensitive and is only supposed to give the user a good idea of which document this is and whether it has been modified. |
| Public property | [DocumentID](P_Grasshopper_Kernel_GH_Document_DocumentID.htm) | Gets the document Id. The Id is assigned at construction and never changed. Note: clusters may choose to modify the Id of their internal documents. |
| Public property | [Enabled](P_Grasshopper_Kernel_GH_Document_Enabled.htm) | Gets or sets the enabled state for this document. Enabled documents respond to events and display their previews in the Rhino viewport. |
| Public propertyStatic member | [EnableSolutions](P_Grasshopper_Kernel_GH_Document_EnableSolutions.htm) | Gets or sets a global variable that indicates whether solutions are allowed to be recomputed. When this flag is off, the solver will be disabled and the event watchers should be silent. |
| Public property | [EventServer](P_Grasshopper_Kernel_GH_Document_EventServer.htm) | Gets the event server that belongs to this document. The Event server may be in an inactive state, but it is never null. |
| Public property | [FilePath](P_Grasshopper_Kernel_GH_Document_FilePath.htm) | Gets or sets the file path of this document. If the file path is not set Nothing is returned. |
| Public property | [IgnoredCount](P_Grasshopper_Kernel_GH_Document_IgnoredCount.htm) | Returns the total numbers of components currently in the Object Exception Ignore List. |
| Public property | [IsFilePathDefined](P_Grasshopper_Kernel_GH_Document_IsFilePathDefined.htm) | Returns True if the filename flag of this document has been set |
| Public property | [IsModified](P_Grasshopper_Kernel_GH_Document_IsModified.htm) | Gets or sets the modified flag. If the new value differs from the old value, the ModifiedChanged() event is raised. |
| Public property | [ModifiedSubsidiaries](P_Grasshopper_Kernel_GH_Document_ModifiedSubsidiaries.htm) | Gets the number of modified subsidiary documents. |
| Public property | [Nested](P_Grasshopper_Kernel_GH_Document_Nested.htm) | Gets or sets whether this document is nested. A nested document is always part of some other document and is therefore unknown to the DocumentServer and the Canvas. |
| Public property | [ObjectCount](P_Grasshopper_Kernel_GH_Document_ObjectCount.htm) | Returns the total number of top-level objects in the document. |
| Public property | [Objects](P_Grasshopper_Kernel_GH_Document_Objects.htm) | Returns a list of all normal, top-level objects. |
| Public property | [ObjectSpan](P_Grasshopper_Kernel_GH_Document_ObjectSpan.htm) | Gets the total timespan for all objects. |
| Public property | [Owner](P_Grasshopper_Kernel_GH_Document_Owner.htm) | Gets or sets the owner of this document. A document is typically owned when it is subsidiary to some object, such as a cluster. |
| Public property | [PreviewBoundary](P_Grasshopper_Kernel_GH_Document_PreviewBoundary.htm) | Gets or sets the preview boundary applied to this document. If a boundary has been set, only those objects which are inside the boundary will be previewed. |
| Public property | [PreviewBoundingBox](P_Grasshopper_Kernel_GH_Document_PreviewBoundingBox.htm) | Gets the boundingbox used for previews. |
| Public property | [PreviewColour](P_Grasshopper_Kernel_GH_Document_PreviewColour.htm) | Gets or sets the colour of unselected preview geometry. |
| Public property | [PreviewColourSelected](P_Grasshopper_Kernel_GH_Document_PreviewColourSelected.htm) | Gets or sets the colour of selected preview geometry. |
| Public property | [PreviewCustomMeshParameters](P_Grasshopper_Kernel_GH_Document_PreviewCustomMeshParameters.htm) | Gets or sets the Custom Meshing Parameters for this document, these are only used when PreviewMeshType = GH\_PreviewMesh.Custom |
| Public property | [PreviewFilter](P_Grasshopper_Kernel_GH_Document_PreviewFilter.htm) | Gets or set the preview filter. |
| Public property | [PreviewMeshType](P_Grasshopper_Kernel_GH_Document_PreviewMeshType.htm) | Gets or sets the preview mesh type for this document. |
| Public property | [PreviewMode](P_Grasshopper_Kernel_GH_Document_PreviewMode.htm) | Gets or sets the preview display mode and makes sure the conduit instance of this class is set to match. |
| Public property | [Profiler](P_Grasshopper_Kernel_GH_Document_Profiler.htm) | Gets or sets the profiler mode used in this document. |
| Public property | [Properties](P_Grasshopper_Kernel_GH_Document_Properties.htm) | The properties of this document |
| Public property | [RaiseEvents](P_Grasshopper_Kernel_GH_Document_RaiseEvents.htm) | If RaiseEvents is set to false, all the On....() methods of this document will stop raising events. |
| Public property | [RemotePanelLayout](P_Grasshopper_Kernel_GH_Document_RemotePanelLayout.htm) | Gets the Remote Control Panel layout for this document. |
| Public property | [RhinoDocument](P_Grasshopper_Kernel_GH_Document_RhinoDocument.htm) |  |
| Public property | [RuntimeID](P_Grasshopper_Kernel_GH_Document_RuntimeID.htm) | Gets the runtime ID of this document. RuntimeID is assigned once and never changed. It is also not deserialized so every document will always have a unique ID when loaded. |
| Public property | [ScheduleDelay](P_Grasshopper_Kernel_GH_Document_ScheduleDelay.htm) | Gets the delay for the next scheduled solution. If there is no solution scheduled the delay will be negative. |
| Public property | [SelectedCount](P_Grasshopper_Kernel_GH_Document_SelectedCount.htm) | Gets the number of selected objects |
| Public property | [SelectionTopology](P_Grasshopper_Kernel_GH_Document_SelectionTopology.htm) | Gets the selection topology of the document. |
| Public property | [SolutionDepth](P_Grasshopper_Kernel_GH_Document_SolutionDepth.htm) | Gets the number of nested solutions currently running. If no solutions are running, the depth should be zero. If one solution is runnnig, the depth should be one. Higher depths are only possible if a new solution was scheduled from within an existing solution with delay=0ms. |
| Public property | [SolutionHistory](P_Grasshopper_Kernel_GH_Document_SolutionHistory.htm) | Gets a list of the last 1000 solution timespans, from oldest to youngest. |
| Public property | [SolutionSpan](P_Grasshopper_Kernel_GH_Document_SolutionSpan.htm) | Gets the timespan for the most recent solution. |
| Public property | [SolutionState](P_Grasshopper_Kernel_GH_Document_SolutionState.htm) | Gets the state of this document. |
| Public property | [StateServer](P_Grasshopper_Kernel_GH_Document_StateServer.htm) | Gets the list of stored states in this document |
| Public property | [Thumbnail](P_Grasshopper_Kernel_GH_Document_Thumbnail.htm) | Gets or sets the thumbnail bitmap for this document. |
| Public property | [UndoServer](P_Grasshopper_Kernel_GH_Document_UndoServer.htm) | Gets the UndoServer instance that belongs to this document. |
| Public property | [UndoUtil](P_Grasshopper_Kernel_GH_Document_UndoUtil.htm) | Gets a temporary undo utility instance that allows you to easily create standard undo events. |
| Public property | [ValueTable](P_Grasshopper_Kernel_GH_Document_ValueTable.htm) | Gets the value table associated with this document. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [ActiveObjects](M_Grasshopper_Kernel_GH_Document_ActiveObjects.htm) | Returns all normal objects in the document that implement the IGH\_ActiveObject interface |
| Public method | [AddObject](M_Grasshopper_Kernel_GH_Document_AddObject.htm) | Add a new object to the document. If the object is already contained, nothing will happen |
| Public method | [AlignObjects(GH\_Align, GH\_Distribute)](M_Grasshopper_Kernel_GH_Document_AlignObjects.htm) | Perform alignment and distribution logic on all selected objects. |
| Public method | [AlignObjects(GH\_Align, GH\_Distribute, ListAddLanguageSpecificTextSet("LST30C267B0\_2?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");IGH\_DocumentObjectAddLanguageSpecificTextSet("LST30C267B0\_3?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");)](M_Grasshopper_Kernel_GH_Document_AlignObjects_1.htm) | Perform alignment and distribution logic on a set of objects. |
| Public method | [AppendToDebugLog](M_Grasshopper_Kernel_GH_Document_AppendToDebugLog.htm) | Useful for creating textual representations of this document for debugging purposes. |
| Public method | [ArrangeObject](M_Grasshopper_Kernel_GH_Document_ArrangeObject.htm) | Rearrange the stack order of the object. |
| Public method | [ArrangeObjects](M_Grasshopper_Kernel_GH_Document_ArrangeObjects.htm) | Rearrange the stack order of a collection of objects. |
| Public method | [AssociateWithRhinoDocument](M_Grasshopper_Kernel_GH_Document_AssociateWithRhinoDocument.htm) | Associate this GH\_Document with the currently active Rhino document. This only works if both the 3dm and the ghx file have been saved at least once. |
| Public method | [AutoLayoutComponents](M_Grasshopper_Kernel_GH_Document_AutoLayoutComponents.htm) | Perform automatic layout on this document. |
| Public method | [AutoSave(GH\_AutoSaveTrigger)](M_Grasshopper_Kernel_GH_Document_AutoSave.htm) | Creates a new autosave file on the disk. The previous autosave file (assuming it exists) will be temporarily renamed and eventually deleted entirely. Note: AutoSave is only possible on Documents that have TopLevel Rank and a valid FilePath. |
| Public method | [AutoSave(GH\_AutoSaveTrigger, Guid)](M_Grasshopper_Kernel_GH_Document_AutoSave_1.htm) | Creates a new autosave file on the disk. The previous autosave file (assuming it exists) will be temporarily renamed and eventually deleted entirely. Note: AutoSave is only possible on Documents that have TopLevel Rank and a valid FilePath. |
| Public methodStatic member | [AutoSaveFileName](M_Grasshopper_Kernel_GH_Document_AutoSaveFileName.htm) | Computes the autosave filename for a full grasshopper filepath. |
| Public method | [BoundingBox](M_Grasshopper_Kernel_GH_Document_BoundingBox.htm) | Returns the boundingbox of all the normal attributes. If the document contains no normal attributes an Empty RectangleF structure is returned. |
| Public method | [BringSelectionToTop](M_Grasshopper_Kernel_GH_Document_BringSelectionToTop.htm) | Move the selection set to the top of the visible stack |
| Public method | [ClearIgnoreList](M_Grasshopper_Kernel_GH_Document_ClearIgnoreList.htm) | Clears the Object Exception Ignore List. |
| Public method | [ClearReferenceTable](M_Grasshopper_Kernel_GH_Document_ClearReferenceTable.htm) | Destroys the Referenced object table in the Rhino event watcher. You must call this function if you either add or remove a reference to a Rhino object. |
| Public method | [CloseAllSubsidiaries](M_Grasshopper_Kernel_GH_Document_CloseAllSubsidiaries.htm) | Iterate over all subsidiary documents and close them all without saving. |
| Public method | [ClusterInputHooks](M_Grasshopper_Kernel_GH_Document_ClusterInputHooks.htm) | Gets a sorted list of all the cluster input hooks. |
| Public method | [ClusterInstanceCount](M_Grasshopper_Kernel_GH_Document_ClusterInstanceCount.htm) | Counts the number of instances of a specific cluster document ID. |
| Public method | [ClusterOutputHooks](M_Grasshopper_Kernel_GH_Document_ClusterOutputHooks.htm) | Gets a sorted list of all the cluster output hooks. |
| Public method | [CompareTo](M_Grasshopper_Kernel_GH_Document_CompareTo.htm) | Compare two documents. This function *does not* compare document content. |
| Public method | [ConstructDocumentTree](M_Grasshopper_Kernel_GH_Document_ConstructDocumentTree.htm) | Create a hierarchical document tree of ownership with this document as the root. |
| Public method | [ContainsClusterHooks](M_Grasshopper_Kernel_GH_Document_ContainsClusterHooks.htm) | Tests whether this document contains at least one cluster hook. |
| Public method | [ConvertFullNamesToNickNames](M_Grasshopper_Kernel_GH_Document_ConvertFullNamesToNickNames.htm) | Convert all nicknames to original nicknames if they are equal to the default full name. There will be no undo record associated with this operation. |
| Public method | [ConvertNickNamesToFullNames](M_Grasshopper_Kernel_GH_Document_ConvertNickNamesToFullNames.htm) | Convert all nicknames to full names, if they are equal to the default nickname. There will be no undo record associated with this operation. |
| Public method | [CreateAutomaticClusterHooks](M_Grasshopper_Kernel_GH_Document_CreateAutomaticClusterHooks.htm) | Add an input hook for every non-optional input parameter with no persistent data and no sources. Then add an output hook for every floating parameter without recipients, and for every first component output parameter where the parent component has no recipients. |
| Public method | [CreateConnectivityDiagram](M_Grasshopper_Kernel_GH_Document_CreateConnectivityDiagram.htm) | Gets the connectivity diagram for the current state of this document. |
| Public method | [CreateExpressionParser](M_Grasshopper_Kernel_GH_Document_CreateExpressionParser.htm) | Create a new Expression Solver preloaded with the constants defined in this document. |
| Public method | [DefineConstant](M_Grasshopper_Kernel_GH_Document_DefineConstant.htm) | Add a new constant to the document. Constants are not case-sensitive, when you define a constant with an existing name, the old one will be replaced. Note: constants are as of yet unused. Eventually they are supposed to become accessible to all expressions running inside a document. |
| Public method | [DeselectAll](M_Grasshopper_Kernel_GH_Document_DeselectAll.htm) | Deselect all top-level attributes. |
| Public method | [DestroyAttributeCache](M_Grasshopper_Kernel_GH_Document_DestroyAttributeCache.htm) | Destroys the Attribute cache. Call this function whenever you do something which might affect attributes. |
| Public method | [DestroyAutoSaveFiles](M_Grasshopper_Kernel_GH_Document_DestroyAutoSaveFiles.htm) | Destroys all autosave files and backup files that are associated with this document. Only call this function when you are certain that the document has been properly saved and no changes have occured since. |
| Public method | [DestroyObjectTable](M_Grasshopper_Kernel_GH_Document_DestroyObjectTable.htm) | Erase the Object fast lookup table. You *must* call this whenever you add or remove objects to or from the document while circumventing the regular channels. |
| Public method | [DestroyPreviewCaches](M_Grasshopper_Kernel_GH_Document_DestroyPreviewCaches.htm) | Wipe all caches for Viewport Preview logic. |
| Public method | [DestroyPreviewMeshes](M_Grasshopper_Kernel_GH_Document_DestroyPreviewMeshes.htm) | Attempts to destroy all the preview meshes in this document. It might not work for all objects, but this is still your best bet. |
| Public method | [DestroyProxySources](M_Grasshopper_Kernel_GH_Document_DestroyProxySources.htm) | Remove all remaining proxy sources from the document. |
| Public method | [DisabledObjects](M_Grasshopper_Kernel_GH_Document_DisabledObjects.htm) | Returns all disabled objects in the document |
| Public method | [Dispose](M_Grasshopper_Kernel_GH_Document_Dispose.htm) | When you discard documents you must call Dispose or the Viewport Display event handlers will not be disconnected. |
| Public methodStatic member | [DuplicateDocument](M_Grasshopper_Kernel_GH_Document_DuplicateDocument.htm) | Attempt to duplicate a document. |
| Public method | [EnabledObjects](M_Grasshopper_Kernel_GH_Document_EnabledObjects.htm) | Returns all enabled objects in the document |
| Public method | [ExpandSelection](M_Grasshopper_Kernel_GH_Document_ExpandSelection.htm) | Grow or shift the selection set based on source and recipient links |
| Public method | [ExpirePreview](M_Grasshopper_Kernel_GH_Document_ExpirePreview.htm) | Expires the preview caches of the conduit. |
| Public method | [ExpireSolution](M_Grasshopper_Kernel_GH_Document_ExpireSolution.htm) | Expire the entire solution. This will blank all objects. |
| Public methodStatic member | [FilterActive](M_Grasshopper_Kernel_GH_Document_FilterActive.htm) | Filter a list of objects. |
| Public methodStatic member | [FilterDisabled](M_Grasshopper_Kernel_GH_Document_FilterDisabled.htm) | Filter a list of objects. |
| Public methodStatic member | [FilterEnabled](M_Grasshopper_Kernel_GH_Document_FilterEnabled.htm) | Filter a list of objects. |
| Public methodStatic member | [FilterInactive](M_Grasshopper_Kernel_GH_Document_FilterInactive.htm) | Filter a list of objects. |
| Public method | [FilterObjects(GH\_Filter, GH\_Filter, GH\_Filter)](M_Grasshopper_Kernel_GH_Document_FilterObjects.htm) | Returns all objects in the document that pass the filter specification |
| Public methodStatic member | [FilterObjects(ListAddLanguageSpecificTextSet("LST30C267B0\_4?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");IGH\_DocumentObjectAddLanguageSpecificTextSet("LST30C267B0\_5?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");, GH\_Filter, GH\_Filter, GH\_Filter)](M_Grasshopper_Kernel_GH_Document_FilterObjects_1.htm) | Filter a list of objects using several filters at once |
| Public methodStatic member | [FilterSelected](M_Grasshopper_Kernel_GH_Document_FilterSelected.htm) | Filter a list of objects. |
| Public methodStatic member | [FilterUnselected](M_Grasshopper_Kernel_GH_Document_FilterUnselected.htm) | Filter a list of objects. |
| Public method | [FindAllDownstreamObjects(IGH\_ActiveObject)](M_Grasshopper_Kernel_GH_Document_FindAllDownstreamObjects.htm) | Find all objects that depend in some way on the Source. |
| Public method | [FindAllDownstreamObjects(ListAddLanguageSpecificTextSet("LST30C267B0\_6?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");IGH\_ActiveObjectAddLanguageSpecificTextSet("LST30C267B0\_7?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");)](M_Grasshopper_Kernel_GH_Document_FindAllDownstreamObjects_2.htm) | Find all objects that depend in some way on the Source collection |
| Public method | [FindAllDownstreamObjects(IGH\_ActiveObject, GH\_DocumentAddLanguageSpecificTextSet("LST30C267B0\_8?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_ActiveObjectFilter)](M_Grasshopper_Kernel_GH_Document_FindAllDownstreamObjects_1.htm) | Find all objects that depend in some way on the Source. |
| Public method | [FindAllDownstreamObjects(ListAddLanguageSpecificTextSet("LST30C267B0\_9?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");IGH\_ActiveObjectAddLanguageSpecificTextSet("LST30C267B0\_10?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");, GH\_DocumentAddLanguageSpecificTextSet("LST30C267B0\_11?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_ActiveObjectFilter)](M_Grasshopper_Kernel_GH_Document_FindAllDownstreamObjects_3.htm) | Find all objects that depend in some way on the Source collection |
| Public method | [FindAttribute(Guid)](M_Grasshopper_Kernel_GH_Document_FindAttribute_1.htm) | Find the object that matches the ID |
| Public method | [FindAttribute(PointF, Boolean)](M_Grasshopper_Kernel_GH_Document_FindAttribute.htm) | Search for attributes that contain a certain point. |
| Public method | [FindAttributeByGrip(PointF, Boolean, Int32)](M_Grasshopper_Kernel_GH_Document_FindAttributeByGrip_1.htm) | Search for attributes that contain grips near the search locus |
| Public method | [FindAttributeByGrip(PointF, Boolean, Boolean, Boolean, Int32)](M_Grasshopper_Kernel_GH_Document_FindAttributeByGrip.htm) | Search for attributes that contain grips near the search locus |
| Public method | [FindClusters(Guid)](M_Grasshopper_Kernel_GH_Document_FindClusters.htm) | Find all the clusters that have a matching ID. |
| Public method | [FindClusters(String)](M_Grasshopper_Kernel_GH_Document_FindClusters_1.htm) | Find all the clusters that have a matching filepath. |
| Public method | [FindComponent(Guid)](M_Grasshopper_Kernel_GH_Document_FindComponent_1.htm) | Search for components using an ID filter |
| Public method | [FindComponent(Point)](M_Grasshopper_Kernel_GH_Document_FindComponent.htm) | Search for components that contain the locus |
| Public method | [FindFloatingParameter](M_Grasshopper_Kernel_GH_Document_FindFloatingParameter.htm) | Search for floating parameters that contain the locus |
| Public method | [FindInputParameter](M_Grasshopper_Kernel_GH_Document_FindInputParameter.htm) | Search for input (upstream) parameters that contain the locus |
| Public method | [FindObject(Guid, Boolean)](M_Grasshopper_Kernel_GH_Document_FindObject_1.htm) | Find the object that matches the ID. |
| Public method | [FindObject(PointF, Single)](M_Grasshopper_Kernel_GH_Document_FindObject.htm) | Find the topmost object that is closest to the point |
| Public method | [FindObjectAddLanguageSpecificTextSet("LST30C267B0\_12?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST30C267B0\_13?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");(Guid, Boolean)](M_Grasshopper_Kernel_GH_Document_FindObject__1.htm) | Find the object that matches the ID. |
| Public method | [FindObjects](M_Grasshopper_Kernel_GH_Document_FindObjects.htm) | Find the objects in the document that match the search term. Top level object names and nicknames are searched, as well as descriptions. Some objects are special cased to allow for more targeted searches. Data descriptions are not searched. |
| Public method | [FindOutputParameter](M_Grasshopper_Kernel_GH_Document_FindOutputParameter.htm) | Search for output (downstream) parameters that contain the locus |
| Public method | [FindParameter](M_Grasshopper_Kernel_GH_Document_FindParameter.htm) | Search for parameters using an ID filter |
| Public method | [FindWireAt](M_Grasshopper_Kernel_GH_Document_FindWireAt.htm) | Find the wire at or near the given coordinate. |
| Public method | [ForcePreview](M_Grasshopper_Kernel_GH_Document_ForcePreview.htm) | If true, the document will draw viewport previews regardless of other conditions. Typically a document only previews if it is loaded in the canvas or when it has an RCP. |
| Public method | [GetAllInstanceIDs](M_Grasshopper_Kernel_GH_Document_GetAllInstanceIDs.htm) | Get a sorted list of all the IGH\_DocumentObject instance IDs in this document. |
| Public method | [InactiveObjects](M_Grasshopper_Kernel_GH_Document_InactiveObjects.htm) | Returns all objects in the document that don't implement the IGH\_ActiveObject interface |
| Public method | [InvertSelection](M_Grasshopper_Kernel_GH_Document_InvertSelection.htm) | Invert the selected state of all top-level attributes. |
| Public methodStatic member | [IsEscapeKeyDown](M_Grasshopper_Kernel_GH_Document_IsEscapeKeyDown.htm) | Gets whether the escape key was pressed since the last time this function was called. Though in reality the actual escape state is checked no more than once every 50 milliseconds or so, which should be sufficient for a smooth user experience. |
| Public method | [IsRenderMeshPipelineViewport](M_Grasshopper_Kernel_GH_Document_IsRenderMeshPipelineViewport.htm) | Test to see whether a pipeline should have custom render meshes vs. previews. |
| Public method | [MergeDocument(GH\_Document)](M_Grasshopper_Kernel_GH_Document_MergeDocument.htm) | Hoist all objects from another document into this one. |
| Public method | [MergeDocument(GH\_Document, Boolean)](M_Grasshopper_Kernel_GH_Document_MergeDocument_1.htm) | Hoist all objects from another document into this one. |
| Public method | [MergeDocument(GH\_Document, Boolean, Boolean)](M_Grasshopper_Kernel_GH_Document_MergeDocument_2.htm) | Hoist all objects from another document into this one. |
| Public method | [Modified](M_Grasshopper_Kernel_GH_Document_Modified.htm) | Sets the modified flag of this document. |
| Public method | [MutateAllIds](M_Grasshopper_Kernel_GH_Document_MutateAllIds.htm) | Change all the instance UUIDs of all objects in the document. Be sure to resolve all proxy sources before mutating IDs. This function will ensure all groups are updated appropriately. |
| Public method | [NewSolution(Boolean)](M_Grasshopper_Kernel_GH_Document_NewSolution.htm) | Start a new solution. |
| Public method | [NewSolution(Boolean, GH\_SolutionMode)](M_Grasshopper_Kernel_GH_Document_NewSolution_1.htm) | Start a new solution. |
| Public methodStatic member | [NonBlankFilter](M_Grasshopper_Kernel_GH_Document_NonBlankFilter.htm) | This delegate can be used in the FindAllDownstreamObjects(...) methods. Only includes objects that are non-blank and non-failed. |
| Public methodStatic member | [NullFilter](M_Grasshopper_Kernel_GH_Document_NullFilter.htm) | This delegate can be used in the FindAllDownstreamObjects(...) methods. Includes all objects. |
| Public method | [OnContextChanged](M_Grasshopper_Kernel_GH_Document_OnContextChanged.htm) | Raise the ContextChanged event. |
| Public method | [OnEnabledChanged](M_Grasshopper_Kernel_GH_Document_OnEnabledChanged.htm) | Raise the EnabledChanged event. |
| Public method | [OnFilePathChanged](M_Grasshopper_Kernel_GH_Document_OnFilePathChanged.htm) | Raise the FilePathChanged event. |
| Public method | [OnModifiedChanged](M_Grasshopper_Kernel_GH_Document_OnModifiedChanged.htm) | Raise the ModifiedChanged event |
| Public method | [OnObjectAdded](M_Grasshopper_Kernel_GH_Document_OnObjectAdded.htm) | Raise the ObjectsAdded event. |
| Public method | [OnObjectDeleted](M_Grasshopper_Kernel_GH_Document_OnObjectDeleted.htm) | Raise the ObjectsDeleted event. |
| Public method | [OnObjectsAdded](M_Grasshopper_Kernel_GH_Document_OnObjectsAdded.htm) | Raise the ObjectsAdded event. |
| Public method | [OnObjectsDeleted](M_Grasshopper_Kernel_GH_Document_OnObjectsDeleted.htm) | Raise the ObjectsDeleted event. |
| Public method | [OnSettingsChanged](M_Grasshopper_Kernel_GH_Document_OnSettingsChanged.htm) | Raise the SettingsChanged event. |
| Public method | [OnUndoStateChanged](M_Grasshopper_Kernel_GH_Document_OnUndoStateChanged.htm) | Raise the UndoStateChanged event. |
| Public method | [PreviewCurrentMeshParameters](M_Grasshopper_Kernel_GH_Document_PreviewCurrentMeshParameters.htm) | Gets the currently relevant meshing parameters (do not modify the instance as it may be shared). |
| Public method | [Read](M_Grasshopper_Kernel_GH_Document_Read.htm) | Standard archiving function. Will deserialize the entire document. |
| Public method | [Redo](M_Grasshopper_Kernel_GH_Document_Redo.htm) | Perform the first redo event. |
| Public method | [RelevantObjectAtPoint(PointF)](M_Grasshopper_Kernel_GH_Document_RelevantObjectAtPoint.htm) | Find the most relevant object at a given canvas location. The most relevant object might be a regular Object (Component or Parameter), it might be an attribute grip, an attribute balloon, a wire or a group. |
| Public method | [RelevantObjectAtPoint(PointF, GH\_RelevantObjectFilter)](M_Grasshopper_Kernel_GH_Document_RelevantObjectAtPoint_1.htm) | Find the most relevant object at a given canvas location. The most relevant object might be a regular Object (Component or Parameter), it might be an attribute grip, an attribute balloon, a wire or a group. |
| Public method | [RemoveObject(IGH\_Attributes, Boolean)](M_Grasshopper_Kernel_GH_Document_RemoveObject.htm) | Remove the top-level object in the attribute tree from the document. This method does not add an Undo event, that is the responsibility of the caller. |
| Public method | [RemoveObject(IGH\_DocumentObject, Boolean)](M_Grasshopper_Kernel_GH_Document_RemoveObject_1.htm) | Remove the object from the document. This removal is the precursor to object deletion. Do not call this function if you intend to transfer the object to another GH\_Document. This method does not add an Undo event, that is the responsibility of the caller. |
| Public method | [RemoveObjects](M_Grasshopper_Kernel_GH_Document_RemoveObjects.htm) | Remove the specified objects from the document. This removal is the precursor to object deletion. Do not call this function if you intend to transfer the objects to another GH\_Document. This method does not add an Undo event, that is the responsibility of the caller. |
| Public method | [RemoveSelection](M_Grasshopper_Kernel_GH_Document_RemoveSelection.htm) | Delete all the objects in the selection set. This method does not record an Undo event, that is the responsibility of the caller. |
| Public method | [RepairProxySources](M_Grasshopper_Kernel_GH_Document_RepairProxySources.htm) | Attempts to resolve all proxy sources in the document. |
| Public method | [ReplaceProxySources](M_Grasshopper_Kernel_GH_Document_ReplaceProxySources.htm) | Replace all remaining proxy sources in the document with UnresolvedProxy Objects. |
| Public method | [RequestAbortSolution](M_Grasshopper_Kernel_GH_Document_RequestAbortSolution.htm) | Set the requestabort flag. The solution will be aborted whenever the current active object is completed. It is also possible that active objects themselves implement an abortion mechanism, in which case abortion might occur even sooner. |
| Public method | [RunningAsCommand](M_Grasshopper_Kernel_GH_Document_RunningAsCommand.htm) | When the document is being solved inside the context of an executing Rhino command, this function will return the command instance. Under normal operation of Grasshopper in the traditional sense, this function will return null. The document executes as a command when inside of the grasshopper player or as a compiled grasshopper player based command. The way to run a GH\_Document as a command is to call the GH\_RhinoScriptInterface.RunAsCommand function |
| Public method | [ScheduleSolution(Int32)](M_Grasshopper_Kernel_GH_Document_ScheduleSolution.htm) | Schedule a new solution after a specified time interval. The schedule is erased if another solution is triggered before the schedule is executed. Tight schedules override loose schedules. If this method is called *during* a solution, the schedule will be started after the current solution completes. |
| Public method | [ScheduleSolution(Int32, GH\_DocumentAddLanguageSpecificTextSet("LST30C267B0\_14?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_ScheduleDelegate)](M_Grasshopper_Kernel_GH_Document_ScheduleSolution_1.htm) | Schedule a new solution after a specified time interval. The schedule is erased if another solution is triggered before the schedule is executed. Tight schedules override loose schedules. If this method is called *during* a solution, the schedule will be started after the current solution completes. |
| Public method | [Select(GH\_RelevantObjectData)](M_Grasshopper_Kernel_GH_Document_Select.htm) | Default pick selection behaviour. (looks at current Shift + Control modifier states to determine addition/removal) |
| Public method | [Select(GH\_RelevantObjectData, Boolean, Boolean)](M_Grasshopper_Kernel_GH_Document_Select_1.htm) | Default pick selection behaviour |
| Public method | [SelectAll](M_Grasshopper_Kernel_GH_Document_SelectAll.htm) | Select all top-level attributes. |
| Public method | [SelectedObjects](M_Grasshopper_Kernel_GH_Document_SelectedObjects.htm) | Returns all selected objects in the document |
| Public method | [SetEnabledFlags(Boolean)](M_Grasshopper_Kernel_GH_Document_SetEnabledFlags.htm) | Set the enabled flags of all selected objects to true or false |
| Public method | [SetEnabledFlags(ListAddLanguageSpecificTextSet("LST30C267B0\_15?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");IGH\_DocumentObjectAddLanguageSpecificTextSet("LST30C267B0\_16?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");, Boolean)](M_Grasshopper_Kernel_GH_Document_SetEnabledFlags_1.htm) | Set the enabled flags of all specified objects to true or false |
| Public method | [SetPreviewFlags(Boolean)](M_Grasshopper_Kernel_GH_Document_SetPreviewFlags.htm) | Set the preview flags of all selected objects to true or false |
| Public method | [SetPreviewFlags(ListAddLanguageSpecificTextSet("LST30C267B0\_17?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");IGH\_DocumentObjectAddLanguageSpecificTextSet("LST30C267B0\_18?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");, Boolean)](M_Grasshopper_Kernel_GH_Document_SetPreviewFlags_1.htm) | Set the preview flags of all specified objects to true or false |
| Public method | [SetStatusBarEventHelper](M_Grasshopper_Kernel_GH_Document_SetStatusBarEventHelper.htm) |  |
| Public method | [ShowPreviewSettings](M_Grasshopper_Kernel_GH_Document_ShowPreviewSettings.htm) | Display the Preview settings dialog. |
| Public method | [SolutionProgress](M_Grasshopper_Kernel_GH_Document_SolutionProgress.htm) | Returns the progress of the current solution. |
| Public method | [ToggleEnabledFlagsAddLanguageSpecificTextSet("LST30C267B0\_19?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_GH_Document_ToggleEnabledFlags.htm) | Toggle the enabled flags of all selected objects |
| Public method | [ToggleEnabledFlags(ListAddLanguageSpecificTextSet("LST30C267B0\_20?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");IGH\_DocumentObjectAddLanguageSpecificTextSet("LST30C267B0\_21?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");)](M_Grasshopper_Kernel_GH_Document_ToggleEnabledFlags_1.htm) | Toggle the enabled flags of all specified objects |
| Public method | [TogglePreviewFlagsAddLanguageSpecificTextSet("LST30C267B0\_22?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_GH_Document_TogglePreviewFlags.htm) | Toggle the preview flags of all selected objects |
| Public method | [TogglePreviewFlags(ListAddLanguageSpecificTextSet("LST30C267B0\_23?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");IGH\_DocumentObjectAddLanguageSpecificTextSet("LST30C267B0\_24?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");)](M_Grasshopper_Kernel_GH_Document_TogglePreviewFlags_1.htm) | Toggle the preview flags of all specified objects |
| Public method | [ToString](M_Grasshopper_Kernel_GH_Document_ToString.htm) | A document serializes itself using the filename of the current path. This is useful for sorting purposes and ListBoxes. (Overrides [ObjectAddLanguageSpecificTextSet("LST30C267B0\_25?cs=.|vb=.|cpp=::|nu=.|fs=.");ToStringAddLanguageSpecificTextSet("LST30C267B0\_26?cs=()|vb=|cpp=()|nu=()|fs=()");](https://docs.microsoft.com/dotnet/api/system.object.tostring#system-object-tostring).) |
| Public method | [TranslateObjects](M_Grasshopper_Kernel_GH_Document_TranslateObjects.htm) | Offset objects by a certain distance in X and Y |
| Public method | [Undo](M_Grasshopper_Kernel_GH_Document_Undo.htm) | Perform the first undo event. |
| Public method | [UnselectedObjects](M_Grasshopper_Kernel_GH_Document_UnselectedObjects.htm) | Returns all unselected objects in the document |
| Public method | [UpdateAllSubsidiaries](M_Grasshopper_Kernel_GH_Document_UpdateAllSubsidiaries.htm) | Iterate over all subsidiary documents and update them with their respective owners. If a subsidiary hasn't been modified, it will not be updated and it will not be counted. |
| Public method | [Write(GH\_IWriter)](M_Grasshopper_Kernel_GH_Document_Write.htm) | Standard archiving function. Will serialize the entire document. |
| Public method | [Write(GH\_IWriter, IListAddLanguageSpecificTextSet("LST30C267B0\_27?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");IGH\_DocumentObjectAddLanguageSpecificTextSet("LST30C267B0\_28?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");)](M_Grasshopper_Kernel_GH_Document_Write_1.htm) | Special function that allows writing of a custom object list. This function is used when partial documents need to be serialized such as when exporting or during clipboard operations. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Events

|  | Name | Description |
| --- | --- | --- |
| Public event | [ContextChanged](E_Grasshopper_Kernel_GH_Document_ContextChanged.htm) | The context for this document was changed. |
| Public eventStatic member | [DefaultPreviewColourChanged](E_Grasshopper_Kernel_GH_Document_DefaultPreviewColourChanged.htm) | This even is raised whenever the global default for Normal preview colour is changed. |
| Public eventStatic member | [DefaultSelectedPreviewColourChanged](E_Grasshopper_Kernel_GH_Document_DefaultSelectedPreviewColourChanged.htm) | This even is raised whenever the global default for Selected preview colour is changed. |
| Public event | [EnabledChanged](E_Grasshopper_Kernel_GH_Document_EnabledChanged.htm) | The Enabled state was changed on this document. |
| Public eventStatic member | [EnableSolutionsChanged](E_Grasshopper_Kernel_GH_Document_EnableSolutionsChanged.htm) | Raised whenever the Shared EnabledSolutions property is changed. |
| Public event | [FilePathChanged](E_Grasshopper_Kernel_GH_Document_FilePathChanged.htm) | Raised whenever the FilePath of the document is modified. |
| Public event | [ModifiedChanged](E_Grasshopper_Kernel_GH_Document_ModifiedChanged.htm) | The modified flag on the document was changed. |
| Public event | [ObjectsAdded](E_Grasshopper_Kernel_GH_Document_ObjectsAdded.htm) | Raised after a collection of objects was added to the document. |
| Public event | [ObjectsDeleted](E_Grasshopper_Kernel_GH_Document_ObjectsDeleted.htm) | Raised after a collection of objects was removed from the document. At this point, the objects still exist, but they no longer belong to this document. |
| Public event | [SettingsChanged](E_Grasshopper_Kernel_GH_Document_SettingsChanged.htm) | Some settings of the document were changed. |
| Public event | [SolutionEnd](E_Grasshopper_Kernel_GH_Document_SolutionEnd.htm) | This event is raised whenever a new solution request has been handled. Even if the document is locked. |
| Public event | [SolutionStart](E_Grasshopper_Kernel_GH_Document_SolutionStart.htm) | This event is raised whenever a new solution is requested. Even if the document is locked. |
| Public event | [UndoStateChanged](E_Grasshopper_Kernel_GH_Document_UndoStateChanged.htm) | Raised whenever there is a change to the document undo/redo stack. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Fields

|  | Name | Description |
| --- | --- | --- |
| Public fieldStatic member | [IgnoredUnknowns](F_Grasshopper_Kernel_GH_Document_IgnoredUnknowns.htm) | A collection of missing component IDs to ignore during file load operations. Erase this cache to re-enable all the load warnings. |
| Public fieldStatic member | [ScheduleInactive](F_Grasshopper_Kernel_GH_Document_ScheduleInactive.htm) | Defined the delay used to indicate the absence of a schedule. |
| Public fieldStatic member | [ScheduleRecursive](F_Grasshopper_Kernel_GH_Document_ScheduleRecursive.htm) | Defines the delay used to indicate the schedule should be immedate and recursive. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)