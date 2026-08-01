# Methods_T_Grasshopper_DataTree_1

﻿ DataTree(T) Methods

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper](../html/N_Grasshopper.htm "Grasshopper")

[DataTree(T) Class](../html/T_Grasshopper_DataTree_1.htm "DataTree(T) Class")

[DataTree(T) Methods](../html/Methods_T_Grasshopper_DataTree_1.htm "DataTree(T) Methods")

[Add Method](../html/Overload_Grasshopper_DataTree_1_Add.htm "Add Method ")

[AddRange Method](../html/Overload_Grasshopper_DataTree_1_AddRange.htm "AddRange Method ")

[AllData Method](../html/M_Grasshopper_DataTree_1_AllData.htm "AllData Method ")

[Branch Method](../html/Overload_Grasshopper_DataTree_1_Branch.htm "Branch Method ")

[Clear Method](../html/M_Grasshopper_DataTree_1_Clear.htm "Clear Method ")

[ClearData Method](../html/M_Grasshopper_DataTree_1_ClearData.htm "ClearData Method ")

[EnsurePath Method](../html/Overload_Grasshopper_DataTree_1_EnsurePath.htm "EnsurePath Method ")

[Flatten Method](../html/M_Grasshopper_DataTree_1_Flatten.htm "Flatten Method ")

[Graft Method](../html/Overload_Grasshopper_DataTree_1_Graft.htm "Graft Method ")

[Insert Method](../html/M_Grasshopper_DataTree_1_Insert.htm "Insert Method ")

[ItemExists Method](../html/M_Grasshopper_DataTree_1_ItemExists.htm "ItemExists Method ")

[MergeTree Method](../html/M_Grasshopper_DataTree_1_MergeTree.htm "MergeTree Method ")

[Path Method](../html/M_Grasshopper_DataTree_1_Path.htm "Path Method ")

[PathExists Method](../html/Overload_Grasshopper_DataTree_1_PathExists.htm "PathExists Method ")

[RemovePath Method](../html/Overload_Grasshopper_DataTree_1_RemovePath.htm "RemovePath Method ")

[RenumberPaths Method](../html/Overload_Grasshopper_DataTree_1_RenumberPaths.htm "RenumberPaths Method ")

[SimplifyPaths Method](../html/M_Grasshopper_DataTree_1_SimplifyPaths.htm "SimplifyPaths Method ")

[ToString Method](../html/M_Grasshopper_DataTree_1_ToString.htm "ToString Method ")

[TrimExcess Method](../html/M_Grasshopper_DataTree_1_TrimExcess.htm "TrimExcess Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| DataTreeAddLanguageSpecificTextSet("LSTE30A472C\_0?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTE30A472C\_1?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)"); Methods |

