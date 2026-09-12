# M_Grasshopper_Kernel_IGH_EventConsumer_TotalExpiration

﻿ IGH\_EventConsumer.TotalExpiration Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH\_EventConsumer Interface](../html/T_Grasshopper_Kernel_IGH_EventConsumer.htm "IGH_EventConsumer Interface")

[IGH\_EventConsumer Methods](../html/Methods_T_Grasshopper_Kernel_IGH_EventConsumer.htm "IGH_EventConsumer Methods")

[IsRelevantEvent Method](../html/M_Grasshopper_Kernel_IGH_EventConsumer_IsRelevantEvent.htm "IsRelevantEvent Method ")

[PartialExpiration Method](../html/M_Grasshopper_Kernel_IGH_EventConsumer_PartialExpiration.htm "PartialExpiration Method ")

[TotalExpiration Method](../html/M_Grasshopper_Kernel_IGH_EventConsumer_TotalExpiration.htm "TotalExpiration Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_EventConsumerAddLanguageSpecificTextSet("LSTC59D0172\_0?cpp=::|nu=.");TotalExpiration Method |

This method will be called by the GH\_CustomEventServer to indicate all
interesting object events can now be processed.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
void TotalExpiration(
	GH_CustomEventServer server
)
```

```
Sub TotalExpiration ( 
	server As GH_CustomEventServer
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

server
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LSTC59D0172\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_CustomEventServer](T_Grasshopper_Kernel_GH_CustomEventServer.htm)  
    Server that called this method.

![](../icons/SectionExpanded.png)See Also

#### Reference

[IGH\_EventConsumer Interface](T_Grasshopper_Kernel_IGH_EventConsumer.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)