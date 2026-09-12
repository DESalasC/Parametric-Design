# T_Grasshopper_GUI_Canvas_GH_CanvasWireValidator

﻿ GH\_CanvasWireValidator Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI.Canvas](../html/N_Grasshopper_GUI_Canvas.htm "Grasshopper.GUI.Canvas")

[GH\_CanvasWireValidator Class](../html/T_Grasshopper_GUI_Canvas_GH_CanvasWireValidator.htm "GH_CanvasWireValidator Class")

[GH\_CanvasWireValidator Constructor](../html/M_Grasshopper_GUI_Canvas_GH_CanvasWireValidator__ctor.htm "GH_CanvasWireValidator Constructor ")

[GH\_CanvasWireValidator Properties](../html/Properties_T_Grasshopper_GUI_Canvas_GH_CanvasWireValidator.htm "GH_CanvasWireValidator Properties")

[GH\_CanvasWireValidator Methods](../html/Methods_T_Grasshopper_GUI_Canvas_GH_CanvasWireValidator.htm "GH_CanvasWireValidator Methods")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_CanvasWireValidator Class |

Utility validator for restricting wire creation.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LST477568EE\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  [Grasshopper.GUI.CanvasAddLanguageSpecificTextSet("LST477568EE\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_CanvasValidator](T_Grasshopper_GUI_Canvas_GH_CanvasValidator.htm)  
    Grasshopper.GUI.CanvasAddLanguageSpecificTextSet("LST477568EE\_2?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_CanvasWireValidator

**Namespace:**
 [Grasshopper.GUI.Canvas](N_Grasshopper_GUI_Canvas.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_CanvasWireValidator : GH_CanvasValidator
```

```
Public Class GH_CanvasWireValidator
	Inherits GH_CanvasValidator
```

AddLanguageTabSet("ID1EBCA");

The GH\_CanvasWireValidator type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_CanvasWireValidator](M_Grasshopper_GUI_Canvas_GH_CanvasWireValidator__ctor.htm) | Initializes a new instance of the GH\_CanvasWireValidator class |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Protected property | [Canvas](P_Grasshopper_GUI_Canvas_GH_CanvasValidator_Canvas.htm) | Gets the canvas this validator is associated with. (Inherited from [GH\_CanvasValidator](T_Grasshopper_GUI_Canvas_GH_CanvasValidator.htm).) |
| Protected property | [Document](P_Grasshopper_GUI_Canvas_GH_CanvasValidator_Document.htm) | Gets the document (if it exists) that is currently loaded in the canvas. (Inherited from [GH\_CanvasValidator](T_Grasshopper_GUI_Canvas_GH_CanvasValidator.htm).) |
| Public property | [WireDelegate](P_Grasshopper_GUI_Canvas_GH_CanvasWireValidator_WireDelegate.htm) | Gets or sets the delegate to be invoked when a wire is created. |
| Public property | [WireMotionText](P_Grasshopper_GUI_Canvas_GH_CanvasWireValidator_WireMotionText.htm) | Gets or sets the text to draw at the wire interior. |
| Public property | [WireSource](P_Grasshopper_GUI_Canvas_GH_CanvasWireValidator_WireSource.htm) | Gets or sets the wire source filter. |
| Public property | [WireSourceText](P_Grasshopper_GUI_Canvas_GH_CanvasWireValidator_WireSourceText.htm) | Gets or sets the text to draw at the wire source location. |
| Public property | [WireTarget](P_Grasshopper_GUI_Canvas_GH_CanvasWireValidator_WireTarget.htm) | Gets or sets the wire target filter. |
| Public property | [WireTargetText](P_Grasshopper_GUI_Canvas_GH_CanvasWireValidator_WireTargetText.htm) | Gets or sets the text to draw at the wire target location. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [AddedToCanvas](M_Grasshopper_GUI_Canvas_GH_CanvasWireValidator_AddedToCanvas.htm) | (Overrides [GH\_CanvasValidatorAddLanguageSpecificTextSet("LST477568EE\_3?cs=.|vb=.|cpp=::|nu=.|fs=.");AddedToCanvas(GH\_Canvas)](M_Grasshopper_GUI_Canvas_GH_CanvasValidator_AddedToCanvas.htm).) |
| Public method | [AppliesToDocument](M_Grasshopper_GUI_Canvas_GH_CanvasWireValidator_AppliesToDocument.htm) | (Overrides [GH\_CanvasValidatorAddLanguageSpecificTextSet("LST477568EE\_4?cs=.|vb=.|cpp=::|nu=.|fs=.");AppliesToDocument(Guid)](M_Grasshopper_GUI_Canvas_GH_CanvasValidator_AppliesToDocument.htm).) |
| Public method | [CanAcceptObject](M_Grasshopper_GUI_Canvas_GH_CanvasWireValidator_CanAcceptObject.htm) | (Overrides [GH\_CanvasValidatorAddLanguageSpecificTextSet("LST477568EE\_5?cs=.|vb=.|cpp=::|nu=.|fs=.");CanAcceptObject(Guid)](M_Grasshopper_GUI_Canvas_GH_CanvasValidator_CanAcceptObject.htm).) |
| Public method | [CanCreateObject](M_Grasshopper_GUI_Canvas_GH_CanvasWireValidator_CanCreateObject.htm) | (Overrides [GH\_CanvasValidatorAddLanguageSpecificTextSet("LST477568EE\_6?cs=.|vb=.|cpp=::|nu=.|fs=.");CanCreateObject(Guid, PointF)](M_Grasshopper_GUI_Canvas_GH_CanvasValidator_CanCreateObject.htm).) |
| Public method | [CanCreateWire](M_Grasshopper_GUI_Canvas_GH_CanvasWireValidator_CanCreateWire.htm) | (Overrides [GH\_CanvasValidatorAddLanguageSpecificTextSet("LST477568EE\_7?cs=.|vb=.|cpp=::|nu=.|fs=.");CanCreateWire(IGH\_Param, IGH\_Param)](M_Grasshopper_GUI_Canvas_GH_CanvasValidator_CanCreateWire.htm).) |
| Public method | [CanDeleteObject](M_Grasshopper_GUI_Canvas_GH_CanvasWireValidator_CanDeleteObject.htm) | (Overrides [GH\_CanvasValidatorAddLanguageSpecificTextSet("LST477568EE\_8?cs=.|vb=.|cpp=::|nu=.|fs=.");CanDeleteObject(IGH\_DocumentObject)](M_Grasshopper_GUI_Canvas_GH_CanvasValidator_CanDeleteObject.htm).) |
| Public method | [CanDeleteWire](M_Grasshopper_GUI_Canvas_GH_CanvasWireValidator_CanDeleteWire.htm) | (Overrides [GH\_CanvasValidatorAddLanguageSpecificTextSet("LST477568EE\_9?cs=.|vb=.|cpp=::|nu=.|fs=.");CanDeleteWire(IGH\_Param, IGH\_Param)](M_Grasshopper_GUI_Canvas_GH_CanvasValidator_CanDeleteWire.htm).) |
| Public method | [CanDragObject](M_Grasshopper_GUI_Canvas_GH_CanvasWireValidator_CanDragObject.htm) | (Overrides [GH\_CanvasValidatorAddLanguageSpecificTextSet("LST477568EE\_10?cs=.|vb=.|cpp=::|nu=.|fs=.");CanDragObject(IGH\_DocumentObject, PointF)](M_Grasshopper_GUI_Canvas_GH_CanvasValidator_CanDragObject.htm).) |
| Public method | [CanNavigateCanvas](M_Grasshopper_GUI_Canvas_GH_CanvasValidator_CanNavigateCanvas.htm) | (Inherited from [GH\_CanvasValidator](T_Grasshopper_GUI_Canvas_GH_CanvasValidator.htm).) |
| Public method | [CanShowCanvasMenu](M_Grasshopper_GUI_Canvas_GH_CanvasWireValidator_CanShowCanvasMenu.htm) | (Overrides [GH\_CanvasValidatorAddLanguageSpecificTextSet("LST477568EE\_11?cs=.|vb=.|cpp=::|nu=.|fs=.");CanShowCanvasMenu(PointF)](M_Grasshopper_GUI_Canvas_GH_CanvasValidator_CanShowCanvasMenu.htm).) |
| Public method | [CanShowComponentSearchBox](M_Grasshopper_GUI_Canvas_GH_CanvasWireValidator_CanShowComponentSearchBox.htm) | (Overrides [GH\_CanvasValidatorAddLanguageSpecificTextSet("LST477568EE\_12?cs=.|vb=.|cpp=::|nu=.|fs=.");CanShowComponentSearchBox(PointF)](M_Grasshopper_GUI_Canvas_GH_CanvasValidator_CanShowComponentSearchBox.htm).) |
| Public method | [CanShowObjectMenu](M_Grasshopper_GUI_Canvas_GH_CanvasValidator_CanShowObjectMenu.htm) | (Inherited from [GH\_CanvasValidator](T_Grasshopper_GUI_Canvas_GH_CanvasValidator.htm).) |
| Public method | [RemovedFromCanvas](M_Grasshopper_GUI_Canvas_GH_CanvasWireValidator_RemovedFromCanvas.htm) | (Overrides [GH\_CanvasValidatorAddLanguageSpecificTextSet("LST477568EE\_13?cs=.|vb=.|cpp=::|nu=.|fs=.");RemovedFromCanvas(GH\_Canvas)](M_Grasshopper_GUI_Canvas_GH_CanvasValidator_RemovedFromCanvas.htm).) |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI.Canvas Namespace](N_Grasshopper_GUI_Canvas.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)