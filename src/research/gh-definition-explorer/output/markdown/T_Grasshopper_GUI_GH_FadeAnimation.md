# T_Grasshopper_GUI_GH_FadeAnimation

﻿ GH\_FadeAnimation Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH\_FadeAnimation Class](../html/T_Grasshopper_GUI_GH_FadeAnimation.htm "GH_FadeAnimation Class")

[GH\_FadeAnimation Constructor](../html/Overload_Grasshopper_GUI_GH_FadeAnimation__ctor.htm "GH_FadeAnimation Constructor ")

[GH\_FadeAnimation Properties](../html/Properties_T_Grasshopper_GUI_GH_FadeAnimation.htm "GH_FadeAnimation Properties")

[GH\_FadeAnimation Methods](../html/Methods_T_Grasshopper_GUI_GH_FadeAnimation.htm "GH_FadeAnimation Methods")

[GH\_FadeAnimation Fields](../html/Fields_T_Grasshopper_GUI_GH_FadeAnimation.htm "GH_FadeAnimation Fields")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_FadeAnimation Class |

Utility class for animating fade ZUI events on the canvas.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST378BA4DF\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.GUIAddLanguageSpecificTextSet("LST378BA4DF\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_FadeAnimation

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_FadeAnimation
```

```
Public Class GH_FadeAnimation
```

AddLanguageTabSet("ID1EBCA");

The GH\_FadeAnimation type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_FadeAnimationAddLanguageSpecificTextSet("LST378BA4DF\_2?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_GUI_GH_FadeAnimation__ctor.htm) | Creates a new instance of the Animator class with default settings. |
| Public method | [GH\_FadeAnimation(Single)](M_Grasshopper_GUI_GH_FadeAnimation__ctor_1.htm) | Create a new instance of the Animator class with custom values for zoom threshold. |
| Public method | [GH\_FadeAnimation(Single, Int32)](M_Grasshopper_GUI_GH_FadeAnimation__ctor_2.htm) | Create a new instance of the Animator class with custom values for zoom threshold and duration. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Duration](P_Grasshopper_GUI_GH_FadeAnimation_Duration.htm) | Gets or sets the duration (in milliseconds) for ZUI animations. Negative durations are not allowed. The default is 350 milliseconds. |
| Public property | [FadeAlpha](P_Grasshopper_GUI_GH_FadeAnimation_FadeAlpha.htm) | Gets the blend alpha byte for the current state. 0 means fully hidden, 255 means fully shown. |
| Public property | [FadeFactor](P_Grasshopper_GUI_GH_FadeAnimation_FadeFactor.htm) | Gets the blend factor for the current state. 0.0 means fully hidden, 1.0 means fully shown. |
| Public property | [IsFinished](P_Grasshopper_GUI_GH_FadeAnimation_IsFinished.htm) | Gets a value indicating whether this animator has finished animating. |
| Public property | [Phase](P_Grasshopper_GUI_GH_FadeAnimation_Phase.htm) | Gets the current animation phase. |
| Public property | [Threshold](P_Grasshopper_GUI_GH_FadeAnimation_Threshold.htm) | Gets or sets the threshold value for the fade animation trigger. |
| Public property | [TriggerUpdate](P_Grasshopper_GUI_GH_FadeAnimation_TriggerUpdate.htm) | Gets or sets whether this animator triggers canvas updates. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [Evaluate(GH\_Canvas)](M_Grasshopper_GUI_GH_FadeAnimation_Evaluate.htm) | Reevaluate the fade animation parameters. You should call this method from within the Render method of your attributes. If an animation is currently in progress a redraw of the canvas will be scheduled, whether or not the attributes are actually visible on the canvas. You should therefore only call this method if your attributes are already drawing themselves. |
| Public method | [Evaluate(GH\_Canvas, Boolean)](M_Grasshopper_GUI_GH_FadeAnimation_Evaluate_1.htm) | Reevaluate the fade animation parameters. You should call this method from within the Render method of your attributes. If an animation is currently in progress a redraw of the canvas will be scheduled, whether or not the attributes are actually visible on the canvas. You should therefore only call this method if your attributes are already drawing themselves. |
| Public method | [Evaluate(GH\_Canvas, Single)](M_Grasshopper_GUI_GH_FadeAnimation_Evaluate_2.htm) | Reevaluate the fade animation parameters. You should call this method from within the Render method of your attributes. If an animation is currently in progress a redraw of the canvas will be scheduled, whether or not the attributes are actually visible on the canvas. You should therefore only call this method if your attributes are already drawing themselves. |
| Public method | [Evaluate(GH\_Canvas, Single, Boolean)](M_Grasshopper_GUI_GH_FadeAnimation_Evaluate_3.htm) | Reevaluate the fade animation parameters. You should call this method from within the Render method of your attributes. If an animation is currently in progress a redraw of the canvas will be scheduled, whether or not the attributes are actually visible on the canvas. You should therefore only call this method if your attributes are already drawing themselves. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Fields

|  | Name | Description |
| --- | --- | --- |
| Public fieldStatic member | [Delay](F_Grasshopper_GUI_GH_FadeAnimation_Delay.htm) | Gets the number of milliseconds between redraws (25 milliseconds, resulting in ~40 fps) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)