The [DataTreeAddLanguageSpecificTextSet("LSTE30A472C\_2?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTE30A472C\_3?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_DataTree_1.htm) generic type exposes the following members.

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [Add(T)](M_Grasshopper_DataTree_1_Add.htm) | Add (append) a data item to the last branch in the tree. If no branches exist yet, a new one will be created with [path = {0}] |
| Public method | [Add(T, GH\_Path)](M_Grasshopper_DataTree_1_Add_1.htm) | Add (append) a data item to the specified branch in the tree. If the branch doesn't exist yet, it will be created. |
| Public method | [AddRange(IEnumerableAddLanguageSpecificTextSet("LSTE30A472C\_4?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTE30A472C\_5?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");)](M_Grasshopper_DataTree_1_AddRange.htm) | Add (append) a list of data items to the last branch in the tree. If no branch exists yet, a new one will be created. |
| Public method | [AddRange(IEnumerableAddLanguageSpecificTextSet("LSTE30A472C\_6?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTE30A472C\_7?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");, GH\_Path)](M_Grasshopper_DataTree_1_AddRange_1.htm) | Add (append) a list of data items to the specified branch in the tree. If the branch doesn't exist yet, it will be created. |
| Public method | [AllData](M_Grasshopper_DataTree_1_AllData.htm) | Collects all data in the tree in a single list. Does not alter the topology of this tree. |
| Public method | [Branch(GH\_Path)](M_Grasshopper_DataTree_1_Branch.htm) | Gets the list of data which belongs to a given Branch path. |
| Public method | [Branch(Int32)](M_Grasshopper_DataTree_1_Branch_1.htm) | Gets the list of data which belongs to the branch path at the given index. |
| Public method | [Branch(AddLanguageSpecificTextSet("LSTE30A472C\_8?cpp=array&lt;");Int32AddLanguageSpecificTextSet("LSTE30A472C\_9?cpp=&gt;|cs=[]|vb=()|nu=[]|fs=[]");)](M_Grasshopper_DataTree_1_Branch_2.htm) | Gets the list of data which belongs to a given Branch path. |
| Public method | [Clear](M_Grasshopper_DataTree_1_Clear.htm) | Clears the entire tree. |
| Public method | [ClearData](M_Grasshopper_DataTree_1_ClearData.htm) | Removes all data from all branches without affecting the tree topology. |
| Public method | [EnsurePath(GH\_Path)](M_Grasshopper_DataTree_1_EnsurePath.htm) | Create a new branch with the specified path if it doesn't already exists. |
| Public method | [EnsurePath(AddLanguageSpecificTextSet("LSTE30A472C\_10?cpp=array&lt;");Int32AddLanguageSpecificTextSet("LSTE30A472C\_11?cpp=&gt;|cs=[]|vb=()|nu=[]|fs=[]");)](M_Grasshopper_DataTree_1_EnsurePath_1.htm) | Create a new branch with the specified path if it doesn't already exists. |
| Public method | [Flatten](M_Grasshopper_DataTree_1_Flatten.htm) | Flattens the entire tree into a single path. |
| Public method | [Graft(Boolean)](M_Grasshopper_DataTree_1_Graft_1.htm) | Graft all paths in this tree. "Grafting" means appending a new branch for every item in an existing branch. |
| Public method | [Graft(GH\_Path, Boolean)](M_Grasshopper_DataTree_1_Graft.htm) | Graft a single path in the tree. "Grafting" means appending a new branch for every item in an existing branch. |
| Public method | [Insert](M_Grasshopper_DataTree_1_Insert.htm) | Insert a data item to the specified branch in the tree. If the branch doesn't exist yet, it will be created. |
| Public method | [ItemExists](M_Grasshopper_DataTree_1_ItemExists.htm) | Test if the specified path + item index are defined inside the tree. |
| Public method | [MergeTree](M_Grasshopper_DataTree_1_MergeTree.htm) | Merges two trees together. Data inside similar branches will be merged into single lists and unique paths will be appended. The other tree will not be altered, so beware that data is now shared among both trees. |
| Public method | [Path](M_Grasshopper_DataTree_1_Path.htm) | Gets the data path at the specified index. |
| Public method | [PathExists(GH\_Path)](M_Grasshopper_DataTree_1_PathExists.htm) | Test if the specified path is already defined inside the tree. |
| Public method | [PathExists(AddLanguageSpecificTextSet("LSTE30A472C\_12?cpp=array&lt;");Int32AddLanguageSpecificTextSet("LSTE30A472C\_13?cpp=&gt;|cs=[]|vb=()|nu=[]|fs=[]");)](M_Grasshopper_DataTree_1_PathExists_1.htm) | Test if the specified path is already defined inside the tree. |
| Public method | [RemovePath(GH\_Path)](M_Grasshopper_DataTree_1_RemovePath.htm) | Removes a path and all associated data from the structure. If the path doesn't exist, nothing will happen. |
| Public method | [RemovePath(AddLanguageSpecificTextSet("LSTE30A472C\_14?cpp=array&lt;");Int32AddLanguageSpecificTextSet("LSTE30A472C\_15?cpp=&gt;|cs=[]|vb=()|nu=[]|fs=[]");)](M_Grasshopper_DataTree_1_RemovePath_1.htm) | Removes a path and all associated data from the structure. If the path doesn't exist, nothing will happen. |
| Public method | [RenumberPathsAddLanguageSpecificTextSet("LSTE30A472C\_16?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_DataTree_1_RenumberPaths.htm) | Renumber all paths in this data tree, using a single incrementing path index. |
| Public method | [RenumberPaths(String)](M_Grasshopper_DataTree_1_RenumberPaths_1.htm) | Renumber all paths in this data tree, using a single incrementing path index. |
| Public method | [SimplifyPaths](M_Grasshopper_DataTree_1_SimplifyPaths.htm) | Simplify the branches in this tree by removing all identical path entries. The length of the shortest path will be indicative of the similarity search depth. If this tree only contains a single branch, the branch wil be simplified to its last index. |
| Public method | [ToString](M_Grasshopper_DataTree_1_ToString.htm) | Creates a brief description of the tree. (Overrides [ObjectAddLanguageSpecificTextSet("LSTE30A472C\_17?cs=.|vb=.|cpp=::|nu=.|fs=.");ToStringAddLanguageSpecificTextSet("LSTE30A472C\_18?cs=()|vb=|cpp=()|nu=()|fs=()");](https://docs.microsoft.com/dotnet/api/system.object.tostring#system-object-tostring).) |
| Public method | [TrimExcess](M_Grasshopper_DataTree_1_TrimExcess.htm) | Trims the excess allocated memory in all branches |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[DataTreeAddLanguageSpecificTextSet("LSTE30A472C\_19?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTE30A472C\_20?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;"); Class](T_Grasshopper_DataTree_1.htm)

[Grasshopper Namespace](N_Grasshopper.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)