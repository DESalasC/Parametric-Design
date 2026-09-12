# M_Grasshopper_GUI_Canvas_GH_ResizeBorder_Solve

﻿ GH\_ResizeBorder.Solve Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI.Canvas](../html/N_Grasshopper_GUI_Canvas.htm "Grasshopper.GUI.Canvas")

[GH\_ResizeBorder Class](../html/T_Grasshopper_GUI_Canvas_GH_ResizeBorder.htm "GH_ResizeBorder Class")

[GH\_ResizeBorder Methods](../html/Methods_T_Grasshopper_GUI_Canvas_GH_ResizeBorder.htm "GH_ResizeBorder Methods")

[Setup Method](../html/Overload_Grasshopper_GUI_Canvas_GH_ResizeBorder_Setup.htm "Setup Method ")

[Solve Method](../html/M_Grasshopper_GUI_Canvas_GH_ResizeBorder_Solve.htm "Solve Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ResizeBorderAddLanguageSpecificTextSet("LSTAA59D06B\_0?cpp=::|nu=.");Solve Method |

Solve a resizing step.

**Namespace:**
 [Grasshopper.GUI.Canvas](N_Grasshopper_GUI_Canvas.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public void Solve(
	PointF nCursor,
	out RectangleF new_shape,
	out PointF new_pivot
)
```

```
Public Sub Solve ( 
	nCursor As PointF,
	<OutAttribute> ByRef new_shape As RectangleF,
	<OutAttribute> ByRef new_pivot As PointF
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

nCursor
:   Type: [System.DrawingAddLanguageSpecificTextSet("LSTAA59D06B\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");PointF](https://docs.microsoft.com/dotnet/api/system.drawing.pointf)  
    The new cursor location.

new\_shape
:   Type: [System.DrawingAddLanguageSpecificTextSet("LSTAA59D06B\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");RectangleF](https://docs.microsoft.com/dotnet/api/system.drawing.rectanglef)AddLanguageSpecificTextSet("LSTAA59D06B\_3?cpp=%");  
    The resized shape bounding box.

new\_pivot
:   Type: [System.DrawingAddLanguageSpecificTextSet("LSTAA59D06B\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");PointF](https://docs.microsoft.com/dotnet/api/system.drawing.pointf)AddLanguageSpecificTextSet("LSTAA59D06B\_5?cpp=%");  
    The adjusted shape pivot.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_ResizeBorder Class](T_Grasshopper_GUI_Canvas_GH_ResizeBorder.htm)

[Grasshopper.GUI.Canvas Namespace](N_Grasshopper_GUI_Canvas.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)