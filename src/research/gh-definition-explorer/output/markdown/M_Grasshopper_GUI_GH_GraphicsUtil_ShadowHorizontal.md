# M_Grasshopper_GUI_GH_GraphicsUtil_ShadowHorizontal

﻿ GH\_GraphicsUtil.ShadowHorizontal Method (Graphics, Int32, Int32, Int32, Int32, Boolean, Color)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH\_GraphicsUtil Class](../html/T_Grasshopper_GUI_GH_GraphicsUtil.htm "GH_GraphicsUtil Class")

[GH\_GraphicsUtil Methods](../html/Methods_T_Grasshopper_GUI_GH_GraphicsUtil.htm "GH_GraphicsUtil Methods")

[ShadowHorizontal Method](../html/Overload_Grasshopper_GUI_GH_GraphicsUtil_ShadowHorizontal.htm "ShadowHorizontal Method ")

[ShadowHorizontal Method (Graphics, Int32, Int32, Int32, Int32, Boolean, Color)](../html/M_Grasshopper_GUI_GH_GraphicsUtil_ShadowHorizontal.htm "ShadowHorizontal Method (Graphics, Int32, Int32, Int32, Int32, Boolean, Color)")

[ShadowHorizontal Method (Graphics, Int32, Int32, Int32, Int32, Boolean, Int32)](../html/M_Grasshopper_GUI_GH_GraphicsUtil_ShadowHorizontal_1.htm "ShadowHorizontal Method (Graphics, Int32, Int32, Int32, Int32, Boolean, Int32)")

[ShadowHorizontal Method (Graphics, Single, Single, Single, Single, Boolean, Int32)](../html/M_Grasshopper_GUI_GH_GraphicsUtil_ShadowHorizontal_2.htm "ShadowHorizontal Method (Graphics, Single, Single, Single, Single, Boolean, Int32)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_GraphicsUtilAddLanguageSpecificTextSet("LSTD390E272\_0?cpp=::|nu=.");ShadowHorizontal Method (Graphics, Int32, Int32, Int32, Int32, Boolean, Color) |

Draws a horizontal shadow edge.

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static void ShadowHorizontal(
	Graphics g,
	int x0,
	int x1,
	int y,
	int size,
	bool below,
	Color color
)
```

```
Public Shared Sub ShadowHorizontal ( 
	g As Graphics,
	x0 As Integer,
	x1 As Integer,
	y As Integer,
	size As Integer,
	below As Boolean,
	color As Color
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

g
:   Type: [System.DrawingAddLanguageSpecificTextSet("LSTD390E272\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Graphics](https://docs.microsoft.com/dotnet/api/system.drawing.graphics)  
    Graphics object to draw with.

x0
:   Type: [SystemAddLanguageSpecificTextSet("LSTD390E272\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Start of shadow edge.

x1
:   Type: [SystemAddLanguageSpecificTextSet("LSTD390E272\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    End of shadow edge.

y
:   Type: [SystemAddLanguageSpecificTextSet("LSTD390E272\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Elevation of shadow edge.

size
:   Type: [SystemAddLanguageSpecificTextSet("LSTD390E272\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Length of cast shadow.

below
:   Type: [SystemAddLanguageSpecificTextSet("LSTD390E272\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
    If true, shadow is drawn below elevation line.

color
:   Type: [System.DrawingAddLanguageSpecificTextSet("LSTD390E272\_7?cs=.|vb=.|cpp=::|nu=.|fs=.");Color](https://docs.microsoft.com/dotnet/api/system.drawing.color)  
    Colour at shadow edge.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_GraphicsUtil Class](T_Grasshopper_GUI_GH_GraphicsUtil.htm)

[ShadowHorizontal Overload](Overload_Grasshopper_GUI_GH_GraphicsUtil_ShadowHorizontal.htm)

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)