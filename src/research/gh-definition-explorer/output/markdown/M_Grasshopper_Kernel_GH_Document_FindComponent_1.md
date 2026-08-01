# M_Grasshopper_Kernel_GH_Document_FindComponent_1

﻿ GH\_Document.FindComponent Method (Guid)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_Document Class](../html/T_Grasshopper_Kernel_GH_Document.htm "GH_Document Class")

[GH\_Document Methods](../html/Methods_T_Grasshopper_Kernel_GH_Document.htm "GH_Document Methods")

[FindComponent Method](../html/Overload_Grasshopper_Kernel_GH_Document_FindComponent.htm "FindComponent Method ")

[FindComponent Method (Guid)](../html/M_Grasshopper_Kernel_GH_Document_FindComponent_1.htm "FindComponent Method (Guid)")

[FindComponent Method (Point)](../html/M_Grasshopper_Kernel_GH_Document_FindComponent.htm "FindComponent Method (Point)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_DocumentAddLanguageSpecificTextSet("LST3CD40D80\_0?cpp=::|nu=.");FindComponent Method (Guid) |

Search for components using an ID filter

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public IGH_Component FindComponent(
	Guid id
)
```

```
Public Function FindComponent ( 
	id As Guid
) As IGH_Component
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

id
:   Type: [SystemAddLanguageSpecificTextSet("LST3CD40D80\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Guid](https://docs.microsoft.com/dotnet/api/system.guid)  
    ID to search for

#### Return Value

Type: [IGH\_Component](T_Grasshopper_Kernel_IGH_Component.htm)  
The component with the ID, or Null if no component could be found

![](../icons/SectionExpanded.png)Remarks

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Document Class](T_Grasshopper_Kernel_GH_Document.htm)

[FindComponent Overload](Overload_Grasshopper_Kernel_GH_Document_FindComponent.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)