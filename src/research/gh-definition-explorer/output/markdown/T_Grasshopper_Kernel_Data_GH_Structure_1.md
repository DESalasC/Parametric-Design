# T_Grasshopper_Kernel_Data_GH_Structure_1

﻿ GH\_Structure(T) Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Data](../html/N_Grasshopper_Kernel_Data.htm "Grasshopper.Kernel.Data")

[GH\_Structure(T) Class](../html/T_Grasshopper_Kernel_Data_GH_Structure_1.htm "GH_Structure(T) Class")

[GH\_Structure(T) Constructor](../html/Overload_Grasshopper_Kernel_Data_GH_Structure_1__ctor.htm "GH_Structure(T) Constructor ")

[GH\_Structure(T) Properties](../html/Properties_T_Grasshopper_Kernel_Data_GH_Structure_1.htm "GH_Structure(T) Properties")

[GH\_Structure(T) Methods](../html/Methods_T_Grasshopper_Kernel_Data_GH_Structure_1.htm "GH_Structure(T) Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_StructureAddLanguageSpecificTextSet("LST7ECFC46\_0?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST7ECFC46\_1?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)"); Class |

Represents a data tree where each branch has a unique path

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST7ECFC46\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.Kernel.DataAddLanguageSpecificTextSet("LST7ECFC46\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_StructureAddLanguageSpecificTextSet("LST7ECFC46\_4?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST7ECFC46\_5?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");

**Namespace:**
 [Grasshopper.Kernel.Data](N_Grasshopper_Kernel_Data.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_Structure<T> : IGH_Structure, 
	IEnumerable<T>, GH_ISerializable
where T : IGH_Goo
```

```
Public Class GH_Structure(Of T As IGH_Goo)
	Implements IGH_Structure, IEnumerable(Of T), GH_ISerializable
```

AddLanguageTabSet("ID1EBCA");

#### Type Parameters

T
:   The data type that this structure maintains. Must implement IGH\_Goo or derive from a class that implements IGH\_Goo.

The GH\_StructureAddLanguageSpecificTextSet("LST7ECFC46\_6?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST7ECFC46\_7?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;"); type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_StructureAddLanguageSpecificTextSet("LST7ECFC46\_8?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST7ECFC46\_9?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LST7ECFC46\_10?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_Kernel_Data_GH_Structure_1__ctor.htm) | Default constructor, create a blank data structure. |
| Public method | [GH\_StructureAddLanguageSpecificTextSet("LST7ECFC46\_11?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST7ECFC46\_12?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");(GH\_StructureAddLanguageSpecificTextSet("LST7ECFC46\_13?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST7ECFC46\_14?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");, Boolean)](M_Grasshopper_Kernel_Data_GH_Structure_1__ctor_1.htm) | Copy constructor, duplicate another data structure. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [BranchAddLanguageSpecificTextSet("LST7ECFC46\_15?cs=[|vb=(|cpp=[|nu=(|fs= ");GH\_PathAddLanguageSpecificTextSet("LST7ECFC46\_16?cs=]|vb=)|cpp=]|nu=)|fs= ");](P_Grasshopper_Kernel_Data_GH_Structure_1_Branch.htm) | Gets a limited access pointer to the data list associated with a certain path. |
| Public property | [BranchAddLanguageSpecificTextSet("LST7ECFC46\_17?cs=[|vb=(|cpp=[|nu=(|fs= ");Int32AddLanguageSpecificTextSet("LST7ECFC46\_18?cs=]|vb=)|cpp=]|nu=)|fs= ");](P_Grasshopper_Kernel_Data_GH_Structure_1_Branch_1.htm) | Gets a limited access pointer to the data list at the specified index |
| Public property | [Branches](P_Grasshopper_Kernel_Data_GH_Structure_1_Branches.htm) | Gets a list of all the data-arrays in this structure |
| Public property | [DataCount](P_Grasshopper_Kernel_Data_GH_Structure_1_DataCount.htm) | Gets the total number of data items stored in all paths. |
| Public property | [DataItemAddLanguageSpecificTextSet("LST7ECFC46\_19?cs=[|vb=(|cpp=[|nu=(|fs= ");Int32AddLanguageSpecificTextSet("LST7ECFC46\_20?cs=]|vb=)|cpp=]|nu=)|fs= ");](P_Grasshopper_Kernel_Data_GH_Structure_1_DataItem_1.htm) | Gets the item at a given offset. The structure is treated as a linear list in this case. If index is out of range, null is returned. For repeated indexed retrieval, consider using a For Each loop since the enumerator is more efficient. |
| Public property | [DataItemAddLanguageSpecificTextSet("LST7ECFC46\_21?cs=[|vb=(|cpp=[|nu=(|fs= ");GH\_Path, Int32AddLanguageSpecificTextSet("LST7ECFC46\_22?cs=]|vb=)|cpp=]|nu=)|fs= ");](P_Grasshopper_Kernel_Data_GH_Structure_1_DataItem.htm) | Gets a direct pointer to a data item under a specific path and index. |
| Public property | [DataListAddLanguageSpecificTextSet("LST7ECFC46\_23?cs=[|vb=(|cpp=[|nu=(|fs= ");GH\_PathAddLanguageSpecificTextSet("LST7ECFC46\_24?cs=]|vb=)|cpp=]|nu=)|fs= ");](P_Grasshopper_Kernel_Data_GH_Structure_1_DataList.htm) | Gets a direct pointer to the list of data under a specific path. |
| Public property | [DataListAddLanguageSpecificTextSet("LST7ECFC46\_25?cs=[|vb=(|cpp=[|nu=(|fs= ");Int32AddLanguageSpecificTextSet("LST7ECFC46\_26?cs=]|vb=)|cpp=]|nu=)|fs= ");](P_Grasshopper_Kernel_Data_GH_Structure_1_DataList_1.htm) | Gets a direct pointer to the list of data under the specified index. |
| Public property | [FirstItem](P_Grasshopper_Kernel_Data_GH_Structure_1_FirstItem.htm) | Gets the first item in the structure. If no such item exists, null is returned. |
| Public property | [IsEmpty](P_Grasshopper_Kernel_Data_GH_Structure_1_IsEmpty.htm) | Gets the Empty state of the structure. If the structure is Empty it contains no paths and no branches. |
| Public property | [LastItem](P_Grasshopper_Kernel_Data_GH_Structure_1_LastItem.htm) | Gets the last item in the structure. If no such item exists, null is returned. |
| Public property | [NonNulls](P_Grasshopper_Kernel_Data_GH_Structure_1_NonNulls.htm) | Get an enumerator for this structure that allow linear iteration over the data hierarchy while skipping all Null entries. This Enumerator has been optimized, do not cache instances of it. |
| Public property | [Path](P_Grasshopper_Kernel_Data_GH_Structure_1_Path.htm) | Gets the data path at the specified index. |
| Public property | [PathCount](P_Grasshopper_Kernel_Data_GH_Structure_1_PathCount.htm) | Gets the number of paths defined in this structure. |
| Public property | [Paths](P_Grasshopper_Kernel_Data_GH_Structure_1_Paths.htm) | Gets a list of all the paths in this structure. |
| Public property | [StructureProxy](P_Grasshopper_Kernel_Data_GH_Structure_1_StructureProxy.htm) | Gets a proxy list of all the data-arrays in this structure. |
| Public property | [TopologyDescription](P_Grasshopper_Kernel_Data_GH_Structure_1_TopologyDescription.htm) | Gets a description of the topology of the structure. Useful for debugging purposes. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [AllData](M_Grasshopper_Kernel_Data_GH_Structure_1_AllData.htm) | Gets an enumerator for all the data items in this structure. |
| Public method | [Append(T)](M_Grasshopper_Kernel_Data_GH_Structure_1_Append.htm) | Append a data item to the last branch in the structure. If no branch exist yet, a new one will be created with [path = {0}] |
| Public method | [Append(T, GH\_Path)](M_Grasshopper_Kernel_Data_GH_Structure_1_Append_1.htm) | Append a data item to the specified branch in the structure. If the branch doesn't exist yet, it will be created. |
| Public method | [AppendRange(IEnumerableAddLanguageSpecificTextSet("LST7ECFC46\_27?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST7ECFC46\_28?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");)](M_Grasshopper_Kernel_Data_GH_Structure_1_AppendRange.htm) | Append a list of data items to the last branch in the structure |
| Public method | [AppendRange(IEnumerableAddLanguageSpecificTextSet("LST7ECFC46\_29?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST7ECFC46\_30?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");, GH\_Path)](M_Grasshopper_Kernel_Data_GH_Structure_1_AppendRange_1.htm) | Append a list of data items to the specified branch in the structure. If the branch doesn't exist yet, it will be created. |
| Public method | [Clear](M_Grasshopper_Kernel_Data_GH_Structure_1_Clear.htm) | Clears the entire structure. |
| Public method | [ClearData](M_Grasshopper_Kernel_Data_GH_Structure_1_ClearData.htm) | Removes all data from all paths without affecting the structure topology. |
| Public method | [DataDescription](M_Grasshopper_Kernel_Data_GH_Structure_1_DataDescription.htm) | Gets a description of the data contained in this structure. |
| Public method | [Duplicate](M_Grasshopper_Kernel_Data_GH_Structure_1_Duplicate.htm) | Create an exact duplicate of this structure. All data items are copied as well. |
| Public method | [DuplicateCastAddLanguageSpecificTextSet("LST7ECFC46\_31?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");QAddLanguageSpecificTextSet("LST7ECFC46\_32?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");](M_Grasshopper_Kernel_Data_GH_Structure_1_DuplicateCast__1.htm) | Create a duplicate of this structure in a different type. |
| Public method | [EnsureCapacity](M_Grasshopper_Kernel_Data_GH_Structure_1_EnsureCapacity.htm) | Ensures that all current branches have a certain capacity. |
| Public method | [EnsurePath(GH\_Path)](M_Grasshopper_Kernel_Data_GH_Structure_1_EnsurePath.htm) | Create a new branch with the specified path if it doesn't already exists. |
| Public method | [EnsurePath(AddLanguageSpecificTextSet("LST7ECFC46\_33?cpp=array&lt;");Int32AddLanguageSpecificTextSet("LST7ECFC46\_34?cpp=&gt;|cs=[]|vb=()|nu=[]|fs=[]");)](M_Grasshopper_Kernel_Data_GH_Structure_1_EnsurePath_1.htm) | Create a new branch with the specified path if it doesn't already exists. |
| Public method | [ExpandPath](M_Grasshopper_Kernel_Data_GH_Structure_1_ExpandPath.htm) | Expand a path in this structure by appending an element. |
| Public method | [Flatten](M_Grasshopper_Kernel_Data_GH_Structure_1_Flatten.htm) | Flattens the entire structure into a single path. |
| Public method | [FlattenData](M_Grasshopper_Kernel_Data_GH_Structure_1_FlattenData.htm) | Collects all data in the structure under a single list. Does not alter the state of this structure. |
| Public method | [GetEnumerator](M_Grasshopper_Kernel_Data_GH_Structure_1_GetEnumerator.htm) |  |
| Public method | [GetEnumerator\_Generic](M_Grasshopper_Kernel_Data_GH_Structure_1_GetEnumerator_Generic.htm) |  |
| Public method | [Graft(GH\_GraftMode)](M_Grasshopper_Kernel_Data_GH_Structure_1_Graft.htm) | Grafts all paths by reallocating all data into child paths. |
| Public method | [Graft(GH\_GraftMode, GH\_Path)](M_Grasshopper_Kernel_Data_GH_Structure_1_Graft_1.htm) | Grafts a specific path by reallocating all data into child paths. If a grafted path coincides with an existing path, the data item in question will be appended to the existing path. |
| Public method | [Insert](M_Grasshopper_Kernel_Data_GH_Structure_1_Insert.htm) | Insert a data item into the specified branch in the structure. If the branch doesn't exist yet, it will be created. |
| Public method | [LongestPathIndex](M_Grasshopper_Kernel_Data_GH_Structure_1_LongestPathIndex.htm) | Finds the path in this structure with the most dimensions. In case of multiple equally long longest paths, the last one will be returned. |
| Public method | [MergeStructure](M_Grasshopper_Kernel_Data_GH_Structure_1_MergeStructure.htm) | Merges two structures together. Data inside similar paths will be merged into single lists and unique paths will be appended. The other structure will not be altered, so beware that data is now shared among both structures. |
| Public method | [PathExists](M_Grasshopper_Kernel_Data_GH_Structure_1_PathExists.htm) | Returns True if the specified path is already defined inside the structure. |
| Public method | [PathIndex](M_Grasshopper_Kernel_Data_GH_Structure_1_PathIndex.htm) | Find the indices that surround the given path domain. Indices may be out of bounds. |
| Public method | [Read](M_Grasshopper_Kernel_Data_GH_Structure_1_Read.htm) | Read the entire GH\_Structure from an archive. This method relies on the the serialization of the IGH\_Goo items it contains. Also, the IGH\_Goo T generic must have a public constructor that takes no arguments. |
| Public method | [RemoveData](M_Grasshopper_Kernel_Data_GH_Structure_1_RemoveData.htm) | Removes the first occurence of a data instance in the tree. |
| Public method | [RemovePath](M_Grasshopper_Kernel_Data_GH_Structure_1_RemovePath.htm) | Removes a path and all associated data from the structure. If the path doesn't exist, nothing will happen. |
| Public method | [ReplacePath](M_Grasshopper_Kernel_Data_GH_Structure_1_ReplacePath.htm) | Replace an existing path with a different one. If the operation is successfull, then the 'find' path will be deleted. If the 'replace' path is already defined, the items in 'find' will be appended to the existing path. |
| Public method | [Reverse](M_Grasshopper_Kernel_Data_GH_Structure_1_Reverse.htm) | Reverse the order of items in all branches. |
| Public method | [ShallowDuplicate](M_Grasshopper_Kernel_Data_GH_Structure_1_ShallowDuplicate.htm) | Create a structure with a similar topology to this one with pointers to the same data items. |
| Public method | [ShortestPathIndex](M_Grasshopper_Kernel_Data_GH_Structure_1_ShortestPathIndex.htm) | Finds the path in this structure with the least dimensions. In case of multiple equally long longest paths, the first one will be returned. |
| Public method | [Simplify](M_Grasshopper_Kernel_Data_GH_Structure_1_Simplify.htm) | Simplify the data structure by collapsing path indices shared by all branches. |
| Public method | [ToString](M_Grasshopper_Kernel_Data_GH_Structure_1_ToString.htm) | (Overrides [ObjectAddLanguageSpecificTextSet("LST7ECFC46\_35?cs=.|vb=.|cpp=::|nu=.|fs=.");ToStringAddLanguageSpecificTextSet("LST7ECFC46\_36?cs=()|vb=|cpp=()|nu=()|fs=()");](https://docs.microsoft.com/dotnet/api/system.object.tostring#system-object-tostring).) |
| Public method | [TrimExcess](M_Grasshopper_Kernel_Data_GH_Structure_1_TrimExcess.htm) | Trims the excess allocated memory in all branches. |
| Public method | [Write](M_Grasshopper_Kernel_Data_GH_Structure_1_Write.htm) | Write the entire GH\_Structure to an archive. This method relies on the the serialization of the IGH\_Goo items it contains. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Data Namespace](N_Grasshopper_Kernel_Data.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)