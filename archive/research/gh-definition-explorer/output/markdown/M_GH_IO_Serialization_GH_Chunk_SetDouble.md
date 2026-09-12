# M_GH_IO_Serialization_GH_Chunk_SetDouble

﻿ GH\_Chunk.SetDouble Method (String, Double)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_Chunk Class](../html/T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Class")

[GH\_Chunk Methods](../html/Methods_T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Methods")

[SetDouble Method](../html/Overload_GH_IO_Serialization_GH_Chunk_SetDouble.htm "SetDouble Method ")

[SetDouble Method (String, Double)](../html/M_GH_IO_Serialization_GH_Chunk_SetDouble.htm "SetDouble Method (String, Double)")

[SetDouble Method (String, Int32, Double)](../html/M_GH_IO_Serialization_GH_Chunk_SetDouble_1.htm "SetDouble Method (String, Int32, Double)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ChunkAddLanguageSpecificTextSet("LSTDCCCC2C3\_0?cpp=::|nu=.");SetDouble Method (String, Double) |

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
public void SetDouble(
	string item_name,
	double item_value
)
```

```
Public Sub SetDouble ( 
	item_name As String,
	item_value As Double
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

item\_name
:   Type: [SystemAddLanguageSpecificTextSet("LSTDCCCC2C3\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of item to add.

item\_value
:   Type: [SystemAddLanguageSpecificTextSet("LSTDCCCC2C3\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Double](https://docs.microsoft.com/dotnet/api/system.double)  
    Value of item to add.

#### Implements

[GH\_IWriterAddLanguageSpecificTextSet("LSTDCCCC2C3\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");SetDouble(String, Double)](M_GH_IO_Serialization_GH_IWriter_SetDouble.htm)

![](../icons/SectionExpanded.png)Exceptions

| Exception | Condition |
| --- | --- |
| [InvalidOperationException](https://docs.microsoft.com/dotnet/api/system.invalidoperationexception) | Thrown if another item with the same name already exists. |

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Chunk Class](T_GH_IO_Serialization_GH_Chunk.htm)

[SetDouble Overload](Overload_GH_IO_Serialization_GH_Chunk_SetDouble.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)