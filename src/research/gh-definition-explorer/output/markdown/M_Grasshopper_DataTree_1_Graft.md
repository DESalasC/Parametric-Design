# M_Grasshopper_DataTree_1_Graft

﻿ DataTree(T).Graft Method (GH\_Path, Boolean)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper](../html/N_Grasshopper.htm "Grasshopper")

[DataTree(T) Class](../html/T_Grasshopper_DataTree_1.htm "DataTree(T) Class")

[DataTree(T) Methods](../html/Methods_T_Grasshopper_DataTree_1.htm "DataTree(T) Methods")

[Graft Method](../html/Overload_Grasshopper_DataTree_1_Graft.htm "Graft Method ")

[Graft Method (Boolean)](../html/M_Grasshopper_DataTree_1_Graft_1.htm "Graft Method (Boolean)")

[Graft Method (GH\_Path, Boolean)](../html/M_Grasshopper_DataTree_1_Graft.htm "Graft Method (GH_Path, Boolean)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| DataTreeAddLanguageSpecificTextSet("LSTD8651755\_0?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTD8651755\_1?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");AddLanguageSpecificTextSet("LSTD8651755\_2?cpp=::|nu=.");Graft Method (GH\_Path, Boolean) |

Graft a single path in the tree.
"Grafting" means appending a new branch for every item in an existing branch.

**Namespace:**
 [Grasshopper](N_Grasshopper.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public void Graft(
	GH_Path path,
	bool skip_nulls = false
)
```

```
Public Sub Graft ( 
	path As GH_Path,
	Optional skip_nulls As Boolean = false
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

path
:   Type: [Grasshopper.Kernel.DataAddLanguageSpecificTextSet("LSTD8651755\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Path](T_Grasshopper_Kernel_Data_GH_Path.htm)  
    Path to graft.

skip\_nulls (Optional)
:   Type: [SystemAddLanguageSpecificTextSet("LSTD8651755\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
    If true, null items in the grafted path will **not** be included in the new tree.

![](../icons/SectionExpanded.png)See Also

#### Reference

[DataTreeAddLanguageSpecificTextSet("LSTD8651755\_5?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTD8651755\_6?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;"); Class](T_Grasshopper_DataTree_1.htm)

[Graft Overload](Overload_Grasshopper_DataTree_1_Graft.htm)

[Grasshopper Namespace](N_Grasshopper.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)