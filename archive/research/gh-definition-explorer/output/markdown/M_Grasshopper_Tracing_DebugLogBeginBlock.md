# M_Grasshopper_Tracing_DebugLogBeginBlock

﻿ Tracing.DebugLogBeginBlock Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper](../html/N_Grasshopper.htm "Grasshopper")

[Tracing Class](../html/T_Grasshopper_Tracing.htm "Tracing Class")

[Tracing Methods](../html/Methods_T_Grasshopper_Tracing.htm "Tracing Methods")

[Assert Method](../html/Overload_Grasshopper_Tracing_Assert.htm "Assert Method ")

[DebugLogAddEntry Method](../html/M_Grasshopper_Tracing_DebugLogAddEntry.htm "DebugLogAddEntry Method ")

[DebugLogBeginBlock Method](../html/M_Grasshopper_Tracing_DebugLogBeginBlock.htm "DebugLogBeginBlock Method ")

[DebugLogEndBlock Method](../html/M_Grasshopper_Tracing_DebugLogEndBlock.htm "DebugLogEndBlock Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| TracingAddLanguageSpecificTextSet("LST2D9FF578\_0?cpp=::|nu=.");DebugLogBeginBlock Method |

Start a new block in the debug data. You *must* end all your own blocks.
This function will only work if the Grasshopper window exists. This method is threadsafe.

**Namespace:**
 [Grasshopper](N_Grasshopper.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static void DebugLogBeginBlock(
	string name
)
```

```
Public Shared Sub DebugLogBeginBlock ( 
	name As String
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

name
:   Type: [SystemAddLanguageSpecificTextSet("LST2D9FF578\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of block

![](../icons/SectionExpanded.png)See Also

#### Reference

[Tracing Class](T_Grasshopper_Tracing.htm)

[Grasshopper Namespace](N_Grasshopper.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)