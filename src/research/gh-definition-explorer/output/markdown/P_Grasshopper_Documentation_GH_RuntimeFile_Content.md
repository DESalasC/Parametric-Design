# P_Grasshopper_Documentation_GH_RuntimeFile_Content

﻿ GH\_RuntimeFile.Content Property 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.Documentation](../html/N_Grasshopper_Documentation.htm "Grasshopper.Documentation")

[GH\_RuntimeFile Class](../html/T_Grasshopper_Documentation_GH_RuntimeFile.htm "GH_RuntimeFile Class")

[GH\_RuntimeFile Properties](../html/Properties_T_Grasshopper_Documentation_GH_RuntimeFile.htm "GH_RuntimeFile Properties")

[Content Property](../html/P_Grasshopper_Documentation_GH_RuntimeFile_Content.htm "Content Property ")

[Keys Property](../html/P_Grasshopper_Documentation_GH_RuntimeFile_Keys.htm "Keys Property ")

[Path Property](../html/P_Grasshopper_Documentation_GH_RuntimeFile_Path.htm "Path Property ")

[Tags Property](../html/P_Grasshopper_Documentation_GH_RuntimeFile_Tags.htm "Tags Property ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_RuntimeFileAddLanguageSpecificTextSet("LSTBA353BB9\_0?cpp=::|nu=.");Content Property |

Gets the data associated with a certain key. For every time the key appears
in the file, an array of content strings will be returned.

**Namespace:**
 [Grasshopper.Documentation](N_Grasshopper_Documentation.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public List<string[]> this[
	string key
] { get; }
```

```
Public ReadOnly Default Property Content ( 
	key As String
) As List(Of String())
	Get
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

key
:   Type: [SystemAddLanguageSpecificTextSet("LSTBA353BB9\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Key to search for, key comparison is not case-sensitive.

#### Property Value

Type: [List](https://docs.microsoft.com/dotnet/api/system.collections.generic.list-1)AddLanguageSpecificTextSet("LSTBA353BB9\_2?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");AddLanguageSpecificTextSet("LSTBA353BB9\_3?cpp=array&lt;");[String](https://docs.microsoft.com/dotnet/api/system.string)AddLanguageSpecificTextSet("LSTBA353BB9\_4?cpp=&gt;|vb=()|nu=[]");AddLanguageSpecificTextSet("LSTBA353BB9\_5?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  

[Missing <value> documentation for "P:Grasshopper.Documentation.GH\_RuntimeFile.Content(System.String)"]

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_RuntimeFile Class](T_Grasshopper_Documentation_GH_RuntimeFile.htm)

[Grasshopper.Documentation Namespace](N_Grasshopper_Documentation.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)