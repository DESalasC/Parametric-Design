# T_Grasshopper_Kernel_GH_DocumentAssociations

﻿ GH\_DocumentAssociations Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_DocumentAssociations Class](../html/T_Grasshopper_Kernel_GH_DocumentAssociations.htm "GH_DocumentAssociations Class")

[GH\_DocumentAssociations Constructor](../html/M_Grasshopper_Kernel_GH_DocumentAssociations__ctor.htm "GH_DocumentAssociations Constructor ")

[GH\_DocumentAssociations Methods](../html/Methods_T_Grasshopper_Kernel_GH_DocumentAssociations.htm "GH_DocumentAssociations Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_DocumentAssociations Class |

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST2C1D5A7B\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.KernelAddLanguageSpecificTextSet("LST2C1D5A7B\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_DocumentAssociations

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_DocumentAssociations
```

```
Public Class GH_DocumentAssociations
```

AddLanguageTabSet("ID1EBCA");

The GH\_DocumentAssociations type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_DocumentAssociations](M_Grasshopper_Kernel_GH_DocumentAssociations__ctor.htm) | Initializes a new instance of the GH\_DocumentAssociations class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [Associate](M_Grasshopper_Kernel_GH_DocumentAssociations_Associate.htm) | Add an association between a Rhino and a Grasshopper file. If a similar association already exists, it will be overwritten. This function reads and writes to the disk, it is SLOW. Only call it when you KNOW something changed. |
| Public method | [GetGrasshopperAssociations](M_Grasshopper_Kernel_GH_DocumentAssociations_GetGrasshopperAssociations.htm) | Find all the Grasshopper ghx files that have been associated with a given Rhino file. |
| Public method | [GetRhinoAssociations](M_Grasshopper_Kernel_GH_DocumentAssociations_GetRhinoAssociations.htm) | Find all the Rhino 3dm files that have been associated with a given Grasshopper file. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)