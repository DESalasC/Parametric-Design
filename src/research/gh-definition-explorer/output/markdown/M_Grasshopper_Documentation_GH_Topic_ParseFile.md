# M_Grasshopper_Documentation_GH_Topic_ParseFile

﻿ GH\_Topic.ParseFile Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Documentation](../html/N_Grasshopper_Documentation.htm "Grasshopper.Documentation")

[GH\_Topic Class](../html/T_Grasshopper_Documentation_GH_Topic.htm "GH_Topic Class")

[GH\_Topic Methods](../html/Methods_T_Grasshopper_Documentation_GH_Topic.htm "GH_Topic Methods")

[ParseFile Method](../html/M_Grasshopper_Documentation_GH_Topic_ParseFile.htm "ParseFile Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_TopicAddLanguageSpecificTextSet("LST546EF884\_0?cpp=::|nu=.");ParseFile Method |

Parse a \*.topic file and return a topic entry.

**Namespace:**
 [Grasshopper.Documentation](N_Grasshopper_Documentation.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static GH_Topic ParseFile(
	string path
)
```

```
Public Shared Function ParseFile ( 
	path As String
) As GH_Topic
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

path
:   Type: [SystemAddLanguageSpecificTextSet("LST546EF884\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    File to parse.

#### Return Value

Type: [GH\_Topic](T_Grasshopper_Documentation_GH_Topic.htm)  
The topic defined by the file. This function always returns a valid topic or it throws an exception.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Topic Class](T_Grasshopper_Documentation_GH_Topic.htm)

[Grasshopper.Documentation Namespace](N_Grasshopper_Documentation.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)