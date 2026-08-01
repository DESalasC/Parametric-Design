# Properties_T_Grasshopper_Kernel_GH_Component

﻿ GH\_Component Properties

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_Component Class](../html/T_Grasshopper_Kernel_GH_Component.htm "GH_Component Class")

[GH\_Component Properties](../html/Properties_T_Grasshopper_Kernel_GH_Component.htm "GH_Component Properties")

[ClippingBox Property](../html/P_Grasshopper_Kernel_GH_Component_ClippingBox.htm "ClippingBox Property ")

[HelpDescription Property](../html/P_Grasshopper_Kernel_GH_Component_HelpDescription.htm "HelpDescription Property ")

[Hidden Property](../html/P_Grasshopper_Kernel_GH_Component_Hidden.htm "Hidden Property ")

[InConstructor Property](../html/P_Grasshopper_Kernel_GH_Component_InConstructor.htm "InConstructor Property ")

[InstanceDescription Property](../html/P_Grasshopper_Kernel_GH_Component_InstanceDescription.htm "InstanceDescription Property ")

[IsBakeCapable Property](../html/P_Grasshopper_Kernel_GH_Component_IsBakeCapable.htm "IsBakeCapable Property ")

[IsDataProvider Property](../html/P_Grasshopper_Kernel_GH_Component_IsDataProvider.htm "IsDataProvider Property ")

[IsPreviewCapable Property](../html/P_Grasshopper_Kernel_GH_Component_IsPreviewCapable.htm "IsPreviewCapable Property ")

[IsValidPrincipalParameterIndex Property](../html/P_Grasshopper_Kernel_GH_Component_IsValidPrincipalParameterIndex.htm "IsValidPrincipalParameterIndex Property ")

[Locked Property](../html/P_Grasshopper_Kernel_GH_Component_Locked.htm "Locked Property ")

[Message Property](../html/P_Grasshopper_Kernel_GH_Component_Message.htm "Message Property ")

[Params Property](../html/P_Grasshopper_Kernel_GH_Component_Params.htm "Params Property ")

[PrincipalParameterIndex Property](../html/P_Grasshopper_Kernel_GH_Component_PrincipalParameterIndex.htm "PrincipalParameterIndex Property ")

[ProcessorTime Property](../html/P_Grasshopper_Kernel_GH_Component_ProcessorTime.htm "ProcessorTime Property ")

[RunCount Property](../html/P_Grasshopper_Kernel_GH_Component_RunCount.htm "RunCount Property ")

