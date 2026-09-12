# T_Grasshopper_Kernel_Data_GH_IndexRange

﻿ GH\_IndexRange Structure

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel.Data](../html/N_Grasshopper_Kernel_Data.htm "Grasshopper.Kernel.Data")

[GH\_IndexRange Structure](../html/T_Grasshopper_Kernel_Data_GH_IndexRange.htm "GH_IndexRange Structure")

[GH\_IndexRange Constructor](../html/Overload_Grasshopper_Kernel_Data_GH_IndexRange__ctor.htm "GH_IndexRange Constructor ")

[GH\_IndexRange Properties](../html/Properties_T_Grasshopper_Kernel_Data_GH_IndexRange.htm "GH_IndexRange Properties")

[GH\_IndexRange Methods](../html/Methods_T_Grasshopper_Kernel_Data_GH_IndexRange.htm "GH_IndexRange Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_IndexRange Structure |

Represents a range of indices.

**Namespace:**
 [Grasshopper.Kernel.Data](N_Grasshopper_Kernel_Data.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public struct GH_IndexRange : GH_ISerializable
```

```
Public Structure GH_IndexRange
	Implements GH_ISerializable
```

AddLanguageTabSet("ID0EBCA");

The GH\_IndexRange type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_IndexRange(Int32)](M_Grasshopper_Kernel_Data_GH_IndexRange__ctor.htm) | Create a new singular range. |
| Public method | [GH\_IndexRange(Int32, Int32)](M_Grasshopper_Kernel_Data_GH_IndexRange__ctor_1.htm) | Create a new range. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Index0](P_Grasshopper_Kernel_Data_GH_IndexRange_Index0.htm) | Gets the first index in the range. |
| Public property | [Index1](P_Grasshopper_Kernel_Data_GH_IndexRange_Index1.htm) | Gets the last index in the range. |
| Public propertyStatic member | [InvalidRange](P_Grasshopper_Kernel_Data_GH_IndexRange_InvalidRange.htm) | Gets the predefined invalid range. |
| Public property | [IsSingular](P_Grasshopper_Kernel_Data_GH_IndexRange_IsSingular.htm) | Gets whether the range has zero length. |
| Public property | [IsValid](P_Grasshopper_Kernel_Data_GH_IndexRange_IsValid.htm) | Gets whether this range is valid. |
| Public property | [Length](P_Grasshopper_Kernel_Data_GH_IndexRange_Length.htm) | Gets the length of the range. |
| Public propertyStatic member | [MaxValue](P_Grasshopper_Kernel_Data_GH_IndexRange_MaxValue.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [AdjacentTo](M_Grasshopper_Kernel_Data_GH_IndexRange_AdjacentTo.htm) | Tests whether this range is adjacent to another. |
| Public method | [Contains(GH\_IndexRange)](M_Grasshopper_Kernel_Data_GH_IndexRange_Contains.htm) | Tests whether a specified range is entirely contained within this range. |
| Public method | [Contains(Int32)](M_Grasshopper_Kernel_Data_GH_IndexRange_Contains_1.htm) | Tests whether a specified index is defined by this range. |
| Public methodStatic member | [Intersection](M_Grasshopper_Kernel_Data_GH_IndexRange_Intersection.htm) | Create the intersection between two ranges. |
| Public method | [IntersectsWith](M_Grasshopper_Kernel_Data_GH_IndexRange_IntersectsWith.htm) | Tests whether certain indices are described by both this and another range. |
| Public methodStatic member | [Split](M_Grasshopper_Kernel_Data_GH_IndexRange_Split.htm) | Split a range into two using an integer index. |
| Public method | [ToString](M_Grasshopper_Kernel_Data_GH_IndexRange_ToString.htm) | (Overrides [ValueTypeAddLanguageSpecificTextSet("LST8FD650FE\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");ToStringAddLanguageSpecificTextSet("LST8FD650FE\_1?cs=()|vb=|cpp=()|nu=()|fs=()");](https://docs.microsoft.com/dotnet/api/system.valuetype.tostring#system-valuetype-tostring).) |
| Public methodStatic member | [Union](M_Grasshopper_Kernel_Data_GH_IndexRange_Union.htm) | Create a range which contains both input ranges. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Data Namespace](N_Grasshopper_Kernel_Data.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)