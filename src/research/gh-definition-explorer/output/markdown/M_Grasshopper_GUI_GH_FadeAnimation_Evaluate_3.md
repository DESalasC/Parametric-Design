# M_Grasshopper_GUI_GH_FadeAnimation_Evaluate_3

﻿ GH\_FadeAnimation.Evaluate Method (GH\_Canvas, Single, Boolean)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH\_FadeAnimation Class](../html/T_Grasshopper_GUI_GH_FadeAnimation.htm "GH_FadeAnimation Class")

[GH\_FadeAnimation Methods](../html/Methods_T_Grasshopper_GUI_GH_FadeAnimation.htm "GH_FadeAnimation Methods")

[Evaluate Method](../html/Overload_Grasshopper_GUI_GH_FadeAnimation_Evaluate.htm "Evaluate Method ")

[Evaluate Method (GH\_Canvas)](../html/M_Grasshopper_GUI_GH_FadeAnimation_Evaluate.htm "Evaluate Method (GH_Canvas)")

[Evaluate Method (GH\_Canvas, Boolean)](../html/M_Grasshopper_GUI_GH_FadeAnimation_Evaluate_1.htm "Evaluate Method (GH_Canvas, Boolean)")

[Evaluate Method (GH\_Canvas, Single)](../html/M_Grasshopper_GUI_GH_FadeAnimation_Evaluate_2.htm "Evaluate Method (GH_Canvas, Single)")

[Evaluate Method (GH\_Canvas, Single, Boolean)](../html/M_Grasshopper_GUI_GH_FadeAnimation_Evaluate_3.htm "Evaluate Method (GH_Canvas, Single, Boolean)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_FadeAnimationAddLanguageSpecificTextSet("LST7B98F7BB\_0?cpp=::|nu=.");Evaluate Method (GH\_Canvas, Single, Boolean) |

Reevaluate the fade animation parameters. You should call this
method from within the Render method of your attributes. If an animation
is currently in progress a redraw of the canvas will be scheduled, whether
or not the attributes are actually visible on the canvas. You should therefore
only call this method if your attributes are already drawing themselves.

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public void Evaluate(
	GH_Canvas canvas,
	float value,
	bool scheduleRedraw
)
```

```
Public Sub Evaluate ( 
	canvas As GH_Canvas,
	value As Single,
	scheduleRedraw As Boolean
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

canvas
:   Type: [Grasshopper.GUI.CanvasAddLanguageSpecificTextSet("LST7B98F7BB\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Canvas](T_Grasshopper_GUI_Canvas_GH_Canvas.htm)  
    Canvas currently drawing in.

value
:   Type: [SystemAddLanguageSpecificTextSet("LST7B98F7BB\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Single](https://docs.microsoft.com/dotnet/api/system.single)

scheduleRedraw
:   Type: [SystemAddLanguageSpecificTextSet("LST7B98F7BB\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
    If true and the animator is active, a redraw will be scheduled.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_FadeAnimation Class](T_Grasshopper_GUI_GH_FadeAnimation.htm)

[Evaluate Overload](Overload_Grasshopper_GUI_GH_FadeAnimation_Evaluate.htm)

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)