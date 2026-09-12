# M_GH_IO_Types_GH_Version_op_LessThan

﻿ GH\_Version.LessThan Operator 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Types](../html/N_GH_IO_Types.htm "GH_IO.Types")

[GH\_Version Structure](../html/T_GH_IO_Types_GH_Version.htm "GH_Version Structure")

[GH\_Version Operators](../html/Operators_T_GH_IO_Types_GH_Version.htm "GH_Version Operators")

[Equality Operator](../html/M_GH_IO_Types_GH_Version_op_Equality.htm "Equality Operator ")

[GreaterThan Operator](../html/M_GH_IO_Types_GH_Version_op_GreaterThan.htm "GreaterThan Operator ")

[GreaterThanOrEqual Operator](../html/M_GH_IO_Types_GH_Version_op_GreaterThanOrEqual.htm "GreaterThanOrEqual Operator ")

[Inequality Operator](../html/M_GH_IO_Types_GH_Version_op_Inequality.htm "Inequality Operator ")

[LessThan Operator](../html/M_GH_IO_Types_GH_Version_op_LessThan.htm "LessThan Operator ")

[LessThanOrEqual Operator](../html/M_GH_IO_Types_GH_Version_op_LessThanOrEqual.htm "LessThanOrEqual Operator ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_VersionAddLanguageSpecificTextSet("LST30D95071\_0?cpp=::|nu=.");LessThan Operator |

Compares versions for smaller than relationships.

**Namespace:**
 [GH\_IO.Types](N_GH_IO_Types.htm)  
**Assembly:**
 GH\_IO (in GH\_IO.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static bool operator <(
	GH_Version A,
	GH_Version B
)
```

```
Public Shared Operator < ( 
	A As GH_Version,
	B As GH_Version
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

A
:   Type: [GH\_IO.TypesAddLanguageSpecificTextSet("LST30D95071\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Version](T_GH_IO_Types_GH_Version.htm)  
    Version to compare.

B
:   Type: [GH\_IO.TypesAddLanguageSpecificTextSet("LST30D95071\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Version](T_GH_IO_Types_GH_Version.htm)  
    Version to compare with.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True if A represents an older version than B.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Version Structure](T_GH_IO_Types_GH_Version.htm)

[GH\_IO.Types Namespace](N_GH_IO_Types.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)