# P_GH_IO_Types_GH_Item__point3d

﻿ GH\_Item.\_point3d Property 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Types](../html/N_GH_IO_Types.htm "GH_IO.Types")

[GH\_Item Class](../html/T_GH_IO_Types_GH_Item.htm "GH_Item Class")

[GH\_Item Properties](../html/Properties_T_GH_IO_Types_GH_Item.htm "GH_Item Properties")

[\_bool Property](../html/P_GH_IO_Types_GH_Item__bool.htm "_bool Property ")

[\_boundingbox Property](../html/P_GH_IO_Types_GH_Item__boundingbox.htm "_boundingbox Property ")

[\_byte Property](../html/P_GH_IO_Types_GH_Item__byte.htm "_byte Property ")

[\_bytearray Property](../html/P_GH_IO_Types_GH_Item__bytearray.htm "_bytearray Property ")

[\_date Property](../html/P_GH_IO_Types_GH_Item__date.htm "_date Property ")

[\_decimal Property](../html/P_GH_IO_Types_GH_Item__decimal.htm "_decimal Property ")

[\_double Property](../html/P_GH_IO_Types_GH_Item__double.htm "_double Property ")

[\_doublearray Property](../html/P_GH_IO_Types_GH_Item__doublearray.htm "_doublearray Property ")

[\_drawing\_bitmap Property](../html/P_GH_IO_Types_GH_Item__drawing_bitmap.htm "_drawing_bitmap Property ")

[\_drawing\_color Property](../html/P_GH_IO_Types_GH_Item__drawing_color.htm "_drawing_color Property ")

[\_drawing\_point Property](../html/P_GH_IO_Types_GH_Item__drawing_point.htm "_drawing_point Property ")

[\_drawing\_pointf Property](../html/P_GH_IO_Types_GH_Item__drawing_pointf.htm "_drawing_pointf Property ")

[\_drawing\_rectangle Property](../html/P_GH_IO_Types_GH_Item__drawing_rectangle.htm "_drawing_rectangle Property ")

[\_drawing\_rectanglef Property](../html/P_GH_IO_Types_GH_Item__drawing_rectanglef.htm "_drawing_rectanglef Property ")

[\_drawing\_size Property](../html/P_GH_IO_Types_GH_Item__drawing_size.htm "_drawing_size Property ")

[\_drawing\_sizef Property](../html/P_GH_IO_Types_GH_Item__drawing_sizef.htm "_drawing_sizef Property ")

[\_guid Property](../html/P_GH_IO_Types_GH_Item__guid.htm "_guid Property ")

[\_int32 Property](../html/P_GH_IO_Types_GH_Item__int32.htm "_int32 Property ")

[\_int64 Property](../html/P_GH_IO_Types_GH_Item__int64.htm "_int64 Property ")

[\_interval1d Property](../html/P_GH_IO_Types_GH_Item__interval1d.htm "_interval1d Property ")

[\_interval2d Property](../html/P_GH_IO_Types_GH_Item__interval2d.htm "_interval2d Property ")

[\_line Property](../html/P_GH_IO_Types_GH_Item__line.htm "_line Property ")

[\_plane Property](../html/P_GH_IO_Types_GH_Item__plane.htm "_plane Property ")

[\_point2d Property](../html/P_GH_IO_Types_GH_Item__point2d.htm "_point2d Property ")

[\_point3d Property](../html/P_GH_IO_Types_GH_Item__point3d.htm "_point3d Property ")

[\_point4d Property](../html/P_GH_IO_Types_GH_Item__point4d.htm "_point4d Property ")

[\_single Property](../html/P_GH_IO_Types_GH_Item__single.htm "_single Property ")

[\_string Property](../html/P_GH_IO_Types_GH_Item__string.htm "_string Property ")

[\_version Property](../html/P_GH_IO_Types_GH_Item__version.htm "_version Property ")

[HasIndex Property](../html/P_GH_IO_Types_GH_Item_HasIndex.htm "HasIndex Property ")

[HasName Property](../html/P_GH_IO_Types_GH_Item_HasName.htm "HasName Property ")

[HasType Property](../html/P_GH_IO_Types_GH_Item_HasType.htm "HasType Property ")

[Index Property](../html/P_GH_IO_Types_GH_Item_Index.htm "Index Property ")

[InternalData Property](../html/P_GH_IO_Types_GH_Item_InternalData.htm "InternalData Property ")

[Name Property](../html/P_GH_IO_Types_GH_Item_Name.htm "Name Property ")

[Type Property](../html/P_GH_IO_Types_GH_Item_Type.htm "Type Property ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ItemAddLanguageSpecificTextSet("LSTAAB7E507\_0?cpp=::|nu=.");\_point3d Property |

Returns the internal data of this item cast to a Point3D.
If the data is not stored as a Point3D, a conversion exception might be thrown.

**Namespace:**
 [GH\_IO.Types](N_GH_IO_Types.htm)  
**Assembly:**
 GH\_IO (in GH\_IO.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public GH_Point3D _point3d { get; }
```

```
Public ReadOnly Property _point3d As GH_Point3D
	Get
```

AddLanguageTabSet("ID0EBCA");

#### Property Value

Type: [GH\_Point3D](T_GH_IO_Types_GH_Point3D.htm)  

[Missing <value> documentation for "P:GH\_IO.Types.GH\_Item.\_point3d"]

![](../icons/SectionExpanded.png)Exceptions

| Exception | Condition |
| --- | --- |
| [OverflowException](https://docs.microsoft.com/dotnet/api/system.overflowexception) | Thrown if the type conversion fails. |
| [InvalidCastException](https://docs.microsoft.com/dotnet/api/system.invalidcastexception) | Thrown if the type conversion is invalid. |

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Item Class](T_GH_IO_Types_GH_Item.htm)

[GH\_IO.Types Namespace](N_GH_IO_Types.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)