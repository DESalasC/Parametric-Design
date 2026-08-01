# M_Grasshopper_DataTree_1_RenumberPaths_1

﻿ DataTree(T).RenumberPaths Method (String)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper](../html/N_Grasshopper.htm "Grasshopper")

[DataTree(T) Class](../html/T_Grasshopper_DataTree_1.htm "DataTree(T) Class")

[DataTree(T) Methods](../html/Methods_T_Grasshopper_DataTree_1.htm "DataTree(T) Methods")

[RenumberPaths Method](../html/Overload_Grasshopper_DataTree_1_RenumberPaths.htm "RenumberPaths Method ")

[RenumberPaths Method](../html/M_Grasshopper_DataTree_1_RenumberPaths.htm "RenumberPaths Method ")

[RenumberPaths Method (String)](../html/M_Grasshopper_DataTree_1_RenumberPaths_1.htm "RenumberPaths Method (String)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| DataTreeAddLanguageSpecificTextSet("LST249C37FA\_0?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST249C37FA\_1?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");AddLanguageSpecificTextSet("LST249C37FA\_2?cpp=::|nu=.");RenumberPaths Method (String) |

Renumber all paths in this data tree, using a single incrementing path index.

**Namespace:**
 [Grasshopper](N_Grasshopper.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public void RenumberPaths(
	string mask
)
```

```
Public Sub RenumberPaths ( 
	mask As String
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

mask
:   Type: [SystemAddLanguageSpecificTextSet("LST249C37FA\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    String formatting mask for paths. Use semi-colons for path index separators and "{i}" as a path index placeholder.
    Examples:

    "{i}" -> {i}

    "0;{i}" -> {0;i}

    "{i};0;0" -> {i;0;0}

![](../icons/SectionExpanded.png)See Also

#### Reference

[DataTreeAddLanguageSpecificTextSet("LST249C37FA\_4?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST249C37FA\_5?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;"); Class](T_Grasshopper_DataTree_1.htm)

[RenumberPaths Overload](Overload_Grasshopper_DataTree_1_RenumberPaths.htm)

[Grasshopper Namespace](N_Grasshopper.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)