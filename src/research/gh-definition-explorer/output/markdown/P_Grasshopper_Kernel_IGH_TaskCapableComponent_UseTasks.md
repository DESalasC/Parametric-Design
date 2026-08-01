# P_Grasshopper_Kernel_IGH_TaskCapableComponent_UseTasks

﻿ IGH\_TaskCapableComponent.UseTasks Property 

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
| IGH\_TaskCapableComponentAddLanguageSpecificTextSet("LST4792BE8D\_0?cpp=::|nu=.");UseTasks Property |

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
bool UseTasks { get; set; }
```

```
Property UseTasks As Boolean
	Get
	Set
```

AddLanguageTabSet("ID0EBCA");

#### Property Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  

[Missing <value> documentation for "P:Grasshopper.Kernel.IGH\_TaskCapableComponent.UseTasks"]

![](../icons/SectionExpanded.png)See Also

#### Reference

[IGH\_TaskCapableComponent Interface](T_Grasshopper_Kernel_IGH_TaskCapableComponent.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)