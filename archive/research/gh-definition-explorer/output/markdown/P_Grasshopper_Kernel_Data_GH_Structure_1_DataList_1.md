# P_Grasshopper_Kernel_Data_GH_Structure_1_DataList_1

﻿ GH\_Structure(T).DataList Property (Int32)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Data](../html/N_Grasshopper_Kernel_Data.htm "Grasshopper.Kernel.Data")

[GH\_Structure(T) Class](../html/T_Grasshopper_Kernel_Data_GH_Structure_1.htm "GH_Structure(T) Class")

[GH\_Structure(T) Properties](../html/Properties_T_Grasshopper_Kernel_Data_GH_Structure_1.htm "GH_Structure(T) Properties")

[DataList Property](../html/Overload_Grasshopper_Kernel_Data_GH_Structure_1_DataList.htm "DataList Property ")

[DataList Property (GH\_Path)](../html/P_Grasshopper_Kernel_Data_GH_Structure_1_DataList.htm "DataList Property (GH_Path)")

[DataList Property (Int32)](../html/P_Grasshopper_Kernel_Data_GH_Structure_1_DataList_1.htm "DataList Property (Int32)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_StructureAddLanguageSpecificTextSet("LST44B7AE1D\_0?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST44B7AE1D\_1?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");AddLanguageSpecificTextSet("LST44B7AE1D\_2?cpp=::|nu=.");DataList Property (Int32) |

Gets a direct pointer to the list of data under the specified index.

**Namespace:**
 [Grasshopper.Kernel.Data](N_Grasshopper_Kernel_Data.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public List<T> this[
	int index
] { get; }
```

```
Public ReadOnly Default Property DataList ( 
	index As Integer
) As List(Of T)
	Get
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

index
:   Type: [SystemAddLanguageSpecificTextSet("LST44B7AE1D\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Index of the data branch to retrieve.

#### Property Value

Type: [List](https://docs.microsoft.com/dotnet/api/system.collections.generic.list-1)AddLanguageSpecificTextSet("LST44B7AE1D\_4?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");[T](T_Grasshopper_Kernel_Data_GH_Structure_1.htm)AddLanguageSpecificTextSet("LST44B7AE1D\_5?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  

[Missing <value> documentation for "P:Grasshopper.Kernel.Data.GH\_Structure`1.DataList(System.Int32)"]

![](../icons/SectionExpanded.png)Exceptions

| Exception | Condition |
| --- | --- |
| [IndexOutOfRangeException](https://docs.microsoft.com/dotnet/api/system.indexoutofrangeexception) | Thrown if the index does not represent a valid branch. |

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_StructureAddLanguageSpecificTextSet("LST44B7AE1D\_6?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST44B7AE1D\_7?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;"); Class](T_Grasshopper_Kernel_Data_GH_Structure_1.htm)

[DataList Overload](Overload_Grasshopper_Kernel_Data_GH_Structure_1_DataList.htm)

[Grasshopper.Kernel.Data Namespace](N_Grasshopper_Kernel_Data.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)