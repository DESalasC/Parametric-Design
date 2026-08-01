# N_GH_IO_Serialization

﻿ GH\_IO.Serialization Namespace

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_Archive Class](../html/T_GH_IO_Serialization_GH_Archive.htm "GH_Archive Class")

[GH\_Chunk Class](../html/T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Class")

[GH\_Chunk.ChunkKeyedCollection Class](../html/T_GH_IO_Serialization_GH_Chunk_ChunkKeyedCollection.htm "GH_Chunk.ChunkKeyedCollection Class")

[GH\_Compression Class](../html/T_GH_IO_Serialization_GH_Compression.htm "GH_Compression Class")

[GH\_IBinarySupport Interface](../html/T_GH_IO_Serialization_GH_IBinarySupport.htm "GH_IBinarySupport Interface")

[GH\_IChunk Interface](../html/T_GH_IO_Serialization_GH_IChunk.htm "GH_IChunk Interface")

[GH\_IReader Interface](../html/T_GH_IO_Serialization_GH_IReader.htm "GH_IReader Interface")

[GH\_IWriter Interface](../html/T_GH_IO_Serialization_GH_IWriter.htm "GH_IWriter Interface")

[GH\_IXmlSupport Interface](../html/T_GH_IO_Serialization_GH_IXmlSupport.htm "GH_IXmlSupport Interface")

[GH\_LooseChunk Class](../html/T_GH_IO_Serialization_GH_LooseChunk.htm "GH_LooseChunk Class")

[GH\_Message Class](../html/T_GH_IO_Serialization_GH_Message.htm "GH_Message Class")

[GH\_Message\_Type Enumeration](../html/T_GH_IO_Serialization_GH_Message_Type.htm "GH_Message_Type Enumeration")

[ID Structure](../html/T_GH_IO_Serialization_ID.htm "ID Structure")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_IO.Serialization Namespace |

Namespace in GH\_IO.dll that contains all the classes used during (de)serialization.

![](../icons/SectionExpanded.png)Classes

|  | Class | Description |
| --- | --- | --- |
| Public class | [GH\_Archive](T_GH_IO_Serialization_GH_Archive.htm) | This is the base archive class which takes care of all (de)serialization and messaging. |
| Public class | [GH\_Chunk](T_GH_IO_Serialization_GH_Chunk.htm) | Full implementation of GH\_IChunk, GH\_IReader, GH\_IWriter, GH\_IBinarySupport and GH\_IXmlSupport. Instances of this class are usually disguised as one of the interfaces it implements. |
| Public class | [GH\_ChunkAddLanguageSpecificTextSet("LSTE9A79857\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");ChunkKeyedCollection](T_GH_IO_Serialization_GH_Chunk_ChunkKeyedCollection.htm) | Represents a collection of chunks with associated IDs |
| Public class | [GH\_Compression](T_GH_IO_Serialization_GH_Compression.htm) | Provides static methods for compression of byte-arrays. |
| Public class | [GH\_LooseChunk](T_GH_IO_Serialization_GH_LooseChunk.htm) | A utility class for creating partial archives. |
| Public class | [GH\_Message](T_GH_IO_Serialization_GH_Message.htm) | Represents an archive log message. Messages are collected during read/write operations. |

![](../icons/SectionExpanded.png)Structures

|  | Structure | Description |
| --- | --- | --- |
| Public structure | [ID](T_GH_IO_Serialization_ID.htm) | An ID is used to uniquely identify a specific item. |

![](../icons/SectionExpanded.png)Interfaces

|  | Interface | Description |
| --- | --- | --- |
| Public interface | [GH\_IBinarySupport](T_GH_IO_Serialization_GH_IBinarySupport.htm) | Interface which declares all methods required for objects that can be (de)serialized to and from a binary archive. |
| Public interface | [GH\_IChunk](T_GH_IO_Serialization_GH_IChunk.htm) | Base interface for all Archive Chunks. |
| Public interface | [GH\_IReader](T_GH_IO_Serialization_GH_IReader.htm) | Provides access to a subset of GH\_Chunk methods used for reading archives. |
| Public interface | [GH\_IWriter](T_GH_IO_Serialization_GH_IWriter.htm) | Provides access to a subset of GH\_Chunk methods used for writing archives. |
| Public interface | [GH\_IXmlSupport](T_GH_IO_Serialization_GH_IXmlSupport.htm) | Interface which declares all methods required for objects that can be (de)serialized to and from an Xml archive. |

![](../icons/SectionExpanded.png)Enumerations

|  | Enumeration | Description |
| --- | --- | --- |
| Public enumeration | [GH\_Message\_Type](T_GH_IO_Serialization_GH_Message_Type.htm) | Message type flag. |

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)