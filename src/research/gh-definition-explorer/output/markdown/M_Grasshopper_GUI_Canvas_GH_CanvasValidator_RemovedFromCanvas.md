# M_Grasshopper_GUI_Canvas_GH_CanvasValidator_RemovedFromCanvas

﻿ GH\_CanvasValidator.RemovedFromCanvas Method 

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI.Canvas](../html/N_Grasshopper_GUI_Canvas.htm "Grasshopper.GUI.Canvas")

[GH\_CanvasValidator Class](../html/T_Grasshopper_GUI_Canvas_GH_CanvasValidator.htm "GH_CanvasValidator Class")

[GH\_CanvasValidator Methods](../html/Methods_T_Grasshopper_GUI_Canvas_GH_CanvasValidator.htm "GH_CanvasValidator Methods")

[AddedToCanvas Method](../html/M_Grasshopper_GUI_Canvas_GH_CanvasValidator_AddedToCanvas.htm "AddedToCanvas Method ")

[AppliesToDocument Method](../html/M_Grasshopper_GUI_Canvas_GH_CanvasValidator_AppliesToDocument.htm "AppliesToDocument Method ")

[CanAcceptObject Method](../html/M_Grasshopper_GUI_Canvas_GH_CanvasValidator_CanAcceptObject.htm "CanAcceptObject Method ")

[CanCreateObject Method](../html/M_Grasshopper_GUI_Canvas_GH_CanvasValidator_CanCreateObject.htm "CanCreateObject Method ")

[CanCreateWire Method](../html/M_Grasshopper_GUI_Canvas_GH_CanvasValidator_CanCreateWire.htm "CanCreateWire Method ")

[CanDeleteObject Method](../html/M_Grasshopper_GUI_Canvas_GH_CanvasValidator_CanDeleteObject.htm "CanDeleteObject Method ")

[CanDeleteWire Method](../html/M_Grasshopper_GUI_Canvas_GH_CanvasValidator_CanDeleteWire.htm "CanDeleteWire Method ")

[CanDragObject Method](../html/M_Grasshopper_GUI_Canvas_GH_CanvasValidator_CanDragObject.htm "CanDragObject Method ")

[CanNavigateCanvas Method](../html/M_Grasshopper_GUI_Canvas_GH_CanvasValidator_CanNavigateCanvas.htm "CanNavigateCanvas Method ")

[CanShowCanvasMenu Method](../html/M_Grasshopper_GUI_Canvas_GH_CanvasValidator_CanShowCanvasMenu.htm "CanShowCanvasMenu Method ")

[CanShowComponentSearchBox Method](../html/M_Grasshopper_GUI_Canvas_GH_CanvasValidator_CanShowComponentSearchBox.htm "CanShowComponentSearchBox Method ")

[CanShowObjectMenu Method](../html/M_Grasshopper_GUI_Canvas_GH_CanvasValidator_CanShowObjectMenu.htm "CanShowObjectMenu Method ")

[RemovedFromCanvas Method](../html/M_Grasshopper_GUI_Canvas_GH_CanvasValidator_RemovedFromCanvas.htm "RemovedFromCanvas Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_CanvasValidatorAddLanguageSpecificTextSet("LST416CABC2\_0?cpp=::|nu=.");RemovedFromCanvas Method |

Override this method if you want to be informed when this validator gets removed from a canvas.
But \*always\* call the base class method.

**Namespace:**
 [Grasshopper.GUI.Canvas](N_Grasshopper_GUI_Canvas.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public virtual void RemovedFromCanvas(
	GH_Canvas canvas
)
```

```
Public Overridable Sub RemovedFromCanvas ( 
	canvas As GH_Canvas
)
```

AddLanguageTabSet("ID0EBCA");

#### Parameters

canvas
:   Type: [Grasshopper.GUI.CanvasAddLanguageSpecificTextSet("LST416CABC2\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Canvas](T_Grasshopper_GUI_Canvas_GH_Canvas.htm)

#### Implements

[IGH\_CanvasValidatorAddLanguageSpecificTextSet("LST416CABC2\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");RemovedFromCanvas(GH\_Canvas)](M_Grasshopper_GUI_Canvas_IGH_CanvasValidator_RemovedFromCanvas.htm)

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_CanvasValidator Class](T_Grasshopper_GUI_Canvas_GH_CanvasValidator.htm)

[Grasshopper.GUI.Canvas Namespace](N_Grasshopper_GUI_Canvas.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)