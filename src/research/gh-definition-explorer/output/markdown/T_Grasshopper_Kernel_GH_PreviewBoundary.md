# T_Grasshopper_Kernel_GH_PreviewBoundary

﻿ GH\_PreviewBoundary Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_PreviewBoundary Class](../html/T_Grasshopper_Kernel_GH_PreviewBoundary.htm "GH_PreviewBoundary Class")

[GH\_PreviewBoundary Constructor](../html/M_Grasshopper_Kernel_GH_PreviewBoundary__ctor.htm "GH_PreviewBoundary Constructor ")

[GH\_PreviewBoundary Properties](../html/Properties_T_Grasshopper_Kernel_GH_PreviewBoundary.htm "GH_PreviewBoundary Properties")

[GH\_PreviewBoundary Methods](../html/Methods_T_Grasshopper_Kernel_GH_PreviewBoundary.htm "GH_PreviewBoundary Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_PreviewBoundary Class |

A closed boundary for filtering previewed objects.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LSTA20D71E9\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.KernelAddLanguageSpecificTextSet("LSTA20D71E9\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_PreviewBoundary

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_PreviewBoundary : GH_ISerializable
```

```
Public Class GH_PreviewBoundary
	Implements GH_ISerializable
```

AddLanguageTabSet("ID1EBCA");

The GH\_PreviewBoundary type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_PreviewBoundary](M_Grasshopper_Kernel_GH_PreviewBoundary__ctor.htm) | Create a new preview boundary. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Boundary](P_Grasshopper_Kernel_GH_PreviewBoundary_Boundary.htm) | Gets the boundary region. |
| Public property | [Limits](P_Grasshopper_Kernel_GH_PreviewBoundary_Limits.htm) | Gets the limits of the boundary. |
| Public property | [Points](P_Grasshopper_Kernel_GH_PreviewBoundary_Points.htm) | Gets the array of points this boundary was made from. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [IsVisible](M_Grasshopper_Kernel_GH_PreviewBoundary_IsVisible.htm) | Gets whether a specific object is visible within this boundary. |
| Public method | [Read](M_Grasshopper_Kernel_GH_PreviewBoundary_Read.htm) |  |
| Public method | [Write](M_Grasshopper_Kernel_GH_PreviewBoundary_Write.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)