# M_GH_IO_Serialization_GH_Chunk_GetPath_1

﻿ GH\_Chunk.GetPath Method (String, String)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_Chunk Class](../html/T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Class")

[GH\_Chunk Methods](../html/Methods_T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Methods")

[GetPath Method](../html/Overload_GH_IO_Serialization_GH_Chunk_GetPath.htm "GetPath Method ")

[GetPath Method (String, String)](../html/M_GH_IO_Serialization_GH_Chunk_GetPath_1.htm "GetPath Method (String, String)")

[GetPath Method (String, Int32, String)](../html/M_GH_IO_Serialization_GH_Chunk_GetPath.htm "GetPath Method (String, Int32, String)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ChunkAddLanguageSpecificTextSet("LST5DA87A44\_0?cpp=::|nu=.");GetPath Method (String, String) |

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
public string[] GetPath(
	string item_name,
	string basePath
)
```

```
Public Function GetPath ( 
	item_name As String,
	basePath As String
) As String()
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

item\_name
:   Type: [SystemAddLanguageSpecificTextSet("LST5DA87A44\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of item to retrieve.

basePath
:   Type: [SystemAddLanguageSpecificTextSet("LST5DA87A44\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Base path for relative path resolution.

#### Return Value

Type: AddLanguageSpecificTextSet("LST5DA87A44\_3?cpp=array&lt;");[String](https://docs.microsoft.com/dotnet/api/system.string)AddLanguageSpecificTextSet("LST5DA87A44\_4?cpp=&gt;|vb=()|nu=[]");  
An array of path strings. If the resolved relative path is different
from the stored absolute path, an array of two strings will be returned [absolute, relative].

#### Implements

[GH\_IReaderAddLanguageSpecificTextSet("LST5DA87A44\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");GetPath(String, String)](M_GH_IO_Serialization_GH_IReader_GetPath_1.htm)

![](../icons/SectionExpanded.png)Exceptions

| Exception | Condition |
| --- | --- |
| [OverflowException](https://docs.microsoft.com/dotnet/api/system.overflowexception) | Thrown if the type conversion fails. |
| [InvalidCastException](https://docs.microsoft.com/dotnet/api/system.invalidcastexception) | Thrown if the type conversion is invalid. |
| [NullReferenceException](https://docs.microsoft.com/dotnet/api/system.nullreferenceexception) | Thrown if the item with the specified name does not exist. |

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Chunk Class](T_GH_IO_Serialization_GH_Chunk.htm)

[GetPath Overload](Overload_GH_IO_Serialization_GH_Chunk_GetPath.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)