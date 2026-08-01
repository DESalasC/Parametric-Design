# M_Grasshopper_GUI_GH_Animator_1__ctor

﻿ GH\_Animator(T) Constructor (T, T, DateTime, DateTime, GH\_Animator(T).Interpolate)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH\_Animator(T) Class](../html/T_Grasshopper_GUI_GH_Animator_1.htm "GH_Animator(T) Class")

[GH\_Animator(T) Constructor](../html/Overload_Grasshopper_GUI_GH_Animator_1__ctor.htm "GH_Animator(T) Constructor ")

[GH\_Animator(T) Constructor (T, T, TimeSpan, GH\_Animator(T).Interpolate)](../html/M_Grasshopper_GUI_GH_Animator_1__ctor_1.htm "GH_Animator(T) Constructor (T, T, TimeSpan, GH_Animator(T).Interpolate)")

[GH\_Animator(T) Constructor (T, T, DateTime, DateTime, GH\_Animator(T).Interpolate)](../html/M_Grasshopper_GUI_GH_Animator_1__ctor.htm "GH_Animator(T) Constructor (T, T, DateTime, DateTime, GH_Animator(T).Interpolate)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_AnimatorAddLanguageSpecificTextSet("LSTF82E3BA9\_0?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTF82E3BA9\_1?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)"); Constructor (T, T, DateTime, DateTime, GH\_AnimatorAddLanguageSpecificTextSet("LSTF82E3BA9\_2?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");TAddLanguageSpecificTextSet("LSTF82E3BA9\_3?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");AddLanguageSpecificTextSet("LSTF82E3BA9\_4?cpp=::|nu=.");Interpolate) |

Create a new instance of the generic animator.

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public GH_Animator(
	T A,
	T B,
	DateTime startTime,
	DateTime endTime,
	GH_AnimatorAddLanguageSpecificTextSet("LSTF82E3BA9_5?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTF82E3BA9_6?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTF82E3BA9_7?cs=.|vb=.|cpp=::|nu=.|fs=.");Interpolate interpolator
)
```

```
Public Sub New ( 
	A As T,
	B As T,
	startTime As DateTime,
	endTime As DateTime,
	interpolator As GH_AnimatorAddLanguageSpecificTextSet("LSTF82E3BA9_8?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTF82E3BA9_9?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTF82E3BA9_10?cs=.|vb=.|cpp=::|nu=.|fs=.");Interpolate
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

A
:   Type: [T](T_Grasshopper_GUI_GH_Animator_1.htm)  
    Start value of animation.

B
:   Type: [T](T_Grasshopper_GUI_GH_Animator_1.htm)  
    End value of animation.

startTime
:   Type: [SystemAddLanguageSpecificTextSet("LSTF82E3BA9\_11?cs=.|vb=.|cpp=::|nu=.|fs=.");DateTime](https://docs.microsoft.com/dotnet/api/system.datetime)  
    Start of animation, should be expressed in UTC time.

endTime
:   Type: [SystemAddLanguageSpecificTextSet("LSTF82E3BA9\_12?cs=.|vb=.|cpp=::|nu=.|fs=.");DateTime](https://docs.microsoft.com/dotnet/api/system.datetime)  
    End of animation, should be expressed in UTC time.

interpolator
:   Type: [Grasshopper.GUIAddLanguageSpecificTextSet("LSTF82E3BA9\_13?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_AnimatorAddLanguageSpecificTextSet("LSTF82E3BA9\_14?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTF82E3BA9\_15?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;");AddLanguageSpecificTextSet("LSTF82E3BA9\_16?cs=.|vb=.|cpp=::|nu=.|fs=.");Interpolate](T_Grasshopper_GUI_GH_Animator_1_Interpolate.htm)  
    Interpolation delegate.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_AnimatorAddLanguageSpecificTextSet("LSTF82E3BA9\_17?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTF82E3BA9\_18?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;"); Class](T_Grasshopper_GUI_GH_Animator_1.htm)

[GH\_AnimatorAddLanguageSpecificTextSet("LSTF82E3BA9\_19?cs=&lt;|vb=(Of |cpp=&lt;|nu=(|fs=&lt;'");TAddLanguageSpecificTextSet("LSTF82E3BA9\_20?cs=&gt;|vb=)|cpp=&gt;|nu=)|fs=&gt;"); Overload](Overload_Grasshopper_GUI_GH_Animator_1__ctor.htm)

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)