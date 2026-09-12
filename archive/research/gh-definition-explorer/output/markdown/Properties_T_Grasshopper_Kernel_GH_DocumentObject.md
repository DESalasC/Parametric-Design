# Properties_T_Grasshopper_Kernel_GH_DocumentObject

﻿ GH\_DocumentObject Properties

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_DocumentObject Class](../html/T_Grasshopper_Kernel_GH_DocumentObject.htm "GH_DocumentObject Class")

[GH\_DocumentObject Properties](../html/Properties_T_Grasshopper_Kernel_GH_DocumentObject.htm "GH_DocumentObject Properties")

[Attributes Property](../html/P_Grasshopper_Kernel_GH_DocumentObject_Attributes.htm "Attributes Property ")

[ComponentGuid Property](../html/P_Grasshopper_Kernel_GH_DocumentObject_ComponentGuid.htm "ComponentGuid Property ")

[Exposure Property](../html/P_Grasshopper_Kernel_GH_DocumentObject_Exposure.htm "Exposure Property ")

[Icon Property](../html/P_Grasshopper_Kernel_GH_DocumentObject_Icon.htm "Icon Property ")

[Icon\_24x24 Property](../html/P_Grasshopper_Kernel_GH_DocumentObject_Icon_24x24.htm "Icon_24x24 Property ")

[Icon\_24x24\_Locked Property](../html/P_Grasshopper_Kernel_GH_DocumentObject_Icon_24x24_Locked.htm "Icon_24x24_Locked Property ")

[IconDisplayMode Property](../html/P_Grasshopper_Kernel_GH_DocumentObject_IconDisplayMode.htm "IconDisplayMode Property ")

[Obsolete Property](../html/P_Grasshopper_Kernel_GH_DocumentObject_Obsolete.htm "Obsolete Property ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_DocumentObject Properties |

The [GH\_DocumentObject](T_Grasshopper_Kernel_GH_DocumentObject.htm) type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Attributes](P_Grasshopper_Kernel_GH_DocumentObject_Attributes.htm) | Gets or sets the attributes that are associated with this object. Only set custom attributes if you know what you are doing. |
| Public property | [Category](P_Grasshopper_Kernel_GH_InstanceDescription_Category.htm) | Gets or sets the Category in which this object belongs. If HasCategory() returns false, this field has no meaning. (Inherited from [GH\_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).) |
| Public property | [ComponentGuid](P_Grasshopper_Kernel_GH_DocumentObject_ComponentGuid.htm) | Returns a consistent ID for this object type. Every object must supply a unique and unchanging ID that is used to identify objects of the same type. |
| Public property | [Description](P_Grasshopper_Kernel_GH_InstanceDescription_Description.htm) | Gets or sets the description of the object. This field typically remains fixed during the lifetime of an object. (Inherited from [GH\_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).) |
| Public property | [Exposure](P_Grasshopper_Kernel_GH_DocumentObject_Exposure.htm) | Gets the exposure of this object in the Graphical User Interface. The default is to expose everywhere. |
| Public property | [HasCategory](P_Grasshopper_Kernel_GH_InstanceDescription_HasCategory.htm) | Gets whether or not the Category field has been set. (Inherited from [GH\_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).) |
| Public property | [HasSubCategory](P_Grasshopper_Kernel_GH_InstanceDescription_HasSubCategory.htm) | Gets whether or not the SubCategory field has been set. (Inherited from [GH\_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).) |
| Protected property | [Icon](P_Grasshopper_Kernel_GH_DocumentObject_Icon.htm) | Override this function to supply a custom icon (24x24 pixels). The result of this property is cached, so don't worry if icon retrieval is not very fast. |
| Public property | [Icon\_24x24](P_Grasshopper_Kernel_GH_DocumentObject_Icon_24x24.htm) | The icon associated with this object. |
| Public property | [Icon\_24x24\_Locked](P_Grasshopper_Kernel_GH_DocumentObject_Icon_24x24_Locked.htm) | The greyscale icon of this object. |
| Public property | [IconDisplayMode](P_Grasshopper_Kernel_GH_DocumentObject_IconDisplayMode.htm) | Gets the current display mode of the object. |
| Public property | [InstanceDescription](P_Grasshopper_Kernel_GH_InstanceDescription_InstanceDescription.htm) | Gets a description of the current state of the object. This field is usually the same as the Description() field, but it might be variable when overridden. (Inherited from [GH\_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).) |
| Public property | [InstanceGuid](P_Grasshopper_Kernel_GH_InstanceDescription_InstanceGuid.htm) | Gets the ID of this runtime instance. (Inherited from [GH\_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).) |
| Public property | [Keywords](P_Grasshopper_Kernel_GH_InstanceDescription_Keywords.htm) | Gets a list of additional keywords that describe the object. Typically this list is empty but you can override this property to aid in object searches. (Inherited from [GH\_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).) |
| Public property | [Name](P_Grasshopper_Kernel_GH_InstanceDescription_Name.htm) | Gets or sets the name of the object. This field typically remains fixed during the lifetime of an object. (Inherited from [GH\_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).) |
| Public property | [NickName](P_Grasshopper_Kernel_GH_InstanceDescription_NickName.htm) | Gets or sets the nickname of the object. This field can be changed by the user. (Inherited from [GH\_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).) |
| Public property | [Obsolete](P_Grasshopper_Kernel_GH_DocumentObject_Obsolete.htm) | Gets whether this object is obsolete. Default implementation returns true if the class name contains the string "OBSOLETE" or if this class has been decorated with the ObsoleteAttribute. You are free to override this if you want, but I suggest adding the ObsoleteAttribute instead. |
| Public property | [SubCategory](P_Grasshopper_Kernel_GH_InstanceDescription_SubCategory.htm) | Gets or sets the SubCategory in which this object belongs. If HasSubCategory() returns false, this field has no meaning. (Inherited from [GH\_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_DocumentObject Class](T_Grasshopper_Kernel_GH_DocumentObject.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)