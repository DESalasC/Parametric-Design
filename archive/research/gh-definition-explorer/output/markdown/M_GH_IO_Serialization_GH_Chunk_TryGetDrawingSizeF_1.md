# M_GH_IO_Serialization_GH_Chunk_TryGetDrawingSizeF_1

﻿ GH\_Chunk.TryGetDrawingSizeF Method (String, Int32, SizeF)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_Chunk Class](../html/T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Class")

[GH\_Chunk Methods](../html/Methods_T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Methods")

[TryGetDrawingSizeF Method](../html/Overload_GH_IO_Serialization_GH_Chunk_TryGetDrawingSizeF.htm "TryGetDrawingSizeF Method ")

[TryGetDrawingSizeF Method (String, SizeF)](../html/M_GH_IO_Serialization_GH_Chunk_TryGetDrawingSizeF.htm "TryGetDrawingSizeF Method (String, SizeF)")

[TryGetDrawingSizeF Method (String, Int32, SizeF)](../html/M_GH_IO_Serialization_GH_Chunk_TryGetDrawingSizeF_1.htm "TryGetDrawingSizeF Method (String, Int32, SizeF)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ChunkAddLanguageSpecificTextSet("LST2B420420\_0?cpp=::|nu=.");TryGetDrawingSizeF Method (String, Int32, SizeFAddLanguageSpecificTextSet("LST2B420420\_1?cpp=%");) |

Gets the value of the item with the specified name and index.
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
public bool TryGetDrawingSizeF(
	string item_name,
	int item_index,
	ref SizeF value
)
```

```
Public Function TryGetDrawingSizeF ( 
	item_name As String,
	item_index As Integer,
	ByRef value As SizeF
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

item\_name
:   Type: [SystemAddLanguageSpecificTextSet("LST2B420420\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of item to retrieve.

item\_index
:   Type: [SystemAddLanguageSpecificTextSet("LST2B420420\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Index of item to retrieve.

value
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST2B420420\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");SizeF](https://docs.microsoft.com/dotnet/api/system.drawing.sizef)AddLanguageSpecificTextSet("LST2B420420\_5?cpp=%");  
    Target of assignment.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True if the value was set.

#### Implements

[GH\_IReaderAddLanguageSpecificTextSet("LST2B420420\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");TryGetDrawingSizeF(String, Int32, SizeFAddLanguageSpecificTextSet("LST2B420420\_7?cpp=%");)](M_GH_IO_Serialization_GH_IReader_TryGetDrawingSizeF_1.htm)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Chunk Class](T_GH_IO_Serialization_GH_Chunk.htm)

[TryGetDrawingSizeF Overload](Overload_GH_IO_Serialization_GH_Chunk_TryGetDrawingSizeF.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)