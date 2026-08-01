# M_GH_IO_Serialization_GH_Chunk_SetDate_1

﻿ GH\_Chunk.SetDate Method (String, Int32, DateTime)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_Chunk Class](../html/T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Class")

[GH\_Chunk Methods](../html/Methods_T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Methods")

[SetDate Method](../html/Overload_GH_IO_Serialization_GH_Chunk_SetDate.htm "SetDate Method ")

[SetDate Method (String, DateTime)](../html/M_GH_IO_Serialization_GH_Chunk_SetDate.htm "SetDate Method (String, DateTime)")

[SetDate Method (String, Int32, DateTime)](../html/M_GH_IO_Serialization_GH_Chunk_SetDate_1.htm "SetDate Method (String, Int32, DateTime)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ChunkAddLanguageSpecificTextSet("LST4010A84F\_0?cpp=::|nu=.");SetDate Method (String, Int32, DateTime) |

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
public void SetDate(
	string item_name,
	int item_index,
	DateTime item_value
)
```

```
Public Sub SetDate ( 
	item_name As String,
	item_index As Integer,
	item_value As DateTime
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

item\_name
:   Type: [SystemAddLanguageSpecificTextSet("LST4010A84F\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of item to add.

item\_index
:   Type: [SystemAddLanguageSpecificTextSet("LST4010A84F\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Index of item to add.

item\_value
:   Type: [SystemAddLanguageSpecificTextSet("LST4010A84F\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");DateTime](https://docs.microsoft.com/dotnet/api/system.datetime)  
    Value of item to add.

#### Implements

[GH\_IWriterAddLanguageSpecificTextSet("LST4010A84F\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");SetDate(String, Int32, DateTime)](M_GH_IO_Serialization_GH_IWriter_SetDate_1.htm)

![](../icons/SectionExpanded.png)Exceptions

| Exception | Condition |
| --- | --- |
| [InvalidOperationException](https://docs.microsoft.com/dotnet/api/system.invalidoperationexception) | Thrown if another item with the same name and index already exists. |

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Chunk Class](T_GH_IO_Serialization_GH_Chunk.htm)

[SetDate Overload](Overload_GH_IO_Serialization_GH_Chunk_SetDate.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)