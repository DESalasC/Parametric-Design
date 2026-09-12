# M_GH_IO_GH_ISerializable_Write

﻿ GH\_ISerializable.Write Method 

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
| GH\_ISerializableAddLanguageSpecificTextSet("LST774C030B\_0?cpp=::|nu=.");Write Method |

This method is called whenever the instance is required to serialize itself.

**Namespace:**
 [GH\_IO](N_GH_IO.htm)  
**Assembly:**
 GH\_IO (in GH\_IO.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
bool Write(
	GH_IWriter writer
)
```

```
Function Write ( 
	writer As GH_IWriter
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

writer
:   Type: [GH\_IO.SerializationAddLanguageSpecificTextSet("LST774C030B\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_IWriter](T_GH_IO_Serialization_GH_IWriter.htm)  
    Writer object to serialize with.

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