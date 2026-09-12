# Properties_T_Grasshopper_Kernel_IGH_Component

﻿ IGH\_Component Properties

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH\_Component Interface](../html/T_Grasshopper_Kernel_IGH_Component.htm "IGH_Component Interface")

[IGH\_Component Properties](../html/Properties_T_Grasshopper_Kernel_IGH_Component.htm "IGH_Component Properties")

[InConstructor Property](../html/P_Grasshopper_Kernel_IGH_Component_InConstructor.htm "InConstructor Property ")

[IsValidMasterParameterIndex Property](../html/P_Grasshopper_Kernel_IGH_Component_IsValidMasterParameterIndex.htm "IsValidMasterParameterIndex Property ")

[MasterParameterIndex Property](../html/P_Grasshopper_Kernel_IGH_Component_MasterParameterIndex.htm "MasterParameterIndex Property ")

[Message Property](../html/P_Grasshopper_Kernel_IGH_Component_Message.htm "Message Property ")

[Params Property](../html/P_Grasshopper_Kernel_IGH_Component_Params.htm "Params Property ")

[RunCount Property](../html/P_Grasshopper_Kernel_IGH_Component_RunCount.htm "RunCount Property ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_Component Properties |

The [IGH\_Component](T_Grasshopper_Kernel_IGH_Component.htm) type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [ClippingBox](P_Grasshopper_Kernel_IGH_PreviewObject_ClippingBox.htm) | Gets the clipping box for this object. The clipping box is typically the union of the boundingboxes of all the geometry that is drawn by this object. (Inherited from [IGH\_PreviewObject](T_Grasshopper_Kernel_IGH_PreviewObject.htm).) |
| Public property | [Hidden](P_Grasshopper_Kernel_IGH_PreviewObject_Hidden.htm) | Gets or sets a value indicating whether or not this object is currently drawing preview flags. (Inherited from [IGH\_PreviewObject](T_Grasshopper_Kernel_IGH_PreviewObject.htm).) |
| Public property | [InConstructor](P_Grasshopper_Kernel_IGH_Component_InConstructor.htm) | Gets the constructor flag for this instance. If InConstructor = True, it means the component is still registering parameters and the layout is not yet complete. |
| Public property | [IsBakeCapable](P_Grasshopper_Kernel_IGH_BakeAwareObject_IsBakeCapable.htm) | Gets a value indicating whether or not the object can potentially Bake data in its current state. (Inherited from [IGH\_BakeAwareObject](T_Grasshopper_Kernel_IGH_BakeAwareObject.htm).) |
| Public property | [IsDataProvider](P_Grasshopper_Kernel_IGH_ActiveObject_IsDataProvider.htm) | Gets whether or not this object is capable of emitting data. (Inherited from [IGH\_ActiveObject](T_Grasshopper_Kernel_IGH_ActiveObject.htm).) |
| Public property | [IsPreviewCapable](P_Grasshopper_Kernel_IGH_PreviewObject_IsPreviewCapable.htm) | Gets a value indicating whether or not this object (in its current state) can draw geometric previews at all. (Inherited from [IGH\_PreviewObject](T_Grasshopper_Kernel_IGH_PreviewObject.htm).) |
| Public property | [IsValidMasterParameterIndex](P_Grasshopper_Kernel_IGH_Component_IsValidMasterParameterIndex.htm) | Gets whether the MasterParameterIndex property identifies a valid parameter. |
| Public property | [Locked](P_Grasshopper_Kernel_IGH_ActiveObject_Locked.htm) | Gets or sets the locked flag of this object. Locked objects are ignored during solutions. (Inherited from [IGH\_ActiveObject](T_Grasshopper_Kernel_IGH_ActiveObject.htm).) |
| Public property | [MasterParameterIndex](P_Grasshopper_Kernel_IGH_Component_MasterParameterIndex.htm) | Gets or sets the master parameter index override. Negative indices or indices larger than or equal to the input parameter count will be ignored and regular master parameter detection will kick in. |
| Public property | [Message](P_Grasshopper_Kernel_IGH_Component_Message.htm) | Gets or sets a custom message to be displayed underneath the component. |
| Public property | [MutableNickName](P_Grasshopper_Kernel_IGH_ActiveObject_MutableNickName.htm) | Gets or sets a value that enables Nick name changes through the menu. The default is TRUE. (Inherited from [IGH\_ActiveObject](T_Grasshopper_Kernel_IGH_ActiveObject.htm).) |
| Public property | [Params](P_Grasshopper_Kernel_IGH_Component_Params.htm) | Gets the Params object that managed input and output parameters. |
| Public property | [Phase](P_Grasshopper_Kernel_IGH_ActiveObject_Phase.htm) | Gets the solution phase in which this object is currently stuck. (Inherited from [IGH\_ActiveObject](T_Grasshopper_Kernel_IGH_ActiveObject.htm).) |
| Public property | [ProcessorTime](P_Grasshopper_Kernel_IGH_ActiveObject_ProcessorTime.htm) | Gets the most recent measured processor time. (Inherited from [IGH\_ActiveObject](T_Grasshopper_Kernel_IGH_ActiveObject.htm).) |
| Public property | [RunCount](P_Grasshopper_Kernel_IGH_Component_RunCount.htm) | Gets a value indicating how many times the SolveInstance method was called on this component during the last solution. This property will return -1 if no valid runcount is available. |
| Public property | [RuntimeMessageLevel](P_Grasshopper_Kernel_IGH_ActiveObject_RuntimeMessageLevel.htm) | Gets the worst-case level of all messages. I.e. if only warnings have been recorded, the level will be ::warning. If even a single error exists, the level will be ::error. (Inherited from [IGH\_ActiveObject](T_Grasshopper_Kernel_IGH_ActiveObject.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[IGH\_Component Interface](T_Grasshopper_Kernel_IGH_Component.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)