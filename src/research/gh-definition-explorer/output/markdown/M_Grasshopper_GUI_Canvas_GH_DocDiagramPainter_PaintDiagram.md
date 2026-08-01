# M_Grasshopper_GUI_Canvas_GH_DocDiagramPainter_PaintDiagram

﻿ GH\_DocDiagramPainter.PaintDiagram Method (IEnumerable(IGH\_DocumentObject), Int32, Int32)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI.Canvas](../html/N_Grasshopper_GUI_Canvas.htm "Grasshopper.GUI.Canvas")

[GH\_DocDiagramPainter Class](../html/T_Grasshopper_GUI_Canvas_GH_DocDiagramPainter.htm "GH_DocDiagramPainter Class")

[GH\_DocDiagramPainter Methods](../html/Methods_T_Grasshopper_GUI_Canvas_GH_DocDiagramPainter.htm "GH_DocDiagramPainter Methods")

[PaintDiagram Method](../html/Overload_Grasshopper_GUI_Canvas_GH_DocDiagramPainter_PaintDiagram.htm "PaintDiagram Method ")

[PaintDiagram Method (IEnumerable(IGH\_DocumentObject), Int32, Int32)](../html/M_Grasshopper_GUI_Canvas_GH_DocDiagramPainter_PaintDiagram.htm "PaintDiagram Method (IEnumerable(IGH_DocumentObject), Int32, Int32)")

[PaintDiagram Method (IEnumerable(IGH\_DocumentObject), Int32, Int32, Int32)](../html/M_Grasshopper_GUI_Canvas_GH_DocDiagramPainter_PaintDiagram_1.htm "PaintDiagram Method (IEnumerable(IGH_DocumentObject), Int32, Int32, Int32)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_DocDiagramPainterAddLanguageSpecificTextSet("LSTB9E06DE6\_0?cpp=::|nu=.");PaintDiagram Method (IEnumerableAddLanguageSpecificTextSet("LSTB9E06DE6\_1?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");IGH\_DocumentObjectAddLanguageSpecificTextSet("LSTB9E06DE6\_2?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");, Int32, Int32) |

Paint a diagram of a document.

**Namespace:**
 [Grasshopper.GUI.Canvas](N_Grasshopper_GUI_Canvas.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public bool PaintDiagram(
	IEnumerable<IGH_DocumentObject> objs,
	int approx_size,
	int inflate
)
```

```
Public Function PaintDiagram ( 
	objs As IEnumerable(Of IGH_DocumentObject),
	approx_size As Integer,
	inflate As Integer
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

objs
:   Type: [System.Collections.GenericAddLanguageSpecificTextSet("LSTB9E06DE6\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");IEnumerable](https://docs.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)AddLanguageSpecificTextSet("LSTB9E06DE6\_4?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");[IGH\_DocumentObject](T_Grasshopper_Kernel_IGH_DocumentObject.htm)AddLanguageSpecificTextSet("LSTB9E06DE6\_5?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
    Objects to paint.

approx\_size
:   Type: [SystemAddLanguageSpecificTextSet("LSTB9E06DE6\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Approximate size along each side.

inflate
:   Type: [SystemAddLanguageSpecificTextSet("LSTB9E06DE6\_7?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Padding around the objects.

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)  
True on success, false on failure.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_DocDiagramPainter Class](T_Grasshopper_GUI_Canvas_GH_DocDiagramPainter.htm)

[PaintDiagram Overload](Overload_Grasshopper_GUI_Canvas_GH_DocDiagramPainter_PaintDiagram.htm)

[Grasshopper.GUI.Canvas Namespace](N_Grasshopper_GUI_Canvas.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)