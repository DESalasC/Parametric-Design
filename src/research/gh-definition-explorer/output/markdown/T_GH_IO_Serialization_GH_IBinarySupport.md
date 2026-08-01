# T_GH_IO_Serialization_GH_IBinarySupport

﻿ GH\_IBinarySupport Interface

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_IBinarySupport Interface](../html/T_GH_IO_Serialization_GH_IBinarySupport.htm "GH_IBinarySupport Interface")

[GH\_IBinarySupport Methods](../html/Methods_T_GH_IO_Serialization_GH_IBinarySupport.htm "GH_IBinarySupport Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_IBinarySupport Interface |

Interface which declares all methods required for objects that
can be (de)serialized to and from a binary archive.

**Namespace:**
 [GH\_IO.Serialization](N_GH_IO_Serialization.htm)  
**Assembly:**
 GH\_IO (in GH\_IO.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public interface GH_IBinarySupport
```

```
Public Interface GH_IBinarySupport
```

AddLanguageTabSet("ID0EBCA");

The GH\_IBinarySupport type exposes the following members.

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [Read](M_GH_IO_Serialization_GH_IBinarySupport_Read.htm) | Called when an object is required to deserialize itself. |
| Public method | [Write](M_GH_IO_Serialization_GH_IBinarySupport_Write.htm) | Called when an object is required to serialize itself. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)