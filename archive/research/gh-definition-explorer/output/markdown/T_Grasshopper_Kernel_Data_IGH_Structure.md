# T_Grasshopper_Kernel_Data_IGH_Structure

﻿ IGH\_Structure Interface

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Data](../html/N_Grasshopper_Kernel_Data.htm "Grasshopper.Kernel.Data")

[IGH\_Structure Interface](../html/T_Grasshopper_Kernel_Data_IGH_Structure.htm "IGH_Structure Interface")

[IGH\_Structure Properties](../html/Properties_T_Grasshopper_Kernel_Data_IGH_Structure.htm "IGH_Structure Properties")

[IGH\_Structure Methods](../html/Methods_T_Grasshopper_Kernel_Data_IGH_Structure.htm "IGH_Structure Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_Structure Interface |

Base interface for all GH\_Structure types.

**Namespace:**
 [Grasshopper.Kernel.Data](N_Grasshopper_Kernel_Data.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public interface IGH_Structure
```

```
Public Interface IGH_Structure
```

AddLanguageTabSet("ID0EBCA");

The IGH\_Structure type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [BranchAddLanguageSpecificTextSet("LST9ECA0457\_0?cs=[|vb=(|cpp=[|nu=(|fs= ");GH\_PathAddLanguageSpecificTextSet("LST9ECA0457\_1?cs=]|vb=)|cpp=]|nu=)|fs= ");](P_Grasshopper_Kernel_Data_IGH_Structure_Branch.htm) | Gets a limited access pointer to the data list associated with a certain path. |
| Public property | [BranchAddLanguageSpecificTextSet("LST9ECA0457\_2?cs=[|vb=(|cpp=[|nu=(|fs= ");Int32AddLanguageSpecificTextSet("LST9ECA0457\_3?cs=]|vb=)|cpp=]|nu=)|fs= ");](P_Grasshopper_Kernel_Data_IGH_Structure_Branch_1.htm) | Gets a limited access pointer to the data list at the specified index. |
| Public property | [DataCount](P_Grasshopper_Kernel_Data_IGH_Structure_DataCount.htm) | Gets the total number of data items stored in all paths. |
| Public property | [IsEmpty](P_Grasshopper_Kernel_Data_IGH_Structure_IsEmpty.htm) | Gets the Empty state of the structure. If the structure is Empty when it contains no paths and no branches. |
| Public property | [Path](P_Grasshopper_Kernel_Data_IGH_Structure_Path.htm) | Gets the data path at the specified index. |
| Public property | [PathCount](P_Grasshopper_Kernel_Data_IGH_Structure_PathCount.htm) | Gets the number of paths defined in this structure. |
| Public property | [Paths](P_Grasshopper_Kernel_Data_IGH_Structure_Paths.htm) | Gets a list of all the paths in this structure. |
| Public property | [StructureProxy](P_Grasshopper_Kernel_Data_IGH_Structure_StructureProxy.htm) | Gets a proxy list of all the data-arrays in this structure |
| Public property | [TopologyDescription](P_Grasshopper_Kernel_Data_IGH_Structure_TopologyDescription.htm) | Gets a description of the topology of the structure. Useful for debugging purposes. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [AllData](M_Grasshopper_Kernel_Data_IGH_Structure_AllData.htm) | Gets an enumerator for all the data items in this structure. |
| Public method | [Clear](M_Grasshopper_Kernel_Data_IGH_Structure_Clear.htm) | Clears the entire structure. |
| Public method | [ClearData](M_Grasshopper_Kernel_Data_IGH_Structure_ClearData.htm) | Removes all data from all paths without affecting the structure topology. |
| Public method | [DataDescription](M_Grasshopper_Kernel_Data_IGH_Structure_DataDescription.htm) | Gets a description of the data contained in this structure. |
| Public method | [EnsureCapacity](M_Grasshopper_Kernel_Data_IGH_Structure_EnsureCapacity.htm) | Ensures that all branches have a certain capacity |
| Public method | [ExpandPath](M_Grasshopper_Kernel_Data_IGH_Structure_ExpandPath.htm) | Expand a path in this structure by appending an element. |
| Public method | [Flatten](M_Grasshopper_Kernel_Data_IGH_Structure_Flatten.htm) | Flattens the entire structure into a single path. |
| Public method | [Graft(GH\_GraftMode)](M_Grasshopper_Kernel_Data_IGH_Structure_Graft.htm) | Grafts all paths by reallocating all data into child paths. |
| Public method | [Graft(GH\_GraftMode, GH\_Path)](M_Grasshopper_Kernel_Data_IGH_Structure_Graft_1.htm) | Grafts a specific path by reallocating all data into child paths. If a grafted path coincides with an existing path, the data item in question will be appended to the existing path. |
| Public method | [LongestPathIndex](M_Grasshopper_Kernel_Data_IGH_Structure_LongestPathIndex.htm) | Finds the path in this structure with the most dimensions. In case of multiple equally long longest paths, the last one will be returned. |
| Public method | [PathExists](M_Grasshopper_Kernel_Data_IGH_Structure_PathExists.htm) | Returns True if the specified path is already defined inside the structure. |
| Public method | [PathIndex](M_Grasshopper_Kernel_Data_IGH_Structure_PathIndex.htm) | Find the indices that delineate the given path domain. |
| Public method | [RemovePath](M_Grasshopper_Kernel_Data_IGH_Structure_RemovePath.htm) | Removes a path and all associated data from the structure. If the path doesn't exist, nothing will happen. |
| Public method | [ReplacePath](M_Grasshopper_Kernel_Data_IGH_Structure_ReplacePath.htm) | Replace an existing path with a different one. If the operation is successfull, then the 'find' path will be deleted. If the 'replace' path is already defined, the items in 'find' will be appended to the existing path. |
| Public method | [ShortestPathIndex](M_Grasshopper_Kernel_Data_IGH_Structure_ShortestPathIndex.htm) | Finds the path in this structure with the least dimensions. In case of multiple equally long longest paths, the first one will be returned. |
| Public method | [Simplify](M_Grasshopper_Kernel_Data_IGH_Structure_Simplify.htm) | Simplify the data structure by removing path indices shared by all branches. |
| Public method | [TrimExcess](M_Grasshopper_Kernel_Data_IGH_Structure_TrimExcess.htm) | Trims the excess allocated memory in all branches |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Data Namespace](N_Grasshopper_Kernel_Data.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)