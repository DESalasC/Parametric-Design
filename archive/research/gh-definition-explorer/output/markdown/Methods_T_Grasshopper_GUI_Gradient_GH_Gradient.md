# Methods_T_Grasshopper_GUI_Gradient_GH_Gradient

﻿ GH\_Gradient Methods

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm "Grasshopper API")

[Grasshopper.GUI.Gradient](../html/N_Grasshopper_GUI_Gradient.htm "Grasshopper.GUI.Gradient")

[GH\_Gradient Class](../html/T_Grasshopper_GUI_Gradient_GH_Gradient.htm "GH_Gradient Class")

[GH\_Gradient Methods](../html/Methods_T_Grasshopper_GUI_Gradient_GH_Gradient.htm "GH_Gradient Methods")

[AddGrip Method](../html/Overload_Grasshopper_GUI_Gradient_GH_Gradient_AddGrip.htm "AddGrip Method ")

[ColourAt Method](../html/M_Grasshopper_GUI_Gradient_GH_Gradient_ColourAt.htm "ColourAt Method ")

[DeleteGripRegion Method](../html/M_Grasshopper_GUI_Gradient_GH_Gradient_DeleteGripRegion.htm "DeleteGripRegion Method ")

[DisplayGradientEditor Method](../html/M_Grasshopper_GUI_Gradient_GH_Gradient_DisplayGradientEditor.htm "DisplayGradientEditor Method ")

[DisplayGripColourPicker Method](../html/M_Grasshopper_GUI_Gradient_GH_Gradient_DisplayGripColourPicker.htm "DisplayGripColourPicker Method ")

[EarthlyBrown Method](../html/M_Grasshopper_GUI_Gradient_GH_Gradient_EarthlyBrown.htm "EarthlyBrown Method ")

[Forest Method](../html/M_Grasshopper_GUI_Gradient_GH_Gradient_Forest.htm "Forest Method ")

[GreyScale Method](../html/M_Grasshopper_GUI_Gradient_GH_Gradient_GreyScale.htm "GreyScale Method ")

[Heat Method](../html/M_Grasshopper_GUI_Gradient_GH_Gradient_Heat.htm "Heat Method ")

[MouseDown Method](../html/M_Grasshopper_GUI_Gradient_GH_Gradient_MouseDown.htm "MouseDown Method ")

[MouseDragAbort Method](../html/M_Grasshopper_GUI_Gradient_GH_Gradient_MouseDragAbort.htm "MouseDragAbort Method ")

[MouseMove Method](../html/M_Grasshopper_GUI_Gradient_GH_Gradient_MouseMove.htm "MouseMove Method ")

[MouseUp Method](../html/M_Grasshopper_GUI_Gradient_GH_Gradient_MouseUp.htm "MouseUp Method ")

[NearestGrip Method](../html/Overload_Grasshopper_GUI_Gradient_GH_Gradient_NearestGrip.htm "NearestGrip Method ")

[NewGripRegion Method](../html/M_Grasshopper_GUI_Gradient_GH_Gradient_NewGripRegion.htm "NewGripRegion Method ")

[NormalizeGrips Method](../html/M_Grasshopper_GUI_Gradient_GH_Gradient_NormalizeGrips.htm "NormalizeGrips Method ")

[OnGradientChanged Method](../html/M_Grasshopper_GUI_Gradient_GH_Gradient_OnGradientChanged.htm "OnGradientChanged Method ")

[OnGradientChangedIntermediate Method](../html/M_Grasshopper_GUI_Gradient_GH_Gradient_OnGradientChangedIntermediate.htm "OnGradientChangedIntermediate Method ")

[OnSelectionChanged Method](../html/M_Grasshopper_GUI_Gradient_GH_Gradient_OnSelectionChanged.htm "OnSelectionChanged Method ")

[Read Method](../html/M_Grasshopper_GUI_Gradient_GH_Gradient_Read.htm "Read Method ")

[RemoveGrip Method](../html/Overload_Grasshopper_GUI_Gradient_GH_Gradient_RemoveGrip.htm "RemoveGrip Method ")

[Render\_Background Method](../html/M_Grasshopper_GUI_Gradient_GH_Gradient_Render_Background.htm "Render_Background Method ")

[Render\_Gradient Method](../html/M_Grasshopper_GUI_Gradient_GH_Gradient_Render_Gradient.htm "Render_Gradient Method ")

[Render\_Grips Method](../html/M_Grasshopper_GUI_Gradient_GH_Gradient_Render_Grips.htm "Render_Grips Method ")

[SoGay Method](../html/M_Grasshopper_GUI_Gradient_GH_Gradient_SoGay.htm "SoGay Method ")

[Spectrum Method](../html/M_Grasshopper_GUI_Gradient_GH_Gradient_Spectrum.htm "Spectrum Method ")

[Traffic Method](../html/M_Grasshopper_GUI_Gradient_GH_Gradient_Traffic.htm "Traffic Method ")

[Write Method](../html/M_Grasshopper_GUI_Gradient_GH_Gradient_Write.htm "Write Method ")

[Zebra Method](../html/M_Grasshopper_GUI_Gradient_GH_Gradient_Zebra.htm "Zebra Method ")

![Click or drag to resize](../icons/TocOpen.gif "Click or drag to resize")![Click or drag to resize](../icons/TocClose.gif "Click or drag to resize")

|  |
| --- |
| GH\_Gradient Methods |

The [GH\_Gradient](T_Grasshopper_GUI_Gradient_GH_Gradient.htm) type exposes the following members.

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

![](../icons/SectionExpanded.png)See Also

#### Reference

[GH\_Gradient Class](T_Grasshopper_GUI_Gradient_GH_Gradient.htm)

[Grasshopper.GUI.Gradient Namespace](N_Grasshopper_GUI_Gradient.htm)

Grasshopper for Rhino 8.33.26188.13000 (2026-07-07)  
Copyright © 2009-2026 Robert McNeel & Associates

[Report wishes and bugs at discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)