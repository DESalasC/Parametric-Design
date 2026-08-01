# M_GH_IO_VersionNumber__ctor_1

﻿ VersionNumber Constructor (Int32, Int32, Int32, Int32)

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
| VersionNumber Constructor (Int32, Int32, Int32, Int32) |

Initializes a new instance of the VersionNumber structure to the version specified by the version quartet values.

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
	int majorVersionNumber,
	int minorVersionNumber,
	int versionQuartetYyddd,
	int versionQuartetHhmmb
)
```

```
Public Sub New ( 
	majorVersionNumber As Integer,
	minorVersionNumber As Integer,
	versionQuartetYyddd As Integer,
	versionQuartetHhmmb As Integer
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

majorVersionNumber
:   Type: [SystemAddLanguageSpecificTextSet("LSTDDF335E8\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    The major version number (0 through 63).

minorVersionNumber
:   Type: [SystemAddLanguageSpecificTextSet("LSTDDF335E8\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    The minor version number (0 through 127)

versionQuartetYyddd
:   Type: [SystemAddLanguageSpecificTextSet("LSTDDF335E8\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    The third version quartet value is (year - 2000)\*1000 + yday, where year is 2000 to 2099 and yday is 1 to the number of days in the specified year.

versionQuartetHhmmb
:   Type: [SystemAddLanguageSpecificTextSet("LSTDDF335E8\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    The forth version quartet value is (hour\*1000 + minute\*10 + branch) where hour is 0 to 23, minute is 0 to 59, and branch is 0 to 3.

![](../icons/SectionExpanded.png)See Also

#### Reference

[VersionNumber Structure](T_GH_IO_VersionNumber.htm)

[VersionNumber Overload](Overload_GH_IO_VersionNumber__ctor.htm)

[GH\_IO Namespace](N_GH_IO.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)