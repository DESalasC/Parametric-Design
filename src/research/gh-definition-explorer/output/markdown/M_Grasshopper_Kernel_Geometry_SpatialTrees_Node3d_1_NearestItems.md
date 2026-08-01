# M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_NearestItems

﻿ Node3d(T).NearestItems Method (Double, Double, Double, Int32)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Geometry.SpatialTrees](../html/N_Grasshopper_Kernel_Geometry_SpatialTrees.htm "Grasshopper.Kernel.Geometry.SpatialTrees")

[Node3d(T) Class](../html/T_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1.htm "Node3d(T) Class")

[Node3d(T) Methods](../html/Methods_T_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1.htm "Node3d(T) Methods")

[NearestItems Method](../html/Overload_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_NearestItems.htm "NearestItems Method ")

[NearestItems Method (T, Int32)](../html/M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_NearestItems_2.htm "NearestItems Method (T, Int32)")

[NearestItems Method (Double, Double, Double, Int32)](../html/M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_NearestItems.htm "NearestItems Method (Double, Double, Double, Int32)")

[NearestItems Method (T, Int32, Double, Double)](../html/M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_NearestItems_3.htm "NearestItems Method (T, Int32, Double, Double)")

[NearestItems Method (Double, Double, Double, Int32, Double, Double)](../html/M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_NearestItems_1.htm "NearestItems Method (Double, Double, Double, Int32, Double, Double)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| Node3dAddLanguageSpecificTextSet("LST4B21899\_0?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST4B21899\_1?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");AddLanguageSpecificTextSet("LST4B21899\_2?cpp=::|nu=.");NearestItems Method (Double, Double, Double, Int32) |

Find the N nearest items.

**Namespace:**
 [Grasshopper.Kernel.Geometry.SpatialTrees](N_Grasshopper_Kernel_Geometry_SpatialTrees.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public List<Index3d<T>> NearestItems(
	double x,
	double y,
	double z,
	int groupSize
)
```

```
Public Function NearestItems ( 
	x As Double,
	y As Double,
	z As Double,
	groupSize As Integer
) As List(Of Index3d(Of T))
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

x
:   Type: [SystemAddLanguageSpecificTextSet("LST4B21899\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Double](https://docs.microsoft.com/dotnet/api/system.double)  
    x coordinate to search from.

y
:   Type: [SystemAddLanguageSpecificTextSet("LST4B21899\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");Double](https://docs.microsoft.com/dotnet/api/system.double)  
    y coordinate to search from.

z
:   Type: [SystemAddLanguageSpecificTextSet("LST4B21899\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");Double](https://docs.microsoft.com/dotnet/api/system.double)  
    z coordinate to search from.

groupSize
:   Type: [SystemAddLanguageSpecificTextSet("LST4B21899\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Number of nearest items to return.

#### Return Value

Type: [List](https://docs.microsoft.com/dotnet/api/system.collections.generic.list-1)AddLanguageSpecificTextSet("LST4B21899\_7?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");[Index3d](T_Grasshopper_Kernel_Geometry_SpatialTrees_Index3d_1.htm)AddLanguageSpecificTextSet("LST4B21899\_8?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");[T](T_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1.htm)AddLanguageSpecificTextSet("LST4B21899\_9?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");AddLanguageSpecificTextSet("LST4B21899\_10?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
A list of nearest items, sorted from nearest to furthest.

![](../icons/SectionExpanded.png)See Also

#### Reference

[Node3dAddLanguageSpecificTextSet("LST4B21899\_11?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST4B21899\_12?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;"); Class](T_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1.htm)

[NearestItems Overload](Overload_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_NearestItems.htm)

[Grasshopper.Kernel.Geometry.SpatialTrees Namespace](N_Grasshopper_Kernel_Geometry_SpatialTrees.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)