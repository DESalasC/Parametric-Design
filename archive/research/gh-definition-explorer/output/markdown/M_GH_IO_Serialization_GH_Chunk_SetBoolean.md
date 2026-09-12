# M_GH_IO_Serialization_GH_Chunk_SetBoolean

﻿ GH\_Chunk.SetBoolean Method (String, Boolean)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_Chunk Class](../html/T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Class")

[GH\_Chunk Methods](../html/Methods_T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Methods")

[SetBoolean Method](../html/Overload_GH_IO_Serialization_GH_Chunk_SetBoolean.htm "SetBoolean Method ")

[SetBoolean Method (String, Boolean)](../html/M_GH_IO_Serialization_GH_Chunk_SetBoolean.htm "SetBoolean Method (String, Boolean)")

[SetBoolean Method (String, Int32, Boolean)](../html/M_GH_IO_Serialization_GH_Chunk_SetBoolean_1.htm "SetBoolean Method (String, Int32, Boolean)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ChunkAddLanguageSpecificTextSet("LST96C4C8D8\_0?cpp=::|nu=.");SetBoolean Method (String, Boolean) |

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
public void SetBoolean(
	string item_name,
	bool item_value
)
```

```
Public Sub SetBoolean ( 
	item_name As String,
	item_value As Boolean
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

item\_name
:   Type: [SystemAddLanguageSpecificTextSet("LST96C4C8D8\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of item to add.

item\_value
:   Type: [SystemAddLanguageSpecificTextSet("LST96C4C8D8\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
    Value of item to add.

#### Implements

[GH\_IWriterAddLanguageSpecificTextSet("LST96C4C8D8\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");SetBoolean(String, Boolean)](M_GH_IO_Serialization_GH_IWriter_SetBoolean.htm)

![](../icons/SectionExpanded.png)Exceptions

| Exception | Condition |
| --- | --- |
| [InvalidOperationException](https://docs.microsoft.com/dotnet/api/system.invalidoperationexception) | Thrown if another item with the same name already exists. |

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Chunk Class](T_GH_IO_Serialization_GH_Chunk.htm)

[SetBoolean Overload](Overload_GH_IO_Serialization_GH_Chunk_SetBoolean.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)