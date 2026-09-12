# M_GH_IO_Serialization_GH_Chunk_GetPoint3D

﻿ GH\_Chunk.GetPoint3D Method (String)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_Chunk Class](../html/T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Class")

[GH\_Chunk Methods](../html/Methods_T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Methods")

[GetPoint3D Method](../html/Overload_GH_IO_Serialization_GH_Chunk_GetPoint3D.htm "GetPoint3D Method ")

[GetPoint3D Method (String)](../html/M_GH_IO_Serialization_GH_Chunk_GetPoint3D.htm "GetPoint3D Method (String)")

[GetPoint3D Method (String, Int32)](../html/M_GH_IO_Serialization_GH_Chunk_GetPoint3D_1.htm "GetPoint3D Method (String, Int32)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ChunkAddLanguageSpecificTextSet("LST535C8BDB\_0?cpp=::|nu=.");GetPoint3D Method (String) |

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
public GH_Point3D GetPoint3D(
	string item_name
)
```

```
Public Function GetPoint3D ( 
	item_name As String
) As GH_Point3D
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

item\_name
:   Type: [SystemAddLanguageSpecificTextSet("LST535C8BDB\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of item to retrieve.

#### Return Value

Type: [GH\_Point3D](T_GH_IO_Types_GH_Point3D.htm)  
The inner value of the item.

#### Implements

[GH\_IReaderAddLanguageSpecificTextSet("LST535C8BDB\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");GetPoint3D(String)](M_GH_IO_Serialization_GH_IReader_GetPoint3D.htm)

![](../icons/SectionExpanded.png)Exceptions

| Exception | Condition |
| --- | --- |
| [OverflowException](https://docs.microsoft.com/dotnet/api/system.overflowexception) | Thrown if the type conversion fails. |
| [InvalidCastException](https://docs.microsoft.com/dotnet/api/system.invalidcastexception) | Thrown if the type conversion is invalid. |
| [NullReferenceException](https://docs.microsoft.com/dotnet/api/system.nullreferenceexception) | Thrown if the item with the specified name does not exist. |

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Chunk Class](T_GH_IO_Serialization_GH_Chunk.htm)

[GetPoint3D Overload](Overload_GH_IO_Serialization_GH_Chunk_GetPoint3D.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)