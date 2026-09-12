# T_Grasshopper_Kernel_IGH_ContextualParameter

﻿ IGH\_ContextualParameter Interface

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH\_ContextualParameter Interface](../html/T_Grasshopper_Kernel_IGH_ContextualParameter.htm "IGH_ContextualParameter Interface")

[IGH\_ContextualParameter Properties](../html/Properties_T_Grasshopper_Kernel_IGH_ContextualParameter.htm "IGH_ContextualParameter Properties")

[IGH\_ContextualParameter Methods](../html/Methods_T_Grasshopper_Kernel_IGH_ContextualParameter.htm "IGH_ContextualParameter Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_ContextualParameter Interface |

Base interface for contextual parameters.
This makes accessing non-strongly-typed functionality easier.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public interface IGH_ContextualParameter
```

```
Public Interface IGH_ContextualParameter
```

AddLanguageTabSet("ID0EBCA");

The IGH\_ContextualParameter type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [AtLeast](P_Grasshopper_Kernel_IGH_ContextualParameter_AtLeast.htm) | Minimum number of inputs to request |
| Public property | [AtMost](P_Grasshopper_Kernel_IGH_ContextualParameter_AtMost.htm) | Maximum number of inputs to request. |
| Public property | [ContextualData](P_Grasshopper_Kernel_IGH_ContextualParameter_ContextualData.htm) | Iterate over all specified contextual values. |
| Public property | [Immediate](P_Grasshopper_Kernel_IGH_ContextualParameter_Immediate.htm) | Gets whether this parameter triggers immediate updates from inside its getter. Immediacy is important for a smooth experience, but it maybe disabled if the expected recalculation time becomes excessive. |
| Public property | [Prompt](P_Grasshopper_Kernel_IGH_ContextualParameter_Prompt.htm) | Gets the prompt to be displayed while asking the user to enter data. The prompt string may contain '{0}' fields which will be populated with the amount of values picked so far. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [AssignContextualData](M_Grasshopper_Kernel_IGH_ContextualParameter_AssignContextualData.htm) | Assign a collection of values as contextual data. |
| Public method | [AutoAssignContextualData](M_Grasshopper_Kernel_IGH_ContextualParameter_AutoAssignContextualData.htm) | Use the in-build getter UI to assign data to the parameter. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)