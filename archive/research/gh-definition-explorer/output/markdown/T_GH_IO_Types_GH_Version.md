# T_GH_IO_Types_GH_Version

﻿ GH\_Version Structure

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Types](../html/N_GH_IO_Types.htm "GH_IO.Types")

[GH\_Version Structure](../html/T_GH_IO_Types_GH_Version.htm "GH_Version Structure")

[GH\_Version Constructor](../html/Overload_GH_IO_Types_GH_Version__ctor.htm "GH_Version Constructor ")

[GH\_Version Methods](../html/Methods_T_GH_IO_Types_GH_Version.htm "GH_Version Methods")

[GH\_Version Operators](../html/Operators_T_GH_IO_Types_GH_Version.htm "GH_Version Operators")

[GH\_Version Fields](../html/Fields_T_GH_IO_Types_GH_Version.htm "GH_Version Fields")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_Version Structure |

Basic version type. Contains Major, Minor and Revision fields.

**Namespace:**
 [GH\_IO.Types](N_GH_IO_Types.htm)  
**Assembly:**
 GH\_IO (in GH\_IO.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public struct GH_Version
```

```
Public Structure GH_Version
```

AddLanguageTabSet("ID0EBCA");

The GH\_Version type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_Version(GH\_Version)](M_GH_IO_Types_GH_Version__ctor.htm) | Copy constructor. Duplicate an existing version structure. |
| Public method | [GH\_Version(Int32, Int32, Int32)](M_GH_IO_Types_GH_Version__ctor_1.htm) | Default constructor. Create a new version from specified fields. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [Equals](M_GH_IO_Types_GH_Version_Equals.htm) | Performs value equality comparison. (Overrides [ValueTypeAddLanguageSpecificTextSet("LSTF274161E\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Equals(Object)](https://docs.microsoft.com/dotnet/api/system.valuetype.equals#system-valuetype-equals(system-object)).) |
| Public method | [GetHashCode](M_GH_IO_Types_GH_Version_GetHashCode.htm) | Returns the hash code for this instance. (Overrides [ValueTypeAddLanguageSpecificTextSet("LSTF274161E\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GetHashCodeAddLanguageSpecificTextSet("LSTF274161E\_2?cs=()|vb=|cpp=()|nu=()|fs=()");](https://docs.microsoft.com/dotnet/api/system.valuetype.gethashcode#system-valuetype-gethashcode).) |
| Public method | [ToString](M_GH_IO_Types_GH_Version_ToString.htm) | Default formatter for Version data: M.m.RRRR Revision section is padded with zeroes until it is at least 4 digits long. (Overrides [ValueTypeAddLanguageSpecificTextSet("LSTF274161E\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");ToStringAddLanguageSpecificTextSet("LSTF274161E\_4?cs=()|vb=|cpp=()|nu=()|fs=()");](https://docs.microsoft.com/dotnet/api/system.valuetype.tostring#system-valuetype-tostring).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Operators

|  | Name | Description |
| --- | --- | --- |
| Public operatorStatic member | [Equality](M_GH_IO_Types_GH_Version_op_Equality.htm) | Compares two version structures for equality. |
| Public operatorStatic member | [GreaterThan](M_GH_IO_Types_GH_Version_op_GreaterThan.htm) | Compares versions for larger than relationships. |
| Public operatorStatic member | [GreaterThanOrEqual](M_GH_IO_Types_GH_Version_op_GreaterThanOrEqual.htm) | Compares versions for larger than or equal to relationships. |
| Public operatorStatic member | [Inequality](M_GH_IO_Types_GH_Version_op_Inequality.htm) | Compares two version structures for inequality. |
| Public operatorStatic member | [LessThan](M_GH_IO_Types_GH_Version_op_LessThan.htm) | Compares versions for smaller than relationships. |
| Public operatorStatic member | [LessThanOrEqual](M_GH_IO_Types_GH_Version_op_LessThanOrEqual.htm) | Compares versions for smaller than or equal to relationships. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Fields

|  | Name | Description |
| --- | --- | --- |
| Public field | [major](F_GH_IO_Types_GH_Version_major.htm) | Major component of version structure. |
| Public field | [minor](F_GH_IO_Types_GH_Version_minor.htm) | Minor component of version structure. |
| Public field | [revision](F_GH_IO_Types_GH_Version_revision.htm) | Revision component of version structure. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_IO.Types Namespace](N_GH_IO_Types.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)