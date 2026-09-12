# M_Grasshopper_Kernel_GH_Param_1_ReplaceSource_1

﻿ GH\_Param(T).ReplaceSource Method (Guid, IGH\_Param)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_Param(T) Class](../html/T_Grasshopper_Kernel_GH_Param_1.htm "GH_Param(T) Class")

[GH\_Param(T) Methods](../html/Methods_T_Grasshopper_Kernel_GH_Param_1.htm "GH_Param(T) Methods")

[ReplaceSource Method](../html/Overload_Grasshopper_Kernel_GH_Param_1_ReplaceSource.htm "ReplaceSource Method ")

[ReplaceSource Method (Guid, IGH\_Param)](../html/M_Grasshopper_Kernel_GH_Param_1_ReplaceSource_1.htm "ReplaceSource Method (Guid, IGH_Param)")

[ReplaceSource Method (IGH\_Param, IGH\_Param)](../html/M_Grasshopper_Kernel_GH_Param_1_ReplaceSource.htm "ReplaceSource Method (IGH_Param, IGH_Param)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ParamAddLanguageSpecificTextSet("LSTF28A9F2C\_0?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTF28A9F2C\_1?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");AddLanguageSpecificTextSet("LSTF28A9F2C\_2?cpp=::|nu=.");ReplaceSource Method (Guid, IGH\_Param) |

Replace an existing source with a new one. If the old\_source
does not exist in this parameter, nothing happens.

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public virtual void ReplaceSource(
	Guid old_source_id,
	IGH_Param new_source
)
```

```
Public Overridable Sub ReplaceSource ( 
	old_source_id As Guid,
	new_source As IGH_Param
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

old\_source\_id
:   Type: [SystemAddLanguageSpecificTextSet("LSTF28A9F2C\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Guid](https://docs.microsoft.com/dotnet/api/system.guid)  
    Source to replace.

new\_source
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LSTF28A9F2C\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");IGH\_Param](T_Grasshopper_Kernel_IGH_Param.htm)  
    Source to replace with.

#### Implements

[IGH\_ParamAddLanguageSpecificTextSet("LSTF28A9F2C\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");ReplaceSource(Guid, IGH\_Param)](M_Grasshopper_Kernel_IGH_Param_ReplaceSource_1.htm)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_ParamAddLanguageSpecificTextSet("LSTF28A9F2C\_6?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTF28A9F2C\_7?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;"); Class](T_Grasshopper_Kernel_GH_Param_1.htm)

[ReplaceSource Overload](Overload_Grasshopper_Kernel_GH_Param_1_ReplaceSource.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)