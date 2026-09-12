# T_GH_IO_Serialization_GH_Message_Type

﻿ GH\_Message\_Type Enumeration

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
| GH\_Message\_Type Enumeration |

Message type flag.

**Namespace:**
 [GH\_IO.Serialization](N_GH_IO_Serialization.htm)  
**Assembly:**
 GH\_IO (in GH\_IO.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public enum GH_Message_Type
```

```
Public Enumeration GH_Message_Type
```

AddLanguageTabSet("ID0EBCA");

![](../icons/SectionExpanded.png)Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | info | 0 | Indicates a message represents information. |
|  | warning | 1 | Indicates the message represents a warning. Warnings are not severe enough to be regarded as IO errors. |
|  | error | 2 | Indicates the message represents an error. Errors mean (de)serialization failed (partially). |

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)