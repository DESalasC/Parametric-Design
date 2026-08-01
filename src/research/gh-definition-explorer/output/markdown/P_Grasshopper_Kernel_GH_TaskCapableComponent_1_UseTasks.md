# P_Grasshopper_Kernel_GH_TaskCapableComponent_1_UseTasks

﻿ GH\_TaskCapableComponent(T).UseTasks Property 

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
| GH\_TaskCapableComponentAddLanguageSpecificTextSet("LSTC7DDA55A\_0?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTC7DDA55A\_1?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");AddLanguageSpecificTextSet("LSTC7DDA55A\_2?cpp=::|nu=.");UseTasks Property |

Returns True if the component is set to support tasks. Components can have this
feature turned on/off. Note that even if UseTasks returns True, there is a chance
that a multipass task based solution may not be invoked depending on if multiple
calls need to be made during enumeration. You must pay attention to the value of
InPreSolve during SolveInstance.
The set version of this property can be called by the framework if we want to
provide a technique to globally turn on/off task support for all components in
a definition.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public bool UseTasks { get; set; }
```

```
Public Property UseTasks As Boolean
	Get
	Set
```

AddLanguageTabSet("ID0EBCA");

#### Property Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  

[Missing <value> documentation for "P:Grasshopper.Kernel.GH\_TaskCapableComponent`1.UseTasks"]

#### Implements

[IGH\_TaskCapableComponentAddLanguageSpecificTextSet("LSTC7DDA55A\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");UseTasks](P_Grasshopper_Kernel_IGH_TaskCapableComponent_UseTasks.htm)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_TaskCapableComponentAddLanguageSpecificTextSet("LSTC7DDA55A\_4?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTC7DDA55A\_5?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;"); Class](T_Grasshopper_Kernel_GH_TaskCapableComponent_1.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)