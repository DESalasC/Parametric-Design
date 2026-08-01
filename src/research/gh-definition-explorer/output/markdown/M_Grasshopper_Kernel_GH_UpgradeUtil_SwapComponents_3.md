# M_Grasshopper_Kernel_GH_UpgradeUtil_SwapComponents_3

﻿ GH\_UpgradeUtil.SwapComponents Method (IGH\_Component, Guid, Boolean)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_UpgradeUtil Class](../html/T_Grasshopper_Kernel_GH_UpgradeUtil.htm "GH_UpgradeUtil Class")

[GH\_UpgradeUtil Methods](../html/Methods_T_Grasshopper_Kernel_GH_UpgradeUtil.htm "GH_UpgradeUtil Methods")

[SwapComponents Method](../html/Overload_Grasshopper_Kernel_GH_UpgradeUtil_SwapComponents.htm "SwapComponents Method ")

[SwapComponents Method (IGH\_Component, IGH\_Component)](../html/M_Grasshopper_Kernel_GH_UpgradeUtil_SwapComponents.htm "SwapComponents Method (IGH_Component, IGH_Component)")

[SwapComponents Method (IGH\_Component, Guid)](../html/M_Grasshopper_Kernel_GH_UpgradeUtil_SwapComponents_2.htm "SwapComponents Method (IGH_Component, Guid)")

[SwapComponents Method (IGH\_Component, IGH\_Component, Boolean)](../html/M_Grasshopper_Kernel_GH_UpgradeUtil_SwapComponents_1.htm "SwapComponents Method (IGH_Component, IGH_Component, Boolean)")

[SwapComponents Method (IGH\_Component, Guid, Boolean)](../html/M_Grasshopper_Kernel_GH_UpgradeUtil_SwapComponents_3.htm "SwapComponents Method (IGH_Component, Guid, Boolean)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_UpgradeUtilAddLanguageSpecificTextSet("LST9EA4C4CC\_0?cpp=::|nu=.");SwapComponents Method (IGH\_Component, Guid, Boolean) |

Replace an existing component with a different one. All parameters (input and output) will be migrated.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static IGH_Component SwapComponents(
	IGH_Component oldComponent,
	Guid newComponentGuid,
	bool migrateParameters
)
```

```
Public Shared Function SwapComponents ( 
	oldComponent As IGH_Component,
	newComponentGuid As Guid,
	migrateParameters As Boolean
) As IGH_Component
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

oldComponent
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LST9EA4C4CC\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");IGH\_Component](T_Grasshopper_Kernel_IGH_Component.htm)  
    Component current in a GH\_Document.

newComponentGuid
:   Type: [SystemAddLanguageSpecificTextSet("LST9EA4C4CC\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Guid](https://docs.microsoft.com/dotnet/api/system.guid)  
    ComponentGuid of the component to add.

migrateParameters
:   Type: [SystemAddLanguageSpecificTextSet("LST9EA4C4CC\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
    If true, all parameters will be moved from old to new.

#### Return Value

Type: [IGH\_Component](T_Grasshopper_Kernel_IGH_Component.htm)  
Component that was added.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_UpgradeUtil Class](T_Grasshopper_Kernel_GH_UpgradeUtil.htm)

[SwapComponents Overload](Overload_Grasshopper_Kernel_GH_UpgradeUtil_SwapComponents.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)