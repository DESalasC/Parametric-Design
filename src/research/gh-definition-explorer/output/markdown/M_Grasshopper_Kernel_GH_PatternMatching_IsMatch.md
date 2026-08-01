# M_Grasshopper_Kernel_GH_PatternMatching_IsMatch

﻿ GH\_PatternMatching.IsMatch Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH\_PatternMatching Class](../html/T_Grasshopper_Kernel_GH_PatternMatching.htm "GH_PatternMatching Class")

[GH\_PatternMatching Methods](../html/Methods_T_Grasshopper_Kernel_GH_PatternMatching.htm "GH_PatternMatching Methods")

[Contains Method](../html/M_Grasshopper_Kernel_GH_PatternMatching_Contains.htm "Contains Method ")

[EndsWith Method](../html/M_Grasshopper_Kernel_GH_PatternMatching_EndsWith.htm "EndsWith Method ")

[Equals Method](../html/M_Grasshopper_Kernel_GH_PatternMatching_Equals.htm "Equals Method ")

[IsMatch Method](../html/M_Grasshopper_Kernel_GH_PatternMatching_IsMatch.htm "IsMatch Method ")

[MatchRegex Method](../html/M_Grasshopper_Kernel_GH_PatternMatching_MatchRegex.htm "MatchRegex Method ")

[MatchWildcards Method](../html/M_Grasshopper_Kernel_GH_PatternMatching_MatchWildcards.htm "MatchWildcards Method ")

[StartsWith Method](../html/M_Grasshopper_Kernel_GH_PatternMatching_StartsWith.htm "StartsWith Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_PatternMatchingAddLanguageSpecificTextSet("LST2A1E1FC3\_0?cpp=::|nu=.");IsMatch Method |

**Namespace:**
 [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static bool IsMatch(
	GH_PatternMatchingAddLanguageSpecificTextSet("LST2A1E1FC3_1?cs=.|vb=.|cpp=::|nu=.|fs=.");MatchingMode mode,
	string value,
	string pattern,
	bool ignoreCase,
	CultureInfo culture
)
```

```
Public Shared Function IsMatch ( 
	mode As GH_PatternMatchingAddLanguageSpecificTextSet("LST2A1E1FC3_2?cs=.|vb=.|cpp=::|nu=.|fs=.");MatchingMode,
	value As String,
	pattern As String,
	ignoreCase As Boolean,
	culture As CultureInfo
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

mode
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LST2A1E1FC3\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_PatternMatchingAddLanguageSpecificTextSet("LST2A1E1FC3\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");MatchingMode](T_Grasshopper_Kernel_GH_PatternMatching_MatchingMode.htm)

value
:   Type: [SystemAddLanguageSpecificTextSet("LST2A1E1FC3\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)

pattern
:   Type: [SystemAddLanguageSpecificTextSet("LST2A1E1FC3\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)

ignoreCase
:   Type: [SystemAddLanguageSpecificTextSet("LST2A1E1FC3\_7?cs=.|vb=.|cpp=::|nu=.|fs=.");Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)

culture
:   Type: [System.GlobalizationAddLanguageSpecificTextSet("LST2A1E1FC3\_8?cs=.|vb=.|cpp=::|nu=.|fs=.");CultureInfo](https://docs.microsoft.com/dotnet/api/system.globalization.cultureinfo)

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_PatternMatching Class](T_Grasshopper_Kernel_GH_PatternMatching.htm)

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)