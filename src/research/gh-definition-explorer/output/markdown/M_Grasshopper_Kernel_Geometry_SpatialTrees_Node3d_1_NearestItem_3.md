# M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_NearestItem_3

﻿ Node3d(T).NearestItem Method (Double, Double, Double, Validation3d(T))

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Geometry.SpatialTrees](../html/N_Grasshopper_Kernel_Geometry_SpatialTrees.htm "Grasshopper.Kernel.Geometry.SpatialTrees")

[Node3d(T) Class](../html/T_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1.htm "Node3d(T) Class")

[Node3d(T) Methods](../html/Methods_T_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1.htm "Node3d(T) Methods")

[NearestItem Method](../html/Overload_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_NearestItem.htm "NearestItem Method ")

[NearestItem Method (T)](../html/M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_NearestItem_5.htm "NearestItem Method (T)")

[NearestItem Method (Point3d)](../html/M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_NearestItem.htm "NearestItem Method (Point3d)")

[NearestItem Method (Double, Double, Double)](../html/M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_NearestItem_2.htm "NearestItem Method (Double, Double, Double)")

[NearestItem Method (T, Double, Double)](../html/M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_NearestItem_6.htm "NearestItem Method (T, Double, Double)")

[NearestItem Method (Point3d, Double, Double)](../html/M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_NearestItem_1.htm "NearestItem Method (Point3d, Double, Double)")

[NearestItem Method (Double, Double, Double, Validation3d(T))](../html/M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_NearestItem_3.htm "NearestItem Method (Double, Double, Double, Validation3d(T))")

[NearestItem Method (Double, Double, Double, Double, Double)](../html/M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_NearestItem_4.htm "NearestItem Method (Double, Double, Double, Double, Double)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| Node3dAddLanguageSpecificTextSet("LST289AEE71\_0?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST289AEE71\_1?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");AddLanguageSpecificTextSet("LST289AEE71\_2?cpp=::|nu=.");NearestItem Method (Double, Double, Double, Validation3dAddLanguageSpecificTextSet("LST289AEE71\_3?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST289AEE71\_4?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");) |

Find the nearest item using custom validation criteria.

**Namespace:**
 [Grasshopper.Kernel.Geometry.SpatialTrees](N_Grasshopper_Kernel_Geometry_SpatialTrees.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public Index3d<T> NearestItem(
	double x,
	double y,
	double z,
	Validation3d<T> validationDelegate
)
```

```
Public Function NearestItem ( 
	x As Double,
	y As Double,
	z As Double,
	validationDelegate As Validation3d(Of T)
) As Index3d(Of T)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

x
:   Type: [SystemAddLanguageSpecificTextSet("LST289AEE71\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");Double](https://docs.microsoft.com/dotnet/api/system.double)  
    x coordinate to search from.

y
:   Type: [SystemAddLanguageSpecificTextSet("LST289AEE71\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");Double](https://docs.microsoft.com/dotnet/api/system.double)  
    y coordinate to search from.

z
:   Type: [SystemAddLanguageSpecificTextSet("LST289AEE71\_7?cs=.|vb=.|cpp=::|nu=.|fs=.");Double](https://docs.microsoft.com/dotnet/api/system.double)  
    z coordinate to search from.

validationDelegate
:   Type: [Grasshopper.Kernel.Geometry.SpatialTreesAddLanguageSpecificTextSet("LST289AEE71\_8?cs=.|vb=.|cpp=::|nu=.|fs=.");Validation3d](T_Grasshopper_Kernel_Geometry_SpatialTrees_Validation3d_1.htm)AddLanguageSpecificTextSet("LST289AEE71\_9?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");[T](T_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1.htm)AddLanguageSpecificTextSet("LST289AEE71\_10?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
    Item validation delegate.

#### Return Value

Type: [Index3d](T_Grasshopper_Kernel_Geometry_SpatialTrees_Index3d_1.htm)AddLanguageSpecificTextSet("LST289AEE71\_11?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");[T](T_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1.htm)AddLanguageSpecificTextSet("LST289AEE71\_12?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
The index of the nearest item or null if no nearest item could be found.

![](../icons/SectionExpanded.png)See Also

#### Reference

[Node3dAddLanguageSpecificTextSet("LST289AEE71\_13?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST289AEE71\_14?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;"); Class](T_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1.htm)

[NearestItem Overload](Overload_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_NearestItem.htm)

[Grasshopper.Kernel.Geometry.SpatialTrees Namespace](N_Grasshopper_Kernel_Geometry_SpatialTrees.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)