[RuntimeMessageLevel Property](../html/P_Grasshopper_Kernel_GH_Component_RuntimeMessageLevel.htm "RuntimeMessageLevel Property ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_Component Properties |

The [GH\_Component](T_Grasshopper_Kernel_GH_Component.htm) type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Attributes](P_Grasshopper_Kernel_GH_DocumentObject_Attributes.htm) | Gets or sets the attributes that are associated with this object. Only set custom attributes if you know what you are doing. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Public property | [Category](P_Grasshopper_Kernel_GH_InstanceDescription_Category.htm) | Gets or sets the Category in which this object belongs. If HasCategory() returns false, this field has no meaning. (Inherited from [GH\_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).) |
| Public property | [ClippingBox](P_Grasshopper_Kernel_GH_Component_ClippingBox.htm) | Gets the clipping box for all preview geometry drawn by this component and all associated parameters. |
| Public property | [ComponentGuid](P_Grasshopper_Kernel_GH_DocumentObject_ComponentGuid.htm) | Returns a consistent ID for this object type. Every object must supply a unique and unchanging ID that is used to identify objects of the same type. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Public property | [Description](P_Grasshopper_Kernel_GH_InstanceDescription_Description.htm) | Gets or sets the description of the object. This field typically remains fixed during the lifetime of an object. (Inherited from [GH\_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).) |
| Public property | [Exposure](P_Grasshopper_Kernel_GH_DocumentObject_Exposure.htm) | Gets the exposure of this object in the Graphical User Interface. The default is to expose everywhere. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Public property | [HasCategory](P_Grasshopper_Kernel_GH_InstanceDescription_HasCategory.htm) | Gets whether or not the Category field has been set. (Inherited from [GH\_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).) |
| Public property | [HasSubCategory](P_Grasshopper_Kernel_GH_InstanceDescription_HasSubCategory.htm) | Gets whether or not the SubCategory field has been set. (Inherited from [GH\_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).) |
| Protected property | [HelpDescription](P_Grasshopper_Kernel_GH_Component_HelpDescription.htm) | Override this method if you want the help topic content to be more than the Component description. |
| Public property | [Hidden](P_Grasshopper_Kernel_GH_Component_Hidden.htm) | Gets or sets the hidden flag for this component. Does not affect Hidden flags on parameters associated with this component. |
| Protected property | [Icon](P_Grasshopper_Kernel_GH_DocumentObject_Icon.htm) | Override this function to supply a custom icon (24x24 pixels). The result of this property is cached, so don't worry if icon retrieval is not very fast. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Public property | [Icon\_24x24](P_Grasshopper_Kernel_GH_DocumentObject_Icon_24x24.htm) | The icon associated with this object. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Public property | [Icon\_24x24\_Locked](P_Grasshopper_Kernel_GH_DocumentObject_Icon_24x24_Locked.htm) | The greyscale icon of this object. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Public property | [IconCapableUI](P_Grasshopper_Kernel_GH_ActiveObject_IconCapableUI.htm) | By default the NickName menu item supports the Icon Mode override toggle. If your UI is not capable of displaying icons, then override this property and return False. (Inherited from [GH\_ActiveObject](T_Grasshopper_Kernel_GH_ActiveObject.htm).) |
| Public property | [IconDisplayMode](P_Grasshopper_Kernel_GH_DocumentObject_IconDisplayMode.htm) | Gets the current display mode of the object. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Public property | [InConstructor](P_Grasshopper_Kernel_GH_Component_InConstructor.htm) | Gets the constructor flag for this instance. If InConstructor = True, it means the component is still registering parameters and the layout is not yet complete. |
| Public property | [InstanceDescription](P_Grasshopper_Kernel_GH_Component_InstanceDescription.htm) | (Overrides [GH\_InstanceDescriptionAddLanguageSpecificTextSet("LSTD7C81ABE\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");InstanceDescription](P_Grasshopper_Kernel_GH_InstanceDescription_InstanceDescription.htm).) |
| Public property | [InstanceGuid](P_Grasshopper_Kernel_GH_InstanceDescription_InstanceGuid.htm) | Gets the ID of this runtime instance. (Inherited from [GH\_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).) |
| Public property | [IsBakeCapable](P_Grasshopper_Kernel_GH_Component_IsBakeCapable.htm) |  |
| Public property | [IsDataProvider](P_Grasshopper_Kernel_GH_Component_IsDataProvider.htm) | Components are never Data providers. Only the output parameters can be considered to be providers. (Overrides [GH\_ActiveObjectAddLanguageSpecificTextSet("LSTD7C81ABE\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");IsDataProvider](P_Grasshopper_Kernel_GH_ActiveObject_IsDataProvider.htm).) |
| Public property | [IsPreviewCapable](P_Grasshopper_Kernel_GH_Component_IsPreviewCapable.htm) | If a single parameter is PreviewCapable, so is the component. Override this property if you need special Preview flags. |
| Public property | [IsValidPrincipalParameterIndex](P_Grasshopper_Kernel_GH_Component_IsValidPrincipalParameterIndex.htm) | Gets whether the MasterParameterIndex property identifies a valid parameter. |
| Public property | [Keywords](P_Grasshopper_Kernel_GH_InstanceDescription_Keywords.htm) | Gets a list of additional keywords that describe the object. Typically this list is empty but you can override this property to aid in object searches. (Inherited from [GH\_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).) |
| Public property | [Locked](P_Grasshopper_Kernel_GH_Component_Locked.htm) | Gets or sets the Locked state for this Component. This also sets locked states for all input and output parameters. (Overrides [GH\_ActiveObjectAddLanguageSpecificTextSet("LSTD7C81ABE\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Locked](P_Grasshopper_Kernel_GH_ActiveObject_Locked.htm).) |
| Public property | [Message](P_Grasshopper_Kernel_GH_Component_Message.htm) | Gets or sets a custom message to be displayed underneath the component. This message is not serialized and should be assigned on every solution anew. |
| Public property | [MutableNickName](P_Grasshopper_Kernel_GH_ActiveObject_MutableNickName.htm) | Gets or sets a value that enables Nick name changes through the menu. The default is TRUE. (Inherited from [GH\_ActiveObject](T_Grasshopper_Kernel_GH_ActiveObject.htm).) |
| Public property | [Name](P_Grasshopper_Kernel_GH_InstanceDescription_Name.htm) | Gets or sets the name of the object. This field typically remains fixed during the lifetime of an object. (Inherited from [GH\_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).) |
| Public property | [NickName](P_Grasshopper_Kernel_GH_InstanceDescription_NickName.htm) | Gets or sets the nickname of the object. This field can be changed by the user. (Inherited from [GH\_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).) |
| Public property | [Obsolete](P_Grasshopper_Kernel_GH_DocumentObject_Obsolete.htm) | Gets whether this object is obsolete. Default implementation returns true if the class name contains the string "OBSOLETE" or if this class has been decorated with the ObsoleteAttribute. You are free to override this if you want, but I suggest adding the ObsoleteAttribute instead. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Public property | [Params](P_Grasshopper_Kernel_GH_Component_Params.htm) | Gets the parameter manager object for this component. |
| Public property | [Phase](P_Grasshopper_Kernel_GH_ActiveObject_Phase.htm) | Gets or sets the solution phase this object is currenly in. (Inherited from [GH\_ActiveObject](T_Grasshopper_Kernel_GH_ActiveObject.htm).) |
| Public property | [PrincipalParameterIndex](P_Grasshopper_Kernel_GH_Component_PrincipalParameterIndex.htm) | Gets or sets the principal parameter index override. Negative indices or indices larger than or equal to the input parameter count will be ignored and regular principal parameter detection will kick in. |
| Public property | [ProcessorTime](P_Grasshopper_Kernel_GH_Component_ProcessorTime.htm) | Gets the total processor time (profiler) spend by this component and all input parameters. (Overrides [GH\_ActiveObjectAddLanguageSpecificTextSet("LSTD7C81ABE\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");ProcessorTime](P_Grasshopper_Kernel_GH_ActiveObject_ProcessorTime.htm).) |
| Public property | [RunCount](P_Grasshopper_Kernel_GH_Component_RunCount.htm) | Gets a value indicating how many times the SolveInstance method was called on this component during the last solution. This property will return -1 if no valid runcount is available. |
| Public property | [RuntimeMessageLevel](P_Grasshopper_Kernel_GH_Component_RuntimeMessageLevel.htm) | Returns the worst case runtime warning level of me and all my parameters (Overrides [GH\_ActiveObjectAddLanguageSpecificTextSet("LSTD7C81ABE\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");RuntimeMessageLevel](P_Grasshopper_Kernel_GH_ActiveObject_RuntimeMessageLevel.htm).) |
| Public property | [SubCategory](P_Grasshopper_Kernel_GH_InstanceDescription_SubCategory.htm) | Gets or sets the SubCategory in which this object belongs. If HasSubCategory() returns false, this field has no meaning. (Inherited from [GH\_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Component Class](T_Grasshopper_Kernel_GH_Component.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)