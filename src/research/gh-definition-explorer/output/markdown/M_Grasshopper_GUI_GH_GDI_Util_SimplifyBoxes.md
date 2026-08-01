# M_Grasshopper_GUI_GH_GDI_Util_SimplifyBoxes

﻿ GH\_GDI\_Util.SimplifyBoxes Method 

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
| GH\_GDI\_UtilAddLanguageSpecificTextSet("LST376D3AED\_0?cpp=::|nu=.");SimplifyBoxes Method |

Create a simplified collection of Rectangles that describe the same union space as the supplied rectangles.

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static Rectangle[] SimplifyBoxes(
	IEnumerable<Rectangle> boxes
)
```

```
Public Shared Function SimplifyBoxes ( 
	boxes As IEnumerable(Of Rectangle)
) As Rectangle()
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

boxes
:   Type: [System.Collections.GenericAddLanguageSpecificTextSet("LST376D3AED\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");IEnumerable](https://docs.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)AddLanguageSpecificTextSet("LST376D3AED\_2?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");[Rectangle](https://docs.microsoft.com/dotnet/api/system.drawing.rectangle)AddLanguageSpecificTextSet("LST376D3AED\_3?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");  
    Rectangles to simplify.

#### Return Value

Type: AddLanguageSpecificTextSet("LST376D3AED\_4?cpp=array&lt;");[Rectangle](https://docs.microsoft.com/dotnet/api/system.drawing.rectangle)AddLanguageSpecificTextSet("LST376D3AED\_5?cpp=&gt;|vb=()|nu=[]");  
An ordered collection of non-intersecting rectangles or null on failure.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_GDI\_Util Class](T_Grasshopper_GUI_GH_GDI_Util.htm)

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)