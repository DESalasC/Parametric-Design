# M_GH_IO_VersionNumber_TryParse_1

﻿ VersionNumber.TryParse Method (Version, VersionNumber)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO](../html/N_GH_IO.htm "GH_IO")

[VersionNumber Structure](../html/T_GH_IO_VersionNumber.htm "VersionNumber Structure")

[VersionNumber Methods](../html/Methods_T_GH_IO_VersionNumber.htm "VersionNumber Methods")

[TryParse Method](../html/Overload_GH_IO_VersionNumber_TryParse.htm "TryParse Method ")

[TryParse Method (String, VersionNumber)](../html/M_GH_IO_VersionNumber_TryParse.htm "TryParse Method (String, VersionNumber)")

[TryParse Method (Version, VersionNumber)](../html/M_GH_IO_VersionNumber_TryParse_1.htm "TryParse Method (Version, VersionNumber)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| VersionNumberAddLanguageSpecificTextSet("LST582F7AA7\_0?cpp=::|nu=.");TryParse Method (Version, VersionNumberAddLanguageSpecificTextSet("LST582F7AA7\_1?cpp=%");) |

Attempt so convert the System.Version representation of a version number to its VersionNumber equivalent and returns a value that indicates whether the conversion succeeded.

**Namespace:**
 [GH\_IO](N_GH_IO.htm)  
**Assembly:**
 GH\_IO (in GH\_IO.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static bool TryParse(
	Version v,
	out VersionNumber result
)
```

```
Public Shared Function TryParse ( 
	v As Version,
	<OutAttribute> ByRef result As VersionNumber
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

v
:   Type: [SystemAddLanguageSpecificTextSet("LST582F7AA7\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Version](https://docs.microsoft.com/dotnet/api/system.version)  
    A version number with quartet values (v.Major, v.Minor, v.Build, v.Revision) that are valid ((0 to 63),(0 to 127), (1 to 99365), (0 to 23593)).

result
:   Type: [GH\_IOAddLanguageSpecificTextSet("LST582F7AA7\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");VersionNumber](T_GH_IO_VersionNumber.htm)AddLanguageSpecificTextSet("LST582F7AA7\_4?cpp=%");  
    When this method returns, result contains the VersionNumber value equivalent to the version number contained in v, if the conversion succeeded, or VersionNumber.Unset if the conversion failed. The conversion fails if the v parameter is null, is an empty string (""), or does not contain a valid string representation of version number. This parameter is passed uninitialized.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)

![](../icons/SectionExpanded.png)See Also

#### Reference

[VersionNumber Structure](T_GH_IO_VersionNumber.htm)

[TryParse Overload](Overload_GH_IO_VersionNumber_TryParse.htm)

[GH\_IO Namespace](N_GH_IO.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)