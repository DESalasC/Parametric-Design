# M_GH_IO_Serialization_GH_Chunk_GetByteArray

﻿ GH\_Chunk.GetByteArray Method (String)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_Chunk Class](../html/T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Class")

[GH\_Chunk Methods](../html/Methods_T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Methods")

[GetByteArray Method](../html/Overload_GH_IO_Serialization_GH_Chunk_GetByteArray.htm "GetByteArray Method ")

[GetByteArray Method (String)](../html/M_GH_IO_Serialization_GH_Chunk_GetByteArray.htm "GetByteArray Method (String)")

[GetByteArray Method (String, Int32)](../html/M_GH_IO_Serialization_GH_Chunk_GetByteArray_1.htm "GetByteArray Method (String, Int32)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ChunkAddLanguageSpecificTextSet("LST14B6DA0B\_0?cpp=::|nu=.");GetByteArray Method (String) |

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
public byte[] GetByteArray(
	string item_name
)
```

```
Public Function GetByteArray ( 
	item_name As String
) As Byte()
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

item\_name
:   Type: [SystemAddLanguageSpecificTextSet("LST14B6DA0B\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of item to retrieve.

#### Return Value

Type: AddLanguageSpecificTextSet("LST14B6DA0B\_2?cpp=array&lt;");[Byte](https://docs.microsoft.com/dotnet/api/system.byte)AddLanguageSpecificTextSet("LST14B6DA0B\_3?cpp=&gt;|vb=()|nu=[]");  
The inner value of the item.

#### Implements

[GH\_IReaderAddLanguageSpecificTextSet("LST14B6DA0B\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");GetByteArray(String)](M_GH_IO_Serialization_GH_IReader_GetByteArray.htm)

![](../icons/SectionExpanded.png)Exceptions

| Exception | Condition |
| --- | --- |
| [OverflowException](https://docs.microsoft.com/dotnet/api/system.overflowexception) | Thrown if the type conversion fails. |
| [InvalidCastException](https://docs.microsoft.com/dotnet/api/system.invalidcastexception) | Thrown if the type conversion is invalid. |
| [NullReferenceException](https://docs.microsoft.com/dotnet/api/system.nullreferenceexception) | Thrown if the item with the specified name does not exist. |

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Chunk Class](T_GH_IO_Serialization_GH_Chunk.htm)

[GetByteArray Overload](Overload_GH_IO_Serialization_GH_Chunk_GetByteArray.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)