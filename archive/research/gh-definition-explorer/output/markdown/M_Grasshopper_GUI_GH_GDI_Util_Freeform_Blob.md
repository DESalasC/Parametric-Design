# M_Grasshopper_GUI_GH_GDI_Util_Freeform_Blob

﻿ GH\_GDI\_Util.Freeform\_Blob Method (IEnumerable(RectangleF), Int32, Double)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH\_GDI\_Util Class](../html/T_Grasshopper_GUI_GH_GDI_Util.htm "GH_GDI_Util Class")

[GH\_GDI\_Util Methods](../html/Methods_T_Grasshopper_GUI_GH_GDI_Util.htm "GH_GDI_Util Methods")

[Freeform\_Blob Method](../html/Overload_Grasshopper_GUI_GH_GDI_Util_Freeform_Blob.htm "Freeform_Blob Method ")

[Freeform\_Blob Method (IEnumerable(RectangleF), Int32, Double)](../html/M_Grasshopper_GUI_GH_GDI_Util_Freeform_Blob.htm "Freeform_Blob Method (IEnumerable(RectangleF), Int32, Double)")

[Freeform\_Blob Method (IEnumerable(RectangleF), Int32, Double, GH\_Context.FieldSolver, Double)](../html/M_Grasshopper_GUI_GH_GDI_Util_Freeform_Blob_1.htm "Freeform_Blob Method (IEnumerable(RectangleF), Int32, Double, GH_Context.FieldSolver, Double)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_GDI\_UtilAddLanguageSpecificTextSet("LSTA07AB0CA\_0?cpp=::|nu=.");Freeform\_Blob Method (IEnumerableAddLanguageSpecificTextSet("LSTA07AB0CA\_1?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");RectangleFAddLanguageSpecificTextSet("LSTA07AB0CA\_2?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");, Int32, Double) |

Create a meta-ball outline for a set of rectangles.

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static GraphicsPath Freeform_Blob(
	IEnumerable<RectangleF> content,
	int padding,
	double accuracy
)
```

```
Public Shared Function Freeform_Blob ( 
	content As IEnumerable(Of RectangleF),
	padding As Integer,
	accuracy As Double
) As GraphicsPath
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

content
:   Type: [System.Collections.GenericAddLanguageSpecificTextSet("LSTA07AB0CA\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");IEnumerable](https://docs.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)AddLanguageSpecificTextSet("LSTA07AB0CA\_4?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");[RectangleF](https://docs.microsoft.com/dotnet/api/system.drawing.rectanglef)AddLanguageSpecificTextSet("LSTA07AB0CA\_5?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
    Rectangles to encompass.

padding
:   Type: [SystemAddLanguageSpecificTextSet("LSTA07AB0CA\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Number of units to add to each box.

accuracy
:   Type: [SystemAddLanguageSpecificTextSet("LSTA07AB0CA\_7?cs=.|vb=.|cpp=::|nu=.|fs=.");Double](https://docs.microsoft.com/dotnet/api/system.double)  
    Pixel accuracy for isosurface outlines. 3 is a good value for 1:1 UI.

#### Return Value

Type: [GraphicsPath](https://docs.microsoft.com/dotnet/api/system.drawing.drawing2d.graphicspath)  
A graphics path describing all iso-surfaces.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_GDI\_Util Class](T_Grasshopper_GUI_GH_GDI_Util.htm)

[Freeform\_Blob Overload](Overload_Grasshopper_GUI_GH_GDI_Util_Freeform_Blob.htm)

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)