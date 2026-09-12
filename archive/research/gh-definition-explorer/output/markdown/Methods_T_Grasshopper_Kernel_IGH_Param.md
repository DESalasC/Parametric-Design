# Methods_T_Grasshopper_Kernel_IGH_Param

﻿ IGH\_Param Methods

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH\_Param Interface](../html/T_Grasshopper_Kernel_IGH_Param.htm "IGH_Param Interface")

[IGH\_Param Methods](../html/Methods_T_Grasshopper_Kernel_IGH_Param.htm "IGH_Param Methods")

[AddSource Method](../html/Overload_Grasshopper_Kernel_IGH_Param_AddSource.htm "AddSource Method ")

[AddVolatileData Method](../html/M_Grasshopper_Kernel_IGH_Param_AddVolatileData.htm "AddVolatileData Method ")

[AddVolatileDataList Method](../html/M_Grasshopper_Kernel_IGH_Param_AddVolatileDataList.htm "AddVolatileDataList Method ")

[AddVolatileDataTree Method](../html/M_Grasshopper_Kernel_IGH_Param_AddVolatileDataTree.htm "AddVolatileDataTree Method ")

[ClearProxySources Method](../html/M_Grasshopper_Kernel_IGH_Param_ClearProxySources.htm "ClearProxySources Method ")

[CreateProxySources Method](../html/M_Grasshopper_Kernel_IGH_Param_CreateProxySources.htm "CreateProxySources Method ")

[RelinkProxySources Method](../html/M_Grasshopper_Kernel_IGH_Param_RelinkProxySources.htm "RelinkProxySources Method ")

[RemoveAllSources Method](../html/M_Grasshopper_Kernel_IGH_Param_RemoveAllSources.htm "RemoveAllSources Method ")

[RemoveEffects Method](../html/M_Grasshopper_Kernel_IGH_Param_RemoveEffects.htm "RemoveEffects Method ")

[RemoveSource Method](../html/Overload_Grasshopper_Kernel_IGH_Param_RemoveSource.htm "RemoveSource Method ")

