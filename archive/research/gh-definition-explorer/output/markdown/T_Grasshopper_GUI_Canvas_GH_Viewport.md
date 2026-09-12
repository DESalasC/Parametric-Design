# T_Grasshopper_GUI_Canvas_GH_Viewport

﻿ GH\_Viewport Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI.Canvas](../html/N_Grasshopper_GUI_Canvas.htm "Grasshopper.GUI.Canvas")

[GH\_Viewport Class](../html/T_Grasshopper_GUI_Canvas_GH_Viewport.htm "GH_Viewport Class")

[GH\_Viewport Constructor](../html/Overload_Grasshopper_GUI_Canvas_GH_Viewport__ctor.htm "GH_Viewport Constructor ")

[GH\_Viewport Properties](../html/Properties_T_Grasshopper_GUI_Canvas_GH_Viewport.htm "GH_Viewport Properties")

[GH\_Viewport Methods](../html/Methods_T_Grasshopper_GUI_Canvas_GH_Viewport.htm "GH_Viewport Methods")

[GH\_Viewport Fields](../html/Fields_T_Grasshopper_GUI_Canvas_GH_Viewport.htm "GH_Viewport Fields")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_Viewport Class |

Provides functionality for panning and zooming in a GH\_Canvas environment.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LSTF4F5122\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.GUI.CanvasAddLanguageSpecificTextSet("LSTF4F5122\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Viewport

**Namespace:**
 [Grasshopper.GUI.Canvas](N_Grasshopper_GUI_Canvas.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public sealed class GH_Viewport
```

```
Public NotInheritable Class GH_Viewport
```

AddLanguageTabSet("ID1EBCA");

The GH\_Viewport type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_ViewportAddLanguageSpecificTextSet("LSTF4F5122\_2?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_GUI_Canvas_GH_Viewport__ctor.htm) | Initializes a new instance of the GH\_Viewport class |
| Public method | [GH\_Viewport(GH\_Viewport)](M_Grasshopper_GUI_Canvas_GH_Viewport__ctor_1.htm) | Initializes a new instance of the GH\_Viewport class |
| Public method | [GH\_Viewport(Point)](M_Grasshopper_GUI_Canvas_GH_Viewport__ctor_2.htm) | Initializes a new instance of the GH\_Viewport class |
| Public method | [GH\_Viewport(Point, Single)](M_Grasshopper_GUI_Canvas_GH_Viewport__ctor_3.htm) | Initializes a new instance of the GH\_Viewport class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [ControlMidPoint](P_Grasshopper_GUI_Canvas_GH_Viewport_ControlMidPoint.htm) | Gets the point in the exact center of the viewport in control coordinates. |
| Public property | [Diagonal](P_Grasshopper_GUI_Canvas_GH_Viewport_Diagonal.htm) | Gets the length of the diagonal of the viewport in canvas coordinates. |
| Public property | [Height](P_Grasshopper_GUI_Canvas_GH_Viewport_Height.htm) | Gets or sets the height of the viewport. Typically this is tied to the dimensions of the canvas. Height is not allowed to go below 5 pixels. |
| Public property | [MidPoint](P_Grasshopper_GUI_Canvas_GH_Viewport_MidPoint.htm) | Gets or sets the canvas coordinate that is directly underneath the center of the viewport. |
| Public property | [ScreenPort](P_Grasshopper_GUI_Canvas_GH_Viewport_ScreenPort.htm) | Gets the dimensions of the viewport in control coordinates. |
| Public property | [Size](P_Grasshopper_GUI_Canvas_GH_Viewport_Size.htm) | Gets or sets the size of the viewport. The size is typically tied to the dimensions of the Canvas. |
| Public property | [Target](P_Grasshopper_GUI_Canvas_GH_Viewport_Target.htm) | Gets or sets the location of the target pixel. The target represents where the canvas origin is drawn. |
| Public property | [TargetRatio](P_Grasshopper_GUI_Canvas_GH_Viewport_TargetRatio.htm) | Gets or sets the target ratio with respect to the viewport dimensions. This is a useful tool to prevent weird view changes during a canvas resize. |
| Public property | [Tx](P_Grasshopper_GUI_Canvas_GH_Viewport_Tx.htm) | Gets or sets the x-component of the target pixel. The target represents where the canvas origin is drawn. |
| Public property | [Ty](P_Grasshopper_GUI_Canvas_GH_Viewport_Ty.htm) | Gets or sets the y-component of the target pixel. The target represents where the canvas origin is drawn. |
| Public property | [VisibleRegion](P_Grasshopper_GUI_Canvas_GH_Viewport_VisibleRegion.htm) | Gets the rectangle in canvas coordinates that is visible in the control. |
| Public property | [Width](P_Grasshopper_GUI_Canvas_GH_Viewport_Width.htm) | Gets or sets the width of the viewport. Typically this is tied to the dimensions of the canvas. Width is not allowed to go below 5 pixels. |
| Public property | [Zoom](P_Grasshopper_GUI_Canvas_GH_Viewport_Zoom.htm) | Gets or sets the Zoom factor of the viewport. Please assign only sensible values. |
| Public property | [ZoomAddLanguageSpecificTextSet("LSTF4F5122\_3?cs=[|vb=(|cpp=[|nu=(|fs= ");BooleanAddLanguageSpecificTextSet("LSTF4F5122\_4?cs=]|vb=)|cpp=]|nu=)|fs= ");](P_Grasshopper_GUI_Canvas_GH_Viewport_Zoom_1.htm) | Sets the zoom of the viewport with a view anchor. |
| Public property | [ZoomInverse](P_Grasshopper_GUI_Canvas_GH_Viewport_ZoomInverse.htm) | Gets the inverse of the zoom. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [ApplyProjection](M_Grasshopper_GUI_Canvas_GH_Viewport_ApplyProjection.htm) | Apply the current display transformation to a Graphics object. |
| Public method | [ComputeProjection](M_Grasshopper_GUI_Canvas_GH_Viewport_ComputeProjection.htm) | Forces a recomputation of all cached data. |
| Public method | [DollyZoom](M_Grasshopper_GUI_Canvas_GH_Viewport_DollyZoom.htm) | Advanced interface function for mouse 'dolly' zooming. |
| Public method | [Duplicate](M_Grasshopper_GUI_Canvas_GH_Viewport_Duplicate.htm) |  |
| Public method | [Focus(IGH\_Attributes)](M_Grasshopper_GUI_Canvas_GH_Viewport_Focus.htm) | Look at a specific object. |
| Public method | [Focus(ListAddLanguageSpecificTextSet("LSTF4F5122\_5?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");IGH\_AttributesAddLanguageSpecificTextSet("LSTF4F5122\_6?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");)](M_Grasshopper_GUI_Canvas_GH_Viewport_Focus_1.htm) | Look at a set of specific objects. |
| Public method | [Focus(Point)](M_Grasshopper_GUI_Canvas_GH_Viewport_Focus_2.htm) | Look at a specific point. |
| Public method | [Focus(PointF)](M_Grasshopper_GUI_Canvas_GH_Viewport_Focus_3.htm) | Look at a specific point. |
| Public method | [IsVisible(PointFAddLanguageSpecificTextSet("LSTF4F5122\_7?cpp=%");, Single)](M_Grasshopper_GUI_Canvas_GH_Viewport_IsVisible.htm) | Test visibility of a point. |
| Public method | [IsVisible(RectangleFAddLanguageSpecificTextSet("LSTF4F5122\_8?cpp=%");, Single)](M_Grasshopper_GUI_Canvas_GH_Viewport_IsVisible_1.htm) | Test visibility of a rectangle. |
| Public method | [LimitUnit](M_Grasshopper_GUI_Canvas_GH_Viewport_LimitUnit.htm) | Utility function for calculating pixel dimensions in a zoom-aware environment. The desired value is put through the zoom projection and if the resulting size (as displayed on the screen) exceeds the visual limits it is clipped. This function can be used for example to make sure that a certain penwidth never exceeds visual limits (i.e. it doesn't get too thin or too thick on the screen). |
| Public method | [Project](M_Grasshopper_GUI_Canvas_GH_Viewport_Project.htm) | Transform a point from canvas into control coordinate space. |
| Public method | [ProjectPoint](M_Grasshopper_GUI_Canvas_GH_Viewport_ProjectPoint.htm) | Project a point from canvas coordinates into control coordinates. |
| Public method | [ProjectRectangle](M_Grasshopper_GUI_Canvas_GH_Viewport_ProjectRectangle.htm) | Project a rectangle from canvas coordinates into control coordinates. |
| Public method | [ProjectX](M_Grasshopper_GUI_Canvas_GH_Viewport_ProjectX.htm) | Project a value along constant X from canvas coordinates into control coordinates. |
| Public method | [ProjectY](M_Grasshopper_GUI_Canvas_GH_Viewport_ProjectY.htm) | Project a value along constant Y from canvas coordinates into control coordinates. |
| Public method | [Set](M_Grasshopper_GUI_Canvas_GH_Viewport_Set.htm) |  |
| Public method | [SolveUnit](M_Grasshopper_GUI_Canvas_GH_Viewport_SolveUnit.htm) | Utility function for calculating graphics dimensions in a zoom-aware environment. This function can be used for example to compute the linewidth of a pen which always needs to appear as 3 pixels thick on the screen regardless of zoom values. |
| Public method | [Unproject](M_Grasshopper_GUI_Canvas_GH_Viewport_Unproject.htm) | Transform a point from control into canvas coordinate space. |
| Public method | [UnprojectPoint](M_Grasshopper_GUI_Canvas_GH_Viewport_UnprojectPoint.htm) | Project a point from control coordinates into canvas coordinates. |
| Public method | [UnprojectRectangle](M_Grasshopper_GUI_Canvas_GH_Viewport_UnprojectRectangle.htm) | Project a rectangle from control coordinates into canvas coordinates. |
| Public method | [UnprojectX](M_Grasshopper_GUI_Canvas_GH_Viewport_UnprojectX.htm) | Project a value along constant X from control coordinates into canvas coordinates. |
| Public method | [UnprojectY](M_Grasshopper_GUI_Canvas_GH_Viewport_UnprojectY.htm) | Project a value along constant Y from control coordinates into canvas coordinates. |
| Public method | [XFormMatrix](M_Grasshopper_GUI_Canvas_GH_Viewport_XFormMatrix.htm) | Gets the display transformation cached by this viewport. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Fields

|  | Name | Description |
| --- | --- | --- |
| Public fieldStatic member | [ZoomDefault](F_Grasshopper_GUI_Canvas_GH_Viewport_ZoomDefault.htm) |  |
| Public fieldStatic member | [ZoomDefaultLower](F_Grasshopper_GUI_Canvas_GH_Viewport_ZoomDefaultLower.htm) |  |
| Public fieldStatic member | [ZoomDefaultUpper](F_Grasshopper_GUI_Canvas_GH_Viewport_ZoomDefaultUpper.htm) |  |
| Public fieldStatic member | [ZoomMaximum](F_Grasshopper_GUI_Canvas_GH_Viewport_ZoomMaximum.htm) |  |
| Public fieldStatic member | [ZoomMinimum](F_Grasshopper_GUI_Canvas_GH_Viewport_ZoomMinimum.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI.Canvas Namespace](N_Grasshopper_GUI_Canvas.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)