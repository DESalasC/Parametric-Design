# M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_FurthestItem_5

﻿ Node3d(T).FurthestItem Method (T, Double, Double)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Geometry.SpatialTrees](../html/N_Grasshopper_Kernel_Geometry_SpatialTrees.htm "Grasshopper.Kernel.Geometry.SpatialTrees")

[Node3d(T) Class](../html/T_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1.htm "Node3d(T) Class")

[Node3d(T) Methods](../html/Methods_T_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1.htm "Node3d(T) Methods")

[FurthestItem Method](../html/Overload_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_FurthestItem.htm "FurthestItem Method ")

[FurthestItem Method (T)](../html/M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_FurthestItem_4.htm "FurthestItem Method (T)")

[FurthestItem Method (Point3d)](../html/M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_FurthestItem.htm "FurthestItem Method (Point3d)")

[FurthestItem Method (Double, Double, Double)](../html/M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_FurthestItem_2.htm "FurthestItem Method (Double, Double, Double)")

[FurthestItem Method (T, Double, Double)](../html/M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_FurthestItem_5.htm "FurthestItem Method (T, Double, Double)")

[FurthestItem Method (Point3d, Double, Double)](../html/M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_FurthestItem_1.htm "FurthestItem Method (Point3d, Double, Double)")

[FurthestItem Method (Double, Double, Double, Double, Double)](../html/M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_FurthestItem_3.htm "FurthestItem Method (Double, Double, Double, Double, Double)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| Node3dAddLanguageSpecificTextSet("LSTB70A4B51\_0?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTB70A4B51\_1?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");AddLanguageSpecificTextSet("LSTB70A4B51\_2?cpp=::|nu=.");FurthestItem Method (T, Double, Double) |

Find the furtest item.

**Namespace:**
 [Grasshopper.Kernel.Geometry.SpatialTrees](N_Grasshopper_Kernel_Geometry_SpatialTrees.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public Index3d<T> FurthestItem(
	T locus,
	double minimumDistance,
	double maximumDistance
)
```

```
Public Function FurthestItem ( 
	locus As T,
	minimumDistance As Double,
	maximumDistance As Double
) As Index3d(Of T)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

locus
:   Type: [T](T_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1.htm)  
    Location to search from.

minimumDistance
:   Type: [SystemAddLanguageSpecificTextSet("LSTB70A4B51\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Double](https://docs.microsoft.com/dotnet/api/system.double)  
    Minimum distance for furtest item. Items closer than minimumDistance will be ignored.

maximumDistance
:   Type: [SystemAddLanguageSpecificTextSet("LSTB70A4B51\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");Double](https://docs.microsoft.com/dotnet/api/system.double)  
    Maximum distance for furtest item. Items further than maximumDistance will be ignored.

#### Return Value

Type: [Index3d](T_Grasshopper_Kernel_Geometry_SpatialTrees_Index3d_1.htm)AddLanguageSpecificTextSet("LSTB70A4B51\_5?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");[T](T_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1.htm)AddLanguageSpecificTextSet("LSTB70A4B51\_6?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
The index of the furtest item or null if no furtest item could be found.

![](../icons/SectionExpanded.png)See Also

#### Reference

[Node3dAddLanguageSpecificTextSet("LSTB70A4B51\_7?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTB70A4B51\_8?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;"); Class](T_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1.htm)

[FurthestItem Overload](Overload_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_FurthestItem.htm)

[Grasshopper.Kernel.Geometry.SpatialTrees Namespace](N_Grasshopper_Kernel_Geometry_SpatialTrees.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)