# M_Grasshopper_GUI_GH_GraphicsUtil_RenderColourIcon_1

﻿ GH\_GraphicsUtil.RenderColourIcon Method (Graphics, Rectangle, Color, Single)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH\_GraphicsUtil Class](../html/T_Grasshopper_GUI_GH_GraphicsUtil.htm "GH_GraphicsUtil Class")

[GH\_GraphicsUtil Methods](../html/Methods_T_Grasshopper_GUI_GH_GraphicsUtil.htm "GH_GraphicsUtil Methods")

[RenderColourIcon Method](../html/Overload_Grasshopper_GUI_GH_GraphicsUtil_RenderColourIcon.htm "RenderColourIcon Method ")

[RenderColourIcon Method (Graphics, Rectangle, Color)](../html/M_Grasshopper_GUI_GH_GraphicsUtil_RenderColourIcon.htm "RenderColourIcon Method (Graphics, Rectangle, Color)")

[RenderColourIcon Method (Graphics, Rectangle, Color, Single)](../html/M_Grasshopper_GUI_GH_GraphicsUtil_RenderColourIcon_1.htm "RenderColourIcon Method (Graphics, Rectangle, Color, Single)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_GraphicsUtilAddLanguageSpecificTextSet("LST3987E1BB\_0?cpp=::|nu=.");RenderColourIcon Method (Graphics, Rectangle, Color, Single) |

Render a colour icon into a graphics context. A colour icon contains a black outer and white inner edge.

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static void RenderColourIcon(
	Graphics g,
	Rectangle rec,
	Color colour,
	float scale
)
```

```
Public Shared Sub RenderColourIcon ( 
	g As Graphics,
	rec As Rectangle,
	colour As Color,
	scale As Single
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

g
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST3987E1BB\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Graphics](https://docs.microsoft.com/dotnet/api/system.drawing.graphics)  
    Graphics object to draw with.

rec
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST3987E1BB\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Rectangle](https://docs.microsoft.com/dotnet/api/system.drawing.rectangle)  
    Rectangle describing icon dimensions.

colour
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST3987E1BB\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Color](https://docs.microsoft.com/dotnet/api/system.drawing.color)  
    Colour for icon.

scale
:   Type: [SystemAddLanguageSpecificTextSet("LST3987E1BB\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");Single](https://docs.microsoft.com/dotnet/api/system.single)  
    Scale adjustment.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_GraphicsUtil Class](T_Grasshopper_GUI_GH_GraphicsUtil.htm)

[RenderColourIcon Overload](Overload_Grasshopper_GUI_GH_GraphicsUtil_RenderColourIcon.htm)

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)