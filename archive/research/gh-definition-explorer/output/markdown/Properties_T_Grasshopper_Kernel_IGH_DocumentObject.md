# Properties_T_Grasshopper_Kernel_IGH_DocumentObject

﻿ IGH\_DocumentObject Properties

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH\_DocumentObject Interface](../html/T_Grasshopper_Kernel_IGH_DocumentObject.htm "IGH_DocumentObject Interface")

[IGH\_DocumentObject Properties](../html/Properties_T_Grasshopper_Kernel_IGH_DocumentObject.htm "IGH_DocumentObject Properties")

[Attributes Property](../html/P_Grasshopper_Kernel_IGH_DocumentObject_Attributes.htm "Attributes Property ")

[ComponentGuid Property](../html/P_Grasshopper_Kernel_IGH_DocumentObject_ComponentGuid.htm "ComponentGuid Property ")

[Exposure Property](../html/P_Grasshopper_Kernel_IGH_DocumentObject_Exposure.htm "Exposure Property ")

[Icon\_24x24 Property](../html/P_Grasshopper_Kernel_IGH_DocumentObject_Icon_24x24.htm "Icon_24x24 Property ")

[Icon\_24x24\_Locked Property](../html/P_Grasshopper_Kernel_IGH_DocumentObject_Icon_24x24_Locked.htm "Icon_24x24_Locked Property ")

[IconDisplayMode Property](../html/P_Grasshopper_Kernel_IGH_DocumentObject_IconDisplayMode.htm "IconDisplayMode Property ")

[Obsolete Property](../html/P_Grasshopper_Kernel_IGH_DocumentObject_Obsolete.htm "Obsolete Property ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_DocumentObject Properties |

The [IGH\_DocumentObject](T_Grasshopper_Kernel_IGH_DocumentObject.htm) type exposes the following members.

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

![](../icons/SectionExpanded.png)See Also

#### Reference

[IGH\_DocumentObject Interface](T_Grasshopper_Kernel_IGH_DocumentObject.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)