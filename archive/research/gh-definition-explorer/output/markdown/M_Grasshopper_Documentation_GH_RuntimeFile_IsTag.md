# M_Grasshopper_Documentation_GH_RuntimeFile_IsTag

﻿ GH\_RuntimeFile.IsTag Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Documentation](../html/N_Grasshopper_Documentation.htm "Grasshopper.Documentation")

[GH\_RuntimeFile Class](../html/T_Grasshopper_Documentation_GH_RuntimeFile.htm "GH_RuntimeFile Class")

[GH\_RuntimeFile Methods](../html/Methods_T_Grasshopper_Documentation_GH_RuntimeFile.htm "GH_RuntimeFile Methods")

[ContainsKey Method](../html/M_Grasshopper_Documentation_GH_RuntimeFile_ContainsKey.htm "ContainsKey Method ")

[IsTag Method](../html/M_Grasshopper_Documentation_GH_RuntimeFile_IsTag.htm "IsTag Method ")

[IsTagLine Method](../html/M_Grasshopper_Documentation_GH_RuntimeFile_IsTagLine.htm "IsTagLine Method ")

[ParseFile Method](../html/M_Grasshopper_Documentation_GH_RuntimeFile_ParseFile.htm "ParseFile Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_RuntimeFileAddLanguageSpecificTextSet("LSTEF1AE0C9\_0?cpp=::|nu=.");IsTag Method |

Tests whether a string is a predefined Grasshopper Help keyword.

**Namespace:**
 [Grasshopper.Documentation](N_Grasshopper_Documentation.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static bool IsTag(
	string text
)
```

```
Public Shared Function IsTag ( 
	text As String
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

text
:   Type: [SystemAddLanguageSpecificTextSet("LSTEF1AE0C9\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    String to test. Should contain no whitespace, but does not need to properly cased.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True if text is a predefined keyword, false if not.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_RuntimeFile Class](T_Grasshopper_Documentation_GH_RuntimeFile.htm)

[Grasshopper.Documentation Namespace](N_Grasshopper_Documentation.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)