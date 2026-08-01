# P_Grasshopper_Kernel_IGH_Component_InConstructor

﻿ IGH\_Component.InConstructor Property 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH\_Component Interface](../html/T_Grasshopper_Kernel_IGH_Component.htm "IGH_Component Interface")

[IGH\_Component Properties](../html/Properties_T_Grasshopper_Kernel_IGH_Component.htm "IGH_Component Properties")

[InConstructor Property](../html/P_Grasshopper_Kernel_IGH_Component_InConstructor.htm "InConstructor Property ")

[IsValidMasterParameterIndex Property](../html/P_Grasshopper_Kernel_IGH_Component_IsValidMasterParameterIndex.htm "IsValidMasterParameterIndex Property ")

[MasterParameterIndex Property](../html/P_Grasshopper_Kernel_IGH_Component_MasterParameterIndex.htm "MasterParameterIndex Property ")

[Message Property](../html/P_Grasshopper_Kernel_IGH_Component_Message.htm "Message Property ")

[Params Property](../html/P_Grasshopper_Kernel_IGH_Component_Params.htm "Params Property ")

[RunCount Property](../html/P_Grasshopper_Kernel_IGH_Component_RunCount.htm "RunCount Property ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_ComponentAddLanguageSpecificTextSet("LST12B0016B\_0?cpp=::|nu=.");InConstructor Property |

Gets the constructor flag for this instance. If InConstructor = True,
it means the component is still registering parameters and the
layout is not yet complete.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
bool InConstructor { get; }
```

```
ReadOnly Property InConstructor As Boolean
	Get
```

AddLanguageTabSet("ID0EBCA");

#### Property Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  

[Missing <value> documentation for "P:Grasshopper.Kernel.IGH\_Component.InConstructor"]

![](../icons/SectionExpanded.png)See Also

#### Reference

[IGH\_Component Interface](T_Grasshopper_Kernel_IGH_Component.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)