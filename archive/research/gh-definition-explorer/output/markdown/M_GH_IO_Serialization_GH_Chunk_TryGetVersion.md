# M_GH_IO_Serialization_GH_Chunk_TryGetVersion

﻿ GH\_Chunk.TryGetVersion Method (String, GH\_Version)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_Chunk Class](../html/T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Class")

[GH\_Chunk Methods](../html/Methods_T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Methods")

[TryGetVersion Method](../html/Overload_GH_IO_Serialization_GH_Chunk_TryGetVersion.htm "TryGetVersion Method ")

[TryGetVersion Method (String, GH\_Version)](../html/M_GH_IO_Serialization_GH_Chunk_TryGetVersion.htm "TryGetVersion Method (String, GH_Version)")

[TryGetVersion Method (String, Int32, GH\_Version)](../html/M_GH_IO_Serialization_GH_Chunk_TryGetVersion_1.htm "TryGetVersion Method (String, Int32, GH_Version)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ChunkAddLanguageSpecificTextSet("LST74AD633B\_0?cpp=::|nu=.");TryGetVersion Method (String, GH\_VersionAddLanguageSpecificTextSet("LST74AD633B\_1?cpp=%");) |

Gets the value of the item with the specified name.
Name comparison is not case-sensitive.

**Namespace:**
 [GH\_IO.Serialization](N_GH_IO_Serialization.htm)  
**Assembly:**
 GH\_IO (in GH\_IO.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public bool TryGetVersion(
	string item_name,
	ref GH_Version value
)
```

```
Public Function TryGetVersion ( 
	item_name As String,
	ByRef value As GH_Version
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

item\_name
:   Type: [SystemAddLanguageSpecificTextSet("LST74AD633B\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of item to retrieve.

value
:   Type: [GH\_IO.TypesAddLanguageSpecificTextSet("LST74AD633B\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Version](T_GH_IO_Types_GH_Version.htm)AddLanguageSpecificTextSet("LST74AD633B\_4?cpp=%");  
    Target of assignment.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True if the value was set.

#### Implements

[GH\_IReaderAddLanguageSpecificTextSet("LST74AD633B\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");TryGetVersion(String, GH\_VersionAddLanguageSpecificTextSet("LST74AD633B\_6?cpp=%");)](M_GH_IO_Serialization_GH_IReader_TryGetVersion.htm)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Chunk Class](T_GH_IO_Serialization_GH_Chunk.htm)

[TryGetVersion Overload](Overload_GH_IO_Serialization_GH_Chunk_TryGetVersion.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)