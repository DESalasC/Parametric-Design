# M_Grasshopper_GUI_GH_GraphicsUtil_EtchHorizontal

﻿ GH\_GraphicsUtil.EtchHorizontal Method (Graphics, Int32, Int32, Int32, Int32, Int32)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH\_GraphicsUtil Class](../html/T_Grasshopper_GUI_GH_GraphicsUtil.htm "GH_GraphicsUtil Class")

[GH\_GraphicsUtil Methods](../html/Methods_T_Grasshopper_GUI_GH_GraphicsUtil.htm "GH_GraphicsUtil Methods")

[EtchHorizontal Method](../html/Overload_Grasshopper_GUI_GH_GraphicsUtil_EtchHorizontal.htm "EtchHorizontal Method ")

[EtchHorizontal Method (Graphics, Single, Single, Single, Int32)](../html/M_Grasshopper_GUI_GH_GraphicsUtil_EtchHorizontal_1.htm "EtchHorizontal Method (Graphics, Single, Single, Single, Int32)")

[EtchHorizontal Method (Graphics, Int32, Int32, Int32, Int32, Int32)](../html/M_Grasshopper_GUI_GH_GraphicsUtil_EtchHorizontal.htm "EtchHorizontal Method (Graphics, Int32, Int32, Int32, Int32, Int32)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_GraphicsUtilAddLanguageSpecificTextSet("LST580B571C\_0?cpp=::|nu=.");EtchHorizontal Method (Graphics, Int32, Int32, Int32, Int32, Int32) |

Draws an etched line segment.

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static void EtchHorizontal(
	Graphics g,
	int x0,
	int x1,
	int y,
	int alphaLight = 200,
	int alphaDark = 35
)
```

```
Public Shared Sub EtchHorizontal ( 
	g As Graphics,
	x0 As Integer,
	x1 As Integer,
	y As Integer,
	Optional alphaLight As Integer = 200,
	Optional alphaDark As Integer = 35
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

g
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST580B571C\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Graphics](https://docs.microsoft.com/dotnet/api/system.drawing.graphics)  
    Graphics object to draw with.

x0
:   Type: [SystemAddLanguageSpecificTextSet("LST580B571C\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    x component of start point.

x1
:   Type: [SystemAddLanguageSpecificTextSet("LST580B571C\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    x component of end point.

y
:   Type: [SystemAddLanguageSpecificTextSet("LST580B571C\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    y component of line segment.

alphaLight (Optional)
:   Type: [SystemAddLanguageSpecificTextSet("LST580B571C\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Alpha level of etched lit line.

alphaDark (Optional)
:   Type: [SystemAddLanguageSpecificTextSet("LST580B571C\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Alpha level of etched shadow line.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_GraphicsUtil Class](T_Grasshopper_GUI_GH_GraphicsUtil.htm)

[EtchHorizontal Overload](Overload_Grasshopper_GUI_GH_GraphicsUtil_EtchHorizontal.htm)

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)