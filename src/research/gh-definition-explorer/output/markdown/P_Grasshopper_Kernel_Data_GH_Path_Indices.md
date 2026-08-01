# P_Grasshopper_Kernel_Data_GH_Path_Indices

﻿ GH\_Path.Indices Property 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Data](../html/N_Grasshopper_Kernel_Data.htm "Grasshopper.Kernel.Data")

[GH\_Path Class](../html/T_Grasshopper_Kernel_Data_GH_Path.htm "GH_Path Class")

[GH\_Path Properties](../html/Properties_T_Grasshopper_Kernel_Data_GH_Path.htm "GH_Path Properties")

[Indices Property](../html/P_Grasshopper_Kernel_Data_GH_Path_Indices.htm "Indices Property ")

[Length Property](../html/P_Grasshopper_Kernel_Data_GH_Path_Length.htm "Length Property ")

[Valid Property](../html/P_Grasshopper_Kernel_Data_GH_Path_Valid.htm "Valid Property ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_PathAddLanguageSpecificTextSet("LST4A3324DB\_0?cpp=::|nu=.");Indices Property |

Gets or sets the entire index space; the path that identifies an element in structure space.
You should not change the index space when the path is used inside a structure since it will invalidate
the sort order. If you don't know what you're doing, for Pete's sake don't touch this.

**Namespace:**
 [Grasshopper.Kernel.Data](N_Grasshopper_Kernel_Data.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public int[] Indices { get; set; }
```

```
Public Property Indices As Integer()
	Get
	Set
```

AddLanguageTabSet("ID0EBCA");

#### Property Value

Type: AddLanguageSpecificTextSet("LST4A3324DB\_1?cpp=array&lt;");[Int32](https://docs.microsoft.com/dotnet/api/system.int32)AddLanguageSpecificTextSet("LST4A3324DB\_2?cpp=&gt;|vb=()|nu=[]");  

[Missing <value> documentation for "P:Grasshopper.Kernel.Data.GH\_Path.Indices"]

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Path Class](T_Grasshopper_Kernel_Data_GH_Path.htm)

[Grasshopper.Kernel.Data Namespace](N_Grasshopper_Kernel_Data.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)