# M_Grasshopper_Kernel_GH_ComponentParamServer_GetHashCode_1

﻿ GH\_ComponentParamServer.GetHashCode Method (GH\_ParamHashFields)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_ComponentParamServer Class](../html/T_Grasshopper_Kernel_GH_ComponentParamServer.htm "GH_ComponentParamServer Class")

[GH\_ComponentParamServer Methods](../html/Methods_T_Grasshopper_Kernel_GH_ComponentParamServer.htm "GH_ComponentParamServer Methods")

[GetHashCode Method](../html/Overload_Grasshopper_Kernel_GH_ComponentParamServer_GetHashCode.htm "GetHashCode Method ")

[GetHashCode Method](../html/M_Grasshopper_Kernel_GH_ComponentParamServer_GetHashCode.htm "GetHashCode Method ")

[GetHashCode Method (GH\_ParamHashFields)](../html/M_Grasshopper_Kernel_GH_ComponentParamServer_GetHashCode_1.htm "GetHashCode Method (GH_ParamHashFields)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ComponentParamServerAddLanguageSpecificTextSet("LSTC0FAE2B9\_0?cpp=::|nu=.");GetHashCode Method (GH\_ParamHashFields) |

Creates a SHA1 hash from the parameter data.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public Guid GetHashCode(
	GH_ParamHashFields fields
)
```

```
Public Function GetHashCode ( 
	fields As GH_ParamHashFields
) As Guid
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

fields
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LSTC0FAE2B9\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_ParamHashFields](T_Grasshopper_Kernel_GH_ParamHashFields.htm)  
    Fields to include.

#### Return Value

Type: [Guid](https://docs.microsoft.com/dotnet/api/system.guid)  
A Guid representing a SHA hash of the parameter fields.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_ComponentParamServer Class](T_Grasshopper_Kernel_GH_ComponentParamServer.htm)

[GetHashCode Overload](Overload_Grasshopper_Kernel_GH_ComponentParamServer_GetHashCode.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)