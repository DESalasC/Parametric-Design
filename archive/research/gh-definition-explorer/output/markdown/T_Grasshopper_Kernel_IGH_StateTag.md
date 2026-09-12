# T_Grasshopper_Kernel_IGH_StateTag

﻿ IGH\_StateTag Interface

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH\_StateTag Interface](../html/T_Grasshopper_Kernel_IGH_StateTag.htm "IGH_StateTag Interface")

[IGH\_StateTag Properties](../html/Properties_T_Grasshopper_Kernel_IGH_StateTag.htm "IGH_StateTag Properties")

[IGH\_StateTag Methods](../html/Methods_T_Grasshopper_Kernel_IGH_StateTag.htm "IGH_StateTag Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_StateTag Interface |

A StateTag is a visual feedback mechanism that reflects a certain local setting of an Object.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public interface IGH_StateTag
```

```
Public Interface IGH_StateTag
```

AddLanguageTabSet("ID0EBCA");

The IGH\_StateTag type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Description](P_Grasshopper_Kernel_IGH_StateTag_Description.htm) | Gets the description of this state tag. |
| Public property | [Icon](P_Grasshopper_Kernel_IGH_StateTag_Icon.htm) | Gets the 16 by 16 pixel icon associated with this state tag. |
| Public property | [Name](P_Grasshopper_Kernel_IGH_StateTag_Name.htm) | Gets the name field of this state tag. |
| Public property | [Stage](P_Grasshopper_Kernel_IGH_StateTag_Stage.htm) | Gets or sets the Stage rectangle for this state tag. Stages are assigned during Attribute Layout operations by owner objects. |
| Public property | [StateDescription](P_Grasshopper_Kernel_IGH_StateTag_StateDescription.htm) | Gets or sets the state description of this tag. The state description appears in the Tooltip info field. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [Render](M_Grasshopper_Kernel_IGH_StateTag_Render.htm) | Render this tag into a graphics surface. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)