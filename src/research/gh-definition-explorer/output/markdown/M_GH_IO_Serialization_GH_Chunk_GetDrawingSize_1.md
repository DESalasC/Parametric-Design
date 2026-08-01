# M_GH_IO_Serialization_GH_Chunk_GetDrawingSize_1

﻿ GH\_Chunk.GetDrawingSize Method (String, Int32)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_Chunk Class](../html/T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Class")

[GH\_Chunk Methods](../html/Methods_T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Methods")

[GetDrawingSize Method](../html/Overload_GH_IO_Serialization_GH_Chunk_GetDrawingSize.htm "GetDrawingSize Method ")

[GetDrawingSize Method (String)](../html/M_GH_IO_Serialization_GH_Chunk_GetDrawingSize.htm "GetDrawingSize Method (String)")

[GetDrawingSize Method (String, Int32)](../html/M_GH_IO_Serialization_GH_Chunk_GetDrawingSize_1.htm "GetDrawingSize Method (String, Int32)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ChunkAddLanguageSpecificTextSet("LST45B9A86A\_0?cpp=::|nu=.");GetDrawingSize Method (String, Int32) |

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
public Size GetDrawingSize(
	string item_name,
	int item_index
)
```

```
Public Function GetDrawingSize ( 
	item_name As String,
	item_index As Integer
) As Size
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

item\_name
:   Type: [SystemAddLanguageSpecificTextSet("LST45B9A86A\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of item to retrieve.

item\_index
:   Type: [SystemAddLanguageSpecificTextSet("LST45B9A86A\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Index of item to retrieve.

#### Return Value

Type: [Size](https://docs.microsoft.com/dotnet/api/system.drawing.size)  
The inner value of the item.

#### Implements

[GH\_IReaderAddLanguageSpecificTextSet("LST45B9A86A\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");GetDrawingSize(String, Int32)](M_GH_IO_Serialization_GH_IReader_GetDrawingSize_1.htm)

![](../icons/SectionExpanded.png)Exceptions

| Exception | Condition |
| --- | --- |
| [OverflowException](https://docs.microsoft.com/dotnet/api/system.overflowexception) | Thrown if the type conversion fails. |
| [InvalidCastException](https://docs.microsoft.com/dotnet/api/system.invalidcastexception) | Thrown if the type conversion is invalid. |
| [NullReferenceException](https://docs.microsoft.com/dotnet/api/system.nullreferenceexception) | Thrown if the item with the specified name and index does not exist. |

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Chunk Class](T_GH_IO_Serialization_GH_Chunk.htm)

[GetDrawingSize Overload](Overload_GH_IO_Serialization_GH_Chunk_GetDrawingSize.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)