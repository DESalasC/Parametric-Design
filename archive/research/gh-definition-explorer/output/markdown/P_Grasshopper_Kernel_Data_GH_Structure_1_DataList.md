# P_Grasshopper_Kernel_Data_GH_Structure_1_DataList

﻿ GH\_Structure(T).DataList Property (GH\_Path)

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
| GH\_StructureAddLanguageSpecificTextSet("LSTABE01051\_0?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTABE01051\_1?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");AddLanguageSpecificTextSet("LSTABE01051\_2?cpp=::|nu=.");DataList Property (GH\_Path) |

Gets a direct pointer to the list of data under a specific path.

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
	GH_Path path
] { get; }
```

```
Public ReadOnly Default Property DataList ( 
	path As GH_Path
) As List(Of T)
	Get
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

path
:   Type: [Grasshopper.Kernel.DataAddLanguageSpecificTextSet("LSTABE01051\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Path](T_Grasshopper_Kernel_Data_GH_Path.htm)  
    Path of the data branch to retrieve. If the path doesn't exist, null is returned.

#### Property Value

Type: [List](https://docs.microsoft.com/dotnet/api/system.collections.generic.list-1)AddLanguageSpecificTextSet("LSTABE01051\_4?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");[T](T_Grasshopper_Kernel_Data_GH_Structure_1.htm)AddLanguageSpecificTextSet("LSTABE01051\_5?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  

[Missing <value> documentation for "P:Grasshopper.Kernel.Data.GH\_Structure`1.DataList(Grasshopper.Kernel.Data.GH\_Path)"]

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_StructureAddLanguageSpecificTextSet("LSTABE01051\_6?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTABE01051\_7?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;"); Class](T_Grasshopper_Kernel_Data_GH_Structure_1.htm)

[DataList Overload](Overload_Grasshopper_Kernel_Data_GH_Structure_1_DataList.htm)

[Grasshopper.Kernel.Data Namespace](N_Grasshopper_Kernel_Data.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)