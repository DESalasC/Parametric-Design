# M_GH_IO_Serialization_GH_Chunk_SetByte

﻿ GH\_Chunk.SetByte Method (String, Byte)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_Chunk Class](../html/T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Class")

[GH\_Chunk Methods](../html/Methods_T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Methods")

[SetByte Method](../html/Overload_GH_IO_Serialization_GH_Chunk_SetByte.htm "SetByte Method ")

[SetByte Method (String, Byte)](../html/M_GH_IO_Serialization_GH_Chunk_SetByte.htm "SetByte Method (String, Byte)")

[SetByte Method (String, Int32, Byte)](../html/M_GH_IO_Serialization_GH_Chunk_SetByte_1.htm "SetByte Method (String, Int32, Byte)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ChunkAddLanguageSpecificTextSet("LST774B045\_0?cpp=::|nu=.");SetByte Method (String, Byte) |

Add a new data item to this chunk.
The name must be unique or an exception will be thrown.

**Namespace:**
 [GH\_IO.Serialization](N_GH_IO_Serialization.htm)  
**Assembly:**
 GH\_IO (in GH\_IO.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public void SetByte(
	string item_name,
	byte item_value
)
```

```
Public Sub SetByte ( 
	item_name As String,
	item_value As Byte
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

item\_name
:   Type: [SystemAddLanguageSpecificTextSet("LST774B045\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of item to add.

item\_value
:   Type: [SystemAddLanguageSpecificTextSet("LST774B045\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Byte](https://docs.microsoft.com/dotnet/api/system.byte)  
    Value of item to add.

#### Implements

[GH\_IWriterAddLanguageSpecificTextSet("LST774B045\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");SetByte(String, Byte)](M_GH_IO_Serialization_GH_IWriter_SetByte.htm)

![](../icons/SectionExpanded.png)Exceptions

| Exception | Condition |
| --- | --- |
| [InvalidOperationException](https://docs.microsoft.com/dotnet/api/system.invalidoperationexception) | Thrown if another item with the same name already exists. |

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Chunk Class](T_GH_IO_Serialization_GH_Chunk.htm)

[SetByte Overload](Overload_GH_IO_Serialization_GH_Chunk_SetByte.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)