# M_GH_IO_Serialization_GH_Chunk_SetByteArray_1

﻿ GH\_Chunk.SetByteArray Method (String, Int32, Byte[])

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_Chunk Class](../html/T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Class")

[GH\_Chunk Methods](../html/Methods_T_GH_IO_Serialization_GH_Chunk.htm "GH_Chunk Methods")

[SetByteArray Method](../html/Overload_GH_IO_Serialization_GH_Chunk_SetByteArray.htm "SetByteArray Method ")

[SetByteArray Method (String, Byte[])](../html/M_GH_IO_Serialization_GH_Chunk_SetByteArray.htm "SetByteArray Method (String, Byte[])")

[SetByteArray Method (String, Int32, Byte[])](../html/M_GH_IO_Serialization_GH_Chunk_SetByteArray_1.htm "SetByteArray Method (String, Int32, Byte[])")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ChunkAddLanguageSpecificTextSet("LST95B1B521\_0?cpp=::|nu=.");SetByteArray Method (String, Int32, AddLanguageSpecificTextSet("LST95B1B521\_1?cpp=array&lt;");ByteAddLanguageSpecificTextSet("LST95B1B521\_2?cpp=&gt;|vb=()|nu=[]");) |

Add a new data item to this chunk.
The combination of name and index must be unique or an exception will be thrown.

**Namespace:**
 [GH\_IO.Serialization](N_GH_IO_Serialization.htm)  
**Assembly:**
 GH\_IO (in GH\_IO.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public void SetByteArray(
	string item_name,
	int item_index,
	byte[] item_value
)
```

```
Public Sub SetByteArray ( 
	item_name As String,
	item_index As Integer,
	item_value As Byte()
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

item\_name
:   Type: [SystemAddLanguageSpecificTextSet("LST95B1B521\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of item to add.

item\_index
:   Type: [SystemAddLanguageSpecificTextSet("LST95B1B521\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Index of item to add.

item\_value
:   Type: AddLanguageSpecificTextSet("LST95B1B521\_5?cpp=array&lt;");[SystemAddLanguageSpecificTextSet("LST95B1B521\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");Byte](https://docs.microsoft.com/dotnet/api/system.byte)AddLanguageSpecificTextSet("LST95B1B521\_7?cpp=&gt;|vb=()|nu=[]");  
    Value of item to add.

#### Implements

[GH\_IWriterAddLanguageSpecificTextSet("LST95B1B521\_8?cs=.|vb=.|cpp=::|nu=.|fs=.");SetByteArray(String, Int32, AddLanguageSpecificTextSet("LST95B1B521\_9?cpp=array&lt;");ByteAddLanguageSpecificTextSet("LST95B1B521\_10?cpp=&gt;|cs=[]|vb=()|nu=[]|fs=[]");)](M_GH_IO_Serialization_GH_IWriter_SetByteArray_1.htm)

![](../icons/SectionExpanded.png)Exceptions

| Exception | Condition |
| --- | --- |
| [InvalidOperationException](https://docs.microsoft.com/dotnet/api/system.invalidoperationexception) | Thrown if another item with the same name and index already exists. |

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Chunk Class](T_GH_IO_Serialization_GH_Chunk.htm)

[SetByteArray Overload](Overload_GH_IO_Serialization_GH_Chunk_SetByteArray.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)