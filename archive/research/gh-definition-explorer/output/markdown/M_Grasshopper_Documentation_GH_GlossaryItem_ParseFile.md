# M_Grasshopper_Documentation_GH_GlossaryItem_ParseFile

﻿ GH\_GlossaryItem.ParseFile Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Documentation](../html/N_Grasshopper_Documentation.htm "Grasshopper.Documentation")

[GH\_GlossaryItem Class](../html/T_Grasshopper_Documentation_GH_GlossaryItem.htm "GH_GlossaryItem Class")

[GH\_GlossaryItem Methods](../html/Methods_T_Grasshopper_Documentation_GH_GlossaryItem.htm "GH_GlossaryItem Methods")

[ParseFile Method](../html/M_Grasshopper_Documentation_GH_GlossaryItem_ParseFile.htm "ParseFile Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_GlossaryItemAddLanguageSpecificTextSet("LSTC77FEBAC\_0?cpp=::|nu=.");ParseFile Method |

Parse a \*.glossary file and return a glossary entry.

**Namespace:**
 [Grasshopper.Documentation](N_Grasshopper_Documentation.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static GH_GlossaryItem ParseFile(
	string path
)
```

```
Public Shared Function ParseFile ( 
	path As String
) As GH_GlossaryItem
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

path
:   Type: [SystemAddLanguageSpecificTextSet("LSTC77FEBAC\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    File to parse.

#### Return Value

Type: [GH\_GlossaryItem](T_Grasshopper_Documentation_GH_GlossaryItem.htm)  
The glossary entry defined by the file. This function always returns a valid glossary or it throws an exception.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_GlossaryItem Class](T_Grasshopper_Documentation_GH_GlossaryItem.htm)

[Grasshopper.Documentation Namespace](N_Grasshopper_Documentation.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)