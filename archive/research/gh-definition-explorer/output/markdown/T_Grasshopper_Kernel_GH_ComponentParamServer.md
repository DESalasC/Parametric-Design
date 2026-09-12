# T_Grasshopper_Kernel_GH_ComponentParamServer

﻿ GH\_ComponentParamServer Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_ComponentParamServer Class](../html/T_Grasshopper_Kernel_GH_ComponentParamServer.htm "GH_ComponentParamServer Class")

[GH\_ComponentParamServer Properties](../html/Properties_T_Grasshopper_Kernel_GH_ComponentParamServer.htm "GH_ComponentParamServer Properties")

[GH\_ComponentParamServer Methods](../html/Methods_T_Grasshopper_Kernel_GH_ComponentParamServer.htm "GH_ComponentParamServer Methods")

[GH\_ComponentParamServer Events](../html/Events_T_Grasshopper_Kernel_GH_ComponentParamServer.htm "GH_ComponentParamServer Events")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ComponentParamServer Class |

Wraps all members and functions needed for GH\_Component to manage its input and output parameters.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LSTF51110E7\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.KernelAddLanguageSpecificTextSet("LSTF51110E7\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_ComponentParamServer

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_ComponentParamServer : GH_ISerializable, 
	IEnumerable<IGH_Param>
```

```
Public Class GH_ComponentParamServer
	Implements GH_ISerializable, IEnumerable(Of IGH_Param)
```

AddLanguageTabSet("ID1EBCA");

The GH\_ComponentParamServer type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Input](P_Grasshopper_Kernel_GH_ComponentParamServer_Input.htm) | Gets or sets the input list of parameters. Do not insert or remove parameters from this list, use the dedicated functions instead. |
| Public property | [InputWidth](P_Grasshopper_Kernel_GH_ComponentParamServer_InputWidth.htm) | Gets the width of the largest input parameter. |
| Public property | [OnlyTreeAndListParameters](P_Grasshopper_Kernel_GH_ComponentParamServer_OnlyTreeAndListParameters.htm) | Returns True if every input parameter is either a list or a tree parameter. |
| Public property | [OnlyTreeParameters](P_Grasshopper_Kernel_GH_ComponentParamServer_OnlyTreeParameters.htm) | Returns True if every input parameter is a tree parameter. |
| Public property | [Output](P_Grasshopper_Kernel_GH_ComponentParamServer_Output.htm) | Gets or sets the output list of parameters. Do not insert or remove parameters from this list, use the dedicated functions instead. |
| Public property | [OutputWidth](P_Grasshopper_Kernel_GH_ComponentParamServer_OutputWidth.htm) | Gets the width of the largest output parameter. |
| Public property | [Owner](P_Grasshopper_Kernel_GH_ComponentParamServer_Owner.htm) | Gets the owner component of this instance |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [AccessCount](M_Grasshopper_Kernel_GH_ComponentParamServer_AccessCount.htm) | Returns the total number of input parameters that match the access mask. |
| Public method | [ClearAddLanguageSpecificTextSet("LSTF51110E7\_2?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_GH_ComponentParamServer_Clear.htm) | Removes all input and output parameters. |
| Public method | [Clear(Boolean)](M_Grasshopper_Kernel_GH_ComponentParamServer_Clear_1.htm) | Removes all input and output parameters. |
| Public methodStatic member | [CreateDuplicate](M_Grasshopper_Kernel_GH_ComponentParamServer_CreateDuplicate.htm) | Attempts to duplicate a parameter. Attributes will be ignored. Warning! The duplicate will have the same ID as the original! |
| Public method | [EmitSyncObject](M_Grasshopper_Kernel_GH_ComponentParamServer_EmitSyncObject.htm) | Create a synch object that stores a shallow representation of this server. Cache this object if you're planning to make sweeping changes to this param-server. Then, once you are finished call the Sync() function to perform cleanup of removed parameters. This is a utility function and you can choose to perform cleanup yourself. |
| Public method | [Find](M_Grasshopper_Kernel_GH_ComponentParamServer_Find.htm) | Find the parameter that has the given InstanceGuid. |
| Public method | [GetEnumerator](M_Grasshopper_Kernel_GH_ComponentParamServer_GetEnumerator.htm) | Gets a customized enumerator which iterates over all (both input and output) parameters. |
| Public method | [GetHashCodeAddLanguageSpecificTextSet("LSTF51110E7\_3?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_GH_ComponentParamServer_GetHashCode.htm) | (Overrides [ObjectAddLanguageSpecificTextSet("LSTF51110E7\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");GetHashCodeAddLanguageSpecificTextSet("LSTF51110E7\_5?cs=()|vb=|cpp=()|nu=()|fs=()");](https://docs.microsoft.com/dotnet/api/system.object.gethashcode#system-object-gethashcode).) |
| Public method | [GetHashCode(GH\_ParamHashFields)](M_Grasshopper_Kernel_GH_ComponentParamServer_GetHashCode_1.htm) | Creates a SHA1 hash from the parameter data. |
| Public method | [IndexOfInputParam(Guid)](M_Grasshopper_Kernel_GH_ComponentParamServer_IndexOfInputParam.htm) | Finds the index of the input parameter that matches the specified search mask. |
| Public method | [IndexOfInputParam(String)](M_Grasshopper_Kernel_GH_ComponentParamServer_IndexOfInputParam_1.htm) | Finds the index of the input parameter that matches the specified search mask. |
| Public method | [IndexOfOutputParam(Guid)](M_Grasshopper_Kernel_GH_ComponentParamServer_IndexOfOutputParam.htm) | Finds the index of the output parameter that matches the specified search mask. |
| Public method | [IndexOfOutputParam(String)](M_Grasshopper_Kernel_GH_ComponentParamServer_IndexOfOutputParam_1.htm) | Finds the index of the output parameter that matches the specified search mask. |
| Public methodStatic member | [InventUniqueNickname(String, IEnumerableAddLanguageSpecificTextSet("LSTF51110E7\_6?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");IGH\_ParamAddLanguageSpecificTextSet("LSTF51110E7\_7?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");)](M_Grasshopper_Kernel_GH_ComponentParamServer_InventUniqueNickname.htm) | Create a new, unique parameter nickname. |
| Public methodStatic member | [InventUniqueNickname(String, IEnumerableAddLanguageSpecificTextSet("LSTF51110E7\_8?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");StringAddLanguageSpecificTextSet("LSTF51110E7\_9?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");)](M_Grasshopper_Kernel_GH_ComponentParamServer_InventUniqueNickname_1.htm) | Create a new, unique parameter nickname. |
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
| Public method | [SortInput(AddLanguageSpecificTextSet("LSTF51110E7\_10?cpp=array&lt;");DoubleAddLanguageSpecificTextSet("LSTF51110E7\_11?cpp=&gt;|cs=[]|vb=()|nu=[]|fs=[]");)](M_Grasshopper_Kernel_GH_ComponentParamServer_SortInput.htm) | Sort the input parameter order based on a numeric key array. |
| Public method | [SortInput(AddLanguageSpecificTextSet("LSTF51110E7\_12?cpp=array&lt;");Int32AddLanguageSpecificTextSet("LSTF51110E7\_13?cpp=&gt;|cs=[]|vb=()|nu=[]|fs=[]");)](M_Grasshopper_Kernel_GH_ComponentParamServer_SortInput_1.htm) | Sort the input parameter order based on a numeric key array. |
| Public method | [SortInput(AddLanguageSpecificTextSet("LSTF51110E7\_14?cpp=array&lt;");SingleAddLanguageSpecificTextSet("LSTF51110E7\_15?cpp=&gt;|cs=[]|vb=()|nu=[]|fs=[]");)](M_Grasshopper_Kernel_GH_ComponentParamServer_SortInput_2.htm) | Sort the input parameter order based on a numeric key array. |
| Public method | [SortOutput(AddLanguageSpecificTextSet("LSTF51110E7\_16?cpp=array&lt;");DoubleAddLanguageSpecificTextSet("LSTF51110E7\_17?cpp=&gt;|cs=[]|vb=()|nu=[]|fs=[]");)](M_Grasshopper_Kernel_GH_ComponentParamServer_SortOutput.htm) | Sort the input parameter order based on a numeric key array. |
| Public method | [SortOutput(AddLanguageSpecificTextSet("LSTF51110E7\_18?cpp=array&lt;");Int32AddLanguageSpecificTextSet("LSTF51110E7\_19?cpp=&gt;|cs=[]|vb=()|nu=[]|fs=[]");)](M_Grasshopper_Kernel_GH_ComponentParamServer_SortOutput_1.htm) | Sort the output parameter order based on a numeric key array. |
| Public method | [SortOutput(AddLanguageSpecificTextSet("LSTF51110E7\_20?cpp=array&lt;");SingleAddLanguageSpecificTextSet("LSTF51110E7\_21?cpp=&gt;|cs=[]|vb=()|nu=[]|fs=[]");)](M_Grasshopper_Kernel_GH_ComponentParamServer_SortOutput_2.htm) | Sort the output parameter order based on a numeric key array. |
| Public method | [Sync(GH\_ComponentParamServerAddLanguageSpecificTextSet("LSTF51110E7\_22?cs=.|vb=.|cpp=::|nu=.|fs=.");IGH\_SyncObject)](M_Grasshopper_Kernel_GH_ComponentParamServer_Sync.htm) | Sync changes from a prerecorded state. All param references in the sync object which are no longer present in the current server will be properly deleted. The sync object will be reset in the process, so you can only call this function with a specific Sync object once. |
| Public method | [Sync(Object)](M_Grasshopper_Kernel_GH_ComponentParamServer_Sync_2.htm) | Sync changes from a prerecorded state. All param references in the sync object which are no longer present in the current server will be properly deleted. The sync object will be reset in the process, so you can only call this function with a specific Sync object once. |
| Public method | [Sync(GH\_ComponentParamServerAddLanguageSpecificTextSet("LSTF51110E7\_23?cs=.|vb=.|cpp=::|nu=.|fs=.");IGH\_SyncObject, Int32AddLanguageSpecificTextSet("LSTF51110E7\_24?cpp=%");)](M_Grasshopper_Kernel_GH_ComponentParamServer_Sync_1.htm) | Sync changes from a prerecorded state. All param references in the sync object which are no longer present in the current server will be properly deleted. The sync object will be reset in the process, so you can only call this function with a specific Sync object once. |
| Public method | [UnregisterInputParameter(IGH\_Param)](M_Grasshopper_Kernel_GH_ComponentParamServer_UnregisterInputParameter.htm) | Removes the specified parameter from this component. |
| Public method | [UnregisterInputParameter(IGH\_Param, Boolean)](M_Grasshopper_Kernel_GH_ComponentParamServer_UnregisterInputParameter_1.htm) | Removes the specified parameter from this component. |
| Public method | [UnregisterOutputParameter(IGH\_Param)](M_Grasshopper_Kernel_GH_ComponentParamServer_UnregisterOutputParameter.htm) | Removes the specified parameter from this component. |
| Public method | [UnregisterOutputParameter(IGH\_Param, Boolean)](M_Grasshopper_Kernel_GH_ComponentParamServer_UnregisterOutputParameter_1.htm) | Removes the specified parameter from this component. |
| Public method | [UnregisterParameter(IGH\_Param)](M_Grasshopper_Kernel_GH_ComponentParamServer_UnregisterParameter.htm) | Removes the specified parameter from this component. |
| Public method | [UnregisterParameter(IGH\_Param, Boolean)](M_Grasshopper_Kernel_GH_ComponentParamServer_UnregisterParameter_1.htm) | Removes the specified parameter from this component. |
| Public method | [Write](M_Grasshopper_Kernel_GH_ComponentParamServer_Write.htm) | Write all parameter data to an IO archive. |
| Public methodStatic member | [WriteParamHashData](M_Grasshopper_Kernel_GH_ComponentParamServer_WriteParamHashData.htm) | Write parameter data to a binary writer. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Events

|  | Name | Description |
| --- | --- | --- |
| Public event | [ParameterChanged](E_Grasshopper_Kernel_GH_ComponentParamServer_ParameterChanged.htm) | Raised whenever there is a change to any parameter. If you only care about NickName or Source changes, handle the ParameterNickNameChanged or ParameterSourcesChanged events instead. |
| Public event | [ParameterNickNameChanged](E_Grasshopper_Kernel_GH_ComponentParamServer_ParameterNickNameChanged.htm) | Raised whenever a parameter nickname change is accepted. |
| Public event | [ParameterSourcesChanged](E_Grasshopper_Kernel_GH_ComponentParamServer_ParameterSourcesChanged.htm) | Raised whenever the source list of an input parameter is changed. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)