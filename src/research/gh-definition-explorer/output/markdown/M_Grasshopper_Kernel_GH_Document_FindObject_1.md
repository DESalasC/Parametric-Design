# M_Grasshopper_Kernel_GH_Document_FindObject_1

﻿ GH\_Document.FindObject Method (Guid, Boolean)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_Document Class](../html/T_Grasshopper_Kernel_GH_Document.htm "GH_Document Class")

[GH\_Document Methods](../html/Methods_T_Grasshopper_Kernel_GH_Document.htm "GH_Document Methods")

[FindObject Method](../html/Overload_Grasshopper_Kernel_GH_Document_FindObject.htm "FindObject Method ")

[FindObject Method (Guid, Boolean)](../html/M_Grasshopper_Kernel_GH_Document_FindObject_1.htm "FindObject Method (Guid, Boolean)")

[FindObject(T) Method (Guid, Boolean)](../html/M_Grasshopper_Kernel_GH_Document_FindObject__1.htm "FindObject(T) Method (Guid, Boolean)")

[FindObject Method (PointF, Single)](../html/M_Grasshopper_Kernel_GH_Document_FindObject.htm "FindObject Method (PointF, Single)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_DocumentAddLanguageSpecificTextSet("LST3B4ECE6D\_0?cpp=::|nu=.");FindObject Method (Guid, Boolean) |

Find the object that matches the ID.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public IGH_DocumentObject FindObject(
	Guid id,
	bool topLevelOnly
)
```

```
Public Function FindObject ( 
	id As Guid,
	topLevelOnly As Boolean
) As IGH_DocumentObject
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

id
:   Type: [SystemAddLanguageSpecificTextSet("LST3B4ECE6D\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Guid](https://docs.microsoft.com/dotnet/api/system.guid)  
    The ID to search for.

topLevelOnly
:   Type: [SystemAddLanguageSpecificTextSet("LST3B4ECE6D\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
    If True, only top-level objects are included. If False, the entire object attribute tree is recursed

#### Return Value

Type: [IGH\_DocumentObject](T_Grasshopper_Kernel_IGH_DocumentObject.htm)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Document Class](T_Grasshopper_Kernel_GH_Document.htm)

[FindObject Overload](Overload_Grasshopper_Kernel_GH_Document_FindObject.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)