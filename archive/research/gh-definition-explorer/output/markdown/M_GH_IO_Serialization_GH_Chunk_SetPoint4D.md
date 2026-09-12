# M_GH_IO_Serialization_GH_Chunk_SetPoint4D

﻿ GH\_Chunk.SetPoint4D Method (String, GH\_Point4D)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_Chunk Class](../html/T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Class")

[GH\_Chunk Methods](../html/Methods_T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Methods")

[SetPoint4D Method](../html/Overload_GH_IO_Serialization_GH_Chunk_SetPoint4D.htm "SetPoint4D Method ")

[SetPoint4D Method (String, GH\_Point4D)](../html/M_GH_IO_Serialization_GH_Chunk_SetPoint4D.htm "SetPoint4D Method (String, GH_Point4D)")

[SetPoint4D Method (String, Int32, GH\_Point4D)](../html/M_GH_IO_Serialization_GH_Chunk_SetPoint4D_1.htm "SetPoint4D Method (String, Int32, GH_Point4D)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ChunkAddLanguageSpecificTextSet("LST12B76A12\_0?cpp=::|nu=.");SetPoint4D Method (String, GH\_Point4D) |

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
public void SetPoint4D(
	string item_name,
	GH_Point4D item_value
)
```

```
Public Sub SetPoint4D ( 
	item_name As String,
	item_value As GH_Point4D
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

item\_name
:   Type: [SystemAddLanguageSpecificTextSet("LST12B76A12\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of item to add.

item\_value
:   Type: [GH\_IO.TypesAddLanguageSpecificTextSet("LST12B76A12\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Point4D](T_GH_IO_Types_GH_Point4D.htm)  
    Value of item to add.

#### Implements

[GH\_IWriterAddLanguageSpecificTextSet("LST12B76A12\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");SetPoint4D(String, GH\_Point4D)](M_GH_IO_Serialization_GH_IWriter_SetPoint4D.htm)

![](../icons/SectionExpanded.png)Exceptions

| Exception | Condition |
| --- | --- |
| [InvalidOperationException](https://docs.microsoft.com/dotnet/api/system.invalidoperationexception) | Thrown if another item with the same name already exists. |

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Chunk Class](T_GH_IO_Serialization_GH_Chunk.htm)

[SetPoint4D Overload](Overload_GH_IO_Serialization_GH_Chunk_SetPoint4D.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)