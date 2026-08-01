# M_Grasshopper_Kernel_Types_GH_PointUtil_PullPointsToPlane

﻿ GH\_PointUtil.PullPointsToPlane Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm "Grasshopper.Kernel.Types")

[GH\_PointUtil Class](../html/T_Grasshopper_Kernel_Types_GH_PointUtil.htm "GH_PointUtil Class")

[GH\_PointUtil Methods](../html/Methods_T_Grasshopper_Kernel_Types_GH_PointUtil.htm "GH_PointUtil Methods")

[FitPlaneThroughPoints Method](../html/M_Grasshopper_Kernel_Types_GH_PointUtil_FitPlaneThroughPoints.htm "FitPlaneThroughPoints Method ")

[ProjectPointsToPlane Method](../html/M_Grasshopper_Kernel_Types_GH_PointUtil_ProjectPointsToPlane.htm "ProjectPointsToPlane Method ")

[PullPointsToPlane Method](../html/M_Grasshopper_Kernel_Types_GH_PointUtil_PullPointsToPlane.htm "PullPointsToPlane Method ")

[RemapPointsToPlane Method](../html/M_Grasshopper_Kernel_Types_GH_PointUtil_RemapPointsToPlane.htm "RemapPointsToPlane Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_PointUtilAddLanguageSpecificTextSet("LSTF6B4D030\_0?cpp=::|nu=.");PullPointsToPlane Method |

Pull a list of points onto the plane. The result will be points in 3D world coordinates
which are coincident with the given plane.

**Namespace:**
 [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static List<GH_Point> PullPointsToPlane(
	IEnumerable<GH_Point> pts,
	Plane plane,
	bool include_nulls
)
```

```
Public Shared Function PullPointsToPlane ( 
	pts As IEnumerable(Of GH_Point),
	plane As Plane,
	include_nulls As Boolean
) As List(Of GH_Point)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

pts
:   Type: [System.Collections.GenericAddLanguageSpecificTextSet("LSTF6B4D030\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");IEnumerable](https://docs.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)AddLanguageSpecificTextSet("LSTF6B4D030\_2?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");[GH\_Point](T_Grasshopper_Kernel_Types_GH_Point.htm)AddLanguageSpecificTextSet("LSTF6B4D030\_3?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
    Points to pull.

plane
:   Type: Plane  
    Plane to pull onto.

include\_nulls
:   Type: [SystemAddLanguageSpecificTextSet("LSTF6B4D030\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
    If True, nulls in the pts list are maintained.

#### Return Value

Type: [List](https://docs.microsoft.com/dotnet/api/system.collections.generic.list-1)AddLanguageSpecificTextSet("LSTF6B4D030\_5?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");[GH\_Point](T_Grasshopper_Kernel_Types_GH_Point.htm)AddLanguageSpecificTextSet("LSTF6B4D030\_6?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_PointUtil Class](T_Grasshopper_Kernel_Types_GH_PointUtil.htm)

[Grasshopper.Kernel.Types Namespace](N_Grasshopper_Kernel_Types.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)