# T_Grasshopper_GUI_Canvas_GH_Capsule

﻿ GH\_Capsule Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI.Canvas](../html/N_Grasshopper_GUI_Canvas.htm "Grasshopper.GUI.Canvas")

[GH\_Capsule Class](../html/T_Grasshopper_GUI_Canvas_GH_Capsule.htm "GH_Capsule Class")

[GH\_Capsule Properties](../html/Properties_T_Grasshopper_GUI_Canvas_GH_Capsule.htm "GH_Capsule Properties")

[GH\_Capsule Methods](../html/Methods_T_Grasshopper_GUI_Canvas_GH_Capsule.htm "GH_Capsule Methods")

[GH\_Capsule Fields](../html/Fields_T_Grasshopper_GUI_Canvas_GH_Capsule.htm "GH_Capsule Fields")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_Capsule Class |

Class used to draw standard Grasshopper interface boxes.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST2A33C2AA\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.GUI.CanvasAddLanguageSpecificTextSet("LST2A33C2AA\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Capsule

**Namespace:**
 [Grasshopper.GUI.Canvas](N_Grasshopper_GUI_Canvas.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_Capsule : IDisposable
```

```
Public Class GH_Capsule
	Implements IDisposable
```

AddLanguageTabSet("ID1EBCA");

The GH\_Capsule type exposes the following members.

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Box](P_Grasshopper_GUI_Canvas_GH_Capsule_Box.htm) | Gets the outline box for this Capsule. |
| Public property | [Box\_Content](P_Grasshopper_GUI_Canvas_GH_Capsule_Box_Content.htm) | Gets the content box for this Capsule. Text and icons are drawn inside this box. |
| Public property | [Font](P_Grasshopper_GUI_Canvas_GH_Capsule_Font.htm) | Gets or sets the Font to use for text rendering. |
| Public property | [Highlight](P_Grasshopper_GUI_Canvas_GH_Capsule_Highlight.htm) | Gets the highlight size for this Capsule. Zero or negative means there is no highlight. |
| Public property | [HighlightShape](P_Grasshopper_GUI_Canvas_GH_Capsule_HighlightShape.htm) | Gets the graphics path that describes the highlight bar shape of the capsule. |
| Public property | [InputGrips](P_Grasshopper_GUI_Canvas_GH_Capsule_InputGrips.htm) | Gets the list of locally defined input grip locations. |
| Public property | [JaggedLeft](P_Grasshopper_GUI_Canvas_GH_Capsule_JaggedLeft.htm) | Gets whether the left edge of this capsule is jagged. |
| Public property | [JaggedRight](P_Grasshopper_GUI_Canvas_GH_Capsule_JaggedRight.htm) | Gets whether the right edge of this capsule is jagged. |
| Public property | [MaxRadius](P_Grasshopper_GUI_Canvas_GH_Capsule_MaxRadius.htm) | Gets the largest radius defined for this capsule. |
| Public property | [OutlineShape](P_Grasshopper_GUI_Canvas_GH_Capsule_OutlineShape.htm) | Gets the graphics path that describes the outer edge of the capsule. |
| Public property | [OutputGrips](P_Grasshopper_GUI_Canvas_GH_Capsule_OutputGrips.htm) | Gets the list of locally defined output grip locations. |
| Public property | [Palette](P_Grasshopper_GUI_Canvas_GH_Capsule_Palette.htm) | Gets or sets the palette for this Capsule. |
| Public property | [Radius](P_Grasshopper_GUI_Canvas_GH_Capsule_Radius.htm) | Gets the radius of the rounded corners of this Capsule. |
| Public property | [RenderEngine](P_Grasshopper_GUI_Canvas_GH_Capsule_RenderEngine.htm) | Gets the RenderEngine associated with this capsule. You typically don't need to go this far, just use one of the Render() overloads on GH\_Capsule directly. |
| Public property | [Text](P_Grasshopper_GUI_Canvas_GH_Capsule_Text.htm) | Gets or sets the text to render in the content box. |
| Public property | [TextOrientation](P_Grasshopper_GUI_Canvas_GH_Capsule_TextOrientation.htm) | Gets or sets the orientation of the text within the content box. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [AddInputGrip(Point)](M_Grasshopper_GUI_Canvas_GH_Capsule_AddInputGrip.htm) | Add an input grip to this UI Box. |
| Public method | [AddInputGrip(PointF)](M_Grasshopper_GUI_Canvas_GH_Capsule_AddInputGrip_1.htm) | Add an input grip to this UI Box. |
| Public method | [AddInputGrip(Single)](M_Grasshopper_GUI_Canvas_GH_Capsule_AddInputGrip_2.htm) | Add an input grip to this UI Box. This is the recommended overload. |
| Public method | [AddInputGrip(Single, Single)](M_Grasshopper_GUI_Canvas_GH_Capsule_AddInputGrip_3.htm) | Add an input grip to this UI Box. |
| Public method | [AddOutputGrip(Point)](M_Grasshopper_GUI_Canvas_GH_Capsule_AddOutputGrip.htm) | Add an output grip to this UI Box. |
| Public method | [AddOutputGrip(PointF)](M_Grasshopper_GUI_Canvas_GH_Capsule_AddOutputGrip_1.htm) | Add an output grip to this UI Box. |
| Public method | [AddOutputGrip(Single)](M_Grasshopper_GUI_Canvas_GH_Capsule_AddOutputGrip_2.htm) | Add an output grip to this UI Box. This is the recommended overload. |
| Public method | [AddOutputGrip(Single, Single)](M_Grasshopper_GUI_Canvas_GH_Capsule_AddOutputGrip_3.htm) | Add an output grip to this UI Box. |
| Public method | [Contains](M_Grasshopper_GUI_Canvas_GH_Capsule_Contains.htm) | Test a point for capsule containment. |
| Public methodStatic member | [CreateCapsule(Rectangle, GH\_Palette)](M_Grasshopper_GUI_Canvas_GH_Capsule_CreateCapsule.htm) | Create a new blank capsule with default radius and highlight dimensions. |
| Public methodStatic member | [CreateCapsule(RectangleF, GH\_Palette)](M_Grasshopper_GUI_Canvas_GH_Capsule_CreateCapsule_3.htm) | Create a new blank capsule with default radius and highlight dimensions. |
| Public methodStatic member | [CreateCapsule(Rectangle, GH\_Palette, Int32, Int32)](M_Grasshopper_GUI_Canvas_GH_Capsule_CreateCapsule_1.htm) | Create a new blank capsule. |
| Public methodStatic member | [CreateCapsule(Rectangle, GH\_Palette, AddLanguageSpecificTextSet("LST2A33C2AA\_2?cpp=array&lt;");Int32AddLanguageSpecificTextSet("LST2A33C2AA\_3?cpp=&gt;|cs=[]|vb=()|nu=[]|fs=[]");, Int32)](M_Grasshopper_GUI_Canvas_GH_Capsule_CreateCapsule_2.htm) | Create a new blank capsule. |
| Public methodStatic member | [CreateCapsule(RectangleF, GH\_Palette, Int32, Int32)](M_Grasshopper_GUI_Canvas_GH_Capsule_CreateCapsule_4.htm) | Create a new blank capsule. |
| Public methodStatic member | [CreateCapsule(RectangleF, GH\_Palette, AddLanguageSpecificTextSet("LST2A33C2AA\_4?cpp=array&lt;");Int32AddLanguageSpecificTextSet("LST2A33C2AA\_5?cpp=&gt;|cs=[]|vb=()|nu=[]|fs=[]");, Int32)](M_Grasshopper_GUI_Canvas_GH_Capsule_CreateCapsule_5.htm) | Create a new blank capsule. |
| Public methodStatic member | [CreateTextCapsule(Rectangle, Rectangle, GH\_Palette, String)](M_Grasshopper_GUI_Canvas_GH_Capsule_CreateTextCapsule.htm) | Create a new capsule with content text. |
| Public methodStatic member | [CreateTextCapsule(RectangleF, RectangleF, GH\_Palette, String)](M_Grasshopper_GUI_Canvas_GH_Capsule_CreateTextCapsule_9.htm) | Create a new capsule with content text. |
| Public methodStatic member | [CreateTextCapsule(Rectangle, Rectangle, GH\_Palette, String, Font)](M_Grasshopper_GUI_Canvas_GH_Capsule_CreateTextCapsule_1.htm) | Create a new capsule with content text. |
| Public methodStatic member | [CreateTextCapsule(RectangleF, RectangleF, GH\_Palette, String, Font)](M_Grasshopper_GUI_Canvas_GH_Capsule_CreateTextCapsule_10.htm) | Create a new capsule with content text. |
| Public methodStatic member | [CreateTextCapsule(Rectangle, Rectangle, GH\_Palette, String, Font, GH\_Orientation)](M_Grasshopper_GUI_Canvas_GH_Capsule_CreateTextCapsule_2.htm) | Create a new capsule with content text. |
| Public methodStatic member | [CreateTextCapsule(Rectangle, Rectangle, GH\_Palette, String, Int32, Int32)](M_Grasshopper_GUI_Canvas_GH_Capsule_CreateTextCapsule_7.htm) | Create a new capsule with content text. |
| Public methodStatic member | [CreateTextCapsule(Rectangle, Rectangle, GH\_Palette, String, AddLanguageSpecificTextSet("LST2A33C2AA\_6?cpp=array&lt;");Int32AddLanguageSpecificTextSet("LST2A33C2AA\_7?cpp=&gt;|cs=[]|vb=()|nu=[]|fs=[]");, Int32)](M_Grasshopper_GUI_Canvas_GH_Capsule_CreateTextCapsule_8.htm) | Create a new capsule with content text. |
| Public methodStatic member | [CreateTextCapsule(RectangleF, RectangleF, GH\_Palette, String, Font, GH\_Orientation)](M_Grasshopper_GUI_Canvas_GH_Capsule_CreateTextCapsule_11.htm) | Create a new capsule with content text. |
| Public methodStatic member | [CreateTextCapsule(RectangleF, RectangleF, GH\_Palette, String, Int32, Int32)](M_Grasshopper_GUI_Canvas_GH_Capsule_CreateTextCapsule_16.htm) | Create a new capsule with content text. |
| Public methodStatic member | [CreateTextCapsule(RectangleF, RectangleF, GH\_Palette, String, AddLanguageSpecificTextSet("LST2A33C2AA\_8?cpp=array&lt;");Int32AddLanguageSpecificTextSet("LST2A33C2AA\_9?cpp=&gt;|cs=[]|vb=()|nu=[]|fs=[]");, Int32)](M_Grasshopper_GUI_Canvas_GH_Capsule_CreateTextCapsule_17.htm) | Create a new capsule with content text. |
| Public methodStatic member | [CreateTextCapsule(Rectangle, Rectangle, GH\_Palette, String, Font, Int32, Int32)](M_Grasshopper_GUI_Canvas_GH_Capsule_CreateTextCapsule_5.htm) | Create a new capsule with content text. |
| Public methodStatic member | [CreateTextCapsule(Rectangle, Rectangle, GH\_Palette, String, Font, AddLanguageSpecificTextSet("LST2A33C2AA\_10?cpp=array&lt;");Int32AddLanguageSpecificTextSet("LST2A33C2AA\_11?cpp=&gt;|cs=[]|vb=()|nu=[]|fs=[]");, Int32)](M_Grasshopper_GUI_Canvas_GH_Capsule_CreateTextCapsule_6.htm) | Create a new capsule with content text. |
| Public methodStatic member | [CreateTextCapsule(RectangleF, RectangleF, GH\_Palette, String, Font, Int32, Int32)](M_Grasshopper_GUI_Canvas_GH_Capsule_CreateTextCapsule_14.htm) | Create a new capsule with content text. |
| Public methodStatic member | [CreateTextCapsule(RectangleF, RectangleF, GH\_Palette, String, Font, AddLanguageSpecificTextSet("LST2A33C2AA\_12?cpp=array&lt;");Int32AddLanguageSpecificTextSet("LST2A33C2AA\_13?cpp=&gt;|cs=[]|vb=()|nu=[]|fs=[]");, Int32)](M_Grasshopper_GUI_Canvas_GH_Capsule_CreateTextCapsule_15.htm) | Create a new capsule with content text. |
| Public methodStatic member | [CreateTextCapsule(Rectangle, Rectangle, GH\_Palette, String, Font, GH\_Orientation, Int32, Int32)](M_Grasshopper_GUI_Canvas_GH_Capsule_CreateTextCapsule_3.htm) | Create a new capsule with content text. |
| Public methodStatic member | [CreateTextCapsule(Rectangle, Rectangle, GH\_Palette, String, Font, GH\_Orientation, AddLanguageSpecificTextSet("LST2A33C2AA\_14?cpp=array&lt;");Int32AddLanguageSpecificTextSet("LST2A33C2AA\_15?cpp=&gt;|cs=[]|vb=()|nu=[]|fs=[]");, Int32)](M_Grasshopper_GUI_Canvas_GH_Capsule_CreateTextCapsule_4.htm) | Create a new capsule with content text. |
| Public methodStatic member | [CreateTextCapsule(RectangleF, RectangleF, GH\_Palette, String, Font, GH\_Orientation, Int32, Int32)](M_Grasshopper_GUI_Canvas_GH_Capsule_CreateTextCapsule_12.htm) | Create a new capsule with content text. |
| Public methodStatic member | [CreateTextCapsule(RectangleF, RectangleF, GH\_Palette, String, Font, GH\_Orientation, AddLanguageSpecificTextSet("LST2A33C2AA\_16?cpp=array&lt;");Int32AddLanguageSpecificTextSet("LST2A33C2AA\_17?cpp=&gt;|cs=[]|vb=()|nu=[]|fs=[]");, Int32)](M_Grasshopper_GUI_Canvas_GH_Capsule_CreateTextCapsule_13.htm) | Create a new capsule with content text. |
| Public method | [DisposeAddLanguageSpecificTextSet("LST2A33C2AA\_18?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_GUI_Canvas_GH_Capsule_Dispose.htm) | Releases all resources used by the GH\_Capsule |
| Protected method | [Dispose(Boolean)](M_Grasshopper_GUI_Canvas_GH_Capsule_Dispose_1.htm) | Releases the unmanaged resources used by the GH\_Capsule and optionally releases the managed resources |
| Public method | [Render(Graphics, GH\_PaletteStyle)](M_Grasshopper_GUI_Canvas_GH_Capsule_Render.htm) | Have this capsule draw itself onto a Graphics surface with a custom Style override. |
| Public method | [Render(Graphics, Color)](M_Grasshopper_GUI_Canvas_GH_Capsule_Render_2.htm) | Have this capsule draw itself onto a Graphics surface with a custom colour override. |
| Public method | [Render(Graphics, Image, GH\_PaletteStyle)](M_Grasshopper_GUI_Canvas_GH_Capsule_Render_3.htm) | Have this capsule draw itself onto a Graphics surface with a custom Style override. |
| Public method | [Render(Graphics, Image, Color)](M_Grasshopper_GUI_Canvas_GH_Capsule_Render_5.htm) | Have this capsule draw itself onto a Graphics surface with a custom colour override. |
| Public method | [Render(Graphics, Boolean, Boolean, Boolean)](M_Grasshopper_GUI_Canvas_GH_Capsule_Render_1.htm) | Render the capsule onto a graphics context. |
| Public method | [Render(Graphics, Image, Boolean, Boolean, Boolean)](M_Grasshopper_GUI_Canvas_GH_Capsule_Render_4.htm) | Render the capsule onto a graphics context. |
| Public method | [SetJaggedEdges](M_Grasshopper_GUI_Canvas_GH_Capsule_SetJaggedEdges.htm) | Assign left and right jagged edges. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Fields

|  | Name | Description |
| --- | --- | --- |
| Public fieldStatic member | [DefaultHighlight](F_Grasshopper_GUI_Canvas_GH_Capsule_DefaultHighlight.htm) | The default size (in pixel units) of the highlight bar. |
| Public fieldStatic member | [DefaultRadius](F_Grasshopper_GUI_Canvas_GH_Capsule_DefaultRadius.htm) | The default radius (in pixel units) of the rounded corners. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI.Canvas Namespace](N_Grasshopper_GUI_Canvas.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)