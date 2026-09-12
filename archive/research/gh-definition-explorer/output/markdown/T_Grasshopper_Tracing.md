# T_Grasshopper_Tracing

﻿ Tracing Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper](../html/N_Grasshopper.htm "Grasshopper")

[Tracing Class](../html/T_Grasshopper_Tracing.htm "Tracing Class")

[Tracing Methods](../html/Methods_T_Grasshopper_Tracing.htm "Tracing Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| Tracing Class |

Class that provides useful static methods for debugging, tracing and messaging.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LSTA04FF6E6\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  GrasshopperAddLanguageSpecificTextSet("LSTA04FF6E6\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Tracing

**Namespace:**
 [Grasshopper](N_Grasshopper.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public sealed class Tracing
```

```
Public NotInheritable Class Tracing
```

AddLanguageTabSet("ID1EBCA");

The Tracing type exposes the following members.

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public methodStatic member | [Assert(Guid)](M_Grasshopper_Tracing_Assert.htm) | Display a typical ASSERT dialog with stack information. |
| Public methodStatic member | [Assert(Guid, Exception)](M_Grasshopper_Tracing_Assert_1.htm) | Display a typical assert dialog with stack information. |
| Public methodStatic member | [Assert(Guid, String)](M_Grasshopper_Tracing_Assert_2.htm) | Display a typical assert dialog with stack information. |
| Public methodStatic member | [Assert(Guid, String, Exception)](M_Grasshopper_Tracing_Assert_3.htm) | Display a typical assert dialog with stack information. |
| Public methodStatic member | [DebugLogAddEntry](M_Grasshopper_Tracing_DebugLogAddEntry.htm) | Add a message to the debug log. If the debug log doesn't exist yet, it will be created. This function will only work if the Grasshopper window exists. This method is threadsafe. |
| Public methodStatic member | [DebugLogBeginBlock](M_Grasshopper_Tracing_DebugLogBeginBlock.htm) | Start a new block in the debug data. You *must* end all your own blocks. This function will only work if the Grasshopper window exists. This method is threadsafe. |
| Public methodStatic member | [DebugLogEndBlock](M_Grasshopper_Tracing_DebugLogEndBlock.htm) | Start a new block in the debug data. You *must* end all your own blocks. This function will only work if the Grasshopper window exists. This method is threadsafe. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper Namespace](N_Grasshopper.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)