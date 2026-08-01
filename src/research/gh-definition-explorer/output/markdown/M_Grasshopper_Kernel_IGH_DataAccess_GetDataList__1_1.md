# M_Grasshopper_Kernel_IGH_DataAccess_GetDataList__1_1

﻿ IGH\_DataAccess.GetDataList(T) Method (String, List(T))

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH\_DataAccess Interface](../html/T_Grasshopper_Kernel_IGH_DataAccess.htm "IGH_DataAccess Interface")

[IGH\_DataAccess Methods](../html/Methods_T_Grasshopper_Kernel_IGH_DataAccess.htm "IGH_DataAccess Methods")

[GetDataList Method](../html/Overload_Grasshopper_Kernel_IGH_DataAccess_GetDataList.htm "GetDataList Method ")

[GetDataList(T) Method (Int32, List(T))](../html/M_Grasshopper_Kernel_IGH_DataAccess_GetDataList__1.htm "GetDataList(T) Method (Int32, List(T))")

[GetDataList(T) Method (String, List(T))](../html/M_Grasshopper_Kernel_IGH_DataAccess_GetDataList__1_1.htm "GetDataList(T) Method (String, List(T))")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_DataAccessAddLanguageSpecificTextSet("LST2C286609\_0?cpp=::|nu=.");GetDataListAddLanguageSpecificTextSet("LST2C286609\_1?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST2C286609\_2?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)"); Method (String, ListAddLanguageSpecificTextSet("LST2C286609\_3?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST2C286609\_4?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");) |

Retrieve an entire list of data from an input parameter during GH\_Component.SolveInstance().

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
bool GetDataList<T>(
	string name,
	List<T> list
)
```

```
Function GetDataList(Of T) ( 
	name As String,
	list As List(Of T)
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

name
:   Type: [SystemAddLanguageSpecificTextSet("LST2C286609\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)

list
:   Type: [System.Collections.GenericAddLanguageSpecificTextSet("LST2C286609\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");List](https://docs.microsoft.com/dotnet/api/system.collections.generic.list-1)AddLanguageSpecificTextSet("LST2C286609\_7?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST2C286609\_8?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");

#### Type Parameters

T
:   Type of the data to retrieve.
    If the data type does not match the parameter type,
    a conversion will be attempted.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True on success, false on failure.

![](../icons/SectionExpanded.png)Remarks

Parameter access by index is faster, consider using the other overload if possible.

![](../icons/SectionExpanded.png)See Also

#### Reference

[IGH\_DataAccess Interface](T_Grasshopper_Kernel_IGH_DataAccess.htm)

[GetDataList Overload](Overload_Grasshopper_Kernel_IGH_DataAccess_GetDataList.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)