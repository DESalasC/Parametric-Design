# M_Grasshopper_Kernel_IGH_DataAccess_GetData__1_1

﻿ IGH\_DataAccess.GetData(T) Method (String, T)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH\_DataAccess Interface](../html/T_Grasshopper_Kernel_IGH_DataAccess.htm "IGH_DataAccess Interface")

[IGH\_DataAccess Methods](../html/Methods_T_Grasshopper_Kernel_IGH_DataAccess.htm "IGH_DataAccess Methods")

[GetData Method](../html/Overload_Grasshopper_Kernel_IGH_DataAccess_GetData.htm "GetData Method ")

[GetData(T) Method (Int32, T)](../html/M_Grasshopper_Kernel_IGH_DataAccess_GetData__1.htm "GetData(T) Method (Int32, T)")

[GetData(T) Method (String, T)](../html/M_Grasshopper_Kernel_IGH_DataAccess_GetData__1_1.htm "GetData(T) Method (String, T)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_DataAccessAddLanguageSpecificTextSet("LST9C5F7D12\_0?cpp=::|nu=.");GetDataAddLanguageSpecificTextSet("LST9C5F7D12\_1?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST9C5F7D12\_2?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)"); Method (String, TAddLanguageSpecificTextSet("LST9C5F7D12\_3?cpp=%");) |

Retrieve data from an input parameter during GH\_Component.SolveInstance().

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
bool GetData<T>(
	string name,
	ref T destination
)
```

```
Function GetData(Of T) ( 
	name As String,
	ByRef destination As T
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

name
:   Type: [SystemAddLanguageSpecificTextSet("LST9C5F7D12\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)

destination
:   Type: TAddLanguageSpecificTextSet("LST9C5F7D12\_5?cpp=%");

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

[GetData Overload](Overload_Grasshopper_Kernel_IGH_DataAccess_GetData.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)