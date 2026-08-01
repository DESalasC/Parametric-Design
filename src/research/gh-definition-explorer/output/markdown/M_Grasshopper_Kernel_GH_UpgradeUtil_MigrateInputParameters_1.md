# M_Grasshopper_Kernel_GH_UpgradeUtil_MigrateInputParameters_1

﻿ GH\_UpgradeUtil.MigrateInputParameters Method (IGH\_Component, IGH\_Component, Int32[], Int32[])

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
| GH\_UpgradeUtilAddLanguageSpecificTextSet("LSTE6A33C1B\_0?cpp=::|nu=.");MigrateInputParameters Method (IGH\_Component, IGH\_Component, AddLanguageSpecificTextSet("LSTE6A33C1B\_1?cpp=array&lt;");Int32AddLanguageSpecificTextSet("LSTE6A33C1B\_2?cpp=&gt;|vb=()|nu=[]");, AddLanguageSpecificTextSet("LSTE6A33C1B\_3?cpp=array&lt;");Int32AddLanguageSpecificTextSet("LSTE6A33C1B\_4?cpp=&gt;|vb=()|nu=[]");) |

Migrate a bunch of input parameters.

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
	IGH_Component target,
	int[] index0,
	int[] index1
)
```

```
Public Shared Function MigrateInputParameters ( 
	source As IGH_Component,
	target As IGH_Component,
	index0 As Integer(),
	index1 As Integer()
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

source
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LSTE6A33C1B\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");IGH\_Component](T_Grasshopper_Kernel_IGH_Component.htm)  
    Source component.

target
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LSTE6A33C1B\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");IGH\_Component](T_Grasshopper_Kernel_IGH_Component.htm)  
    Target component.

index0
:   Type: AddLanguageSpecificTextSet("LSTE6A33C1B\_7?cpp=array&lt;");[SystemAddLanguageSpecificTextSet("LSTE6A33C1B\_8?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)AddLanguageSpecificTextSet("LSTE6A33C1B\_9?cpp=&gt;|vb=()|nu=[]");  
    List of input indices to migrate.

index1
:   Type: AddLanguageSpecificTextSet("LSTE6A33C1B\_10?cpp=array&lt;");[SystemAddLanguageSpecificTextSet("LSTE6A33C1B\_11?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)AddLanguageSpecificTextSet("LSTE6A33C1B\_12?cpp=&gt;|vb=()|nu=[]");  
    Matching list of target indices.

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