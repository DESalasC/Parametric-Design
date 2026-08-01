# P_Grasshopper_DataTree_1_Item

﻿ DataTree(T).Item Property 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper](../html/N_Grasshopper.htm "Grasshopper")

[DataTree(T) Class](../html/T_Grasshopper_DataTree_1.htm "DataTree(T) Class")

[DataTree(T) Properties](../html/Properties_T_Grasshopper_DataTree_1.htm "DataTree(T) Properties")

[BranchCount Property](../html/P_Grasshopper_DataTree_1_BranchCount.htm "BranchCount Property ")

[Branches Property](../html/P_Grasshopper_DataTree_1_Branches.htm "Branches Property ")

[DataCount Property](../html/P_Grasshopper_DataTree_1_DataCount.htm "DataCount Property ")

[Item Property](../html/P_Grasshopper_DataTree_1_Item.htm "Item Property ")

[Paths Property](../html/P_Grasshopper_DataTree_1_Paths.htm "Paths Property ")

[TopologyDescription Property](../html/P_Grasshopper_DataTree_1_TopologyDescription.htm "TopologyDescription Property ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| DataTreeAddLanguageSpecificTextSet("LST9507395C\_0?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST9507395C\_1?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");AddLanguageSpecificTextSet("LST9507395C\_2?cpp=::|nu=.");Item Property |

Gets or set the data item at the specified path and index.

**Namespace:**
 [Grasshopper](N_Grasshopper.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public T this[
	GH_Path path,
	int index
] { get; set; }
```

```
Public Default Property Item ( 
	path As GH_Path,
	index As Integer
) As T
	Get
	Set
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

path
:   Type: [Grasshopper.Kernel.DataAddLanguageSpecificTextSet("LST9507395C\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Path](T_Grasshopper_Kernel_Data_GH_Path.htm)  
    Path of the data branch to retrieve. Path must be defined in the tree.

index
:   Type: [SystemAddLanguageSpecificTextSet("LST9507395C\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Index of item to retrieve. Index must be defined in the branch.

#### Property Value

Type: [T](T_Grasshopper_DataTree_1.htm)  

[Missing <value> documentation for "P:Grasshopper.DataTree`1.Item(Grasshopper.Kernel.Data.GH\_Path,System.Int32)"]

![](../icons/SectionExpanded.png)Exceptions

| Exception | Condition |
| --- | --- |
| [NullReferenceException](https://docs.microsoft.com/dotnet/api/system.nullreferenceexception) | Thrown if the path doesn't exist. |
| [IndexOutOfRangeException](https://docs.microsoft.com/dotnet/api/system.indexoutofrangeexception) | Thrown if the index does not exist within the path list. |

![](../icons/SectionExpanded.png)See Also

#### Reference

[DataTreeAddLanguageSpecificTextSet("LST9507395C\_5?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST9507395C\_6?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;"); Class](T_Grasshopper_DataTree_1.htm)

[Grasshopper Namespace](N_Grasshopper.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)