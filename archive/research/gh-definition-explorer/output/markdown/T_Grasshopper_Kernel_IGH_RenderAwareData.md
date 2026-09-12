# T_Grasshopper_Kernel_IGH_RenderAwareData

﻿ IGH\_RenderAwareData Interface

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH\_RenderAwareData Interface](../html/T_Grasshopper_Kernel_IGH_RenderAwareData.htm "IGH_RenderAwareData Interface")

[IGH\_RenderAwareData Methods](../html/Methods_T_Grasshopper_Kernel_IGH_RenderAwareData.htm "IGH_RenderAwareData Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_RenderAwareData Interface |

Implement this interface in your IGH\_Goo type if it may have render geometry.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public interface IGH_RenderAwareData
```

```
Public Interface IGH_RenderAwareData
```

AddLanguageTabSet("ID0EBCA");

The IGH\_RenderAwareData type exposes the following members.

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [AppendRenderGeometry](M_Grasshopper_Kernel_IGH_RenderAwareData_AppendRenderGeometry.htm) | Push this geometry down a render pipeline. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)