[ReplaceSource Method](../html/Overload_Grasshopper_Kernel_IGH_Param_ReplaceSource.htm "ReplaceSource Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_Param Methods |

The [IGH\_Param](T_Grasshopper_Kernel_IGH_Param.htm) type exposes the following members.

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [AddRuntimeMessage](M_Grasshopper_Kernel_IGH_ActiveObject_AddRuntimeMessage.htm) | Add a new message to this object. Valid message type flags are Warning and Error. If the Message string is empty or zero-length no message is added. (Inherited from [IGH\_ActiveObject](T_Grasshopper_Kernel_IGH_ActiveObject.htm).) |
| Public method | [AddSource(IGH\_Param)](M_Grasshopper_Kernel_IGH_Param_AddSource.htm) | Append a new Source parameter to the end of the Sources list. Sources provide this parameter with data at runtime. |
| Public method | [AddSource(IGH\_Param, Int32)](M_Grasshopper_Kernel_IGH_Param_AddSource_1.htm) | Insert a new Source parameter into the Sources list. Sources provide this parameter with data at runtime. |
| Public method | [AddVolatileData](M_Grasshopper_Kernel_IGH_Param_AddVolatileData.htm) | Inserts an item of volatile data into the data structure. |
| Public method | [AddVolatileDataList](M_Grasshopper_Kernel_IGH_Param_AddVolatileDataList.htm) | Inserts a list of items into the data structure. |
| Public method | [AddVolatileDataTree](M_Grasshopper_Kernel_IGH_Param_AddVolatileDataTree.htm) | Insert an entire data tree into this parameter. |
| Public method | [ClearData](M_Grasshopper_Kernel_IGH_ActiveObject_ClearData.htm) | This function is called whenever the object needs to clear all solution data. This usually amounts to wiping volatile caches and messages. This function will not affect any other objects, but it will set the Phase flag to Blank (Inherited from [IGH\_ActiveObject](T_Grasshopper_Kernel_IGH_ActiveObject.htm).) |
| Public method | [ClearProxySources](M_Grasshopper_Kernel_IGH_Param_ClearProxySources.htm) | Remove all proxy sources without attempting to relink them. |
| Public method | [ClearRuntimeMessages](M_Grasshopper_Kernel_IGH_ActiveObject_ClearRuntimeMessages.htm) | Clear all message lists. (Inherited from [IGH\_ActiveObject](T_Grasshopper_Kernel_IGH_ActiveObject.htm).) |
| Public method | [CollectData](M_Grasshopper_Kernel_IGH_ActiveObject_CollectData.htm) | This function is called whenever the object is required to collect all data. Either from Persistent records, from source params or whatever. This step is only performed if the phase flag is Blank or Failed. Upon completion, the phase flag will be set to Collected (Inherited from [IGH\_ActiveObject](T_Grasshopper_Kernel_IGH_ActiveObject.htm).) |
| Public method | [ComputeData](M_Grasshopper_Kernel_IGH_ActiveObject_ComputeData.htm) | This function is called whenever the object is required to generate new data. This step is only performed by some objects and only when the Phase flag is Collected. Upon completion, the Phase will be Computed. If this object throws exceptions, it is the responsibility of the caller to set the Phase flag to Failed. (Inherited from [IGH\_ActiveObject](T_Grasshopper_Kernel_IGH_ActiveObject.htm).) |
| Public method | [CreateProxySources](M_Grasshopper_Kernel_IGH_Param_CreateProxySources.htm) | Convert all proper source parameters into proxy sources. |
| Public method | [DependsOn](M_Grasshopper_Kernel_IGH_ActiveObject_DependsOn.htm) | Solve the inheritance relationship between this object and a potential parental object. (Inherited from [IGH\_ActiveObject](T_Grasshopper_Kernel_IGH_ActiveObject.htm).) |
| Public method | [RegisterRemoteIDs](M_Grasshopper_Kernel_IGH_ActiveObject_RegisterRemoteIDs.htm) | If this object depends on Rhino Objects, you must register the UUIDs of those objects. Failure to do so will result in faulty event handling. (Inherited from [IGH\_ActiveObject](T_Grasshopper_Kernel_IGH_ActiveObject.htm).) |
| Public method | [RelinkProxySources](M_Grasshopper_Kernel_IGH_Param_RelinkProxySources.htm) | Attempt to replace all proxy sources with real sources. Proxy sources are used during file IO, when actual sources might not be available yet. Once an IO operation has been completed there should be no more proxy sources. |
| Public method | [RemoveAllSources](M_Grasshopper_Kernel_IGH_Param_RemoveAllSources.htm) | Remove all sources from this parameter. |
| Public method | [RemoveEffects](M_Grasshopper_Kernel_IGH_Param_RemoveEffects.htm) | Remove all post-process effects. |
| Public method | [RemoveSource(Guid)](M_Grasshopper_Kernel_IGH_Param_RemoveSource_1.htm) | Remove the specified source from this parameter. |
| Public method | [RemoveSource(IGH\_Param)](M_Grasshopper_Kernel_IGH_Param_RemoveSource.htm) | Remove the specified source from this parameter. |
| Public method | [ReplaceSource(Guid, IGH\_Param)](M_Grasshopper_Kernel_IGH_Param_ReplaceSource_1.htm) | Replace an existing source with a new one. If the old\_source does not exist in this parameter, nothing happens. |
| Public method | [ReplaceSource(IGH\_Param, IGH\_Param)](M_Grasshopper_Kernel_IGH_Param_ReplaceSource.htm) | Replace an existing source with a new one. If the old\_source does not exist in this parameter, nothing happens. |
| Public method | [RuntimeMessages](M_Grasshopper_Kernel_IGH_ActiveObject_RuntimeMessages.htm) | Gets the list of cached runtime messages that were recorded during solver-time processes. (Inherited from [IGH\_ActiveObject](T_Grasshopper_Kernel_IGH_ActiveObject.htm).) |
| Public method | [SDKCompliancy](M_Grasshopper_Kernel_IGH_ActiveObject_SDKCompliancy.htm) | Test whether this object is compliant with a given Rhino version. (Inherited from [IGH\_ActiveObject](T_Grasshopper_Kernel_IGH_ActiveObject.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[IGH\_Param Interface](T_Grasshopper_Kernel_IGH_Param.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)