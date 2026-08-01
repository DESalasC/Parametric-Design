# P_Grasshopper_Kernel_IGH_ActiveObject_RuntimeMessageLevel

﻿ IGH\_ActiveObject.RuntimeMessageLevel Property 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH\_ActiveObject Interface](../html/T_Grasshopper_Kernel_IGH_ActiveObject.htm "IGH_ActiveObject Interface")

[IGH\_ActiveObject Properties](../html/Properties_T_Grasshopper_Kernel_IGH_ActiveObject.htm "IGH_ActiveObject Properties")

[IsDataProvider Property](../html/P_Grasshopper_Kernel_IGH_ActiveObject_IsDataProvider.htm "IsDataProvider Property ")

[Locked Property](../html/P_Grasshopper_Kernel_IGH_ActiveObject_Locked.htm "Locked Property ")

[MutableNickName Property](../html/P_Grasshopper_Kernel_IGH_ActiveObject_MutableNickName.htm "MutableNickName Property ")

[Phase Property](../html/P_Grasshopper_Kernel_IGH_ActiveObject_Phase.htm "Phase Property ")

[ProcessorTime Property](../html/P_Grasshopper_Kernel_IGH_ActiveObject_ProcessorTime.htm "ProcessorTime Property ")

[RuntimeMessageLevel Property](../html/P_Grasshopper_Kernel_IGH_ActiveObject_RuntimeMessageLevel.htm "RuntimeMessageLevel Property ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_ActiveObjectAddLanguageSpecificTextSet("LSTE9C3569B\_0?cpp=::|nu=.");RuntimeMessageLevel Property |

Gets the worst-case level of all messages. I.e. if only warnings have been recorded,
the level will be ::warning. If even a single error exists, the level will be ::error.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
GH_RuntimeMessageLevel RuntimeMessageLevel { get; }
```

```
ReadOnly Property RuntimeMessageLevel As GH_RuntimeMessageLevel
	Get
```

AddLanguageTabSet("ID0EBCA");

#### Property Value

Type: [GH\_RuntimeMessageLevel](T_Grasshopper_Kernel_GH_RuntimeMessageLevel.htm)  

[Missing <value> documentation for "P:Grasshopper.Kernel.IGH\_ActiveObject.RuntimeMessageLevel"]

![](../icons/SectionExpanded.png)See Also

#### Reference

[IGH\_ActiveObject Interface](T_Grasshopper_Kernel_IGH_ActiveObject.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)