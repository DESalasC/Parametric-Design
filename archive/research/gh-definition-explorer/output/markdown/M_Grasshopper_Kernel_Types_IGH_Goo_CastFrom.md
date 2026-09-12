# M_Grasshopper_Kernel_Types_IGH_Goo_CastFrom

﻿ IGH\_Goo.CastFrom Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm "Grasshopper.Kernel.Types")

[IGH\_Goo Interface](../html/T_Grasshopper_Kernel_Types_IGH_Goo.htm "IGH_Goo Interface")

[IGH\_Goo Methods](../html/Methods_T_Grasshopper_Kernel_Types_IGH_Goo.htm "IGH_Goo Methods")

[CastFrom Method](../html/M_Grasshopper_Kernel_Types_IGH_Goo_CastFrom.htm "CastFrom Method ")

[CastTo(T) Method](../html/M_Grasshopper_Kernel_Types_IGH_Goo_CastTo__1.htm "CastTo(T) Method ")

[Duplicate Method](../html/M_Grasshopper_Kernel_Types_IGH_Goo_Duplicate.htm "Duplicate Method ")

[EmitProxy Method](../html/M_Grasshopper_Kernel_Types_IGH_Goo_EmitProxy.htm "EmitProxy Method ")

[ScriptVariable Method](../html/M_Grasshopper_Kernel_Types_IGH_Goo_ScriptVariable.htm "ScriptVariable Method ")

[ToString Method](../html/M_Grasshopper_Kernel_Types_IGH_Goo_ToString.htm "ToString Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_GooAddLanguageSpecificTextSet("LST35D3B136\_0?cpp=::|nu=.");CastFrom Method |

Attempt a cast from generic object

**Namespace:**
 [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
bool CastFrom(
	Object source
)
```

```
Function CastFrom ( 
	source As Object
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

source
:   Type: [SystemAddLanguageSpecificTextSet("LST35D3B136\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
    Reference to source of cast.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True on success, false on failure.

![](../icons/SectionExpanded.png)Remarks

If False, the contents of this instance are not to be trusted.

![](../icons/SectionExpanded.png)See Also

#### Reference

[IGH\_Goo Interface](T_Grasshopper_Kernel_Types_IGH_Goo.htm)

[Grasshopper.Kernel.Types Namespace](N_Grasshopper_Kernel_Types.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)