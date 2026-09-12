# Methods_T_Grasshopper_Kernel_IGH_Component

﻿ IGH\_Component Methods

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH\_Component Interface](../html/T_Grasshopper_Kernel_IGH_Component.htm "IGH_Component Interface")

[IGH\_Component Properties](../html/Properties_T_Grasshopper_Kernel_IGH_Component.htm "IGH_Component Properties")

[IGH\_Component Methods](../html/Methods_T_Grasshopper_Kernel_IGH_Component.htm "IGH_Component Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_Component Methods |

The [IGH\_Component](T_Grasshopper_Kernel_IGH_Component.htm) type exposes the following members.

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [AddRuntimeMessage](M_Grasshopper_Kernel_IGH_ActiveObject_AddRuntimeMessage.htm) | Add a new message to this object. Valid message type flags are Warning and Error. If the Message string is empty or zero-length no message is added. (Inherited from [IGH\_ActiveObject](T_Grasshopper_Kernel_IGH_ActiveObject.htm).) |
| Public method | [BakeGeometry(RhinoDoc, ListAddLanguageSpecificTextSet("LST52A755D7\_0?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");GuidAddLanguageSpecificTextSet("LST52A755D7\_1?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");)](M_Grasshopper_Kernel_IGH_BakeAwareObject_BakeGeometry_1.htm) | Bake all the goemetry in this object in the given Rhino document. (Inherited from [IGH\_BakeAwareObject](T_Grasshopper_Kernel_IGH_BakeAwareObject.htm).) |
| Public method | [BakeGeometry(RhinoDoc, ObjectAttributes, ListAddLanguageSpecificTextSet("LST52A755D7\_2?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");GuidAddLanguageSpecificTextSet("LST52A755D7\_3?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");)](M_Grasshopper_Kernel_IGH_BakeAwareObject_BakeGeometry.htm) | Bake all the goemetry in this object in the given Rhino document. (Inherited from [IGH\_BakeAwareObject](T_Grasshopper_Kernel_IGH_BakeAwareObject.htm).) |
| Public method | [ClearData](M_Grasshopper_Kernel_IGH_ActiveObject_ClearData.htm) | This function is called whenever the object needs to clear all solution data. This usually amounts to wiping volatile caches and messages. This function will not affect any other objects, but it will set the Phase flag to Blank (Inherited from [IGH\_ActiveObject](T_Grasshopper_Kernel_IGH_ActiveObject.htm).) |
| Public method | [ClearRuntimeMessages](M_Grasshopper_Kernel_IGH_ActiveObject_ClearRuntimeMessages.htm) | Clear all message lists. (Inherited from [IGH\_ActiveObject](T_Grasshopper_Kernel_IGH_ActiveObject.htm).) |
| Public method | [CollectData](M_Grasshopper_Kernel_IGH_ActiveObject_CollectData.htm) | This function is called whenever the object is required to collect all data. Either from Persistent records, from source params or whatever. This step is only performed if the phase flag is Blank or Failed. Upon completion, the phase flag will be set to Collected (Inherited from [IGH\_ActiveObject](T_Grasshopper_Kernel_IGH_ActiveObject.htm).) |
| Public method | [ComputeData](M_Grasshopper_Kernel_IGH_ActiveObject_ComputeData.htm) | This function is called whenever the object is required to generate new data. This step is only performed by some objects and only when the Phase flag is Collected. Upon completion, the Phase will be Computed. If this object throws exceptions, it is the responsibility of the caller to set the Phase flag to Failed. (Inherited from [IGH\_ActiveObject](T_Grasshopper_Kernel_IGH_ActiveObject.htm).) |
| Public method | [DependsOn](M_Grasshopper_Kernel_IGH_ActiveObject_DependsOn.htm) | Solve the inheritance relationship between this object and a potential parental object. (Inherited from [IGH\_ActiveObject](T_Grasshopper_Kernel_IGH_ActiveObject.htm).) |
| Public method | [DrawViewportMeshes](M_Grasshopper_Kernel_IGH_PreviewObject_DrawViewportMeshes.htm) | Implement this function to draw all shaded meshes. If the viewport does not support shading, this function will not be called. (Inherited from [IGH\_PreviewObject](T_Grasshopper_Kernel_IGH_PreviewObject.htm).) |
| Public method | [DrawViewportWires](M_Grasshopper_Kernel_IGH_PreviewObject_DrawViewportWires.htm) | Implement this function to draw all wire and point geometry previews. (Inherited from [IGH\_PreviewObject](T_Grasshopper_Kernel_IGH_PreviewObject.htm).) |
| Public method | [RegisterRemoteIDs](M_Grasshopper_Kernel_IGH_ActiveObject_RegisterRemoteIDs.htm) | If this object depends on Rhino Objects, you must register the UUIDs of those objects. Failure to do so will result in faulty event handling. (Inherited from [IGH\_ActiveObject](T_Grasshopper_Kernel_IGH_ActiveObject.htm).) |
| Public method | [RuntimeMessages](M_Grasshopper_Kernel_IGH_ActiveObject_RuntimeMessages.htm) | Gets the list of cached runtime messages that were recorded during solver-time processes. (Inherited from [IGH\_ActiveObject](T_Grasshopper_Kernel_IGH_ActiveObject.htm).) |
| Public method | [SDKCompliancy](M_Grasshopper_Kernel_IGH_ActiveObject_SDKCompliancy.htm) | Test whether this object is compliant with a given Rhino version. (Inherited from [IGH\_ActiveObject](T_Grasshopper_Kernel_IGH_ActiveObject.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[IGH\_Component Interface](T_Grasshopper_Kernel_IGH_Component.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)