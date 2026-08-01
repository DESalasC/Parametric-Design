# M_GH_IO_Serialization_GH_Chunk_SetVersion_3

﻿ GH\_Chunk.SetVersion Method (String, Int32, Int32, Int32, Int32)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_Chunk Class](../html/T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Class")

[GH\_Chunk Methods](../html/Methods_T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Methods")

[SetVersion Method](../html/Overload_GH_IO_Serialization_GH_Chunk_SetVersion.htm "SetVersion Method ")

[SetVersion Method (String, GH\_Version)](../html/M_GH_IO_Serialization_GH_Chunk_SetVersion.htm "SetVersion Method (String, GH_Version)")

[SetVersion Method (String, Int32, GH\_Version)](../html/M_GH_IO_Serialization_GH_Chunk_SetVersion_1.htm "SetVersion Method (String, Int32, GH_Version)")

[SetVersion Method (String, Int32, Int32, Int32)](../html/M_GH_IO_Serialization_GH_Chunk_SetVersion_2.htm "SetVersion Method (String, Int32, Int32, Int32)")

[SetVersion Method (String, Int32, Int32, Int32, Int32)](../html/M_GH_IO_Serialization_GH_Chunk_SetVersion_3.htm "SetVersion Method (String, Int32, Int32, Int32, Int32)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ChunkAddLanguageSpecificTextSet("LST400E119C\_0?cpp=::|nu=.");SetVersion Method (String, Int32, Int32, Int32, Int32) |

Add a new data item to this chunk.
The combination of name and index must be unique or an exception will be thrown.

**Namespace:**
 [GH\_IO.Serialization](N_GH_IO_Serialization.htm)  
**Assembly:**
 GH\_IO (in GH\_IO.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public void SetVersion(
	string item_name,
	int item_index,
	int major,
	int minor,
	int revision
)
```

```
Public Sub SetVersion ( 
	item_name As String,
	item_index As Integer,
	major As Integer,
	minor As Integer,
	revision As Integer
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

item\_name
:   Type: [SystemAddLanguageSpecificTextSet("LST400E119C\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of item to add.

item\_index
:   Type: [SystemAddLanguageSpecificTextSet("LST400E119C\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Index of item to add.

major
:   Type: [SystemAddLanguageSpecificTextSet("LST400E119C\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Major component of Version structure.

minor
:   Type: [SystemAddLanguageSpecificTextSet("LST400E119C\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Minor component of Version structure.

revision
:   Type: [SystemAddLanguageSpecificTextSet("LST400E119C\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Revision component of Version structure.

#### Implements

[GH\_IWriterAddLanguageSpecificTextSet("LST400E119C\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");SetVersion(String, Int32, Int32, Int32, Int32)](M_GH_IO_Serialization_GH_IWriter_SetVersion_3.htm)

![](../icons/SectionExpanded.png)Exceptions

| Exception | Condition |
| --- | --- |
| [InvalidOperationException](https://docs.microsoft.com/dotnet/api/system.invalidoperationexception) | Thrown if another item with the same name and index already exists. |

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Chunk Class](T_GH_IO_Serialization_GH_Chunk.htm)

[SetVersion Overload](Overload_GH_IO_Serialization_GH_Chunk_SetVersion.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)