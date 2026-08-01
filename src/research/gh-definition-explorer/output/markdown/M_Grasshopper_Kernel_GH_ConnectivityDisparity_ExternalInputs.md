# M_Grasshopper_Kernel_GH_ConnectivityDisparity_ExternalInputs

﻿ GH\_ConnectivityDisparity.ExternalInputs Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_ConnectivityDisparity Class](../html/T_Grasshopper_Kernel_GH_ConnectivityDisparity.htm "GH_ConnectivityDisparity Class")

[GH\_ConnectivityDisparity Methods](../html/Methods_T_Grasshopper_Kernel_GH_ConnectivityDisparity.htm "GH_ConnectivityDisparity Methods")

[ExternalInputs Method](../html/M_Grasshopper_Kernel_GH_ConnectivityDisparity_ExternalInputs.htm "ExternalInputs Method ")

[ExternalOutputs Method](../html/M_Grasshopper_Kernel_GH_ConnectivityDisparity_ExternalOutputs.htm "ExternalOutputs Method ")

[InternalInputs Method](../html/M_Grasshopper_Kernel_GH_ConnectivityDisparity_InternalInputs.htm "InternalInputs Method ")

[InternalOutputs Method](../html/M_Grasshopper_Kernel_GH_ConnectivityDisparity_InternalOutputs.htm "InternalOutputs Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ConnectivityDisparityAddLanguageSpecificTextSet("LSTD4C62508\_0?cpp=::|nu=.");ExternalInputs Method |

Find all external sources for a given id in the subset.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public List<Guid> ExternalInputs(
	Guid id
)
```

```
Public Function ExternalInputs ( 
	id As Guid
) As List(Of Guid)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

id
:   Type: [SystemAddLanguageSpecificTextSet("LSTD4C62508\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Guid](https://docs.microsoft.com/dotnet/api/system.guid)  
    ID of parameter.

#### Return Value

Type: [List](https://docs.microsoft.com/dotnet/api/system.collections.generic.list-1)AddLanguageSpecificTextSet("LSTD4C62508\_2?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");[Guid](https://docs.microsoft.com/dotnet/api/system.guid)AddLanguageSpecificTextSet("LSTD4C62508\_3?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
A list containing all sources that are not present in the subset topology.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_ConnectivityDisparity Class](T_Grasshopper_Kernel_GH_ConnectivityDisparity.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)