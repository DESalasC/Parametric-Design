# M_Grasshopper_Kernel_GH_ComponentParamServer_IndexOfInputParam

﻿ GH\_ComponentParamServer.IndexOfInputParam Method (Guid)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_ComponentParamServer Class](../html/T_Grasshopper_Kernel_GH_ComponentParamServer.htm "GH_ComponentParamServer Class")

[GH\_ComponentParamServer Methods](../html/Methods_T_Grasshopper_Kernel_GH_ComponentParamServer.htm "GH_ComponentParamServer Methods")

[IndexOfInputParam Method](../html/Overload_Grasshopper_Kernel_GH_ComponentParamServer_IndexOfInputParam.htm "IndexOfInputParam Method ")

[IndexOfInputParam Method (Guid)](../html/M_Grasshopper_Kernel_GH_ComponentParamServer_IndexOfInputParam.htm "IndexOfInputParam Method (Guid)")

[IndexOfInputParam Method (String)](../html/M_Grasshopper_Kernel_GH_ComponentParamServer_IndexOfInputParam_1.htm "IndexOfInputParam Method (String)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ComponentParamServerAddLanguageSpecificTextSet("LST1A7DE515\_0?cpp=::|nu=.");IndexOfInputParam Method (Guid) |

Finds the index of the input parameter that matches the specified search mask.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public int IndexOfInputParam(
	Guid id
)
```

```
Public Function IndexOfInputParam ( 
	id As Guid
) As Integer
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

id
:   Type: [SystemAddLanguageSpecificTextSet("LST1A7DE515\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Guid](https://docs.microsoft.com/dotnet/api/system.guid)  
    ID to search for

#### Return Value

Type: [Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
The index of the parameter, or -1 if no parameter was found to match

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_ComponentParamServer Class](T_Grasshopper_Kernel_GH_ComponentParamServer.htm)

[IndexOfInputParam Overload](Overload_Grasshopper_Kernel_GH_ComponentParamServer_IndexOfInputParam.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)