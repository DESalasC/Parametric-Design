# M_Grasshopper_Documentation_GH_Parser_IsCommentLine

﻿ GH\_Parser.IsCommentLine Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Documentation](../html/N_Grasshopper_Documentation.htm "Grasshopper.Documentation")

[GH\_Parser Class](../html/T_Grasshopper_Documentation_GH_Parser.htm "GH_Parser Class")

[GH\_Parser Methods](../html/Methods_T_Grasshopper_Documentation_GH_Parser.htm "GH_Parser Methods")

[IsChapterHeaderLine Method](../html/M_Grasshopper_Documentation_GH_Parser_IsChapterHeaderLine.htm "IsChapterHeaderLine Method ")

[IsCommentLine Method](../html/M_Grasshopper_Documentation_GH_Parser_IsCommentLine.htm "IsCommentLine Method ")

[IsLinkLine Method](../html/Overload_Grasshopper_Documentation_GH_Parser_IsLinkLine.htm "IsLinkLine Method ")

[IsListLine Method](../html/M_Grasshopper_Documentation_GH_Parser_IsListLine.htm "IsListLine Method ")

[IsParagraphHeaderLine Method](../html/M_Grasshopper_Documentation_GH_Parser_IsParagraphHeaderLine.htm "IsParagraphHeaderLine Method ")

[IsQuoteLine Method](../html/M_Grasshopper_Documentation_GH_Parser_IsQuoteLine.htm "IsQuoteLine Method ")

[StringToFragment Method](../html/M_Grasshopper_Documentation_GH_Parser_StringToFragment.htm "StringToFragment Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ParserAddLanguageSpecificTextSet("LSTC6FD3E5F\_0?cpp=::|nu=.");IsCommentLine Method |

Test whether a line is a comment.
Commented lines begin with double slashes (//) and are ignored during parsing.

**Namespace:**
 [Grasshopper.Documentation](N_Grasshopper_Documentation.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static bool IsCommentLine(
	string line
)
```

```
Public Shared Function IsCommentLine ( 
	line As String
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

line
:   Type: [SystemAddLanguageSpecificTextSet("LSTC6FD3E5F\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Line to test. If you supply a multi-line string, death's too good for you.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True if the line is a comment line.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Parser Class](T_Grasshopper_Documentation_GH_Parser.htm)

[Grasshopper.Documentation Namespace](N_Grasshopper_Documentation.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)