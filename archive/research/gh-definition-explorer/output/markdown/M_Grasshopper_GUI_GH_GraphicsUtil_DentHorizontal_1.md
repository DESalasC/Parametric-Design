# M_Grasshopper_GUI_GH_GraphicsUtil_DentHorizontal_1

﻿ GH\_GraphicsUtil.DentHorizontal Method (Graphics, Rectangle, Int32, Int32)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH\_GraphicsUtil Class](../html/T_Grasshopper_GUI_GH_GraphicsUtil.htm "GH_GraphicsUtil Class")

[GH\_GraphicsUtil Methods](../html/Methods_T_Grasshopper_GUI_GH_GraphicsUtil.htm "GH_GraphicsUtil Methods")

[DentHorizontal Method](../html/Overload_Grasshopper_GUI_GH_GraphicsUtil_DentHorizontal.htm "DentHorizontal Method ")

[DentHorizontal Method (Graphics, Rectangle)](../html/M_Grasshopper_GUI_GH_GraphicsUtil_DentHorizontal.htm "DentHorizontal Method (Graphics, Rectangle)")

[DentHorizontal Method (Graphics, Rectangle, Int32, Int32)](../html/M_Grasshopper_GUI_GH_GraphicsUtil_DentHorizontal_1.htm "DentHorizontal Method (Graphics, Rectangle, Int32, Int32)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_GraphicsUtilAddLanguageSpecificTextSet("LSTE7816B93\_0?cpp=::|nu=.");DentHorizontal Method (Graphics, Rectangle, Int32, Int32) |

Draws a horizontal dent. A horizontal dent had dark lines along the top and bottom edges.

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static void DentHorizontal(
	Graphics g,
	Rectangle box,
	int alphaEdge,
	int alphaFill
)
```

```
Public Shared Sub DentHorizontal ( 
	g As Graphics,
	box As Rectangle,
	alphaEdge As Integer,
	alphaFill As Integer
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

g
:   Type: [System.DrawingAddLanguageSpecificTextSet("LSTE7816B93\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Graphics](https://docs.microsoft.com/dotnet/api/system.drawing.graphics)  
    Graphics object to draw with.

box
:   Type: [System.DrawingAddLanguageSpecificTextSet("LSTE7816B93\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Rectangle](https://docs.microsoft.com/dotnet/api/system.drawing.rectangle)  
    Dimensions of the dent.

alphaEdge
:   Type: [SystemAddLanguageSpecificTextSet("LSTE7816B93\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Transparency on the middle of the edges.

alphaFill
:   Type: [SystemAddLanguageSpecificTextSet("LSTE7816B93\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Transparency on the middle of the fill.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_GraphicsUtil Class](T_Grasshopper_GUI_GH_GraphicsUtil.htm)

[DentHorizontal Overload](Overload_Grasshopper_GUI_GH_GraphicsUtil_DentHorizontal.htm)

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)