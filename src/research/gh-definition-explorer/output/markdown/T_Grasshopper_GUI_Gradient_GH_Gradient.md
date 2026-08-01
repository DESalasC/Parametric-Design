# T_Grasshopper_GUI_Gradient_GH_Gradient

﻿ GH\_Gradient Class

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI.Gradient](../html/N_Grasshopper_GUI_Gradient.htm "Grasshopper.GUI.Gradient")

[GH\_Gradient Class](../html/T_Grasshopper_GUI_Gradient_GH_Gradient.htm "GH_Gradient Class")

[GH\_Gradient Constructor](../html/Overload_Grasshopper_GUI_Gradient_GH_Gradient__ctor.htm "GH_Gradient Constructor ")

[GH\_Gradient Properties](../html/Properties_T_Grasshopper_GUI_Gradient_GH_Gradient.htm "GH_Gradient Properties")

[GH\_Gradient Methods](../html/Methods_T_Grasshopper_GUI_Gradient_GH_Gradient.htm "GH_Gradient Methods")

[GH\_Gradient Events](../html/Events_T_Grasshopper_GUI_Gradient_GH_Gradient.htm "GH_Gradient Events")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_Gradient Class |

Represents a colour gradient defined by a succession of grips.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemAddLanguageSpecificTextSet("LSTEE6AF387\_0?cs=.|vb=.|cpp=::|nu=.|fs=.");Object](https://docs.microsoft.com/dotnet/api/system.object)  
  Grasshopper.GUI.GradientAddLanguageSpecificTextSet("LSTEE6AF387\_1?cs=.|vb=.|cpp=::|nu=.|fs=.");GH\_Gradient

**Namespace:**
 [Grasshopper.GUI.Gradient](N_Grasshopper_GUI_Gradient.htm)  
**Assembly:**
 Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

[C#](#)

[VB](#)

[Copy](# "Copy")

```
public class GH_Gradient : GH_ISerializable, 
	IGradient
```

```
Public Class GH_Gradient
	Implements GH_ISerializable, IGradient
```

AddLanguageTabSet("ID1EBCA");

The GH\_Gradient type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

|  | Name | Description |
| --- | --- | --- |
| Public method | [GH\_GradientAddLanguageSpecificTextSet("LSTEE6AF387\_2?cs=()|vb=|cpp=()|nu=()|fs=()");](M_Grasshopper_GUI_Gradient_GH_Gradient__ctor.htm) | Initializes a new instance of the GH\_Gradient class |
| Public method | [GH\_Gradient(GH\_Gradient)](M_Grasshopper_GUI_Gradient_GH_Gradient__ctor_1.htm) | Create a duplicate of another gradient. |
| Public method | [GH\_Gradient(IEnumerableAddLanguageSpecificTextSet("LSTEE6AF387\_3?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");DoubleAddLanguageSpecificTextSet("LSTEE6AF387\_4?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");, IEnumerableAddLanguageSpecificTextSet("LSTEE6AF387\_5?cs=&lt;|vb=(Of |cpp=&lt;|fs=&lt;'|nu=(");ColorAddLanguageSpecificTextSet("LSTEE6AF387\_6?cs=&gt;|vb=)|cpp=&gt;|fs=&gt;|nu=)");)](M_Grasshopper_GUI_Gradient_GH_Gradient__ctor_2.htm) | Create a new gradient from grips and colours. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Properties

|  | Name | Description |
| --- | --- | --- |
| Public property | [Grip](P_Grasshopper_GUI_Gradient_GH_Gradient_Grip.htm) | Gets or sets the grip at the given index. |
| Public property | [GripCount](P_Grasshopper_GUI_Gradient_GH_Gradient_GripCount.htm) | Gets the number of grips in this gradient. |
| Public property | [Linear](P_Grasshopper_GUI_Gradient_GH_Gradient_Linear.htm) | Gets or sets whether the colours are interpolated linearly between grips. |
| Public property | [Locked](P_Grasshopper_GUI_Gradient_GH_Gradient_Locked.htm) | Gets or sets whether this gradient is locked. A locked gradient cannot be modified by the user. |
| Public property | [SelectedGrip](P_Grasshopper_GUI_Gradient_GH_Gradient_SelectedGrip.htm) | Gets or sets the selected grip. |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Methods

|  | Name | Description |
| --- | --- | --- |
| Public method | [AddGrip(Double)](M_Grasshopper_GUI_Gradient_GH_Gradient_AddGrip_1.htm) | Add a new grip to the gradient. The colour of the grip will be picked so that there is no difference to the gradient, though this is not actually possible when the interpolation mode is not linear. |
| Public method | [AddGrip(GH\_Grip)](M_Grasshopper_GUI_Gradient_GH_Gradient_AddGrip.htm) | Add a new grip to the gradient. This method does not raise the GradientChanged event, so you need to do that yourself by calling OnGradientChanged(). |
| Public method | [AddGrip(Double, Color)](M_Grasshopper_GUI_Gradient_GH_Gradient_AddGrip_2.htm) | Add a new single-colour grip. |
| Public method | [AddGrip(Double, Color, Color)](M_Grasshopper_GUI_Gradient_GH_Gradient_AddGrip_3.htm) | Add a new bi-colour grip. |
| Public method | [ColourAt](M_Grasshopper_GUI_Gradient_GH_Gradient_ColourAt.htm) | Evaluate the colour at a specific parameter. |
| Public methodStatic member | [DeleteGripRegion](M_Grasshopper_GUI_Gradient_GH_Gradient_DeleteGripRegion.htm) | Gets the Delete Grip region rectangle based on a gradient destination rectangle. |
| Public method | [DisplayGradientEditor](M_Grasshopper_GUI_Gradient_GH_Gradient_DisplayGradientEditor.htm) |  |
| Public method | [DisplayGripColourPicker](M_Grasshopper_GUI_Gradient_GH_Gradient_DisplayGripColourPicker.htm) |  |
| Public methodStatic member | [EarthlyBrown](M_Grasshopper_GUI_Gradient_GH_Gradient_EarthlyBrown.htm) |  |
| Public methodStatic member | [Forest](M_Grasshopper_GUI_Gradient_GH_Gradient_Forest.htm) |  |
| Public methodStatic member | [GreyScale](M_Grasshopper_GUI_Gradient_GH_Gradient_GreyScale.htm) |  |
| Public methodStatic member | [Heat](M_Grasshopper_GUI_Gradient_GH_Gradient_Heat.htm) |  |
| Public method | [MouseDown](M_Grasshopper_GUI_Gradient_GH_Gradient_MouseDown.htm) | Begin grip drag operation. |
| Public method | [MouseDragAbort](M_Grasshopper_GUI_Gradient_GH_Gradient_MouseDragAbort.htm) | Abort grip drag. |
| Public method | [MouseMove](M_Grasshopper_GUI_Gradient_GH_Gradient_MouseMove.htm) | Continue grip dragging operation. |
| Public method | [MouseUp](M_Grasshopper_GUI_Gradient_GH_Gradient_MouseUp.htm) | Terminate grip drag. |
| Public method | [NearestGrip(Double)](M_Grasshopper_GUI_Gradient_GH_Gradient_NearestGrip.htm) | Find the nearest grip to a parameter. |
| Public method | [NearestGrip(Double, GH\_GripSide)](M_Grasshopper_GUI_Gradient_GH_Gradient_NearestGrip_1.htm) | Find the nearest grip to a parameter. |
| Public method | [NearestGrip(RectangleF, PointF, Double)](M_Grasshopper_GUI_Gradient_GH_Gradient_NearestGrip_2.htm) | Find the nearest grip in screen coordinates. |
| Public methodStatic member | [NewGripRegion](M_Grasshopper_GUI_Gradient_GH_Gradient_NewGripRegion.htm) | Gets the new Grip region rectangle based on a gradient destination rectangle. |
| Public method | [NormalizeGrips](M_Grasshopper_GUI_Gradient_GH_Gradient_NormalizeGrips.htm) | Normalize all grips. This will scale all grip parameters so that the full gradient extend equals 0~1. |
| Public method | [OnGradientChanged](M_Grasshopper_GUI_Gradient_GH_Gradient_OnGradientChanged.htm) | Raise the GradientChanged event. |
| Public method | [OnGradientChangedIntermediate](M_Grasshopper_GUI_Gradient_GH_Gradient_OnGradientChangedIntermediate.htm) | Raise the GradientChanged event. |
| Public method | [OnSelectionChanged](M_Grasshopper_GUI_Gradient_GH_Gradient_OnSelectionChanged.htm) | Raise the SelectionChanged event. |
| Public method | [Read](M_Grasshopper_GUI_Gradient_GH_Gradient_Read.htm) |  |
| Public method | [RemoveGrip(GH\_Grip)](M_Grasshopper_GUI_Gradient_GH_Gradient_RemoveGrip.htm) | Remove the specified grip. |
| Public method | [RemoveGrip(Int32)](M_Grasshopper_GUI_Gradient_GH_Gradient_RemoveGrip_1.htm) | Remove the grip at the specified index. |
| Public method | [Render\_Background](M_Grasshopper_GUI_Gradient_GH_Gradient_Render_Background.htm) |  |
| Public method | [Render\_Gradient](M_Grasshopper_GUI_Gradient_GH_Gradient_Render_Gradient.htm) |  |
| Public method | [Render\_Grips](M_Grasshopper_GUI_Gradient_GH_Gradient_Render_Grips.htm) |  |
| Public methodStatic member | [SoGay](M_Grasshopper_GUI_Gradient_GH_Gradient_SoGay.htm) |  |
| Public methodStatic member | [Spectrum](M_Grasshopper_GUI_Gradient_GH_Gradient_Spectrum.htm) |  |
| Public methodStatic member | [Traffic](M_Grasshopper_GUI_Gradient_GH_Gradient_Traffic.htm) |  |
| Public method | [Write](M_Grasshopper_GUI_Gradient_GH_Gradient_Write.htm) |  |
| Public methodStatic member | [Zebra](M_Grasshopper_GUI_Gradient_GH_Gradient_Zebra.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)Events

|  | Name | Description |
| --- | --- | --- |
| Public event | [GradientChanged](E_Grasshopper_GUI_Gradient_GH_Gradient_GradientChanged.htm) |  |
| Public event | [SelectionChanged](E_Grasshopper_GUI_Gradient_GH_Gradient_SelectionChanged.htm) |  |

[Top](#PageHeader)

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.GUI.Gradient Namespace](N_Grasshopper_GUI_Gradient.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)