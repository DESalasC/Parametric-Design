# M_Grasshopper_GUI_Canvas_GH_Painter_DrawConnection

﻿ GH\_Painter.DrawConnection Method 

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
| GH\_PainterAddLanguageSpecificTextSet("LSTC6FFC3B1\_0?cpp=::|nu=.");DrawConnection Method |

**Namespace:**
 [Grasshopper.GUI.Canvas](N_Grasshopper_GUI_Canvas.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public void DrawConnection(
	PointF pointA,
	PointF pointB,
	GH_WireDirection directionA,
	GH_WireDirection directionB,
	bool selectedA,
	bool selectedB,
	GH_WireType type
)
```

```
Public Sub DrawConnection ( 
	pointA As PointF,
	pointB As PointF,
	directionA As GH_WireDirection,
	directionB As GH_WireDirection,
	selectedA As Boolean,
	selectedB As Boolean,
	type As GH_WireType
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

pointA
:   Type: [System.DrawingAddLanguageSpecificTextSet("LSTC6FFC3B1\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");PointF](https://docs.microsoft.com/dotnet/api/system.drawing.pointf)

pointB
:   Type: [System.DrawingAddLanguageSpecificTextSet("LSTC6FFC3B1\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");PointF](https://docs.microsoft.com/dotnet/api/system.drawing.pointf)

directionA
:   Type: [Grasshopper.GUI.CanvasAddLanguageSpecificTextSet("LSTC6FFC3B1\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_WireDirection](T_Grasshopper_GUI_Canvas_GH_WireDirection.htm)

directionB
:   Type: [Grasshopper.GUI.CanvasAddLanguageSpecificTextSet("LSTC6FFC3B1\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_WireDirection](T_Grasshopper_GUI_Canvas_GH_WireDirection.htm)

selectedA
:   Type: [SystemAddLanguageSpecificTextSet("LSTC6FFC3B1\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)

selectedB
:   Type: [SystemAddLanguageSpecificTextSet("LSTC6FFC3B1\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)

type
:   Type: [Grasshopper.GUI.CanvasAddLanguageSpecificTextSet("LSTC6FFC3B1\_7?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_WireType](T_Grasshopper_GUI_Canvas_GH_WireType.htm)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Painter Class](T_Grasshopper_GUI_Canvas_GH_Painter.htm)

[Grasshopper.GUI.Canvas Namespace](N_Grasshopper_GUI_Canvas.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)