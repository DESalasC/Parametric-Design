# M_Grasshopper_Kernel_GH_ComponentServer_FindObjects

﻿ GH\_ComponentServer.FindObjects Method (Guid)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_ComponentServer Class](../html/T_Grasshopper_Kernel_GH_ComponentServer.htm "GH_ComponentServer Class")

[GH\_ComponentServer Methods](../html/Methods_T_Grasshopper_Kernel_GH_ComponentServer.htm "GH_ComponentServer Methods")

[FindObjects Method](../html/Overload_Grasshopper_Kernel_GH_ComponentServer_FindObjects.htm "FindObjects Method ")

[FindObjects Method (Guid)](../html/M_Grasshopper_Kernel_GH_ComponentServer_FindObjects.htm "FindObjects Method (Guid)")

[FindObjects Method (String[], Int32, IGH\_ObjectProxy[], Double[])](../html/M_Grasshopper_Kernel_GH_ComponentServer_FindObjects_1.htm "FindObjects Method (String[], Int32, IGH_ObjectProxy[], Double[])")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ComponentServerAddLanguageSpecificTextSet("LST4D0BF424\_0?cpp=::|nu=.");FindObjects Method (Guid) |

Find all the objects that are part of a certain library.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public List<IGH_ObjectProxy> FindObjects(
	Guid libraryID
)
```

```
Public Function FindObjects ( 
	libraryID As Guid
) As List(Of IGH_ObjectProxy)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

libraryID
:   Type: [SystemAddLanguageSpecificTextSet("LST4D0BF424\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Guid](https://docs.microsoft.com/dotnet/api/system.guid)  
    ID of library to search for.

#### Return Value

Type: [List](https://docs.microsoft.com/dotnet/api/system.collections.generic.list-1)AddLanguageSpecificTextSet("LST4D0BF424\_2?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");[IGH\_ObjectProxy](T_Grasshopper_Kernel_IGH_ObjectProxy.htm)AddLanguageSpecificTextSet("LST4D0BF424\_3?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
A list of all the objects that are defined in the specified library.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_ComponentServer Class](T_Grasshopper_Kernel_GH_ComponentServer.htm)

[FindObjects Overload](Overload_Grasshopper_Kernel_GH_ComponentServer_FindObjects.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)