# M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1__ctor

﻿ Node3d(T) Constructor (Coordinates3d(T), BoundingBox)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Geometry.SpatialTrees](../html/N_Grasshopper_Kernel_Geometry_SpatialTrees.htm "Grasshopper.Kernel.Geometry.SpatialTrees")

[Node3d(T) Class](../html/T_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1.htm "Node3d(T) Class")

[Node3d(T) Constructor](../html/Overload_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1__ctor.htm "Node3d(T) Constructor ")

[Node3d(T) Constructor (Coordinates3d(T), BoundingBox)](../html/M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1__ctor.htm "Node3d(T) Constructor (Coordinates3d(T), BoundingBox)")

[Node3d(T) Constructor (Coordinates3d(T), BoundingBox, Int32)](../html/M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1__ctor_1.htm "Node3d(T) Constructor (Coordinates3d(T), BoundingBox, Int32)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| Node3dAddLanguageSpecificTextSet("LST3F270D4F\_0?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST3F270D4F\_1?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)"); Constructor (Coordinates3dAddLanguageSpecificTextSet("LST3F270D4F\_2?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST3F270D4F\_3?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");, BoundingBox) |

Create a new spatial tree root.

**Namespace:**
 [Grasshopper.Kernel.Geometry.SpatialTrees](N_Grasshopper_Kernel_Geometry_SpatialTrees.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public Node3d(
	Coordinates3d<T> converter,
	BoundingBox region
)
```

```
Public Sub New ( 
	converter As Coordinates3d(Of T),
	region As BoundingBox
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

converter
:   Type: [Grasshopper.Kernel.Geometry.SpatialTreesAddLanguageSpecificTextSet("LST3F270D4F\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");Coordinates3d](T_Grasshopper_Kernel_Geometry_SpatialTrees_Coordinates3d_1.htm)AddLanguageSpecificTextSet("LST3F270D4F\_5?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");[T](T_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1.htm)AddLanguageSpecificTextSet("LST3F270D4F\_6?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
    Converter delegate.

region
:   Type: BoundingBox  
    Bounding box for this node. The region should be big enough to contain all items you're going to insert.

![](../icons/SectionExpanded.png)See Also

#### Reference

[Node3dAddLanguageSpecificTextSet("LST3F270D4F\_7?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST3F270D4F\_8?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;"); Class](T_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1.htm)

[Node3dAddLanguageSpecificTextSet("LST3F270D4F\_9?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST3F270D4F\_10?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;"); Overload](Overload_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1__ctor.htm)

[Grasshopper.Kernel.Geometry.SpatialTrees Namespace](N_Grasshopper_Kernel_Geometry_SpatialTrees.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)