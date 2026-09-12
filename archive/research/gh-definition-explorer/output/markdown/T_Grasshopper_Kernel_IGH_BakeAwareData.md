# T_Grasshopper_Kernel_IGH_BakeAwareData

﻿ IGH\_BakeAwareData Interface

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH\_BakeAwareData Interface](../html/T_Grasshopper_Kernel_IGH_BakeAwareData.htm "IGH_BakeAwareData Interface")

[IGH\_BakeAwareData Methods](../html/Methods_T_Grasshopper_Kernel_IGH_BakeAwareData.htm "IGH_BakeAwareData Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_BakeAwareData Interface |

Implement this interface in your IGH\_Goo data type if you want to
be included in baking operations.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public interface IGH_BakeAwareData
```

```
Public Interface IGH_BakeAwareData
```

AddLanguageTabSet("ID0EBCA");

The IGH\_BakeAwareData type exposes the following members.

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [BakeGeometry](M_Grasshopper_Kernel_IGH_BakeAwareData_BakeGeometry.htm) | Bake an object in the given Rhino document. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)