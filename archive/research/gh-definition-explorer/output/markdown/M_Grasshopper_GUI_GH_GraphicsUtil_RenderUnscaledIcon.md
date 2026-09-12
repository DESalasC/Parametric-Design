# M_Grasshopper_GUI_GH_GraphicsUtil_RenderUnscaledIcon

﻿ GH\_GraphicsUtil.RenderUnscaledIcon Method (Graphics, Image, Int32, Int32)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH\_GraphicsUtil Class](../html/T_Grasshopper_GUI_GH_GraphicsUtil.htm "GH_GraphicsUtil Class")

[GH\_GraphicsUtil Methods](../html/Methods_T_Grasshopper_GUI_GH_GraphicsUtil.htm "GH_GraphicsUtil Methods")

[RenderUnscaledIcon Method](../html/Overload_Grasshopper_GUI_GH_GraphicsUtil_RenderUnscaledIcon.htm "RenderUnscaledIcon Method ")

[RenderUnscaledIcon Method (Graphics, Image, Int32, Int32)](../html/M_Grasshopper_GUI_GH_GraphicsUtil_RenderUnscaledIcon.htm "RenderUnscaledIcon Method (Graphics, Image, Int32, Int32)")

[RenderUnscaledIcon Method (Graphics, Image, Int32, Int32, Double)](../html/M_Grasshopper_GUI_GH_GraphicsUtil_RenderUnscaledIcon_1.htm "RenderUnscaledIcon Method (Graphics, Image, Int32, Int32, Double)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_GraphicsUtilAddLanguageSpecificTextSet("LST56342439\_0?cpp=::|nu=.");RenderUnscaledIcon Method (Graphics, Image, Int32, Int32) |

**Note: This API is now obsolete.**

Draws an image file at 1:1 scale centered on the given coordinates.

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
public static void RenderUnscaledIcon(
	Graphics g,
	Image icon,
	int cx,
	int cy
)
```

```
<ObsoleteAttribute("This method is obsolete, use a RenderIcon() overload instead.")>
Public Shared Sub RenderUnscaledIcon ( 
	g As Graphics,
	icon As Image,
	cx As Integer,
	cy As Integer
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

g
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST56342439\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Graphics](https://docs.microsoft.com/dotnet/api/system.drawing.graphics)  
    Graphics object to draw with.

icon
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST56342439\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Image](https://docs.microsoft.com/dotnet/api/system.drawing.image)  
    Image to draw.

cx
:   Type: [SystemAddLanguageSpecificTextSet("LST56342439\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    X center of image in Graphics coordinate.

cy
:   Type: [SystemAddLanguageSpecificTextSet("LST56342439\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Y center of image in Graphics coordinate.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_GraphicsUtil Class](T_Grasshopper_GUI_GH_GraphicsUtil.htm)

[RenderUnscaledIcon Overload](Overload_Grasshopper_GUI_GH_GraphicsUtil_RenderUnscaledIcon.htm)

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)