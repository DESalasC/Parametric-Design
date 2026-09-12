# M_Grasshopper_Kernel_IGH_ActiveObject_CollectData

﻿ IGH\_ActiveObject.CollectData Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH\_ActiveObject Interface](../html/T_Grasshopper_Kernel_IGH_ActiveObject.htm "IGH_ActiveObject Interface")

[IGH\_ActiveObject Methods](../html/Methods_T_Grasshopper_Kernel_IGH_ActiveObject.htm "IGH_ActiveObject Methods")

[AddRuntimeMessage Method](../html/M_Grasshopper_Kernel_IGH_ActiveObject_AddRuntimeMessage.htm "AddRuntimeMessage Method ")

[ClearData Method](../html/M_Grasshopper_Kernel_IGH_ActiveObject_ClearData.htm "ClearData Method ")

[ClearRuntimeMessages Method](../html/M_Grasshopper_Kernel_IGH_ActiveObject_ClearRuntimeMessages.htm "ClearRuntimeMessages Method ")

[CollectData Method](../html/M_Grasshopper_Kernel_IGH_ActiveObject_CollectData.htm "CollectData Method ")

[ComputeData Method](../html/M_Grasshopper_Kernel_IGH_ActiveObject_ComputeData.htm "ComputeData Method ")

[DependsOn Method](../html/M_Grasshopper_Kernel_IGH_ActiveObject_DependsOn.htm "DependsOn Method ")

[RegisterRemoteIDs Method](../html/M_Grasshopper_Kernel_IGH_ActiveObject_RegisterRemoteIDs.htm "RegisterRemoteIDs Method ")

[RuntimeMessages Method](../html/M_Grasshopper_Kernel_IGH_ActiveObject_RuntimeMessages.htm "RuntimeMessages Method ")

[SDKCompliancy Method](../html/M_Grasshopper_Kernel_IGH_ActiveObject_SDKCompliancy.htm "SDKCompliancy Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_ActiveObjectAddLanguageSpecificTextSet("LST63D81BA9\_0?cpp=::|nu=.");CollectData Method |

This function is called whenever the object is required to collect
all data. Either from Persistent records, from source params or whatever.
This step is only performed if the phase flag is Blank or Failed.
Upon completion, the phase flag will be set to Collected

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
void CollectData()
```

```
Sub CollectData
```

AddLanguageTabSet("ID0EBCA");

![](../icons/SectionExpanded.png)See Also

#### Reference

[IGH\_ActiveObject Interface](T_Grasshopper_Kernel_IGH_ActiveObject.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)