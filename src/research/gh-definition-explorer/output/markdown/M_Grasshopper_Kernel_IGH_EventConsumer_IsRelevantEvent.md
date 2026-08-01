# M_Grasshopper_Kernel_IGH_EventConsumer_IsRelevantEvent

﻿ IGH\_EventConsumer.IsRelevantEvent Method 

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
| IGH\_EventConsumerAddLanguageSpecificTextSet("LST1AAE02BC\_0?cpp=::|nu=.");IsRelevantEvent Method |

Whenever a new object event is handled, this function will be called to determine whether it will cause an update.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
bool IsRelevantEvent(
	RhinoObject obj
)
```

```
Function IsRelevantEvent ( 
	obj As RhinoObject
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

obj
:   Type: RhinoObject  
    Object that is the pivot of the event.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True if the object should cause an update, false if not.

![](../icons/SectionExpanded.png)See Also

#### Reference

[IGH\_EventConsumer Interface](T_Grasshopper_Kernel_IGH_EventConsumer.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)