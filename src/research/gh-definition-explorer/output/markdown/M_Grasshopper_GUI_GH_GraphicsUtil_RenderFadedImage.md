# M_Grasshopper_GUI_GH_GraphicsUtil_RenderFadedImage

﻿ GH\_GraphicsUtil.RenderFadedImage Method (Graphics, Image, Rectangle, Double)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH\_GraphicsUtil Class](../html/T_Grasshopper_GUI_GH_GraphicsUtil.htm "GH_GraphicsUtil Class")

[GH\_GraphicsUtil Methods](../html/Methods_T_Grasshopper_GUI_GH_GraphicsUtil.htm "GH_GraphicsUtil Methods")

[RenderFadedImage Method](../html/Overload_Grasshopper_GUI_GH_GraphicsUtil_RenderFadedImage.htm "RenderFadedImage Method ")

[RenderFadedImage Method (Graphics, Image, Rectangle, Double)](../html/M_Grasshopper_GUI_GH_GraphicsUtil_RenderFadedImage.htm "RenderFadedImage Method (Graphics, Image, Rectangle, Double)")

[RenderFadedImage Method (Graphics, Image, Rectangle, Int32)](../html/M_Grasshopper_GUI_GH_GraphicsUtil_RenderFadedImage_1.htm "RenderFadedImage Method (Graphics, Image, Rectangle, Int32)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_GraphicsUtilAddLanguageSpecificTextSet("LSTBCC08AAE\_0?cpp=::|nu=.");RenderFadedImage Method (Graphics, Image, Rectangle, Double) |

Render an icon into a rectangle with a specific fading factor.

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static void RenderFadedImage(
	Graphics graphics,
	Image image,
	Rectangle destination,
	double fade
)
```

```
Public Shared Sub RenderFadedImage ( 
	graphics As Graphics,
	image As Image,
	destination As Rectangle,
	fade As Double
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

graphics
:   Type: [System.DrawingAddLanguageSpecificTextSet("LSTBCC08AAE\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Graphics](https://docs.microsoft.com/dotnet/api/system.drawing.graphics)  
    Graphics object to draw with.

image
:   Type: [System.DrawingAddLanguageSpecificTextSet("LSTBCC08AAE\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Image](https://docs.microsoft.com/dotnet/api/system.drawing.image)  
    Image to draw.

destination
:   Type: [System.DrawingAddLanguageSpecificTextSet("LSTBCC08AAE\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Rectangle](https://docs.microsoft.com/dotnet/api/system.drawing.rectangle)  
    Destination rectangle.

fade
:   Type: [SystemAddLanguageSpecificTextSet("LSTBCC08AAE\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");Double](https://docs.microsoft.com/dotnet/api/system.double)  
    Fading amount. 0.0=completely transparent, 1.0=original transparency.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_GraphicsUtil Class](T_Grasshopper_GUI_GH_GraphicsUtil.htm)

[RenderFadedImage Overload](Overload_Grasshopper_GUI_GH_GraphicsUtil_RenderFadedImage.htm)

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)