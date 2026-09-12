# M_GH_IO_Serialization_GH_Chunk_SetDecimal

﻿ GH\_Chunk.SetDecimal Method (String, Decimal)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_Chunk Class](../html/T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Class")

[GH\_Chunk Methods](../html/Methods_T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Methods")

[SetDecimal Method](../html/Overload_GH_IO_Serialization_GH_Chunk_SetDecimal.htm "SetDecimal Method ")

[SetDecimal Method (String, Decimal)](../html/M_GH_IO_Serialization_GH_Chunk_SetDecimal.htm "SetDecimal Method (String, Decimal)")

[SetDecimal Method (String, Int32, Decimal)](../html/M_GH_IO_Serialization_GH_Chunk_SetDecimal_1.htm "SetDecimal Method (String, Int32, Decimal)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ChunkAddLanguageSpecificTextSet("LSTAC5E0FBE\_0?cpp=::|nu=.");SetDecimal Method (String, Decimal) |

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
public void SetDecimal(
	string item_name,
	decimal item_value
)
```

```
Public Sub SetDecimal ( 
	item_name As String,
	item_value As Decimal
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

item\_name
:   Type: [SystemAddLanguageSpecificTextSet("LSTAC5E0FBE\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of item to add.

item\_value
:   Type: [SystemAddLanguageSpecificTextSet("LSTAC5E0FBE\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Decimal](https://docs.microsoft.com/dotnet/api/system.decimal)  
    Value of item to add.

#### Implements

[GH\_IWriterAddLanguageSpecificTextSet("LSTAC5E0FBE\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");SetDecimal(String, Decimal)](M_GH_IO_Serialization_GH_IWriter_SetDecimal.htm)

![](../icons/SectionExpanded.png)Exceptions

| Exception | Condition |
| --- | --- |
| [InvalidOperationException](https://docs.microsoft.com/dotnet/api/system.invalidoperationexception) | Thrown if another item with the same name already exists. |

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Chunk Class](T_GH_IO_Serialization_GH_Chunk.htm)

[SetDecimal Overload](Overload_GH_IO_Serialization_GH_Chunk_SetDecimal.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)