# T_GH_IO_VersionNumber

﻿ VersionNumber Structure

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO](../html/N_GH_IO.htm "GH_IO")

[VersionNumber Structure](../html/T_GH_IO_VersionNumber.htm "VersionNumber Structure")

[VersionNumber Constructor](../html/Overload_GH_IO_VersionNumber__ctor.htm "VersionNumber Constructor ")

[VersionNumber Properties](../html/Properties_T_GH_IO_VersionNumber.htm "VersionNumber Properties")

[VersionNumber Methods](../html/Methods_T_GH_IO_VersionNumber.htm "VersionNumber Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| VersionNumber Structure |

Represents a product version number that encodes major, minor, time and build branch information.
as major.minor.yyddd.hhmmb where:
yy = year of build - 2000
ddd = year day of build (1-366)
hh = hour of build
mm = minute of build
b = branch of build

**Namespace:**
 [GH\_IO](N_GH_IO.htm)  
**Assembly:**
 GH\_IO (in GH\_IO.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
[SerializableAttribute]
public struct VersionNumber : IComparable, 
	IComparable<VersionNumber>
```

```
<SerializableAttribute>
Public Structure VersionNumber
	Implements IComparable, IComparable(Of VersionNumber)
```

AddLanguageTabSet("ID0EBCA");

The VersionNumber type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [VersionNumber(Version)](M_GH_IO_VersionNumber__ctor_2.htm) | Construct VersionNumber based on existing System.Version class. |
| Public method | [VersionNumber(Int32, Int32, DateTime, VersionNumberAddLanguageSpecificTextSet("LST2C2BF58D\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Branch)](M_GH_IO_VersionNumber__ctor.htm) | Initializes a new instance of the VersionNumber structure to the version specified by the parameters. |
| Public method | [VersionNumber(Int32, Int32, Int32, Int32)](M_GH_IO_VersionNumber__ctor_1.htm) | Initializes a new instance of the VersionNumber structure to the version specified by the version quartet values. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [BuildBranch](P_GH_IO_VersionNumber_BuildBranch.htm) | Gets the build branch component of this instance. |
| Public property | [IsValid](P_GH_IO_VersionNumber_IsValid.htm) | True when all information in the VersionNumber has valid values. |
| Public property | [Major](P_GH_IO_VersionNumber_Major.htm) | Gets the major version number component of this instance. |
| Public propertyStatic member | [MaxMajorVersionNumber](P_GH_IO_VersionNumber_MaxMajorVersionNumber.htm) | The largest possible valid value of VersionNumber.MajorVersionNumber. |
| Public propertyStatic member | [MaxMinorVersionNumber](P_GH_IO_VersionNumber_MaxMinorVersionNumber.htm) | The largest possible valid value of VersionNumber.MinorVersionNumber. |
| Public propertyStatic member | [MaxValid](P_GH_IO_VersionNumber_MaxValid.htm) | The largest possible valid VersionNumber. |
| Public propertyStatic member | [MaxValidBuildBranch](P_GH_IO_VersionNumber_MaxValidBuildBranch.htm) | Represents the largest possible valid value of VersionNumber.BuildBranch. This field is read-only. |
| Public propertyStatic member | [MaxValidTime](P_GH_IO_VersionNumber_MaxValidTime.htm) | The largest possible valid value of VersionNumber.Time. This field is read-only. |
| Public propertyStatic member | [MinMajorVersionNumber](P_GH_IO_VersionNumber_MinMajorVersionNumber.htm) | The smallest possible valid value of VersionNumber.MajorVersionNumber. |
| Public propertyStatic member | [MinMinorVersionNumber](P_GH_IO_VersionNumber_MinMinorVersionNumber.htm) | The smallest possible valid value of VersionNumber.MinorVersionNumber. |
| Public property | [Minor](P_GH_IO_VersionNumber_Minor.htm) | Gets the minor version number component of this instance. |
| Public propertyStatic member | [MinValid](P_GH_IO_VersionNumber_MinValid.htm) | The smallest possible valid VersionNumber. |
| Public propertyStatic member | [MinValidBuildBranch](P_GH_IO_VersionNumber_MinValidBuildBranch.htm) | Represents the smallest possible valid value of VersionNumber.BuildBranch. This field is read-only. |
| Public propertyStatic member | [MinValidTime](P_GH_IO_VersionNumber_MinValidTime.htm) | The smallest possible valid value of VersionNumber.Time. This field is read-only. |
| Public property | [Time](P_GH_IO_VersionNumber_Time.htm) | Gets the version time component of this instance. |
| Public propertyStatic member | [Unset](P_GH_IO_VersionNumber_Unset.htm) | The Unset VersionNumber. VersionNumber.Unset.IsValid is false. |
| Public propertyStatic member | [UnsetBuildBranch](P_GH_IO_VersionNumber_UnsetBuildBranch.htm) | The value of an Unset VersionNumber.BuildBranch. |
| Public propertyStatic member | [UnsetTime](P_GH_IO_VersionNumber_UnsetTime.htm) | The value of an Unset VersionNumber.Time. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [CompareTo(Object)](M_GH_IO_VersionNumber_CompareTo_1.htm) | Compares the value of this instance to a specified VersionNumber value and returns an integer that indicates whether this instance is earlier than, the same as, or later than the specified VersionNumber value. |
| Public method | [CompareTo(VersionNumber)](M_GH_IO_VersionNumber_CompareTo.htm) | Compares the value of this instance to a specified VersionNumber value and returns an integer that indicates whether this instance is earlier than, the same as, or later than the specified VersionNumber value. |
| Public method | [ToString](M_GH_IO_VersionNumber_ToString.htm) | Converts the value of the current VersionNumber object to its equivalent string representation major.minor.yyddd.hhmmb. (Overrides ValueType.ToString().) (Overrides [ValueTypeAddLanguageSpecificTextSet("LST2C2BF58D\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");ToStringAddLanguageSpecificTextSet("LST2C2BF58D\_2?cs=()|vb=|cpp=()|nu=()|fs=()");](https://docs.microsoft.com/dotnet/api/system.valuetype.tostring#system-valuetype-tostring).) |
| Public method | [ToVersion](M_GH_IO_VersionNumber_ToVersion.htm) | Convert this VersionNumber class to System.Version() |
| Public methodStatic member | [TryParse(String, VersionNumberAddLanguageSpecificTextSet("LST2C2BF58D\_3?cpp=%");)](M_GH_IO_VersionNumber_TryParse.htm) | Converts the specified string representation of a version number to its VersionNumber equivalent and returns a value that indicates whether the conversion succeeded. |
| Public methodStatic member | [TryParse(Version, VersionNumberAddLanguageSpecificTextSet("LST2C2BF58D\_4?cpp=%");)](M_GH_IO_VersionNumber_TryParse_1.htm) | Attempt so convert the System.Version representation of a version number to its VersionNumber equivalent and returns a value that indicates whether the conversion succeeded. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_IO Namespace](N_GH_IO.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)