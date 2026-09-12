# M_GH_IO_Serialization_GH_Chunk_TryGetString_1

﻿ GH\_Chunk.TryGetString Method (String, String)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_Chunk Class](../html/T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Class")

[GH\_Chunk Methods](../html/Methods_T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Methods")

[TryGetString Method](../html/Overload_GH_IO_Serialization_GH_Chunk_TryGetString.htm "TryGetString Method ")

[TryGetString Method (String, String)](../html/M_GH_IO_Serialization_GH_Chunk_TryGetString_1.htm "TryGetString Method (String, String)")

[TryGetString Method (String, Int32, String)](../html/M_GH_IO_Serialization_GH_Chunk_TryGetString.htm "TryGetString Method (String, Int32, String)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ChunkAddLanguageSpecificTextSet("LSTD7037543\_0?cpp=::|nu=.");TryGetString Method (String, StringAddLanguageSpecificTextSet("LSTD7037543\_1?cpp=%");) |

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
public bool TryGetString(
	string item_name,
	ref string value
)
```

```
Public Function TryGetString ( 
	item_name As String,
	ByRef value As String
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

item\_name
:   Type: [SystemAddLanguageSpecificTextSet("LSTD7037543\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of item to retrieve.

value
:   Type: [SystemAddLanguageSpecificTextSet("LSTD7037543\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)AddLanguageSpecificTextSet("LSTD7037543\_4?cpp=%");  
    Target of assignment.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True if the value was set.

#### Implements

[GH\_IReaderAddLanguageSpecificTextSet("LSTD7037543\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");TryGetString(String, StringAddLanguageSpecificTextSet("LSTD7037543\_6?cpp=%");)](M_GH_IO_Serialization_GH_IReader_TryGetString_1.htm)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Chunk Class](T_GH_IO_Serialization_GH_Chunk.htm)

[TryGetString Overload](Overload_GH_IO_Serialization_GH_Chunk_TryGetString.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)