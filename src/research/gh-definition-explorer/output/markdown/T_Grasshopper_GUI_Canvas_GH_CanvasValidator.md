# T_Grasshopper_GUI_Canvas_GH_CanvasValidator

﻿ GH\_CanvasValidator Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI.Canvas](../html/N_Grasshopper_GUI_Canvas.htm "Grasshopper.GUI.Canvas")

[GH\_CanvasValidator Class](../html/T_Grasshopper_GUI_Canvas_GH_CanvasValidator.htm "GH_CanvasValidator Class")

[GH\_CanvasValidator Constructor](../html/M_Grasshopper_GUI_Canvas_GH_CanvasValidator__ctor.htm "GH_CanvasValidator Constructor ")

[GH\_CanvasValidator Properties](../html/Properties_T_Grasshopper_GUI_Canvas_GH_CanvasValidator.htm "GH_CanvasValidator Properties")

[GH\_CanvasValidator Methods](../html/Methods_T_Grasshopper_GUI_Canvas_GH_CanvasValidator.htm "GH_CanvasValidator Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_CanvasValidator Class |

Abstract implementation of IGH\_CanvasValidator.
Inherit from this class rather than implementing IGH\_CanvasValidator from scratch.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LSTC20BE530\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.GUI.CanvasAddLanguageSpecificTextSet("LSTC20BE530\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_CanvasValidator  
    [Grasshopper.GUI.CanvasAddLanguageSpecificTextSet("LSTC20BE530\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_CanvasDropTargetValidator](T_Grasshopper_GUI_Canvas_GH_CanvasDropTargetValidator.htm)  
    [Grasshopper.GUI.CanvasAddLanguageSpecificTextSet("LSTC20BE530\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_CanvasWireValidator](T_Grasshopper_GUI_Canvas_GH_CanvasWireValidator.htm)

**Namespace:**
 [Grasshopper.GUI.Canvas](N_Grasshopper_GUI_Canvas.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public abstract class GH_CanvasValidator : IGH_CanvasValidator
```

```
Public MustInherit Class GH_CanvasValidator
	Implements IGH_CanvasValidator
```

AddLanguageTabSet("ID1EBCA");

The GH\_CanvasValidator type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Protected method | [GH\_CanvasValidator](M_Grasshopper_GUI_Canvas_GH_CanvasValidator__ctor.htm) | Initializes a new instance of the GH\_CanvasValidator class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Protected property | [Canvas](P_Grasshopper_GUI_Canvas_GH_CanvasValidator_Canvas.htm) | Gets the canvas this validator is associated with. |
| Protected property | [Document](P_Grasshopper_GUI_Canvas_GH_CanvasValidator_Document.htm) | Gets the document (if it exists) that is currently loaded in the canvas. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [AddedToCanvas](M_Grasshopper_GUI_Canvas_GH_CanvasValidator_AddedToCanvas.htm) | Override this method if you want to be informed when this validator gets assigned to a canvas. But \*always\* call the base class method. |
| Public method | [AppliesToDocument](M_Grasshopper_GUI_Canvas_GH_CanvasValidator_AppliesToDocument.htm) |  |
| Public method | [CanAcceptObject](M_Grasshopper_GUI_Canvas_GH_CanvasValidator_CanAcceptObject.htm) |  |
| Public method | [CanCreateObject](M_Grasshopper_GUI_Canvas_GH_CanvasValidator_CanCreateObject.htm) |  |
| Public method | [CanCreateWire](M_Grasshopper_GUI_Canvas_GH_CanvasValidator_CanCreateWire.htm) |  |
| Public method | [CanDeleteObject](M_Grasshopper_GUI_Canvas_GH_CanvasValidator_CanDeleteObject.htm) |  |
| Public method | [CanDeleteWire](M_Grasshopper_GUI_Canvas_GH_CanvasValidator_CanDeleteWire.htm) |  |
| Public method | [CanDragObject](M_Grasshopper_GUI_Canvas_GH_CanvasValidator_CanDragObject.htm) |  |
| Public method | [CanNavigateCanvas](M_Grasshopper_GUI_Canvas_GH_CanvasValidator_CanNavigateCanvas.htm) |  |
| Public method | [CanShowCanvasMenu](M_Grasshopper_GUI_Canvas_GH_CanvasValidator_CanShowCanvasMenu.htm) |  |
| Public method | [CanShowComponentSearchBox](M_Grasshopper_GUI_Canvas_GH_CanvasValidator_CanShowComponentSearchBox.htm) |  |
| Public method | [CanShowObjectMenu](M_Grasshopper_GUI_Canvas_GH_CanvasValidator_CanShowObjectMenu.htm) |  |
| Public method | [RemovedFromCanvas](M_Grasshopper_GUI_Canvas_GH_CanvasValidator_RemovedFromCanvas.htm) | Override this method if you want to be informed when this validator gets removed from a canvas. But \*always\* call the base class method. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI.Canvas Namespace](N_Grasshopper_GUI_Canvas.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)