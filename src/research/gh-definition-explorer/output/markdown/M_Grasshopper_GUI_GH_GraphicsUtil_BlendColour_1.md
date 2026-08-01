# M_Grasshopper_GUI_GH_GraphicsUtil_BlendColour_1

﻿ GH\_GraphicsUtil.BlendColour Method (Color, Color, Double)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH\_GraphicsUtil Class](../html/T_Grasshopper_GUI_GH_GraphicsUtil.htm "GH_GraphicsUtil Class")

[GH\_GraphicsUtil Methods](../html/Methods_T_Grasshopper_GUI_GH_GraphicsUtil.htm "GH_GraphicsUtil Methods")

[BlendColour Method](../html/Overload_Grasshopper_GUI_GH_GraphicsUtil_BlendColour.htm "BlendColour Method ")

[BlendColour Method (Color, Color)](../html/M_Grasshopper_GUI_GH_GraphicsUtil_BlendColour.htm "BlendColour Method (Color, Color)")

[BlendColour Method (Color, Color, Double)](../html/M_Grasshopper_GUI_GH_GraphicsUtil_BlendColour_1.htm "BlendColour Method (Color, Color, Double)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_GraphicsUtilAddLanguageSpecificTextSet("LST3439970A\_0?cpp=::|nu=.");BlendColour Method (Color, Color, Double) |

Overlays two colours.

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static Color BlendColour(
	Color bottom,
	Color top,
	double factor
)
```

```
Public Shared Function BlendColour ( 
	bottom As Color,
	top As Color,
	factor As Double
) As Color
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

bottom
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST3439970A\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Color](https://docs.microsoft.com/dotnet/api/system.drawing.color)  
    Base colour.

top
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST3439970A\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Color](https://docs.microsoft.com/dotnet/api/system.drawing.color)  
    Overlay colour.

factor
:   Type: [SystemAddLanguageSpecificTextSet("LST3439970A\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Double](https://docs.microsoft.com/dotnet/api/system.double)  
    Blend factor. 0.0 means the return colour will be identical to the bottom colour,
    1.0 means the return colour will be identical to the top colour.

#### Return Value

Type: [Color](https://docs.microsoft.com/dotnet/api/system.drawing.color)  
The blended colour.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_GraphicsUtil Class](T_Grasshopper_GUI_GH_GraphicsUtil.htm)

[BlendColour Overload](Overload_Grasshopper_GUI_GH_GraphicsUtil_BlendColour.htm)

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)