# M_GH_IO_VersionNumber_TryParse

﻿ VersionNumber.TryParse Method (String, VersionNumber)

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
| VersionNumberAddLanguageSpecificTextSet("LSTCAE9E9C1\_0?cpp=::|nu=.");TryParse Method (String, VersionNumberAddLanguageSpecificTextSet("LSTCAE9E9C1\_1?cpp=%");) |

Converts the specified string representation of a version number to its VersionNumber equivalent and returns a value that indicates whether the conversion succeeded.

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
	string s,
	out VersionNumber result
)
```

```
Public Shared Function TryParse ( 
	s As String,
	<OutAttribute> ByRef result As VersionNumber
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

s
:   Type: [SystemAddLanguageSpecificTextSet("LSTCAE9E9C1\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    A string containing four integers separated by full stops in the format major.minor.yyddd.hhmmb, where yy is year-2000, ddd is the day of the year, hh is the hour, mm is the minute and b identifies the build branch.

result
:   Type: [GH\_IOAddLanguageSpecificTextSet("LSTCAE9E9C1\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");VersionNumber](T_GH_IO_VersionNumber.htm)AddLanguageSpecificTextSet("LSTCAE9E9C1\_4?cpp=%");  
    When this method returns, result contains the VersionNumber value equivalent to the version number contained in s, if the conversion succeeded, or VersionNumber.Unset if the conversion failed. The conversion fails if the s parameter is null, is an empty string (""), or does not contain a valid string representation of version number. This parameter is passed uninitialized.

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