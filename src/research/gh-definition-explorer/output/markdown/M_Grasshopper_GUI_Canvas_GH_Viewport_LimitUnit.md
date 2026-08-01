# M_Grasshopper_GUI_Canvas_GH_Viewport_LimitUnit

﻿ GH\_Viewport.LimitUnit Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI.Canvas](../html/N_Grasshopper_GUI_Canvas.htm "Grasshopper.GUI.Canvas")

[GH\_Viewport Class](../html/T_Grasshopper_GUI_Canvas_GH_Viewport.htm "GH_Viewport Class")

[GH\_Viewport Methods](../html/Methods_T_Grasshopper_GUI_Canvas_GH_Viewport.htm "GH_Viewport Methods")

[ApplyProjection Method](../html/M_Grasshopper_GUI_Canvas_GH_Viewport_ApplyProjection.htm "ApplyProjection Method ")

[ComputeProjection Method](../html/M_Grasshopper_GUI_Canvas_GH_Viewport_ComputeProjection.htm "ComputeProjection Method ")

[DollyZoom Method](../html/M_Grasshopper_GUI_Canvas_GH_Viewport_DollyZoom.htm "DollyZoom Method ")

[Duplicate Method](../html/M_Grasshopper_GUI_Canvas_GH_Viewport_Duplicate.htm "Duplicate Method ")

[Focus Method](../html/Overload_Grasshopper_GUI_Canvas_GH_Viewport_Focus.htm "Focus Method ")

[IsVisible Method](../html/Overload_Grasshopper_GUI_Canvas_GH_Viewport_IsVisible.htm "IsVisible Method ")

[LimitUnit Method](../html/M_Grasshopper_GUI_Canvas_GH_Viewport_LimitUnit.htm "LimitUnit Method ")

[Project Method](../html/M_Grasshopper_GUI_Canvas_GH_Viewport_Project.htm "Project Method ")

[ProjectPoint Method](../html/M_Grasshopper_GUI_Canvas_GH_Viewport_ProjectPoint.htm "ProjectPoint Method ")

[ProjectRectangle Method](../html/M_Grasshopper_GUI_Canvas_GH_Viewport_ProjectRectangle.htm "ProjectRectangle Method ")

[ProjectX Method](../html/M_Grasshopper_GUI_Canvas_GH_Viewport_ProjectX.htm "ProjectX Method ")

[ProjectY Method](../html/M_Grasshopper_GUI_Canvas_GH_Viewport_ProjectY.htm "ProjectY Method ")

[Set Method](../html/M_Grasshopper_GUI_Canvas_GH_Viewport_Set.htm "Set Method ")

[SolveUnit Method](../html/M_Grasshopper_GUI_Canvas_GH_Viewport_SolveUnit.htm "SolveUnit Method ")

[Unproject Method](../html/M_Grasshopper_GUI_Canvas_GH_Viewport_Unproject.htm "Unproject Method ")

[UnprojectPoint Method](../html/M_Grasshopper_GUI_Canvas_GH_Viewport_UnprojectPoint.htm "UnprojectPoint Method ")

[UnprojectRectangle Method](../html/M_Grasshopper_GUI_Canvas_GH_Viewport_UnprojectRectangle.htm "UnprojectRectangle Method ")

[UnprojectX Method](../html/M_Grasshopper_GUI_Canvas_GH_Viewport_UnprojectX.htm "UnprojectX Method ")

[UnprojectY Method](../html/M_Grasshopper_GUI_Canvas_GH_Viewport_UnprojectY.htm "UnprojectY Method ")

[XFormMatrix Method](../html/M_Grasshopper_GUI_Canvas_GH_Viewport_XFormMatrix.htm "XFormMatrix Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ViewportAddLanguageSpecificTextSet("LST8AEF6F00\_0?cpp=::|nu=.");LimitUnit Method |

Utility function for calculating pixel dimensions in a zoom-aware environment.
The desired value is put through the zoom projection and if the resulting
size (as displayed on the screen) exceeds the visual limits it is clipped.
This function can be used for example to make sure that a certain penwidth
never exceeds visual limits (i.e. it doesn't get too thin or too thick on the screen).

**Namespace:**
 [Grasshopper.GUI.Canvas](N_Grasshopper_GUI_Canvas.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public float LimitUnit(
	float guide_value,
	float no_less_than = -3.402823E+38f,
	float no_more_than = 3.402823E+38f
)
```

```
Public Function LimitUnit ( 
	guide_value As Single,
	Optional no_less_than As Single = -3.402823E+38F,
	Optional no_more_than As Single = 3.402823E+38F
) As Single
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

guide\_value
:   Type: [SystemAddLanguageSpecificTextSet("LST8AEF6F00\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Single](https://docs.microsoft.com/dotnet/api/system.single)  
    Initial value.

no\_less\_than (Optional)
:   Type: [SystemAddLanguageSpecificTextSet("LST8AEF6F00\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Single](https://docs.microsoft.com/dotnet/api/system.single)  
    Minimum allowed visible size on screen.

no\_more\_than (Optional)
:   Type: [SystemAddLanguageSpecificTextSet("LST8AEF6F00\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");Single](https://docs.microsoft.com/dotnet/api/system.single)  
    Maximum allowed visible size on screen.

#### Return Value

Type: [Single](https://docs.microsoft.com/dotnet/api/system.single)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Viewport Class](T_Grasshopper_GUI_Canvas_GH_Viewport.htm)

[Grasshopper.GUI.Canvas Namespace](N_Grasshopper_GUI_Canvas.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)