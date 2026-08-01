# Properties_T_Grasshopper_Kernel_Data_GH_Structure_1

﻿ GH\_Structure(T) Properties

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Data](../html/N_Grasshopper_Kernel_Data.htm "Grasshopper.Kernel.Data")

[GH\_Structure(T) Class](../html/T_Grasshopper_Kernel_Data_GH_Structure_1.htm "GH_Structure(T) Class")

[GH\_Structure(T) Properties](../html/Properties_T_Grasshopper_Kernel_Data_GH_Structure_1.htm "GH_Structure(T) Properties")

[Branch Property](../html/Overload_Grasshopper_Kernel_Data_GH_Structure_1_Branch.htm "Branch Property ")

[Branches Property](../html/P_Grasshopper_Kernel_Data_GH_Structure_1_Branches.htm "Branches Property ")

[DataCount Property](../html/P_Grasshopper_Kernel_Data_GH_Structure_1_DataCount.htm "DataCount Property ")

[DataItem Property](../html/Overload_Grasshopper_Kernel_Data_GH_Structure_1_DataItem.htm "DataItem Property ")

[DataList Property](../html/Overload_Grasshopper_Kernel_Data_GH_Structure_1_DataList.htm "DataList Property ")

[FirstItem Property](../html/P_Grasshopper_Kernel_Data_GH_Structure_1_FirstItem.htm "FirstItem Property ")

[IsEmpty Property](../html/P_Grasshopper_Kernel_Data_GH_Structure_1_IsEmpty.htm "IsEmpty Property ")

[LastItem Property](../html/P_Grasshopper_Kernel_Data_GH_Structure_1_LastItem.htm "LastItem Property ")

[NonNulls Property](../html/P_Grasshopper_Kernel_Data_GH_Structure_1_NonNulls.htm "NonNulls Property ")

[Path Property](../html/P_Grasshopper_Kernel_Data_GH_Structure_1_Path.htm "Path Property ")

[PathCount Property](../html/P_Grasshopper_Kernel_Data_GH_Structure_1_PathCount.htm "PathCount Property ")

[Paths Property](../html/P_Grasshopper_Kernel_Data_GH_Structure_1_Paths.htm "Paths Property ")

[StructureProxy Property](../html/P_Grasshopper_Kernel_Data_GH_Structure_1_StructureProxy.htm "StructureProxy Property ")

[TopologyDescription Property](../html/P_Grasshopper_Kernel_Data_GH_Structure_1_TopologyDescription.htm "TopologyDescription Property ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_StructureAddLanguageSpecificTextSet("LSTC2B20A74\_0?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTC2B20A74\_1?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)"); Properties |

The [GH\_StructureAddLanguageSpecificTextSet("LSTC2B20A74\_2?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTC2B20A74\_3?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");](T_Grasshopper_Kernel_Data_GH_Structure_1.htm) generic type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [BranchAddLanguageSpecificTextSet("LSTC2B20A74\_4?cs=[|vb=(|cpp=[|nu=(|fs= ");GH\_PathAddLanguageSpecificTextSet("LSTC2B20A74\_5?cs=]|vb=)|cpp=]|nu=)|fs= ");](P_Grasshopper_Kernel_Data_GH_Structure_1_Branch.htm) | Gets a limited access pointer to the data list associated with a certain path. |
| Public property | [BranchAddLanguageSpecificTextSet("LSTC2B20A74\_6?cs=[|vb=(|cpp=[|nu=(|fs= ");Int32AddLanguageSpecificTextSet("LSTC2B20A74\_7?cs=]|vb=)|cpp=]|nu=)|fs= ");](P_Grasshopper_Kernel_Data_GH_Structure_1_Branch_1.htm) | Gets a limited access pointer to the data list at the specified index |
| Public property | [Branches](P_Grasshopper_Kernel_Data_GH_Structure_1_Branches.htm) | Gets a list of all the data-arrays in this structure |
| Public property | [DataCount](P_Grasshopper_Kernel_Data_GH_Structure_1_DataCount.htm) | Gets the total number of data items stored in all paths. |
| Public property | [DataItemAddLanguageSpecificTextSet("LSTC2B20A74\_8?cs=[|vb=(|cpp=[|nu=(|fs= ");Int32AddLanguageSpecificTextSet("LSTC2B20A74\_9?cs=]|vb=)|cpp=]|nu=)|fs= ");](P_Grasshopper_Kernel_Data_GH_Structure_1_DataItem_1.htm) | Gets the item at a given offset. The structure is treated as a linear list in this case. If index is out of range, null is returned. For repeated indexed retrieval, consider using a For Each loop since the enumerator is more efficient. |
| Public property | [DataItemAddLanguageSpecificTextSet("LSTC2B20A74\_10?cs=[|vb=(|cpp=[|nu=(|fs= ");GH\_Path, Int32AddLanguageSpecificTextSet("LSTC2B20A74\_11?cs=]|vb=)|cpp=]|nu=)|fs= ");](P_Grasshopper_Kernel_Data_GH_Structure_1_DataItem.htm) | Gets a direct pointer to a data item under a specific path and index. |
| Public property | [DataListAddLanguageSpecificTextSet("LSTC2B20A74\_12?cs=[|vb=(|cpp=[|nu=(|fs= ");GH\_PathAddLanguageSpecificTextSet("LSTC2B20A74\_13?cs=]|vb=)|cpp=]|nu=)|fs= ");](P_Grasshopper_Kernel_Data_GH_Structure_1_DataList.htm) | Gets a direct pointer to the list of data under a specific path. |
| Public property | [DataListAddLanguageSpecificTextSet("LSTC2B20A74\_14?cs=[|vb=(|cpp=[|nu=(|fs= ");Int32AddLanguageSpecificTextSet("LSTC2B20A74\_15?cs=]|vb=)|cpp=]|nu=)|fs= ");](P_Grasshopper_Kernel_Data_GH_Structure_1_DataList_1.htm) | Gets a direct pointer to the list of data under the specified index. |
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

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_StructureAddLanguageSpecificTextSet("LSTC2B20A74\_16?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTC2B20A74\_17?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;"); Class](T_Grasshopper_Kernel_Data_GH_Structure_1.htm)

[Grasshopper.Kernel.Data Namespace](N_Grasshopper_Kernel_Data.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)