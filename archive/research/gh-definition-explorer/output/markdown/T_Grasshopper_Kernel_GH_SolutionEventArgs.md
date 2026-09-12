# T_Grasshopper_Kernel_GH_SolutionEventArgs

﻿ GH\_SolutionEventArgs Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_SolutionEventArgs Class](../html/T_Grasshopper_Kernel_GH_SolutionEventArgs.htm "GH_SolutionEventArgs Class")

[GH\_SolutionEventArgs Properties](../html/Properties_T_Grasshopper_Kernel_GH_SolutionEventArgs.htm "GH_SolutionEventArgs Properties")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_SolutionEventArgs Class |

Event arguments used for Document Solution events.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST54901723\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [SystemAddLanguageSpecificTextSet("LST54901723\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");EventArgs](https://docs.microsoft.com/dotnet/api/system.eventargs)  
    Grasshopper.KernelAddLanguageSpecificTextSet("LST54901723\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_SolutionEventArgs

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_SolutionEventArgs : EventArgs
```

```
Public Class GH_SolutionEventArgs
	Inherits EventArgs
```

AddLanguageTabSet("ID1EBCA");

The GH\_SolutionEventArgs type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Document](P_Grasshopper_Kernel_GH_SolutionEventArgs_Document.htm) | Gets the document that raised the event, should be the same as the "sender" parameter in the event handler. |
| Public property | [Duration](P_Grasshopper_Kernel_GH_SolutionEventArgs_Duration.htm) | Gets the duration for this solution. The duration is a more accurate measure than EndTime-StartTime. |
| Public property | [StartTime](P_Grasshopper_Kernel_GH_SolutionEventArgs_StartTime.htm) | Gets the time when the current solution began. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)