# M_GH_IO_Serialization_GH_Chunk_GetInterval1D

﻿ GH\_Chunk.GetInterval1D Method (String)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_Chunk Class](../html/T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Class")

[GH\_Chunk Methods](../html/Methods_T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Methods")

[GetInterval1D Method](../html/Overload_GH_IO_Serialization_GH_Chunk_GetInterval1D.htm "GetInterval1D Method ")

[GetInterval1D Method (String)](../html/M_GH_IO_Serialization_GH_Chunk_GetInterval1D.htm "GetInterval1D Method (String)")

[GetInterval1D Method (String, Int32)](../html/M_GH_IO_Serialization_GH_Chunk_GetInterval1D_1.htm "GetInterval1D Method (String, Int32)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ChunkAddLanguageSpecificTextSet("LST36B346BF\_0?cpp=::|nu=.");GetInterval1D Method (String) |

Gets the value of the item with the specified name.
Name comparison is not case-sensitive.

**Namespace:**
 [GH\_IO.Serialization](N_GH_IO_Serialization.htm)  
**Assembly:**
 GH\_IO (in GH\_IO.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public GH_Interval1D GetInterval1D(
	string item_name
)
```

```
Public Function GetInterval1D ( 
	item_name As String
) As GH_Interval1D
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

item\_name
:   Type: [SystemAddLanguageSpecificTextSet("LST36B346BF\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of item to retrieve.

#### Return Value

Type: [GH\_Interval1D](T_GH_IO_Types_GH_Interval1D.htm)  
The inner value of the item.

#### Implements

[GH\_IReaderAddLanguageSpecificTextSet("LST36B346BF\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");GetInterval1D(String)](M_GH_IO_Serialization_GH_IReader_GetInterval1D.htm)

![](../icons/SectionExpanded.png)Exceptions

| Exception | Condition |
| --- | --- |
| [OverflowException](https://docs.microsoft.com/dotnet/api/system.overflowexception) | Thrown if the type conversion fails. |
| [InvalidCastException](https://docs.microsoft.com/dotnet/api/system.invalidcastexception) | Thrown if the type conversion is invalid. |
| [NullReferenceException](https://docs.microsoft.com/dotnet/api/system.nullreferenceexception) | Thrown if the item with the specified name does not exist. |

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Chunk Class](T_GH_IO_Serialization_GH_Chunk.htm)

[GetInterval1D Overload](Overload_GH_IO_Serialization_GH_Chunk_GetInterval1D.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)