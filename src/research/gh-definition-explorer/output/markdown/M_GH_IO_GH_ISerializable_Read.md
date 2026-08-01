# M_GH_IO_GH_ISerializable_Read

﻿ GH\_ISerializable.Read Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO](../html/N_GH_IO.htm "GH_IO")

[GH\_ISerializable Interface](../html/T_GH_IO_GH_ISerializable.htm "GH_ISerializable Interface")

[GH\_ISerializable Methods](../html/Methods_T_GH_IO_GH_ISerializable.htm "GH_ISerializable Methods")

[Read Method](../html/M_GH_IO_GH_ISerializable_Read.htm "Read Method ")

[Write Method](../html/M_GH_IO_GH_ISerializable_Write.htm "Write Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ISerializableAddLanguageSpecificTextSet("LSTBAAF5AE\_0?cpp=::|nu=.");Read Method |

This method is called whenever the instance is required to deserialize itself.

**Namespace:**
 [GH\_IO](N_GH_IO.htm)  
**Assembly:**
 GH\_IO (in GH\_IO.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
bool Read(
	GH_IReader reader
)
```

```
Function Read ( 
	reader As GH_IReader
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

reader
:   Type: [GH\_IO.SerializationAddLanguageSpecificTextSet("LSTBAAF5AE\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_IReader](T_GH_IO_Serialization_GH_IReader.htm)  
    Reader object to deserialize from.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True on success, false on failure.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_ISerializable Interface](T_GH_IO_GH_ISerializable.htm)

[GH\_IO Namespace](N_GH_IO.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)