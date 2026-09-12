# M_Grasshopper_DataTree_1_Path

﻿ DataTree(T).Path Method 

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
| DataTreeAddLanguageSpecificTextSet("LST3471F36C\_0?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST3471F36C\_1?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");AddLanguageSpecificTextSet("LST3471F36C\_2?cpp=::|nu=.");Path Method |

Gets the data path at the specified index.

**Namespace:**
 [Grasshopper](N_Grasshopper.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public GH_Path Path(
	int index
)
```

```
Public Function Path ( 
	index As Integer
) As GH_Path
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

index
:   Type: [SystemAddLanguageSpecificTextSet("LST3471F36C\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Index of path to retrieve.

#### Return Value

Type: [GH\_Path](T_Grasshopper_Kernel_Data_GH_Path.htm)

![](../icons/SectionExpanded.png)Exceptions

| Exception | Condition |
| --- | --- |
| [IndexOutOfRangeException](https://docs.microsoft.com/dotnet/api/system.indexoutofrangeexception) | Thrown if the index does not represent a valid path. |

![](../icons/SectionExpanded.png)See Also

#### Reference

[DataTreeAddLanguageSpecificTextSet("LST3471F36C\_4?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST3471F36C\_5?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;"); Class](T_Grasshopper_DataTree_1.htm)

[Grasshopper Namespace](N_Grasshopper.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)