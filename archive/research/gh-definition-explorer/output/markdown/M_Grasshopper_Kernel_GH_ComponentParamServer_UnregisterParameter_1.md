# M_Grasshopper_Kernel_GH_ComponentParamServer_UnregisterParameter_1

﻿ GH\_ComponentParamServer.UnregisterParameter Method (IGH\_Param, Boolean)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_ComponentParamServer Class](../html/T_Grasshopper_Kernel_GH_ComponentParamServer.htm "GH_ComponentParamServer Class")

[GH\_ComponentParamServer Methods](../html/Methods_T_Grasshopper_Kernel_GH_ComponentParamServer.htm "GH_ComponentParamServer Methods")

[UnregisterParameter Method](../html/Overload_Grasshopper_Kernel_GH_ComponentParamServer_UnregisterParameter.htm "UnregisterParameter Method ")

[UnregisterParameter Method (IGH\_Param)](../html/M_Grasshopper_Kernel_GH_ComponentParamServer_UnregisterParameter.htm "UnregisterParameter Method (IGH_Param)")

[UnregisterParameter Method (IGH\_Param, Boolean)](../html/M_Grasshopper_Kernel_GH_ComponentParamServer_UnregisterParameter_1.htm "UnregisterParameter Method (IGH_Param, Boolean)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ComponentParamServerAddLanguageSpecificTextSet("LSTB9A17EDE\_0?cpp=::|nu=.");UnregisterParameter Method (IGH\_Param, Boolean) |

Removes the specified parameter from this component.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public bool UnregisterParameter(
	IGH_Param param,
	bool isolate
)
```

```
Public Function UnregisterParameter ( 
	param As IGH_Param,
	isolate As Boolean
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

param
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LSTB9A17EDE\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");IGH\_Param](T_Grasshopper_Kernel_IGH_Param.htm)  
    Parameter to remove

isolate
:   Type: [SystemAddLanguageSpecificTextSet("LSTB9A17EDE\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
    If true, parameters that are removed will be isolated from sources and recipients.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_ComponentParamServer Class](T_Grasshopper_Kernel_GH_ComponentParamServer.htm)

[UnregisterParameter Overload](Overload_Grasshopper_Kernel_GH_ComponentParamServer_UnregisterParameter.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)