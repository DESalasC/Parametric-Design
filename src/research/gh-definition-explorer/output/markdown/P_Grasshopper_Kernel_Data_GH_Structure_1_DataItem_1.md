# P_Grasshopper_Kernel_Data_GH_Structure_1_DataItem_1

﻿ GH\_Structure(T).DataItem Property (Int32)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Data](../html/N_Grasshopper_Kernel_Data.htm "Grasshopper.Kernel.Data")

[GH\_Structure(T) Class](../html/T_Grasshopper_Kernel_Data_GH_Structure_1.htm "GH_Structure(T) Class")

[GH\_Structure(T) Properties](../html/Properties_T_Grasshopper_Kernel_Data_GH_Structure_1.htm "GH_Structure(T) Properties")

[DataItem Property](../html/Overload_Grasshopper_Kernel_Data_GH_Structure_1_DataItem.htm "DataItem Property ")

[DataItem Property (Int32)](../html/P_Grasshopper_Kernel_Data_GH_Structure_1_DataItem_1.htm "DataItem Property (Int32)")

[DataItem Property (GH\_Path, Int32)](../html/P_Grasshopper_Kernel_Data_GH_Structure_1_DataItem.htm "DataItem Property (GH_Path, Int32)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_StructureAddLanguageSpecificTextSet("LST698BA57F\_0?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST698BA57F\_1?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");AddLanguageSpecificTextSet("LST698BA57F\_2?cpp=::|nu=.");DataItem Property (Int32) |

Gets the item at a given offset. The structure is treated as a linear list in this case.
If index is out of range, null is returned. For repeated indexed retrieval,
consider using a For Each loop since the enumerator is more efficient.

**Namespace:**
 [Grasshopper.Kernel.Data](N_Grasshopper_Kernel_Data.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public T this[
	int index
] { get; }
```

```
Public ReadOnly Property DataItem ( 
	index As Integer
) As T
	Get
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

index
:   Type: [SystemAddLanguageSpecificTextSet("LST698BA57F\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Offset of item to retrieve

#### Property Value

Type: [T](T_Grasshopper_Kernel_Data_GH_Structure_1.htm)  

[Missing <value> documentation for "P:Grasshopper.Kernel.Data.GH\_Structure`1.DataItem(System.Int32)"]

![](../icons/SectionExpanded.png)Exceptions

| Exception | Condition |
| --- | --- |
| [IndexOutOfRangeException](https://docs.microsoft.com/dotnet/api/system.indexoutofrangeexception) | Thrown if index is smaller than zero or larger than the size of the collection |

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_StructureAddLanguageSpecificTextSet("LST698BA57F\_4?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST698BA57F\_5?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;"); Class](T_Grasshopper_Kernel_Data_GH_Structure_1.htm)

[DataItem Overload](Overload_Grasshopper_Kernel_Data_GH_Structure_1_DataItem.htm)

[Grasshopper.Kernel.Data Namespace](N_Grasshopper_Kernel_Data.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)