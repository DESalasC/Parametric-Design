# M_GH_IO_Serialization_GH_Chunk_SetInterval1D

﻿ GH\_Chunk.SetInterval1D Method (String, GH\_Interval1D)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_Chunk Class](../html/T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Class")

[GH\_Chunk Methods](../html/Methods_T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Methods")

[SetInterval1D Method](../html/Overload_GH_IO_Serialization_GH_Chunk_SetInterval1D.htm "SetInterval1D Method ")

[SetInterval1D Method (String, GH\_Interval1D)](../html/M_GH_IO_Serialization_GH_Chunk_SetInterval1D.htm "SetInterval1D Method (String, GH_Interval1D)")

[SetInterval1D Method (String, Int32, GH\_Interval1D)](../html/M_GH_IO_Serialization_GH_Chunk_SetInterval1D_1.htm "SetInterval1D Method (String, Int32, GH_Interval1D)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ChunkAddLanguageSpecificTextSet("LST3D03B91E\_0?cpp=::|nu=.");SetInterval1D Method (String, GH\_Interval1D) |

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
public void SetInterval1D(
	string item_name,
	GH_Interval1D item_value
)
```

```
Public Sub SetInterval1D ( 
	item_name As String,
	item_value As GH_Interval1D
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

item\_name
:   Type: [SystemAddLanguageSpecificTextSet("LST3D03B91E\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of item to add.

item\_value
:   Type: [GH\_IO.TypesAddLanguageSpecificTextSet("LST3D03B91E\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Interval1D](T_GH_IO_Types_GH_Interval1D.htm)  
    Value of item to add.

#### Implements

[GH\_IWriterAddLanguageSpecificTextSet("LST3D03B91E\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");SetInterval1D(String, GH\_Interval1D)](M_GH_IO_Serialization_GH_IWriter_SetInterval1D.htm)

![](../icons/SectionExpanded.png)Exceptions

| Exception | Condition |
| --- | --- |
| [InvalidOperationException](https://docs.microsoft.com/dotnet/api/system.invalidoperationexception) | Thrown if another item with the same name already exists. |

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Chunk Class](T_GH_IO_Serialization_GH_Chunk.htm)

[SetInterval1D Overload](Overload_GH_IO_Serialization_GH_Chunk_SetInterval1D.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)