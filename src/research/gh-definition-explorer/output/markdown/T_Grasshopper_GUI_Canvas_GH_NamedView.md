# T_Grasshopper_GUI_Canvas_GH_NamedView

﻿ GH\_NamedView Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI.Canvas](../html/N_Grasshopper_GUI_Canvas.htm "Grasshopper.GUI.Canvas")

[GH\_NamedView Class](../html/T_Grasshopper_GUI_Canvas_GH_NamedView.htm "GH_NamedView Class")

[GH\_NamedView Constructor](../html/Overload_Grasshopper_GUI_Canvas_GH_NamedView__ctor.htm "GH_NamedView Constructor ")

[GH\_NamedView Properties](../html/Properties_T_Grasshopper_GUI_Canvas_GH_NamedView.htm "GH_NamedView Properties")

[GH\_NamedView Methods](../html/Methods_T_Grasshopper_GUI_Canvas_GH_NamedView.htm "GH_NamedView Methods")

[GH\_NamedView Events](../html/Events_T_Grasshopper_GUI_Canvas_GH_NamedView.htm "GH_NamedView Events")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_NamedView Class |

Named views are used both to store named views but also to allow smooth programmatic canvas navigation.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST6A0D7037\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.GUI.CanvasAddLanguageSpecificTextSet("LST6A0D7037\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_NamedView

**Namespace:**
 [Grasshopper.GUI.Canvas](N_Grasshopper_GUI_Canvas.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_NamedView : GH_ISerializable
```

```
Public Class GH_NamedView
	Implements GH_ISerializable
```

AddLanguageTabSet("ID1EBCA");

The GH\_NamedView type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_NamedViewAddLanguageSpecificTextSet("LST6A0D7037\_2?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_GUI_Canvas_GH_NamedView__ctor.htm) | Create a default named view. |
| Public method | [GH\_NamedView(Rectangle, RectangleF)](M_Grasshopper_GUI_Canvas_GH_NamedView__ctor_3.htm) | Create a new view useful for box-fit transitions. |
| Public method | [GH\_NamedView(GH\_Viewport, Point, PointF)](M_Grasshopper_GUI_Canvas_GH_NamedView__ctor_1.htm) | Create a new view useful for point match transitions. |
| Public method | [GH\_NamedView(GH\_Viewport, Rectangle, PointF)](M_Grasshopper_GUI_Canvas_GH_NamedView__ctor_2.htm) | Create a new view useful for point inclusion transitions. |
| Public method | [GH\_NamedView(String, PointF, Single, GH\_NamedViewType)](M_Grasshopper_GUI_Canvas_GH_NamedView__ctor_4.htm) | Create a new named view. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Name](P_Grasshopper_GUI_Canvas_GH_NamedView_Name.htm) | Gets or sets the name of the view. |
| Public property | [Point](P_Grasshopper_GUI_Canvas_GH_NamedView_Point.htm) | Gets or sets the anchor point of the named view. |
| Public property | [Type](P_Grasshopper_GUI_Canvas_GH_NamedView_Type.htm) | Gets or sets a value indicating whether the anchor point represents the target or the center. |
| Public property | [Zoom](P_Grasshopper_GUI_Canvas_GH_NamedView_Zoom.htm) | Gets or sets the zoom factor of the named view. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [LoadFromViewport](M_Grasshopper_GUI_Canvas_GH_NamedView_LoadFromViewport.htm) | Create a named view from a viewport. |
| Public method | [Read](M_Grasshopper_GUI_Canvas_GH_NamedView_Read.htm) |  |
| Public method | [SetToViewport(GH\_Canvas)](M_Grasshopper_GUI_Canvas_GH_NamedView_SetToViewport.htm) | Set the named view to the canvas viewport and redraw the canvas. |
| Public method | [SetToViewport(GH\_Viewport)](M_Grasshopper_GUI_Canvas_GH_NamedView_SetToViewport_2.htm) | Set the named view to a viewport. |
| Public method | [SetToViewport(GH\_Canvas, Int32)](M_Grasshopper_GUI_Canvas_GH_NamedView_SetToViewport_1.htm) | Animates a view transition. |
| Public method | [Write](M_Grasshopper_GUI_Canvas_GH_NamedView_Write.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Events

|  | Name | Description |
| --- | --- | --- |
| Public event | [SmoothFrame](E_Grasshopper_GUI_Canvas_GH_NamedView_SmoothFrame.htm) | This event is raised during smooth animations. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI.Canvas Namespace](N_Grasshopper_GUI_Canvas.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)