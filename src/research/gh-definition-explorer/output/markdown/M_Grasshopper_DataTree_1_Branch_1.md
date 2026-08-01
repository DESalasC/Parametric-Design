# M_Grasshopper_DataTree_1_Branch_1

﻿ DataTree(T).Branch Method (Int32)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper](../html/N_Grasshopper.htm "Grasshopper")

[DataTree(T) Class](../html/T_Grasshopper_DataTree_1.htm "DataTree(T) Class")

[DataTree(T) Methods](../html/Methods_T_Grasshopper_DataTree_1.htm "DataTree(T) Methods")

[Branch Method](../html/Overload_Grasshopper_DataTree_1_Branch.htm "Branch Method ")

[Branch Method (GH\_Path)](../html/M_Grasshopper_DataTree_1_Branch.htm "Branch Method (GH_Path)")

[Branch Method (Int32)](../html/M_Grasshopper_DataTree_1_Branch_1.htm "Branch Method (Int32)")

[Branch Method (Int32[])](../html/M_Grasshopper_DataTree_1_Branch_2.htm "Branch Method (Int32[])")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| DataTreeAddLanguageSpecificTextSet("LST37ECA2DF\_0?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST37ECA2DF\_1?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");AddLanguageSpecificTextSet("LST37ECA2DF\_2?cpp=::|nu=.");Branch Method (Int32) |

Gets the list of data which belongs to the branch path at the given index.

**Namespace:**
 [Grasshopper](N_Grasshopper.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public List<T> Branch(
	int index
)
```

```
Public Function Branch ( 
	index As Integer
) As List(Of T)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

index
:   Type: [SystemAddLanguageSpecificTextSet("LST37ECA2DF\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Index of data to retrieve.

#### Return Value

Type: [List](https://docs.microsoft.com/dotnet/api/system.collections.generic.list-1)AddLanguageSpecificTextSet("LST37ECA2DF\_4?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");[T](T_Grasshopper_DataTree_1.htm)AddLanguageSpecificTextSet("LST37ECA2DF\_5?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");

![](../icons/SectionExpanded.png)Exceptions

| Exception | Condition |
| --- | --- |
| [IndexOutOfRangeException](https://docs.microsoft.com/dotnet/api/system.indexoutofrangeexception) | Thrown if the index does not represent a valid path. |

![](../icons/SectionExpanded.png)See Also

#### Reference

[DataTreeAddLanguageSpecificTextSet("LST37ECA2DF\_6?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST37ECA2DF\_7?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;"); Class](T_Grasshopper_DataTree_1.htm)

[Branch Overload](Overload_Grasshopper_DataTree_1_Branch.htm)

[Grasshopper Namespace](N_Grasshopper.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)