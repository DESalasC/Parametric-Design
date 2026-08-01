# T_Grasshopper_Kernel_Parameters_IGH_TypeHint

﻿ IGH\_TypeHint Interface

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Parameters](../html/N_Grasshopper_Kernel_Parameters.htm "Grasshopper.Kernel.Parameters")

[IGH\_TypeHint Interface](../html/T_Grasshopper_Kernel_Parameters_IGH_TypeHint.htm "IGH_TypeHint Interface")

[IGH\_TypeHint Properties](../html/Properties_T_Grasshopper_Kernel_Parameters_IGH_TypeHint.htm "IGH_TypeHint Properties")

[IGH\_TypeHint Methods](../html/Methods_T_Grasshopper_Kernel_Parameters_IGH_TypeHint.htm "IGH_TypeHint Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_TypeHint Interface |

Represents conversion logic for a certain data type.

**Namespace:**
 [Grasshopper.Kernel.Parameters](N_Grasshopper_Kernel_Parameters.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public interface IGH_TypeHint
```

```
Public Interface IGH_TypeHint
```

AddLanguageTabSet("ID0EBCA");

The IGH\_TypeHint type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [HintID](P_Grasshopper_Kernel_Parameters_IGH_TypeHint_HintID.htm) | Unique ID for every type of Hint. |
| Public property | [TypeName](P_Grasshopper_Kernel_Parameters_IGH_TypeHint_TypeName.htm) | Name of target Type |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [Cast](M_Grasshopper_Kernel_Parameters_IGH_TypeHint_Cast.htm) | Apply conversion logic to a specific object. This function should not throw exceptions. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Parameters Namespace](N_Grasshopper_Kernel_Parameters.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)