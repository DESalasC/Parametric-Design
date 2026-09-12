# M_GH_IO_Serialization_GH_IWriter_SetByteArray

﻿ GH\_IWriter.SetByteArray Method (String, Byte[])

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_IWriter Interface](../html/T_GH_IO_Serialization_GH_IWriter.htm "GH_IWriter Interface")

[GH\_IWriter Methods](../html/Methods_T_GH_IO_Serialization_GH_IWriter.htm "GH_IWriter Methods")

[SetByteArray Method](../html/Overload_GH_IO_Serialization_GH_IWriter_SetByteArray.htm "SetByteArray Method ")

[SetByteArray Method (String, Byte[])](../html/M_GH_IO_Serialization_GH_IWriter_SetByteArray.htm "SetByteArray Method (String, Byte[])")

[SetByteArray Method (String, Int32, Byte[])](../html/M_GH_IO_Serialization_GH_IWriter_SetByteArray_1.htm "SetByteArray Method (String, Int32, Byte[])")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_IWriterAddLanguageSpecificTextSet("LST303D6965\_0?cpp=::|nu=.");SetByteArray Method (String, AddLanguageSpecificTextSet("LST303D6965\_1?cpp=array&lt;");ByteAddLanguageSpecificTextSet("LST303D6965\_2?cpp=&gt;|vb=()|nu=[]");) |

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
void SetByteArray(
	string item_name,
	byte[] item_value
)
```

```
Sub SetByteArray ( 
	item_name As String,
	item_value As Byte()
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

item\_name
:   Type: [SystemAddLanguageSpecificTextSet("LST303D6965\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    Name of item to add.

item\_value
:   Type: AddLanguageSpecificTextSet("LST303D6965\_4?cpp=array&lt;");[SystemAddLanguageSpecificTextSet("LST303D6965\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");Byte](https://docs.microsoft.com/dotnet/api/system.byte)AddLanguageSpecificTextSet("LST303D6965\_6?cpp=&gt;|vb=()|nu=[]");  
    Value of item to add.

![](../icons/SectionExpanded.png)Exceptions

| Exception | Condition |
| --- | --- |
| [InvalidOperationException](https://docs.microsoft.com/dotnet/api/system.invalidoperationexception) | Thrown if another item with the same name already exists. |

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_IWriter Interface](T_GH_IO_Serialization_GH_IWriter.htm)

[SetByteArray Overload](Overload_GH_IO_Serialization_GH_IWriter_SetByteArray.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)