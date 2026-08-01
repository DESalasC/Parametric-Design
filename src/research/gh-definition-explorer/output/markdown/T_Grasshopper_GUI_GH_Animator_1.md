# T_Grasshopper_GUI_GH_Animator_1

﻿ GH\_Animator(T) Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH\_Animator(T) Class](../html/T_Grasshopper_GUI_GH_Animator_1.htm "GH_Animator(T) Class")

[GH\_Animator(T) Constructor](../html/Overload_Grasshopper_GUI_GH_Animator_1__ctor.htm "GH_Animator(T) Constructor ")

[GH\_Animator(T) Properties](../html/Properties_T_Grasshopper_GUI_GH_Animator_1.htm "GH_Animator(T) Properties")

[GH\_Animator(T) Methods](../html/Methods_T_Grasshopper_GUI_GH_Animator_1.htm "GH_Animator(T) Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_AnimatorAddLanguageSpecificTextSet("LSTD3336D34\_0?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTD3336D34\_1?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)"); Class |

Provides methods for animating values.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LSTD3336D34\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.GUIAddLanguageSpecificTextSet("LSTD3336D34\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_AnimatorAddLanguageSpecificTextSet("LSTD3336D34\_4?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTD3336D34\_5?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_Animator<T>
```

```
Public Class GH_Animator(Of T)
```

AddLanguageTabSet("ID1EBCA");

#### Type Parameters

T
:   Data type to animate.

The GH\_AnimatorAddLanguageSpecificTextSet("LSTD3336D34\_6?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTD3336D34\_7?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;"); type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_AnimatorAddLanguageSpecificTextSet("LSTD3336D34\_8?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTD3336D34\_9?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");(T, T, TimeSpan, GH\_AnimatorAddLanguageSpecificTextSet("LSTD3336D34\_10?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTD3336D34\_11?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");AddLanguageSpecificTextSet("LSTD3336D34\_12?cs=.|vb=.|cpp=::|nu=.|fs=.");Interpolate)](M_Grasshopper_GUI_GH_Animator_1__ctor_1.htm) | Create a new instance of the generic animator. |
| Public method | [GH\_AnimatorAddLanguageSpecificTextSet("LSTD3336D34\_13?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTD3336D34\_14?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");(T, T, DateTime, DateTime, GH\_AnimatorAddLanguageSpecificTextSet("LSTD3336D34\_15?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTD3336D34\_16?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");AddLanguageSpecificTextSet("LSTD3336D34\_17?cs=.|vb=.|cpp=::|nu=.|fs=.");Interpolate)](M_Grasshopper_GUI_GH_Animator_1__ctor.htm) | Create a new instance of the generic animator. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Interpolation](P_Grasshopper_GUI_GH_Animator_1_Interpolation.htm) | Gets or sets the interpolation mode. Changing the mode during an animation will result in discontinuous motion. |
| Public property | [Phase](P_Grasshopper_GUI_GH_Animator_1_Phase.htm) | Gets the current animation phase. |
| Public property | [ValueA](P_Grasshopper_GUI_GH_Animator_1_ValueA.htm) | Gets or sets the start value of the animation. This value is set from within the constructor though you can change it at any time. |
| Public property | [ValueB](P_Grasshopper_GUI_GH_Animator_1_ValueB.htm) | Gets or sets the end value of the animation. This value is set from within the constructor though you can change it at any time. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [AdjustAnimation(T)](M_Grasshopper_GUI_GH_Animator_1_AdjustAnimation.htm) | Adjust the animation. |
| Public method | [AdjustAnimation(T, Int32)](M_Grasshopper_GUI_GH_Animator_1_AdjustAnimation_2.htm) | Adjust the animation. |
| Public method | [AdjustAnimation(T, DateTime, DateTime)](M_Grasshopper_GUI_GH_Animator_1_AdjustAnimation_1.htm) | Adjust the animation. |
| Public method | [CurrentValue](M_Grasshopper_GUI_GH_Animator_1_CurrentValue.htm) | Gets the current animated value. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)