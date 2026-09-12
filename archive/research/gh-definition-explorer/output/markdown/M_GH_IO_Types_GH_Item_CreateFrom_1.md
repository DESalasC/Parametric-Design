# M_GH_IO_Types_GH_Item_CreateFrom_1

﻿ GH\_Item.CreateFrom Method (XmlNode)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Types](../html/N_GH_IO_Types.htm "GH_IO.Types")

[GH\_Item Class](../html/T_GH_IO_Types_GH_Item.htm "GH_Item Class")

[GH\_Item Methods](../html/Methods_T_GH_IO_Types_GH_Item.htm "GH_Item Methods")

[CreateFrom Method](../html/Overload_GH_IO_Types_GH_Item_CreateFrom.htm "CreateFrom Method ")

[CreateFrom Method (BinaryReader)](../html/M_GH_IO_Types_GH_Item_CreateFrom.htm "CreateFrom Method (BinaryReader)")

[CreateFrom Method (XmlNode)](../html/M_GH_IO_Types_GH_Item_CreateFrom_1.htm "CreateFrom Method (XmlNode)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ItemAddLanguageSpecificTextSet("LST4EB7642F\_0?cpp=::|nu=.");CreateFrom Method (XmlNode) |

Creates a new instance of GH\_Item and sets the fields from an Xml node object.

**Namespace:**
 [GH\_IO.Types](N_GH_IO_Types.htm)  
**Assembly:**
 GH\_IO (in GH\_IO.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static GH_Item CreateFrom(
	XmlNode node
)
```

```
Public Shared Function CreateFrom ( 
	node As XmlNode
) As GH_Item
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

node
:   Type: [System.XmlAddLanguageSpecificTextSet("LST4EB7642F\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");XmlNode](https://docs.microsoft.com/dotnet/api/system.xml.xmlnode)  
    Xml node object that defines the field data.

#### Return Value

Type: [GH\_Item](T_GH_IO_Types_GH_Item.htm)  
The constructed and read item.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Item Class](T_GH_IO_Types_GH_Item.htm)

[CreateFrom Overload](Overload_GH_IO_Types_GH_Item_CreateFrom.htm)

[GH\_IO.Types Namespace](N_GH_IO_Types.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)