# T_Grasshopper_Kernel_GH_TaskCapableComponent_1

﻿ GH\_TaskCapableComponent(T) Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_TaskCapableComponent(T) Class](../html/T_Grasshopper_Kernel_GH_TaskCapableComponent_1.htm "GH_TaskCapableComponent(T) Class")

[GH\_TaskCapableComponent(T) Properties](../html/Properties_T_Grasshopper_Kernel_GH_TaskCapableComponent_1.htm "GH_TaskCapableComponent(T) Properties")

[GH\_TaskCapableComponent(T) Methods](../html/Methods_T_Grasshopper_Kernel_GH_TaskCapableComponent_1.htm "GH_TaskCapableComponent(T) Methods")

[GH\_TaskCapableComponent(T) Events](../html/Events_T_Grasshopper_Kernel_GH_TaskCapableComponent_1.htm "GH_TaskCapableComponent(T) Events")

[GH\_TaskCapableComponent(T) Fields](../html/Fields_T_Grasshopper_Kernel_GH_TaskCapableComponent_1.htm "GH_TaskCapableComponent(T) Fields")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_TaskCapableComponentAddLanguageSpecificTextSet("LST88DF80B7\_0?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST88DF80B7\_1?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)"); Class |

Abstract implementation of IGH\_TaskCapableComponent. Inherit from this class
instead of implementing IGH\_TaskCapableComponent directly.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST88DF80B7\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [Grasshopper.KernelAddLanguageSpecificTextSet("LST88DF80B7\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm)  
    [Grasshopper.KernelAddLanguageSpecificTextSet("LST88DF80B7\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm)  
      [Grasshopper.KernelAddLanguageSpecificTextSet("LST88DF80B7\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_ActiveObject](T_Grasshopper_Kernel_GH_ActiveObject.htm)  
        [Grasshopper.KernelAddLanguageSpecificTextSet("LST88DF80B7\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Component](T_Grasshopper_Kernel_GH_Component.htm)  
          Grasshopper.KernelAddLanguageSpecificTextSet("LST88DF80B7\_7?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_TaskCapableComponentAddLanguageSpecificTextSet("LST88DF80B7\_8?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST88DF80B7\_9?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public abstract class GH_TaskCapableComponent<T> : GH_Component, 
	IGH_TaskCapableComponent
```

```
Public MustInherit Class GH_TaskCapableComponent(Of T)
	Inherits GH_Component
	Implements IGH_TaskCapableComponent
```

AddLanguageTabSet("ID1EBCA");

#### Type Parameters

T

The GH\_TaskCapableComponentAddLanguageSpecificTextSet("LST88DF80B7\_10?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST88DF80B7\_11?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;"); type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Attributes](P_Grasshopper_Kernel_GH_DocumentObject_Attributes.htm) | Gets or sets the attributes that are associated with this object. Only set custom attributes if you know what you are doing. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Protected property | [CancelToken](P_Grasshopper_Kernel_GH_TaskCapableComponent_1_CancelToken.htm) |  |
| Public property | [Category](P_Grasshopper_Kernel_GH_InstanceDescription_Category.htm) | Gets or sets the Category in which this object belongs. If HasCategory() returns false, this field has no meaning. (Inherited from [GH\_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).) |
| Public property | [ClippingBox](P_Grasshopper_Kernel_GH_Component_ClippingBox.htm) | Gets the clipping box for all preview geometry drawn by this component and all associated parameters. (Inherited from [GH\_Component](T_Grasshopper_Kernel_GH_Component.htm).) |
| Public property | [ComponentGuid](P_Grasshopper_Kernel_GH_DocumentObject_ComponentGuid.htm) | Returns a consistent ID for this object type. Every object must supply a unique and unchanging ID that is used to identify objects of the same type. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Public property | [Description](P_Grasshopper_Kernel_GH_InstanceDescription_Description.htm) | Gets or sets the description of the object. This field typically remains fixed during the lifetime of an object. (Inherited from [GH\_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).) |
| Public property | [Exposure](P_Grasshopper_Kernel_GH_DocumentObject_Exposure.htm) | Gets the exposure of this object in the Graphical User Interface. The default is to expose everywhere. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Public property | [HasCategory](P_Grasshopper_Kernel_GH_InstanceDescription_HasCategory.htm) | Gets whether or not the Category field has been set. (Inherited from [GH\_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).) |
| Public property | [HasSubCategory](P_Grasshopper_Kernel_GH_InstanceDescription_HasSubCategory.htm) | Gets whether or not the SubCategory field has been set. (Inherited from [GH\_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).) |
| Protected property | [HelpDescription](P_Grasshopper_Kernel_GH_Component_HelpDescription.htm) | Override this method if you want the help topic content to be more than the Component description. (Inherited from [GH\_Component](T_Grasshopper_Kernel_GH_Component.htm).) |
| Public property | [Hidden](P_Grasshopper_Kernel_GH_Component_Hidden.htm) | Gets or sets the hidden flag for this component. Does not affect Hidden flags on parameters associated with this component. (Inherited from [GH\_Component](T_Grasshopper_Kernel_GH_Component.htm).) |
| Protected property | [Icon](P_Grasshopper_Kernel_GH_DocumentObject_Icon.htm) | Override this function to supply a custom icon (24x24 pixels). The result of this property is cached, so don't worry if icon retrieval is not very fast. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Public property | [Icon\_24x24](P_Grasshopper_Kernel_GH_DocumentObject_Icon_24x24.htm) | The icon associated with this object. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Public property | [Icon\_24x24\_Locked](P_Grasshopper_Kernel_GH_DocumentObject_Icon_24x24_Locked.htm) | The greyscale icon of this object. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Public property | [IconCapableUI](P_Grasshopper_Kernel_GH_ActiveObject_IconCapableUI.htm) | By default the NickName menu item supports the Icon Mode override toggle. If your UI is not capable of displaying icons, then override this property and return False. (Inherited from [GH\_ActiveObject](T_Grasshopper_Kernel_GH_ActiveObject.htm).) |
| Public property | [IconDisplayMode](P_Grasshopper_Kernel_GH_DocumentObject_IconDisplayMode.htm) | Gets the current display mode of the object. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Public property | [InConstructor](P_Grasshopper_Kernel_GH_Component_InConstructor.htm) | Gets the constructor flag for this instance. If InConstructor = True, it means the component is still registering parameters and the layout is not yet complete. (Inherited from [GH\_Component](T_Grasshopper_Kernel_GH_Component.htm).) |
| Public property | [InPreSolve](P_Grasshopper_Kernel_GH_TaskCapableComponent_1_InPreSolve.htm) | Is set to True by the framework right before a "use tasks" pass is made on SolveIntance calls. When True, SolveInstance should be using Tasks to start calculations on input data. When False, SolveInstance should be setting the output data by either using the result of a task or directly computing the results. |
| Public property | [InstanceDescription](P_Grasshopper_Kernel_GH_TaskCapableComponent_1_InstanceDescription.htm) | (Overrides [GH\_ComponentAddLanguageSpecificTextSet("LST88DF80B7\_12?cs=.|vb=.|cpp=::|nu=.|fs=.");InstanceDescription](P_Grasshopper_Kernel_GH_Component_InstanceDescription.htm).) |
| Public property | [InstanceGuid](P_Grasshopper_Kernel_GH_InstanceDescription_InstanceGuid.htm) | Gets the ID of this runtime instance. (Inherited from [GH\_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).) |
| Public property | [IsBakeCapable](P_Grasshopper_Kernel_GH_Component_IsBakeCapable.htm) | (Inherited from [GH\_Component](T_Grasshopper_Kernel_GH_Component.htm).) |
| Public property | [IsDataProvider](P_Grasshopper_Kernel_GH_Component_IsDataProvider.htm) | Components are never Data providers. Only the output parameters can be considered to be providers. (Inherited from [GH\_Component](T_Grasshopper_Kernel_GH_Component.htm).) |
| Public property | [IsPreviewCapable](P_Grasshopper_Kernel_GH_Component_IsPreviewCapable.htm) | If a single parameter is PreviewCapable, so is the component. Override this property if you need special Preview flags. (Inherited from [GH\_Component](T_Grasshopper_Kernel_GH_Component.htm).) |
| Public property | [IsValidPrincipalParameterIndex](P_Grasshopper_Kernel_GH_Component_IsValidPrincipalParameterIndex.htm) | Gets whether the MasterParameterIndex property identifies a valid parameter. (Inherited from [GH\_Component](T_Grasshopper_Kernel_GH_Component.htm).) |
| Public property | [Keywords](P_Grasshopper_Kernel_GH_InstanceDescription_Keywords.htm) | Gets a list of additional keywords that describe the object. Typically this list is empty but you can override this property to aid in object searches. (Inherited from [GH\_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).) |
| Public property | [Locked](P_Grasshopper_Kernel_GH_Component_Locked.htm) | Gets or sets the Locked state for this Component. This also sets locked states for all input and output parameters. (Inherited from [GH\_Component](T_Grasshopper_Kernel_GH_Component.htm).) |
| Public property | [Message](P_Grasshopper_Kernel_GH_Component_Message.htm) | Gets or sets a custom message to be displayed underneath the component. This message is not serialized and should be assigned on every solution anew. (Inherited from [GH\_Component](T_Grasshopper_Kernel_GH_Component.htm).) |
| Public property | [MutableNickName](P_Grasshopper_Kernel_GH_ActiveObject_MutableNickName.htm) | Gets or sets a value that enables Nick name changes through the menu. The default is TRUE. (Inherited from [GH\_ActiveObject](T_Grasshopper_Kernel_GH_ActiveObject.htm).) |
| Public property | [Name](P_Grasshopper_Kernel_GH_InstanceDescription_Name.htm) | Gets or sets the name of the object. This field typically remains fixed during the lifetime of an object. (Inherited from [GH\_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).) |
| Public property | [NickName](P_Grasshopper_Kernel_GH_InstanceDescription_NickName.htm) | Gets or sets the nickname of the object. This field can be changed by the user. (Inherited from [GH\_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).) |
| Public property | [Obsolete](P_Grasshopper_Kernel_GH_DocumentObject_Obsolete.htm) | Gets whether this object is obsolete. Default implementation returns true if the class name contains the string "OBSOLETE" or if this class has been decorated with the ObsoleteAttribute. You are free to override this if you want, but I suggest adding the ObsoleteAttribute instead. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Public property | [Params](P_Grasshopper_Kernel_GH_Component_Params.htm) | Gets the parameter manager object for this component. (Inherited from [GH\_Component](T_Grasshopper_Kernel_GH_Component.htm).) |
| Public property | [Phase](P_Grasshopper_Kernel_GH_ActiveObject_Phase.htm) | Gets or sets the solution phase this object is currenly in. (Inherited from [GH\_ActiveObject](T_Grasshopper_Kernel_GH_ActiveObject.htm).) |
| Public property | [PrincipalParameterIndex](P_Grasshopper_Kernel_GH_Component_PrincipalParameterIndex.htm) | Gets or sets the principal parameter index override. Negative indices or indices larger than or equal to the input parameter count will be ignored and regular principal parameter detection will kick in. (Inherited from [GH\_Component](T_Grasshopper_Kernel_GH_Component.htm).) |
| Public property | [ProcessorTime](P_Grasshopper_Kernel_GH_Component_ProcessorTime.htm) | Gets the total processor time (profiler) spend by this component and all input parameters. (Inherited from [GH\_Component](T_Grasshopper_Kernel_GH_Component.htm).) |
| Public property | [RunCount](P_Grasshopper_Kernel_GH_Component_RunCount.htm) | Gets a value indicating how many times the SolveInstance method was called on this component during the last solution. This property will return -1 if no valid runcount is available. (Inherited from [GH\_Component](T_Grasshopper_Kernel_GH_Component.htm).) |
| Public property | [RuntimeMessageLevel](P_Grasshopper_Kernel_GH_Component_RuntimeMessageLevel.htm) | Returns the worst case runtime warning level of me and all my parameters (Inherited from [GH\_Component](T_Grasshopper_Kernel_GH_Component.htm).) |
| Public property | [SubCategory](P_Grasshopper_Kernel_GH_InstanceDescription_SubCategory.htm) | Gets or sets the SubCategory in which this object belongs. If HasSubCategory() returns false, this field has no meaning. (Inherited from [GH\_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).) |
| Protected property | [TaskList](P_Grasshopper_Kernel_GH_TaskCapableComponent_1_TaskList.htm) |  |
| Public property | [UseTasks](P_Grasshopper_Kernel_GH_TaskCapableComponent_1_UseTasks.htm) | Returns True if the component is set to support tasks. Components can have this feature turned on/off. Note that even if UseTasks returns True, there is a chance that a multipass task based solution may not be invoked depending on if multiple calls need to be made during enumeration. You must pay attention to the value of InPreSolve during SolveInstance. The set version of this property can be called by the framework if we want to provide a technique to globally turn on/off task support for all components in a definition. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [AddedToDocument](M_Grasshopper_Kernel_GH_Component_AddedToDocument.htm) | Overrides the AddedToDocument method and delegates the call to all parameters. (Inherited from [GH\_Component](T_Grasshopper_Kernel_GH_Component.htm).) |
| Public method | [AddRuntimeMessage](M_Grasshopper_Kernel_GH_ActiveObject_AddRuntimeMessage.htm) | Add a new message to this object. Valid message type flags are Warning and Error. If the Message string is empty or zero-length no message is added. (Inherited from [GH\_ActiveObject](T_Grasshopper_Kernel_GH_ActiveObject.htm).) |
| Protected method | [AfterSolveInstance](M_Grasshopper_Kernel_GH_TaskCapableComponent_1_AfterSolveInstance.htm) | (Overrides [GH\_ComponentAddLanguageSpecificTextSet("LST88DF80B7\_13?cs=.|vb=.|cpp=::|nu=.|fs=.");AfterSolveInstanceAddLanguageSpecificTextSet("LST88DF80B7\_14?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_GH_Component_AfterSolveInstance.htm).) |
| Protected method | [AppendAdditionalComponentMenuItems](M_Grasshopper_Kernel_GH_Component_AppendAdditionalComponentMenuItems.htm) | Override this function if you want to insert some custom menu items in your derived Component class. Items will be added between List Matching items and parameter menus. (Inherited from [GH\_Component](T_Grasshopper_Kernel_GH_Component.htm).) |
| Public method | [AppendAdditionalMenuItems](M_Grasshopper_Kernel_GH_TaskCapableComponent_1_AppendAdditionalMenuItems.htm) | (Overrides [GH\_ComponentAddLanguageSpecificTextSet("LST88DF80B7\_15?cs=.|vb=.|cpp=::|nu=.|fs=.");AppendAdditionalMenuItems(ToolStripDropDown)](M_Grasshopper_Kernel_GH_Component_AppendAdditionalMenuItems.htm).) |
| Public method | [AppendMenuItems](M_Grasshopper_Kernel_GH_ActiveObject_AppendMenuItems.htm) | This function is called when a context menu is about to be displayed. Override it to set custom items. GH\_ActiveObject will already populate the menu with default items, if you merely wish to insert object-specific menu item, consider overriding AppendAdditionalMenuItems instead. (Inherited from [GH\_ActiveObject](T_Grasshopper_Kernel_GH_ActiveObject.htm).) |
| Protected method | [AssignInitCodeToInputParameter](M_Grasshopper_Kernel_GH_Component_AssignInitCodeToInputParameter.htm) | Utility function for parsing and assigning init codes. This only works for standard parameter types. (Inherited from [GH\_Component](T_Grasshopper_Kernel_GH_Component.htm).) |
| Public method | [BakeGeometry(RhinoDoc, ListAddLanguageSpecificTextSet("LST88DF80B7\_16?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");GuidAddLanguageSpecificTextSet("LST88DF80B7\_17?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");)](M_Grasshopper_Kernel_GH_Component_BakeGeometry_1.htm) | (Inherited from [GH\_Component](T_Grasshopper_Kernel_GH_Component.htm).) |
| Public method | [BakeGeometry(RhinoDoc, ObjectAttributes, ListAddLanguageSpecificTextSet("LST88DF80B7\_18?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");GuidAddLanguageSpecificTextSet("LST88DF80B7\_19?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");)](M_Grasshopper_Kernel_GH_Component_BakeGeometry.htm) | (Inherited from [GH\_Component](T_Grasshopper_Kernel_GH_Component.htm).) |
| Protected method | [BeforeSolveInstance](M_Grasshopper_Kernel_GH_Component_BeforeSolveInstance.htm) | Override this method if you want to be called before the first call to SolveInstance. (Inherited from [GH\_Component](T_Grasshopper_Kernel_GH_Component.htm).) |
| Public method | [ClearData](M_Grasshopper_Kernel_GH_Component_ClearData.htm) | Clear the data inside this component and all output parameters. (Inherited from [GH\_Component](T_Grasshopper_Kernel_GH_Component.htm).) |
| Public method | [ClearRuntimeMessages](M_Grasshopper_Kernel_GH_Component_ClearRuntimeMessages.htm) | Clears all runtime messages in me and my parameters (Inherited from [GH\_Component](T_Grasshopper_Kernel_GH_Component.htm).) |
| Public method | [CollectData](M_Grasshopper_Kernel_GH_Component_CollectData.htm) | Calls CollectData on all input parameters and makes sure the Component and all associated parameters are left in a valid state. (Inherited from [GH\_Component](T_Grasshopper_Kernel_GH_Component.htm).) |
| Public method | [ComputeData](M_Grasshopper_Kernel_GH_Component_ComputeData.htm) | Compute all data and fill out all output parameters. (Inherited from [GH\_Component](T_Grasshopper_Kernel_GH_Component.htm).) |
| Public method | [CopyFrom](M_Grasshopper_Kernel_GH_InstanceDescription_CopyFrom.htm) | Copy all fields (except the instance ID) from another instance description. (Inherited from [GH\_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).) |
| Public method | [CreateAttributes](M_Grasshopper_Kernel_GH_Component_CreateAttributes.htm) | Create new attributes. (Inherited from [GH\_Component](T_Grasshopper_Kernel_GH_Component.htm).) |
| Public method | [DependsOn](M_Grasshopper_Kernel_GH_Component_DependsOn.htm) | Returns True is any one of my input parameters depends on the source. (Inherited from [GH\_Component](T_Grasshopper_Kernel_GH_Component.htm).) |
| Protected method | [DestroyIconCache](M_Grasshopper_Kernel_GH_DocumentObject_DestroyIconCache.htm) | Call this method to erase the existing icon cache. You must call this if you want to change the display icon of an object. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Public method | [DocumentContextChanged](M_Grasshopper_Kernel_GH_Component_DocumentContextChanged.htm) | Overrides the DocumentContextChanged method and delegates the call to all parameters. (Inherited from [GH\_Component](T_Grasshopper_Kernel_GH_Component.htm).) |
| Public method | [DrawViewportMeshes](M_Grasshopper_Kernel_GH_Component_DrawViewportMeshes.htm) | Draw preview meshes for this component and all associated parameters. (Inherited from [GH\_Component](T_Grasshopper_Kernel_GH_Component.htm).) |
| Public method | [DrawViewportWires](M_Grasshopper_Kernel_GH_Component_DrawViewportWires.htm) | Draw preview wires for this component and all associated parameters. (Inherited from [GH\_Component](T_Grasshopper_Kernel_GH_Component.htm).) |
| Protected method | [ExpireDownStreamObjects](M_Grasshopper_Kernel_GH_Component_ExpireDownStreamObjects.htm) | Expire all objects that depend on any of the output parameters. (Inherited from [GH\_Component](T_Grasshopper_Kernel_GH_Component.htm).) |
| Public method | [ExpirePreview](M_Grasshopper_Kernel_GH_DocumentObject_ExpirePreview.htm) | Call this function when you suspect that the preview has expired for this object. This will cause the display cache to be eradicated. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Public method | [ExpireSolution](M_Grasshopper_Kernel_GH_ActiveObject_ExpireSolution.htm) | Informs the document that owns this object that the solution has expired. The current object will be set to BLANK as a result. This method is recursive, it will also expire any and all objects which depend on this object. If you want a less destructive expiration, consider using ClearData(). If this object is already Blank, you should consider not expiring it. (Inherited from [GH\_ActiveObject](T_Grasshopper_Kernel_GH_ActiveObject.htm).) |
| Protected method | [GenerateDefaultHTML](M_Grasshopper_Kernel_GH_Component_GenerateDefaultHTML.htm) | Creates the default component help topic, including all parameter lists. (Inherited from [GH\_Component](T_Grasshopper_Kernel_GH_Component.htm).) |
| Protected method | [GenerateParameterHelpAddLanguageSpecificTextSet("LST88DF80B7\_20?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_GH_Component_GenerateParameterHelp.htm) | Create an HTML string that lists names and descriptions for input and output parameters. (Inherited from [GH\_Component](T_Grasshopper_Kernel_GH_Component.htm).) |
| Protected method | [GenerateParameterHelp(IGH\_Param)](M_Grasshopper_Kernel_GH_Component_GenerateParameterHelp_1.htm) | Generate HTML string for a single parameter. (Inherited from [GH\_Component](T_Grasshopper_Kernel_GH_Component.htm).) |
| Protected method | [GetSolveResults](M_Grasshopper_Kernel_GH_TaskCapableComponent_1_GetSolveResults.htm) | Call this method to await the associated task and retrieve its data. |
| Protected method | [GetValue(String, Boolean)](M_Grasshopper_Kernel_GH_DocumentObject_GetValue.htm) | Get a boolean value from the component value table. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Protected method | [GetValue(String, Double)](M_Grasshopper_Kernel_GH_DocumentObject_GetValue_1.htm) | Get a double value from the component value table. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Protected method | [GetValue(String, Color)](M_Grasshopper_Kernel_GH_DocumentObject_GetValue_2.htm) | Get a color value from the component value table. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Protected method | [GetValue(String, Int32)](M_Grasshopper_Kernel_GH_DocumentObject_GetValue_3.htm) | Get an integer value from the component value table. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Protected method | [GetValue(String, String)](M_Grasshopper_Kernel_GH_DocumentObject_GetValue_4.htm) | Get a string value from the component value table. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Protected method | [HtmlHelp\_Source](M_Grasshopper_Kernel_GH_Component_HtmlHelp_Source.htm) | Return a String which contains HTML formatted source for the help topic. If you want to pass a URL that points to a remote page, then prefix the URL with a GOTO: tag, like so: GOTO:http://www.YourWebAddressHere.com (Inherited from [GH\_Component](T_Grasshopper_Kernel_GH_Component.htm).) |
| Public method | [IsolateObject](M_Grasshopper_Kernel_GH_Component_IsolateObject.htm) | Sever the connections of all input and output parameters. (Inherited from [GH\_Component](T_Grasshopper_Kernel_GH_Component.htm).) |
| Protected method | [Menu\_AppendBakeItem](M_Grasshopper_Kernel_GH_ActiveObject_Menu_AppendBakeItem.htm) | Append the default Bake menu item. (Inherited from [GH\_ActiveObject](T_Grasshopper_Kernel_GH_ActiveObject.htm).) |
| Protected method | [Menu\_AppendEnableItem](M_Grasshopper_Kernel_GH_ActiveObject_Menu_AppendEnableItem.htm) | Append the default Enable/Disable menu item. (Inherited from [GH\_ActiveObject](T_Grasshopper_Kernel_GH_ActiveObject.htm).) |
| Protected method | [Menu\_AppendObjectHelp](M_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendObjectHelp.htm) | Appends the default object Help menu item. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Protected method | [Menu\_AppendObjectName](M_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendObjectName.htm) | Appends the old-fashioned object name menu item. If you also want the Display mode toggle then use Menu\_AppendObjectNameEx() (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Protected method | [Menu\_AppendObjectNameEx](M_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendObjectNameEx.htm) | Appends the default object name + display mode menu item. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Protected method | [Menu\_AppendPreviewItem](M_Grasshopper_Kernel_GH_ActiveObject_Menu_AppendPreviewItem.htm) | Append the default Show/Hide preview menu item. (Inherited from [GH\_ActiveObject](T_Grasshopper_Kernel_GH_ActiveObject.htm).) |
| Protected method | [Menu\_AppendPublish](M_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendPublish.htm) | Appends the default item for publishing to RCP. This menu will only appear if the current class implement IRcpAwareObject (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Protected method | [Menu\_AppendRuntimeMessages](M_Grasshopper_Kernel_GH_ActiveObject_Menu_AppendRuntimeMessages.htm) | Append the default warnings and errors menu items. (Inherited from [GH\_ActiveObject](T_Grasshopper_Kernel_GH_ActiveObject.htm).) |
| Public method | [MovedBetweenDocuments](M_Grasshopper_Kernel_GH_Component_MovedBetweenDocuments.htm) | Overrides the MovedBetweenDocuments method and delegates the call to all parameters. (Inherited from [GH\_Component](T_Grasshopper_Kernel_GH_Component.htm).) |
| Public method | [NewInstanceGuidAddLanguageSpecificTextSet("LST88DF80B7\_21?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_GH_InstanceDescription_NewInstanceGuid.htm) | Generate a new random instance GUID (Inherited from [GH\_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).) |
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
| Public method | [OnUseTasksClicked](M_Grasshopper_Kernel_GH_TaskCapableComponent_1_OnUseTasksClicked.htm) |  |
| Protected method | [PostConstructor](M_Grasshopper_Kernel_GH_Component_PostConstructor.htm) | The PostConstructor is called from within each constructor. DO NOT OVERRIDE THIS unless you know what you are doing. (Inherited from [GH\_Component](T_Grasshopper_Kernel_GH_Component.htm).) |
| Public method | [Read](M_Grasshopper_Kernel_GH_TaskCapableComponent_1_Read.htm) | (Overrides [GH\_ComponentAddLanguageSpecificTextSet("LST88DF80B7\_22?cs=.|vb=.|cpp=::|nu=.|fs=.");Read(GH\_IReader)](M_Grasshopper_Kernel_GH_Component_Read.htm).) |
| Public method | [ReadFull](M_Grasshopper_Kernel_GH_InstanceDescription_ReadFull.htm) | GH\_InstanceDescription does not by default serialize all fields. Use this function to read *all* fields from the archive. This method is compatible with the default Write()/Read() operations. (Inherited from [GH\_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).) |
| Public method | [RecordUndoEvent(GH\_UndoRecord)](M_Grasshopper_Kernel_GH_DocumentObject_RecordUndoEvent.htm) | Record an entire undo record. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Public method | [RecordUndoEvent(String)](M_Grasshopper_Kernel_GH_DocumentObject_RecordUndoEvent_1.htm) | Record a generic object change undo event. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Public method | [RecordUndoEvent(String, IGH\_UndoAction)](M_Grasshopper_Kernel_GH_DocumentObject_RecordUndoEvent_2.htm) | Record a specific object change undo event. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Protected method | [RegisterInputParams](M_Grasshopper_Kernel_GH_Component_RegisterInputParams.htm) | Declare all your input parameters here. (Inherited from [GH\_Component](T_Grasshopper_Kernel_GH_Component.htm).) |
| Protected method | [RegisterOutputParams](M_Grasshopper_Kernel_GH_Component_RegisterOutputParams.htm) | Declare all your output parameters here. (Inherited from [GH\_Component](T_Grasshopper_Kernel_GH_Component.htm).) |
| Public method | [RegisterRemoteIDs](M_Grasshopper_Kernel_GH_Component_RegisterRemoteIDs.htm) | Registers all my input parameters with the UUID\_LookUpTable (Inherited from [GH\_Component](T_Grasshopper_Kernel_GH_Component.htm).) |
| Public method | [RemovedFromDocument](M_Grasshopper_Kernel_GH_Component_RemovedFromDocument.htm) | Overrides the RemovedFromDocument method and delegates the call to all parameters. (Inherited from [GH\_Component](T_Grasshopper_Kernel_GH_Component.htm).) |
| Public method | [RequestTaskCancellation](M_Grasshopper_Kernel_GH_TaskCapableComponent_1_RequestTaskCancellation.htm) | Called by the framework when solving has been interrupted and tasks do not need to complete. |
| Public method | [RuntimeMessages](M_Grasshopper_Kernel_GH_Component_RuntimeMessages.htm) | Gets the list of cached runtime messages that were recorded during solver-time processes. For components, the set of runtime messages also includes input and output parameters. (Inherited from [GH\_Component](T_Grasshopper_Kernel_GH_Component.htm).) |
| Public method | [SDKCompliancy](M_Grasshopper_Kernel_GH_ActiveObject_SDKCompliancy.htm) | Test whether this object is compliant with a given Rhino version. (Inherited from [GH\_ActiveObject](T_Grasshopper_Kernel_GH_ActiveObject.htm).) |
| Public method | [SetIconOverride](M_Grasshopper_Kernel_GH_DocumentObject_SetIconOverride.htm) | Set a new custom icon override for this object. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Protected method | [SetValue(String, Boolean)](M_Grasshopper_Kernel_GH_DocumentObject_SetValue.htm) | Set a named value. This value will be serialized with the component. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Protected method | [SetValue(String, Double)](M_Grasshopper_Kernel_GH_DocumentObject_SetValue_1.htm) | Set a named value. This value will be serialized with the component. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Protected method | [SetValue(String, Color)](M_Grasshopper_Kernel_GH_DocumentObject_SetValue_2.htm) | Set a named value. This value will be serialized with the component. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Protected method | [SetValue(String, Int32)](M_Grasshopper_Kernel_GH_DocumentObject_SetValue_3.htm) | Set a named value. This value will be serialized with the component. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Protected method | [SetValue(String, String)](M_Grasshopper_Kernel_GH_DocumentObject_SetValue_4.htm) | Set a named value. This value will be serialized with the component. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Protected method | [SolveInstance](M_Grasshopper_Kernel_GH_Component_SolveInstance.htm) | This function will be called (successively) from within the ComputeData method of this component. (Inherited from [GH\_Component](T_Grasshopper_Kernel_GH_Component.htm).) |
| Public method | [TriggerAutoSaveAddLanguageSpecificTextSet("LST88DF80B7\_23?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_GH_DocumentObject_TriggerAutoSave.htm) | Triggers the AutoSave function on the owner document with the object\_changed flag. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Public method | [TriggerAutoSave(GH\_AutoSaveTrigger)](M_Grasshopper_Kernel_GH_DocumentObject_TriggerAutoSave_1.htm) | Triggers the AutoSave function on the owner document with a custom flag. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Public method | [TriggerAutoSave(Guid)](M_Grasshopper_Kernel_GH_DocumentObject_TriggerAutoSave_3.htm) | Triggers the AutoSave function on the owner document with the object\_changed flag. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Public method | [TriggerAutoSave(GH\_AutoSaveTrigger, Guid)](M_Grasshopper_Kernel_GH_DocumentObject_TriggerAutoSave_2.htm) | Triggers the AutoSave function on the owner document with a custom flag. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Protected method | [ValuesChanged](M_Grasshopper_Kernel_GH_DocumentObject_ValuesChanged.htm) | Override this method if you want to respond to changes to the value table. The base implementation is empty, so you don't have to call it. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Public method | [Write](M_Grasshopper_Kernel_GH_TaskCapableComponent_1_Write.htm) | (Overrides [GH\_ComponentAddLanguageSpecificTextSet("LST88DF80B7\_24?cs=.|vb=.|cpp=::|nu=.|fs=.");Write(GH\_IWriter)](M_Grasshopper_Kernel_GH_Component_Write.htm).) |
| Public method | [WriteFull](M_Grasshopper_Kernel_GH_InstanceDescription_WriteFull.htm) | GH\_InstanceDescription does not by default serialize all fields. Use this function to write *all* fields to the archive. This method is compatible with the default Write()/Read() operations. (Inherited from [GH\_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Events

|  | Name | Description |
| --- | --- | --- |
| Public event | [AttributesChanged](E_Grasshopper_Kernel_GH_DocumentObject_AttributesChanged.htm) | Raised whenever the number or kind of attributes changes. This event is handled by GH\_Documents who subsequently wipe their attribute caches. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Public event | [DisplayExpired](E_Grasshopper_Kernel_GH_DocumentObject_DisplayExpired.htm) | Raised whenever the display (on the Canvas) of a certain object becomes invalid. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Public event | [ObjectChanged](E_Grasshopper_Kernel_GH_DocumentObject_ObjectChanged.htm) | (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Public event | [PingDocument](E_Grasshopper_Kernel_GH_DocumentObject_PingDocument.htm) | Raised whenever an object needs to know which GH\_Document it belongs to. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Public event | [PreviewExpired](E_Grasshopper_Kernel_GH_DocumentObject_PreviewExpired.htm) | Raised whenever the display (in the Rhino viewports) of a certain object becomes invalid. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Public event | [SolutionExpired](E_Grasshopper_Kernel_GH_DocumentObject_SolutionExpired.htm) | Raised whenever the solution of a certain object becomes invalid. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Fields

|  | Name | Description |
| --- | --- | --- |
| Protected field | [m\_attributes](F_Grasshopper_Kernel_GH_DocumentObject_m_attributes.htm) | (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)