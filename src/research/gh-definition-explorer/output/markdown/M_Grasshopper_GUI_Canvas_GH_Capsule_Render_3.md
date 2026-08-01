# M_Grasshopper_GUI_Canvas_GH_Capsule_Render_3

﻿ GH\_Capsule.Render Method (Graphics, Image, GH\_PaletteStyle)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI.Canvas](../html/N_Grasshopper_GUI_Canvas.htm "Grasshopper.GUI.Canvas")

[GH\_Capsule Class](../html/T_Grasshopper_GUI_Canvas_GH_Capsule.htm "GH_Capsule Class")

[GH\_Capsule Methods](../html/Methods_T_Grasshopper_GUI_Canvas_GH_Capsule.htm "GH_Capsule Methods")

[Render Method](../html/Overload_Grasshopper_GUI_Canvas_GH_Capsule_Render.htm "Render Method ")

[Render Method (Graphics, GH\_PaletteStyle)](../html/M_Grasshopper_GUI_Canvas_GH_Capsule_Render.htm "Render Method (Graphics, GH_PaletteStyle)")

[Render Method (Graphics, Color)](../html/M_Grasshopper_GUI_Canvas_GH_Capsule_Render_2.htm "Render Method (Graphics, Color)")

[Render Method (Graphics, Image, GH\_PaletteStyle)](../html/M_Grasshopper_GUI_Canvas_GH_Capsule_Render_3.htm "Render Method (Graphics, Image, GH_PaletteStyle)")

[Render Method (Graphics, Image, Color)](../html/M_Grasshopper_GUI_Canvas_GH_Capsule_Render_5.htm "Render Method (Graphics, Image, Color)")

[Render Method (Graphics, Boolean, Boolean, Boolean)](../html/M_Grasshopper_GUI_Canvas_GH_Capsule_Render_1.htm "Render Method (Graphics, Boolean, Boolean, Boolean)")

[Render Method (Graphics, Image, Boolean, Boolean, Boolean)](../html/M_Grasshopper_GUI_Canvas_GH_Capsule_Render_4.htm "Render Method (Graphics, Image, Boolean, Boolean, Boolean)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_CapsuleAddLanguageSpecificTextSet("LST8AE7EE0D\_0?cpp=::|nu=.");Render Method (Graphics, Image, GH\_PaletteStyle) |

Have this capsule draw itself onto a Graphics surface with a custom Style override.

**Namespace:**
 [Grasshopper.GUI.Canvas](N_Grasshopper_GUI_Canvas.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public void Render(
	Graphics G,
	Image icon,
	GH_PaletteStyle style
)
```

```
Public Sub Render ( 
	G As Graphics,
	icon As Image,
	style As GH_PaletteStyle
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

G
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST8AE7EE0D\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Graphics](https://docs.microsoft.com/dotnet/api/system.drawing.graphics)  
    Graphics object to draw with. Zoom factor is implied by the G.Transform property.

icon
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST8AE7EE0D\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Image](https://docs.microsoft.com/dotnet/api/system.drawing.image)  
    Icon to render in center of content/bounding box.

style
:   Type: [Grasshopper.GUI.CanvasAddLanguageSpecificTextSet("LST8AE7EE0D\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_PaletteStyle](T_Grasshopper_GUI_Canvas_GH_PaletteStyle.htm)  
    Style to draw capsule with.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Capsule Class](T_Grasshopper_GUI_Canvas_GH_Capsule.htm)

[Render Overload](Overload_Grasshopper_GUI_Canvas_GH_Capsule_Render.htm)

[Grasshopper.GUI.Canvas Namespace](N_Grasshopper_GUI_Canvas.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)