# M_Grasshopper_Kernel_GH_UpgradeUtil_ReplaceOutputParameters

﻿ GH\_UpgradeUtil.ReplaceOutputParameters Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_UpgradeUtil Class](../html/T_Grasshopper_Kernel_GH_UpgradeUtil.htm "GH_UpgradeUtil Class")

[GH\_UpgradeUtil Methods](../html/Methods_T_Grasshopper_Kernel_GH_UpgradeUtil.htm "GH_UpgradeUtil Methods")

[MigrateInputParameters Method](../html/Overload_Grasshopper_Kernel_GH_UpgradeUtil_MigrateInputParameters.htm "MigrateInputParameters Method ")

[MigrateOutputParameters Method](../html/Overload_Grasshopper_Kernel_GH_UpgradeUtil_MigrateOutputParameters.htm "MigrateOutputParameters Method ")

[MigrateRecipients Method](../html/Overload_Grasshopper_Kernel_GH_UpgradeUtil_MigrateRecipients.htm "MigrateRecipients Method ")

[MigrateSources Method](../html/Overload_Grasshopper_Kernel_GH_UpgradeUtil_MigrateSources.htm "MigrateSources Method ")

[ReplaceInputParameters Method](../html/M_Grasshopper_Kernel_GH_UpgradeUtil_ReplaceInputParameters.htm "ReplaceInputParameters Method ")

[ReplaceOutputParameters Method](../html/M_Grasshopper_Kernel_GH_UpgradeUtil_ReplaceOutputParameters.htm "ReplaceOutputParameters Method ")

[SwapComponents Method](../html/Overload_Grasshopper_Kernel_GH_UpgradeUtil_SwapComponents.htm "SwapComponents Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_UpgradeUtilAddLanguageSpecificTextSet("LST6FA1252E\_0?cpp=::|nu=.");ReplaceOutputParameters Method |

Move all output parameters from one component to another.
Only use this function if the target component can handle the output layout of the source component.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static void ReplaceOutputParameters(
	IGH_Component source,
	IGH_Component target
)
```

```
Public Shared Sub ReplaceOutputParameters ( 
	source As IGH_Component,
	target As IGH_Component
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

source
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LST6FA1252E\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");IGH\_Component](T_Grasshopper_Kernel_IGH_Component.htm)  
    Component to move parameters from.

target
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LST6FA1252E\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");IGH\_Component](T_Grasshopper_Kernel_IGH_Component.htm)  
    Component to move parameters to.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_UpgradeUtil Class](T_Grasshopper_Kernel_GH_UpgradeUtil.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)