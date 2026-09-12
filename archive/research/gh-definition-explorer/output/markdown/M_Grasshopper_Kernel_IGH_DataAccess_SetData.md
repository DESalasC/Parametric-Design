# M_Grasshopper_Kernel_IGH_DataAccess_SetData

﻿ IGH\_DataAccess.SetData Method (Int32, Object)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH\_DataAccess Interface](../html/T_Grasshopper_Kernel_IGH_DataAccess.htm "IGH_DataAccess Interface")

[IGH\_DataAccess Methods](../html/Methods_T_Grasshopper_Kernel_IGH_DataAccess.htm "IGH_DataAccess Methods")

[SetData Method](../html/Overload_Grasshopper_Kernel_IGH_DataAccess_SetData.htm "SetData Method ")

[SetData Method (Int32, Object)](../html/M_Grasshopper_Kernel_IGH_DataAccess_SetData.htm "SetData Method (Int32, Object)")

[SetData Method (String, Object)](../html/M_Grasshopper_Kernel_IGH_DataAccess_SetData_2.htm "SetData Method (String, Object)")

[SetData Method (Int32, Object, Int32)](../html/M_Grasshopper_Kernel_IGH_DataAccess_SetData_1.htm "SetData Method (Int32, Object, Int32)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_DataAccessAddLanguageSpecificTextSet("LST2E17F2B8\_0?cpp=::|nu=.");SetData Method (Int32, Object) |

Stores data in an output parameter during GH\_Component.SolveInstance().
Use this function only for setting individual data items.
If you want to set lists of data, you \*must\* call SetDataList() instead.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
bool SetData(
	int paramIndex,
	Object data
)
```

```
Function SetData ( 
	paramIndex As Integer,
	data As Object
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

paramIndex
:   Type: [SystemAddLanguageSpecificTextSet("LST2E17F2B8\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Index of the output parameter at which to store the data.

data
:   Type: [SystemAddLanguageSpecificTextSet("LST2E17F2B8\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
    Data to store. Data will be converted if necessary,
    but it will not be duplicated automatically.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)

![](../icons/SectionExpanded.png)See Also

#### Reference

[IGH\_DataAccess Interface](T_Grasshopper_Kernel_IGH_DataAccess.htm)

[SetData Overload](Overload_Grasshopper_Kernel_IGH_DataAccess_SetData.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)