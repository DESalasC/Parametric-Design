# M_GH_IO_Serialization_GH_Compression_Compress

﻿ GH\_Compression.Compress Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_Compression Class](../html/T_GH_IO_Serialization_GH_Compression.htm "GH_Compression Class")

[GH\_Compression Methods](../html/Methods_T_GH_IO_Serialization_GH_Compression.htm "GH_Compression Methods")

[Compress Method](../html/M_GH_IO_Serialization_GH_Compression_Compress.htm "Compress Method ")

[Decompress Method](../html/M_GH_IO_Serialization_GH_Compression_Decompress.htm "Decompress Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_CompressionAddLanguageSpecificTextSet("LST74851DDA\_0?cpp=::|nu=.");Compress Method |

Compress an array of bytes using the Deflate algorithm.

**Namespace:**
 [GH\_IO.Serialization](N_GH_IO_Serialization.htm)  
**Assembly:**
 GH\_IO (in GH\_IO.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static byte[] Compress(
	byte[] data
)
```

```
Public Shared Function Compress ( 
	data As Byte()
) As Byte()
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

data
:   Type: AddLanguageSpecificTextSet("LST74851DDA\_1?cpp=array&lt;");[SystemAddLanguageSpecificTextSet("LST74851DDA\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Byte](https://docs.microsoft.com/dotnet/api/system.byte)AddLanguageSpecificTextSet("LST74851DDA\_3?cpp=&gt;|vb=()|nu=[]");  
    Byte array to compress.

#### Return Value

Type: AddLanguageSpecificTextSet("LST74851DDA\_4?cpp=array&lt;");[Byte](https://docs.microsoft.com/dotnet/api/system.byte)AddLanguageSpecificTextSet("LST74851DDA\_5?cpp=&gt;|vb=()|nu=[]");  
An array of compressed bytes.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Compression Class](T_GH_IO_Serialization_GH_Compression.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)