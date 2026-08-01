# M_Grasshopper_Tracing_Assert

﻿ Tracing.Assert Method (Guid)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper](../html/N_Grasshopper.htm "Grasshopper")

[Tracing Class](../html/T_Grasshopper_Tracing.htm "Tracing Class")

[Tracing Methods](../html/Methods_T_Grasshopper_Tracing.htm "Tracing Methods")

[Assert Method](../html/Overload_Grasshopper_Tracing_Assert.htm "Assert Method ")

[Assert Method (Guid)](../html/M_Grasshopper_Tracing_Assert.htm "Assert Method (Guid)")

[Assert Method (Guid, Exception)](../html/M_Grasshopper_Tracing_Assert_1.htm "Assert Method (Guid, Exception)")

[Assert Method (Guid, String)](../html/M_Grasshopper_Tracing_Assert_2.htm "Assert Method (Guid, String)")

[Assert Method (Guid, String, Exception)](../html/M_Grasshopper_Tracing_Assert_3.htm "Assert Method (Guid, String, Exception)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| TracingAddLanguageSpecificTextSet("LSTCE7078A1\_0?cpp=::|nu=.");Assert Method (Guid) |

Display a typical ASSERT dialog with stack information.

**Namespace:**
 [Grasshopper](N_Grasshopper.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static void Assert(
	Guid assert_id
)
```

```
Public Shared Sub Assert ( 
	assert_id As Guid
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

assert\_id
:   Type: [SystemAddLanguageSpecificTextSet("LSTCE7078A1\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Guid](https://docs.microsoft.com/dotnet/api/system.guid)  
    ID of assert message. Every assert must have a unique ID so individual messages can be ignored.

![](../icons/SectionExpanded.png)See Also

#### Reference

[Tracing Class](T_Grasshopper_Tracing.htm)

[Assert Overload](Overload_Grasshopper_Tracing_Assert.htm)

[Grasshopper Namespace](N_Grasshopper.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)