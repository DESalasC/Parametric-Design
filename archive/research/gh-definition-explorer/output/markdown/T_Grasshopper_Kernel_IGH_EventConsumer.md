# T_Grasshopper_Kernel_IGH_EventConsumer

﻿ IGH\_EventConsumer Interface

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH\_EventConsumer Interface](../html/T_Grasshopper_Kernel_IGH_EventConsumer.htm "IGH_EventConsumer Interface")

[IGH\_EventConsumer Methods](../html/Methods_T_Grasshopper_Kernel_IGH_EventConsumer.htm "IGH_EventConsumer Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_EventConsumer Interface |

Implement this interface if you want to inter-operate with a GH\_EventServer.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public interface IGH_EventConsumer
```

```
Public Interface IGH_EventConsumer
```

AddLanguageTabSet("ID0EBCA");

The IGH\_EventConsumer type exposes the following members.

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [IsRelevantEvent](M_Grasshopper_Kernel_IGH_EventConsumer_IsRelevantEvent.htm) | Whenever a new object event is handled, this function will be called to determine whether it will cause an update. |
| Public method | [PartialExpiration](M_Grasshopper_Kernel_IGH_EventConsumer_PartialExpiration.htm) | This method will be called by the GH\_CustomEventServer to indicate one or more interesting object events can now be processed. |
| Public method | [TotalExpiration](M_Grasshopper_Kernel_IGH_EventConsumer_TotalExpiration.htm) | This method will be called by the GH\_CustomEventServer to indicate all interesting object events can now be processed. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)