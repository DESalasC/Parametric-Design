# M_GH_IO_Serialization_GH_Chunk_GetInt64_1

﻿ GH\_Chunk.GetInt64 Method (String, Int32)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_Chunk Class](../html/T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Class")

[GH\_Chunk Methods](../html/Methods_T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Methods")

[GetInt64 Method](../html/Overload_GH_IO_Serialization_GH_Chunk_GetInt64.htm "GetInt64 Method ")

[GetInt64 Method (String)](../html/M_GH_IO_Serialization_GH_Chunk_GetInt64.htm "GetInt64 Method (String)")

[GetInt64 Method (String, Int32)](../html/M_GH_IO_Serialization_GH_Chunk_GetInt64_1.htm "GetInt64 Method (String, Int32)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ChunkAddLanguageSpecificTextSet("LST4434A761\_0?cpp=::|nu=.");GetInt64 Method (String, Int32) |

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
public long GetInt64(
	string item_name,
	int item_index
)
```

```
Public Function GetInt64 ( 
	item_name As String,
	item_index As Integer
) As Long
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

item\_name
:   Type: [SystemAddLanguageSpecificTextSet("LST4434A761\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of item to retrieve.

item\_index
:   Type: [SystemAddLanguageSpecificTextSet("LST4434A761\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Index of item to retrieve.

#### Return Value

Type: [Int64](https://docs.microsoft.com/dotnet/api/system.int64)  
The inner value of the item.

#### Implements

[GH\_IReaderAddLanguageSpecificTextSet("LST4434A761\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");GetInt64(String, Int32)](M_GH_IO_Serialization_GH_IReader_GetInt64_1.htm)

![](../icons/SectionExpanded.png)Exceptions

| Exception | Condition |
| --- | --- |
| [OverflowException](https://docs.microsoft.com/dotnet/api/system.overflowexception) | Thrown if the type conversion fails. |
| [InvalidCastException](https://docs.microsoft.com/dotnet/api/system.invalidcastexception) | Thrown if the type conversion is invalid. |
| [NullReferenceException](https://docs.microsoft.com/dotnet/api/system.nullreferenceexception) | Thrown if the item with the specified name and index does not exist. |

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Chunk Class](T_GH_IO_Serialization_GH_Chunk.htm)

[GetInt64 Overload](Overload_GH_IO_Serialization_GH_Chunk_GetInt64.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)