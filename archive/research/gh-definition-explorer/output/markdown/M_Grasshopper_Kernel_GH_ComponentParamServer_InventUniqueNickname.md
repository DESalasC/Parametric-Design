# M_Grasshopper_Kernel_GH_ComponentParamServer_InventUniqueNickname

﻿ GH\_ComponentParamServer.InventUniqueNickname Method (String, IEnumerable(IGH\_Param))

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_ComponentParamServer Class](../html/T_Grasshopper_Kernel_GH_ComponentParamServer.htm "GH_ComponentParamServer Class")

[GH\_ComponentParamServer Methods](../html/Methods_T_Grasshopper_Kernel_GH_ComponentParamServer.htm "GH_ComponentParamServer Methods")

[InventUniqueNickname Method](../html/Overload_Grasshopper_Kernel_GH_ComponentParamServer_InventUniqueNickname.htm "InventUniqueNickname Method ")

[InventUniqueNickname Method (String, IEnumerable(IGH\_Param))](../html/M_Grasshopper_Kernel_GH_ComponentParamServer_InventUniqueNickname.htm "InventUniqueNickname Method (String, IEnumerable(IGH_Param))")

[InventUniqueNickname Method (String, IEnumerable(String))](../html/M_Grasshopper_Kernel_GH_ComponentParamServer_InventUniqueNickname_1.htm "InventUniqueNickname Method (String, IEnumerable(String))")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ComponentParamServerAddLanguageSpecificTextSet("LST5886AAD3\_0?cpp=::|nu=.");InventUniqueNickname Method (String, IEnumerableAddLanguageSpecificTextSet("LST5886AAD3\_1?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");IGH\_ParamAddLanguageSpecificTextSet("LST5886AAD3\_2?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");) |

Create a new, unique parameter nickname.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static string InventUniqueNickname(
	string allowedChars,
	IEnumerable<IGH_Param> existingNames
)
```

```
Public Shared Function InventUniqueNickname ( 
	allowedChars As String,
	existingNames As IEnumerable(Of IGH_Param)
) As String
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

allowedChars
:   Type: [SystemAddLanguageSpecificTextSet("LST5886AAD3\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Allowed character set for naming logic.

existingNames
:   Type: [System.Collections.GenericAddLanguageSpecificTextSet("LST5886AAD3\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");IEnumerable](https://docs.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)AddLanguageSpecificTextSet("LST5886AAD3\_5?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");[IGH\_Param](T_Grasshopper_Kernel_IGH_Param.htm)AddLanguageSpecificTextSet("LST5886AAD3\_6?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
    A collection of parameter names to avoid.

#### Return Value

Type: [String](https://docs.microsoft.com/dotnet/api/system.string)  
The first name combination that doesn't occur in the existingNames collection.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_ComponentParamServer Class](T_Grasshopper_Kernel_GH_ComponentParamServer.htm)

[InventUniqueNickname Overload](Overload_Grasshopper_Kernel_GH_ComponentParamServer_InventUniqueNickname.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)