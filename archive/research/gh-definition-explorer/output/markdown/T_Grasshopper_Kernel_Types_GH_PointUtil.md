# T_Grasshopper_Kernel_Types_GH_PointUtil

﻿ GH\_PointUtil Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm "Grasshopper.Kernel.Types")

[GH\_PointUtil Class](../html/T_Grasshopper_Kernel_Types_GH_PointUtil.htm "GH_PointUtil Class")

[GH\_PointUtil Methods](../html/Methods_T_Grasshopper_Kernel_Types_GH_PointUtil.htm "GH_PointUtil Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_PointUtil Class |

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LSTA77C80F2\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.Kernel.TypesAddLanguageSpecificTextSet("LSTA77C80F2\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_PointUtil

**Namespace:**
 [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public sealed class GH_PointUtil
```

```
Public NotInheritable Class GH_PointUtil
```

AddLanguageTabSet("ID1EBCA");

The GH\_PointUtil type exposes the following members.

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public methodStatic member | [FitPlaneThroughPoints](M_Grasshopper_Kernel_Types_GH_PointUtil_FitPlaneThroughPoints.htm) | Fit a least-squares plane through a collection of points. |
| Public methodStatic member | [ProjectPointsToPlane](M_Grasshopper_Kernel_Types_GH_PointUtil_ProjectPointsToPlane.htm) | Project a list of points onto the plane. The result will be points in plane-uv coordinates. |
| Public methodStatic member | [PullPointsToPlane](M_Grasshopper_Kernel_Types_GH_PointUtil_PullPointsToPlane.htm) | Pull a list of points onto the plane. The result will be points in 3D world coordinates which are coincident with the given plane. |
| Public methodStatic member | [RemapPointsToPlane](M_Grasshopper_Kernel_Types_GH_PointUtil_RemapPointsToPlane.htm) | Remap a list of points onto the plane. This operation equals a ChangeBasisXForm for each point. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Types Namespace](N_Grasshopper_Kernel_Types.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)