# M_GH_IO_Serialization_GH_Chunk_TryGetBoolean_1

﻿ GH\_Chunk.TryGetBoolean Method (String, Int32, Boolean)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_Chunk Class](../html/T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Class")

[GH\_Chunk Methods](../html/Methods_T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Methods")

[TryGetBoolean Method](../html/Overload_GH_IO_Serialization_GH_Chunk_TryGetBoolean.htm "TryGetBoolean Method ")

[TryGetBoolean Method (String, Boolean)](../html/M_GH_IO_Serialization_GH_Chunk_TryGetBoolean.htm "TryGetBoolean Method (String, Boolean)")

[TryGetBoolean Method (String, Int32, Boolean)](../html/M_GH_IO_Serialization_GH_Chunk_TryGetBoolean_1.htm "TryGetBoolean Method (String, Int32, Boolean)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ChunkAddLanguageSpecificTextSet("LSTE8528EB7\_0?cpp=::|nu=.");TryGetBoolean Method (String, Int32, BooleanAddLanguageSpecificTextSet("LSTE8528EB7\_1?cpp=%");) |

Gets the value of the item with the specified name and index.
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
public bool TryGetBoolean(
	string item_name,
	int item_index,
	ref bool value
)
```

```
Public Function TryGetBoolean ( 
	item_name As String,
	item_index As Integer,
	ByRef value As Boolean
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

item\_name
:   Type: [SystemAddLanguageSpecificTextSet("LSTE8528EB7\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of item to retrieve.

item\_index
:   Type: [SystemAddLanguageSpecificTextSet("LSTE8528EB7\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Index of item to retrieve.

value
:   Type: [SystemAddLanguageSpecificTextSet("LSTE8528EB7\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)AddLanguageSpecificTextSet("LSTE8528EB7\_5?cpp=%");  
    Target of assignment.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True if the value was set.

#### Implements

[GH\_IReaderAddLanguageSpecificTextSet("LSTE8528EB7\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");TryGetBoolean(String, Int32, BooleanAddLanguageSpecificTextSet("LSTE8528EB7\_7?cpp=%");)](M_GH_IO_Serialization_GH_IReader_TryGetBoolean_1.htm)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Chunk Class](T_GH_IO_Serialization_GH_Chunk.htm)

[TryGetBoolean Overload](Overload_GH_IO_Serialization_GH_Chunk_TryGetBoolean.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)