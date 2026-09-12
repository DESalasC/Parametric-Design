# M_Grasshopper_GUI_GH_GraphicsUtil_RenderObjectOverlay

﻿ GH\_GraphicsUtil.RenderObjectOverlay Method (Graphics, IGH\_DocumentObject, RectangleF)

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI](../html/N_Grasshopper_GUI.htm "Grasshopper.GUI")

[GH\_GraphicsUtil Class](../html/T_Grasshopper_GUI_GH_GraphicsUtil.htm "GH_GraphicsUtil Class")

[GH\_GraphicsUtil Methods](../html/Methods_T_Grasshopper_GUI_GH_GraphicsUtil.htm "GH_GraphicsUtil Methods")

[RenderObjectOverlay Method](../html/Overload_Grasshopper_GUI_GH_GraphicsUtil_RenderObjectOverlay.htm "RenderObjectOverlay Method ")

[RenderObjectOverlay Method (Graphics, IGH\_DocumentObject, RectangleF)](../html/M_Grasshopper_GUI_GH_GraphicsUtil_RenderObjectOverlay.htm "RenderObjectOverlay Method (Graphics, IGH_DocumentObject, RectangleF)")

[RenderObjectOverlay Method (Graphics, IGH\_ObjectProxy, RectangleF)](../html/M_Grasshopper_GUI_GH_GraphicsUtil_RenderObjectOverlay_1.htm "RenderObjectOverlay Method (Graphics, IGH_ObjectProxy, RectangleF)")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_GraphicsUtilAddLanguageSpecificTextSet("LSTEB0F32D2\_0?cpp=::|nu=.");RenderObjectOverlay Method (Graphics, IGH\_DocumentObject, RectangleF) |

Render all overlay icons for a specific object.
Overlays aren't drawn when the zoom is less than 80%

**Namespace:**
 [Grasshopper.GUI](N_Grasshopper_GUI.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public static void RenderObjectOverlay(
	Graphics graphics,
	IGH_DocumentObject obj,
	RectangleF target
)
```

```
Public Shared Sub RenderObjectOverlay ( 
	graphics As Graphics,
	obj As IGH_DocumentObject,
	target As RectangleF
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

graphics
:   Type: [System.DrawingAddLanguageSpecificTextSet("LSTEB0F32D2\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Graphics](https://docs.microsoft.com/dotnet/api/system.drawing.graphics)  
    Graphics object to draw with.

obj
:   Type: [Grasshopper.KernelAddLanguageSpecificTextSet("LSTEB0F32D2\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");IGH\_DocumentObject](T_Grasshopper_Kernel_IGH_DocumentObject.htm)  
    Object to draw overlay for.

target
:   Type: [System.DrawingAddLanguageSpecificTextSet("LSTEB0F32D2\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");RectangleF](https://docs.microsoft.com/dotnet/api/system.drawing.rectanglef)  
    Destination area for overlay icons.

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_GraphicsUtil Class](T_Grasshopper_GUI_GH_GraphicsUtil.htm)

[RenderObjectOverlay Overload](Overload_Grasshopper_GUI_GH_GraphicsUtil_RenderObjectOverlay.htm)

[Grasshopper.GUI Namespace](N_Grasshopper_GUI.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)