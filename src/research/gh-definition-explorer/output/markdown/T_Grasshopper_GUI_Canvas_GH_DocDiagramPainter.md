# T_Grasshopper_GUI_Canvas_GH_DocDiagramPainter

﻿ GH\_DocDiagramPainter Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI.Canvas](../html/N_Grasshopper_GUI_Canvas.htm "Grasshopper.GUI.Canvas")

[GH\_DocDiagramPainter Class](../html/T_Grasshopper_GUI_Canvas_GH_DocDiagramPainter.htm "GH_DocDiagramPainter Class")

[GH\_DocDiagramPainter Constructor](../html/M_Grasshopper_GUI_Canvas_GH_DocDiagramPainter__ctor.htm "GH_DocDiagramPainter Constructor ")

[GH\_DocDiagramPainter Properties](../html/Properties_T_Grasshopper_GUI_Canvas_GH_DocDiagramPainter.htm "GH_DocDiagramPainter Properties")

[GH\_DocDiagramPainter Methods](../html/Methods_T_Grasshopper_GUI_Canvas_GH_DocDiagramPainter.htm "GH_DocDiagramPainter Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_DocDiagramPainter Class |

This class paints diagrammatic images of a collection of objects.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST17A97186\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.GUI.CanvasAddLanguageSpecificTextSet("LST17A97186\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_DocDiagramPainter

**Namespace:**
 [Grasshopper.GUI.Canvas](N_Grasshopper_GUI_Canvas.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_DocDiagramPainter
```

```
Public Class GH_DocDiagramPainter
```

AddLanguageTabSet("ID1EBCA");

The GH\_DocDiagramPainter type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_DocDiagramPainter](M_Grasshopper_GUI_Canvas_GH_DocDiagramPainter__ctor.htm) | Initializes a new instance of the GH\_DocDiagramPainter class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [BoundingBox](P_Grasshopper_GUI_Canvas_GH_DocDiagramPainter_BoundingBox.htm) | Gets the 2D domain of the diagram in canvas coordinates. |
| Public property | [DrawingBox](P_Grasshopper_GUI_Canvas_GH_DocDiagramPainter_DrawingBox.htm) | Gets the 2D domain of the diagram in image coordinates. |
| Public property | [IgnoreSelectedStates](P_Grasshopper_GUI_Canvas_GH_DocDiagramPainter_IgnoreSelectedStates.htm) | Gets or sets the Ignore Selected State flag. When set to True, selected objects are not drawn in a different colour. |
| Public property | [Image](P_Grasshopper_GUI_Canvas_GH_DocDiagramPainter_Image.htm) | Gets the diagram image (only available after a call to PaintDiagram(). |
| Public property | [Size](P_Grasshopper_GUI_Canvas_GH_DocDiagramPainter_Size.htm) | Gets the width and height (in pixels) of this diagram image. |
| Public property | [Zoom](P_Grasshopper_GUI_Canvas_GH_DocDiagramPainter_Zoom.htm) | Gets the zoom factor for this diagram. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [MapPoint(Point)](M_Grasshopper_GUI_Canvas_GH_DocDiagramPainter_MapPoint.htm) |  |
| Public method | [MapPoint(PointF)](M_Grasshopper_GUI_Canvas_GH_DocDiagramPainter_MapPoint_1.htm) |  |
| Public method | [MapRectangle](M_Grasshopper_GUI_Canvas_GH_DocDiagramPainter_MapRectangle.htm) |  |
| Public method | [MapX(Int32)](M_Grasshopper_GUI_Canvas_GH_DocDiagramPainter_MapX.htm) |  |
| Public method | [MapX(Single)](M_Grasshopper_GUI_Canvas_GH_DocDiagramPainter_MapX_1.htm) |  |
| Public method | [MapY(Int32)](M_Grasshopper_GUI_Canvas_GH_DocDiagramPainter_MapY.htm) |  |
| Public method | [MapY(Single)](M_Grasshopper_GUI_Canvas_GH_DocDiagramPainter_MapY_1.htm) |  |
| Public method | [PaintDiagram(IEnumerableAddLanguageSpecificTextSet("LST17A97186\_2?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");IGH\_DocumentObjectAddLanguageSpecificTextSet("LST17A97186\_3?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");, Int32, Int32)](M_Grasshopper_GUI_Canvas_GH_DocDiagramPainter_PaintDiagram.htm) | Paint a diagram of a document. |
| Public method | [PaintDiagram(IEnumerableAddLanguageSpecificTextSet("LST17A97186\_4?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");IGH\_DocumentObjectAddLanguageSpecificTextSet("LST17A97186\_5?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");, Int32, Int32, Int32)](M_Grasshopper_GUI_Canvas_GH_DocDiagramPainter_PaintDiagram_1.htm) | Paint a diagram of a document. |
| Public method | [UnmapPoint](M_Grasshopper_GUI_Canvas_GH_DocDiagramPainter_UnmapPoint.htm) |  |
| Public method | [UnmapRectangle](M_Grasshopper_GUI_Canvas_GH_DocDiagramPainter_UnmapRectangle.htm) |  |
| Public method | [UnmapX](M_Grasshopper_GUI_Canvas_GH_DocDiagramPainter_UnmapX.htm) |  |
| Public method | [UnmapY](M_Grasshopper_GUI_Canvas_GH_DocDiagramPainter_UnmapY.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI.Canvas Namespace](N_Grasshopper_GUI_Canvas.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)