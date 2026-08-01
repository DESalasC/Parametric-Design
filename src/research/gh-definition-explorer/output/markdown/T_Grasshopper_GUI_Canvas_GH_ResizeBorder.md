# T_Grasshopper_GUI_Canvas_GH_ResizeBorder

﻿ GH\_ResizeBorder Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI.Canvas](../html/N_Grasshopper_GUI_Canvas.htm "Grasshopper.GUI.Canvas")

[GH\_ResizeBorder Class](../html/T_Grasshopper_GUI_Canvas_GH_ResizeBorder.htm "GH_ResizeBorder Class")

[GH\_ResizeBorder Constructor](../html/Overload_Grasshopper_GUI_Canvas_GH_ResizeBorder__ctor.htm "GH_ResizeBorder Constructor ")

[GH\_ResizeBorder Properties](../html/Properties_T_Grasshopper_GUI_Canvas_GH_ResizeBorder.htm "GH_ResizeBorder Properties")

[GH\_ResizeBorder Methods](../html/Methods_T_Grasshopper_GUI_Canvas_GH_ResizeBorder.htm "GH_ResizeBorder Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_ResizeBorder Class |

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST3629B587\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [Grasshopper.GUI.CanvasAddLanguageSpecificTextSet("LST3629B587\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Border](T_Grasshopper_GUI_Canvas_GH_Border.htm)  
    Grasshopper.GUI.CanvasAddLanguageSpecificTextSet("LST3629B587\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_ResizeBorder

**Namespace:**
 [Grasshopper.GUI.Canvas](N_Grasshopper_GUI_Canvas.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_ResizeBorder : GH_Border
```

```
Public Class GH_ResizeBorder
	Inherits GH_Border
```

AddLanguageTabSet("ID1EBCA");

The GH\_ResizeBorder type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_ResizeBorder(GH\_Border)](M_Grasshopper_GUI_Canvas_GH_ResizeBorder__ctor.htm) | Create a new instance of the GH\_ResizeBorder class. |
| Public method | [GH\_ResizeBorder(RectangleF, GH\_BorderTopology)](M_Grasshopper_GUI_Canvas_GH_ResizeBorder__ctor_1.htm) | Create a new instance of the GH\_ResizeBorder class. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Anchor](P_Grasshopper_GUI_Canvas_GH_ResizeBorder_Anchor.htm) | Gets or sets the anchor point for sizing operations. This point is determined automatically when you call Setup(), however you can alter it afterwards if you want. |
| Public property | [Region](P_Grasshopper_GUI_Canvas_GH_Border_Region.htm) | Gets the shape of the border. (Inherited from [GH\_Border](T_Grasshopper_GUI_Canvas_GH_Border.htm).) |
| Public property | [Size\_Cursor](P_Grasshopper_GUI_Canvas_GH_Border_Size_Cursor.htm) | Gets the cursor associated with this border. (Inherited from [GH\_Border](T_Grasshopper_GUI_Canvas_GH_Border.htm).) |
| Public property | [Topology](P_Grasshopper_GUI_Canvas_GH_Border_Topology.htm) | Gets the type of border. (Inherited from [GH\_Border](T_Grasshopper_GUI_Canvas_GH_Border.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [Contains](M_Grasshopper_GUI_Canvas_GH_Border_Contains.htm) | Test a point for border inclusion. (Inherited from [GH\_Border](T_Grasshopper_GUI_Canvas_GH_Border.htm).) |
| Public method | [Setup(IGH\_Attributes, PointF)](M_Grasshopper_GUI_Canvas_GH_ResizeBorder_Setup.htm) | Set up a new sizing operation. |
| Public method | [Setup(IGH\_Attributes, PointF, SizeF)](M_Grasshopper_GUI_Canvas_GH_ResizeBorder_Setup_1.htm) | Set up a new sizing operation. |
| Public method | [Setup(RectangleF, PointF, PointF)](M_Grasshopper_GUI_Canvas_GH_ResizeBorder_Setup_3.htm) | Set up a new sizing operation. |
| Public method | [Setup(IGH\_Attributes, PointF, SizeF, SizeF)](M_Grasshopper_GUI_Canvas_GH_ResizeBorder_Setup_2.htm) | Set up a new sizing operation. |
| Public method | [Setup(RectangleF, PointF, PointF, SizeF)](M_Grasshopper_GUI_Canvas_GH_ResizeBorder_Setup_4.htm) | Set up a new sizing operation. |
| Public method | [Setup(RectangleF, PointF, PointF, SizeF, SizeF)](M_Grasshopper_GUI_Canvas_GH_ResizeBorder_Setup_5.htm) | Set up a new sizing operation. |
| Public method | [Solve](M_Grasshopper_GUI_Canvas_GH_ResizeBorder_Solve.htm) | Solve a resizing step. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI.Canvas Namespace](N_Grasshopper_GUI_Canvas.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)