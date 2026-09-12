# M_Grasshopper_Kernel_GH_UpgradeUtil_MigrateInputParameters

﻿ GH\_UpgradeUtil.MigrateInputParameters Method (IGH\_Component, IGH\_Component)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_UpgradeUtil Class](../html/T_Grasshopper_Kernel_GH_UpgradeUtil.htm "GH_UpgradeUtil Class")

[GH\_UpgradeUtil Methods](../html/Methods_T_Grasshopper_Kernel_GH_UpgradeUtil.htm "GH_UpgradeUtil Methods")

[MigrateInputParameters Method](../html/Overload_Grasshopper_Kernel_GH_UpgradeUtil_MigrateInputParameters.htm "MigrateInputParameters Method ")

[MigrateInputParameters Method (IGH\_Component, IGH\_Component)](../html/M_Grasshopper_Kernel_GH_UpgradeUtil_MigrateInputParameters.htm "MigrateInputParameters Method (IGH_Component, IGH_Component)")

[MigrateInputParameters Method (IGH\_Component, IGH\_Component, Int32[], Int32[])](../html/M_Grasshopper_Kernel_GH_UpgradeUtil_MigrateInputParameters_1.htm "MigrateInputParameters Method (IGH_Component, IGH_Component, Int32[], Int32[])")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_UpgradeUtilAddLanguageSpecificTextSet("LST71AB84B9\_0?cpp=::|nu=.");MigrateInputParameters Method (IGH\_Component, IGH\_Component) |

Migrate all input parameters.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static bool MigrateInputParameters(
	IGH_Component source,
	IGH_Component target
)
```

```
Public Shared Function MigrateInputParameters ( 
	source As IGH_Component,
	target As IGH_Component
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

source
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LST71AB84B9\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");IGH\_Component](T_Grasshopper_Kernel_IGH_Component.htm)  
    Source component.

target
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LST71AB84B9\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");IGH\_Component](T_Grasshopper_Kernel_IGH_Component.htm)  
    Target component.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True on success, false on failure.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_UpgradeUtil Class](T_Grasshopper_Kernel_GH_UpgradeUtil.htm)

[MigrateInputParameters Overload](Overload_Grasshopper_Kernel_GH_UpgradeUtil_MigrateInputParameters.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)