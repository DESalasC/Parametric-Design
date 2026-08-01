# M_Grasshopper_Kernel_IGH_DataAccess_SetDataList_2

﻿ IGH\_DataAccess.SetDataList Method (String, IEnumerable)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH\_DataAccess Interface](../html/T_Grasshopper_Kernel_IGH_DataAccess.htm "IGH_DataAccess Interface")

[IGH\_DataAccess Methods](../html/Methods_T_Grasshopper_Kernel_IGH_DataAccess.htm "IGH_DataAccess Methods")

[SetDataList Method](../html/Overload_Grasshopper_Kernel_IGH_DataAccess_SetDataList.htm "SetDataList Method ")

[SetDataList Method (Int32, IEnumerable)](../html/M_Grasshopper_Kernel_IGH_DataAccess_SetDataList.htm "SetDataList Method (Int32, IEnumerable)")

[SetDataList Method (String, IEnumerable)](../html/M_Grasshopper_Kernel_IGH_DataAccess_SetDataList_2.htm "SetDataList Method (String, IEnumerable)")

[SetDataList Method (Int32, IEnumerable, Int32)](../html/M_Grasshopper_Kernel_IGH_DataAccess_SetDataList_1.htm "SetDataList Method (Int32, IEnumerable, Int32)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_DataAccessAddLanguageSpecificTextSet("LSTC8C37881\_0?cpp=::|nu=.");SetDataList Method (String, IEnumerable) |

Stores data in an output parameter during GH\_Component.SolveInstance().

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
bool SetDataList(
	string paramName,
	IEnumerable data
)
```

```
Function SetDataList ( 
	paramName As String,
	data As IEnumerable
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

paramName
:   Type: [SystemAddLanguageSpecificTextSet("LSTC8C37881\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of the parameter at which to store the data.

data
:   Type: [System.CollectionsAddLanguageSpecificTextSet("LSTC8C37881\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");IEnumerable](https://docs.microsoft.com/dotnet/api/system.collections.ienumerable)  
    Data to store. Data will be converted if necessary,
    but it will not be duplicated automatically.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)

![](../icons/SectionExpanded.png)Remarks

Parameter access by index is faster, consider using the other overload if possible.

![](../icons/SectionExpanded.png)See Also

#### Reference

[IGH\_DataAccess Interface](T_Grasshopper_Kernel_IGH_DataAccess.htm)

[SetDataList Overload](Overload_Grasshopper_Kernel_IGH_DataAccess_SetDataList.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)