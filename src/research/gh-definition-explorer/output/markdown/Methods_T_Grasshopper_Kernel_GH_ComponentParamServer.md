# Methods_T_Grasshopper_Kernel_GH_ComponentParamServer

﻿ GH\_ComponentParamServer Methods

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_ComponentParamServer Class](../html/T_Grasshopper_Kernel_GH_ComponentParamServer.htm "GH_ComponentParamServer Class")

[GH\_ComponentParamServer Methods](../html/Methods_T_Grasshopper_Kernel_GH_ComponentParamServer.htm "GH_ComponentParamServer Methods")

[AccessCount Method](../html/M_Grasshopper_Kernel_GH_ComponentParamServer_AccessCount.htm "AccessCount Method ")

[Clear Method](../html/Overload_Grasshopper_Kernel_GH_ComponentParamServer_Clear.htm "Clear Method ")

[CreateDuplicate Method](../html/M_Grasshopper_Kernel_GH_ComponentParamServer_CreateDuplicate.htm "CreateDuplicate Method ")

[EmitSyncObject Method](../html/M_Grasshopper_Kernel_GH_ComponentParamServer_EmitSyncObject.htm "EmitSyncObject Method ")

[Find Method](../html/M_Grasshopper_Kernel_GH_ComponentParamServer_Find.htm "Find Method ")

[GetEnumerator Method](../html/M_Grasshopper_Kernel_GH_ComponentParamServer_GetEnumerator.htm "GetEnumerator Method ")

[GetHashCode Method](../html/Overload_Grasshopper_Kernel_GH_ComponentParamServer_GetHashCode.htm "GetHashCode Method ")

[IndexOfInputParam Method](../html/Overload_Grasshopper_Kernel_GH_ComponentParamServer_IndexOfInputParam.htm "IndexOfInputParam Method ")

[IndexOfOutputParam Method](../html/Overload_Grasshopper_Kernel_GH_ComponentParamServer_IndexOfOutputParam.htm "IndexOfOutputParam Method ")

[InventUniqueNickname Method](../html/Overload_Grasshopper_Kernel_GH_ComponentParamServer_InventUniqueNickname.htm "InventUniqueNickname Method ")

[IsInputParam Method](../html/M_Grasshopper_Kernel_GH_ComponentParamServer_IsInputParam.htm "IsInputParam Method ")

[IsOutputParam Method](../html/M_Grasshopper_Kernel_GH_ComponentParamServer_IsOutputParam.htm "IsOutputParam Method ")

[IsParam Method](../html/M_Grasshopper_Kernel_GH_ComponentParamServer_IsParam.htm "IsParam Method ")

[OnParametersChanged Method](../html/M_Grasshopper_Kernel_GH_ComponentParamServer_OnParametersChanged.htm "OnParametersChanged Method ")

[Read Method](../html/M_Grasshopper_Kernel_GH_ComponentParamServer_Read.htm "Read Method ")

[RegisterInputParam Method](../html/Overload_Grasshopper_Kernel_GH_ComponentParamServer_RegisterInputParam.htm "RegisterInputParam Method ")

[RegisterOutputParam Method](../html/Overload_Grasshopper_Kernel_GH_ComponentParamServer_RegisterOutputParam.htm "RegisterOutputParam Method ")

[RepairParamAssociations Method](../html/M_Grasshopper_Kernel_GH_ComponentParamServer_RepairParamAssociations.htm "RepairParamAssociations Method ")

[RepairProxyParams Method](../html/M_Grasshopper_Kernel_GH_ComponentParamServer_RepairProxyParams.htm "RepairProxyParams Method ")

[SortInput Method](../html/Overload_Grasshopper_Kernel_GH_ComponentParamServer_SortInput.htm "SortInput Method ")

[SortOutput Method](../html/Overload_Grasshopper_Kernel_GH_ComponentParamServer_SortOutput.htm "SortOutput Method ")

[Sync Method](../html/Overload_Grasshopper_Kernel_GH_ComponentParamServer_Sync.htm "Sync Method ")

[UnregisterInputParameter Method](../html/Overload_Grasshopper_Kernel_GH_ComponentParamServer_UnregisterInputParameter.htm "UnregisterInputParameter Method ")

