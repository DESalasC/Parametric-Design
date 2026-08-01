# T_Grasshopper_Kernel_Types_IGH_GooProxy

﻿ IGH\_GooProxy Interface

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm "Grasshopper.Kernel.Types")

[IGH\_GooProxy Interface](../html/T_Grasshopper_Kernel_Types_IGH_GooProxy.htm "IGH_GooProxy Interface")

[IGH\_GooProxy Properties](../html/Properties_T_Grasshopper_Kernel_Types_IGH_GooProxy.htm "IGH_GooProxy Properties")

[IGH\_GooProxy Methods](../html/Methods_T_Grasshopper_Kernel_Types_IGH_GooProxy.htm "IGH_GooProxy Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_GooProxy Interface |

Base interface for all type proxies.

**Namespace:**
 [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public interface IGH_GooProxy
```

```
Public Interface IGH_GooProxy
```

AddLanguageTabSet("ID0EBCA");

The IGH\_GooProxy type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [IsParsable](P_Grasshopper_Kernel_Types_IGH_GooProxy_IsParsable.htm) | Gets a value indicating whether or not the type can be instantiated from a String. |
| Public property | [ProxyOwner](P_Grasshopper_Kernel_Types_IGH_GooProxy_ProxyOwner.htm) | Gets the piece of Grasshopper data that spawned this proxy. |
| Public property | [UserString](P_Grasshopper_Kernel_Types_IGH_GooProxy_UserString.htm) | Gets or sets the user-defined string that describes this proxy. This only really makes sense if the Proxy is Parsable. |
| Public property | [Valid](P_Grasshopper_Kernel_Types_IGH_GooProxy_Valid.htm) | Gets a value indicating whether this proxy represents valid data. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [Construct](M_Grasshopper_Kernel_Types_IGH_GooProxy_Construct.htm) | This method will be called when a new instance of this type is constructed. It allows implementers to supply a customized UI to be shown during construction. This method should never throw exceptions. |
| Public method | [FormatInstance](M_Grasshopper_Kernel_Types_IGH_GooProxy_FormatInstance.htm) | Returns a String description of the current value. |
| Public method | [FromString](M_Grasshopper_Kernel_Types_IGH_GooProxy_FromString.htm) | If IsParsable(), then attempts to convert the string to a generic type value |
| Public method | [MutateString](M_Grasshopper_Kernel_Types_IGH_GooProxy_MutateString.htm) | Munge a string to remove obvious errors on account of the user. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Types Namespace](N_Grasshopper_Kernel_Types.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)