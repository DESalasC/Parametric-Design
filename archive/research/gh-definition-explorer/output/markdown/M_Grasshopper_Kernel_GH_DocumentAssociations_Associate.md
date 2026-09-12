# M_Grasshopper_Kernel_GH_DocumentAssociations_Associate

﻿ GH\_DocumentAssociations.Associate Method 

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
| GH\_DocumentAssociationsAddLanguageSpecificTextSet("LST39D50A67\_0?cpp=::|nu=.");Associate Method |

Add an association between a Rhino and a Grasshopper file.
If a similar association already exists, it will be overwritten.
This function reads and writes to the disk, it is SLOW. Only call
it when you KNOW something changed.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public void Associate(
	string rhinoFile,
	string grasshopperFile
)
```

```
Public Sub Associate ( 
	rhinoFile As String,
	grasshopperFile As String
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

rhinoFile
:   Type: [SystemAddLanguageSpecificTextSet("LST39D50A67\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Path to Rhino 3dm file.

grasshopperFile
:   Type: [SystemAddLanguageSpecificTextSet("LST39D50A67\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Path to Grasshopper ghx or gh file.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_DocumentAssociations Class](T_Grasshopper_Kernel_GH_DocumentAssociations.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)