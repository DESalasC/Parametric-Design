# M_Grasshopper_Kernel_GH_ComponentServer_FindAssemblyByObject_1

﻿ GH\_ComponentServer.FindAssemblyByObject Method (Guid)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_ComponentServer Class](../html/T_Grasshopper_Kernel_GH_ComponentServer.htm "GH_ComponentServer Class")

[GH\_ComponentServer Methods](../html/Methods_T_Grasshopper_Kernel_GH_ComponentServer.htm "GH_ComponentServer Methods")

[FindAssemblyByObject Method](../html/Overload_Grasshopper_Kernel_GH_ComponentServer_FindAssemblyByObject.htm "FindAssemblyByObject Method ")

[FindAssemblyByObject Method (Guid)](../html/M_Grasshopper_Kernel_GH_ComponentServer_FindAssemblyByObject_1.htm "FindAssemblyByObject Method (Guid)")

[FindAssemblyByObject Method (IGH\_DocumentObject)](../html/M_Grasshopper_Kernel_GH_ComponentServer_FindAssemblyByObject.htm "FindAssemblyByObject Method (IGH_DocumentObject)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ComponentServerAddLanguageSpecificTextSet("LSTB5A8981E\_0?cpp=::|nu=.");FindAssemblyByObject Method (Guid) |

Gets the assembly that corresponds to the given library ID.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public GH_AssemblyInfo FindAssemblyByObject(
	Guid objectId
)
```

```
Public Function FindAssemblyByObject ( 
	objectId As Guid
) As GH_AssemblyInfo
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

objectId
:   Type: [SystemAddLanguageSpecificTextSet("LSTB5A8981E\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Guid](https://docs.microsoft.com/dotnet/api/system.guid)  
    The object ComponentGuid.

#### Return Value

Type: [GH\_AssemblyInfo](T_Grasshopper_Kernel_GH_AssemblyInfo.htm)  
The library info, or null if the ID is not registered.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_ComponentServer Class](T_Grasshopper_Kernel_GH_ComponentServer.htm)

[FindAssemblyByObject Overload](Overload_Grasshopper_Kernel_GH_ComponentServer_FindAssemblyByObject.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)