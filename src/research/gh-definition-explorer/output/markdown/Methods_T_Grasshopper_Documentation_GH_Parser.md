# Methods_T_Grasshopper_Documentation_GH_Parser

﻿ GH\_Parser Methods

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
| GH\_Parser Methods |

The [GH\_Parser](T_Grasshopper_Documentation_GH_Parser.htm) type exposes the following members.

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public methodStatic member | [IsChapterHeaderLine](M_Grasshopper_Documentation_GH_Parser_IsChapterHeaderLine.htm) | Test whether a line represents a chapter header underline. Chapter header underlines contain at least 4 consecutive equals symbols preceded or followed by any amount of white space. |
| Public methodStatic member | [IsCommentLine](M_Grasshopper_Documentation_GH_Parser_IsCommentLine.htm) | Test whether a line is a comment. Commented lines begin with double slashes (//) and are ignored during parsing. |
| Public methodStatic member | [IsLinkLine(String)](M_Grasshopper_Documentation_GH_Parser_IsLinkLine.htm) | Test whether a line represents a referenced link target. Note; this is a quick check. The link might still be invalid, use the IsLinkLine overload to include validity checks. |
| Public methodStatic member | [IsLinkLine(String, StringAddLanguageSpecificTextSet("LSTB9024681\_0?cpp=%");, StringAddLanguageSpecificTextSet("LSTB9024681\_1?cpp=%");, StringAddLanguageSpecificTextSet("LSTB9024681\_2?cpp=%");)](M_Grasshopper_Documentation_GH_Parser_IsLinkLine_1.htm) | Test whether a line represents a referenced link target. |
| Public methodStatic member | [IsListLine](M_Grasshopper_Documentation_GH_Parser_IsListLine.htm) | Test whether a line contains a list item. |
| Public methodStatic member | [IsParagraphHeaderLine](M_Grasshopper_Documentation_GH_Parser_IsParagraphHeaderLine.htm) | Test whether a line represents a paragraph header underline. Paragraph header underlines contain at least 4 consecutive dashes preceded or followed by any amount of white space. |
| Public methodStatic member | [IsQuoteLine](M_Grasshopper_Documentation_GH_Parser_IsQuoteLine.htm) | Test whether a line is a block quote line. Block quotes start with a larger than symbol. |
| Public methodStatic member | [StringToFragment](M_Grasshopper_Documentation_GH_Parser_StringToFragment.htm) | Parse a block of text and return it as an interpreted IGH\_Fragment. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Parser Class](T_Grasshopper_Documentation_GH_Parser.htm)

[Grasshopper.Documentation Namespace](N_Grasshopper_Documentation.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)