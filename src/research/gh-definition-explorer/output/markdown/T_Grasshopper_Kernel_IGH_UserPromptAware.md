# T_Grasshopper_Kernel_IGH_UserPromptAware

﻿ IGH\_UserPromptAware Interface

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH\_UserPromptAware Interface](../html/T_Grasshopper_Kernel_IGH_UserPromptAware.htm "IGH_UserPromptAware Interface")

[IGH\_UserPromptAware Methods](../html/Methods_T_Grasshopper_Kernel_IGH_UserPromptAware.htm "IGH_UserPromptAware Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_UserPromptAware Interface |

Implement this interface in your IGH\_Param if you want to allow users to set data
either through the menu or by double clicking.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public interface IGH_UserPromptAware
```

```
Public Interface IGH_UserPromptAware
```

AddLanguageTabSet("ID0EBCA");

The IGH\_UserPromptAware type exposes the following members.

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [PromptMenuMultipleItems](M_Grasshopper_Kernel_IGH_UserPromptAware_PromptMenuMultipleItems.htm) | Create a menu item that will be inserted into the Parameter context menu for getting multiple values. |
| Public method | [PromptMenuSingleItem](M_Grasshopper_Kernel_IGH_UserPromptAware_PromptMenuSingleItem.htm) | Create a menu item that will be inserted into the Parameter context menu for getting single values. |
| Public method | [PromptMultipleItems](M_Grasshopper_Kernel_IGH_UserPromptAware_PromptMultipleItems.htm) | Get multiple items from the user. |
| Public method | [PromptSingleItem](M_Grasshopper_Kernel_IGH_UserPromptAware_PromptSingleItem.htm) | Get a single item from the user. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)