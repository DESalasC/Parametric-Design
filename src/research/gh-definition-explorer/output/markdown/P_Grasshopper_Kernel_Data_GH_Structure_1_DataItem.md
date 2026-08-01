# P_Grasshopper_Kernel_Data_GH_Structure_1_DataItem

﻿ GH\_Structure(T).DataItem Property (GH\_Path, Int32)

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
| GH\_StructureAddLanguageSpecificTextSet("LST7487D9E7\_0?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST7487D9E7\_1?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");AddLanguageSpecificTextSet("LST7487D9E7\_2?cpp=::|nu=.");DataItem Property (GH\_Path, Int32) |

Gets a direct pointer to a data item under a specific path and index.

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
	GH_Path path,
	int index
] { get; }
```

```
Public ReadOnly Property DataItem ( 
	path As GH_Path,
	index As Integer
) As T
	Get
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

path
:   Type: [Grasshopper.Kernel.DataAddLanguageSpecificTextSet("LST7487D9E7\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Path](T_Grasshopper_Kernel_Data_GH_Path.htm)  
    Path of the data branch to retrieve.

index
:   Type: [SystemAddLanguageSpecificTextSet("LST7487D9E7\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Index of item to retrieve.

#### Property Value

Type: [T](T_Grasshopper_Kernel_Data_GH_Structure_1.htm)  

[Missing <value> documentation for "P:Grasshopper.Kernel.Data.GH\_Structure`1.DataItem(Grasshopper.Kernel.Data.GH\_Path,System.Int32)"]

![](../icons/SectionExpanded.png)Exceptions

| Exception | Condition |
| --- | --- |
| [NullReferenceException](https://docs.microsoft.com/dotnet/api/system.nullreferenceexception) | Thrown if the path doesn't exist. |
| [IndexOutOfRangeException](https://docs.microsoft.com/dotnet/api/system.indexoutofrangeexception) | Thrown if the index does not exist within the path list. |

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_StructureAddLanguageSpecificTextSet("LST7487D9E7\_5?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST7487D9E7\_6?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;"); Class](T_Grasshopper_Kernel_Data_GH_Structure_1.htm)

[DataItem Overload](Overload_Grasshopper_Kernel_Data_GH_Structure_1_DataItem.htm)

[Grasshopper.Kernel.Data Namespace](N_Grasshopper_Kernel_Data.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)