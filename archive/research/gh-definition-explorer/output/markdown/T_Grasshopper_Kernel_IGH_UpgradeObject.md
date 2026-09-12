# T_Grasshopper_Kernel_IGH_UpgradeObject

﻿ IGH\_UpgradeObject Interface

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[IGH\_UpgradeObject Interface](../html/T_Grasshopper_Kernel_IGH_UpgradeObject.htm "IGH_UpgradeObject Interface")

[IGH\_UpgradeObject Properties](../html/Properties_T_Grasshopper_Kernel_IGH_UpgradeObject.htm "IGH_UpgradeObject Properties")

[IGH\_UpgradeObject Methods](../html/Methods_T_Grasshopper_Kernel_IGH_UpgradeObject.htm "IGH_UpgradeObject Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_UpgradeObject Interface |

Create a class with an empty constructor that implements this interface if you
want to provide an upgrade mechanism.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public interface IGH_UpgradeObject
```

```
Public Interface IGH_UpgradeObject
```

AddLanguageTabSet("ID0EBCA");

The IGH\_UpgradeObject type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [UpgradeFrom](P_Grasshopper_Kernel_IGH_UpgradeObject_UpgradeFrom.htm) | Gets the ComponentGuid of the old object (the object to be updated). |
| Public property | [UpgradeTo](P_Grasshopper_Kernel_IGH_UpgradeObject_UpgradeTo.htm) | Gets the ComponentGuid of the new object (the object that will be inserted). |
| Public property | [Version](P_Grasshopper_Kernel_IGH_UpgradeObject_Version.htm) | Return a DateTime object that indicates when this upgrade mechanism was written, so that it becomes possible to distinguish competing upgrade mechanisms. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [Upgrade](M_Grasshopper_Kernel_IGH_UpgradeObject_Upgrade.htm) | Upgrade an existing object. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)