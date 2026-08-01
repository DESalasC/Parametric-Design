# Properties_T_Grasshopper_Kernel_IGH_Param

﻿ IGH\_Param Properties

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH\_Param Interface](../html/T_Grasshopper_Kernel_IGH_Param.htm "IGH_Param Interface")

[IGH\_Param Properties](../html/Properties_T_Grasshopper_Kernel_IGH_Param.htm "IGH_Param Properties")

[Access Property](../html/P_Grasshopper_Kernel_IGH_Param_Access.htm "Access Property ")

[DataMapping Property](../html/P_Grasshopper_Kernel_IGH_Param_DataMapping.htm "DataMapping Property ")

[DataType Property](../html/P_Grasshopper_Kernel_IGH_Param_DataType.htm "DataType Property ")

[HasProxySources Property](../html/P_Grasshopper_Kernel_IGH_Param_HasProxySources.htm "HasProxySources Property ")

[Kind Property](../html/P_Grasshopper_Kernel_IGH_Param_Kind.htm "Kind Property ")

[Optional Property](../html/P_Grasshopper_Kernel_IGH_Param_Optional.htm "Optional Property ")

[ProxySourceCount Property](../html/P_Grasshopper_Kernel_IGH_Param_ProxySourceCount.htm "ProxySourceCount Property ")

[Recipients Property](../html/P_Grasshopper_Kernel_IGH_Param_Recipients.htm "Recipients Property ")

[Reverse Property](../html/P_Grasshopper_Kernel_IGH_Param_Reverse.htm "Reverse Property ")

[Simplify Property](../html/P_Grasshopper_Kernel_IGH_Param_Simplify.htm "Simplify Property ")

[SourceCount Property](../html/P_Grasshopper_Kernel_IGH_Param_SourceCount.htm "SourceCount Property ")

[Sources Property](../html/P_Grasshopper_Kernel_IGH_Param_Sources.htm "Sources Property ")

[StateTags Property](../html/P_Grasshopper_Kernel_IGH_Param_StateTags.htm "StateTags Property ")

[Type Property](../html/P_Grasshopper_Kernel_IGH_Param_Type.htm "Type Property ")

[TypeName Property](../html/P_Grasshopper_Kernel_IGH_Param_TypeName.htm "TypeName Property ")

[VolatileData Property](../html/P_Grasshopper_Kernel_IGH_Param_VolatileData.htm "VolatileData Property ")

[VolatileDataCount Property](../html/P_Grasshopper_Kernel_IGH_Param_VolatileDataCount.htm "VolatileDataCount Property ")

