# M_Grasshopper_Kernel_GH_UpgradeUtil_MigrateRecipients

﻿ GH\_UpgradeUtil.MigrateRecipients Method (IGH\_Param, IGH\_Param)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_UpgradeUtil Class](../html/T_Grasshopper_Kernel_GH_UpgradeUtil.htm "GH_UpgradeUtil Class")

[GH\_UpgradeUtil Methods](../html/Methods_T_Grasshopper_Kernel_GH_UpgradeUtil.htm "GH_UpgradeUtil Methods")

[MigrateRecipients Method](../html/Overload_Grasshopper_Kernel_GH_UpgradeUtil_MigrateRecipients.htm "MigrateRecipients Method ")

[MigrateRecipients Method (IEnumerable(IGH\_Param), IGH\_Param)](../html/M_Grasshopper_Kernel_GH_UpgradeUtil_MigrateRecipients_1.htm "MigrateRecipients Method (IEnumerable(IGH_Param), IGH_Param)")

[MigrateRecipients Method (IGH\_Param, IGH\_Param)](../html/M_Grasshopper_Kernel_GH_UpgradeUtil_MigrateRecipients.htm "MigrateRecipients Method (IGH_Param, IGH_Param)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_UpgradeUtilAddLanguageSpecificTextSet("LSTD95C824D\_0?cpp=::|nu=.");MigrateRecipients Method (IGH\_Param, IGH\_Param) |

Migrate all recipients from A to B, while maintaining order.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static int MigrateRecipients(
	IGH_Param from,
	IGH_Param to
)
```

```
Public Shared Function MigrateRecipients ( 
	from As IGH_Param,
	to As IGH_Param
) As Integer
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

from
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LSTD95C824D\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");IGH\_Param](T_Grasshopper_Kernel_IGH_Param.htm)  
    Parameter to move recipients from.

to
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LSTD95C824D\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");IGH\_Param](T_Grasshopper_Kernel_IGH_Param.htm)  
    Parameter to move recipients to.

#### Return Value

Type: [Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
Number of recipients migrated.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_UpgradeUtil Class](T_Grasshopper_Kernel_GH_UpgradeUtil.htm)

[MigrateRecipients Overload](Overload_Grasshopper_Kernel_GH_UpgradeUtil_MigrateRecipients.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)