# Methods_T_Grasshopper_Kernel_GH_UpgradeUtil

﻿ GH\_UpgradeUtil Methods

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
| GH\_UpgradeUtil Methods |

The [GH\_UpgradeUtil](T_Grasshopper_Kernel_GH_UpgradeUtil.htm) type exposes the following members.

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public methodStatic member | [MigrateInputParameters(IGH\_Component, IGH\_Component)](M_Grasshopper_Kernel_GH_UpgradeUtil_MigrateInputParameters.htm) | Migrate all input parameters. |
| Public methodStatic member | [MigrateInputParameters(IGH\_Component, IGH\_Component, AddLanguageSpecificTextSet("LST35207326\_0?cpp=array&lt;");Int32AddLanguageSpecificTextSet("LST35207326\_1?cpp=&gt;|cs=[]|vb=()|nu=[]|fs=[]");, AddLanguageSpecificTextSet("LST35207326\_2?cpp=array&lt;");Int32AddLanguageSpecificTextSet("LST35207326\_3?cpp=&gt;|cs=[]|vb=()|nu=[]|fs=[]");)](M_Grasshopper_Kernel_GH_UpgradeUtil_MigrateInputParameters_1.htm) | Migrate a bunch of input parameters. |
| Public methodStatic member | [MigrateOutputParameters(IGH\_Component, IGH\_Component)](M_Grasshopper_Kernel_GH_UpgradeUtil_MigrateOutputParameters.htm) | Migrate all output parameters. |
| Public methodStatic member | [MigrateOutputParameters(IGH\_Component, IGH\_Component, AddLanguageSpecificTextSet("LST35207326\_4?cpp=array&lt;");Int32AddLanguageSpecificTextSet("LST35207326\_5?cpp=&gt;|cs=[]|vb=()|nu=[]|fs=[]");, AddLanguageSpecificTextSet("LST35207326\_6?cpp=array&lt;");Int32AddLanguageSpecificTextSet("LST35207326\_7?cpp=&gt;|cs=[]|vb=()|nu=[]|fs=[]");)](M_Grasshopper_Kernel_GH_UpgradeUtil_MigrateOutputParameters_1.htm) | Migrate a bunch of output parameters. |
| Public methodStatic member | [MigrateRecipients(IEnumerableAddLanguageSpecificTextSet("LST35207326\_8?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");IGH\_ParamAddLanguageSpecificTextSet("LST35207326\_9?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");, IGH\_Param)](M_Grasshopper_Kernel_GH_UpgradeUtil_MigrateRecipients_1.htm) | Utility method for bulk assigning a bunch of sources. |
| Public methodStatic member | [MigrateRecipients(IGH\_Param, IGH\_Param)](M_Grasshopper_Kernel_GH_UpgradeUtil_MigrateRecipients.htm) | Migrate all recipients from A to B, while maintaining order. |
| Public methodStatic member | [MigrateSources(IEnumerableAddLanguageSpecificTextSet("LST35207326\_10?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");IGH\_ParamAddLanguageSpecificTextSet("LST35207326\_11?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");, IGH\_Param)](M_Grasshopper_Kernel_GH_UpgradeUtil_MigrateSources_1.htm) | Utility method for bulk assigning a bunch of sources. |
| Public methodStatic member | [MigrateSources(IGH\_Param, IGH\_Param)](M_Grasshopper_Kernel_GH_UpgradeUtil_MigrateSources.htm) | Migrate all sources from A to B, while maintaining order. |
| Public methodStatic member | [ReplaceInputParameters](M_Grasshopper_Kernel_GH_UpgradeUtil_ReplaceInputParameters.htm) | Move all input parameters from one component to another. Only use this function if the target component can handle the input layout of the source component. |
| Public methodStatic member | [ReplaceOutputParameters](M_Grasshopper_Kernel_GH_UpgradeUtil_ReplaceOutputParameters.htm) | Move all output parameters from one component to another. Only use this function if the target component can handle the output layout of the source component. |
| Public methodStatic member | [SwapComponents(IGH\_Component, IGH\_Component)](M_Grasshopper_Kernel_GH_UpgradeUtil_SwapComponents.htm) | Replace an existing component with a different one. All parameters (input and output) will be migrated. |
| Public methodStatic member | [SwapComponents(IGH\_Component, Guid)](M_Grasshopper_Kernel_GH_UpgradeUtil_SwapComponents_2.htm) | Replace an existing component with a different one. All parameters (input and output) will be migrated. |
| Public methodStatic member | [SwapComponents(IGH\_Component, IGH\_Component, Boolean)](M_Grasshopper_Kernel_GH_UpgradeUtil_SwapComponents_1.htm) | Replace an existing component with a different one. All parameters (input and output) will be migrated. |
| Public methodStatic member | [SwapComponents(IGH\_Component, Guid, Boolean)](M_Grasshopper_Kernel_GH_UpgradeUtil_SwapComponents_3.htm) | Replace an existing component with a different one. All parameters (input and output) will be migrated. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_UpgradeUtil Class](T_Grasshopper_Kernel_GH_UpgradeUtil.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)