# M_Grasshopper_Kernel_GH_DocumentAssociations_GetRhinoAssociations

﻿ GH\_DocumentAssociations.GetRhinoAssociations Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_DocumentAssociations Class](../html/T_Grasshopper_Kernel_GH_DocumentAssociations.htm "GH_DocumentAssociations Class")

[GH\_DocumentAssociations Methods](../html/Methods_T_Grasshopper_Kernel_GH_DocumentAssociations.htm "GH_DocumentAssociations Methods")

[Associate Method](../html/M_Grasshopper_Kernel_GH_DocumentAssociations_Associate.htm "Associate Method ")

[GetGrasshopperAssociations Method](../html/M_Grasshopper_Kernel_GH_DocumentAssociations_GetGrasshopperAssociations.htm "GetGrasshopperAssociations Method ")

[GetRhinoAssociations Method](../html/M_Grasshopper_Kernel_GH_DocumentAssociations_GetRhinoAssociations.htm "GetRhinoAssociations Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_DocumentAssociationsAddLanguageSpecificTextSet("LSTFBEB7190\_0?cpp=::|nu=.");GetRhinoAssociations Method |

Find all the Rhino 3dm files that have been associated with a given Grasshopper file.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public List<string> GetRhinoAssociations(
	string grasshopperFile
)
```

```
Public Function GetRhinoAssociations ( 
	grasshopperFile As String
) As List(Of String)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

grasshopperFile
:   Type: [SystemAddLanguageSpecificTextSet("LSTFBEB7190\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Grasshopper file path.

#### Return Value

Type: [List](https://docs.microsoft.com/dotnet/api/system.collections.generic.list-1)AddLanguageSpecificTextSet("LSTFBEB7190\_2?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");[String](https://docs.microsoft.com/dotnet/api/system.string)AddLanguageSpecificTextSet("LSTFBEB7190\_3?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
A list of files, ordered chronologically (most recent association first)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_DocumentAssociations Class](T_Grasshopper_Kernel_GH_DocumentAssociations.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)