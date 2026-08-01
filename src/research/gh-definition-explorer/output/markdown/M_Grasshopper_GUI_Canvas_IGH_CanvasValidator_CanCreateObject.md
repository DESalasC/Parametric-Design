# M_Grasshopper_GUI_Canvas_IGH_CanvasValidator_CanCreateObject

﻿ IGH\_CanvasValidator.CanCreateObject Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI.Canvas](../html/N_Grasshopper_GUI_Canvas.htm "Grasshopper.GUI.Canvas")

[IGH\_CanvasValidator Interface](../html/T_Grasshopper_GUI_Canvas_IGH_CanvasValidator.htm "IGH_CanvasValidator Interface")

[IGH\_CanvasValidator Methods](../html/Methods_T_Grasshopper_GUI_Canvas_IGH_CanvasValidator.htm "IGH_CanvasValidator Methods")

[AddedToCanvas Method](../html/M_Grasshopper_GUI_Canvas_IGH_CanvasValidator_AddedToCanvas.htm "AddedToCanvas Method ")

[AppliesToDocument Method](../html/M_Grasshopper_GUI_Canvas_IGH_CanvasValidator_AppliesToDocument.htm "AppliesToDocument Method ")

[CanAcceptObject Method](../html/M_Grasshopper_GUI_Canvas_IGH_CanvasValidator_CanAcceptObject.htm "CanAcceptObject Method ")

[CanCreateObject Method](../html/M_Grasshopper_GUI_Canvas_IGH_CanvasValidator_CanCreateObject.htm "CanCreateObject Method ")

[CanCreateWire Method](../html/M_Grasshopper_GUI_Canvas_IGH_CanvasValidator_CanCreateWire.htm "CanCreateWire Method ")

[CanDeleteObject Method](../html/M_Grasshopper_GUI_Canvas_IGH_CanvasValidator_CanDeleteObject.htm "CanDeleteObject Method ")

[CanDeleteWire Method](../html/M_Grasshopper_GUI_Canvas_IGH_CanvasValidator_CanDeleteWire.htm "CanDeleteWire Method ")

[CanDragObject Method](../html/M_Grasshopper_GUI_Canvas_IGH_CanvasValidator_CanDragObject.htm "CanDragObject Method ")

[CanNavigateCanvas Method](../html/M_Grasshopper_GUI_Canvas_IGH_CanvasValidator_CanNavigateCanvas.htm "CanNavigateCanvas Method ")

[CanShowCanvasMenu Method](../html/M_Grasshopper_GUI_Canvas_IGH_CanvasValidator_CanShowCanvasMenu.htm "CanShowCanvasMenu Method ")

[CanShowComponentSearchBox Method](../html/M_Grasshopper_GUI_Canvas_IGH_CanvasValidator_CanShowComponentSearchBox.htm "CanShowComponentSearchBox Method ")

[CanShowObjectMenu Method](../html/M_Grasshopper_GUI_Canvas_IGH_CanvasValidator_CanShowObjectMenu.htm "CanShowObjectMenu Method ")

[RemovedFromCanvas Method](../html/M_Grasshopper_GUI_Canvas_IGH_CanvasValidator_RemovedFromCanvas.htm "RemovedFromCanvas Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| IGH\_CanvasValidatorAddLanguageSpecificTextSet("LSTDE3A2D3F\_0?cpp=::|nu=.");CanCreateObject Method |

Validates whether a specific component may be inserted at a specific point.

**Namespace:**
 [Grasshopper.GUI.Canvas](N_Grasshopper_GUI_Canvas.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
bool CanCreateObject(
	Guid id,
	PointF pt
)
```

```
Function CanCreateObject ( 
	id As Guid,
	pt As PointF
) As Boolean
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

id
:   Type: [SystemAddLanguageSpecificTextSet("LSTDE3A2D3F\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");Guid](https://docs.microsoft.com/dotnet/api/system.guid)

pt
:   Type: [System.DrawingAddLanguageSpecificTextSet("LSTDE3A2D3F\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");PointF](https://docs.microsoft.com/dotnet/api/system.drawing.pointf)

#### Return Value

Type: [Boolean](https://docs.microsoft.com/dotnet/api/system.boolean)

![](../icons/SectionExpanded.png)See Also

#### Reference

[IGH\_CanvasValidator Interface](T_Grasshopper_GUI_Canvas_IGH_CanvasValidator.htm)

[Grasshopper.GUI.Canvas Namespace](N_Grasshopper_GUI_Canvas.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)