# M_Grasshopper_GUI_GH_GraphicsUtil_EtchVertical_1

﻿ GH\_GraphicsUtil.EtchVertical Method (Graphics, Single, Single, Single, Int32)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH\_GraphicsUtil Class](../html/T_Grasshopper_GUI_GH_GraphicsUtil.htm "GH_GraphicsUtil Class")

[GH\_GraphicsUtil Methods](../html/Methods_T_Grasshopper_GUI_GH_GraphicsUtil.htm "GH_GraphicsUtil Methods")

[EtchVertical Method](../html/Overload_Grasshopper_GUI_GH_GraphicsUtil_EtchVertical.htm "EtchVertical Method ")

[EtchVertical Method (Graphics, Int32, Int32, Int32, Int32)](../html/M_Grasshopper_GUI_GH_GraphicsUtil_EtchVertical.htm "EtchVertical Method (Graphics, Int32, Int32, Int32, Int32)")

[EtchVertical Method (Graphics, Single, Single, Single, Int32)](../html/M_Grasshopper_GUI_GH_GraphicsUtil_EtchVertical_1.htm "EtchVertical Method (Graphics, Single, Single, Single, Int32)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_GraphicsUtilAddLanguageSpecificTextSet("LST7A85B16C\_0?cpp=::|nu=.");EtchVertical Method (Graphics, Single, Single, Single, Int32) |

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
public static void EtchVertical(
	Graphics g,
	float x,
	float y0,
	float y1,
	int alpha = 50
)
```

```
Public Shared Sub EtchVertical ( 
	g As Graphics,
	x As Single,
	y0 As Single,
	y1 As Single,
	Optional alpha As Integer = 50
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

g
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST7A85B16C\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Graphics](https://docs.microsoft.com/dotnet/api/system.drawing.graphics)  
    Graphics object to draw with.

x
:   Type: [SystemAddLanguageSpecificTextSet("LST7A85B16C\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Single](https://docs.microsoft.com/dotnet/api/system.single)  
    x component of line segment.

y0
:   Type: [SystemAddLanguageSpecificTextSet("LST7A85B16C\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Single](https://docs.microsoft.com/dotnet/api/system.single)  
    x component of start point.

y1
:   Type: [SystemAddLanguageSpecificTextSet("LST7A85B16C\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");Single](https://docs.microsoft.com/dotnet/api/system.single)  
    y component of end point.

alpha (Optional)
:   Type: [SystemAddLanguageSpecificTextSet("LST7A85B16C\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Alpha level of etched line.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_GraphicsUtil Class](T_Grasshopper_GUI_GH_GraphicsUtil.htm)

[EtchVertical Overload](Overload_Grasshopper_GUI_GH_GraphicsUtil_EtchVertical.htm)

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)