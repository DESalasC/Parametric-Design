# M_Grasshopper_Documentation_GH_RuntimeFile_ParseFile

﻿ GH\_RuntimeFile.ParseFile Method 

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
| GH\_RuntimeFileAddLanguageSpecificTextSet("LSTA948E4BD\_0?cpp=::|nu=.");ParseFile Method |

Parse a file and return the runtime representation of said file.

**Namespace:**
 [Grasshopper.Documentation](N_Grasshopper_Documentation.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static GH_RuntimeFile ParseFile(
	string path
)
```

```
Public Shared Function ParseFile ( 
	path As String
) As GH_RuntimeFile
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

path
:   Type: [SystemAddLanguageSpecificTextSet("LSTA948E4BD\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Path to file.

#### Return Value

Type: [GH\_RuntimeFile](T_Grasshopper_Documentation_GH_RuntimeFile.htm)  
The runtime representation of the file on the disk.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_RuntimeFile Class](T_Grasshopper_Documentation_GH_RuntimeFile.htm)

[Grasshopper.Documentation Namespace](N_Grasshopper_Documentation.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)