# T_Grasshopper_Kernel_GH_UpgradeUtil

﻿ GH\_UpgradeUtil Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_UpgradeUtil Class](../html/T_Grasshopper_Kernel_GH_UpgradeUtil.htm "GH_UpgradeUtil Class")

[GH\_UpgradeUtil Constructor](../html/M_Grasshopper_Kernel_GH_UpgradeUtil__ctor.htm "GH_UpgradeUtil Constructor ")

[GH\_UpgradeUtil Methods](../html/Methods_T_Grasshopper_Kernel_GH_UpgradeUtil.htm "GH_UpgradeUtil Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_UpgradeUtil Class |

Exposes several utility functions for migrating parameters and wires between components useful
while upgrading components.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LSTFD7331B5\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.KernelAddLanguageSpecificTextSet("LSTFD7331B5\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_UpgradeUtil

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_UpgradeUtil
```

```
Public Class GH_UpgradeUtil
```

AddLanguageTabSet("ID1EBCA");

The GH\_UpgradeUtil type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_UpgradeUtil](M_Grasshopper_Kernel_GH_UpgradeUtil__ctor.htm) | Initializes a new instance of the GH\_UpgradeUtil class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public methodStatic member | [MigrateInputParameters(IGH\_Component, IGH\_Component)](M_Grasshopper_Kernel_GH_UpgradeUtil_MigrateInputParameters.htm) | Migrate all input parameters. |
| Public methodStatic member | [MigrateInputParameters(IGH\_Component, IGH\_Component, AddLanguageSpecificTextSet("LSTFD7331B5\_2?cpp=array&lt;");Int32AddLanguageSpecificTextSet("LSTFD7331B5\_3?cpp=&gt;|cs=[]|vb=()|nu=[]|fs=[]");, AddLanguageSpecificTextSet("LSTFD7331B5\_4?cpp=array&lt;");Int32AddLanguageSpecificTextSet("LSTFD7331B5\_5?cpp=&gt;|cs=[]|vb=()|nu=[]|fs=[]");)](M_Grasshopper_Kernel_GH_UpgradeUtil_MigrateInputParameters_1.htm) | Migrate a bunch of input parameters. |
| Public methodStatic member | [MigrateOutputParameters(IGH\_Component, IGH\_Component)](M_Grasshopper_Kernel_GH_UpgradeUtil_MigrateOutputParameters.htm) | Migrate all output parameters. |
| Public methodStatic member | [MigrateOutputParameters(IGH\_Component, IGH\_Component, AddLanguageSpecificTextSet("LSTFD7331B5\_6?cpp=array&lt;");Int32AddLanguageSpecificTextSet("LSTFD7331B5\_7?cpp=&gt;|cs=[]|vb=()|nu=[]|fs=[]");, AddLanguageSpecificTextSet("LSTFD7331B5\_8?cpp=array&lt;");Int32AddLanguageSpecificTextSet("LSTFD7331B5\_9?cpp=&gt;|cs=[]|vb=()|nu=[]|fs=[]");)](M_Grasshopper_Kernel_GH_UpgradeUtil_MigrateOutputParameters_1.htm) | Migrate a bunch of output parameters. |
| Public methodStatic member | [MigrateRecipients(IEnumerableAddLanguageSpecificTextSet("LSTFD7331B5\_10?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");IGH\_ParamAddLanguageSpecificTextSet("LSTFD7331B5\_11?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");, IGH\_Param)](M_Grasshopper_Kernel_GH_UpgradeUtil_MigrateRecipients_1.htm) | Utility method for bulk assigning a bunch of sources. |
| Public methodStatic member | [MigrateRecipients(IGH\_Param, IGH\_Param)](M_Grasshopper_Kernel_GH_UpgradeUtil_MigrateRecipients.htm) | Migrate all recipients from A to B, while maintaining order. |
| Public methodStatic member | [MigrateSources(IEnumerableAddLanguageSpecificTextSet("LSTFD7331B5\_12?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");IGH\_ParamAddLanguageSpecificTextSet("LSTFD7331B5\_13?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");, IGH\_Param)](M_Grasshopper_Kernel_GH_UpgradeUtil_MigrateSources_1.htm) | Utility method for bulk assigning a bunch of sources. |
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

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)