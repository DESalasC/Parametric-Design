# M_Grasshopper_Kernel_Data_GH_Path_IsCoincident_1

﻿ GH\_Path.IsCoincident Method (Int32[])

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Data](../html/N_Grasshopper_Kernel_Data.htm "Grasshopper.Kernel.Data")

[GH\_Path Class](../html/T_Grasshopper_Kernel_Data_GH_Path.htm "GH_Path Class")

[GH\_Path Methods](../html/Methods_T_Grasshopper_Kernel_Data_GH_Path.htm "GH_Path Methods")

[IsCoincident Method](../html/Overload_Grasshopper_Kernel_Data_GH_Path_IsCoincident.htm "IsCoincident Method ")

[IsCoincident Method (GH\_Path)](../html/M_Grasshopper_Kernel_Data_GH_Path_IsCoincident.htm "IsCoincident Method (GH_Path)")

[IsCoincident Method (Int32[])](../html/M_Grasshopper_Kernel_Data_GH_Path_IsCoincident_1.htm "IsCoincident Method (Int32[])")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_PathAddLanguageSpecificTextSet("LST7E44DF09\_0?cpp=::|nu=.");IsCoincident Method (AddLanguageSpecificTextSet("LST7E44DF09\_1?cpp=array&lt;");Int32AddLanguageSpecificTextSet("LST7E44DF09\_2?cpp=&gt;|vb=()|nu=[]");) |

Test to see if this path is coincident with set of integers.

**Namespace:**
 [Grasshopper.Kernel.Data](N_Grasshopper_Kernel_Data.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public bool IsCoincident(
	params int[] index_list
)
```

```
Public Function IsCoincident ( 
	ParamArray index_list As Integer()
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

index\_list
:   Type: AddLanguageSpecificTextSet("LST7E44DF09\_3?cpp=array&lt;");[SystemAddLanguageSpecificTextSet("LST7E44DF09\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)AddLanguageSpecificTextSet("LST7E44DF09\_5?cpp=&gt;|vb=()|nu=[]");  
    Integers to compare to.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True if both paths are coincident (identical), false if not.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Path Class](T_Grasshopper_Kernel_Data_GH_Path.htm)

[IsCoincident Overload](Overload_Grasshopper_Kernel_Data_GH_Path_IsCoincident.htm)

[Grasshopper.Kernel.Data Namespace](N_Grasshopper_Kernel_Data.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)