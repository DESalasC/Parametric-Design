# M_GH_IO_Serialization_GH_Chunk_TryGetDecimal

﻿ GH\_Chunk.TryGetDecimal Method (String, Decimal)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_Chunk Class](../html/T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Class")

[GH\_Chunk Methods](../html/Methods_T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Methods")

[TryGetDecimal Method](../html/Overload_GH_IO_Serialization_GH_Chunk_TryGetDecimal.htm "TryGetDecimal Method ")

[TryGetDecimal Method (String, Decimal)](../html/M_GH_IO_Serialization_GH_Chunk_TryGetDecimal.htm "TryGetDecimal Method (String, Decimal)")

[TryGetDecimal Method (String, Int32, Decimal)](../html/M_GH_IO_Serialization_GH_Chunk_TryGetDecimal_1.htm "TryGetDecimal Method (String, Int32, Decimal)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ChunkAddLanguageSpecificTextSet("LSTA99EA9AB\_0?cpp=::|nu=.");TryGetDecimal Method (String, DecimalAddLanguageSpecificTextSet("LSTA99EA9AB\_1?cpp=%");) |

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
public bool TryGetDecimal(
	string item_name,
	ref decimal value
)
```

```
Public Function TryGetDecimal ( 
	item_name As String,
	ByRef value As Decimal
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

item\_name
:   Type: [SystemAddLanguageSpecificTextSet("LSTA99EA9AB\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of item to retrieve.

value
:   Type: [SystemAddLanguageSpecificTextSet("LSTA99EA9AB\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Decimal](https://docs.microsoft.com/dotnet/api/system.decimal)AddLanguageSpecificTextSet("LSTA99EA9AB\_4?cpp=%");  
    Target of assignment.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True if the value was set.

#### Implements

[GH\_IReaderAddLanguageSpecificTextSet("LSTA99EA9AB\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");TryGetDecimal(String, DecimalAddLanguageSpecificTextSet("LSTA99EA9AB\_6?cpp=%");)](M_GH_IO_Serialization_GH_IReader_TryGetDecimal.htm)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Chunk Class](T_GH_IO_Serialization_GH_Chunk.htm)

[TryGetDecimal Overload](Overload_GH_IO_Serialization_GH_Chunk_TryGetDecimal.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)