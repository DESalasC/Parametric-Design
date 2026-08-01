# M_GH_IO_Serialization_GH_LooseChunk_Serialize_Xml

﻿ GH\_LooseChunk.Serialize\_Xml Method  

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_LooseChunk Class](../html/T_GH_IO_Serialization_GH_LooseChunk.htm "GH_LooseChunk Class")

[GH\_LooseChunk Methods](../html/Methods_T_GH_IO_Serialization_GH_LooseChunk.htm "GH_LooseChunk Methods")

[Deserialize\_Binary Method](../html/M_GH_IO_Serialization_GH_LooseChunk_Deserialize_Binary.htm "Deserialize_Binary Method ")

[Deserialize\_Xml Method](../html/M_GH_IO_Serialization_GH_LooseChunk_Deserialize_Xml.htm "Deserialize_Xml Method ")

[Serialize\_Binary Method](../html/M_GH_IO_Serialization_GH_LooseChunk_Serialize_Binary.htm "Serialize_Binary Method ")

[Serialize\_Xml Method](../html/M_GH_IO_Serialization_GH_LooseChunk_Serialize_Xml.htm "Serialize_Xml Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_LooseChunkAddLanguageSpecificTextSet("LSTB3D29C91\_0?cpp=::|nu=.");Serialize\_Xml Method |

Serializes the data tree into an Xml string.

**Namespace:**
 [GH\_IO.Serialization](N_GH_IO_Serialization.htm)  
**Assembly:**
 GH\_IO (in GH\_IO.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public string Serialize_Xml()
```

```
Public Function Serialize_Xml As String
```

AddLanguageTabSet("ID0EBCA");

#### Return Value

Type: [String](https://docs.microsoft.com/dotnet/api/system.string)  
A string containing the Xml content.

![](../icons/SectionExpanded.png)Examples

This sample shows how to create a new loose chunk and serialize some values.

C#

[Copy](# "Copy")

```
public string CreateXML(string archive_name, string[] item_names, int[] item_values)
{
  GH_LooseChunk chunk = new GH_LooseChunk(archive_name);

  for (int i = 0; i < item_names.Length; i++)
  {
    chunk.SetInt32(item_names[i], i, item_values[i]);
  }

  return chunk.Serialize_Xml();
}
```

AddLanguageTabSet("ID0EAAABA");

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_LooseChunk Class](T_GH_IO_Serialization_GH_LooseChunk.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)