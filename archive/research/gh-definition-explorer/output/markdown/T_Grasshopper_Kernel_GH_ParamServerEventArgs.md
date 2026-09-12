# T_Grasshopper_Kernel_GH_ParamServerEventArgs

﻿ GH\_ParamServerEventArgs Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_ParamServerEventArgs Class](../html/T_Grasshopper_Kernel_GH_ParamServerEventArgs.htm "GH_ParamServerEventArgs Class")

[GH\_ParamServerEventArgs Properties](../html/Properties_T_Grasshopper_Kernel_GH_ParamServerEventArgs.htm "GH_ParamServerEventArgs Properties")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ParamServerEventArgs Class |

Arguments used in events for the GH\_ComponentParamServer type.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LSTD0E0728B\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [SystemAddLanguageSpecificTextSet("LSTD0E0728B\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");EventArgs](https://docs.microsoft.com/dotnet/api/system.eventargs)  
    Grasshopper.KernelAddLanguageSpecificTextSet("LSTD0E0728B\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_ParamServerEventArgs

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_ParamServerEventArgs : EventArgs
```

```
Public Class GH_ParamServerEventArgs
	Inherits EventArgs
```

AddLanguageTabSet("ID1EBCA");

The GH\_ParamServerEventArgs type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [OriginalArguments](P_Grasshopper_Kernel_GH_ParamServerEventArgs_OriginalArguments.htm) | Gets access to the original parameter event arguments. |
| Public property | [Parameter](P_Grasshopper_Kernel_GH_ParamServerEventArgs_Parameter.htm) | Gets the parameter that caused the original event. |
| Public property | [ParameterIndex](P_Grasshopper_Kernel_GH_ParamServerEventArgs_ParameterIndex.htm) | Gets the index of the parameter that caused the original event. |
| Public property | [ParameterSide](P_Grasshopper_Kernel_GH_ParamServerEventArgs_ParameterSide.htm) | Gets the side of the parameter that caused the original event. |
| Public property | [Server](P_Grasshopper_Kernel_GH_ParamServerEventArgs_Server.htm) | Gets the GH\_ComponentParamServer object that raised the event. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)