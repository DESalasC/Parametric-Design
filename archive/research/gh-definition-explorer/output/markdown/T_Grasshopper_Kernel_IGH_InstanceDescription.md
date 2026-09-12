# T_Grasshopper_Kernel_IGH_InstanceDescription

﻿ IGH\_InstanceDescription Interface

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH\_InstanceDescription Interface](../html/T_Grasshopper_Kernel_IGH_InstanceDescription.htm "IGH_InstanceDescription Interface")

[IGH\_InstanceDescription Properties](../html/Properties_T_Grasshopper_Kernel_IGH_InstanceDescription.htm "IGH_InstanceDescription Properties")

[IGH\_InstanceDescription Methods](../html/Methods_T_Grasshopper_Kernel_IGH_InstanceDescription.htm "IGH_InstanceDescription Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_InstanceDescription Interface |

Base interface for all objects that participate in the Grasshopper GUI.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public interface IGH_InstanceDescription : GH_ISerializable
```

```
Public Interface IGH_InstanceDescription
	Inherits GH_ISerializable
```

AddLanguageTabSet("ID0EBCA");

The IGH\_InstanceDescription type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Category](P_Grasshopper_Kernel_IGH_InstanceDescription_Category.htm) | Gets or sets the Category in which this object belongs. If HasCategory() returns false, this field has no meaning. |
| Public property | [Description](P_Grasshopper_Kernel_IGH_InstanceDescription_Description.htm) | Gets or sets the description of the object. This field typically remains fixed during the lifetime of an object. |
| Public property | [HasCategory](P_Grasshopper_Kernel_IGH_InstanceDescription_HasCategory.htm) | Gets whether or not the Category field has been set. |
| Public property | [HasSubCategory](P_Grasshopper_Kernel_IGH_InstanceDescription_HasSubCategory.htm) | Gets whether or not the SubCategory field has been set. |
| Public property | [InstanceDescription](P_Grasshopper_Kernel_IGH_InstanceDescription_InstanceDescription.htm) | Gets a description of the current state of the object. This field is usually the same as the Description() field, but it might be variable when overridden. |
| Public property | [InstanceGuid](P_Grasshopper_Kernel_IGH_InstanceDescription_InstanceGuid.htm) | Gets the ID of this runtime instance. |
| Public property | [Keywords](P_Grasshopper_Kernel_IGH_InstanceDescription_Keywords.htm) | Gets a list of additional keywords that describe the object. Typically this list is empty but you can override this property to aid in object searches. |
| Public property | [Name](P_Grasshopper_Kernel_IGH_InstanceDescription_Name.htm) | Gets or sets the name of the object. This field typically remains fixed during the lifetime of an object. |
| Public property | [NickName](P_Grasshopper_Kernel_IGH_InstanceDescription_NickName.htm) | Gets or sets the nickname of the object. This field can be changed by the user. |
| Public property | [SubCategory](P_Grasshopper_Kernel_IGH_InstanceDescription_SubCategory.htm) | Gets or sets the SubCategory in which this object belongs. If HasSubCategory() returns false, this field has no meaning. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [NewInstanceGuidAddLanguageSpecificTextSet("LSTF29BDBBB\_0?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_IGH_InstanceDescription_NewInstanceGuid.htm) | Generate a new random instance GUID |
| Public method | [NewInstanceGuid(Guid)](M_Grasshopper_Kernel_IGH_InstanceDescription_NewInstanceGuid_1.htm) | Set the instance ID to be a specific GUID. This is very dangerous, only use this function if you're 6"4' and called David. |
| Public method | [Read](M_GH_IO_GH_ISerializable_Read.htm) | This method is called whenever the instance is required to deserialize itself. (Inherited from [GH\_ISerializable](T_GH_IO_GH_ISerializable.htm).) |
| Public method | [Write](M_GH_IO_GH_ISerializable_Write.htm) | This method is called whenever the instance is required to serialize itself. (Inherited from [GH\_ISerializable](T_GH_IO_GH_ISerializable.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Remarks

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)