# M_Grasshopper_Kernel_GH_ComponentParamServer_Write

﻿ GH\_ComponentParamServer.Write Method 

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
| GH\_ComponentParamServerAddLanguageSpecificTextSet("LSTF9575537\_0?cpp=::|nu=.");Write Method |

Write all parameter data to an IO archive.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public bool Write(
	GH_IWriter writer
)
```

```
Public Function Write ( 
	writer As GH_IWriter
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

writer
:   Type: [GH\_IO.SerializationAddLanguageSpecificTextSet("LSTF9575537\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_IWriter](T_GH_IO_Serialization_GH_IWriter.htm)  
    Object to write with.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True on success, false on failure.

#### Implements

[GH\_ISerializableAddLanguageSpecificTextSet("LSTF9575537\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Write(GH\_IWriter)](M_GH_IO_GH_ISerializable_Write.htm)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_ComponentParamServer Class](T_Grasshopper_Kernel_GH_ComponentParamServer.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)