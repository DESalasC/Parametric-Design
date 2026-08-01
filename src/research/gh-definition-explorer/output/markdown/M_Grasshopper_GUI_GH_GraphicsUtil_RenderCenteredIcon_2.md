# M_Grasshopper_GUI_GH_GraphicsUtil_RenderCenteredIcon_2

﻿ GH\_GraphicsUtil.RenderCenteredIcon Method (Graphics, RectangleF, Image, Single)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH\_GraphicsUtil Class](../html/T_Grasshopper_GUI_GH_GraphicsUtil.htm "GH_GraphicsUtil Class")

[GH\_GraphicsUtil Methods](../html/Methods_T_Grasshopper_GUI_GH_GraphicsUtil.htm "GH_GraphicsUtil Methods")

[RenderCenteredIcon Method](../html/Overload_Grasshopper_GUI_GH_GraphicsUtil_RenderCenteredIcon.htm "RenderCenteredIcon Method ")

[RenderCenteredIcon Method (Graphics, RectangleF, Image)](../html/M_Grasshopper_GUI_GH_GraphicsUtil_RenderCenteredIcon.htm "RenderCenteredIcon Method (Graphics, RectangleF, Image)")

[RenderCenteredIcon Method (Graphics, RectangleF, Image, Double)](../html/M_Grasshopper_GUI_GH_GraphicsUtil_RenderCenteredIcon_1.htm "RenderCenteredIcon Method (Graphics, RectangleF, Image, Double)")

[RenderCenteredIcon Method (Graphics, RectangleF, Image, Single)](../html/M_Grasshopper_GUI_GH_GraphicsUtil_RenderCenteredIcon_2.htm "RenderCenteredIcon Method (Graphics, RectangleF, Image, Single)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_GraphicsUtilAddLanguageSpecificTextSet("LST898297B0\_0?cpp=::|nu=.");RenderCenteredIcon Method (Graphics, RectangleF, Image, Single) |

**Note: This API is now obsolete.**

Draw an icon centered in a frame. This code is not zoom-aware, but it will
perform consistent rounding (to avoid pixel-jitter when moving the frame across the screen).
Icon will not be clipped to the frame.

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
[ObsoleteAttribute("This method is obsolete, use a RenderIcon() overload instead.")]
public static void RenderCenteredIcon(
	Graphics g,
	RectangleF frame,
	Image icon,
	float scale
)
```

```
<ObsoleteAttribute("This method is obsolete, use a RenderIcon() overload instead.")>
Public Shared Sub RenderCenteredIcon ( 
	g As Graphics,
	frame As RectangleF,
	icon As Image,
	scale As Single
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

g
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST898297B0\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Graphics](https://docs.microsoft.com/dotnet/api/system.drawing.graphics)  
    Graphics object to render with.

frame
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST898297B0\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");RectangleF](https://docs.microsoft.com/dotnet/api/system.drawing.rectanglef)  
    Frame to center icon in.

icon
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST898297B0\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Image](https://docs.microsoft.com/dotnet/api/system.drawing.image)  
    Icon to render

scale
:   Type: [SystemAddLanguageSpecificTextSet("LST898297B0\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");Single](https://docs.microsoft.com/dotnet/api/system.single)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_GraphicsUtil Class](T_Grasshopper_GUI_GH_GraphicsUtil.htm)

[RenderCenteredIcon Overload](Overload_Grasshopper_GUI_GH_GraphicsUtil_RenderCenteredIcon.htm)

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)