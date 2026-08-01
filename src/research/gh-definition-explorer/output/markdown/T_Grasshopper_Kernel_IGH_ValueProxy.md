# T_Grasshopper_Kernel_IGH_ValueProxy

﻿ IGH\_ValueProxy Interface

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH\_ValueProxy Interface](../html/T_Grasshopper_Kernel_IGH_ValueProxy.htm "IGH_ValueProxy Interface")

[IGH\_ValueProxy Properties](../html/Properties_T_Grasshopper_Kernel_IGH_ValueProxy.htm "IGH_ValueProxy Properties")

[IGH\_ValueProxy Methods](../html/Methods_T_Grasshopper_Kernel_IGH_ValueProxy.htm "IGH_ValueProxy Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_ValueProxy Interface |

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public interface IGH_ValueProxy
```

```
Public Interface IGH_ValueProxy
```

AddLanguageTabSet("ID0EBCA");

The IGH\_ValueProxy type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [IsParsable](P_Grasshopper_Kernel_IGH_ValueProxy_IsParsable.htm) | Gets a value indicating whether or not the type can be instantiated from a String |
| Public property | [IsValid](P_Grasshopper_Kernel_IGH_ValueProxy_IsValid.htm) | Gets a value indicating whether or not the current value is valid |
| Public property | [ProxyName](P_Grasshopper_Kernel_IGH_ValueProxy_ProxyName.htm) | Gets a human-friendly name description of the template type |
| Public property | [ProxyType](P_Grasshopper_Kernel_IGH_ValueProxy_ProxyType.htm) | Gets the System.Type description of the template type |
| Public property | [ProxyValue](P_Grasshopper_Kernel_IGH_ValueProxy_ProxyValue.htm) | Gets an instance of the local template type object |
| Public property | [UserString](P_Grasshopper_Kernel_IGH_ValueProxy_UserString.htm) | Gets or sets the user-defined string that describes this proxy This only really makes sense if the Proxy is Parsable. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [Duplicate](M_Grasshopper_Kernel_IGH_ValueProxy_Duplicate.htm) | Create an exact duplicate of the type. |
| Public method | [FromString](M_Grasshopper_Kernel_IGH_ValueProxy_FromString.htm) | If IsParsable(), then attempts to convert the string to a generic type value |
| Public method | [MutateString](M_Grasshopper_Kernel_IGH_ValueProxy_MutateString.htm) | Munge a string to remove obvious errors on account of the user. |
| Public method | [ToString](M_Grasshopper_Kernel_IGH_ValueProxy_ToString.htm) | Returns a String description of the current value. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)