[WireDisplay Property](../html/P_Grasshopper_Kernel_IGH_Param_WireDisplay.htm "WireDisplay Property ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_Param Properties |

The [IGH\_Param](T_Grasshopper_Kernel_IGH_Param.htm) type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Access](P_Grasshopper_Kernel_IGH_Param_Access.htm) | Gets or sets the Access level for this parameter. |
| Public property | [DataMapping](P_Grasshopper_Kernel_IGH_Param_DataMapping.htm) | Gets or sets the data mapping of this Parameter. |
| Public property | [DataType](P_Grasshopper_Kernel_IGH_Param_DataType.htm) | Gets the type of the current data state. |
| Public property | [HasProxySources](P_Grasshopper_Kernel_IGH_Param_HasProxySources.htm) | Gets a value indicating whether or not this parameter maintains proxy sources. Proxy sources are used during file IO, when actual sources might not be available yet. Once an IO operation has been completed there should be no more proxy sources. |
| Public property | [IsDataProvider](P_Grasshopper_Kernel_IGH_ActiveObject_IsDataProvider.htm) | Gets whether or not this object is capable of emitting data. (Inherited from [IGH\_ActiveObject](T_Grasshopper_Kernel_IGH_ActiveObject.htm).) |
| Public property | [Kind](P_Grasshopper_Kernel_IGH_Param_Kind.htm) | Gets the parameter kind. The kind is evaluated lazily and cached. |
| Public property | [Locked](P_Grasshopper_Kernel_IGH_ActiveObject_Locked.htm) | Gets or sets the locked flag of this object. Locked objects are ignored during solutions. (Inherited from [IGH\_ActiveObject](T_Grasshopper_Kernel_IGH_ActiveObject.htm).) |
| Public property | [MutableNickName](P_Grasshopper_Kernel_IGH_ActiveObject_MutableNickName.htm) | Gets or sets a value that enables Nick name changes through the menu. The default is TRUE. (Inherited from [IGH\_ActiveObject](T_Grasshopper_Kernel_IGH_ActiveObject.htm).) |
| Public property | [Optional](P_Grasshopper_Kernel_IGH_Param_Optional.htm) | Gets or sets whether or not this parameter is considered optional by the owner component. Empty, non-optional parameters prevent the component from being solved. |
| Public property | [Phase](P_Grasshopper_Kernel_IGH_ActiveObject_Phase.htm) | Gets the solution phase in which this object is currently stuck. (Inherited from [IGH\_ActiveObject](T_Grasshopper_Kernel_IGH_ActiveObject.htm).) |
| Public property | [ProcessorTime](P_Grasshopper_Kernel_IGH_ActiveObject_ProcessorTime.htm) | Gets the most recent measured processor time. (Inherited from [IGH\_ActiveObject](T_Grasshopper_Kernel_IGH_ActiveObject.htm).) |
| Public property | [ProxySourceCount](P_Grasshopper_Kernel_IGH_Param_ProxySourceCount.htm) | Gets the number of proxy sources for this parameter. Proxy sources are used during file IO, when actual sources might not be available yet. Once an IO operation has been completed there should be no more proxy sources. |
| Public property | [Recipients](P_Grasshopper_Kernel_IGH_Param_Recipients.htm) | Gets a list of all the recipients of this parameter. I.e. a recipient has this parameter as one of the sources. The Recipient list is maintained by the parameter, do not modify it yourself. |
| Public property | [Reverse](P_Grasshopper_Kernel_IGH_Param_Reverse.htm) | Gets or sets the data reverse modifier of this parameter. |
| Public property | [RuntimeMessageLevel](P_Grasshopper_Kernel_IGH_ActiveObject_RuntimeMessageLevel.htm) | Gets the worst-case level of all messages. I.e. if only warnings have been recorded, the level will be ::warning. If even a single error exists, the level will be ::error. (Inherited from [IGH\_ActiveObject](T_Grasshopper_Kernel_IGH_ActiveObject.htm).) |
| Public property | [Simplify](P_Grasshopper_Kernel_IGH_Param_Simplify.htm) | Gets or sets the simplify modifier for this parameter. |
| Public property | [SourceCount](P_Grasshopper_Kernel_IGH_Param_SourceCount.htm) | Gets the number of sources for this parameter. |
| Public property | [Sources](P_Grasshopper_Kernel_IGH_Param_Sources.htm) | Gets a list of source parameters. Do not modify this list, if you wish to add or remove sources, use dedicated functions like AddSource() and RemoveSource instead. |
| Public property | [StateTags](P_Grasshopper_Kernel_IGH_Param_StateTags.htm) | Gets all the StateTags that are associated with this parameter. A state tag is a visual feedback icon that represents specific internal settings. |
| Public property | [Type](P_Grasshopper_Kernel_IGH_Param_Type.htm) | Gets the Framework Type descriptor for the stored Data. |
| Public property | [TypeName](P_Grasshopper_Kernel_IGH_Param_TypeName.htm) | Gets a human readable description of the data stored in this parameter. |
| Public property | [VolatileData](P_Grasshopper_Kernel_IGH_Param_VolatileData.htm) | Gets the instance of the volatile data tree stored in this parameter. |
| Public property | [VolatileDataCount](P_Grasshopper_Kernel_IGH_Param_VolatileDataCount.htm) | Gets the total number of volatile data items stored in this parameter. |
| Public property | [WireDisplay](P_Grasshopper_Kernel_IGH_Param_WireDisplay.htm) | Gets or sets the wire display style for this parameter. Wire display only affects the wires connected to the parameter input. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[IGH\_Param Interface](T_Grasshopper_Kernel_IGH_Param.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)