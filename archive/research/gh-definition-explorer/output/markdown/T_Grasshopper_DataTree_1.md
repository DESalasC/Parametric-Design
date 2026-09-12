# T_Grasshopper_DataTree_1

﻿ DataTree(T) Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper](../html/N_Grasshopper.htm "Grasshopper")

[DataTree(T) Class](../html/T_Grasshopper_DataTree_1.htm "DataTree(T) Class")

[DataTree(T) Constructor](../html/Overload_Grasshopper_DataTree_1__ctor.htm "DataTree(T) Constructor ")

[DataTree(T) Properties](../html/Properties_T_Grasshopper_DataTree_1.htm "DataTree(T) Properties")

[DataTree(T) Methods](../html/Methods_T_Grasshopper_DataTree_1.htm "DataTree(T) Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| DataTreeAddLanguageSpecificTextSet("LSTE990EC6F\_0?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTE990EC6F\_1?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)"); Class |

Implements basic Grasshopper Data Tree functionality in an easy-to-use class.
This class is used primarily in Scripting components. If you're using the Grasshopper
SDK you should consider using the [GH\_StructureAddLanguageSpecificTextSet("LSTE990EC6F\_2?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTE990EC6F\_3?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Data_GH_Structure_1.htm) class instead.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LSTE990EC6F\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  GrasshopperAddLanguageSpecificTextSet("LSTE990EC6F\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");DataTreeAddLanguageSpecificTextSet("LSTE990EC6F\_6?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTE990EC6F\_7?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");

**Namespace:**
 [Grasshopper](N_Grasshopper.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class DataTree<T> : IGH_DataTree
```

```
Public Class DataTree(Of T)
	Implements IGH_DataTree
```

AddLanguageTabSet("ID1EBCA");

#### Type Parameters

T
:   Data type of this class.

The DataTreeAddLanguageSpecificTextSet("LSTE990EC6F\_8?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTE990EC6F\_9?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;"); type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [DataTreeAddLanguageSpecificTextSet("LSTE990EC6F\_10?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTE990EC6F\_11?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTE990EC6F\_12?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_DataTree_1__ctor.htm) | Default constructor, create an empty data tree. |
| Public method | [DataTreeAddLanguageSpecificTextSet("LSTE990EC6F\_13?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTE990EC6F\_14?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");(DataTreeAddLanguageSpecificTextSet("LSTE990EC6F\_15?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTE990EC6F\_16?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");)](M_Grasshopper_DataTree_1__ctor_1.htm) | Create a shallow duplicate of another data tree. This means it will create a new tree that contains the same items. |
| Public method | [DataTreeAddLanguageSpecificTextSet("LSTE990EC6F\_17?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTE990EC6F\_18?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");(DataTreeAddLanguageSpecificTextSet("LSTE990EC6F\_19?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTE990EC6F\_20?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");, DataTreeAddLanguageSpecificTextSet("LSTE990EC6F\_21?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTE990EC6F\_22?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");AddLanguageSpecificTextSet("LSTE990EC6F\_23?cs=.|vb=.|cpp=::|nu=.|fs=.");DuplicateT)](M_Grasshopper_DataTree_1__ctor_2.htm) | Create a true duplicate of another data tree. |
| Public method | [DataTreeAddLanguageSpecificTextSet("LSTE990EC6F\_24?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTE990EC6F\_25?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");(IEnumerableAddLanguageSpecificTextSet("LSTE990EC6F\_26?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTE990EC6F\_27?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");, GH\_Path)](M_Grasshopper_DataTree_1__ctor_3.htm) | Create a tree with a single branch |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [BranchCount](P_Grasshopper_DataTree_1_BranchCount.htm) | Gets the number of branches defined in this tree. |
| Public property | [Branches](P_Grasshopper_DataTree_1_Branches.htm) | Gets a list of all the data-arrays in this tree |
| Public property | [DataCount](P_Grasshopper_DataTree_1_DataCount.htm) | Gets the total number of data items (including nulls) stored in all branches. |
| Public property | [Item](P_Grasshopper_DataTree_1_Item.htm) | Gets or set the data item at the specified path and index. |
| Public property | [Paths](P_Grasshopper_DataTree_1_Paths.htm) | Gets a list of all the branch paths in this tree. |
| Public property | [TopologyDescription](P_Grasshopper_DataTree_1_TopologyDescription.htm) | Gets a description of the topology of the tree. Useful for debugging purposes. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [Add(T)](M_Grasshopper_DataTree_1_Add.htm) | Add (append) a data item to the last branch in the tree. If no branches exist yet, a new one will be created with [path = {0}] |
| Public method | [Add(T, GH\_Path)](M_Grasshopper_DataTree_1_Add_1.htm) | Add (append) a data item to the specified branch in the tree. If the branch doesn't exist yet, it will be created. |
| Public method | [AddRange(IEnumerableAddLanguageSpecificTextSet("LSTE990EC6F\_28?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTE990EC6F\_29?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");)](M_Grasshopper_DataTree_1_AddRange.htm) | Add (append) a list of data items to the last branch in the tree. If no branch exists yet, a new one will be created. |
| Public method | [AddRange(IEnumerableAddLanguageSpecificTextSet("LSTE990EC6F\_30?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTE990EC6F\_31?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");, GH\_Path)](M_Grasshopper_DataTree_1_AddRange_1.htm) | Add (append) a list of data items to the specified branch in the tree. If the branch doesn't exist yet, it will be created. |
| Public method | [AllData](M_Grasshopper_DataTree_1_AllData.htm) | Collects all data in the tree in a single list. Does not alter the topology of this tree. |
| Public method | [Branch(GH\_Path)](M_Grasshopper_DataTree_1_Branch.htm) | Gets the list of data which belongs to a given Branch path. |
| Public method | [Branch(Int32)](M_Grasshopper_DataTree_1_Branch_1.htm) | Gets the list of data which belongs to the branch path at the given index. |
| Public method | [Branch(AddLanguageSpecificTextSet("LSTE990EC6F\_32?cpp=array&lt;");Int32AddLanguageSpecificTextSet("LSTE990EC6F\_33?cpp=&gt;|cs=[]|vb=()|nu=[]|fs=[]");)](M_Grasshopper_DataTree_1_Branch_2.htm) | Gets the list of data which belongs to a given Branch path. |
| Public method | [Clear](M_Grasshopper_DataTree_1_Clear.htm) | Clears the entire tree. |
| Public method | [ClearData](M_Grasshopper_DataTree_1_ClearData.htm) | Removes all data from all branches without affecting the tree topology. |
| Public method | [EnsurePath(GH\_Path)](M_Grasshopper_DataTree_1_EnsurePath.htm) | Create a new branch with the specified path if it doesn't already exists. |
| Public method | [EnsurePath(AddLanguageSpecificTextSet("LSTE990EC6F\_34?cpp=array&lt;");Int32AddLanguageSpecificTextSet("LSTE990EC6F\_35?cpp=&gt;|cs=[]|vb=()|nu=[]|fs=[]");)](M_Grasshopper_DataTree_1_EnsurePath_1.htm) | Create a new branch with the specified path if it doesn't already exists. |
| Public method | [Flatten](M_Grasshopper_DataTree_1_Flatten.htm) | Flattens the entire tree into a single path. |
| Public method | [Graft(Boolean)](M_Grasshopper_DataTree_1_Graft_1.htm) | Graft all paths in this tree. "Grafting" means appending a new branch for every item in an existing branch. |
| Public method | [Graft(GH\_Path, Boolean)](M_Grasshopper_DataTree_1_Graft.htm) | Graft a single path in the tree. "Grafting" means appending a new branch for every item in an existing branch. |
| Public method | [Insert](M_Grasshopper_DataTree_1_Insert.htm) | Insert a data item to the specified branch in the tree. If the branch doesn't exist yet, it will be created. |
| Public method | [ItemExists](M_Grasshopper_DataTree_1_ItemExists.htm) | Test if the specified path + item index are defined inside the tree. |
| Public method | [MergeTree](M_Grasshopper_DataTree_1_MergeTree.htm) | Merges two trees together. Data inside similar branches will be merged into single lists and unique paths will be appended. The other tree will not be altered, so beware that data is now shared among both trees. |
| Public method | [Path](M_Grasshopper_DataTree_1_Path.htm) | Gets the data path at the specified index. |
| Public method | [PathExists(GH\_Path)](M_Grasshopper_DataTree_1_PathExists.htm) | Test if the specified path is already defined inside the tree. |
| Public method | [PathExists(AddLanguageSpecificTextSet("LSTE990EC6F\_36?cpp=array&lt;");Int32AddLanguageSpecificTextSet("LSTE990EC6F\_37?cpp=&gt;|cs=[]|vb=()|nu=[]|fs=[]");)](M_Grasshopper_DataTree_1_PathExists_1.htm) | Test if the specified path is already defined inside the tree. |
| Public method | [RemovePath(GH\_Path)](M_Grasshopper_DataTree_1_RemovePath.htm) | Removes a path and all associated data from the structure. If the path doesn't exist, nothing will happen. |
| Public method | [RemovePath(AddLanguageSpecificTextSet("LSTE990EC6F\_38?cpp=array&lt;");Int32AddLanguageSpecificTextSet("LSTE990EC6F\_39?cpp=&gt;|cs=[]|vb=()|nu=[]|fs=[]");)](M_Grasshopper_DataTree_1_RemovePath_1.htm) | Removes a path and all associated data from the structure. If the path doesn't exist, nothing will happen. |
| Public method | [RenumberPathsAddLanguageSpecificTextSet("LSTE990EC6F\_40?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_DataTree_1_RenumberPaths.htm) | Renumber all paths in this data tree, using a single incrementing path index. |
| Public method | [RenumberPaths(String)](M_Grasshopper_DataTree_1_RenumberPaths_1.htm) | Renumber all paths in this data tree, using a single incrementing path index. |
| Public method | [SimplifyPaths](M_Grasshopper_DataTree_1_SimplifyPaths.htm) | Simplify the branches in this tree by removing all identical path entries. The length of the shortest path will be indicative of the similarity search depth. If this tree only contains a single branch, the branch wil be simplified to its last index. |
| Public method | [ToString](M_Grasshopper_DataTree_1_ToString.htm) | Creates a brief description of the tree. (Overrides [ObjectAddLanguageSpecificTextSet("LSTE990EC6F\_41?cs=.|vb=.|cpp=::|nu=.|fs=.");ToStringAddLanguageSpecificTextSet("LSTE990EC6F\_42?cs=()|vb=|cpp=()|nu=()|fs=()");](https://docs.microsoft.com/dotnet/api/system.object.tostring#system-object-tostring).) |
| Public method | [TrimExcess](M_Grasshopper_DataTree_1_TrimExcess.htm) | Trims the excess allocated memory in all branches |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper Namespace](N_Grasshopper.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)