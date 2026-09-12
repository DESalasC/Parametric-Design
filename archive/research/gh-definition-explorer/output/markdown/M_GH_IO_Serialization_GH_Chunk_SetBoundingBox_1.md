# M_GH_IO_Serialization_GH_Chunk_SetBoundingBox_1

﻿ GH\_Chunk.SetBoundingBox Method (String, Int32, GH\_BoundingBox)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_Chunk Class](../html/T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Class")

[GH\_Chunk Methods](../html/Methods_T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Methods")

[SetBoundingBox Method](../html/Overload_GH_IO_Serialization_GH_Chunk_SetBoundingBox.htm "SetBoundingBox Method ")

[SetBoundingBox Method (String, GH\_BoundingBox)](../html/M_GH_IO_Serialization_GH_Chunk_SetBoundingBox.htm "SetBoundingBox Method (String, GH_BoundingBox)")

[SetBoundingBox Method (String, Int32, GH\_BoundingBox)](../html/M_GH_IO_Serialization_GH_Chunk_SetBoundingBox_1.htm "SetBoundingBox Method (String, Int32, GH_BoundingBox)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ChunkAddLanguageSpecificTextSet("LSTABDA9930\_0?cpp=::|nu=.");SetBoundingBox Method (String, Int32, GH\_BoundingBox) |

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
public void SetBoundingBox(
	string item_name,
	int item_index,
	GH_BoundingBox item_value
)
```

```
Public Sub SetBoundingBox ( 
	item_name As String,
	item_index As Integer,
	item_value As GH_BoundingBox
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

item\_name
:   Type: [SystemAddLanguageSpecificTextSet("LSTABDA9930\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of item to add.

item\_index
:   Type: [SystemAddLanguageSpecificTextSet("LSTABDA9930\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Index of item to add.

item\_value
:   Type: [GH\_IO.TypesAddLanguageSpecificTextSet("LSTABDA9930\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_BoundingBox](T_GH_IO_Types_GH_BoundingBox.htm)  
    Value of item to add.

#### Implements

[GH\_IWriterAddLanguageSpecificTextSet("LSTABDA9930\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");SetBoundingBox(String, Int32, GH\_BoundingBox)](M_GH_IO_Serialization_GH_IWriter_SetBoundingBox_1.htm)

![](../icons/SectionExpanded.png)Exceptions

| Exception | Condition |
| --- | --- |
| [InvalidOperationException](https://docs.microsoft.com/dotnet/api/system.invalidoperationexception) | Thrown if another item with the same name and index already exists. |

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Chunk Class](T_GH_IO_Serialization_GH_Chunk.htm)

[SetBoundingBox Overload](Overload_GH_IO_Serialization_GH_Chunk_SetBoundingBox.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)