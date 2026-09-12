# M_GH_IO_VersionNumber__ctor

﻿ VersionNumber Constructor (Int32, Int32, DateTime, VersionNumber.Branch)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO](../html/N_GH_IO.htm "GH_IO")

[VersionNumber Structure](../html/T_GH_IO_VersionNumber.htm "VersionNumber Structure")

[VersionNumber Constructor](../html/Overload_GH_IO_VersionNumber__ctor.htm "VersionNumber Constructor ")

[VersionNumber Constructor (Version)](../html/M_GH_IO_VersionNumber__ctor_2.htm "VersionNumber Constructor (Version)")

[VersionNumber Constructor (Int32, Int32, DateTime, VersionNumber.Branch)](../html/M_GH_IO_VersionNumber__ctor.htm "VersionNumber Constructor (Int32, Int32, DateTime, VersionNumber.Branch)")

[VersionNumber Constructor (Int32, Int32, Int32, Int32)](../html/M_GH_IO_VersionNumber__ctor_1.htm "VersionNumber Constructor (Int32, Int32, Int32, Int32)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| VersionNumber Constructor (Int32, Int32, DateTime, VersionNumberAddLanguageSpecificTextSet("LSTB6FB44F0\_0?cpp=::|nu=.");Branch) |

Initializes a new instance of the VersionNumber structure to the version specified by the parameters.

**Namespace:**
 [GH\_IO](N_GH_IO.htm)  
**Assembly:**
 GH\_IO (in GH\_IO.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public VersionNumber(
	int major,
	int minor,
	DateTime time,
	VersionNumberAddLanguageSpecificTextSet("LSTB6FB44F0_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Branch buildBranch
)
```

```
Public Sub New ( 
	major As Integer,
	minor As Integer,
	time As DateTime,
	buildBranch As VersionNumberAddLanguageSpecificTextSet("LSTB6FB44F0_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Branch
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

major
:   Type: [SystemAddLanguageSpecificTextSet("LSTB6FB44F0\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    The major version number (0 through 63).

minor
:   Type: [SystemAddLanguageSpecificTextSet("LSTB6FB44F0\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    The minor version number (0 through 127).

time
:   Type: [SystemAddLanguageSpecificTextSet("LSTB6FB44F0\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");DateTime](https://docs.microsoft.com/dotnet/api/system.datetime)  
    The time is the version time (January 1, 2000 00:00 through December 31 23:59). Seconds are ignored.

buildBranch
:   Type: [GH\_IOAddLanguageSpecificTextSet("LSTB6FB44F0\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");VersionNumberAddLanguageSpecificTextSet("LSTB6FB44F0\_7?cs=.|vb=.|cpp=::|nu=.|fs=.");Branch](T_GH_IO_VersionNumber_Branch.htm)  
    The branch used to build the product (developer, trunk, release\_candidate, or release).

![](../icons/SectionExpanded.png)See Also

#### Reference

[VersionNumber Structure](T_GH_IO_VersionNumber.htm)

[VersionNumber Overload](Overload_GH_IO_VersionNumber__ctor.htm)

[GH\_IO Namespace](N_GH_IO.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)