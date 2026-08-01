# M_GH_IO_Serialization_GH_IWriter_AddComment

﻿ GH\_IWriter.AddComment Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[GH\_IO.Serialization](../html/N_GH_IO_Serialization.htm "GH_IO.Serialization")

[GH\_IWriter Interface](../html/T_GH_IO_Serialization_GH_IWriter.htm "GH_IWriter Interface")

[GH\_IWriter Methods](../html/Methods_T_GH_IO_Serialization_GH_IWriter.htm "GH_IWriter Methods")

[AddComment Method](../html/M_GH_IO_Serialization_GH_IWriter_AddComment.htm "AddComment Method ")

[CreateChunk Method](../html/Overload_GH_IO_Serialization_GH_IWriter_CreateChunk.htm "CreateChunk Method ")

[RemoveChunk Method](../html/Overload_GH_IO_Serialization_GH_IWriter_RemoveChunk.htm "RemoveChunk Method ")

[RemoveItem Method](../html/Overload_GH_IO_Serialization_GH_IWriter_RemoveItem.htm "RemoveItem Method ")

[SetBoolean Method](../html/Overload_GH_IO_Serialization_GH_IWriter_SetBoolean.htm "SetBoolean Method ")

[SetBoundingBox Method](../html/Overload_GH_IO_Serialization_GH_IWriter_SetBoundingBox.htm "SetBoundingBox Method ")

[SetByte Method](../html/Overload_GH_IO_Serialization_GH_IWriter_SetByte.htm "SetByte Method ")

[SetByteArray Method](../html/Overload_GH_IO_Serialization_GH_IWriter_SetByteArray.htm "SetByteArray Method ")

[SetDate Method](../html/Overload_GH_IO_Serialization_GH_IWriter_SetDate.htm "SetDate Method ")

[SetDecimal Method](../html/Overload_GH_IO_Serialization_GH_IWriter_SetDecimal.htm "SetDecimal Method ")

[SetDouble Method](../html/Overload_GH_IO_Serialization_GH_IWriter_SetDouble.htm "SetDouble Method ")

[SetDoubleArray Method](../html/Overload_GH_IO_Serialization_GH_IWriter_SetDoubleArray.htm "SetDoubleArray Method ")

[SetDrawingBitmap Method](../html/Overload_GH_IO_Serialization_GH_IWriter_SetDrawingBitmap.htm "SetDrawingBitmap Method ")

[SetDrawingColor Method](../html/Overload_GH_IO_Serialization_GH_IWriter_SetDrawingColor.htm "SetDrawingColor Method ")

[SetDrawingPoint Method](../html/Overload_GH_IO_Serialization_GH_IWriter_SetDrawingPoint.htm "SetDrawingPoint Method ")

[SetDrawingPointF Method](../html/Overload_GH_IO_Serialization_GH_IWriter_SetDrawingPointF.htm "SetDrawingPointF Method ")

[SetDrawingRectangle Method](../html/Overload_GH_IO_Serialization_GH_IWriter_SetDrawingRectangle.htm "SetDrawingRectangle Method ")

[SetDrawingRectangleF Method](../html/Overload_GH_IO_Serialization_GH_IWriter_SetDrawingRectangleF.htm "SetDrawingRectangleF Method ")

[SetDrawingSize Method](../html/Overload_GH_IO_Serialization_GH_IWriter_SetDrawingSize.htm "SetDrawingSize Method ")

[SetDrawingSizeF Method](../html/Overload_GH_IO_Serialization_GH_IWriter_SetDrawingSizeF.htm "SetDrawingSizeF Method ")

[SetGuid Method](../html/Overload_GH_IO_Serialization_GH_IWriter_SetGuid.htm "SetGuid Method ")

[SetInt32 Method](../html/Overload_GH_IO_Serialization_GH_IWriter_SetInt32.htm "SetInt32 Method ")

[SetInt64 Method](../html/Overload_GH_IO_Serialization_GH_IWriter_SetInt64.htm "SetInt64 Method ")

[SetInterval1D Method](../html/Overload_GH_IO_Serialization_GH_IWriter_SetInterval1D.htm "SetInterval1D Method ")

[SetInterval2D Method](../html/Overload_GH_IO_Serialization_GH_IWriter_SetInterval2D.htm "SetInterval2D Method ")

[SetLine Method](../html/Overload_GH_IO_Serialization_GH_IWriter_SetLine.htm "SetLine Method ")

[SetPath Method](../html/Overload_GH_IO_Serialization_GH_IWriter_SetPath.htm "SetPath Method ")

[SetPlane Method](../html/Overload_GH_IO_Serialization_GH_IWriter_SetPlane.htm "SetPlane Method ")

[SetPoint2D Method](../html/Overload_GH_IO_Serialization_GH_IWriter_SetPoint2D.htm "SetPoint2D Method ")

[SetPoint3D Method](../html/Overload_GH_IO_Serialization_GH_IWriter_SetPoint3D.htm "SetPoint3D Method ")

[SetPoint4D Method](../html/Overload_GH_IO_Serialization_GH_IWriter_SetPoint4D.htm "SetPoint4D Method ")

[SetSingle Method](../html/Overload_GH_IO_Serialization_GH_IWriter_SetSingle.htm "SetSingle Method ")

[SetString Method](../html/Overload_GH_IO_Serialization_GH_IWriter_SetString.htm "SetString Method ")

[SetVersion Method](../html/Overload_GH_IO_Serialization_GH_IWriter_SetVersion.htm "SetVersion Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_IWriterAddLanguageSpecificTextSet("LST78147C7C\_0?cpp=::|nu=.");AddComment Method |

Adds a text comment to this chunk. Comments are serialized only if the output flavour is a
human readable format. Comments are never deserialized, they are purely for the benefit of the
humans reading the file data.

**Namespace:**
 [GH\_IO.Serialization](N_GH_IO_Serialization.htm)  
**Assembly:**
 GH\_IO (in GH\_IO.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
void AddComment(
	string comment_text
)
```

```
Sub AddComment ( 
	comment_text As String
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

comment\_text
:   Type: [SystemAddLanguageSpecificTextSet("LST78147C7C\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");String](https://docs.microsoft.com/dotnet/api/system.string)  
    The content of the comment,
    text might be altered if it contains invalid characters for a chosen format flavour.

![](../icons/SectionExpanded.png)Exceptions

| Exception | Condition |
| --- | --- |
| [ArgumentNullException](https://docs.microsoft.com/dotnet/api/system.argumentnullexception) | Thrown if the content text is either null or empty. |

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_IWriter Interface](T_GH_IO_Serialization_GH_IWriter.htm)

[GH\_IO.Serialization Namespace](N_GH_IO_Serialization.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)