# M_Grasshopper_GUI_GH_GDI_Util_BoxUnion

﻿ GH\_GDI\_Util.BoxUnion Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH\_GDI\_Util Class](../html/T_Grasshopper_GUI_GH_GDI_Util.htm "GH_GDI_Util Class")

[GH\_GDI\_Util Methods](../html/Methods_T_Grasshopper_GUI_GH_GDI_Util.htm "GH_GDI_Util Methods")

[BoxUnion Method](../html/M_Grasshopper_GUI_GH_GDI_Util_BoxUnion.htm "BoxUnion Method ")

[FilletBoxOutline Method](../html/M_Grasshopper_GUI_GH_GDI_Util_FilletBoxOutline.htm "FilletBoxOutline Method ")

[FilletPolyline Method](../html/Overload_Grasshopper_GUI_GH_GDI_Util_FilletPolyline.htm "FilletPolyline Method ")

[FilletRectangle Method](../html/M_Grasshopper_GUI_GH_GDI_Util_FilletRectangle.htm "FilletRectangle Method ")

[Freeform\_Blob Method](../html/Overload_Grasshopper_GUI_GH_GDI_Util_Freeform_Blob.htm "Freeform_Blob Method ")

[SimplifyBoxes Method](../html/M_Grasshopper_GUI_GH_GDI_Util_SimplifyBoxes.htm "SimplifyBoxes Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_GDI\_UtilAddLanguageSpecificTextSet("LST17C5C576\_0?cpp=::|nu=.");BoxUnion Method |

Create the outline of a set of boxes.

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static List<Point[]> BoxUnion(
	IEnumerable<Rectangle> rectangles
)
```

```
Public Shared Function BoxUnion ( 
	rectangles As IEnumerable(Of Rectangle)
) As List(Of Point())
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

rectangles
:   Type: [System.Collections.GenericAddLanguageSpecificTextSet("LST17C5C576\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");IEnumerable](https://docs.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)AddLanguageSpecificTextSet("LST17C5C576\_2?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");[Rectangle](https://docs.microsoft.com/dotnet/api/system.drawing.rectangle)AddLanguageSpecificTextSet("LST17C5C576\_3?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
    Boxes to union.

#### Return Value

Type: [List](https://docs.microsoft.com/dotnet/api/system.collections.generic.list-1)AddLanguageSpecificTextSet("LST17C5C576\_4?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");AddLanguageSpecificTextSet("LST17C5C576\_5?cpp=array&lt;");[Point](https://docs.microsoft.com/dotnet/api/system.drawing.point)AddLanguageSpecificTextSet("LST17C5C576\_6?cpp=&gt;|vb=()|nu=[]");AddLanguageSpecificTextSet("LST17C5C576\_7?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
A list of Point arrays, where each array describes the corners of each silhouette.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_GDI\_Util Class](T_Grasshopper_GUI_GH_GDI_Util.htm)

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)