# M_Grasshopper_Kernel_GH_AssemblyPriority_PriorityLoad

﻿ GH\_AssemblyPriority.PriorityLoad Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_AssemblyPriority Class](../html/T_Grasshopper_Kernel_GH_AssemblyPriority.htm "GH_AssemblyPriority Class")

[GH\_AssemblyPriority Methods](../html/Methods_T_Grasshopper_Kernel_GH_AssemblyPriority.htm "GH_AssemblyPriority Methods")

[PriorityLoad Method](../html/M_Grasshopper_Kernel_GH_AssemblyPriority_PriorityLoad.htm "PriorityLoad Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_AssemblyPriorityAddLanguageSpecificTextSet("LSTDB65F6D9\_0?cpp=::|nu=.");PriorityLoad Method |

This method will be called exactly once before any of the Components in your project are loaded.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public abstract GH_LoadingInstruction PriorityLoad()
```

```
Public MustOverride Function PriorityLoad As GH_LoadingInstruction
```

AddLanguageTabSet("ID0EBCA");

#### Return Value

Type: [GH\_LoadingInstruction](T_Grasshopper_Kernel_GH_LoadingInstruction.htm)  
Loading instruction. If you wish to abort the loading of your project,
then return GH\_LoadingInstruction.Abort.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_AssemblyPriority Class](T_Grasshopper_Kernel_GH_AssemblyPriority.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)