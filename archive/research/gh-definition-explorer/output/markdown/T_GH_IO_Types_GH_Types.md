# T_GH_IO_Types_GH_Types

﻿ GH\_Types Enumeration

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Types](../html/N_GH_IO_Types.htm "GH_IO.Types")

[GH\_BoundingBox Structure](../html/T_GH_IO_Types_GH_BoundingBox.htm "GH_BoundingBox Structure")

[GH\_Interval1D Structure](../html/T_GH_IO_Types_GH_Interval1D.htm "GH_Interval1D Structure")

[GH\_Interval2D Structure](../html/T_GH_IO_Types_GH_Interval2D.htm "GH_Interval2D Structure")

[GH\_Item Class](../html/T_GH_IO_Types_GH_Item.htm "GH_Item Class")

[GH\_Line Structure](../html/T_GH_IO_Types_GH_Line.htm "GH_Line Structure")

[GH\_Plane Structure](../html/T_GH_IO_Types_GH_Plane.htm "GH_Plane Structure")

[GH\_Point2D Structure](../html/T_GH_IO_Types_GH_Point2D.htm "GH_Point2D Structure")

[GH\_Point3D Structure](../html/T_GH_IO_Types_GH_Point3D.htm "GH_Point3D Structure")

[GH\_Point4D Structure](../html/T_GH_IO_Types_GH_Point4D.htm "GH_Point4D Structure")

[GH\_Types Enumeration](../html/T_GH_IO_Types_GH_Types.htm "GH_Types Enumeration")

[GH\_Version Structure](../html/T_GH_IO_Types_GH_Version.htm "GH_Version Structure")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_Types Enumeration |

Contains flags for all data types currently supported by GH\_IO.dll

**Namespace:**
 [GH\_IO.Types](N_GH_IO_Types.htm)  
**Assembly:**
 GH\_IO (in GH\_IO.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public enum GH_Types
```

```
Public Enumeration GH_Types
```

AddLanguageTabSet("ID0EBCA");

![](../icons/SectionExpanded.png)Members

|  | Member name | Value | Description |
| --- | --- | --- | --- |
|  | unset | 0 | Represents an unset type. GH\_Items with this type will throw exceptions during serialization. |
|  | gh\_bool | 1 | boolean |
|  | gh\_byte | 2 | byte |
|  | gh\_int32 | 3 | 32 bit integer |
|  | gh\_int64 | 4 | 64 bit integer |
|  | gh\_single | 5 | single precision floating point number |
|  | gh\_double | 6 | double precision floating point number |
|  | gh\_decimal | 7 | decimal number |
|  | gh\_date | 8 | date time structure |
|  | gh\_guid | 9 | 128 bit globally unique identifier |
|  | gh\_string | 10 | unicode string |
|  | gh\_bytearray | 20 | an array of bytes |
|  | gh\_doublearray | 21 | an array of doubles |
|  | gh\_drawing\_point | 30 | gdi+ integer precision point |
|  | gh\_drawing\_pointf | 31 | gdi+ single precision point |
|  | gh\_drawing\_size | 32 | gdi+ integer precision size |
|  | gh\_drawing\_sizef | 33 | gdi+ single precision size |
|  | gh\_drawing\_rectangle | 34 | gdi+ integer precision rectangle |
|  | gh\_drawing\_rectanglef | 35 | gdi+ single precision rectangle |
|  | gh\_drawing\_color | 36 | gdi+ argb color |
|  | gh\_drawing\_bitmap | 37 | gdi+ bitmap (png format bytestream) |
|  | gh\_point2d | 50 | double precision two-dimensional point |
|  | gh\_point3d | 51 | double precision three-dimensional point |
|  | gh\_point4d | 52 | double precision four-dimensional point |
|  | gh\_interval1d | 60 | double precision one-dimensional numeric interval |
|  | gh\_interval2d | 61 | double precision two-dimensional numeric interval |
|  | gh\_line | 70 | double precision three-dimensional line segment |
|  | gh\_boundingbox | 71 | double precision three-dimensional box volume |
|  | gh\_plane | 72 | double precision three-dimensional plane construct |
|  | gh\_version | 80 | version structure with major, minor and revision fields |

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_IO.Types Namespace](N_GH_IO_Types.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)