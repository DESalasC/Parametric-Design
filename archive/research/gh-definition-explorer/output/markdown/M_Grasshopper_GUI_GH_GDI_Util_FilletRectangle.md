# M_Grasshopper_GUI_GH_GDI_Util_FilletRectangle

﻿ GH\_GDI\_Util.FilletRectangle Method 

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
| GH\_GDI\_UtilAddLanguageSpecificTextSet("LSTEA14F299\_0?cpp=::|nu=.");FilletRectangle Method |

Create a rectangle with filleted corners.

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static GraphicsPath FilletRectangle(
	Rectangle box,
	int radius
)
```

```
Public Shared Function FilletRectangle ( 
	box As Rectangle,
	radius As Integer
) As GraphicsPath
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

box
:   Type: [System.DrawingAddLanguageSpecificTextSet("LSTEA14F299\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Rectangle](https://docs.microsoft.com/dotnet/api/system.drawing.rectangle)  
    Rectangle to fillet.

radius
:   Type: [SystemAddLanguageSpecificTextSet("LSTEA14F299\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");Int32](https://docs.microsoft.com/dotnet/api/system.int32)  
    Fillet radius, radius will be limited if too large.

#### Return Value

Type: [GraphicsPath](https://docs.microsoft.com/dotnet/api/system.drawing.drawing2d.graphicspath)  
GraphicsPath describing filletted rectangle.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_GDI\_Util Class](T_Grasshopper_GUI_GH_GDI_Util.htm)

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)