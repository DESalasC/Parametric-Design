# M_GH_IO_Serialization_GH_Chunk_Write

﻿ GH\_Chunk.Write Method (BinaryWriter)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_Chunk Class](../html/T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Class")

[GH\_Chunk Methods](../html/Methods_T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Methods")

[Write Method](../html/Overload_GH_IO_Serialization_GH_Chunk_Write.htm "Write Method ")

[Write Method (BinaryWriter)](../html/M_GH_IO_Serialization_GH_Chunk_Write.htm "Write Method (BinaryWriter)")

[Write Method (XmlWriter)](../html/M_GH_IO_Serialization_GH_Chunk_Write_1.htm "Write Method (XmlWriter)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ChunkAddLanguageSpecificTextSet("LST46354AEF\_0?cpp=::|nu=.");Write Method (BinaryWriter) |

Write this chunk and all child chunks to a binary stream.

**Namespace:**
 [GH\_IO.Serialization](N_GH_IO_Serialization.htm)  
**Assembly:**
 GH\_IO (in GH\_IO.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public void Write(
	BinaryWriter writer
)
```

```
Public Sub Write ( 
	writer As BinaryWriter
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

writer
:   Type: [System.IOAddLanguageSpecificTextSet("LST46354AEF\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");BinaryWriter](https://docs.microsoft.com/dotnet/api/system.io.binarywriter)  
    The Binary writer to use, cannot be null.

#### Implements

[GH\_IBinarySupportAddLanguageSpecificTextSet("LST46354AEF\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Write(BinaryWriter)](M_GH_IO_Serialization_GH_IBinarySupport_Write.htm)

![](../icons/SectionExpanded.png)Exceptions

| Exception | Condition |
| --- | --- |
| [MemberAccessException](https://docs.microsoft.com/dotnet/api/system.memberaccessexception) | Thrown if the name of this chunk is either null or empty. |

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Chunk Class](T_GH_IO_Serialization_GH_Chunk.htm)

[Write Overload](Overload_GH_IO_Serialization_GH_Chunk_Write.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)