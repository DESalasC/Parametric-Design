# Methods_T_Grasshopper_Kernel_GH_InstanceDescription

﻿ GH\_InstanceDescription Methods

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_InstanceDescription Class](../html/T_Grasshopper_Kernel_GH_InstanceDescription.htm "GH_InstanceDescription Class")

[GH\_InstanceDescription Methods](../html/Methods_T_Grasshopper_Kernel_GH_InstanceDescription.htm "GH_InstanceDescription Methods")

[CopyFrom Method](../html/M_Grasshopper_Kernel_GH_InstanceDescription_CopyFrom.htm "CopyFrom Method ")

[NewInstanceGuid Method](../html/Overload_Grasshopper_Kernel_GH_InstanceDescription_NewInstanceGuid.htm "NewInstanceGuid Method ")

[Read Method](../html/M_Grasshopper_Kernel_GH_InstanceDescription_Read.htm "Read Method ")

[ReadFull Method](../html/M_Grasshopper_Kernel_GH_InstanceDescription_ReadFull.htm "ReadFull Method ")

[Write Method](../html/M_Grasshopper_Kernel_GH_InstanceDescription_Write.htm "Write Method ")

[WriteFull Method](../html/M_Grasshopper_Kernel_GH_InstanceDescription_WriteFull.htm "WriteFull Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_InstanceDescription Methods |

The [GH\_InstanceDescription](T_Grasshopper_Kernel_GH_InstanceDescription.htm) type exposes the following members.

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [CopyFrom](M_Grasshopper_Kernel_GH_InstanceDescription_CopyFrom.htm) | Copy all fields (except the instance ID) from another instance description. |
| Public method | [NewInstanceGuidAddLanguageSpecificTextSet("LSTA9C1AD9E\_0?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_GH_InstanceDescription_NewInstanceGuid.htm) | Generate a new random instance GUID |
| Public method | [NewInstanceGuid(Guid)](M_Grasshopper_Kernel_GH_InstanceDescription_NewInstanceGuid_1.htm) | Set the instance ID to be a specific GUID. This is very dangerous, only use this function if you're 6"4' and your first name is David. |
| Public method | [Read](M_Grasshopper_Kernel_GH_InstanceDescription_Read.htm) | Default deserialization. Only retrieves Name, NickName, Description and InstanceGuid fields. If you want to retrieve additional fields use ReadFull() instead. However, ReadFull() will only work if the archive was written using WriteFull(). |
| Public method | [ReadFull](M_Grasshopper_Kernel_GH_InstanceDescription_ReadFull.htm) | GH\_InstanceDescription does not by default serialize all fields. Use this function to read *all* fields from the archive. This method is compatible with the default Write()/Read() operations. |
| Public method | [Write](M_Grasshopper_Kernel_GH_InstanceDescription_Write.htm) | Default serialization. Only stores Name, NickName, Description and InstanceGuid fields. If you want to store additional fields use WriteFull() instead. |
| Public method | [WriteFull](M_Grasshopper_Kernel_GH_InstanceDescription_WriteFull.htm) | GH\_InstanceDescription does not by default serialize all fields. Use this function to write *all* fields to the archive. This method is compatible with the default Write()/Read() operations. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_InstanceDescription Class](T_Grasshopper_Kernel_GH_InstanceDescription.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)