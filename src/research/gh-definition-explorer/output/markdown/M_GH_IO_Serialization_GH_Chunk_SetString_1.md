# M_GH_IO_Serialization_GH_Chunk_SetString_1

﻿ GH\_Chunk.SetString Method (String, String)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_Chunk Class](../html/T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Class")

[GH\_Chunk Methods](../html/Methods_T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Methods")

[SetString Method](../html/Overload_GH_IO_Serialization_GH_Chunk_SetString.htm "SetString Method ")

[SetString Method (String, String)](../html/M_GH_IO_Serialization_GH_Chunk_SetString_1.htm "SetString Method (String, String)")

[SetString Method (String, Int32, String)](../html/M_GH_IO_Serialization_GH_Chunk_SetString.htm "SetString Method (String, Int32, String)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ChunkAddLanguageSpecificTextSet("LST27D0B394\_0?cpp=::|nu=.");SetString Method (String, String) |

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
public void SetString(
	string item_name,
	string item_value
)
```

```
Public Sub SetString ( 
	item_name As String,
	item_value As String
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

item\_name
:   Type: [SystemAddLanguageSpecificTextSet("LST27D0B394\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of item to add.

item\_value
:   Type: [SystemAddLanguageSpecificTextSet("LST27D0B394\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Value of item to add.

#### Implements

[GH\_IWriterAddLanguageSpecificTextSet("LST27D0B394\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");SetString(String, String)](M_GH_IO_Serialization_GH_IWriter_SetString_1.htm)

![](../icons/SectionExpanded.png)Exceptions

| Exception | Condition |
| --- | --- |
| [InvalidOperationException](https://docs.microsoft.com/dotnet/api/system.invalidoperationexception) | Thrown if another item with the same name already exists. |

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Chunk Class](T_GH_IO_Serialization_GH_Chunk.htm)

[SetString Overload](Overload_GH_IO_Serialization_GH_Chunk_SetString.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)