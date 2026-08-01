# M_Grasshopper_GUI_GH_GraphicsUtil_RenderFadedImage_1

﻿ GH\_GraphicsUtil.RenderFadedImage Method (Graphics, Image, Rectangle, Int32)

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
| GH\_GraphicsUtilAddLanguageSpecificTextSet("LST74FE90B0\_0?cpp=::|nu=.");RenderFadedImage Method (Graphics, Image, Rectangle, Int32) |

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
	int alpha
)
```

```
Public Shared Sub RenderFadedImage ( 
	graphics As Graphics,
	image As Image,
	destination As Rectangle,
	alpha As Integer
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

graphics
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST74FE90B0\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Graphics](https://docs.microsoft.com/dotnet/api/system.drawing.graphics)  
    Graphics object to draw with.

image
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST74FE90B0\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Image](https://docs.microsoft.com/dotnet/api/system.drawing.image)  
    Image to draw.

destination
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST74FE90B0\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Rectangle](https://docs.microsoft.com/dotnet/api/system.drawing.rectangle)  
    Destination rectangle.

alpha
:   Type: [SystemAddLanguageSpecificTextSet("LST74FE90B0\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Alpha value. 0=completely transparent, 255=original transparency.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_GraphicsUtil Class](T_Grasshopper_GUI_GH_GraphicsUtil.htm)

[RenderFadedImage Overload](Overload_Grasshopper_GUI_GH_GraphicsUtil_RenderFadedImage.htm)

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)