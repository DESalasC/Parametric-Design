# P_Grasshopper_Kernel_GH_TaskCapableComponent_1_InPreSolve

﻿ GH\_TaskCapableComponent(T).InPreSolve Property 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_TaskCapableComponent(T) Class](../html/T_Grasshopper_Kernel_GH_TaskCapableComponent_1.htm "GH_TaskCapableComponent(T) Class")

[GH\_TaskCapableComponent(T) Properties](../html/Properties_T_Grasshopper_Kernel_GH_TaskCapableComponent_1.htm "GH_TaskCapableComponent(T) Properties")

[CancelToken Property](../html/P_Grasshopper_Kernel_GH_TaskCapableComponent_1_CancelToken.htm "CancelToken Property ")

[InPreSolve Property](../html/P_Grasshopper_Kernel_GH_TaskCapableComponent_1_InPreSolve.htm "InPreSolve Property ")

[InstanceDescription Property](../html/P_Grasshopper_Kernel_GH_TaskCapableComponent_1_InstanceDescription.htm "InstanceDescription Property ")

[TaskList Property](../html/P_Grasshopper_Kernel_GH_TaskCapableComponent_1_TaskList.htm "TaskList Property ")

[UseTasks Property](../html/P_Grasshopper_Kernel_GH_TaskCapableComponent_1_UseTasks.htm "UseTasks Property ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_TaskCapableComponentAddLanguageSpecificTextSet("LST67FBA9F8\_0?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LST67FBA9F8\_1?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");AddLanguageSpecificTextSet("LST67FBA9F8\_2?cpp=::|nu=.");InPreSolve Property |

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
public bool InPreSolve { get; set; }
```

```
Public Property InPreSolve As Boolean
	Get
	Set
```

AddLanguageTabSet("ID0EBCA");

#### Property Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  

[Missing <value> documentation for "P:Grasshopper.Kernel.GH\_TaskCapableComponent`1.InPreSolve"]

#### Implements

[IGH\_TaskCapableComponentAddLanguageSpecificTextSet("LST67FBA9F8\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");InPreSolve](P_Grasshopper_Kernel_IGH_TaskCapableComponent_InPreSolve.htm)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_TaskCapableComponentAddLanguageSpecificTextSet("LST67FBA9F8\_4?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LST67FBA9F8\_5?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;"); Class](T_Grasshopper_Kernel_GH_TaskCapableComponent_1.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)