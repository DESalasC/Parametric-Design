# T_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1

﻿ Node3d(T) Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Geometry.SpatialTrees](../html/N_Grasshopper_Kernel_Geometry_SpatialTrees.htm "Grasshopper.Kernel.Geometry.SpatialTrees")

[Node3d(T) Class](../html/T_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1.htm "Node3d(T) Class")

[Node3d(T) Constructor](../html/Overload_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1__ctor.htm "Node3d(T) Constructor ")

[Node3d(T) Properties](../html/Properties_T_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1.htm "Node3d(T) Properties")

[Node3d(T) Methods](../html/Methods_T_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1.htm "Node3d(T) Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| Node3dAddLanguageSpecificTextSet("LSTD882787F\_0?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTD882787F\_1?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)"); Class |

Basic node in a Tree3d structure. Nodes in tree structures maintain a local region and
either a list of content indices or a list of up to 8 child nodes.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LSTD882787F\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.Kernel.Geometry.SpatialTreesAddLanguageSpecificTextSet("LSTD882787F\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Node3dAddLanguageSpecificTextSet("LSTD882787F\_4?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTD882787F\_5?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");

**Namespace:**
 [Grasshopper.Kernel.Geometry.SpatialTrees](N_Grasshopper_Kernel_Geometry_SpatialTrees.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public sealed class Node3d<T>
```

```
Public NotInheritable Class Node3d(Of T)
```

AddLanguageTabSet("ID1EBCA");

#### Type Parameters

T

The Node3dAddLanguageSpecificTextSet("LSTD882787F\_6?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTD882787F\_7?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;"); type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [Node3dAddLanguageSpecificTextSet("LSTD882787F\_8?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTD882787F\_9?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");(Coordinates3dAddLanguageSpecificTextSet("LSTD882787F\_10?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTD882787F\_11?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");, BoundingBox)](M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1__ctor.htm) | Create a new spatial tree root. |
| Public method | [Node3dAddLanguageSpecificTextSet("LSTD882787F\_12?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTD882787F\_13?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");(Coordinates3dAddLanguageSpecificTextSet("LSTD882787F\_14?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTD882787F\_15?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");, BoundingBox, Int32)](M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1__ctor_1.htm) | Create a new spatial tree root. |

[Top](#PageHeader)

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

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [Add](M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_Add.htm) | Insert another item into the tree. The item should be within the region of this node. |
| Public method | [AddRange](M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_AddRange.htm) | Insert a collection of items into the tree. The items should all be within the region of this node. |
| Public method | [AddToRhinoDocument](M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_AddToRhinoDocument.htm) |  |
| Public method | [CollapseNodes](M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_CollapseNodes.htm) | Collapse the (sub)tree rooted at this node. Collapsing happens when a node only has a single child, in which case the child usurps the position previously held by the parent. Do not collapse a (sub)tree if you still plan to add items later. |
| Public method | [FurthestItem(T)](M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_FurthestItem_4.htm) | Find the furtest item. |
| Public method | [FurthestItem(Point3d)](M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_FurthestItem.htm) | Find the furtest item. |
| Public method | [FurthestItem(Double, Double, Double)](M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_FurthestItem_2.htm) | Find the furtest item. |
| Public method | [FurthestItem(T, Double, Double)](M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_FurthestItem_5.htm) | Find the furtest item. |
| Public method | [FurthestItem(Point3d, Double, Double)](M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_FurthestItem_1.htm) | Find the furtest item. |
| Public method | [FurthestItem(Double, Double, Double, Double, Double)](M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_FurthestItem_3.htm) | Find the furtest item. |
| Public method | [NearestItem(T)](M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_NearestItem_5.htm) | Find the nearest item. |
| Public method | [NearestItem(Point3d)](M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_NearestItem.htm) | Find the nearest item. |
| Public method | [NearestItem(Double, Double, Double)](M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_NearestItem_2.htm) | Find the nearest item. |
| Public method | [NearestItem(T, Double, Double)](M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_NearestItem_6.htm) | Find the nearest item. |
| Public method | [NearestItem(Point3d, Double, Double)](M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_NearestItem_1.htm) | Find the nearest item. |
| Public method | [NearestItem(Double, Double, Double, Validation3dAddLanguageSpecificTextSet("LSTD882787F\_16?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTD882787F\_17?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");)](M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_NearestItem_3.htm) | Find the nearest item using custom validation criteria. |
| Public method | [NearestItem(Double, Double, Double, Double, Double)](M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_NearestItem_4.htm) | Find the nearest item. |
| Public method | [NearestItems(T, Int32)](M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_NearestItems_2.htm) | Find the N nearest items. |
| Public method | [NearestItems(Double, Double, Double, Int32)](M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_NearestItems.htm) | Find the N nearest items. |
| Public method | [NearestItems(T, Int32, Double, Double)](M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_NearestItems_3.htm) | Find the N nearest items. |
| Public method | [NearestItems(Double, Double, Double, Int32, Double, Double)](M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_NearestItems_1.htm) | Find the N nearest items. |
| Public method | [OptimizeTree](M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_OptimizeTree.htm) | Optimize this tree for fast searches. Do not call this method if you still plan to add items in the future. You can no longer modify this tree once it has been optimized. |
| Public method | [Remove(Index3dAddLanguageSpecificTextSet("LSTD882787F\_18?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTD882787F\_19?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");)](M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_Remove.htm) | Remove the item with the given index from the entire tree. It doesn't matter on which node you call this function, it is a tree-wide operation. |
| Public method | [Remove(Int32)](M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_Remove_1.htm) | Remove the item with the given index from the entire tree. It doesn't matter on which node you call this function, it is a tree-wide operation. |
| Public method | [ShrinkRegions](M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_ShrinkRegions.htm) | Shrink the region for this node and all child nodes. Do not use this method if you intend to add more items later as it creates spatial gaps in the tree structure. You can shrink nodes if you're done adding items and want to start searching the tree. |
| Public method | [SubTree](M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_SubTree.htm) | Gets an iterator for all nodes in this (sub)tree. |
| Public method | [TrimExcess](M_Grasshopper_Kernel_Geometry_SpatialTrees_Node3d_1_TrimExcess.htm) | Trim the excess space on all index lists. You can call this method to reduce memory usage. It will not modify the tree in any functional way. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Geometry.SpatialTrees Namespace](N_Grasshopper_Kernel_Geometry_SpatialTrees.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)