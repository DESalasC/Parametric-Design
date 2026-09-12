# T_Grasshopper_Kernel_IGH_InstanceGuidDependent

﻿ IGH\_InstanceGuidDependent Interface

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH\_InstanceGuidDependent Interface](../html/T_Grasshopper_Kernel_IGH_InstanceGuidDependent.htm "IGH_InstanceGuidDependent Interface")

[IGH\_InstanceGuidDependent Methods](../html/Methods_T_Grasshopper_Kernel_IGH_InstanceGuidDependent.htm "IGH_InstanceGuidDependent Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_InstanceGuidDependent Interface |

Implement this interface in your IGH\_DocumentObject class if you want to be informed when
the InstanceGuids of objects in the document are mutated.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public interface IGH_InstanceGuidDependent
```

```
Public Interface IGH_InstanceGuidDependent
```

AddLanguageTabSet("ID0EBCA");

The IGH\_InstanceGuidDependent type exposes the following members.

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [InstanceGuidsChanged](M_Grasshopper_Kernel_IGH_InstanceGuidDependent_InstanceGuidsChanged.htm) | This method will be called by the GH\_Document that owns this object after it mutates some or all of it's object InstanceIds. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)