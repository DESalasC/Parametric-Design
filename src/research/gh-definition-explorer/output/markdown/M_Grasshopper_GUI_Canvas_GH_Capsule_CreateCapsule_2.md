# M_Grasshopper_GUI_Canvas_GH_Capsule_CreateCapsule_2

﻿ GH\_Capsule.CreateCapsule Method (Rectangle, GH\_Palette, Int32[], Int32)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI.Canvas](../html/N_Grasshopper_GUI_Canvas.htm "Grasshopper.GUI.Canvas")

[GH\_Capsule Class](../html/T_Grasshopper_GUI_Canvas_GH_Capsule.htm "GH_Capsule Class")

[GH\_Capsule Methods](../html/Methods_T_Grasshopper_GUI_Canvas_GH_Capsule.htm "GH_Capsule Methods")

[CreateCapsule Method](../html/Overload_Grasshopper_GUI_Canvas_GH_Capsule_CreateCapsule.htm "CreateCapsule Method ")

[CreateCapsule Method (Rectangle, GH\_Palette)](../html/M_Grasshopper_GUI_Canvas_GH_Capsule_CreateCapsule.htm "CreateCapsule Method (Rectangle, GH_Palette)")

[CreateCapsule Method (RectangleF, GH\_Palette)](../html/M_Grasshopper_GUI_Canvas_GH_Capsule_CreateCapsule_3.htm "CreateCapsule Method (RectangleF, GH_Palette)")

[CreateCapsule Method (Rectangle, GH\_Palette, Int32, Int32)](../html/M_Grasshopper_GUI_Canvas_GH_Capsule_CreateCapsule_1.htm "CreateCapsule Method (Rectangle, GH_Palette, Int32, Int32)")

[CreateCapsule Method (Rectangle, GH\_Palette, Int32[], Int32)](../html/M_Grasshopper_GUI_Canvas_GH_Capsule_CreateCapsule_2.htm "CreateCapsule Method (Rectangle, GH_Palette, Int32[], Int32)")

[CreateCapsule Method (RectangleF, GH\_Palette, Int32, Int32)](../html/M_Grasshopper_GUI_Canvas_GH_Capsule_CreateCapsule_4.htm "CreateCapsule Method (RectangleF, GH_Palette, Int32, Int32)")

[CreateCapsule Method (RectangleF, GH\_Palette, Int32[], Int32)](../html/M_Grasshopper_GUI_Canvas_GH_Capsule_CreateCapsule_5.htm "CreateCapsule Method (RectangleF, GH_Palette, Int32[], Int32)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_CapsuleAddLanguageSpecificTextSet("LST3CBF1F67\_0?cpp=::|nu=.");CreateCapsule Method (Rectangle, GH\_Palette, AddLanguageSpecificTextSet("LST3CBF1F67\_1?cpp=array&lt;");Int32AddLanguageSpecificTextSet("LST3CBF1F67\_2?cpp=&gt;|vb=()|nu=[]");, Int32) |

Create a new blank capsule.

**Namespace:**
 [Grasshopper.GUI.Canvas](N_Grasshopper_GUI_Canvas.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static GH_Capsule CreateCapsule(
	Rectangle box,
	GH_Palette palette,
	int[] radii,
	int highlight
)
```

```
Public Shared Function CreateCapsule ( 
	box As Rectangle,
	palette As GH_Palette,
	radii As Integer(),
	highlight As Integer
) As GH_Capsule
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

box
:   Type: [System.DrawingAddLanguageSpecificTextSet("LST3CBF1F67\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Rectangle](https://docs.microsoft.com/dotnet/api/system.drawing.rectangle)  
    Box for capsule dimensions. The box will be grown until it is at least 3 pixels wide and high.

palette
:   Type: [Grasshopper.GUI.CanvasAddLanguageSpecificTextSet("LST3CBF1F67\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Palette](T_Grasshopper_GUI_Canvas_GH_Palette.htm)  
    Colour palette to apply.

radii
:   Type: AddLanguageSpecificTextSet("LST3CBF1F67\_5?cpp=array&lt;");[SystemAddLanguageSpecificTextSet("LST3CBF1F67\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)AddLanguageSpecificTextSet("LST3CBF1F67\_7?cpp=&gt;|vb=()|nu=[]");  
    Radii of rounded corners. This array must contain at least 4 integers.
    Radii are defined clockwise, starting at the upper left corner.

highlight
:   Type: [SystemAddLanguageSpecificTextSet("LST3CBF1F67\_8?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Height of the highlight bar. A value of zero or lower disables the highlight.

#### Return Value

Type: [GH\_Capsule](T_Grasshopper_GUI_Canvas_GH_Capsule.htm)  
A new instance of GH\_Capsule. Caller is responsible for disposing of the object.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Capsule Class](T_Grasshopper_GUI_Canvas_GH_Capsule.htm)

[CreateCapsule Overload](Overload_Grasshopper_GUI_Canvas_GH_Capsule_CreateCapsule.htm)

[Grasshopper.GUI.Canvas Namespace](N_Grasshopper_GUI_Canvas.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)