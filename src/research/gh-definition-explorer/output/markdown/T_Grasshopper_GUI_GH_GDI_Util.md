# T_Grasshopper_GUI_GH_GDI_Util

﻿ GH\_GDI\_Util Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH\_GDI\_Util Class](../html/T_Grasshopper_GUI_GH_GDI_Util.htm "GH_GDI_Util Class")

[GH\_GDI\_Util Methods](../html/Methods_T_Grasshopper_GUI_GH_GDI_Util.htm "GH_GDI_Util Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_GDI\_Util Class |

Contains some global function for filleting corners of GDI objects.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST893CAE28\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.GUIAddLanguageSpecificTextSet("LST893CAE28\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_GDI\_Util

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public sealed class GH_GDI_Util
```

```
Public NotInheritable Class GH_GDI_Util
```

AddLanguageTabSet("ID1EBCA");

The GH\_GDI\_Util type exposes the following members.

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public methodStatic member | [BoxUnion](M_Grasshopper_GUI_GH_GDI_Util_BoxUnion.htm) | Create the outline of a set of boxes. |
| Public methodStatic member | [FilletBoxOutline](M_Grasshopper_GUI_GH_GDI_Util_FilletBoxOutline.htm) | Fillet all the corners of the combined outline of a set of rectangles. |
| Public methodStatic member | [FilletPolyline(AddLanguageSpecificTextSet("LST893CAE28\_2?cpp=array&lt;");PointAddLanguageSpecificTextSet("LST893CAE28\_3?cpp=&gt;|cs=[]|vb=()|nu=[]|fs=[]");, Int32)](M_Grasshopper_GUI_GH_GDI_Util_FilletPolyline.htm) | Fillet all the corners of a freeform outline. |
| Public methodStatic member | [FilletPolyline(AddLanguageSpecificTextSet("LST893CAE28\_4?cpp=array&lt;");PointFAddLanguageSpecificTextSet("LST893CAE28\_5?cpp=&gt;|cs=[]|vb=()|nu=[]|fs=[]");, Single)](M_Grasshopper_GUI_GH_GDI_Util_FilletPolyline_1.htm) | Fillet all the corners of a freeform outline. |
| Public methodStatic member | [FilletRectangle](M_Grasshopper_GUI_GH_GDI_Util_FilletRectangle.htm) | Create a rectangle with filleted corners. |
| Public methodStatic member | [Freeform\_Blob(IEnumerableAddLanguageSpecificTextSet("LST893CAE28\_6?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");RectangleFAddLanguageSpecificTextSet("LST893CAE28\_7?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");, Int32, Double)](M_Grasshopper_GUI_GH_GDI_Util_Freeform_Blob.htm) | Create a meta-ball outline for a set of rectangles. |
| Public methodStatic member | [Freeform\_Blob(IEnumerableAddLanguageSpecificTextSet("LST893CAE28\_8?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");RectangleFAddLanguageSpecificTextSet("LST893CAE28\_9?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");, Int32, Double, FieldSolver, Double)](M_Grasshopper_GUI_GH_GDI_Util_Freeform_Blob_1.htm) | Create a meta-ball outline for a set of rectangles. |
| Public methodStatic member | [SimplifyBoxes](M_Grasshopper_GUI_GH_GDI_Util_SimplifyBoxes.htm) | Create a simplified collection of Rectangles that describe the same union space as the supplied rectangles. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)