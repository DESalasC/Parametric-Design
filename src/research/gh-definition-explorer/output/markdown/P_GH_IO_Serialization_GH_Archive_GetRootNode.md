# P_GH_IO_Serialization_GH_Archive_GetRootNode

﻿ GH\_Archive.GetRootNode Property 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_Archive Class](../html/T_GH_IO_Serialization_GH_Archive.htm "GH_Archive Class")

[GH\_Archive Properties](../html/Properties_T_GH_IO_Serialization_GH_Archive.htm "GH_Archive Properties")

[FileName Property](../html/P_GH_IO_Serialization_GH_Archive_FileName.htm "FileName Property ")

[GetRootNode Property](../html/P_GH_IO_Serialization_GH_Archive_GetRootNode.htm "GetRootNode Property ")

[GH\_IO\_Version Property](../html/P_GH_IO_Serialization_GH_Archive_GH_IO_Version.htm "GH_IO_Version Property ")

[GrasshopperBinaryExtension Property](../html/P_GH_IO_Serialization_GH_Archive_GrasshopperBinaryExtension.htm "GrasshopperBinaryExtension Property ")

[GrasshopperUserExtension Property](../html/P_GH_IO_Serialization_GH_Archive_GrasshopperUserExtension.htm "GrasshopperUserExtension Property ")

[GrasshopperXmlExtension Property](../html/P_GH_IO_Serialization_GH_Archive_GrasshopperXmlExtension.htm "GrasshopperXmlExtension Property ")

[IsBinaryPath Property](../html/P_GH_IO_Serialization_GH_Archive_IsBinaryPath.htm "IsBinaryPath Property ")

[IsPath Property](../html/P_GH_IO_Serialization_GH_Archive_IsPath.htm "IsPath Property ")

[IsXmlPath Property](../html/P_GH_IO_Serialization_GH_Archive_IsXmlPath.htm "IsXmlPath Property ")

[Messages Property](../html/P_GH_IO_Serialization_GH_Archive_Messages.htm "Messages Property ")

[Path Property](../html/P_GH_IO_Serialization_GH_Archive_Path.htm "Path Property ")

[WorstCaseMessageType Property](../html/P_GH_IO_Serialization_GH_Archive_WorstCaseMessageType.htm "WorstCaseMessageType Property ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ArchiveAddLanguageSpecificTextSet("LST70E98B0F\_0?cpp=::|nu=.");GetRootNode Property |

Gets the root node of this archive.
Typically you do not need to modify the Root.
Use functions like CreateTopLevelNode(), AppendObject() and ExtractObject() instead.
If you modify the Root node, you may corrupt the archive.

**Namespace:**
 [GH\_IO.Serialization](N_GH_IO_Serialization.htm)  
**Assembly:**
 GH\_IO (in GH\_IO.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public GH_Chunk GetRootNode { get; }
```

```
Public ReadOnly Property GetRootNode As GH_Chunk
	Get
```

AddLanguageTabSet("ID0EBCA");

#### Property Value

Type: [GH\_Chunk](T_GH_IO_Serialization_GH_Chunk.htm)  

[Missing <value> documentation for "P:GH\_IO.Serialization.GH\_Archive.GetRootNode"]

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Archive Class](T_GH_IO_Serialization_GH_Archive.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)