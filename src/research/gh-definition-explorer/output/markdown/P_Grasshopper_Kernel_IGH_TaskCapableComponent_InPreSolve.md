# P_Grasshopper_Kernel_IGH_TaskCapableComponent_InPreSolve

﻿ IGH\_TaskCapableComponent.InPreSolve Property 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH\_TaskCapableComponent Interface](../html/T_Grasshopper_Kernel_IGH_TaskCapableComponent.htm "IGH_TaskCapableComponent Interface")

[IGH\_TaskCapableComponent Properties](../html/Properties_T_Grasshopper_Kernel_IGH_TaskCapableComponent.htm "IGH_TaskCapableComponent Properties")

[InPreSolve Property](../html/P_Grasshopper_Kernel_IGH_TaskCapableComponent_InPreSolve.htm "InPreSolve Property ")

[UseTasks Property](../html/P_Grasshopper_Kernel_IGH_TaskCapableComponent_UseTasks.htm "UseTasks Property ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_TaskCapableComponentAddLanguageSpecificTextSet("LSTAD141FA3\_0?cpp=::|nu=.");InPreSolve Property |

Is set to True by the framework right before a "use tasks" pass is made on
SolveIntance calls. When True, SolveInstance should be using Tasks to start
calculations on input data. When False, SolveInstance should be setting the
output data by either using the result of a task or directly computing the
results.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
bool InPreSolve { get; set; }
```

```
Property InPreSolve As Boolean
	Get
	Set
```

AddLanguageTabSet("ID0EBCA");

#### Property Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  

[Missing <value> documentation for "P:Grasshopper.Kernel.IGH\_TaskCapableComponent.InPreSolve"]

![](../icons/SectionExpanded.png)See Also

#### Reference

[IGH\_TaskCapableComponent Interface](T_Grasshopper_Kernel_IGH_TaskCapableComponent.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)