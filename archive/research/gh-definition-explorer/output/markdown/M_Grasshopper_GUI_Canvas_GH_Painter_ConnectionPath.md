# M_Grasshopper_GUI_Canvas_GH_Painter_ConnectionPath

﻿ GH\_Painter.ConnectionPath Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI.Canvas](../html/N_Grasshopper_GUI_Canvas.htm "Grasshopper.GUI.Canvas")

[GH\_Painter Class](../html/T_Grasshopper_GUI_Canvas_GH_Painter.htm "GH_Painter Class")

[GH\_Painter Methods](../html/Methods_T_Grasshopper_GUI_Canvas_GH_Painter.htm "GH_Painter Methods")

[ConnectionPath Method](../html/M_Grasshopper_GUI_Canvas_GH_Painter_ConnectionPath.htm "ConnectionPath Method ")

[ConnectionPathBezier Method](../html/M_Grasshopper_GUI_Canvas_GH_Painter_ConnectionPathBezier.htm "ConnectionPathBezier Method ")

[ConnectionVisible Method](../html/M_Grasshopper_GUI_Canvas_GH_Painter_ConnectionVisible.htm "ConnectionVisible Method ")

[DetermineWireType Method](../html/M_Grasshopper_GUI_Canvas_GH_Painter_DetermineWireType.htm "DetermineWireType Method ")

[DrawBackground Method](../html/M_Grasshopper_GUI_Canvas_GH_Painter_DrawBackground.htm "DrawBackground Method ")

[DrawConnection Method](../html/M_Grasshopper_GUI_Canvas_GH_Painter_DrawConnection.htm "DrawConnection Method ")

[DrawMiddleGround Method](../html/M_Grasshopper_GUI_Canvas_GH_Painter_DrawMiddleGround.htm "DrawMiddleGround Method ")

[DrawNoDocumentMessage Method](../html/M_Grasshopper_GUI_Canvas_GH_Painter_DrawNoDocumentMessage.htm "DrawNoDocumentMessage Method ")

[DrawNULLBuffer Method](../html/M_Grasshopper_GUI_Canvas_GH_Painter_DrawNULLBuffer.htm "DrawNULLBuffer Method ")

[DrawPivots Method](../html/M_Grasshopper_GUI_Canvas_GH_Painter_DrawPivots.htm "DrawPivots Method ")

[DrawRecipientLinks Method](../html/Overload_Grasshopper_GUI_Canvas_GH_Painter_DrawRecipientLinks.htm "DrawRecipientLinks Method ")

[DrawStateFlags Method](../html/M_Grasshopper_GUI_Canvas_GH_Painter_DrawStateFlags.htm "DrawStateFlags Method ")

[GenerateWirePen\_Fill Method](../html/M_Grasshopper_GUI_Canvas_GH_Painter_GenerateWirePen_Fill.htm "GenerateWirePen_Fill Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_PainterAddLanguageSpecificTextSet("LST22CD191E\_0?cpp=::|nu=.");ConnectionPath Method |

**Namespace:**
 [Grasshopper.GUI.Canvas](N_Grasshopper_GUI_Canvas.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static GraphicsPath ConnectionPath(
	PointF pointA,
	PointF pointB,
	GH_WireDirection directionA,
	GH_WireDirection directionB
)
```

```
Public Shared Function ConnectionPath ( 
	pointA As PointF,
	pointB As PointF,
	directionA As GH_WireDirection,
	directionB As GH_WireDirection
) As GraphicsPath
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

pointA
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST22CD191E\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");PointF](https://docs.microsoft.com/dotnet/api/system.drawing.pointf)

pointB
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST22CD191E\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");PointF](https://docs.microsoft.com/dotnet/api/system.drawing.pointf)

directionA
:   Type: [Grasshopper.GUI.CanvasAddLanguageSpecificTextSet("LST22CD191E\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_WireDirection](T_Grasshopper_GUI_Canvas_GH_WireDirection.htm)

directionB
:   Type: [Grasshopper.GUI.CanvasAddLanguageSpecificTextSet("LST22CD191E\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_WireDirection](T_Grasshopper_GUI_Canvas_GH_WireDirection.htm)

#### Return Value

Type: [GraphicsPath](https://docs.microsoft.com/dotnet/api/system.drawing.drawing2d.graphicspath)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Painter Class](T_Grasshopper_GUI_Canvas_GH_Painter.htm)

[Grasshopper.GUI.Canvas Namespace](N_Grasshopper_GUI_Canvas.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)