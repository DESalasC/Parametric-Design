# M_GH_IO_Serialization_GH_Chunk_SetPlane

﻿ GH\_Chunk.SetPlane Method (String, GH\_Plane)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_Chunk Class](../html/T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Class")

[GH\_Chunk Methods](../html/Methods_T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Methods")

[SetPlane Method](../html/Overload_GH_IO_Serialization_GH_Chunk_SetPlane.htm "SetPlane Method ")

[SetPlane Method (String, GH\_Plane)](../html/M_GH_IO_Serialization_GH_Chunk_SetPlane.htm "SetPlane Method (String, GH_Plane)")

[SetPlane Method (String, Int32, GH\_Plane)](../html/M_GH_IO_Serialization_GH_Chunk_SetPlane_1.htm "SetPlane Method (String, Int32, GH_Plane)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ChunkAddLanguageSpecificTextSet("LST11460C68\_0?cpp=::|nu=.");SetPlane Method (String, GH\_Plane) |

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
public void SetPlane(
	string item_name,
	GH_Plane item_value
)
```

```
Public Sub SetPlane ( 
	item_name As String,
	item_value As GH_Plane
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

item\_name
:   Type: [SystemAddLanguageSpecificTextSet("LST11460C68\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of item to add.

item\_value
:   Type: [GH\_IO.TypesAddLanguageSpecificTextSet("LST11460C68\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Plane](T_GH_IO_Types_GH_Plane.htm)  
    Value of item to add.

#### Implements

[GH\_IWriterAddLanguageSpecificTextSet("LST11460C68\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");SetPlane(String, GH\_Plane)](M_GH_IO_Serialization_GH_IWriter_SetPlane.htm)

![](../icons/SectionExpanded.png)Exceptions

| Exception | Condition |
| --- | --- |
| [InvalidOperationException](https://docs.microsoft.com/dotnet/api/system.invalidoperationexception) | Thrown if another item with the same name already exists. |

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Chunk Class](T_GH_IO_Serialization_GH_Chunk.htm)

[SetPlane Overload](Overload_GH_IO_Serialization_GH_Chunk_SetPlane.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)