# M_Grasshopper_GUI_Canvas_GH_PaletteStyle_CreateBrush

﻿ GH\_PaletteStyle.CreateBrush Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI.Canvas](../html/N_Grasshopper_GUI_Canvas.htm "Grasshopper.GUI.Canvas")

[GH\_PaletteStyle Class](../html/T_Grasshopper_GUI_Canvas_GH_PaletteStyle.htm "GH_PaletteStyle Class")

[GH\_PaletteStyle Methods](../html/Methods_T_Grasshopper_GUI_Canvas_GH_PaletteStyle.htm "GH_PaletteStyle Methods")

[CreateBrush Method](../html/M_Grasshopper_GUI_Canvas_GH_PaletteStyle_CreateBrush.htm "CreateBrush Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_PaletteStyleAddLanguageSpecificTextSet("LST5578384C\_0?cpp=::|nu=.");CreateBrush Method |

Create a fill brush. At low zoom levels the brush will be solid colour,
at medium to high zoom levels the brush will have a gradient.

**Namespace:**
 [Grasshopper.GUI.Canvas](N_Grasshopper_GUI_Canvas.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public virtual Brush CreateBrush(
	RectangleF rec,
	float zoom
)
```

```
Public Overridable Function CreateBrush ( 
	rec As RectangleF,
	zoom As Single
) As Brush
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

rec
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST5578384C\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");RectangleF](https://docs.microsoft.com/dotnet/api/system.drawing.rectanglef)  
    Target rectangle of fill brush.

zoom
:   Type: [SystemAddLanguageSpecificTextSet("LST5578384C\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Single](https://docs.microsoft.com/dotnet/api/system.single)  
    Zoom level of target graphics surface.

#### Return Value

Type: [Brush](https://docs.microsoft.com/dotnet/api/system.drawing.brush)  
A brush object that can be used to fill a custom area.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_PaletteStyle Class](T_Grasshopper_GUI_Canvas_GH_PaletteStyle.htm)

[Grasshopper.GUI.Canvas Namespace](N_Grasshopper_GUI_Canvas.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)