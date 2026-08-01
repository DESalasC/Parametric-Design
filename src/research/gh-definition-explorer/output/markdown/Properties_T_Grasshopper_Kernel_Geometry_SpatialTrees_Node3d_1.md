# Properties_T_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1

﻿ Node3d(T) Properties

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Geometry.SpatialTrees](../html/N_Grasshopper_Kernel_Geometry_SpatialTrees.htm "Grasshopper.Kernel.Geometry.SpatialTrees")

[Node3d(T) Class](../html/T_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1.htm "Node3d(T) Class")

[Node3d(T) Properties](../html/Properties_T_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1.htm "Node3d(T) Properties")

[Center Property](../html/P_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_Center.htm "Center Property ")

[ChildCount Property](../html/P_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_ChildCount.htm "ChildCount Property ")

[ChildNode Property](../html/P_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_ChildNode.htm "ChildNode Property ")

[ContentAverage Property](../html/P_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_ContentAverage.htm "ContentAverage Property ")

[ContentBoundingBox Property](../html/P_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_ContentBoundingBox.htm "ContentBoundingBox Property ")

[IndicesLocal Property](../html/P_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_IndicesLocal.htm "IndicesLocal Property ")

[IndicesRecursive Property](../html/P_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_IndicesRecursive.htm "IndicesRecursive Property ")

[IsLeaf Property](../html/P_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_IsLeaf.htm "IsLeaf Property ")

[IsMutable Property](../html/P_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_IsMutable.htm "IsMutable Property ")

[IsRoot Property](../html/P_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_IsRoot.htm "IsRoot Property ")

[IsTwig Property](../html/P_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_IsTwig.htm "IsTwig Property ")

[ItemCount Property](../html/P_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_ItemCount.htm "ItemCount Property ")

[ItemsGlobal Property](../html/P_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_ItemsGlobal.htm "ItemsGlobal Property ")

[ItemsLocal Property](../html/P_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_ItemsLocal.htm "ItemsLocal Property ")

[Limit Property](../html/P_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_Limit.htm "Limit Property ")

[MemoryConsumption Property](../html/P_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_MemoryConsumption.htm "MemoryConsumption Property ")

[NextNode Property](../html/P_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_NextNode.htm "NextNode Property ")

[NodeDepth Property](../html/P_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_NodeDepth.htm "NodeDepth Property ")

[ParentNode Property](../html/P_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_ParentNode.htm "ParentNode Property ")

[Region Property](../html/P_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_Region.htm "Region Property ")

[RootNode Property](../html/P_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_RootNode.htm "RootNode Property ")

[WeightedSubdivision Property](../html/P_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_WeightedSubdivision.htm "WeightedSubdivision Property ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| Node3dAddLanguageSpecificTextSet("LST4ABB8216\_0?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST4ABB8216\_1?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)"); Properties |

The [Node3dAddLanguageSpecificTextSet("LST4ABB8216\_2?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST4ABB8216\_3?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1.htm) generic type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Center](P_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_Center.htm) | Gets the center of the spatial region of this node. If the node contains no children the center is always in the middle of the Region. If the node does contain child-nodes, the center may be anywhere within the region. |
| Public property | [ChildCount](P_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_ChildCount.htm) | Gets the number of defined child nodes. Leaf nodes have no children. Root and twig nodes can have anywhere between 1 and 8 children. |
| Public property | [ChildNode](P_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_ChildNode.htm) | Gets the child node at the given index. |
| Public property | [ContentAverage](P_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_ContentAverage.htm) | Returns the average coordinate of all items in this node. If this node does not contain any items, Point3d.Unset is returned. |
| Public property | [ContentBoundingBox](P_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_ContentBoundingBox.htm) | Returns the boundingbox of all items in this node. If this node does not contain any items, BoundingBox.Empty is returned. |
| Public property | [IndicesLocal](P_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_IndicesLocal.htm) | Gets the list of item indices that are contained within this node. |
| Public property | [IndicesRecursive](P_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_IndicesRecursive.htm) | Gets the list of item indices that are contained within this node and any child nodes. |
| Public property | [IsLeaf](P_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_IsLeaf.htm) | Gets whether this node is a leaf node. Leaf nodes have no child nodes. |
| Public property | [IsMutable](P_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_IsMutable.htm) | Gets whether this tree is mutable. You can only add items to mutable trees. We don't recommend removing items from unmutable trees, though that shouldn't necessarily lead to problems. Trees become unmutable after a call to ShrinkRegions(), CollapseNodes() or OptimizeTree(). |
| Public property | [IsRoot](P_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_IsRoot.htm) | Gets whether this node is a root node. Root nodes have no parent node and depth zero. |
| Public property | [IsTwig](P_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_IsTwig.htm) | Gets whether this node is a twig node. Twig nodes have both parents and at least one child. |
| Public property | [ItemCount](P_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_ItemCount.htm) | Gets the total number of items stored directly in this node. |
| Public property | [ItemsGlobal](P_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_ItemsGlobal.htm) | Gets the list of all items stored inside this entire tree. Do not modify this collection unless you know what you are doing. |
| Public property | [ItemsLocal](P_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_ItemsLocal.htm) | Gets a list of all the items stored directly in this node. This list is constructed every time you access this property, so keep it down to a minimum. |
| Public property | [Limit](P_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_Limit.htm) | Gets the subdivision limit for this tree. This limit can only be set once when you create a new tree. It is fixed forever after. |
| Public property | [MemoryConsumption](P_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_MemoryConsumption.htm) | Gets the estimated memory consumption of the (sub)tree structure. Items inside the global list are not included in this estimate. |
| Public property | [NextNode](P_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_NextNode.htm) | Gets the logical neighbour to the right of this node. There is no spatial relationships between logical neighbours, this is purely an iteration aid. |
| Public property | [NodeDepth](P_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_NodeDepth.htm) | Gets the recursive depth of this node. The tree root is at depth zero. The first subdivision is at depth one, and so on and so forth. |
| Public property | [ParentNode](P_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_ParentNode.htm) | Gets the immediate parent of this node. Root nodes have no parent. |
| Public property | [Region](P_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_Region.htm) | Gets the spatial region of this node. |
| Public property | [RootNode](P_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_RootNode.htm) | Gets the ultimate root node for this tree. |
| Public property | [WeightedSubdivision](P_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_WeightedSubdivision.htm) | Gets or sets whether subdivision is weighted based on content averages. Setting this value will only affect future subdivisions, not existing ones. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Node3dAddLanguageSpecificTextSet("LST4ABB8216\_4?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST4ABB8216\_5?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;"); Class](T_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1.htm)

[Grasshopper.Kernel.Geometry.SpatialTrees Namespace](N_Grasshopper_Kernel_Geometry_SpatialTrees.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)