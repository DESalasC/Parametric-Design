# M_Grasshopper_GUI_GH_GraphicsUtil_ShadowVertical

﻿ GH\_GraphicsUtil.ShadowVertical Method (Graphics, Int32, Int32, Int32, Int32, Boolean, Color)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH\_GraphicsUtil Class](../html/T_Grasshopper_GUI_GH_GraphicsUtil.htm "GH_GraphicsUtil Class")

[GH\_GraphicsUtil Methods](../html/Methods_T_Grasshopper_GUI_GH_GraphicsUtil.htm "GH_GraphicsUtil Methods")

[ShadowVertical Method](../html/Overload_Grasshopper_GUI_GH_GraphicsUtil_ShadowVertical.htm "ShadowVertical Method ")

[ShadowVertical Method (Graphics, Int32, Int32, Int32, Int32, Boolean, Color)](../html/M_Grasshopper_GUI_GH_GraphicsUtil_ShadowVertical.htm "ShadowVertical Method (Graphics, Int32, Int32, Int32, Int32, Boolean, Color)")

[ShadowVertical Method (Graphics, Int32, Int32, Int32, Int32, Boolean, Int32)](../html/M_Grasshopper_GUI_GH_GraphicsUtil_ShadowVertical_1.htm "ShadowVertical Method (Graphics, Int32, Int32, Int32, Int32, Boolean, Int32)")

[ShadowVertical Method (Graphics, Single, Single, Single, Single, Boolean, Int32)](../html/M_Grasshopper_GUI_GH_GraphicsUtil_ShadowVertical_2.htm "ShadowVertical Method (Graphics, Single, Single, Single, Single, Boolean, Int32)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_GraphicsUtilAddLanguageSpecificTextSet("LSTB5D3D7FC\_0?cpp=::|nu=.");ShadowVertical Method (Graphics, Int32, Int32, Int32, Int32, Boolean, Color) |

Draws a vertical shadow edge.

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static void ShadowVertical(
	Graphics g,
	int x,
	int y0,
	int y1,
	int size,
	bool right,
	Color color
)
```

```
Public Shared Sub ShadowVertical ( 
	g As Graphics,
	x As Integer,
	y0 As Integer,
	y1 As Integer,
	size As Integer,
	right As Boolean,
	color As Color
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

g
:   Type: [System.DrawingAddLanguageSpecificTextSet("LSTB5D3D7FC\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Graphics](https://docs.microsoft.com/dotnet/api/system.drawing.graphics)  
    Graphics object to draw with.

x
:   Type: [SystemAddLanguageSpecificTextSet("LSTB5D3D7FC\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Offset of shadow edge.

y0
:   Type: [SystemAddLanguageSpecificTextSet("LSTB5D3D7FC\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Start of shadow edge.

y1
:   Type: [SystemAddLanguageSpecificTextSet("LSTB5D3D7FC\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    End of shadow edge.

size
:   Type: [SystemAddLanguageSpecificTextSet("LSTB5D3D7FC\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Length of cast shadow.

right
:   Type: [SystemAddLanguageSpecificTextSet("LSTB5D3D7FC\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
    If true, shadow is drawn to the right of the elevated line.

color
:   Type: [System.DrawingAddLanguageSpecificTextSet("LSTB5D3D7FC\_7?cs=.|vb=.|cpp=::|nu=.|fs=.");Color](https://docs.microsoft.com/dotnet/api/system.drawing.color)  
    Color at shadow edge.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_GraphicsUtil Class](T_Grasshopper_GUI_GH_GraphicsUtil.htm)

[ShadowVertical Overload](Overload_Grasshopper_GUI_GH_GraphicsUtil_ShadowVertical.htm)

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)