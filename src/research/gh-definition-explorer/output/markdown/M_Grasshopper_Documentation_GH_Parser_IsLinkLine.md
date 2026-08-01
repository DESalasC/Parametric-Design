# M_Grasshopper_Documentation_GH_Parser_IsLinkLine

﻿ GH\_Parser.IsLinkLine Method (String)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Documentation](../html/N_Grasshopper_Documentation.htm "Grasshopper.Documentation")

[GH\_Parser Class](../html/T_Grasshopper_Documentation_GH_Parser.htm "GH_Parser Class")

[GH\_Parser Methods](../html/Methods_T_Grasshopper_Documentation_GH_Parser.htm "GH_Parser Methods")

[IsLinkLine Method](../html/Overload_Grasshopper_Documentation_GH_Parser_IsLinkLine.htm "IsLinkLine Method ")

[IsLinkLine Method (String)](../html/M_Grasshopper_Documentation_GH_Parser_IsLinkLine.htm "IsLinkLine Method (String)")

[IsLinkLine Method (String, String, String, String)](../html/M_Grasshopper_Documentation_GH_Parser_IsLinkLine_1.htm "IsLinkLine Method (String, String, String, String)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ParserAddLanguageSpecificTextSet("LST2EB7552B\_0?cpp=::|nu=.");IsLinkLine Method (String) |

Test whether a line represents a referenced link target.
Note; this is a quick check. The link might still be invalid,
use the IsLinkLine overload to include validity checks.

**Namespace:**
 [Grasshopper.Documentation](N_Grasshopper_Documentation.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static bool IsLinkLine(
	string line
)
```

```
Public Shared Function IsLinkLine ( 
	line As String
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

line
:   Type: [SystemAddLanguageSpecificTextSet("LST2EB7552B\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Line to test.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True if the line is a referenced link.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Parser Class](T_Grasshopper_Documentation_GH_Parser.htm)

[IsLinkLine Overload](Overload_Grasshopper_Documentation_GH_Parser_IsLinkLine.htm)

[Grasshopper.Documentation Namespace](N_Grasshopper_Documentation.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)