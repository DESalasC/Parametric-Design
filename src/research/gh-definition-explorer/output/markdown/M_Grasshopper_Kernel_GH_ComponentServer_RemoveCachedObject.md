# M_Grasshopper_Kernel_GH_ComponentServer_RemoveCachedObject

﻿ GH\_ComponentServer.RemoveCachedObject Method (Guid)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_ComponentServer Class](../html/T_Grasshopper_Kernel_GH_ComponentServer.htm "GH_ComponentServer Class")

[GH\_ComponentServer Methods](../html/Methods_T_Grasshopper_Kernel_GH_ComponentServer.htm "GH_ComponentServer Methods")

[RemoveCachedObject Method](../html/Overload_Grasshopper_Kernel_GH_ComponentServer_RemoveCachedObject.htm "RemoveCachedObject Method ")

[RemoveCachedObject Method (Guid)](../html/M_Grasshopper_Kernel_GH_ComponentServer_RemoveCachedObject.htm "RemoveCachedObject Method (Guid)")

[RemoveCachedObject Method (String)](../html/M_Grasshopper_Kernel_GH_ComponentServer_RemoveCachedObject_1.htm "RemoveCachedObject Method (String)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ComponentServerAddLanguageSpecificTextSet("LST83812696\_0?cpp=::|nu=.");RemoveCachedObject Method (Guid) |

Remove a cache entry from the object cache. This cannot be undone.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public bool RemoveCachedObject(
	Guid id
)
```

```
Public Function RemoveCachedObject ( 
	id As Guid
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

id
:   Type: [SystemAddLanguageSpecificTextSet("LST83812696\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Guid](https://docs.microsoft.com/dotnet/api/system.guid)  
    The id to remove.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True on success, false on failure.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_ComponentServer Class](T_Grasshopper_Kernel_GH_ComponentServer.htm)

[RemoveCachedObject Overload](Overload_Grasshopper_Kernel_GH_ComponentServer_RemoveCachedObject.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)