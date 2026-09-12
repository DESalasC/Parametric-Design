# M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_OptimizeTree

﻿ Node3d(T).OptimizeTree Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Geometry.SpatialTrees](../html/N_Grasshopper_Kernel_Geometry_SpatialTrees.htm "Grasshopper.Kernel.Geometry.SpatialTrees")

[Node3d(T) Class](../html/T_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1.htm "Node3d(T) Class")

[Node3d(T) Methods](../html/Methods_T_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1.htm "Node3d(T) Methods")

[Add Method](../html/M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_Add.htm "Add Method ")

[AddRange Method](../html/M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_AddRange.htm "AddRange Method ")

[AddToRhinoDocument Method](../html/M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_AddToRhinoDocument.htm "AddToRhinoDocument Method ")

[CollapseNodes Method](../html/M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_CollapseNodes.htm "CollapseNodes Method ")

[FurthestItem Method](../html/Overload_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_FurthestItem.htm "FurthestItem Method ")

[NearestItem Method](../html/Overload_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_NearestItem.htm "NearestItem Method ")

[NearestItems Method](../html/Overload_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_NearestItems.htm "NearestItems Method ")

[OptimizeTree Method](../html/M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_OptimizeTree.htm "OptimizeTree Method ")

[Remove Method](../html/Overload_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_Remove.htm "Remove Method ")

[ShrinkRegions Method](../html/M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_ShrinkRegions.htm "ShrinkRegions Method ")

[SubTree Method](../html/M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_SubTree.htm "SubTree Method ")

[TrimExcess Method](../html/M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_TrimExcess.htm "TrimExcess Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| Node3dAddLanguageSpecificTextSet("LSTD5880DCF\_0?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTD5880DCF\_1?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");AddLanguageSpecificTextSet("LSTD5880DCF\_2?cpp=::|nu=.");OptimizeTree Method |

Optimize this tree for fast searches. Do not call this method if you still plan to add items in the future.
You can no longer modify this tree once it has been optimized.

**Namespace:**
 [Grasshopper.Kernel.Geometry.SpatialTrees](N_Grasshopper_Kernel_Geometry_SpatialTrees.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public Node3d<T> OptimizeTree()
```

```
Public Function OptimizeTree As Node3d(Of T)
```

AddLanguageTabSet("ID0EBCA");

#### Return Value

Type: [Node3d](T_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1.htm)AddLanguageSpecificTextSet("LSTD5880DCF\_3?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");[T](T_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1.htm)AddLanguageSpecificTextSet("LSTD5880DCF\_4?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
The new root of the optimized tree. If the root could not be optimized an instance of this node will be returned.

![](../icons/SectionExpanded.png)See Also

#### Reference

[Node3dAddLanguageSpecificTextSet("LSTD5880DCF\_5?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTD5880DCF\_6?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;"); Class](T_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1.htm)

[Grasshopper.Kernel.Geometry.SpatialTrees Namespace](N_Grasshopper_Kernel_Geometry_SpatialTrees.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)