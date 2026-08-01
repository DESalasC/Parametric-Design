# M_Grasshopper_Kernel_GH_ComponentServer_RemoveCachedObject_1

﻿ GH\_ComponentServer.RemoveCachedObject Method (String)

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
| GH\_ComponentServerAddLanguageSpecificTextSet("LST4CA145CB\_0?cpp=::|nu=.");RemoveCachedObject Method (String) |

Remove the user object (if any) that loads itself from a specified \*.ghuser file.

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
	string userObjectFilePath
)
```

```
Public Function RemoveCachedObject ( 
	userObjectFilePath As String
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

userObjectFilePath
:   Type: [SystemAddLanguageSpecificTextSet("LST4CA145CB\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    File name path of user object proxy.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True if an object proxy was removed, false if not.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_ComponentServer Class](T_Grasshopper_Kernel_GH_ComponentServer.htm)

[RemoveCachedObject Overload](Overload_Grasshopper_Kernel_GH_ComponentServer_RemoveCachedObject.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)