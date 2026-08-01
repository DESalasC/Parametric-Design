# Properties_T_Grasshopper_Kernel_IGH_ActiveObject

﻿ IGH\_ActiveObject Properties

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH\_ActiveObject Interface](../html/T_Grasshopper_Kernel_IGH_ActiveObject.htm "IGH_ActiveObject Interface")

[IGH\_ActiveObject Properties](../html/Properties_T_Grasshopper_Kernel_IGH_ActiveObject.htm "IGH_ActiveObject Properties")

[IsDataProvider Property](../html/P_Grasshopper_Kernel_IGH_ActiveObject_IsDataProvider.htm "IsDataProvider Property ")

[Locked Property](../html/P_Grasshopper_Kernel_IGH_ActiveObject_Locked.htm "Locked Property ")

[MutableNickName Property](../html/P_Grasshopper_Kernel_IGH_ActiveObject_MutableNickName.htm "MutableNickName Property ")

[Phase Property](../html/P_Grasshopper_Kernel_IGH_ActiveObject_Phase.htm "Phase Property ")

[ProcessorTime Property](../html/P_Grasshopper_Kernel_IGH_ActiveObject_ProcessorTime.htm "ProcessorTime Property ")

[RuntimeMessageLevel Property](../html/P_Grasshopper_Kernel_IGH_ActiveObject_RuntimeMessageLevel.htm "RuntimeMessageLevel Property ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_ActiveObject Properties |

The [IGH\_ActiveObject](T_Grasshopper_Kernel_IGH_ActiveObject.htm) type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Attributes](P_Grasshopper_Kernel_IGH_DocumentObject_Attributes.htm) | Gets or sets the attributes that are associated with this object. Only set custom attributes if you know what you are doing. (Inherited from [IGH\_DocumentObject](T_Grasshopper_Kernel_IGH_DocumentObject.htm).) |
| Public property | [ComponentGuid](P_Grasshopper_Kernel_IGH_DocumentObject_ComponentGuid.htm) | Returns a consistent ID for this object type. Every object must supply a unique and unchanging ID that is used to identify objects of the same type. (Inherited from [IGH\_DocumentObject](T_Grasshopper_Kernel_IGH_DocumentObject.htm).) |
| Public property | [Exposure](P_Grasshopper_Kernel_IGH_DocumentObject_Exposure.htm) | Gets the exposure of this object in the Graphical User Interface. (Inherited from [IGH\_DocumentObject](T_Grasshopper_Kernel_IGH_DocumentObject.htm).) |
| Public property | [Icon\_24x24](P_Grasshopper_Kernel_IGH_DocumentObject_Icon_24x24.htm) | The icon associated with this object. (Inherited from [IGH\_DocumentObject](T_Grasshopper_Kernel_IGH_DocumentObject.htm).) |
| Public property | [Icon\_24x24\_Locked](P_Grasshopper_Kernel_IGH_DocumentObject_Icon_24x24_Locked.htm) | The greyscale icon of this object. (Inherited from [IGH\_DocumentObject](T_Grasshopper_Kernel_IGH_DocumentObject.htm).) |
| Public property | [IconDisplayMode](P_Grasshopper_Kernel_IGH_DocumentObject_IconDisplayMode.htm) | Gets the current display mode of the object. (Inherited from [IGH\_DocumentObject](T_Grasshopper_Kernel_IGH_DocumentObject.htm).) |
| Public property | [IsDataProvider](P_Grasshopper_Kernel_IGH_ActiveObject_IsDataProvider.htm) | Gets whether or not this object is capable of emitting data. |
| Public property | [Locked](P_Grasshopper_Kernel_IGH_ActiveObject_Locked.htm) | Gets or sets the locked flag of this object. Locked objects are ignored during solutions. |
| Public property | [MutableNickName](P_Grasshopper_Kernel_IGH_ActiveObject_MutableNickName.htm) | Gets or sets a value that enables Nick name changes through the menu. The default is TRUE. |
| Public property | [Obsolete](P_Grasshopper_Kernel_IGH_DocumentObject_Obsolete.htm) | Gets whether this object is Obsolete. (Inherited from [IGH\_DocumentObject](T_Grasshopper_Kernel_IGH_DocumentObject.htm).) |
| Public property | [Phase](P_Grasshopper_Kernel_IGH_ActiveObject_Phase.htm) | Gets the solution phase in which this object is currently stuck. |
| Public property | [ProcessorTime](P_Grasshopper_Kernel_IGH_ActiveObject_ProcessorTime.htm) | Gets the most recent measured processor time. |
| Public property | [RuntimeMessageLevel](P_Grasshopper_Kernel_IGH_ActiveObject_RuntimeMessageLevel.htm) | Gets the worst-case level of all messages. I.e. if only warnings have been recorded, the level will be ::warning. If even a single error exists, the level will be ::error. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[IGH\_ActiveObject Interface](T_Grasshopper_Kernel_IGH_ActiveObject.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)