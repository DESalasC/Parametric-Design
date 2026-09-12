# M_Grasshopper_GUI_Canvas_GH_Viewport_IsVisible_1

﻿ GH\_Viewport.IsVisible Method (RectangleF, Single)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI.Canvas](../html/N_Grasshopper_GUI_Canvas.htm "Grasshopper.GUI.Canvas")

[GH\_Viewport Class](../html/T_Grasshopper_GUI_Canvas_GH_Viewport.htm "GH_Viewport Class")

[GH\_Viewport Methods](../html/Methods_T_Grasshopper_GUI_Canvas_GH_Viewport.htm "GH_Viewport Methods")

[IsVisible Method](../html/Overload_Grasshopper_GUI_Canvas_GH_Viewport_IsVisible.htm "IsVisible Method ")

[IsVisible Method (PointF, Single)](../html/M_Grasshopper_GUI_Canvas_GH_Viewport_IsVisible.htm "IsVisible Method (PointF, Single)")

[IsVisible Method (RectangleF, Single)](../html/M_Grasshopper_GUI_Canvas_GH_Viewport_IsVisible_1.htm "IsVisible Method (RectangleF, Single)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ViewportAddLanguageSpecificTextSet("LST4AED6B4B\_0?cpp=::|nu=.");IsVisible Method (RectangleFAddLanguageSpecificTextSet("LST4AED6B4B\_1?cpp=%");, Single) |

Test visibility of a rectangle.

**Namespace:**
 [Grasshopper.GUI.Canvas](N_Grasshopper_GUI_Canvas.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public bool IsVisible(
	ref RectangleF rec,
	float margin = 0f
)
```

```
Public Function IsVisible ( 
	ByRef rec As RectangleF,
	Optional margin As Single = 0F
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

rec
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST4AED6B4B\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");RectangleF](https://docs.microsoft.com/dotnet/api/system.drawing.rectanglef)AddLanguageSpecificTextSet("LST4AED6B4B\_3?cpp=%");  
    Rectangle in canvas coordinates.

margin (Optional)
:   Type: [SystemAddLanguageSpecificTextSet("LST4AED6B4B\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");Single](https://docs.microsoft.com/dotnet/api/system.single)  
    Fuzzy area around rectangle to test.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True if the rectangle is visible in the control upon projection.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Viewport Class](T_Grasshopper_GUI_Canvas_GH_Viewport.htm)

[IsVisible Overload](Overload_Grasshopper_GUI_Canvas_GH_Viewport_IsVisible.htm)

[Grasshopper.GUI.Canvas Namespace](N_Grasshopper_GUI_Canvas.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)