# Properties_T_Grasshopper_Kernel_GH_ActiveObject

﻿ GH\_ActiveObject Properties

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_ActiveObject Class](../html/T_Grasshopper_Kernel_GH_ActiveObject.htm "GH_ActiveObject Class")

[GH\_ActiveObject Properties](../html/Properties_T_Grasshopper_Kernel_GH_ActiveObject.htm "GH_ActiveObject Properties")

[IconCapableUI Property](../html/P_Grasshopper_Kernel_GH_ActiveObject_IconCapableUI.htm "IconCapableUI Property ")

[IsDataProvider Property](../html/P_Grasshopper_Kernel_GH_ActiveObject_IsDataProvider.htm "IsDataProvider Property ")

[Locked Property](../html/P_Grasshopper_Kernel_GH_ActiveObject_Locked.htm "Locked Property ")

[MutableNickName Property](../html/P_Grasshopper_Kernel_GH_ActiveObject_MutableNickName.htm "MutableNickName Property ")

[Phase Property](../html/P_Grasshopper_Kernel_GH_ActiveObject_Phase.htm "Phase Property ")

[ProcessorTime Property](../html/P_Grasshopper_Kernel_GH_ActiveObject_ProcessorTime.htm "ProcessorTime Property ")

[RuntimeMessageLevel Property](../html/P_Grasshopper_Kernel_GH_ActiveObject_RuntimeMessageLevel.htm "RuntimeMessageLevel Property ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ActiveObject Properties |

The [GH\_ActiveObject](T_Grasshopper_Kernel_GH_ActiveObject.htm) type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Attributes](P_Grasshopper_Kernel_GH_DocumentObject_Attributes.htm) | Gets or sets the attributes that are associated with this object. Only set custom attributes if you know what you are doing. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Public property | [Category](P_Grasshopper_Kernel_GH_InstanceDescription_Category.htm) | Gets or sets the Category in which this object belongs. If HasCategory() returns false, this field has no meaning. (Inherited from [GH\_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).) |
| Public property | [ComponentGuid](P_Grasshopper_Kernel_GH_DocumentObject_ComponentGuid.htm) | Returns a consistent ID for this object type. Every object must supply a unique and unchanging ID that is used to identify objects of the same type. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Public property | [Description](P_Grasshopper_Kernel_GH_InstanceDescription_Description.htm) | Gets or sets the description of the object. This field typically remains fixed during the lifetime of an object. (Inherited from [GH\_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).) |
| Public property | [Exposure](P_Grasshopper_Kernel_GH_DocumentObject_Exposure.htm) | Gets the exposure of this object in the Graphical User Interface. The default is to expose everywhere. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Public property | [HasCategory](P_Grasshopper_Kernel_GH_InstanceDescription_HasCategory.htm) | Gets whether or not the Category field has been set. (Inherited from [GH\_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).) |
| Public property | [HasSubCategory](P_Grasshopper_Kernel_GH_InstanceDescription_HasSubCategory.htm) | Gets whether or not the SubCategory field has been set. (Inherited from [GH\_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).) |
| Protected property | [Icon](P_Grasshopper_Kernel_GH_DocumentObject_Icon.htm) | Override this function to supply a custom icon (24x24 pixels). The result of this property is cached, so don't worry if icon retrieval is not very fast. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Public property | [Icon\_24x24](P_Grasshopper_Kernel_GH_DocumentObject_Icon_24x24.htm) | The icon associated with this object. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Public property | [Icon\_24x24\_Locked](P_Grasshopper_Kernel_GH_DocumentObject_Icon_24x24_Locked.htm) | The greyscale icon of this object. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Public property | [IconCapableUI](P_Grasshopper_Kernel_GH_ActiveObject_IconCapableUI.htm) | By default the NickName menu item supports the Icon Mode override toggle. If your UI is not capable of displaying icons, then override this property and return False. |
| Public property | [IconDisplayMode](P_Grasshopper_Kernel_GH_DocumentObject_IconDisplayMode.htm) | Gets the current display mode of the object. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Public property | [InstanceDescription](P_Grasshopper_Kernel_GH_InstanceDescription_InstanceDescription.htm) | Gets a description of the current state of the object. This field is usually the same as the Description() field, but it might be variable when overridden. (Inherited from [GH\_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).) |
| Public property | [InstanceGuid](P_Grasshopper_Kernel_GH_InstanceDescription_InstanceGuid.htm) | Gets the ID of this runtime instance. (Inherited from [GH\_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).) |
| Public property | [IsDataProvider](P_Grasshopper_Kernel_GH_ActiveObject_IsDataProvider.htm) | Returns a boolean indicating whether or not the current object can seed data. |
| Public property | [Keywords](P_Grasshopper_Kernel_GH_InstanceDescription_Keywords.htm) | Gets a list of additional keywords that describe the object. Typically this list is empty but you can override this property to aid in object searches. (Inherited from [GH\_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).) |
| Public property | [Locked](P_Grasshopper_Kernel_GH_ActiveObject_Locked.htm) | Gets or sets the enabled flag of this object. Disabled objects are ignored during solutions. |
| Public property | [MutableNickName](P_Grasshopper_Kernel_GH_ActiveObject_MutableNickName.htm) | Gets or sets a value that enables Nick name changes through the menu. The default is TRUE. |
| Public property | [Name](P_Grasshopper_Kernel_GH_InstanceDescription_Name.htm) | Gets or sets the name of the object. This field typically remains fixed during the lifetime of an object. (Inherited from [GH\_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).) |
| Public property | [NickName](P_Grasshopper_Kernel_GH_InstanceDescription_NickName.htm) | Gets or sets the nickname of the object. This field can be changed by the user. (Inherited from [GH\_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).) |
| Public property | [Obsolete](P_Grasshopper_Kernel_GH_DocumentObject_Obsolete.htm) | Gets whether this object is obsolete. Default implementation returns true if the class name contains the string "OBSOLETE" or if this class has been decorated with the ObsoleteAttribute. You are free to override this if you want, but I suggest adding the ObsoleteAttribute instead. (Inherited from [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm).) |
| Public property | [Phase](P_Grasshopper_Kernel_GH_ActiveObject_Phase.htm) | Gets or sets the solution phase this object is currenly in. |
| Public property | [ProcessorTime](P_Grasshopper_Kernel_GH_ActiveObject_ProcessorTime.htm) | Gets the most recent processor time profiler value. |
| Public property | [RuntimeMessageLevel](P_Grasshopper_Kernel_GH_ActiveObject_RuntimeMessageLevel.htm) | Returns the worst case flag for the current object If the object contains at least 1 error, the result is Error.  If the object contains at least 1 warning, the result is Warning.  If the object contains at least 1 message, the result is Remark.  If the object contains no errors, no warnings and no messages, the result is Blank. |
| Public property | [SubCategory](P_Grasshopper_Kernel_GH_InstanceDescription_SubCategory.htm) | Gets or sets the SubCategory in which this object belongs. If HasSubCategory() returns false, this field has no meaning. (Inherited from [GH\_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_ActiveObject Class](T_Grasshopper_Kernel_GH_ActiveObject.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)