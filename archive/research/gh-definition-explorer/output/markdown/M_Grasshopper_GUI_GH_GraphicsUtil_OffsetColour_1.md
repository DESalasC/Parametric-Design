# M_Grasshopper_GUI_GH_GraphicsUtil_OffsetColour_1

﻿ GH\_GraphicsUtil.OffsetColour Method (Color, Int32, Int32, Int32)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH\_GraphicsUtil Class](../html/T_Grasshopper_GUI_GH_GraphicsUtil.htm "GH_GraphicsUtil Class")

[GH\_GraphicsUtil Methods](../html/Methods_T_Grasshopper_GUI_GH_GraphicsUtil.htm "GH_GraphicsUtil Methods")

[OffsetColour Method](../html/Overload_Grasshopper_GUI_GH_GraphicsUtil_OffsetColour.htm "OffsetColour Method ")

[OffsetColour Method (Color, Int32)](../html/M_Grasshopper_GUI_GH_GraphicsUtil_OffsetColour.htm "OffsetColour Method (Color, Int32)")

[OffsetColour Method (Color, Int32, Int32, Int32)](../html/M_Grasshopper_GUI_GH_GraphicsUtil_OffsetColour_1.htm "OffsetColour Method (Color, Int32, Int32, Int32)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_GraphicsUtilAddLanguageSpecificTextSet("LST7FEA62D1\_0?cpp=::|nu=.");OffsetColour Method (Color, Int32, Int32, Int32) |

Add a fixed value to all the channels in a colour.

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static Color OffsetColour(
	Color col,
	int redShift,
	int greenShift,
	int blueShift
)
```

```
Public Shared Function OffsetColour ( 
	col As Color,
	redShift As Integer,
	greenShift As Integer,
	blueShift As Integer
) As Color
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

col
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST7FEA62D1\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Color](https://docs.microsoft.com/dotnet/api/system.drawing.color)  
    The colour to mutate

redShift
:   Type: [SystemAddLanguageSpecificTextSet("LST7FEA62D1\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Offset value for red channel (-255 ~ +255).

greenShift
:   Type: [SystemAddLanguageSpecificTextSet("LST7FEA62D1\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Offset value for green channel (-255 ~ +255).

blueShift
:   Type: [SystemAddLanguageSpecificTextSet("LST7FEA62D1\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Offset value for blue channel (-255 ~ +255).

#### Return Value

Type: [Color](https://docs.microsoft.com/dotnet/api/system.drawing.color)  
The offsetted colour.

![](../icons/SectionExpanded.png)Remarks

The alpha channel of the colour is not offset.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_GraphicsUtil Class](T_Grasshopper_GUI_GH_GraphicsUtil.htm)

[OffsetColour Overload](Overload_Grasshopper_GUI_GH_GraphicsUtil_OffsetColour.htm)

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)