[UnregisterOutputParameter Method](../html/Overload_Grasshopper_Kernel_GH_ComponentParamServer_UnregisterOutputParameter.htm "UnregisterOutputParameter Method ")

[UnregisterParameter Method](../html/Overload_Grasshopper_Kernel_GH_ComponentParamServer_UnregisterParameter.htm "UnregisterParameter Method ")

[Write Method](../html/M_Grasshopper_Kernel_GH_ComponentParamServer_Write.htm "Write Method ")

[WriteParamHashData Method](../html/M_Grasshopper_Kernel_GH_ComponentParamServer_WriteParamHashData.htm "WriteParamHashData Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ComponentParamServer Methods |

The [GH\_ComponentParamServer](T_Grasshopper_Kernel_GH_ComponentParamServer.htm) type exposes the following members.

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [AccessCount](M_Grasshopper_Kernel_GH_ComponentParamServer_AccessCount.htm) | Returns the total number of input parameters that match the access mask. |
| Public method | [ClearAddLanguageSpecificTextSet("LSTDDCB67CF\_0?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_GH_ComponentParamServer_Clear.htm) | Removes all input and output parameters. |
| Public method | [Clear(Boolean)](M_Grasshopper_Kernel_GH_ComponentParamServer_Clear_1.htm) | Removes all input and output parameters. |
| Public methodStatic member | [CreateDuplicate](M_Grasshopper_Kernel_GH_ComponentParamServer_CreateDuplicate.htm) | Attempts to duplicate a parameter. Attributes will be ignored. Warning! The duplicate will have the same ID as the original! |
| Public method | [EmitSyncObject](M_Grasshopper_Kernel_GH_ComponentParamServer_EmitSyncObject.htm) | Create a synch object that stores a shallow representation of this server. Cache this object if you're planning to make sweeping changes to this param-server. Then, once you are finished call the Sync() function to perform cleanup of removed parameters. This is a utility function and you can choose to perform cleanup yourself. |
| Public method | [Find](M_Grasshopper_Kernel_GH_ComponentParamServer_Find.htm) | Find the parameter that has the given InstanceGuid. |
| Public method | [GetEnumerator](M_Grasshopper_Kernel_GH_ComponentParamServer_GetEnumerator.htm) | Gets a customized enumerator which iterates over all (both input and output) parameters. |
| Public method | [GetHashCodeAddLanguageSpecificTextSet("LSTDDCB67CF\_1?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_GH_ComponentParamServer_GetHashCode.htm) | (Overrides [ObjectAddLanguageSpecificTextSet("LSTDDCB67CF\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");GetHashCodeAddLanguageSpecificTextSet("LSTDDCB67CF\_3?cs=()|vb=|cpp=()|nu=()|fs=()");](https://docs.microsoft.com/dotnet/api/system.object.gethashcode#system-object-gethashcode).) |
| Public method | [GetHashCode(GH\_ParamHashFields)](M_Grasshopper_Kernel_GH_ComponentParamServer_GetHashCode_1.htm) | Creates a SHA1 hash from the parameter data. |
| Public method | [IndexOfInputParam(Guid)](M_Grasshopper_Kernel_GH_ComponentParamServer_IndexOfInputParam.htm) | Finds the index of the input parameter that matches the specified search mask. |
| Public method | [IndexOfInputParam(String)](M_Grasshopper_Kernel_GH_ComponentParamServer_IndexOfInputParam_1.htm) | Finds the index of the input parameter that matches the specified search mask. |
| Public method | [IndexOfOutputParam(Guid)](M_Grasshopper_Kernel_GH_ComponentParamServer_IndexOfOutputParam.htm) | Finds the index of the output parameter that matches the specified search mask. |
| Public method | [IndexOfOutputParam(String)](M_Grasshopper_Kernel_GH_ComponentParamServer_IndexOfOutputParam_1.htm) | Finds the index of the output parameter that matches the specified search mask. |
| Public methodStatic member | [InventUniqueNickname(String, IEnumerableAddLanguageSpecificTextSet("LSTDDCB67CF\_4?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");IGH\_ParamAddLanguageSpecificTextSet("LSTDDCB67CF\_5?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");)](M_Grasshopper_Kernel_GH_ComponentParamServer_InventUniqueNickname.htm) | Create a new, unique parameter nickname. |
| Public methodStatic member | [InventUniqueNickname(String, IEnumerableAddLanguageSpecificTextSet("LSTDDCB67CF\_6?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");StringAddLanguageSpecificTextSet("LSTDDCB67CF\_7?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");)](M_Grasshopper_Kernel_GH_ComponentParamServer_InventUniqueNickname_1.htm) | Create a new, unique parameter nickname. |
| Public method | [IsInputParam](M_Grasshopper_Kernel_GH_ComponentParamServer_IsInputParam.htm) | Returns True if this parameter is an input child of the component |
| Public method | [IsOutputParam](M_Grasshopper_Kernel_GH_ComponentParamServer_IsOutputParam.htm) | Returns True if this parameter is an output child of the component |
| Public method | [IsParam](M_Grasshopper_Kernel_GH_ComponentParamServer_IsParam.htm) | Returns True if this parameter is a child of the component |
| Public method | [OnParametersChanged](M_Grasshopper_Kernel_GH_ComponentParamServer_OnParametersChanged.htm) | Call this function when you change input/output parameter lists or types. This function will wipe all caches that are potentially invalid. PerformLayout on the component attributes will be called. |
| Public method | [Read](M_Grasshopper_Kernel_GH_ComponentParamServer_Read.htm) | Read all parameter data from an IO archive. |
| Public method | [RegisterInputParam(IGH\_Param)](M_Grasshopper_Kernel_GH_ComponentParamServer_RegisterInputParam.htm) | Add a parameter to the end of the input list. |
| Public method | [RegisterInputParam(IGH\_Param, Int32)](M_Grasshopper_Kernel_GH_ComponentParamServer_RegisterInputParam_1.htm) | Add a parameter at the specific index of the input list. |
| Public method | [RegisterOutputParam(IGH\_Param)](M_Grasshopper_Kernel_GH_ComponentParamServer_RegisterOutputParam.htm) | Add a parameter to the end of the output list. |
| Public method | [RegisterOutputParam(IGH\_Param, Int32)](M_Grasshopper_Kernel_GH_ComponentParamServer_RegisterOutputParam_1.htm) | Add a parameter at the specific index of the output list. |
| Public method | [RepairParamAssociations](M_Grasshopper_Kernel_GH_ComponentParamServer_RepairParamAssociations.htm) | Makes sure all parameter attributes are a-ok. If you stick to regular functions, you shouldn't have to call this. |
| Public method | [RepairProxyParams](M_Grasshopper_Kernel_GH_ComponentParamServer_RepairProxyParams.htm) | Attempt to fix all proxy params. Returns false if a single one fails. |
| Public method | [SortInput(AddLanguageSpecificTextSet("LSTDDCB67CF\_8?cpp=array&lt;");DoubleAddLanguageSpecificTextSet("LSTDDCB67CF\_9?cpp=&gt;|cs=[]|vb=()|nu=[]|fs=[]");)](M_Grasshopper_Kernel_GH_ComponentParamServer_SortInput.htm) | Sort the input parameter order based on a numeric key array. |
| Public method | [SortInput(AddLanguageSpecificTextSet("LSTDDCB67CF\_10?cpp=array&lt;");Int32AddLanguageSpecificTextSet("LSTDDCB67CF\_11?cpp=&gt;|cs=[]|vb=()|nu=[]|fs=[]");)](M_Grasshopper_Kernel_GH_ComponentParamServer_SortInput_1.htm) | Sort the input parameter order based on a numeric key array. |
| Public method | [SortInput(AddLanguageSpecificTextSet("LSTDDCB67CF\_12?cpp=array&lt;");SingleAddLanguageSpecificTextSet("LSTDDCB67CF\_13?cpp=&gt;|cs=[]|vb=()|nu=[]|fs=[]");)](M_Grasshopper_Kernel_GH_ComponentParamServer_SortInput_2.htm) | Sort the input parameter order based on a numeric key array. |
| Public method | [SortOutput(AddLanguageSpecificTextSet("LSTDDCB67CF\_14?cpp=array&lt;");DoubleAddLanguageSpecificTextSet("LSTDDCB67CF\_15?cpp=&gt;|cs=[]|vb=()|nu=[]|fs=[]");)](M_Grasshopper_Kernel_GH_ComponentParamServer_SortOutput.htm) | Sort the input parameter order based on a numeric key array. |
| Public method | [SortOutput(AddLanguageSpecificTextSet("LSTDDCB67CF\_16?cpp=array&lt;");Int32AddLanguageSpecificTextSet("LSTDDCB67CF\_17?cpp=&gt;|cs=[]|vb=()|nu=[]|fs=[]");)](M_Grasshopper_Kernel_GH_ComponentParamServer_SortOutput_1.htm) | Sort the output parameter order based on a numeric key array. |
| Public method | [SortOutput(AddLanguageSpecificTextSet("LSTDDCB67CF\_18?cpp=array&lt;");SingleAddLanguageSpecificTextSet("LSTDDCB67CF\_19?cpp=&gt;|cs=[]|vb=()|nu=[]|fs=[]");)](M_Grasshopper_Kernel_GH_ComponentParamServer_SortOutput_2.htm) | Sort the output parameter order based on a numeric key array. |
| Public method | [Sync(GH\_ComponentParamServerAddLanguageSpecificTextSet("LSTDDCB67CF\_20?cs=.|vb=.|cpp=::|nu=.|fs=.");IGH\_SyncObject)](M_Grasshopper_Kernel_GH_ComponentParamServer_Sync.htm) | Sync changes from a prerecorded state. All param references in the sync object which are no longer present in the current server will be properly deleted. The sync object will be reset in the process, so you can only call this function with a specific Sync object once. |
| Public method | [Sync(Object)](M_Grasshopper_Kernel_GH_ComponentParamServer_Sync_2.htm) | Sync changes from a prerecorded state. All param references in the sync object which are no longer present in the current server will be properly deleted. The sync object will be reset in the process, so you can only call this function with a specific Sync object once. |
| Public method | [Sync(GH\_ComponentParamServerAddLanguageSpecificTextSet("LSTDDCB67CF\_21?cs=.|vb=.|cpp=::|nu=.|fs=.");IGH\_SyncObject, Int32AddLanguageSpecificTextSet("LSTDDCB67CF\_22?cpp=%");)](M_Grasshopper_Kernel_GH_ComponentParamServer_Sync_1.htm) | Sync changes from a prerecorded state. All param references in the sync object which are no longer present in the current server will be properly deleted. The sync object will be reset in the process, so you can only call this function with a specific Sync object once. |
| Public method | [UnregisterInputParameter(IGH\_Param)](M_Grasshopper_Kernel_GH_ComponentParamServer_UnregisterInputParameter.htm) | Removes the specified parameter from this component. |
| Public method | [UnregisterInputParameter(IGH\_Param, Boolean)](M_Grasshopper_Kernel_GH_ComponentParamServer_UnregisterInputParameter_1.htm) | Removes the specified parameter from this component. |
| Public method | [UnregisterOutputParameter(IGH\_Param)](M_Grasshopper_Kernel_GH_ComponentParamServer_UnregisterOutputParameter.htm) | Removes the specified parameter from this component. |
| Public method | [UnregisterOutputParameter(IGH\_Param, Boolean)](M_Grasshopper_Kernel_GH_ComponentParamServer_UnregisterOutputParameter_1.htm) | Removes the specified parameter from this component. |
| Public method | [UnregisterParameter(IGH\_Param)](M_Grasshopper_Kernel_GH_ComponentParamServer_UnregisterParameter.htm) | Removes the specified parameter from this component. |
| Public method | [UnregisterParameter(IGH\_Param, Boolean)](M_Grasshopper_Kernel_GH_ComponentParamServer_UnregisterParameter_1.htm) | Removes the specified parameter from this component. |
| Public method | [Write](M_Grasshopper_Kernel_GH_ComponentParamServer_Write.htm) | Write all parameter data to an IO archive. |
| Public methodStatic member | [WriteParamHashData](M_Grasshopper_Kernel_GH_ComponentParamServer_WriteParamHashData.htm) | Write parameter data to a binary writer. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_ComponentParamServer Class](T_Grasshopper_Kernel_GH_ComponentParamServer.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)