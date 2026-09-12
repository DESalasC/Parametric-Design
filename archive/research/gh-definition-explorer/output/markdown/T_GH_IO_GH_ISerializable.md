# T_GH_IO_GH_ISerializable

﻿ GH\_ISerializable Interface

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO](../html/N_GH_IO.htm "GH_IO")

[GH\_ISerializable Interface](../html/T_GH_IO_GH_ISerializable.htm "GH_ISerializable Interface")

[GH\_ISerializable Methods](../html/Methods_T_GH_IO_GH_ISerializable.htm "GH_ISerializable Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ISerializable Interface |

Every object which needs to (de)serialize itself using GH\_IO methodology
must implement this interface.

**Namespace:**
 [GH\_IO](N_GH_IO.htm)  
**Assembly:**
 GH\_IO (in GH\_IO.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public interface GH_ISerializable
```

```
Public Interface GH_ISerializable
```

AddLanguageTabSet("ID0EBCA");

The GH\_ISerializable type exposes the following members.

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [Read](M_GH_IO_GH_ISerializable_Read.htm) | This method is called whenever the instance is required to deserialize itself. |
| Public method | [Write](M_GH_IO_GH_ISerializable_Write.htm) | This method is called whenever the instance is required to serialize itself. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_IO Namespace](N_GH_IO.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)