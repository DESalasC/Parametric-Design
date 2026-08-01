# P_Grasshopper_Kernel_IGH_DataAccess_Iteration

﻿ IGH\_DataAccess.Iteration Property 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH\_DataAccess Interface](../html/T_Grasshopper_Kernel_IGH_DataAccess.htm "IGH_DataAccess Interface")

[IGH\_DataAccess Properties](../html/Properties_T_Grasshopper_Kernel_IGH_DataAccess.htm "IGH_DataAccess Properties")

[Iteration Property](../html/P_Grasshopper_Kernel_IGH_DataAccess_Iteration.htm "Iteration Property ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_DataAccessAddLanguageSpecificTextSet("LSTB6949EE9\_0?cpp=::|nu=.");Iteration Property |

Gets the current iteration count.
The first time the SolveInstance() function is called on a component
during a solution the Iteration counter will be zero. It will be
incremented by one for every subsequent call.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
int Iteration { get; }
```

```
ReadOnly Property Iteration As Integer
	Get
```

AddLanguageTabSet("ID0EBCA");

#### Property Value

Type: [Int32](https://docs.microsoft.com/dotnet/api/system.int32)  

[Missing <value> documentation for "P:Grasshopper.Kernel.IGH\_DataAccess.Iteration"]

#### Return Value

Type: [Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
An integer representing the iteration count.

![](../icons/SectionExpanded.png)See Also

#### Reference

[IGH\_DataAccess Interface](T_Grasshopper_Kernel_IGH_DataAccess.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)