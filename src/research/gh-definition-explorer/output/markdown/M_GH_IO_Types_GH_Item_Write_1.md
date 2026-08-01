# M_GH_IO_Types_GH_Item_Write_1

﻿ GH\_Item.Write Method (XmlWriter)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Types](../html/N_GH_IO_Types.htm "GH_IO.Types")

[GH\_Item Class](../html/T_GH_IO_Types_GH_Item.htm "GH_Item Class")

[GH\_Item Methods](../html/Methods_T_GH_IO_Types_GH_Item.htm "GH_Item Methods")

[Write Method](../html/Overload_GH_IO_Types_GH_Item_Write.htm "Write Method ")

[Write Method (BinaryWriter)](../html/M_GH_IO_Types_GH_Item_Write.htm "Write Method (BinaryWriter)")

[Write Method (XmlWriter)](../html/M_GH_IO_Types_GH_Item_Write_1.htm "Write Method (XmlWriter)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ItemAddLanguageSpecificTextSet("LST453C6A5C\_0?cpp=::|nu=.");Write Method (XmlWriter) |

Serialize this item into an Xml stream.

**Namespace:**
 [GH\_IO.Types](N_GH_IO_Types.htm)  
**Assembly:**
 GH\_IO (in GH\_IO.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public void Write(
	XmlWriter writer
)
```

```
Public Sub Write ( 
	writer As XmlWriter
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

writer
:   Type: [System.XmlAddLanguageSpecificTextSet("LST453C6A5C\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");XmlWriter](https://docs.microsoft.com/dotnet/api/system.xml.xmlwriter)  
    Writer to serialize with.

#### Implements

[GH\_IXmlSupportAddLanguageSpecificTextSet("LST453C6A5C\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Write(XmlWriter)](M_GH_IO_Serialization_GH_IXmlSupport_Write.htm)

![](../icons/SectionExpanded.png)Exceptions

| Exception | Condition |
| --- | --- |
| [MemberAccessException](https://docs.microsoft.com/dotnet/api/system.memberaccessexception) | Thrown if !HasName. |
| [MemberAccessException](https://docs.microsoft.com/dotnet/api/system.memberaccessexception) | Thrown if !HasType. |
| [IOException](https://docs.microsoft.com/dotnet/api/system.io.ioexception) | Thrown if the internal data could not be serialized. |

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Item Class](T_GH_IO_Types_GH_Item.htm)

[Write Overload](Overload_GH_IO_Types_GH_Item_Write.htm)

[GH\_IO.Types Namespace](N_GH_IO_Types.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)